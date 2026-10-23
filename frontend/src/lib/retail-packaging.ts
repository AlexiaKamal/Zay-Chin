/**
 * Zay Chin (ဈေးခြင်း) — Retail Packaging & Grocery Purchasing Engine
 * 
 * Bridges the gap between:
 * 1. "Recipe Ingredient Cost" (portion prorated, e.g. 22.5g salt, 0.6 cucumber)
 * 2. "Grocery Retail Pack Cost" (cashier out-of-pocket, e.g. 1 pack 400g salt, 1 whole cucumber)
 * 3. "Pantry Staples" (items households typically keep in stock: salt, oil, sugar, fish sauce, spices)
 */

export interface PurchasableItemCalculation {
  ingredient_id: string;
  name_en: string;
  name_mm: string;
  required_quantity: number;
  required_unit: string;
  purchasable_quantity: number;
  purchasable_unit_en: string;
  purchasable_unit_mm: string;
  package_description_en: string;
  package_description_mm: string;
  is_pantry_staple: boolean;
  is_discrete_count: boolean;
  portion_cost_mmk: number;
  retail_package_price_mmk: number;
}

// Universal household pantry staples in Myanmar kitchens
export const PANTRY_STAPLE_IDS = new Set([
  "I0003", // Cooking oil (ဆီ)
  "I0004", // Salt (ဆား)
  "I0005", // Sugar (သကြား)
  "I0012", // Hot water (ရေနွေး)
  "I0017", // Water (ရေ)
  "I0038", // Chili powder (ငရုတ်သီးမှုန့်)
  "I0039", // Turmeric powder (နနွင်းမှုန့်)
  "I0040", // Seasoning powder / MSG (ဟင်းခတ်မှုန့်)
  "I0054", // Soy sauce light (ပဲငံပြာရည်အကြည်)
  "I0055", // Fish sauce (ငံပြာရည်)
  "I0062", // Soy sauce dark (ပဲငံပြာရည်အနောက်)
  "I0067", // Sesame oil (နှမ်းဆီ)
  "I0200", // Salt water (ဆားရည်)
]);

interface KnownPackageRule {
  pack_size_grams?: number;
  min_pieces?: number;
  default_price_mmk?: number;
  unit_en: string;
  unit_mm: string;
  desc_en: string;
  desc_mm: string;
  is_pantry: boolean;
}

const KNOWN_PACKAGE_RULES: Record<string, KnownPackageRule> = {
  // Salt: 400g bag
  I0004: {
    pack_size_grams: 400,
    default_price_mmk: 1200,
    unit_en: "pack (400g)",
    unit_mm: "ထုပ် (၄၀၀ ဂရမ်)",
    desc_en: "Iodized Cooking Salt 400G Pack",
    desc_mm: "အိုင်အိုဒင်းဆား ၄၀၀ ဂရမ် ၁ ထုပ်",
    is_pantry: true,
  },
  // Sugar: 1kg pack
  I0005: {
    pack_size_grams: 1000,
    default_price_mmk: 4500,
    unit_en: "pack (1kg)",
    unit_mm: "ထုပ် (၁ ကီလို)",
    desc_en: "White Granulated Sugar 1KG Pack",
    desc_mm: "သကြားဖြူ ၁ ကီလို ၁ ထုပ်",
    is_pantry: true,
  },
  // Cooking Oil: 0.5 viss / 816g bottle
  I0003: {
    pack_size_grams: 816.5,
    default_price_mmk: 8000,
    unit_en: "bottle (0.5 Viss / ~816g)",
    unit_mm: "ပုလင်း (၅၀ ကျပ်သား)",
    desc_en: "Peanut / Cooking Oil Bottle",
    desc_mm: "မြေပဲဆီ / ချက်ဆီ ပုလင်းငယ်",
    is_pantry: true,
  },
  // Sesame Oil: 250ml bottle
  I0067: {
    pack_size_grams: 250,
    default_price_mmk: 4500,
    unit_en: "bottle (250ml)",
    unit_mm: "ပုလင်း (၂၅၀ မီလီလီတာ)",
    desc_en: "Pure Sesame Oil Bottle",
    desc_mm: "နှမ်းဆီသန့် ပုလင်းငယ်",
    is_pantry: true,
  },
  // Fish Sauce: 700ml bottle
  I0055: {
    pack_size_grams: 700,
    default_price_mmk: 2200,
    unit_en: "bottle (700ml)",
    unit_mm: "ပုလင်း (၇၀၀ မီလီလီတာ)",
    desc_en: "Traditional Fish Sauce Bottle",
    desc_mm: "ရိုးရာငါးငံပြာရည် ပုလင်း",
    is_pantry: true,
  },
  // Soy Sauce: 500ml bottle
  I0054: {
    pack_size_grams: 500,
    default_price_mmk: 2500,
    unit_en: "bottle (500ml)",
    unit_mm: "ပုလင်း (၅၀၀ မီလီလီတာ)",
    desc_en: "Soy Sauce Bottle",
    desc_mm: "ပဲငံပြာရည် ပုလင်း",
    is_pantry: true,
  },
  I0062: {
    pack_size_grams: 500,
    default_price_mmk: 2500,
    unit_en: "bottle (500ml)",
    unit_mm: "ပုလင်း (၅၀၀ မီလီလီတာ)",
    desc_en: "Dark Soy Sauce Bottle",
    desc_mm: "ပဲငံပြာရည်အနောက် ပုလင်း",
    is_pantry: true,
  },
  // Turmeric: 50g packet
  I0039: {
    pack_size_grams: 50,
    default_price_mmk: 800,
    unit_en: "packet (50g)",
    unit_mm: "ထုပ် (၅၀ ဂရမ်)",
    desc_en: "Turmeric Powder Packet",
    desc_mm: "နနွင်းမှုန့် အထုပ်ငယ်",
    is_pantry: true,
  },
  // Chili Powder: 100g packet
  I0038: {
    pack_size_grams: 100,
    default_price_mmk: 1500,
    unit_en: "packet (100g)",
    unit_mm: "ထုပ် (၁၀၀ ဂရမ်)",
    desc_en: "Chili Powder Packet",
    desc_mm: "ငရုတ်သီးမှုန့် ၁ ထုပ်",
    is_pantry: true,
  },
  // Seasoning powder: 100g packet
  I0040: {
    pack_size_grams: 100,
    default_price_mmk: 1200,
    unit_en: "packet (100g)",
    unit_mm: "ထုပ် (၁၀၀ ဂရမ်)",
    desc_en: "Seasoning Powder Packet",
    desc_mm: "ဟင်းခတ်မှုန့် ၁ ထုပ်",
    is_pantry: true,
  },
  // Rice: 1 Pyi (2.128 kg)
  I0001: {
    pack_size_grams: 2128,
    default_price_mmk: 4800,
    unit_en: "Pyi (2.128 kg)",
    unit_mm: "ပြည် (၂.၁၂၈ ကီလို)",
    desc_en: "Standard Rice (1 Pyi bag)",
    desc_mm: "ဆန် ၁ ပြည်အိတ်",
    is_pantry: false,
  },
  // Butter: 227g block
  I0002: {
    pack_size_grams: 227,
    default_price_mmk: 11500,
    unit_en: "block (227g)",
    unit_mm: "တုံး (၂၂၇ ဂရမ်)",
    desc_en: "Pure Butter Block (227g)",
    desc_mm: "ထောပတ်သန့် ၁ တုံး",
    is_pantry: false,
  },
  // Chicken Egg: 1 egg minimum
  I0026: {
    min_pieces: 1,
    default_price_mmk: 450,
    unit_en: "whole egg",
    unit_mm: "လုံး",
    desc_en: "Fresh Chicken Egg",
    desc_mm: "လတ်ဆတ်သော ကြက်ဥ",
    is_pantry: false,
  },
  // Duck Egg: 1 egg minimum
  I0027: {
    min_pieces: 1,
    default_price_mmk: 550,
    unit_en: "whole egg",
    unit_mm: "လုံး",
    desc_en: "Fresh Duck Egg",
    desc_mm: "လတ်ဆတ်သော ဘဲဥ",
    is_pantry: false,
  },
  // Lime: 1 piece minimum
  I0041: {
    min_pieces: 1,
    default_price_mmk: 300,
    unit_en: "whole lime",
    unit_mm: "လုံး",
    desc_en: "Fresh Lime",
    desc_mm: "သံပရာသီး ၁ လုံး",
    is_pantry: false,
  },
};

export function isPantryStaple(ingredient_id: string): boolean {
  return PANTRY_STAPLE_IDS.has(ingredient_id);
}

export function calculateRetailPurchasing(params: {
  ingredient_id: string;
  name_en: string;
  name_mm: string;
  unit: string;
  quantity: number; // e.g. 22.5g or 0.6 piece
  unit_price_mmk?: number | null;
  normalized_price_per_kg?: number | null;
  observation_package_unit?: string | null;
  observation_package_price?: number | null;
}): PurchasableItemCalculation {
  const {
    ingredient_id,
    name_en,
    name_mm,
    unit,
    quantity,
    unit_price_mmk,
    normalized_price_per_kg,
    observation_package_unit,
    observation_package_price,
  } = params;

  const isZeroUtility =
    ingredient_id === "I0012" ||
    ingredient_id === "I0017" ||
    ingredient_id === "I0200" ||
    unit === "to_taste";

  if (isZeroUtility) {
    return {
      ingredient_id,
      name_en,
      name_mm,
      required_quantity: quantity,
      required_unit: unit,
      purchasable_quantity: 0,
      purchasable_unit_en: "Utility / To taste",
      purchasable_unit_mm: "အိမ်သုံး / အရသာအတွက်",
      package_description_en: "Domestic Utility / Salt to taste",
      package_description_mm: "အိမ်သုံးရေ / မိမိစိတ်ကြိုက်",
      is_pantry_staple: true,
      is_discrete_count: false,
      portion_cost_mmk: 0,
      retail_package_price_mmk: 0,
    };
  }

  const isStaple = isPantryStaple(ingredient_id);
  const known = KNOWN_PACKAGE_RULES[ingredient_id];
  const isCount =
    unit === "piece" ||
    unit.includes("လုံး") ||
    unit.includes("စီး") ||
    unit.includes("ခေါက်") ||
    unit.includes("ပွင့်") ||
    unit.includes("စေ့");

  // 1. Calculate prorated portion cost (the exact amount consumed)
  let portionCost = 0;
  if (normalized_price_per_kg && (unit === "g" || unit === "ml")) {
    portionCost = Math.round((quantity / 1000.0) * normalized_price_per_kg);
  } else if (unit_price_mmk && isCount) {
    portionCost = Math.round(quantity * unit_price_mmk);
  } else if (normalized_price_per_kg) {
    portionCost = Math.round((quantity / 1000.0) * normalized_price_per_kg);
  } else if (unit_price_mmk) {
    portionCost = Math.round(unit_price_mmk);
  }

  // 2. Calculate purchasable retail package and cashier out-of-pocket cost
  let purchasableQty = 1;
  let purchasableUnitEn = unit;
  let purchasableUnitMm = unit;
  let packageDescEn = `${name_en} (Standard Unit)`;
  let packageDescMm = `${name_mm} (လက်လီဝယ်ယူမှု)`;
  let retailPackagePrice = portionCost;

  if (isCount) {
    // Cannot buy 0.6 cucumber or 2.3 eggs at grocery store -> round up to next integer!
    purchasableQty = Math.max(1, Math.ceil(quantity));
    const piecePrice = unit_price_mmk || known?.default_price_mmk || 800;
    retailPackagePrice = purchasableQty * piecePrice;
    purchasableUnitEn = purchasableQty > 1 ? `${purchasableQty} whole pieces` : "1 whole piece";
    purchasableUnitMm = `${purchasableQty} လုံး အပြည့်`;
    packageDescEn = `${purchasableQty} Whole ${name_en}`;
    packageDescMm = `${name_mm} ${purchasableQty} လုံး`;
  } else if (known && known.pack_size_grams) {
    // Packaged grocery with standard pack size (e.g. 400g salt, 1kg sugar, 816g oil)
    const packsCount = Math.max(1, Math.ceil(quantity / known.pack_size_grams));
    const singlePackPrice =
      observation_package_price ||
      (normalized_price_per_kg
        ? Math.round((known.pack_size_grams / 1000.0) * normalized_price_per_kg)
        : known.default_price_mmk || 1200);

    purchasableQty = packsCount;
    retailPackagePrice = packsCount * singlePackPrice;
    purchasableUnitEn = `${packsCount} ${known.unit_en}`;
    purchasableUnitMm = `${packsCount} ${known.unit_mm}`;
    packageDescEn = `${known.desc_en} (x${packsCount})`;
    packageDescMm = `${known.desc_mm} (${packsCount} ထုပ်)`;
  } else if (unit === "g" || unit === "ml") {
    // Fresh wet-market bulk produce / meat / vegetables
    // Wet markets sell in minimum units (e.g. 10 kyattha / 163g or 250g minimum vendor scoop)
    const minGrams = isStaple ? 250 : 163;
    const actualGramsNeeded = Math.max(minGrams, Math.round(quantity));
    
    // Round to clean supermarket tray or wet-market scoop (nearest 50g)
    const cleanGrams = Math.ceil(actualGramsNeeded / 50) * 50;
    purchasableQty = cleanGrams;
    purchasableUnitEn = `${cleanGrams}g portion`;
    purchasableUnitMm = `${cleanGrams} ဂရမ် အထုပ်`;
    packageDescEn = `Fresh ${name_en} (${cleanGrams}g)`;
    packageDescMm = `လတ်ဆတ်သော ${name_mm} (${cleanGrams} ဂရမ်)`;

    if (normalized_price_per_kg) {
      retailPackagePrice = Math.round((cleanGrams / 1000.0) * normalized_price_per_kg);
    } else {
      retailPackagePrice = Math.max(portionCost, 1000);
    }
  } else {
    // Fallback
    purchasableQty = Math.max(1, Math.ceil(quantity || 1));
    retailPackagePrice = Math.max(portionCost, 1000);
  }

  return {
    ingredient_id,
    name_en,
    name_mm,
    required_quantity: Math.round(quantity * 10) / 10,
    required_unit: unit,
    purchasable_quantity: purchasableQty,
    purchasable_unit_en: purchasableUnitEn,
    purchasable_unit_mm: purchasableUnitMm,
    package_description_en: packageDescEn,
    package_description_mm: packageDescMm,
    is_pantry_staple: isStaple,
    is_discrete_count: isCount,
    portion_cost_mmk: Math.max(0, portionCost),
    retail_package_price_mmk: Math.max(portionCost, retailPackagePrice),
  };
}
