import {
  RecipeListResponse,
  RecipeDetail,
  CategoryCount,
  Market,
  MealPlanGenerateResponse,
  ReplacementOption,
  GroceryListResponse,
} from "@/types";

import {
  queryLocalRecipes,
  getLocalRecipeDetail,
  getLocalCategories,
} from "./local-recipes";
import {
  getLocalMarkets,
  getLocalMealPlan,
  getLocalMealReplacements,
  getLocalGroceryList,
} from "./local-services";

let detectedApiBase: string | null = null;
const CANDIDATE_BASES = Array.from(new Set([
  process.env.NEXT_PUBLIC_API_URL,
  "http://127.0.0.1:8001",
  "http://localhost:8001",
  "http://127.0.0.1:8000",
  "http://localhost:8000",
].filter(Boolean))) as string[];

async function safeFetch<T>(
  path: string,
  options: RequestInit = {},
  timeoutMs = 1200
): Promise<T | null> {
  const bases = detectedApiBase ? [detectedApiBase] : CANDIDATE_BASES;

  for (const base of bases) {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeoutMs);

    try {
      const res = await fetch(`${base}${path}`, {
        ...options,
        signal: controller.signal,
        cache: "no-store",
      });
      clearTimeout(timer);
      if (res.ok) {
        detectedApiBase = base;
        return (await res.json()) as T;
      }
    } catch {
      clearTimeout(timer);
    }
  }

  return null;
}

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

  const remote = await safeFetch<RecipeListResponse>(`/api/v1/recipes?${query.toString()}`);
  if (remote && remote.recipes) {
    return remote;
  }

  return queryLocalRecipes(params);
}

export async function getRecipeDetail(
  id: string,
  servings?: number,
  city = "Yangon"
): Promise<RecipeDetail> {
  const query = new URLSearchParams();
  if (servings) query.set("servings", servings.toString());
  query.set("city", city);

  const remote = await safeFetch<RecipeDetail>(`/api/v1/recipes/${id}?${query.toString()}`);
  if (remote && remote.id) {
    return remote;
  }

  const local = getLocalRecipeDetail(id, servings, city);
  if (!local) {
    throw new Error(`Recipe with id ${id} not found`);
  }
  return local;
}

export async function getCategories(): Promise<CategoryCount[]> {
  const remote = await safeFetch<CategoryCount[]>("/api/v1/recipes/categories");
  if (remote && Array.isArray(remote) && remote.length > 0) {
    return remote;
  }

  return getLocalCategories();
}

export async function getMarkets(city?: string): Promise<Market[]> {
  const query = new URLSearchParams();
  if (city) query.set("city", city);

  const remote = await safeFetch<Market[]>(`/api/v1/markets?${query.toString()}`);
  if (remote && Array.isArray(remote) && remote.length > 0) {
    return remote;
  }

  return getLocalMarkets(city);
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
}): Promise<MealPlanGenerateResponse> {
  const remote = await safeFetch<MealPlanGenerateResponse>("/api/v1/planner/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(params),
  });

  if (remote && remote.schedule && remote.schedule.length > 0) {
    return remote;
  }

  return getLocalMealPlan(params);
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
}): Promise<ReplacementOption[]> {
  const remote = await safeFetch<{ candidates?: ReplacementOption[] }>("/api/v1/planner/replace-options", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(params),
  });

  if (remote && remote.candidates && remote.candidates.length > 0) {
    return remote.candidates;
  }

  return getLocalMealReplacements(params);
}

export async function generateGroceryList(params: {
  city: string;
  household_size: number;
  recipe_ids: string[];
}): Promise<GroceryListResponse> {
  const remote = await safeFetch<GroceryListResponse>("/api/v1/grocery/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(params),
  });

  if (remote && remote.groups && remote.groups.length > 0) {
    return remote;
  }

  return getLocalGroceryList(params);
}
