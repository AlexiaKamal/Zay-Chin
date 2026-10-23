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

        # Cache city prices once to avoid repeated DB queries across recipes
        price_map = PricingService.get_latest_prices_by_city(db, city=req.city)

        # Precompute cost, nutrition, and dietary flags for all eligible recipes
        candidate_items = []
        for r in eligible_recipes:
            servings_mult = req.household_size / (r.servings or 4)
            cost_info = PricingService.calculate_recipe_cost(
                r, db, city=req.city, servings_multiplier=servings_mult, price_map=price_map
            )
            nutr_info = NutritionService.calculate_recipe_nutrition(r, db)
            ps = nutr_info.get("per_serving", {})
            flags = cls.get_dietary_flags(r)

            candidate_items.append({
                "recipe": r,
                "slot_cost": cost_info.get("estimated_cost_mmk", 0.0),
                "calories": ps.get("calories_kcal", 0.0),
                "protein": ps.get("protein_g", 0.0),
                "carbs": ps.get("carbohydrates_g", 0.0),
                "fat": ps.get("fat_g", 0.0),
                "sodium": ps.get("sodium_mg", 0.0),
                "flags": flags,
            })

        # Categorize eligible recipes for balanced slot selection
        breakfast_pool = [
            c for c in candidate_items
            if c["recipe"].category in BREAKFAST_CATEGORIES or
            "soup" in c["recipe"].name_en.lower() or
            "rice" in c["recipe"].name_en.lower() or
            "egg" in c["recipe"].category.lower()
        ]
        if len(breakfast_pool) < 5:
            breakfast_pool = candidate_items

        main_pool = [
            c for c in candidate_items
            if c["recipe"].category not in {"Salads"} or len(candidate_items) < 10
        ]
        if len(main_pool) < 10:
            main_pool = candidate_items

        meals_per_day = req.meals_per_day
        meal_types = ["breakfast", "lunch", "dinner"] if meals_per_day == 3 else ["lunch", "dinner"]
        total_slots = req.plan_duration_days * len(meal_types)

        is_budget_specified = req.weekly_budget_mmk is not None and req.weekly_budget_mmk > 0
        target_budget = req.weekly_budget_mmk if is_budget_specified else round(4500 * (req.household_size / 2) * total_slots)

        min_breakfast_cost = min((c["slot_cost"] for c in breakfast_pool if c["slot_cost"] > 500), default=1500)
        min_main_cost = min((c["slot_cost"] for c in main_pool if c["slot_cost"] > 1000), default=2500)

        remaining_budget = float(target_budget)
        remaining_slots = total_slots
        used_ids_this_week: Dict[str, int] = {}
        schedule_data = []
        current_cost = 0.0

        for day_idx in range(req.plan_duration_days):
            day_num = day_idx + 1
            day_en = DAYS_EN[day_idx % 7]
            day_mm = DAYS_MM[day_idx % 7]

            for m_type in meal_types:
                pool = breakfast_pool if m_type == "breakfast" else main_pool
                is_breakfast = (m_type == "breakfast")

                # Slot weight (breakfast lighter, lunch/dinner more substantial)
                slot_weight = 0.75 if is_breakfast else 1.125
                avg_slot_allowance = remaining_budget / max(1, remaining_slots)
                slot_target_cost = max(min_breakfast_cost if is_breakfast else min_main_cost, avg_slot_allowance * slot_weight)

                reserve_for_future_slots = (remaining_slots - 1) * (min_main_cost if is_breakfast else min_breakfast_cost)
                max_allowed = max(slot_target_cost * 1.5, remaining_budget - reserve_for_future_slots)

                eligible = [c for c in pool if c["slot_cost"] <= max_allowed]
                if not eligible:
                    eligible = sorted(pool, key=lambda c: c["slot_cost"])[:5]

                # Boost preferred categories if requested
                if req.preferred_categories:
                    cat_pref = [c for c in eligible if c["recipe"].category in req.preferred_categories]
                    if cat_pref:
                        eligible = cat_pref

                # Sort by cost proximity + recency penalty
                def score_candidate(cand):
                    last_used = used_ids_this_week.get(cand["recipe"].id, -10)
                    recency_penalty = 5000 if (day_num - last_used <= 2) else 0
                    return abs(cand["slot_cost"] - slot_target_cost) + recency_penalty

                eligible.sort(key=score_candidate)
                chosen = eligible[0]

                used_ids_this_week[chosen["recipe"].id] = day_num
                current_cost += chosen["slot_cost"]
                remaining_budget -= chosen["slot_cost"]
                remaining_slots -= 1

                schedule_data.append({
                    "day_of_week": day_num,
                    "day_name_en": day_en,
                    "day_name_mm": day_mm,
                    "meal_type": m_type,
                    "chosen": chosen
                })

        # Secondary optimization pass: If slightly over budget, replace the most expensive slots with authentic lower-cost alternatives
        if current_cost > target_budget:
            indexed_slots = sorted(range(len(schedule_data)), key=lambda i: schedule_data[i]["chosen"]["slot_cost"], reverse=True)
            for idx in indexed_slots:
                if current_cost <= target_budget:
                    break
                slot_info = schedule_data[idx]
                pool = breakfast_pool if slot_info["meal_type"] == "breakfast" else main_pool
                needed_reduction = current_cost - target_budget

                cheaper = [
                    c for c in pool
                    if c["slot_cost"] < slot_info["chosen"]["slot_cost"] and c["recipe"].id != slot_info["chosen"]["recipe"].id
                ]
                if cheaper:
                    cheaper.sort(key=lambda c: abs((slot_info["chosen"]["slot_cost"] - c["slot_cost"]) - needed_reduction))
                    replacement = cheaper[0]
                    current_cost -= (slot_info["chosen"]["slot_cost"] - replacement["slot_cost"])
                    schedule_data[idx]["chosen"] = replacement

        # Build schedule response
        schedule: List[MealSlotRecommendation] = []
        for item in schedule_data:
            c = item["chosen"]
            r = c["recipe"]
            schedule.append(
                MealSlotRecommendation(
                    day_of_week=item["day_of_week"],
                    day_name_en=item["day_name_en"],
                    day_name_mm=item["day_name_mm"],
                    meal_type=item["meal_type"],
                    recipe_id=r.id,
                    recipe_name_en=r.name_en,
                    recipe_name_mm=r.name_mm,
                    category=r.category or "Traditional",
                    servings=req.household_size,
                    cook_time_minutes=r.cooking_time_minutes,
                    estimated_cost_mmk=round(c["slot_cost"], 2),
                    calories_kcal=round(c["calories"], 1),
                    protein_g=round(c["protein"], 1),
                    is_vegetarian=c["flags"]["is_vegetarian"],
                    is_vegan=c["flags"]["is_vegan"],
                    is_gluten_free=c["flags"]["is_gluten_free"]
                )
            )

        # Build daily summaries
        daily_summaries: List[DailyNutritionSummary] = []
        total_calories_accum = 0.0
        total_protein_accum = 0.0

        for d in range(1, req.plan_duration_days + 1):
            day_items = [s for s in schedule_data if s["day_of_week"] == d]
            d_cal = sum(s["chosen"]["calories"] for s in day_items)
            d_prot = sum(s["chosen"]["protein"] for s in day_items)
            d_carbs = sum(s["chosen"]["carbs"] for s in day_items)
            d_fat = sum(s["chosen"]["fat"] for s in day_items)
            d_sod = sum(s["chosen"]["sodium"] for s in day_items)
            d_cost = sum(s["chosen"]["slot_cost"] for s in day_items)

            total_calories_accum += d_cal
            total_protein_accum += d_prot

            daily_summaries.append(
                DailyNutritionSummary(
                    day_of_week=d,
                    total_calories_kcal=round(d_cal, 1),
                    total_protein_g=round(d_prot, 1),
                    total_carbs_g=round(d_carbs, 1),
                    total_fat_g=round(d_fat, 1),
                    total_sodium_mg=round(d_sod, 1),
                    total_cost_mmk=round(d_cost, 2)
                )
            )

        # Budget analysis & verified messages
        is_exceeded = current_cost > target_budget
        variance = target_budget - current_cost

        if is_budget_specified:
            if is_exceeded:
                over = int(current_cost - target_budget)
                msg_en = f"Optimized to lowest-cost authentic meals. Minimum viable expense for {req.plan_duration_days} days is {int(current_cost):,} MMK (Budget exceeded by {over:,} MMK)."
                msg_mm = f"ကုန်ကျစရိတ် အသက်သာဆုံး စစ်မှန်သော ရိုးရာဟင်းလျာများဖြင့် စီစဉ်ထားသော်လည်း လျာထားဘတ်ဂျက်ထက် {over:,} ကျပ် ကျော်လွန်နေပါသည်။"
            else:
                saved = int(target_budget - current_cost)
                msg_en = f"✓ Generated within your budget! Total: {int(current_cost):,} MMK (Surplus: {saved:,} MMK available for seasonal fruits and snacks)."
                msg_mm = f"✓ လျာထားဘတ်ဂျက်အတွင်း အောင်မြင်စွာ စီစဉ်ပြီးပါပြီ။ စုစုပေါင်း: {int(current_cost):,} ကျပ် (ပိုလျှံငွေ: {saved:,} ကျပ်)။"
        else:
            msg_en = f"Balanced {req.plan_duration_days}-day meal plan totaling {int(current_cost):,} MMK for {req.household_size} person(s)."
            msg_mm = f"လူဦးရေ {req.household_size} ဦးအတွက် သင့်တင့်မျှတသော {req.plan_duration_days} ရက်စာ အစားအစာဇယား စုစုပေါင်း ကုန်ကျစရိတ် {int(current_cost):,} ကျပ် ဖြစ်ပါသည်။"

        days_count = req.plan_duration_days
        avg_cal = round(total_calories_accum / (days_count * req.household_size), 1) if (days_count and req.household_size) else 0.0
        avg_prot = round(total_protein_accum / (days_count * req.household_size), 1) if (days_count and req.household_size) else 0.0

        return MealPlanGenerateResponse(
            plan_name=f"{req.household_size}-Person Weekly Plan ({req.city})",
            city=req.city,
            household_size=req.household_size,
            target_budget_mmk=target_budget if is_budget_specified else None,
            estimated_total_cost_mmk=round(current_cost, 2),
            is_budget_exceeded=is_exceeded,
            budget_variance_mmk=round(variance, 2) if is_budget_specified else None,
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
