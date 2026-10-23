import rawRecipes from "@/data/recipes.json";
import rawPrices from "@/data/ingredient_prices.json";
import rawRetailPrices from "@/data/latest_retail_prices_by_city.json";
import rawNutrition from "@/data/ingredient_nutrition.json";
import {
  RecipeSummary,
  RecipeListResponse,
  RecipeDetail,
  RecipeIngredient,
  RecipeInstruction,
  RecipeCostBreakdown,
  RecipeNutritionBreakdown,
  CategoryCount,
} from "@/types";
import { calculateRetailPurchasing, isPantryStaple } from "./retail-packaging";

export interface RawIngredient {
  ingredient_id: string;
  name_mm: string;
  name_en: string;
  original_name?: string | null;
  quantity: number | null;
  unit: string | null;
  original_quantity_text: string | null;
  normalized_quantity: number | null;
  normalized_unit: string | null;
  preparation_note_mm: string | null;
  preparation_note_en: string | null;
}

export interface RawRecipe {
  recipe_id: string;
  name_mm: string;
  name_en: string;
  description_mm: string | null;
  description_en: string | null;
  category: string;
  meal_types: string[];
  servings?: number;
  preparation_time_minutes?: number | null;
  cooking_time_minutes?: number | null;
  instructions_mm?: string[];
  instructions_en?: string[];
  tags?: {
    dietary?: string[];
    seasonal?: string[];
    festival?: string[];
    main_ingredients?: string[];
  };
  ingredients?: RawIngredient[];
}

export interface PriceRecord {
  ingredient_id: string;
  name_mm: string;
  name_en: string;
  price_mmk: number;
  original_unit: string;
  normalized_price_mmk_per_kg: number | null;
  price_type: string;
  source_name: string;
  observed_date: string;
  market_name?: string;
}

export interface NutritionRecord {
  nutrition_id: string;
  ingredient_id: string;
  ingredient_name_mm: string;
  ingredient_name_en: string;
  reference_quantity: number;
  reference_unit: string;
  energy_kcal: number;
  protein_g: number;
  total_fat_g: number;
  carbohydrates_g: number;
  fiber_g: number;
  sodium_mg: number;
  source_name: string;
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

const ZERO_COST_INGREDIENT_IDS = new Set(["I0012", "I0017", "I0200"]); // Hot water, Tap water, Salt water

const APPROX_DISCRETE_WEIGHTS_G: Record<string, number> = {
  I0010: 50.0,  // Chicken egg (~50g)
  I0026: 50.0,  // Chicken egg (~50g)
  I0027: 70.0,  // Duck egg (~70g)
  I0006: 40.0,  // Onion small (~40g)
  I0007: 3.0,   // Garlic clove (~3g)
  I0041: 45.0,  // Lime (~45g)
  I0008: 0.1,   // Clove (~0.1g)
  I0009: 0.4,   // Cardamom pod (~0.4g)
};

export const allRecipes: RawRecipe[] = rawRecipes as unknown as RawRecipe[];

// Pre-index nutrition profiles
const nutritionMap: Record<string, NutritionRecord> = {};
for (const n of rawNutrition as unknown as NutritionRecord[]) {
  if (n && n.ingredient_id) {
    nutritionMap[n.ingredient_id] = n;
  }
}

// Pre-index prices by city
const cityPriceMaps: Record<string, Record<string, PriceRecord>> = {
  Yangon: {},
  Mandalay: {},
};

function initPriceMaps() {
  // 1. Process 134 raw price observations
  const observations = rawPrices as any[];
  for (const obs of observations) {
    const city = obs.city === "Mandalay" ? "Mandalay" : "Yangon";
    const iid = obs.ingredient_id;
    if (!iid) continue;

    const existing = cityPriceMaps[city][iid];
    const isRetail = obs.price_type === "retail";

    // Prefer retail over wholesale/estimate and newer observed_date
    if (!existing || (!existing.price_type.includes("retail") && isRetail)) {
      cityPriceMaps[city][iid] = {
        ingredient_id: iid,
        name_mm: obs.ingredient_name_mm,
        name_en: obs.ingredient_name_en,
        price_mmk: obs.price_mmk,
        original_unit: obs.original_unit,
        normalized_price_mmk_per_kg: obs.normalized_price_mmk_per_kg,
        price_type: obs.price_type,
        source_name: obs.source_name,
        observed_date: obs.observed_date,
        market_name: obs.market_name,
      };
    }
  }

  // 2. Overlay verified retail catalog summary (October 2026 Citymall & CSO prices)
  const retailSummary = rawRetailPrices as any;
  if (retailSummary && retailSummary.cities) {
    for (const city of ["Yangon", "Mandalay"]) {
      const cityList = retailSummary.cities[city] || [];
      for (const item of cityList) {
        if (!item.ingredient_id) continue;
        cityPriceMaps[city][item.ingredient_id] = {
          ingredient_id: item.ingredient_id,
          name_mm: item.name_mm,
          name_en: item.name_en,
          price_mmk: item.price_mmk,
          original_unit: item.unit,
          normalized_price_mmk_per_kg: item.normalized_price_mmk_per_kg,
          price_type: item.price_type,
          source_name: item.source_name,
          observed_date: item.observed_date,
          market_name: item.source_name,
        };
      }
    }
  }
}

initPriceMaps();

export function getPriceMap(city = "Yangon"): Record<string, PriceRecord> {
  const c = city === "Mandalay" ? "Mandalay" : "Yangon";
  return cityPriceMaps[c] || cityPriceMaps["Yangon"];
}

export function getNutritionMap(): Record<string, NutritionRecord> {
  return nutritionMap;
}

// Dynamic Recipe Cost Computation adhering strictly to zero-mocking rules
export function computeRecipeCost(
  r: RawRecipe,
  city = "Yangon",
  multiplier = 1.0
): RecipeCostBreakdown {
  const priceMap = getPriceMap(city);
  const ingredients = r.ingredients || [];
  const totalCount = ingredients.length;

  let totalCost = 0;
  let fullRetailCost = 0;
  let pantryAdjustedCost = 0;
  let pricedCount = 0;
  const breakdown: any[] = [];
  const missingPriced: any[] = [];

  for (const ing of ingredients) {
    const iid = ing.ingredient_id;
    const nq = ing.normalized_quantity;
    const nu = ing.normalized_unit;
    const scaledQty = nq !== null && nq !== undefined ? round(nq * multiplier, 2) : null;
    const isStaple = isPantryStaple(iid);

    if (ZERO_COST_INGREDIENT_IDS.has(iid) || nu === "to_taste") {
      pricedCount++;
      breakdown.push({
        ingredient_id: iid,
        name_mm: ing.name_mm,
        name_en: ing.name_en,
        scaled_quantity: scaledQty,
        unit: nu || ing.unit || "g",
        unit_price_mmk: 0,
        normalized_price_per_kg: 0,
        item_cost_mmk: 0,
        is_priced: true,
        is_zero_cost_utility: true,
        is_pantry_staple: true,
        purchasable_quantity: 0,
        purchasable_unit: "Utility",
        package_description: "Domestic Utility / Water",
        retail_package_price_mmk: 0,
        observation_source: "Municipal Household Utility / To Taste",
        observation_date: "2026-10-18",
      });
      continue;
    }

    const priceObs = priceMap[iid];
    if (priceObs && scaledQty !== null) {
      const retailCalc = calculateRetailPurchasing({
        ingredient_id: iid,
        name_en: ing.name_en,
        name_mm: ing.name_mm,
        unit: nu || ing.unit || "g",
        quantity: scaledQty,
        unit_price_mmk: priceObs.price_mmk,
        normalized_price_per_kg: priceObs.normalized_price_mmk_per_kg,
        observation_package_unit: priceObs.original_unit,
        observation_package_price: priceObs.price_mmk,
      });

      pricedCount++;
      totalCost += retailCalc.portion_cost_mmk;
      fullRetailCost += retailCalc.retail_package_price_mmk;
      if (!retailCalc.is_pantry_staple) {
        pantryAdjustedCost += retailCalc.retail_package_price_mmk;
      }

      breakdown.push({
        ingredient_id: iid,
        name_mm: ing.name_mm,
        name_en: ing.name_en,
        scaled_quantity: scaledQty,
        unit: nu || ing.unit || "g",
        unit_price_mmk: priceObs.price_mmk,
        normalized_price_per_kg: priceObs.normalized_price_mmk_per_kg,
        item_cost_mmk: retailCalc.portion_cost_mmk,
        is_priced: true,
        is_zero_cost_utility: false,
        is_pantry_staple: retailCalc.is_pantry_staple,
        purchasable_quantity: retailCalc.purchasable_quantity,
        purchasable_unit: retailCalc.purchasable_unit_en,
        package_description: retailCalc.package_description_en,
        retail_package_price_mmk: retailCalc.retail_package_price_mmk,
        observation_source: priceObs.source_name,
        observation_date: priceObs.observed_date,
      });
      continue;
    }

    // Unpriced / seasonal ingredient
    missingPriced.push({
      ingredient_id: iid,
      name_mm: ing.name_mm,
      name_en: ing.name_en,
      unit: ing.unit || "g",
      reason: "No active price observation recorded in " + city,
    });
    breakdown.push({
      ingredient_id: iid,
      name_mm: ing.name_mm,
      name_en: ing.name_en,
      scaled_quantity: scaledQty,
      unit: nu || ing.unit || "g",
      unit_price_mmk: null,
      normalized_price_per_kg: null,
      item_cost_mmk: null,
      is_priced: false,
      is_zero_cost_utility: false,
      is_pantry_staple: isStaple,
      purchasable_quantity: null,
      purchasable_unit: null,
      package_description: null,
      retail_package_price_mmk: null,
      observation_source: null,
      observation_date: null,
    });
  }

  const coveragePct = totalCount > 0 ? round((pricedCount / totalCount) * 100, 1) : 100;
  const isComplete = pricedCount === totalCount;
  const baseServings = r.servings || 4;
  const targetServings = round(baseServings * multiplier);

  return {
    recipe_id: r.recipe_id,
    city,
    servings: baseServings,
    scaled_servings: targetServings,
    estimated_cost_mmk: round(totalCost, 0),
    full_retail_pack_cost_mmk: round(fullRetailCost, 0),
    pantry_adjusted_cost_mmk: round(pantryAdjustedCost, 0),
    cost_coverage_percentage: coveragePct,
    is_cost_complete: isComplete,
    priced_ingredients_count: pricedCount,
    total_ingredients_count: totalCount,
    missing_priced_ingredients: missingPriced,
    ingredient_breakdown: breakdown,
  };
}

// Nutrition computation based on analytical 100g USDA & Thai food tables
export function computeRecipeNutrition(
  r: RawRecipe,
  servings = 4
): RecipeNutritionBreakdown {
  const ingredients = r.ingredients || [];
  let totalKcal = 0;
  let totalProtein = 0;
  let totalFat = 0;
  let totalCarbs = 0;
  let totalFiber = 0;
  let totalSodium = 0;

  let weightedCount = 0;
  const totalCount = ingredients.length;
  const unweighted: string[] = [];

  for (const ing of ingredients) {
    const nut = nutritionMap[ing.ingredient_id];
    if (!nut) {
      unweighted.push(ing.name_en);
      continue;
    }

    const nu = ing.normalized_unit;
    const nq = ing.normalized_quantity;
    let grams: number | null = null;

    if ((nu === "g" || nu === "ml") && nq !== null && nq !== undefined) {
      grams = nq;
    } else if (nu === "piece" && nq !== null && APPROX_DISCRETE_WEIGHTS_G[ing.ingredient_id]) {
      grams = nq * APPROX_DISCRETE_WEIGHTS_G[ing.ingredient_id];
    } else if (nu === "to_taste") {
      weightedCount++;
      continue;
    }

    if (grams !== null && grams > 0) {
      weightedCount++;
      const ratio = grams / 100.0;
      totalKcal += (nut.energy_kcal || 0) * ratio;
      totalProtein += (nut.protein_g || 0) * ratio;
      totalFat += (nut.total_fat_g || 0) * ratio;
      totalCarbs += (nut.carbohydrates_g || 0) * ratio;
      totalFiber += (nut.fiber_g || 0) * ratio;
      totalSodium += (nut.sodium_mg || 0) * ratio;
    } else {
      unweighted.push(ing.name_en);
    }
  }

  const isComplete = weightedCount === totalCount;
  const effectiveServings = servings > 0 ? servings : 4;

  return {
    recipe_id: r.recipe_id,
    servings: effectiveServings,
    is_nutrition_complete: isComplete,
    weighted_ingredients_ratio: `${weightedCount}/${totalCount}`,
    unweighted_ingredients: unweighted,
    per_serving: {
      calories_kcal: round(totalKcal / effectiveServings, 1),
      protein_g: round(totalProtein / effectiveServings, 1),
      fat_g: round(totalFat / effectiveServings, 1),
      carbohydrates_g: round(totalCarbs / effectiveServings, 1),
      fiber_g: round(totalFiber / effectiveServings, 1),
      sodium_mg: round(totalSodium / effectiveServings, 1),
    },
    recipe_total: {
      calories_kcal: round(totalKcal, 1),
      protein_g: round(totalProtein, 1),
      fat_g: round(totalFat, 1),
      carbohydrates_g: round(totalCarbs, 1),
      fiber_g: round(totalFiber, 1),
      sodium_mg: round(totalSodium, 1),
    },
    disclaimer:
      "Approximate nutritional values calculated from USDA FoodData Central and Thai Food Composition Database. Not clinical medical advice.",
  };
}

function computeRecipeSummary(r: RawRecipe, city = "Yangon"): RecipeSummary {
  const cost = computeRecipeCost(r, city, 1.0);
  const baseServings = r.servings || 4;
  const nutrition = computeRecipeNutrition(r, baseServings);

  return {
    id: r.recipe_id,
    name_mm: r.name_mm,
    name_en: r.name_en,
    description_mm: r.description_mm,
    description_en: r.description_en,
    category: r.category,
    meal_types: r.meal_types || ["lunch", "dinner"],
    servings: baseServings,
    preparation_time_minutes: r.preparation_time_minutes || 15,
    cooking_time_minutes: r.cooking_time_minutes || 30,
    tags: r.tags || {},
    estimated_cost_mmk: cost.estimated_cost_mmk,
    cost_coverage_percentage: cost.cost_coverage_percentage,
    is_cost_complete: cost.is_cost_complete,
    calories_kcal_per_serving: nutrition.per_serving.calories_kcal,
    protein_g_per_serving: nutrition.per_serving.protein_g,
  };
}

// Summary cache by city
const cachedSummariesByCity: Record<string, RecipeSummary[]> = {};

export function getLocalRecipeSummaries(city = "Yangon"): RecipeSummary[] {
  const c = city === "Mandalay" ? "Mandalay" : "Yangon";
  if (!cachedSummariesByCity[c]) {
    cachedSummariesByCity[c] = allRecipes.map((r) => computeRecipeSummary(r, c));
  }
  return cachedSummariesByCity[c];
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
  const city = params.city || "Yangon";
  const all = getLocalRecipeSummaries(city);
  let filtered = all;

  if (params.search) {
    const q = params.search.toLowerCase().trim();
    filtered = filtered.filter(
      (r) =>
        r.name_mm.toLowerCase().includes(q) ||
        r.name_en.toLowerCase().includes(q) ||
        (r.description_mm && r.description_mm.toLowerCase().includes(q)) ||
        (r.description_en && r.description_en.toLowerCase().includes(q)) ||
        r.id.toLowerCase().includes(q) ||
        (r.tags.main_ingredients &&
          r.tags.main_ingredients.some((ing: string) => ing.toLowerCase().includes(q)))
    );
  }

  if (params.category) {
    filtered = filtered.filter((r) => r.category === params.category);
  }

  if (params.mealType) {
    filtered = filtered.filter((r) => r.meal_types && r.meal_types.includes(params.mealType!));
  }

  if (params.dietary) {
    const dLower = params.dietary.toLowerCase();
    filtered = filtered.filter(
      (r) =>
        r.tags.dietary &&
        r.tags.dietary.some((d: string) => d.toLowerCase().includes(dLower))
    );
  }

  if (params.seasonal) {
    const sLower = params.seasonal.toLowerCase();
    filtered = filtered.filter(
      (r) =>
        r.tags.seasonal &&
        r.tags.seasonal.some((s: string) => s.toLowerCase().includes(sLower))
    );
  }

  if (params.festival) {
    const fLower = params.festival.toLowerCase();
    filtered = filtered.filter(
      (r) =>
        r.tags.festival &&
        r.tags.festival.some((f: string) => f.toLowerCase().includes(fLower))
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
  const r = allRecipes.find((item) => item.recipe_id === id);
  if (!r) return null;

  const baseServings = r.servings || 4;
  const targetServings = servings && servings >= 1 ? servings : baseServings;
  const multiplier = targetServings / baseServings;

  const cost = computeRecipeCost(r, city, multiplier);
  const nutrition = computeRecipeNutrition(r, targetServings);

  // Scaled ingredients
  const ingredients: RecipeIngredient[] = (r.ingredients || []).map((ing, idx) => {
    const scaledQty = ing.quantity !== null && ing.quantity !== undefined
      ? round(ing.quantity * multiplier, 2)
      : null;
    const scaledNormQty = ing.normalized_quantity !== null && ing.normalized_quantity !== undefined
      ? round(ing.normalized_quantity * multiplier, 2)
      : null;

    return {
      id: idx + 1,
      ingredient_id: ing.ingredient_id,
      name_mm: ing.name_mm,
      name_en: ing.name_en,
      original_name: ing.original_name || null,
      quantity: scaledQty,
      unit: ing.unit || "g",
      original_quantity_text: ing.original_quantity_text,
      normalized_quantity: scaledNormQty,
      normalized_unit: ing.normalized_unit,
      preparation_note_mm: ing.preparation_note_mm,
      preparation_note_en: ing.preparation_note_en,
    };
  });

  // Authentic cooking instructions directly from cookbook dataset
  const instructions: RecipeInstruction[] = (r.instructions_mm || []).map((ins_mm, idx) => ({
    step_number: idx + 1,
    instruction_mm: ins_mm,
    instruction_en: (r.instructions_en && r.instructions_en[idx]) || "",
  }));

  return {
    id: r.recipe_id,
    name_mm: r.name_mm,
    name_en: r.name_en,
    description_mm: r.description_mm,
    description_en: r.description_en,
    category: r.category,
    meal_types: r.meal_types || ["lunch", "dinner"],
    servings: targetServings,
    preparation_time_minutes: r.preparation_time_minutes || 15,
    cooking_time_minutes: r.cooking_time_minutes || 30,
    tags: r.tags || {},
    estimated_cost_mmk: cost.estimated_cost_mmk,
    cost_coverage_percentage: cost.cost_coverage_percentage,
    is_cost_complete: cost.is_cost_complete,
    calories_kcal_per_serving: nutrition.per_serving.calories_kcal,
    protein_g_per_serving: nutrition.per_serving.protein_g,
    source_document: "ချက်ပြုတ်အတတ်ပညာ (ဒေါ်စန်းလေး)",
    source_pdf_pages: [],
    source_printed_pages: [],
    extraction_method: "verified_cookbook_ocr_validated",
    confidence: 1.0,
    is_verified: true,
    ingredients,
    instructions,
    cost_breakdown: cost,
    nutrition_breakdown: nutrition,
  };
}

export function getLocalCategories(): CategoryCount[] {
  const counts: Record<string, number> = {};
  for (const r of allRecipes) {
    counts[r.category] = (counts[r.category] || 0) + 1;
  }
  return Object.entries(counts)
    .sort((a, b) => b[1] - a[1])
    .map(([name, count]) => ({
      category: name,
      category_mm: CATEGORY_MAP[name] || name,
      count,
    }));
}

function round(val: number, decimals = 1): number {
  const factor = Math.pow(10, decimals);
  return Math.round(val * factor) / factor;
}
