"""
Zay Chin Grocery Aggregation & Shopping List Service
Aggregates ingredients across recipe selections and meal plans with unit normalization,
verified MMK pricing by city, and shopping aisle categorization.
"""

from typing import List, Dict, Any, Optional
from collections import defaultdict
from sqlalchemy.orm import Session
import backend.app.models as models
from backend.app.services.pricing_service import PricingService, ZERO_COST_INGREDIENT_IDS
from backend.app.schemas.grocery_schemas import (
    GroceryListGenerateRequest,
    GroceryListResponse,
    GroceryCategoryGroup,
    GroceryItemSchema
)

# Myanmar shopping aisle taxonomy mappings
CATEGORY_METADATA = {
    "produce": {
        "name_en": "Fresh Produce & Aromatics",
        "name_mm": "လတ်ဆတ်သော ဟင်းသီးဟင်းရွက်နှင့် အမွှေးအကြိုင်များ",
        "order": 1
    },
    "meat_seafood": {
        "name_en": "Meat, Poultry, Seafood & Eggs",
        "name_mm": "အသား၊ ငါး၊ ပုစွန်နှင့် ဥအမျိုးမျိုး",
        "order": 2
    },
    "pantry_staples": {
        "name_en": "Pantry, Rice, Oils & Pulses",
        "name_mm": "ဆန်၊ ဆီ၊ ပဲနှင့် မီးဖိုချောင်သုံး အခြောက်အခြမ်းများ",
        "order": 3
    },
    "condiments": {
        "name_en": "Traditional Seasonings & Pastes",
        "name_mm": "ငါးပိ၊ ငါးငံပြာရည်နှင့် ရိုးရာအချဉ်အရသာများ",
        "order": 4
    },
    "other": {
        "name_en": "Other Ingredients",
        "name_mm": "အခြား ပါဝင်ပစ္စည်းများ",
        "order": 5
    }
}

class GroceryService:
    @staticmethod
    def infer_aisle(ri: models.RecipeIngredient) -> str:
        cat = (ri.ingredient.category or "").lower() if ri.ingredient else ""
        name = (ri.name_en or "").lower()

        if any(w in name or w in cat for w in ["chicken", "pork", "beef", "mutton", "fish", "prawn", "egg", "shrimp", "squid", "crab", "duck"]):
            return "meat_seafood"
        if any(w in name or w in cat for w in ["onion", "garlic", "ginger", "chilli", "chili", "tomato", "coriander", "lime", "lemon", "potato", "cabbage", "leaves", "roselle", "gourd", "eggplant", "mushroom"]):
            return "produce"
        if any(w in name or w in cat for w in ["oil", "rice", "flour", "besan", "gram", "lentil", "pulse", "bean", "pea", "sugar", "sesame", "peanut"]):
            return "pantry_staples"
        if any(w in name or w in cat for w in ["fish sauce", "shrimp paste", "ngapi", "tamarind", "turmeric", "salt", "vinegar", "msg", "curry powder"]):
            return "condiments"
        
        return "produce"

    @classmethod
    def generate_grocery_list(cls, db: Session, req: GroceryListGenerateRequest) -> GroceryListResponse:
        recipes = db.query(models.Recipe).filter(models.Recipe.id.in_(req.recipe_ids)).all()
        recipe_map = {r.id: r for r in recipes}

        price_map = PricingService.get_latest_prices_by_city(db, city=req.city)

        # Aggregate quantities by (ingredient_id, normalized_unit)
        aggregated: Dict[str, Dict[str, Any]] = {}

        for r_id in req.recipe_ids:
            recipe = recipe_map.get(r_id)
            if not recipe:
                continue

            multiplier = req.household_size / (recipe.servings or 4)

            for ri in recipe.ingredients:
                iid = ri.ingredient_id
                nu = ri.normalized_unit or ri.unit or "item"
                nq = (ri.normalized_quantity or 1.0) * multiplier

                if iid not in aggregated:
                    aisle = cls.infer_aisle(ri)
                    aggregated[iid] = {
                        "ingredient_id": iid,
                        "name_en": ri.name_en,
                        "name_mm": ri.name_mm,
                        "category": aisle,
                        "unit": nu,
                        "total_quantity": 0.0,
                        "ri_ref": ri
                    }
                
                # Sum quantity
                aggregated[iid]["total_quantity"] += nq

        # Compute prices and format items
        groups_dict = defaultdict(list)
        total_estimated_mmk = 0.0
        priced_count = 0
        total_items = len(aggregated)

        for iid, data in aggregated.items():
            qty = data["total_quantity"]
            unit = data["unit"]
            price_obs = price_map.get(iid)
            
            is_zero_cost = iid in ZERO_COST_INGREDIENT_IDS or unit == "to_taste"
            item_cost = None
            is_available = False
            obs_source = None
            obs_date = None

            if is_zero_cost:
                item_cost = 0.0
                is_available = True
                obs_source = "Domestic Utility / To Taste"
                priced_count += 1
            elif price_obs:
                p_per_kg = price_obs.normalized_price_mmk_per_kg
                if p_per_kg is not None and unit in ["g", "ml"]:
                    item_cost = (qty / 1000.0) * p_per_kg
                    is_available = True
                    priced_count += 1
                elif unit == "piece" and price_obs.original_unit and "piece" in price_obs.original_unit.lower():
                    item_cost = qty * price_obs.price_mmk
                    is_available = True
                    priced_count += 1
                elif p_per_kg is not None:
                    item_cost = (qty / 1000.0) * p_per_kg
                    is_available = True
                    priced_count += 1

                if is_available and item_cost is not None:
                    total_estimated_mmk += item_cost
                    obs_source = f"{price_obs.source_name} ({price_obs.market_name})"
                    obs_date = price_obs.observed_date

            item_schema = GroceryItemSchema(
                ingredient_id=iid,
                name_en=data["name_en"],
                name_mm=data["name_mm"],
                category=data["category"],
                total_quantity=round(qty, 1) if qty >= 10 else round(qty, 2),
                unit=unit,
                estimated_price_mmk=round(item_cost, 2) if item_cost is not None else None,
                is_price_available=is_available,
                is_zero_cost_utility=is_zero_cost,
                observation_source=obs_source,
                observation_date=obs_date,
                is_purchased=False
            )

            groups_dict[data["category"]].append(item_schema)

        # Assemble category groups
        category_groups: List[GroceryCategoryGroup] = []
        for cat_id, meta in sorted(CATEGORY_METADATA.items(), key=lambda x: x[1]["order"]):
            if cat_id in groups_dict and groups_dict[cat_id]:
                items = groups_dict[cat_id]
                # Sort items alphabetically by name
                items.sort(key=lambda x: x.name_en)
                subtotal = sum(i.estimated_price_mmk or 0.0 for i in items)
                category_groups.append(
                    GroceryCategoryGroup(
                        category_id=cat_id,
                        category_name_en=meta["name_en"],
                        category_name_mm=meta["name_mm"],
                        subtotal_mmk=round(subtotal, 2),
                        items=items
                    )
                )

        coverage_pct = round((priced_count / total_items * 100.0), 1) if total_items > 0 else 0.0

        return GroceryListResponse(
            city=req.city,
            household_size=req.household_size,
            total_items_count=total_items,
            purchased_items_count=0,
            estimated_total_mmk=round(total_estimated_mmk, 2),
            coverage_percentage=coverage_pct,
            groups=category_groups,
            unpriced_items_count=total_items - priced_count
        )
