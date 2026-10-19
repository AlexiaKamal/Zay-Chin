"""
Zay Chin Intelligent Meal Planning & Recommendation Service
Engineered specifically for Myanmar culinary culture, budget constraints, and household preferences.
"""

from typing import List, Dict, Any, Optional
import random
from sqlalchemy.orm import Session
import backend.app.models as models
from backend.app.services.pricing_service import PricingService
from backend.app.services.nutrition_service import NutritionService
from backend.app.schemas.planner_schemas import (
    MealPlanGenerateRequest,
    MealPlanGenerateResponse,
    MealSlotRecommendation,
    DailyNutritionSummary,
    MealReplacementRequest,
    MealReplacementResponse,
    ReplacementOption
)

DAYS_EN = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
DAYS_MM = ["တနင်္လာ", "အင်္ဂါ", "ဗုဒ္ဓဟူး", "ကြာသပတေး", "သောကြာ", "စနေ", "တနင်္ဂနွေ"]

# Recipe categories traditionally favored for breakfast in Myanmar
BREAKFAST_CATEGORIES = {"Rice dishes", "Noodles", "Noodles & Pastas", "Soups & Broths", "Snacks", "Salads"}

class PlannerService:
    @staticmethod
    def get_dietary_flags(recipe: models.Recipe) -> Dict[str, bool]:
        tags = recipe.tags if isinstance(recipe.tags, dict) else {}
        dietary_list = [d.lower() for d in tags.get("dietary", [])]
        return {
            "is_vegetarian": "vegetarian" in dietary_list,
            "is_vegan": "vegan" in dietary_list,
            "is_gluten_free": "gluten_free" in dietary_list or "gluten-free" in dietary_list,
            "is_convalescent": "convalescent" in dietary_list,
            "is_baby_food": "baby_food" in dietary_list
        }

    @classmethod
    def filter_eligible_recipes(
        cls,
        db: Session,
        dietary_preferences: List[str],
        disliked_ingredients: List[str]
    ) -> List[models.Recipe]:
        """
        Filters recipes strictly by dietary rules and ingredient exclusions.
        """
        recipes = db.query(models.Recipe).all()

        if dietary_preferences:
            pref_normalized = [p.lower().replace("-", "_") for p in dietary_preferences]
            filtered = []
            for r in recipes:
                flags = cls.get_dietary_flags(r)
                # Must satisfy all specified preferences
                match = True
                for p in pref_normalized:
                    flag_key = f"is_{p}"
                    if not flags.get(flag_key, False):
                        match = False
                        break
                if match:
                    filtered.append(r)
            recipes = filtered

        if not disliked_ingredients:
            return recipes

        # Filter out recipes containing disliked ingredients
        disliked_lower = {d.lower().strip() for d in disliked_ingredients}
        eligible = []
        for r in recipes:
            has_disliked = False
            for ri in r.ingredients:
                if (ri.ingredient_id.lower() in disliked_lower or
                    ri.name_en.lower() in disliked_lower or
                    ri.name_mm.lower() in disliked_lower):
                    has_disliked = True
                    break
            if not has_disliked:
                eligible.append(r)

        return eligible

    @classmethod
    def generate_plan(cls, db: Session, req: MealPlanGenerateRequest) -> MealPlanGenerateResponse:
        eligible_recipes = cls.filter_eligible_recipes(
            db,
            dietary_preferences=req.dietary_preferences,
            disliked_ingredients=req.disliked_ingredients
        )

        if not eligible_recipes:
            # Fallback to general recipes if dietary constraints are overly restrictive
            eligible_recipes = db.query(models.Recipe).all()

        # Categorize eligible recipes for balanced slot selection
        breakfast_pool = [r for r in eligible_recipes if r.category in BREAKFAST_CATEGORIES or "soup" in r.name_en.lower() or "rice" in r.name_en.lower()]
        if not breakfast_pool:
            breakfast_pool = eligible_recipes

        lunch_pool = [r for r in eligible_recipes if r.category not in {"Salads"} or len(eligible_recipes) < 10]
        if not lunch_pool:
            lunch_pool = eligible_recipes

        dinner_pool = eligible_recipes

        schedule: List[MealSlotRecommendation] = []
        daily_summaries: List[DailyNutritionSummary] = []
        used_recipe_ids = set()
        
        total_plan_cost = 0.0
        total_calories_accum = 0.0
        total_protein_accum = 0.0

        meals_per_day = req.meals_per_day
        meal_types = ["breakfast", "lunch", "dinner"] if meals_per_day == 3 else ["lunch", "dinner"]

        for day_idx in range(req.plan_duration_days):
            day_num = day_idx + 1
            day_en = DAYS_EN[day_idx % 7]
            day_mm = DAYS_MM[day_idx % 7]

            day_cost = 0.0
            day_calories = 0.0
            day_protein = 0.0
            day_carbs = 0.0
            day_fat = 0.0
            day_sodium = 0.0

            for m_type in meal_types:
                # Pick pool
                if m_type == "breakfast":
                    pool = breakfast_pool
                elif m_type == "lunch":
                    pool = lunch_pool
                else:
                    pool = dinner_pool

                # Select an unused recipe if possible
                candidates = [r for r in pool if r.id not in used_recipe_ids]
                if not candidates:
                    candidates = pool

                # Preference boost for preferred categories
                if req.preferred_categories:
                    preferred_candidates = [c for c in candidates if c.category in req.preferred_categories]
                    if preferred_candidates:
                        candidates = preferred_candidates

                selected_recipe: models.Recipe = random.choice(candidates)
                used_recipe_ids.add(selected_recipe.id)

                # Servings multiplier for household
                servings_mult = req.household_size / (selected_recipe.servings or 4)

                # Cost & Nutrition calculations
                cost_info = PricingService.calculate_recipe_cost(
                    selected_recipe, db, city=req.city, servings_multiplier=servings_mult
                )
                nutr_info = NutritionService.calculate_recipe_nutrition(selected_recipe, db)

                slot_cost = cost_info.get("estimated_cost_mmk", 0.0)
                per_serving = nutr_info.get("per_serving", {})
                cal = per_serving.get("calories_kcal", 0.0)
                prot = per_serving.get("protein_g", 0.0)
                carb = per_serving.get("carbohydrates_g", 0.0)
                fat = per_serving.get("fat_g", 0.0)
                sod = per_serving.get("sodium_mg", 0.0)

                day_cost += slot_cost
                day_calories += cal
                day_protein += prot
                day_carbs += carb
                day_fat += fat
                day_sodium += sod

                flags = cls.get_dietary_flags(selected_recipe)

                schedule.append(
                    MealSlotRecommendation(
                        day_of_week=day_num,
                        day_name_en=day_en,
                        day_name_mm=day_mm,
                        meal_type=m_type,
                        recipe_id=selected_recipe.id,
                        recipe_name_en=selected_recipe.name_en,
                        recipe_name_mm=selected_recipe.name_mm,
                        category=selected_recipe.category or "Traditional",
                        servings=req.household_size,
                        cook_time_minutes=selected_recipe.cooking_time_minutes,
                        estimated_cost_mmk=round(slot_cost, 2),
                        calories_kcal=round(cal, 1),
                        protein_g=round(prot, 1),
                        is_vegetarian=flags["is_vegetarian"],
                        is_vegan=flags["is_vegan"],
                        is_gluten_free=flags["is_gluten_free"]
                    )
                )

            total_plan_cost += day_cost
            total_calories_accum += day_calories
            total_protein_accum += day_protein

            daily_summaries.append(
                DailyNutritionSummary(
                    day_of_week=day_num,
                    total_calories_kcal=round(day_calories, 1),
                    total_protein_g=round(day_protein, 1),
                    total_carbs_g=round(day_carbs, 1),
                    total_fat_g=round(day_fat, 1),
                    total_sodium_mg=round(day_sodium, 1),
                    total_cost_mmk=round(day_cost, 2)
                )
            )

        # Budget analysis
        is_exceeded = False
        variance = None
        msg_en = "Plan meets estimated budgetary guidelines."
        msg_mm = "အပတ်စဉ် အစားအစာ စီစဉ်မှုသည် ခန့်မှန်းဘတ်ဂျက်နှင့် ကိုက်ညီပါသည်။"

        if req.weekly_budget_mmk is not None:
            variance = req.weekly_budget_mmk - total_plan_cost
            if variance < 0:
                is_exceeded = True
                msg_en = f"Estimated cost exceeds budget by {abs(round(variance, 0)):,} MMK. Consider substituting premium proteins with egg, dhal, or seasonal vegetable curries."
                msg_mm = f"ခန့်မှန်းကုန်ကျစရိတ်သည် သတ်မှတ်ဘတ်ဂျက်ထက် {abs(round(variance, 0)):,} ကျပ် ပိုလွန်နေပါသည်။ ဥ၊ ပဲ သို့မဟုတ် ရာသီပေါ်ဟင်းသီးဟင်းရွက်များဖြင့် အစားထိုးစီစဉ်နိုင်ပါသည်။"

        days_count = req.plan_duration_days
        avg_cal = round(total_calories_accum / days_count, 1) if days_count else 0.0
        avg_prot = round(total_protein_accum / days_count, 1) if days_count else 0.0

        return MealPlanGenerateResponse(
            plan_name=f"{req.household_size}-Person Weekly Plan ({req.city})",
            city=req.city,
            household_size=req.household_size,
            target_budget_mmk=req.weekly_budget_mmk,
            estimated_total_cost_mmk=round(total_plan_cost, 2),
            is_budget_exceeded=is_exceeded,
            budget_variance_mmk=round(variance, 2) if variance is not None else None,
            budget_status_message_en=msg_en,
            budget_status_message_mm=msg_mm,
            days_count=days_count,
            schedule=schedule,
            daily_summaries=daily_summaries,
            average_daily_calories_per_person=avg_cal,
            average_daily_protein_per_person=avg_prot
        )

    @classmethod
    def get_replacement_options(cls, db: Session, req: MealReplacementRequest) -> MealReplacementResponse:
        """
        Finds suitable replacement recipes for a specific slot with price difference comparison.
        """
        current_recipe = db.query(models.Recipe).filter_by(id=req.current_recipe_id).first()
        current_cost = 0.0
        if current_recipe:
            current_mult = req.household_size / (current_recipe.servings or 4)
            current_cost = PricingService.calculate_recipe_cost(
                current_recipe, db, city=req.city, servings_multiplier=current_mult
            ).get("estimated_cost_mmk", 0.0)

        eligible = cls.filter_eligible_recipes(
            db,
            dietary_preferences=req.dietary_preferences,
            disliked_ingredients=req.disliked_ingredients
        )

        # Exclude the current recipe itself
        eligible = [r for r in eligible if r.id != req.current_recipe_id]

        if req.preferred_category:
            cat_matches = [r for r in eligible if r.category == req.preferred_category]
            if cat_matches:
                eligible = cat_matches

        # Pick top 6 varied candidates
        sample_candidates = eligible[:8] if len(eligible) <= 8 else random.sample(eligible, 8)
        
        replacement_options = []
        for r in sample_candidates:
            mult = req.household_size / (r.servings or 4)
            cost_info = PricingService.calculate_recipe_cost(
                r, db, city=req.city, servings_multiplier=mult
            )
            cand_cost = cost_info.get("estimated_cost_mmk", 0.0)
            diff = cand_cost - current_cost

            nutr = NutritionService.calculate_recipe_nutrition(r, db)
            ps = nutr.get("per_serving", {})
            flags = cls.get_dietary_flags(r)

            replacement_options.append(
                ReplacementOption(
                    recipe_id=r.id,
                    name_en=r.name_en,
                    name_mm=r.name_mm,
                    category=r.category or "Traditional",
                    estimated_cost_mmk=round(cand_cost, 2),
                    cost_difference_mmk=round(diff, 2),
                    calories_kcal=ps.get("calories_kcal", 0.0),
                    protein_g=ps.get("protein_g", 0.0),
                    is_vegetarian=flags["is_vegetarian"],
                    is_vegan=flags["is_vegan"],
                    is_gluten_free=flags["is_gluten_free"]
                )
            )

        # Sort candidates by closest cost match
        replacement_options.sort(key=lambda x: abs(x.cost_difference_mmk))

        return MealReplacementResponse(
            current_recipe_id=req.current_recipe_id,
            candidates=replacement_options[:6]
        )
