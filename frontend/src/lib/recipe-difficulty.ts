/**
 * Recipe Difficulty & Cooking Time Classifier
 * Categorizes recipes into Easy, Medium, and Hard based on:
 * 1. Cooking and preparation time (3 averages: ~18m Easy, ~35m Medium, ~55m Hard)
 * 2. Complexity of preparation steps
 * 3. Number of ingredients
 */

export type DifficultyLevel = "easy" | "medium" | "hard";

export interface RecipeDifficultyInfo {
  difficulty: DifficultyLevel;
  cookingTimeMinutes: number;
  label_en: string;
  label_mm: string;
  badgeColor: string;
  badgeBg: string;
}

export function computeRecipeDifficulty(recipe: {
  cooking_time_minutes?: number | null;
  preparation_time_minutes?: number | null;
  category?: string | null;
  name_en?: string | null;
  name_mm?: string | null;
  ingredients?: any[] | null;
  instructions_mm?: string[] | null;
  instructions_en?: string[] | null;
}): RecipeDifficultyInfo {
  let time = recipe.cooking_time_minutes || recipe.preparation_time_minutes;
  const ingCount = Array.isArray(recipe.ingredients) ? recipe.ingredients.length : 8;
  const stepsCount = Array.isArray(recipe.instructions_mm)
    ? recipe.instructions_mm.length
    : Array.isArray(recipe.instructions_en)
    ? recipe.instructions_en.length
    : 5;

  const cat = (recipe.category || "").toLowerCase();
  const nameEn = (recipe.name_en || "").toLowerCase();

  if (!time || time <= 0) {
    if (cat.includes("salad") || nameEn.includes("salad") || nameEn.includes("thoke")) {
      time = 15;
    } else if (cat.includes("soup") || nameEn.includes("soup") || nameEn.includes("hin gyo") || nameEn.includes("chin")) {
      time = 20;
    } else if (cat.includes("egg") || nameEn.includes("egg") || nameEn.includes("fried rice") || nameEn.includes("omelet")) {
      time = 20;
    } else if (cat.includes("noodle") || cat.includes("rice") || cat.includes("vegetable")) {
      time = 25;
    } else if (cat.includes("fish") || cat.includes("seafood") || cat.includes("prawn") || cat.includes("poultry") || nameEn.includes("chicken")) {
      time = 35;
    } else if (cat.includes("pork") || nameEn.includes("pork")) {
      time = 45;
    } else if (cat.includes("beef") || cat.includes("mutton") || nameEn.includes("biryani") || nameEn.includes("danbauk")) {
      time = 55;
    } else {
      time = 30;
    }

    if (stepsCount >= 7) time += 5;
    if (ingCount >= 12) time += 5;
  }

  let difficulty: DifficultyLevel = "medium";
  if (time <= 25 && ingCount <= 10 && stepsCount <= 6) {
    difficulty = "easy";
  } else if (time > 45 || ingCount >= 14 || stepsCount >= 9) {
    difficulty = "hard";
  } else {
    difficulty = "medium";
  }

  if (difficulty === "easy") {
    return {
      difficulty: "easy",
      cookingTimeMinutes: time,
      label_en: "Easy",
      label_mm: "လွယ်ကူ",
      badgeColor: "text-emerald-700 border-emerald-300",
      badgeBg: "bg-emerald-50",
    };
  } else if (difficulty === "medium") {
    return {
      difficulty: "medium",
      cookingTimeMinutes: time,
      label_en: "Medium",
      label_mm: "အလယ်အလတ်",
      badgeColor: "text-amber-700 border-amber-300",
      badgeBg: "bg-amber-50",
    };
  } else {
    return {
      difficulty: "hard",
      cookingTimeMinutes: time,
      label_en: "Hard",
      label_mm: "အချိန်ယူရ",
      badgeColor: "text-rose-700 border-rose-300",
      badgeBg: "bg-rose-50",
    };
  }
}

