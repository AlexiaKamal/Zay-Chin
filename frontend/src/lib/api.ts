import { RecipeListResponse, RecipeDetail, CategoryCount, Market } from "@/types";

import { queryLocalRecipes, getLocalRecipeDetail, getLocalCategories } from "./local-recipes";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8001";

export async function getRecipes(params: {
  page?: number;
  pageSize?: number;
  search?: string;
  category?: string;
  mealType?: string;
  dietary?: string;
  seasonal?: string;
  festival?: string;
  city?: string;
}): Promise<RecipeListResponse> {
  try {
    const query = new URLSearchParams();
    if (params.page) query.set("page", params.page.toString());
    if (params.pageSize) query.set("page_size", params.pageSize.toString());
    if (params.search) query.set("search", params.search);
    if (params.category) query.set("category", params.category);
    if (params.mealType) query.set("meal_type", params.mealType);
    if (params.dietary) query.set("dietary", params.dietary);
    if (params.seasonal) query.set("seasonal", params.seasonal);
    if (params.festival) query.set("festival", params.festival);
    if (params.city) query.set("city", params.city);

    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 2000);
    const res = await fetch(`${API_BASE}/api/v1/recipes?${query.toString()}`, {
      cache: "no-store",
      signal: controller.signal,
    });
    clearTimeout(timeoutId);
    if (res.ok) {
      return await res.json();
    }
  } catch {
    // API server offline, use high-speed authentic local fallback
  }

  return queryLocalRecipes(params);
}

export async function getRecipeDetail(
  id: string,
  servings?: number,
  city: string = "Yangon"
): Promise<RecipeDetail> {
  try {
    const query = new URLSearchParams();
    if (servings) query.set("servings", servings.toString());
    query.set("city", city);

    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 2000);
    const res = await fetch(`${API_BASE}/api/v1/recipes/${id}?${query.toString()}`, {
      cache: "no-store",
      signal: controller.signal,
    });
    clearTimeout(timeoutId);
    if (res.ok) {
      return await res.json();
    }
  } catch {
    // Fallback
  }

  const local = getLocalRecipeDetail(id, servings, city);
  if (!local) {
    throw new Error(`Recipe with id ${id} not found`);
  }
  return local;
}

export async function getCategories(): Promise<CategoryCount[]> {
  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 2000);
    const res = await fetch(`${API_BASE}/api/v1/recipes/categories`, {
      cache: "no-store",
      signal: controller.signal,
    });
    clearTimeout(timeoutId);
    if (res.ok) {
      return await res.json();
    }
  } catch {
    // Fallback
  }

  return getLocalCategories();
}

export async function getMarkets(city?: string): Promise<Market[]> {
  const query = new URLSearchParams();
  if (city) query.set("city", city);

  const res = await fetch(`${API_BASE}/api/v1/markets?${query.toString()}`, {
    cache: "no-store",
  });
  if (!res.ok) {
    throw new Error(`Failed to fetch markets: ${res.statusText}`);
  }
  return res.json();
}

export async function generateMealPlan(params: {
  city: string;
  household_size: number;
  weekly_budget_mmk?: number | null;
  dietary_preferences?: string[];
  disliked_ingredients?: string[];
  preferred_categories?: string[];
  meals_per_day?: number;
  plan_duration_days?: number;
}): Promise<import("@/types").MealPlanGenerateResponse> {
  const res = await fetch(`${API_BASE}/api/v1/planner/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(params),
    cache: "no-store",
  });
  if (!res.ok) {
    throw new Error(`Failed to generate meal plan: ${res.statusText}`);
  }
  return res.json();
}

export async function getMealReplacementOptions(params: {
  city: string;
  household_size: number;
  day_of_week: number;
  meal_type: string;
  current_recipe_id: string;
  dietary_preferences?: string[];
  preferred_category?: string;
  disliked_ingredients?: string[];
}): Promise<import("@/types").ReplacementOption[]> {
  const res = await fetch(`${API_BASE}/api/v1/planner/replace-options`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(params),
    cache: "no-store",
  });
  if (!res.ok) {
    throw new Error(`Failed to fetch replacement options: ${res.statusText}`);
  }
  const data = await res.json();
  return data.candidates || [];
}

export async function generateGroceryList(params: {
  city: string;
  household_size: number;
  recipe_ids: string[];
}): Promise<import("@/types").GroceryListResponse> {
  const res = await fetch(`${API_BASE}/api/v1/grocery/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(params),
    cache: "no-store",
  });
  if (!res.ok) {
    throw new Error(`Failed to generate grocery list: ${res.statusText}`);
  }
  return res.json();
}
