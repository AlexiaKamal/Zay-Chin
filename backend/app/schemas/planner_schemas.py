from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class MealSlotRecommendation(BaseModel):
    day_of_week: int = Field(..., ge=1, le=7, description="1=Monday, 7=Sunday")
    day_name_en: str
    day_name_mm: str
    meal_type: str = Field(..., description="breakfast, lunch, dinner")
    recipe_id: str
    recipe_name_en: str
    recipe_name_mm: str
    category: str
    servings: int
    cook_time_minutes: Optional[int] = None
    estimated_cost_mmk: float
    calories_kcal: float
    protein_g: float
    is_vegetarian: bool = False
    is_vegan: bool = False
    is_gluten_free: bool = False

class DailyNutritionSummary(BaseModel):
    day_of_week: int
    total_calories_kcal: float
    total_protein_g: float
    total_carbs_g: float
    total_fat_g: float
    total_sodium_mg: float
    total_cost_mmk: float

class MealPlanGenerateRequest(BaseModel):
    city: str = Field("Yangon", description="Yangon or Mandalay")
    household_size: int = Field(2, ge=1, le=12, description="Number of people")
    weekly_budget_mmk: Optional[float] = Field(None, description="Optional weekly budget in MMK")
    dietary_preferences: List[str] = Field(default_factory=list, description="vegetarian, vegan, gluten_free, convalescent, baby_food")
    disliked_ingredients: List[str] = Field(default_factory=list, description="Ingredient IDs or names to exclude")
    preferred_categories: List[str] = Field(default_factory=list, description="Preferred recipe categories")
    meals_per_day: int = Field(3, ge=2, le=3, description="2 (lunch/dinner) or 3 (breakfast/lunch/dinner)")
    plan_duration_days: int = Field(7, ge=1, le=7, description="Number of days (default 7)")

class MealPlanGenerateResponse(BaseModel):
    plan_name: str
    city: str
    household_size: int
    target_budget_mmk: Optional[float]
    estimated_total_cost_mmk: float
    is_budget_exceeded: bool
    budget_variance_mmk: Optional[float]
    budget_status_message_en: str
    budget_status_message_mm: str
    days_count: int
    schedule: List[MealSlotRecommendation]
    daily_summaries: List[DailyNutritionSummary]
    average_daily_calories_per_person: float
    average_daily_protein_per_person: float

class MealReplacementRequest(BaseModel):
    city: str = "Yangon"
    household_size: int = 2
    day_of_week: int
    meal_type: str
    current_recipe_id: str
    dietary_preferences: List[str] = Field(default_factory=list)
    preferred_category: Optional[str] = None
    disliked_ingredients: List[str] = Field(default_factory=list)

class ReplacementOption(BaseModel):
    recipe_id: str
    name_en: str
    name_mm: str
    category: str
    estimated_cost_mmk: float
    cost_difference_mmk: float
    calories_kcal: float
    protein_g: float
    is_vegetarian: bool
    is_vegan: bool
    is_gluten_free: bool

class MealReplacementResponse(BaseModel):
    current_recipe_id: str
    candidates: List[ReplacementOption]
