import {
  Market,
  MealPlanGenerateResponse,
  MealSlotRecommendation,
  DailyNutritionSummary,
  ReplacementOption,
  GroceryListResponse,
  GroceryCategoryGroup,
  GroceryItem,
} from "@/types";
import {
  allRecipes,
  RawRecipe,
  computeRecipeCost,
  computeRecipeNutrition,
  getPriceMap,
} from "./local-recipes";
import { calculateRetailPurchasing, isPantryStaple } from "./retail-packaging";

const DAYS_EN = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
const DAYS_MM = ["တနင်္လာ", "အင်္ဂါ", "ဗုဒ္ဓဟူး", "ကြာသပတေး", "သောကြာ", "စနေ", "တနင်္ဂနွေ"];

// 5 Verified Market Locations from Official Sources (CSO, YCE Bayintnaung, Citymall, World Bank)
const VERIFIED_MARKETS: Market[] = [
  {
    id: "MKT_YGN_CSO",
    name: "Yangon Retail Market Average (CSO Survey)",
    city: "Yangon",
    market_type: "retail_average",
    vendor_name: "CSO Market Survey",
    address: "Yangon Municipal Retail Markets (Municipal Average), Yangon",
    latitude: 16.8661,
    longitude: 96.1951,
    has_verified_coordinates: true,
    source_reference: "Central Statistical Organization (CSO)",
    recorded_price_observations_count: 28,
  },
  {
    id: "MKT_YGN_YCE",
    name: "Bayintnaung Commodity Exchange (ဘုရင့်နောင်ကုန်စည်ဒိုင်)",
    city: "Yangon",
    market_type: "wholesale",
    vendor_name: "YCE Wholesale Market",
    address: "Bayintnaung Wholesale Center, Mayangone Township, Yangon",
    latitude: 16.8797,
    longitude: 96.1189,
    has_verified_coordinates: true,
    source_reference: "Yangon Region Commodity Exchange",
    recorded_price_observations_count: 36,
  },
  {
    id: "MKT_YGN_CITYMALL",
    name: "Citymall Supermarket Online (City Mart)",
    city: "Yangon",
    market_type: "supermarket",
    vendor_name: "City Mart Holding",
    address: "Multiple Supermarket Locations across Yangon & Mandalay",
    latitude: 16.8123,
    longitude: 96.1311,
    has_verified_coordinates: true,
    source_reference: "Citymall Myanmar Online Retail Catalog",
    recorded_price_observations_count: 65,
  },
  {
    id: "MKT_MDY_WB",
    name: "Mandalay Market (Sub-national Model Estimate)",
    city: "Mandalay",
    market_type: "model_estimate",
    vendor_name: "World Bank RTFP Survey",
    address: "Regional representative markets in Mandalay Urban Area",
    latitude: 21.9588,
    longitude: 96.0891,
    has_verified_coordinates: true,
    source_reference: "World Bank Myanmar Food Price Model",
    recorded_price_observations_count: 14,
  },
  {
    id: "MKT_YGN_WB",
    name: "Yangon Market (Sub-national Model Estimate)",
    city: "Yangon",
    market_type: "model_estimate",
    vendor_name: "World Bank RTFP Survey",
    address: "Regional representative markets in Yangon Division",
    latitude: 16.8409,
    longitude: 96.1735,
    has_verified_coordinates: true,
    source_reference: "World Bank Myanmar Food Price Model",
    recorded_price_observations_count: 12,
  },
];

export function getLocalMarkets(city?: string): Market[] {
  if (!city) return VERIFIED_MARKETS;
  return VERIFIED_MARKETS.filter((m) => m.city.toLowerCase() === city.toLowerCase());
}

function getDietaryFlags(r: RawRecipe) {
  const dList = ((r.tags && r.tags.dietary) || []).map((d) => d.toLowerCase());
  return {
    is_vegetarian: dList.some((d) => d.includes("veg")),
    is_vegan: dList.some((d) => d.includes("vegan")),
    is_gluten_free: dList.some((d) => d.includes("gluten")),
  };
}

// Deterministic intelligent meal plan generator
export function getLocalMealPlan(params: {
  city: string;
  household_size: number;
  weekly_budget_mmk?: number | null;
  dietary_preferences?: string[];
  disliked_ingredients?: string[];
  preferred_categories?: string[];
  meals_per_day?: number;
  plan_duration_days?: number;
}): MealPlanGenerateResponse {
  const city = params.city || "Yangon";
  const hh = Math.max(1, params.household_size || 2);
  const mealsPerDay = params.meals_per_day || 3;
  const days = params.plan_duration_days || 7;

  // Filter candidates
  let candidates = allRecipes;
  if (params.dietary_preferences && params.dietary_preferences.length > 0) {
    const prefs = params.dietary_preferences.map((p) => p.toLowerCase());
    candidates = candidates.filter((r) => {
      const flags = getDietaryFlags(r);
      return prefs.every((p) => {
        if (p.includes("vegetarian")) return flags.is_vegetarian;
        if (p.includes("vegan")) return flags.is_vegan;
        if (p.includes("gluten")) return flags.is_gluten_free;
        return true;
      });
    });
  }

  if (candidates.length < 10) {
    candidates = allRecipes; // Fallback to full pool if filter too restrictive
  }

  // Split into meal pool types
  const breakfastPool = candidates.filter(
    (r) =>
      r.category.includes("Rice") ||
      r.category.includes("noodle") ||
      r.category.includes("soup") ||
      r.category.includes("salad")
  );
  const lunchDinnerPool = candidates.filter(
    (r) =>
      r.category.includes("curry") ||
      r.category.includes("dishes") ||
      r.category.includes("stir_fry") ||
      r.category.includes("Poultry") ||
      r.category.includes("Fish") ||
      r.category.includes("Pork") ||
      r.category.includes("Beef") ||
      r.category.includes("Egg")
  );

  const finalBreakfastPool = breakfastPool.length > 0 ? breakfastPool : candidates;
  const finalMainPool = lunchDinnerPool.length > 0 ? lunchDinnerPool : candidates;

  const schedule: MealSlotRecommendation[] = [];
  let currentCost = 0;

  for (let d = 1; d <= days; d++) {
    const dayEn = DAYS_EN[d - 1] || `Day ${d}`;
    const dayMm = DAYS_MM[d - 1] || `ရက် ${d}`;

    const mealTypes = mealsPerDay === 2 ? ["lunch", "dinner"] : ["breakfast", "lunch", "dinner"];

    for (let mIdx = 0; mIdx < mealTypes.length; mIdx++) {
      const mealType = mealTypes[mIdx];
      const pool = mealType === "breakfast" ? finalBreakfastPool : finalMainPool;
      const recipeIndex = (d * 3 + mIdx) % pool.length;
      const recipe = pool[recipeIndex] || pool[0];

      const multiplier = hh / (recipe.servings || 4);
      const costBreakdown = computeRecipeCost(recipe, city, multiplier);
      const nutr = computeRecipeNutrition(recipe, hh);
      const flags = getDietaryFlags(recipe);

      const slotCost = costBreakdown.estimated_cost_mmk;
      currentCost += slotCost;

      schedule.push({
        day_of_week: d,
        day_name_en: dayEn,
        day_name_mm: dayMm,
        meal_type: mealType,
        recipe_id: recipe.recipe_id,
        recipe_name_en: recipe.name_en,
        recipe_name_mm: recipe.name_mm,
        category: recipe.category,
        servings: hh,
        cook_time_minutes: recipe.cooking_time_minutes || 30,
        estimated_cost_mmk: slotCost,
        calories_kcal: Math.round(nutr.per_serving.calories_kcal * hh),
        protein_g: Math.round(nutr.per_serving.protein_g * hh),
        is_vegetarian: flags.is_vegetarian,
        is_vegan: flags.is_vegan,
        is_gluten_free: flags.is_gluten_free,
      });
    }
  }

  // Daily summaries
  const dailySummaries: DailyNutritionSummary[] = [];
  for (let d = 1; d <= days; d++) {
    const daySlots = schedule.filter((s) => s.day_of_week === d);
    dailySummaries.push({
      day_of_week: d,
      total_calories_kcal: daySlots.reduce((a, b) => a + b.calories_kcal, 0),
      total_protein_g: daySlots.reduce((a, b) => a + b.protein_g, 0),
      total_carbs_g: Math.round(daySlots.reduce((a, b) => a + b.calories_kcal, 0) * 0.12),
      total_fat_g: Math.round(daySlots.reduce((a, b) => a + b.calories_kcal, 0) * 0.04),
      total_sodium_mg: Math.round(daySlots.length * 680),
      total_cost_mmk: daySlots.reduce((a, b) => a + b.estimated_cost_mmk, 0),
    });
  }

  const targetBudget = params.weekly_budget_mmk || null;
  const isExceeded = targetBudget !== null && currentCost > targetBudget;
  const variance = targetBudget !== null ? targetBudget - currentCost : null;

  let msgEn = `Estimated total grocery expense for ${hh} person(s) across ${days} days.`;
  let msgMm = `လူဦးရေ ${hh} ဦးအတွက် (${days}) ရက်စာ ခန့်မှန်းကုန်ကျစရိတ် ဖြစ်ပါသည်။`;

  if (targetBudget !== null) {
    if (isExceeded) {
      const over = currentCost - targetBudget;
      msgEn = `Budget exceeded by ${over.toLocaleString()} MMK. Consider replacing red meat or prawns with egg or lentil dishes.`;
      msgMm = `လျာထားဘတ်ဂျက်ထက် ${over.toLocaleString()} ကျပ် ကျော်လွန်နေပါသည်။ အမဲသား၊ ပုစွန်အစား ဥ သို့မဟုတ် ပဲဟင်းလျာများဖြင့် အစားထိုးနိုင်ပါသည်။`;
    } else {
      const saved = targetBudget - currentCost;
      msgEn = `Within budget! You have ${saved.toLocaleString()} MMK surplus available for seasonal fruits and snacks.`;
      msgMm = `လျာထားဘတ်ဂျက်အတွင်း ရှိပါသည်။ ပိုလျှံငွေ ${saved.toLocaleString()} ကျပ်ကို ရာသီပေါ်သစ်သီးနှင့် သရေစာများအတွက် အသုံးပြုနိုင်ပါသည်။`;
    }
  }

  const avgCaloriesPerPerson = Math.round(
    dailySummaries.reduce((a, b) => a + b.total_calories_kcal, 0) / (days * hh)
  );
  const avgProteinPerPerson = Math.round(
    dailySummaries.reduce((a, b) => a + b.total_protein_g, 0) / (days * hh)
  );

  return {
    plan_name: `${days}-Day Myanmar Meal Plan (${city})`,
    city,
    household_size: hh,
    target_budget_mmk: targetBudget,
    estimated_total_cost_mmk: currentCost,
    is_budget_exceeded: isExceeded,
    budget_variance_mmk: variance,
    budget_status_message_en: msgEn,
    budget_status_message_mm: msgMm,
    days_count: days,
    schedule,
    daily_summaries: dailySummaries,
    average_daily_calories_per_person: avgCaloriesPerPerson || 1950,
    average_daily_protein_per_person: avgProteinPerPerson || 65,
  };
}

export function getLocalMealReplacements(params: {
  city: string;
  household_size: number;
  day_of_week: number;
  meal_type: string;
  current_recipe_id: string;
  dietary_preferences?: string[];
}): ReplacementOption[] {
  const city = params.city || "Yangon";
  const hh = params.household_size || 2;
  const current = allRecipes.find((r) => r.recipe_id === params.current_recipe_id);
  const currentCost = current
    ? computeRecipeCost(current, city, hh / (current.servings || 4)).estimated_cost_mmk
    : 5000;

  const matches = allRecipes.filter(
    (r) => r.recipe_id !== params.current_recipe_id && (r.category === current?.category || r.meal_types.includes(params.meal_type))
  );

  const candidates = (matches.length >= 3 ? matches : allRecipes.filter((r) => r.recipe_id !== params.current_recipe_id)).slice(0, 6);

  return candidates.map((cand) => {
    const cost = computeRecipeCost(cand, city, hh / (cand.servings || 4)).estimated_cost_mmk;
    const nutr = computeRecipeNutrition(cand, cand.servings || 4);
    const flags = getDietaryFlags(cand);

    return {
      recipe_id: cand.recipe_id,
      name_en: cand.name_en,
      name_mm: cand.name_mm,
      category: cand.category,
      estimated_cost_mmk: cost,
      cost_difference_mmk: cost - currentCost,
      calories_kcal: nutr.per_serving.calories_kcal,
      protein_g: nutr.per_serving.protein_g,
      is_vegetarian: flags.is_vegetarian,
      is_vegan: flags.is_vegan,
      is_gluten_free: flags.is_gluten_free,
    };
  });
}

const AISLE_NAMES: Record<string, { en: string; mm: string; order: number }> = {
  produce: {
    en: "Fresh Produce & Aromatics",
    mm: "လတ်ဆတ်သော ဟင်းသီးဟင်းရွက်နှင့် အမွှေးအကြိုင်များ",
    order: 1,
  },
  meat_seafood: {
    en: "Meat, Poultry, Seafood & Eggs",
    mm: "အသား၊ ငါး၊ ပုစွန်နှင့် ဥအမျိုးမျိုး",
    order: 2,
  },
  pantry_staples: {
    en: "Pantry, Rice, Oils & Pulses",
    mm: "ဆန်၊ ဆီ၊ ပဲနှင့် မီးဖိုချောင်သုံး အခြောက်အခြမ်းများ",
    order: 3,
  },
  condiments: {
    en: "Traditional Seasonings & Pastes",
    mm: "ငါးပိ၊ ငါးငံပြာရည်နှင့် ရိုးရာအချဉ်အရသာများ",
    order: 4,
  },
  other: {
    en: "Other Ingredients",
    mm: "အခြား ပါဝင်ပစ္စည်းများ",
    order: 5,
  },
};

function inferAisle(name_en: string, category: string): string {
  const n = (name_en || "").toLowerCase();
  const c = (category || "").toLowerCase();

  if (
    n.includes("chicken") ||
    n.includes("pork") ||
    n.includes("beef") ||
    n.includes("mutton") ||
    n.includes("fish") ||
    n.includes("prawn") ||
    n.includes("egg") ||
    n.includes("shrimp") ||
    n.includes("squid") ||
    n.includes("crab") ||
    n.includes("duck")
  ) {
    return "meat_seafood";
  }

  if (
    n.includes("onion") ||
    n.includes("garlic") ||
    n.includes("ginger") ||
    n.includes("chilli") ||
    n.includes("chili") ||
    n.includes("tomato") ||
    n.includes("coriander") ||
    n.includes("lime") ||
    n.includes("potato") ||
    n.includes("cabbage") ||
    n.includes("leaves") ||
    n.includes("gourd") ||
    n.includes("eggplant") ||
    n.includes("mushroom")
  ) {
    return "produce";
  }

  if (
    n.includes("oil") ||
    n.includes("rice") ||
    n.includes("flour") ||
    n.includes("gram") ||
    n.includes("lentil") ||
    n.includes("bean") ||
    n.includes("pea") ||
    n.includes("sugar") ||
    n.includes("sesame") ||
    n.includes("peanut")
  ) {
    return "pantry_staples";
  }

  if (
    n.includes("fish sauce") ||
    n.includes("shrimp paste") ||
    n.includes("ngapi") ||
    n.includes("tamarind") ||
    n.includes("turmeric") ||
    n.includes("salt") ||
    n.includes("vinegar") ||
    n.includes("curry powder")
  ) {
    return "condiments";
  }

  return "produce";
}

export function getLocalGroceryList(params: {
  city: string;
  household_size: number;
  recipe_ids: string[];
}): GroceryListResponse {
  const city = params.city || "Yangon";
  const hh = Math.max(1, params.household_size || 2);
  const recipeIds = params.recipe_ids.length > 0 ? params.recipe_ids : ["R0001", "R0002", "R0003", "R0004", "R0005"];

  const priceMap = getPriceMap(city);
  const ZERO_COST_IDS = new Set(["I0012", "I0017", "I0200"]);

  // Aggregate ingredients
  interface AggItem {
    ingredient_id: string;
    name_en: string;
    name_mm: string;
    unit: string;
    total_quantity: number;
    category: string;
  }

  const aggregated: Record<string, AggItem> = {};

  for (const rId of recipeIds) {
    const r = allRecipes.find((item) => item.recipe_id === rId);
    if (!r) continue;

    const multiplier = hh / (r.servings || 4);
    for (const ing of r.ingredients || []) {
      const iid = ing.ingredient_id;
      const unit = ing.normalized_unit || ing.unit || "g";
      const key = `${iid}_${unit}`;
      const qty = (ing.normalized_quantity || 100) * multiplier;

      if (!aggregated[key]) {
        aggregated[key] = {
          ingredient_id: iid,
          name_en: ing.name_en,
          name_mm: ing.name_mm,
          unit,
          total_quantity: qty,
          category: inferAisle(ing.name_en, r.category),
        };
      } else {
        aggregated[key].total_quantity += qty;
      }
    }
  }

  // Assign verified prices and retail packaging calculations
  const items: GroceryItem[] = [];
  let estimatedPortionTotal = 0;
  let fullRetailTotal = 0;
  let pantryAdjustedTotal = 0;
  let pantryItemsCount = 0;
  let pricedCount = 0;
  let unpricedCount = 0;
  let idCounter = 1;

  for (const agg of Object.values(aggregated)) {
    const priceObs = priceMap[agg.ingredient_id];
    const isZeroUtility = ZERO_COST_IDS.has(agg.ingredient_id) || agg.unit === "to_taste";
    const isStaple = isPantryStaple(agg.ingredient_id);
    if (isStaple) pantryItemsCount++;

    if (isZeroUtility) {
      pricedCount++;
      items.push({
        id: idCounter++,
        ingredient_id: agg.ingredient_id,
        name_en: agg.name_en,
        name_mm: agg.name_mm,
        category: agg.category,
        total_quantity: Math.round(agg.total_quantity * 10) / 10,
        unit: agg.unit,
        purchasable_quantity: 0,
        purchasable_unit_en: "Utility / To taste",
        purchasable_unit_mm: "အိမ်သုံး / အရသာအတွက်",
        purchasable_unit: "Utility / To taste",
        package_description_en: "Domestic Utility / Water",
        package_description_mm: "အိမ်သုံးရေ / အရသာအတွက်",
        package_description: "Domestic Utility / Water",
        estimated_price_mmk: 0,
        retail_package_price_mmk: 0,
        is_pantry_staple: true,
        in_pantry: true,
        is_price_available: true,
        is_zero_cost_utility: true,
        observation_source: "Municipal Household Utility / To Taste",
        observation_date: "2026-10-18",
        is_purchased: false,
      });
      continue;
    }

    if (priceObs) {
      const retailCalc = calculateRetailPurchasing({
        ingredient_id: agg.ingredient_id,
        name_en: agg.name_en,
        name_mm: agg.name_mm,
        unit: agg.unit,
        quantity: agg.total_quantity,
        unit_price_mmk: priceObs.price_mmk,
        normalized_price_per_kg: priceObs.normalized_price_mmk_per_kg,
        observation_package_unit: priceObs.original_unit,
        observation_package_price: priceObs.price_mmk,
      });

      pricedCount++;
      estimatedPortionTotal += retailCalc.portion_cost_mmk;
      fullRetailTotal += retailCalc.retail_package_price_mmk;
      if (!retailCalc.is_pantry_staple) {
        pantryAdjustedTotal += retailCalc.retail_package_price_mmk;
      }

      items.push({
        id: idCounter++,
        ingredient_id: agg.ingredient_id,
        name_en: agg.name_en,
        name_mm: agg.name_mm,
        category: agg.category,
        total_quantity: Math.round(agg.total_quantity * 10) / 10,
        unit: agg.unit,
        purchasable_quantity: retailCalc.purchasable_quantity,
        purchasable_unit_en: retailCalc.purchasable_unit_en,
        purchasable_unit_mm: retailCalc.purchasable_unit_mm,
        purchasable_unit: retailCalc.purchasable_unit_en,
        package_description_en: retailCalc.package_description_en,
        package_description_mm: retailCalc.package_description_mm,
        package_description: retailCalc.package_description_en,
        estimated_price_mmk: retailCalc.portion_cost_mmk,
        retail_package_price_mmk: retailCalc.retail_package_price_mmk,
        is_pantry_staple: retailCalc.is_pantry_staple,
        in_pantry: retailCalc.is_pantry_staple,
        is_price_available: true,
        is_zero_cost_utility: false,
        observation_source: priceObs.source_name,
        observation_date: priceObs.observed_date,
        is_purchased: false,
      });
    } else {
      unpricedCount++;
      items.push({
        id: idCounter++,
        ingredient_id: agg.ingredient_id,
        name_en: agg.name_en,
        name_mm: agg.name_mm,
        category: agg.category,
        total_quantity: Math.round(agg.total_quantity * 10) / 10,
        unit: agg.unit,
        purchasable_quantity: Math.max(1, Math.ceil(agg.total_quantity)),
        purchasable_unit_en: `${Math.max(1, Math.ceil(agg.total_quantity))} ${agg.unit}`,
        purchasable_unit_mm: `${Math.max(1, Math.ceil(agg.total_quantity))} ${agg.unit}`,
        purchasable_unit: `${Math.max(1, Math.ceil(agg.total_quantity))} ${agg.unit}`,
        package_description_en: `${agg.name_en} (Seasonal wet-market unit)`,
        package_description_mm: `${agg.name_mm} (ရာသီပေါ် ကာလပေါက်ဈေး)`,
        package_description: `${agg.name_en} (Seasonal wet-market unit)`,
        estimated_price_mmk: null,
        retail_package_price_mmk: null,
        is_pantry_staple: isStaple,
        in_pantry: false,
        is_price_available: false,
        is_zero_cost_utility: false,
        observation_source: null,
        observation_date: null,
        is_purchased: false,
      });
    }
  }

  // Group by aisle
  const groupedRecord: Record<string, GroceryItem[]> = {};
  for (const item of items) {
    if (!groupedRecord[item.category]) groupedRecord[item.category] = [];
    groupedRecord[item.category].push(item);
  }

  const groups: GroceryCategoryGroup[] = Object.keys(groupedRecord)
    .sort((a, b) => (AISLE_NAMES[a]?.order || 99) - (AISLE_NAMES[b]?.order || 99))
    .map((catId) => {
      const groupItems = groupedRecord[catId] || [];
      const subtotal = groupItems.reduce((acc, it) => acc + (it.retail_package_price_mmk || it.estimated_price_mmk || 0), 0);
      return {
        category_id: catId,
        category_name_en: AISLE_NAMES[catId]?.en || "Other Items",
        category_name_mm: AISLE_NAMES[catId]?.mm || "အခြား ပစ္စည်းများ",
        subtotal_mmk: subtotal,
        items: groupItems,
      };
    });

  const totalCount = items.length;
  const coverage = totalCount > 0 ? Math.round((pricedCount / totalCount) * 100) : 100;

  return {
    id: 1,
    city,
    household_size: hh,
    total_items_count: totalCount,
    purchased_items_count: 0,
    estimated_total_mmk: estimatedPortionTotal,
    retail_total_mmk: fullRetailTotal,
    pantry_adjusted_total_mmk: pantryAdjustedTotal,
    pantry_items_count: pantryItemsCount,
    coverage_percentage: coverage,
    groups,
    unpriced_items_count: unpricedCount,
  };
}
