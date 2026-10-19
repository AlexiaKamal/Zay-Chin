"""
Zay Chin Nutrition Service
Calculates approximate nutritional values per serving from laboratory food composition tables.
Adheres strictly to zero-hallucination guidelines:
- Standardized to 100g edible portion basis.
- Clearly states calculation basis and distinguishes complete vs approximate values.
"""

from typing import Dict, Any
from sqlalchemy.orm import Session
import backend.app.models as models

# Approximate reference weights for common discrete units (g) for Myanmar ingredients
APPROX_DISCRETE_WEIGHTS_G = {
    "I0010": 50.0,  # Chicken egg (~50g)
    "I0026": 50.0,  # Chicken egg (~50g)
    "I0027": 70.0,  # Duck egg (~70g)
    "I0006": 40.0,  # Onion small (~40g)
    "I0007": 3.0,   # Garlic clove (~3g)
    "I0041": 45.0,  # Lime (~45g)
    "I0008": 0.1,   # Clove (~0.1g)
    "I0009": 0.4,   # Cardamom pod (~0.4g)
}

class NutritionService:
    @staticmethod
    def calculate_recipe_nutrition(recipe: models.Recipe, db: Session) -> Dict[str, Any]:
        """
        Calculates total and per-serving nutritional metrics for a recipe.
        """
        servings = recipe.servings or 4
        
        total_energy_kcal = 0.0
        total_protein_g = 0.0
        total_fat_g = 0.0
        total_carbs_g = 0.0
        total_fiber_g = 0.0
        total_sodium_mg = 0.0
        
        weighted_count = 0
        total_count = len(recipe.ingredients)
        unweighted_ingredients = []

        for ri in recipe.ingredients:
            nu = ri.normalized_unit
            nq = ri.normalized_quantity
            iid = ri.ingredient_id
            
            # Fetch lab nutrition profile
            nutr = ri.ingredient.nutrition if ri.ingredient else None
            if not nutr:
                nutr = db.query(models.IngredientNutrition).filter_by(ingredient_id=iid).first()
                
            if not nutr:
                unweighted_ingredients.append(ri.name_en)
                continue

            grams = None
            if nu in ["g", "ml"] and nq is not None:
                grams = nq # 1 ml ≈ 1 g for culinary broth/water/sauces
            elif nu == "piece" and nq is not None and iid in APPROX_DISCRETE_WEIGHTS_G:
                grams = nq * APPROX_DISCRETE_WEIGHTS_G[iid]
            elif nu == "to_taste":
                # Trace seasoning amounts contribute negligible calories
                weighted_count += 1
                continue

            if grams is not None and grams > 0:
                weighted_count += 1
                ratio = grams / 100.0 # Per 100g basis
                total_energy_kcal += (nutr.energy_kcal or 0.0) * ratio
                total_protein_g += (nutr.protein_g or 0.0) * ratio
                total_fat_g += (nutr.total_fat_g or 0.0) * ratio
                total_carbs_g += (nutr.carbohydrates_g or 0.0) * ratio
                total_fiber_g += (nutr.fiber_g or 0.0) * ratio
                total_sodium_mg += (nutr.sodium_mg or 0.0) * ratio
            else:
                unweighted_ingredients.append(ri.name_en)

        is_complete = (weighted_count == total_count)
        
        return {
            "recipe_id": recipe.id,
            "servings": servings,
            "is_nutrition_complete": is_complete,
            "weighted_ingredients_ratio": f"{weighted_count}/{total_count}",
            "unweighted_ingredients": unweighted_ingredients,
            "per_serving": {
                "calories_kcal": round(total_energy_kcal / servings, 1) if servings else 0.0,
                "protein_g": round(total_protein_g / servings, 1) if servings else 0.0,
                "fat_g": round(total_fat_g / servings, 1) if servings else 0.0,
                "carbohydrates_g": round(total_carbs_g / servings, 1) if servings else 0.0,
                "fiber_g": round(total_fiber_g / servings, 1) if servings else 0.0,
                "sodium_mg": round(total_sodium_mg / servings, 1) if servings else 0.0,
            },
            "recipe_total": {
                "calories_kcal": round(total_energy_kcal, 1),
                "protein_g": round(total_protein_g, 1),
                "fat_g": round(total_fat_g, 1),
                "carbohydrates_g": round(total_carbs_g, 1),
                "fiber_g": round(total_fiber_g, 1),
                "sodium_mg": round(total_sodium_mg, 1),
            },
            "disclaimer": "Approximate nutritional values calculated from USDA FoodData Central and Thai Food Composition Database. Not clinical medical advice."
        }
