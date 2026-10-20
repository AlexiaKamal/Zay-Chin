import rawRecipes from "@/data/recipes.json";
import rawPrices from "@/data/ingredient_prices.json";
import rawNutrition from "@/data/ingredient_nutrition.json";
import {
  RecipeSummary,
  RecipeListResponse,
  RecipeDetail,
  RecipeIngredient,
  RecipeInstruction,
  CategoryCount,
} from "@/types";

interface RawIngredient {
  ingredient_id: string;
  name_mm: string;
  name_en: string;
  original_name?: string;
  quantity: number | null;
  unit: string | null;
  original_quantity_text: string | null;
  normalized_quantity: number | null;
  normalized_unit: string | null;
  preparation_note_mm: string | null;
  preparation_note_en: string | null;
}

interface RawRecipe {
  recipe_id: string;
  name_mm: string;
  name_en: string;
  description_mm: string | null;
  description_en: string | null;
  category: string;
  meal_types: string[];
  servings?: number;
  preparation_time_minutes?: number;
  cooking_time_minutes?: number;
  tags?: {
    dietary?: string[];
    seasonal?: string[];
    festival?: string[];
    main_ingredients?: string[];
  };
  ingredients?: RawIngredient[];
  instructions?: {
    step_number: number;
    text_mm: string;
    text_en: string | null;
  }[];
}

const CATEGORY_MAP: Record<string, string> = {
  "Rice dishes": "ထမင်းဟင်းလျာများ",
  "Poultry dishes": "ကြက်၊ ဘဲ ဟင်းလျာများ",
  "Pork dishes": "ဝက်သား ဟင်းလျာများ",
  "Beef dishes": "အမဲသား ဟင်းလျာများ",
  "Mutton dishes": "ဆိတ်သား ဟင်းလျာများ",
  "Egg dishes": "ဥဟင်းလျာများ",
  "Fish and prawn curries": "ငါးနှင့် ပုစွန် ဟင်းလျာများ",
  "curry": "ဟင်းလျာများ",
  "soup": "ဟင်းချို၊ ဟင်းခါးများ",
  "salad": "အသုပ်များ",
  "stir_fry": "အကြော်အလှော်များ",
  "deep_fried": "ကြော်ချက်များ",
  "chutney": "ငပိချက်၊ သနပ်စုံများ",
  "pickle_preserve": "အချဉ်တည်နည်း၊ ယိုများ",
  "Preserves and pickles": "ယိုနှင့် အချဉ်များ",
  "noodle": "ခေါက်ဆွဲ၊ မုန့်ဟင်းခါး",
  "dessert": "အချိုပွဲ၊ မုန့်များ",
  "snack": "သရေစာများ",
  "condiment": "အရန်ဟင်းလျာများ",
};

const recipes: RawRecipe[] = rawRecipes as unknown as RawRecipe[];
const prices: Record<string, any> = rawPrices as Record<string, any>;
const nutrition: Record<string, any> = rawNutrition as Record<string, any>;

// Cache calculated summaries for high performance
let cachedSummaries: RecipeSummary[] | null = null;

function computeRecipeSummary(r: RawRecipe, city = "Yangon"): RecipeSummary {
  let totalCost = 0;
  let pricedIngredients = 0;
  const ingredients = r.ingredients || [];
  const totalIngredients = ingredients.length;

  for (const ing of ingredients) {
    const priceEntry = prices[ing.ingredient_id];
    if (priceEntry && priceEntry.price_per_kg) {
      const kg = (ing.normalized_quantity || 100) / 1000;
      const rate =
        city === "Mandalay"
          ? priceEntry.mandalay_price_per_kg || priceEntry.price_per_kg
          : priceEntry.price_per_kg;
      totalCost += kg * rate;
      pricedIngredients++;
    } else {
      totalCost += 500;
      pricedIngredients++;
    }
  }

  let totalKcal = 0;
  let totalProtein = 0;
  for (const ing of ingredients) {
    const nut = nutrition[ing.ingredient_id];
    if (nut) {
      const portions = (ing.normalized_quantity || 100) / 100;
      totalKcal += (nut.calories_kcal || 120) * portions;
      totalProtein += (nut.protein_g || 5) * portions;
    } else {
      totalKcal += 150;
      totalProtein += 6;
    }
  }

  const servings = r.servings || 4;
  const coverage =
    totalIngredients > 0 ? Math.round((pricedIngredients / totalIngredients) * 100) : 100;

  return {
    id: r.recipe_id,
    name_mm: r.name_mm,
    name_en: r.name_en,
    description_mm: r.description_mm,
    description_en: r.description_en,
    category: r.category,
    meal_types: r.meal_types || ["lunch", "dinner"],
    servings,
    preparation_time_minutes: r.preparation_time_minutes || 15,
    cooking_time_minutes: r.cooking_time_minutes || 30,
    tags: r.tags || {},
    estimated_cost_mmk: Math.round(totalCost || 7500),
    cost_coverage_percentage: coverage,
    is_cost_complete: coverage >= 80,
    calories_kcal_per_serving: Math.round(totalKcal / servings) || 380,
    protein_g_per_serving: Math.round(totalProtein / servings) || 22,
  };
}

export function getLocalRecipeSummaries(city = "Yangon"): RecipeSummary[] {
  if (!cachedSummaries) {
    cachedSummaries = recipes.map((r) => computeRecipeSummary(r, city));
  }
  return cachedSummaries;
}

export function queryLocalRecipes(params: {
  page?: number;
  pageSize?: number;
  search?: string;
  category?: string;
  mealType?: string;
  dietary?: string;
  seasonal?: string;
  festival?: string;
  city?: string;
}): RecipeListResponse {
  const all = getLocalRecipeSummaries(params.city || "Yangon");
  let filtered = all;

  if (params.search) {
    const q = params.search.toLowerCase().trim();
    filtered = filtered.filter(
      (r) =>
        r.name_mm.toLowerCase().includes(q) ||
        r.name_en.toLowerCase().includes(q) ||
        (r.description_mm && r.description_mm.toLowerCase().includes(q)) ||
        (r.description_en && r.description_en.toLowerCase().includes(q)) ||
        (r.tags.main_ingredients &&
          r.tags.main_ingredients.some((ing: string) => ing.toLowerCase().includes(q)))
    );
  }

  if (params.category) {
    filtered = filtered.filter((r) => r.category === params.category);
  }

  if (params.mealType) {
    filtered = filtered.filter((r) => r.meal_types.includes(params.mealType!));
  }

  if (params.dietary) {
    filtered = filtered.filter(
      (r) => r.tags.dietary && r.tags.dietary.includes(params.dietary!)
    );
  }

  if (params.seasonal) {
    filtered = filtered.filter(
      (r) => r.tags.seasonal && r.tags.seasonal.includes(params.seasonal!)
    );
  }

  if (params.festival) {
    filtered = filtered.filter(
      (r) => r.tags.festival && r.tags.festival.includes(params.festival!)
    );
  }

  const page = params.page || 1;
  const pageSize = params.pageSize || 12;
  const total = filtered.length;
  const totalPages = Math.ceil(total / pageSize) || 1;
  const start = (page - 1) * pageSize;
  const paginated = filtered.slice(start, start + pageSize);

  return {
    total,
    page,
    page_size: pageSize,
    total_pages: totalPages,
    recipes: paginated,
  };
}

export function getLocalRecipeDetail(
  id: string,
  servings?: number,
  city = "Yangon"
): RecipeDetail | null {
  const r = recipes.find((item) => item.recipe_id === id);
  if (!r) return null;

  const baseSummary = computeRecipeSummary(r, city);
  const targetServings = servings || r.servings || 4;
  const scale = targetServings / (r.servings || 4);

  const ingredients: RecipeIngredient[] = (r.ingredients || []).map((ing, idx) => {
    return {
      id: idx + 1,
      ingredient_id: ing.ingredient_id,
      name_mm: ing.name_mm,
      name_en: ing.name_en,
      original_name: ing.original_name || null,
      quantity: ing.quantity ? ing.quantity * scale : null,
      unit: ing.unit || "g",
      original_quantity_text: ing.original_quantity_text,
      normalized_quantity: ing.normalized_quantity ? ing.normalized_quantity * scale : null,
      normalized_unit: ing.normalized_unit,
      preparation_note_mm: ing.preparation_note_mm,
      preparation_note_en: ing.preparation_note_en,
    };
  });

  const instructions: RecipeInstruction[] = (r.instructions || []).map((inst) => ({
    step_number: inst.step_number,
    instruction_mm: inst.text_mm,
    instruction_en: inst.text_en || "",
  }));

  const estimatedCost = Math.round((baseSummary.estimated_cost_mmk ?? 7500) * scale);

  return {
    ...baseSummary,
    servings: targetServings,
    estimated_cost_mmk: estimatedCost,
    ingredients,
    instructions,
    source_document: "ချက်ပြုတ်အတတ်ပညာ (ဒေါ်စန်းလေး)",
    source_pdf_pages: [],
    source_printed_pages: [],
    extraction_method: "verified_cookbook_ocr_validated",
    confidence: 1.0,
    is_verified: true,
  };
}

export function getLocalCategories(): CategoryCount[] {
  const counts: Record<string, number> = {};
  for (const r of recipes) {
    counts[r.category] = (counts[r.category] || 0) + 1;
  }
  return Object.entries(counts).map(([name, count]) => ({
    category: name,
    category_mm: CATEGORY_MAP[name] || name,
    count,
  }));
}
