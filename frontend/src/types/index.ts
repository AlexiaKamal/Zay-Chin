export type Language = "en" | "mm";

export interface RecipeIngredient {
  id: number;
  ingredient_id: string;
  original_name?: string | null;
  name_mm: string;
  name_en: string;
  quantity?: number | null;
  unit: string;
  original_quantity_text?: string | null;
  normalized_quantity?: number | null;
  normalized_unit?: string | null;
  preparation_note_mm?: string | null;
  preparation_note_en?: string | null;
}

export interface RecipeInstruction {
  step_number: number;
  instruction_mm: string;
  instruction_en: string;
}

export interface RecipeSummary {
  id: string;
  name_mm: string;
  name_en: string;
  description_mm?: string | null;
  description_en?: string | null;
  category: string;
  meal_types: string[];
  servings?: number;
  preparation_time_minutes?: number | null;
  cooking_time_minutes?: number | null;
  tags: {
    dietary?: string[];
    seasonal?: string[];
    festival?: string[];
    main_ingredients?: string[];
  };
  estimated_cost_mmk?: number | null;
  cost_coverage_percentage: number;
  is_cost_complete: boolean;
  calories_kcal_per_serving?: number | null;
  protein_g_per_serving?: number | null;
}

export interface IngredientCostItem {
  ingredient_id: string;
  name_mm: string;
  name_en: string;
  scaled_quantity?: number | null;
  unit: string;
  unit_price_mmk?: number | null;
  normalized_price_per_kg?: number | null;
  item_cost_mmk?: number | null;
  is_priced: boolean;
  is_zero_cost_utility?: boolean;
  observation_source?: string | null;
  observation_date?: string | null;
}

export interface RecipeCostBreakdown {
  recipe_id: string;
  city: string;
  servings: number;
  scaled_servings: number;
  estimated_cost_mmk: number;
  cost_coverage_percentage: number;
  is_cost_complete: boolean;
  priced_ingredients_count: number;
  total_ingredients_count: number;
  missing_priced_ingredients: {
    ingredient_id: string;
    name_mm: string;
    name_en: string;
    unit: string;
    reason: string;
  }[];
  ingredient_breakdown: IngredientCostItem[];
}

export interface RecipeNutritionBreakdown {
  recipe_id: string;
  servings: number;
  is_nutrition_complete: boolean;
  weighted_ingredients_ratio: string;
  unweighted_ingredients: string[];
  per_serving: {
    calories_kcal: number;
    protein_g: number;
    fat_g: number;
    carbohydrates_g: number;
    fiber_g: number;
    sodium_mg: number;
  };
  recipe_total: {
    calories_kcal: number;
    protein_g: number;
    fat_g: number;
    carbohydrates_g: number;
    fiber_g: number;
    sodium_mg: number;
  };
  disclaimer: string;
}

export interface RecipeDetail extends RecipeSummary {
  source_document: string;
  source_pdf_pages: number[];
  source_printed_pages: number[];
  extraction_method: string;
  confidence: number;
  is_verified: boolean;
  ingredients: RecipeIngredient[];
  instructions: RecipeInstruction[];
  cost_breakdown?: RecipeCostBreakdown;
  nutrition_breakdown?: RecipeNutritionBreakdown;
}

export interface RecipeListResponse {
  total: number;
  page: number;
  page_size: number;
  total_pages: number;
  recipes: RecipeSummary[];
}

export interface CategoryCount {
  category: string;
  category_mm: string;
  count: number;
}

export interface Market {
  id: string;
  name: string;
  city: string;
  market_type: string;
  vendor_name?: string;
  address?: string;
  latitude?: number;
  longitude?: number;
  has_verified_coordinates: boolean;
  source_reference?: string;
  recorded_price_observations_count: number;
}

export interface MealSlotRecommendation {
  day_of_week: number;
  day_name_en: string;
  day_name_mm: string;
  meal_type: string;
  recipe_id: string;
  recipe_name_en: string;
  recipe_name_mm: string;
  category: string;
  servings: number;
  cook_time_minutes?: number | null;
  estimated_cost_mmk: number;
  calories_kcal: number;
  protein_g: number;
  is_vegetarian: boolean;
  is_vegan: boolean;
  is_gluten_free: boolean;
}

export interface DailyNutritionSummary {
  day_of_week: number;
  total_calories_kcal: number;
  total_protein_g: number;
  total_carbs_g: number;
  total_fat_g: number;
  total_sodium_mg: number;
  total_cost_mmk: number;
}

export interface MealPlanGenerateResponse {
  plan_name: string;
  city: string;
  household_size: number;
  target_budget_mmk?: number | null;
  estimated_total_cost_mmk: number;
  is_budget_exceeded: boolean;
  budget_variance_mmk?: number | null;
  budget_status_message_en: string;
  budget_status_message_mm: string;
  days_count: number;
  schedule: MealSlotRecommendation[];
  daily_summaries: DailyNutritionSummary[];
  average_daily_calories_per_person: number;
  average_daily_protein_per_person: number;
}

export interface ReplacementOption {
  recipe_id: string;
  name_en: string;
  name_mm: string;
  category: string;
  estimated_cost_mmk: number;
  cost_difference_mmk: number;
  calories_kcal: number;
  protein_g: number;
  is_vegetarian: boolean;
  is_vegan: boolean;
  is_gluten_free: boolean;
}

export interface GroceryItem {
  id?: number | null;
  ingredient_id: string;
  name_en: string;
  name_mm: string;
  category: string;
  total_quantity: number;
  unit: string;
  estimated_price_mmk?: number | null;
  is_price_available: boolean;
  is_zero_cost_utility: boolean;
  observation_source?: string | null;
  observation_date?: string | null;
  is_purchased?: boolean;
}

export interface GroceryCategoryGroup {
  category_id: string;
  category_name_en: string;
  category_name_mm: string;
  subtotal_mmk: number;
  items: GroceryItem[];
}

export interface GroceryListResponse {
  id?: number | null;
  city: string;
  household_size: number;
  total_items_count: number;
  purchased_items_count: number;
  estimated_total_mmk: number;
  coverage_percentage: number;
  groups: GroceryCategoryGroup[];
  unpriced_items_count: number;
}
