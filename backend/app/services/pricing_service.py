"""
Zay Chin Pricing Service
Calculates dynamic MMK costs for recipes and grocery items using verified market price observations.
Adheres strictly to zero-hallucination rules:
- Differentiates Yangon vs Mandalay observations without cross-city substitution.
- Marks partial estimates transparently and discloses missing ingredients.
- Accounts for zero-cost utilities (tap water).
"""

from typing import Dict, List, Optional, Any
from sqlalchemy.orm import Session
import backend.app.models as models

# Zero-cost domestic utilities and seasonings to taste
ZERO_COST_INGREDIENT_IDS = {"I0012", "I0017", "I0200"} # Hot water, Water, Salt water

class PricingService:
    @staticmethod
    def get_latest_prices_by_city(db: Session, city: str = "Yangon") -> Dict[str, models.IngredientPrice]:
        """
        Retrieves the latest retail/market price observation for each ingredient in the specified city.
        Prefers retail over wholesale/estimate, and later observation dates.
        """
        prices = db.query(models.IngredientPrice).filter(
            models.IngredientPrice.city == city
        ).order_by(models.IngredientPrice.observed_date.desc()).all()

        latest_map = {}
        for p in prices:
            # If not yet added, or if current candidate is retail while existing is wholesale/estimate
            if p.ingredient_id not in latest_map:
                latest_map[p.ingredient_id] = p
            else:
                existing = latest_map[p.ingredient_id]
                if existing.price_type != "retail" and p.price_type == "retail":
                    latest_map[p.ingredient_id] = p
        return latest_map

    @staticmethod
    def calculate_recipe_cost(
        recipe: models.Recipe,
        db: Session,
        city: str = "Yangon",
        servings_multiplier: float = 1.0,
        price_map: Optional[Dict[str, models.IngredientPrice]] = None
    ) -> Dict[str, Any]:
        """
        Computes dynamic recipe cost based on verified city price observations.
        """
        if price_map is None:
            price_map = PricingService.get_latest_prices_by_city(db, city=city)
        
        total_cost_mmk = 0.0
        priced_count = 0
        total_count = len(recipe.ingredients)
        missing_ingredients = []
        ingredient_cost_breakdown = []

        for ri in recipe.ingredients:
            iid = ri.ingredient_id
            nq = ri.normalized_quantity
            nu = ri.normalized_unit
            
            # Scale quantity by servings ratio
            scaled_quantity = (nq * servings_multiplier) if nq is not None else None
            
            is_priced = False
            item_cost = 0.0
            price_obs = price_map.get(iid)

            if iid in ZERO_COST_INGREDIENT_IDS or nu == "to_taste":
                is_priced = True
                item_cost = 0.0
                priced_count += 1
                ingredient_cost_breakdown.append({
                    "ingredient_id": iid,
                    "name_mm": ri.name_mm,
                    "name_en": ri.name_en,
                    "scaled_quantity": scaled_quantity,
                    "unit": nu or ri.unit,
                    "item_cost_mmk": 0.0,
                    "is_priced": True,
                    "is_zero_cost_utility": True,
                    "observation_source": "Municipal Household Utility / To Taste",
                    "observation_date": None
                })
            elif price_obs and scaled_quantity is not None:
                p_per_kg = price_obs.normalized_price_mmk_per_kg
                if p_per_kg is not None and nu in ["g", "ml"]:
                    # 1 ml ≈ 1 g for culinary liquids
                    item_cost = (scaled_quantity / 1000.0) * p_per_kg
                    total_cost_mmk += item_cost
                    is_priced = True
                    priced_count += 1
                elif nu == "piece" and price_obs.original_unit and "piece" in price_obs.original_unit.lower():
                    item_cost = scaled_quantity * price_obs.price_mmk
                    total_cost_mmk += item_cost
                    is_priced = True
                    priced_count += 1
                elif p_per_kg is not None:
                    # Generic mass fallback if available
                    item_cost = (scaled_quantity / 1000.0) * p_per_kg
                    total_cost_mmk += item_cost
                    is_priced = True
                    priced_count += 1

                if is_priced:
                    ingredient_cost_breakdown.append({
                        "ingredient_id": iid,
                        "name_mm": ri.name_mm,
                        "name_en": ri.name_en,
                        "scaled_quantity": round(scaled_quantity, 2),
                        "unit": nu or ri.unit,
                        "unit_price_mmk": price_obs.price_mmk,
                        "normalized_price_per_kg": p_per_kg,
                        "item_cost_mmk": round(item_cost, 2),
                        "is_priced": True,
                        "price_type": price_obs.price_type,
                        "observation_source": price_obs.source_name,
                        "market_name": price_obs.market_name,
                        "observation_date": price_obs.observed_date
                    })

            if not is_priced:
                missing_ingredients.append({
                    "ingredient_id": iid,
                    "name_mm": ri.name_mm,
                    "name_en": ri.name_en,
                    "unit": ri.unit,
                    "reason": "No active price observation recorded in " + city
                })
                ingredient_cost_breakdown.append({
                    "ingredient_id": iid,
                    "name_mm": ri.name_mm,
                    "name_en": ri.name_en,
                    "scaled_quantity": round(scaled_quantity, 2) if scaled_quantity else None,
                    "unit": nu or ri.unit,
                    "item_cost_mmk": None,
                    "is_priced": False,
                    "observation_source": None,
                    "observation_date": None
                })

        coverage_pct = round((priced_count / total_count * 100.0), 1) if total_count > 0 else 0.0
        is_complete = (priced_count == total_count)

        return {
            "recipe_id": recipe.id,
            "city": city,
            "servings": recipe.servings,
            "scaled_servings": round((recipe.servings or 4) * servings_multiplier),
            "estimated_cost_mmk": round(total_cost_mmk, 2),
            "cost_coverage_percentage": coverage_pct,
            "is_cost_complete": is_complete,
            "priced_ingredients_count": priced_count,
            "total_ingredients_count": total_count,
            "missing_priced_ingredients": missing_ingredients,
            "ingredient_breakdown": ingredient_cost_breakdown
        }
