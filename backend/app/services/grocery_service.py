"""
Zay Chin Grocery Aggregation & Shopping List Service
Aggregates ingredients across recipe selections and meal plans with unit normalization,
verified MMK pricing by city, shopping aisle categorization, and realistic retail packaging calculations.
"""

from typing import List, Dict, Any, Optional
import math
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

# Common Myanmar household pantry staples
PANTRY_STAPLE_IDS = {
    "I0003", # Cooking oil
    "I0004", # Salt
    "I0005", # Sugar
    "I0012", # Hot water
    "I0017", # Water
    "I0038", # Chili powder
    "I0039", # Turmeric powder
    "I0040", # Seasoning powder
    "I0054", # Soy sauce light
    "I0055", # Fish sauce
    "I0062", # Soy sauce dark
    "I0067", # Sesame oil
    "I0200", # Salt water
}

# Standard packaged grocery sizing rules
KNOWN_PACK_SIZES = {
    "I0004": {"pack_grams": 400.0, "unit_en": "pack (400g)", "unit_mm": "ထုပ် (၄၀၀ ဂရမ်)", "default_price": 1200.0},
    "I0005": {"pack_grams": 1000.0, "unit_en": "pack (1kg)", "unit_mm": "ထုပ် (၁ ကီလို)", "default_price": 4500.0},
    "I0003": {"pack_grams": 816.5, "unit_en": "bottle (0.5 Viss)", "unit_mm": "ပုလင်း (၅၀ ကျပ်သား)", "default_price": 8000.0},
    "I0055": {"pack_grams": 700.0, "unit_en": "bottle (700ml)", "unit_mm": "ပုလင်း (၇၀၀ မီလီလီတာ)", "default_price": 2200.0},
    "I0054": {"pack_grams": 500.0, "unit_en": "bottle (500ml)", "unit_mm": "ပုလင်း (၅၀၀ မီလီလီတာ)", "default_price": 2500.0},
    "I0062": {"pack_grams": 500.0, "unit_en": "bottle (500ml)", "unit_mm": "ပုလင်း (၅၀၀ မီလီလီတာ)", "default_price": 2500.0},
    "I0038": {"pack_grams": 100.0, "unit_en": "packet (100g)", "unit_mm": "ထုပ် (၁၀၀ ဂရမ်)", "default_price": 1500.0},
    "I0039": {"pack_grams": 50.0, "unit_en": "packet (50g)", "unit_mm": "ထုပ် (၅၀ ဂရမ်)", "default_price": 800.0},
    "I0040": {"pack_grams": 100.0, "unit_en": "packet (100g)", "unit_mm": "ထုပ် (၁၀၀ ဂရမ်)", "default_price": 1200.0},
    "I0067": {"pack_grams": 250.0, "unit_en": "bottle (250ml)", "unit_mm": "ပုလင်း (၂၅၀ မီလီလီတာ)", "default_price": 4500.0},
    "I0001": {"pack_grams": 2128.0, "unit_en": "Pyi (2.128 kg)", "unit_mm": "ပြည် (၂.၁၂၈ ကီလို)", "default_price": 4800.0},
    "I0002": {"pack_grams": 227.0, "unit_en": "block (227g)", "unit_mm": "တုံး (၂၂၇ ဂရမ်)", "default_price": 11500.0},
}

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

        # Compute prices, retail packaging, and format items
        groups_dict = defaultdict(list)
        total_estimated_portion_mmk = 0.0
        total_retail_pack_mmk = 0.0
        total_pantry_adjusted_mmk = 0.0
        pantry_items_count = 0
        priced_count = 0
        total_items = len(aggregated)

        for iid, data in aggregated.items():
            qty = data["total_quantity"]
            unit = data["unit"]
            price_obs = price_map.get(iid)
            
            is_zero_cost = iid in ZERO_COST_INGREDIENT_IDS or unit == "to_taste"
            is_staple = iid in PANTRY_STAPLE_IDS
            if is_staple:
                pantry_items_count += 1

            portion_cost = None
            retail_pack_price = None
            purchasable_qty = 1.0
            purchasable_unit_en = unit
            purchasable_unit_mm = unit
            package_desc_en = f"{data['name_en']} (Retail Unit)"
            package_desc_mm = f"{data['name_mm']} (လက်လီအရွယ်အစား)"

            is_available = False
            obs_source = None
            obs_date = None

            if is_zero_cost:
                portion_cost = 0.0
                retail_pack_price = 0.0
                purchasable_qty = 0.0
                purchasable_unit_en = "Domestic Utility"
                purchasable_unit_mm = "အိမ်သုံးရေ"
                package_desc_en = "Domestic Utility / To Taste"
                package_desc_mm = "အိမ်သုံး / အရသာအတွက်"
                is_available = True
                obs_source = "Domestic Utility / To Taste"
                priced_count += 1
            elif price_obs:
                p_per_kg = price_obs.normalized_price_mmk_per_kg
                is_count = unit == "piece" or "piece" in (price_obs.original_unit or "").lower()

                # 1. Prorated Portion Cost
                if p_per_kg is not None and unit in ["g", "ml"]:
                    portion_cost = (qty / 1000.0) * p_per_kg
                    is_available = True
                    priced_count += 1
                elif is_count:
                    portion_cost = qty * price_obs.price_mmk
                    is_available = True
                    priced_count += 1
                elif p_per_kg is not None:
                    portion_cost = (qty / 1000.0) * p_per_kg
                    is_available = True
                    priced_count += 1

                # 2. Purchasable Retail Packaging Calculation
                if is_count:
                    # Discrete produce (e.g. 0.6 cucumber -> 1 whole cucumber)
                    purchasable_qty = float(max(1, math.ceil(qty)))
                    retail_pack_price = purchasable_qty * price_obs.price_mmk
                    purchasable_unit_en = f"{int(purchasable_qty)} whole pieces" if purchasable_qty > 1 else "1 whole piece"
                    purchasable_unit_mm = f"{int(purchasable_qty)} လုံး အပြည့်"
                    package_desc_en = f"Whole Fresh {data['name_en']}"
                    package_desc_mm = f"လတ်ဆတ်သော {data['name_mm']}"
                elif iid in KNOWN_PACK_SIZES:
                    # Standard packaged grocery (e.g. 400g salt, 1kg sugar, 0.5 viss oil)
                    rule = KNOWN_PACK_SIZES[iid]
                    packs = max(1, math.ceil(qty / rule["pack_grams"]))
                    purchasable_qty = float(packs)
                    pack_cost = price_obs.price_mmk if price_obs.price_mmk else rule["default_price"]
                    retail_pack_price = packs * pack_cost
                    purchasable_unit_en = f"{packs} {rule['unit_en']}"
                    purchasable_unit_mm = f"{packs} {rule['unit_mm']}"
                    package_desc_en = f"{data['name_en']} Retail Pack (x{packs})"
                    package_desc_mm = f"{data['name_mm']} လက်လီထုပ် ({packs} ထုပ်)"
                elif unit in ["g", "ml"]:
                    # Bulk wet market produce / meat (clean portions)
                    min_grams = 200.0 if is_staple else 150.0
                    clean_grams = max(min_grams, float(math.ceil(qty / 50.0) * 50))
                    purchasable_qty = clean_grams
                    purchasable_unit_en = f"{int(clean_grams)}g portion"
                    purchasable_unit_mm = f"{int(clean_grams)} ဂရမ်"
                    package_desc_en = f"Fresh {data['name_en']} ({int(clean_grams)}g)"
                    package_desc_mm = f"လတ်ဆတ်သော {data['name_mm']}"
                    if p_per_kg:
                        retail_pack_price = (clean_grams / 1000.0) * p_per_kg
                    else:
                        retail_pack_price = portion_cost
                else:
                    purchasable_qty = float(max(1, math.ceil(qty)))
                    retail_pack_price = portion_cost

                if is_available and portion_cost is not None:
                    total_estimated_portion_mmk += portion_cost
                    total_retail_pack_mmk += (retail_pack_price or portion_cost)
                    if not is_staple:
                        total_pantry_adjusted_mmk += (retail_pack_price or portion_cost)
                    obs_source = f"{price_obs.source_name} ({price_obs.market_name})"
                    obs_date = price_obs.observed_date
            else:
                purchasable_qty = float(max(1, math.ceil(qty)))
                purchasable_unit_en = f"{int(purchasable_qty)} {unit}"
                purchasable_unit_mm = f"{int(purchasable_qty)} {unit}"

            item_schema = GroceryItemSchema(
                ingredient_id=iid,
                name_en=data["name_en"],
                name_mm=data["name_mm"],
                category=data["category"],
                total_quantity=round(qty, 1) if qty >= 10 else round(qty, 2),
                unit=unit,
                purchasable_quantity=purchasable_qty,
                purchasable_unit_en=purchasable_unit_en,
                purchasable_unit_mm=purchasable_unit_mm,
                package_description_en=package_desc_en,
                package_description_mm=package_desc_mm,
                estimated_price_mmk=round(portion_cost, 0) if portion_cost is not None else None,
                retail_package_price_mmk=round(retail_pack_price, 0) if retail_pack_price is not None else None,
                is_pantry_staple=is_staple,
                in_pantry=is_staple,
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
                items.sort(key=lambda x: x.name_en)
                subtotal = sum(i.retail_package_price_mmk or i.estimated_price_mmk or 0.0 for i in items)
                category_groups.append(
                    GroceryCategoryGroup(
                        category_id=cat_id,
                        category_name_en=meta["name_en"],
                        category_name_mm=meta["name_mm"],
                        subtotal_mmk=round(subtotal, 0),
                        items=items
                    )
                )

        coverage_pct = round((priced_count / total_items * 100.0), 1) if total_items > 0 else 0.0

        return GroceryListResponse(
            city=req.city,
            household_size=req.household_size,
            total_items_count=total_items,
            purchased_items_count=0,
            estimated_total_mmk=round(total_estimated_portion_mmk, 0),
            retail_total_mmk=round(total_retail_pack_mmk, 0),
            pantry_adjusted_total_mmk=round(total_pantry_adjusted_mmk, 0),
            pantry_items_count=pantry_items_count,
            coverage_percentage=coverage_pct,
            groups=category_groups,
            unpriced_items_count=total_items - priced_count
        )
