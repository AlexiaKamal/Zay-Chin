"use client";

import React, { useState } from "react";
import Link from "next/link";
import { RecipeSummary } from "@/types";
import { useApp } from "@/context/AppContext";
import {
  ClockIcon,
  UsersIcon,
  CoinsIcon,
  CheckIcon,
  PlusIcon,
  CookingPotIcon,
} from "@/components/ui/Icons";
import recipeImagesData from "@/data/recipe_images.json";
import { computeRecipeDifficulty } from "@/lib/recipe-difficulty";

interface RecipeImageEntry {
  image_url: string;
  source_name?: string;
  license?: string;
  caption?: string;
}

const recipeImages: Record<string, RecipeImageEntry> = recipeImagesData as any;

export function RecipeCard({
  recipe,
  showImage = false,
}: {
  recipe: RecipeSummary;
  showImage?: boolean;
}) {
  const { language, t } = useApp();
  const [imgError, setImgError] = useState(false);
  const [addedToPlan, setAddedToPlan] = useState(false);

  const primaryName = language === "mm" ? recipe.name_mm : recipe.name_en;
  const secondaryName = language === "mm" ? recipe.name_en : recipe.name_mm;

  // Format MMK cost
  const formattedCost = recipe.estimated_cost_mmk
    ? Math.round(recipe.estimated_cost_mmk).toLocaleString()
    : "—";

  // Difficulty & Cooking Time calculation
  const diffInfo = computeRecipeDifficulty(recipe);

  // Verified Image
  const imgInfo = recipeImages[recipe.id];
  const imgSrc = showImage && imgInfo && !imgError ? imgInfo.image_url : null;

  // Add directly to weekly planner & sync grocery list
  const handleAddToPlan = (e: React.MouseEvent) => {
    e.preventDefault();
    e.stopPropagation();

    // 1. Update grocery list recipes
    const savedRecipesRaw = localStorage.getItem("zaychin_grocery_recipes");
    let currentIds: string[] = [];
    try {
      currentIds = savedRecipesRaw ? JSON.parse(savedRecipesRaw) : [];
      if (!Array.isArray(currentIds)) currentIds = [];
    } catch {
      currentIds = [];
    }

    if (!currentIds.includes(recipe.id)) {
      currentIds.push(recipe.id);
      localStorage.setItem("zaychin_grocery_recipes", JSON.stringify(currentIds));
    }

    // 2. Update weekly plan schedule if stored
    const savedPlanRaw = localStorage.getItem("zaychin_weekly_plan");
    if (savedPlanRaw) {
      try {
        const parsed = JSON.parse(savedPlanRaw);
        if (parsed && Array.isArray(parsed.schedule)) {
          parsed.schedule.push({
            day_of_week: (parsed.schedule.length % 7) + 1,
            meal_type: "dinner",
            recipe_id: recipe.id,
            recipe_name_en: recipe.name_en,
            recipe_name_mm: recipe.name_mm,
            category: recipe.category,
            estimated_cost_mmk: recipe.estimated_cost_mmk || 2500,
            calories_kcal: recipe.calories_kcal_per_serving || 280,
            protein_g: recipe.protein_g_per_serving || 14,
          });
          localStorage.setItem("zaychin_weekly_plan", JSON.stringify(parsed));
        }
      } catch {}
    }

    // 3. Dispatch storage event so all pages sync immediately
    if (typeof window !== "undefined") {
      window.dispatchEvent(
        new CustomEvent("zaychin_recipes_updated", {
          detail: { recipeIds: currentIds },
        })
      );
    }

    setAddedToPlan(true);
    setTimeout(() => setAddedToPlan(false), 2200);
  };

  return (
    <div className="bg-white rounded-3xl border border-stone-200/90 shadow-xs hover:shadow-lg hover:border-[var(--color-primary)] transition-all duration-300 flex flex-col justify-between overflow-hidden group hover:-translate-y-1">
      {/* Authentic Picture (Only rendered when showImage is explicitly true) */}
      {imgSrc && (
        <div className="relative aspect-[16/10] w-full overflow-hidden bg-stone-100">
          <img
            src={imgSrc}
            alt={primaryName}
            onError={() => setImgError(true)}
            className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
            loading="lazy"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-transparent pointer-events-none" />
          
          <div className="absolute bottom-2.5 left-2.5 right-2.5 flex items-center justify-between text-white pointer-events-none text-[10px]">
            <span className="bg-black/60 backdrop-blur-xs px-2 py-0.5 rounded-md font-bold">
              📸 {imgInfo?.source_name?.split("/")[0]?.trim() || "Wikimedia"}
            </span>
            <span className="bg-[var(--color-primary)] px-2 py-0.5 rounded-md font-extrabold shadow-2xs">
              Authentic
            </span>
          </div>
        </div>
      )}

      {/* Card Body */}
      <div className="p-5 space-y-3.5 flex-1 flex flex-col justify-between">
        <div className="space-y-3">
          {/* Category & Difficulty Tier */}
          <div className="flex items-center justify-between gap-2 flex-wrap">
            <span className="px-2.5 py-1 rounded-lg text-xs font-semibold bg-stone-100 text-stone-700">
              {recipe.category}
            </span>

            {/* Easy / Medium / Hard Badge with Cooking Time */}
            <span
              className={`inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-bold border ${diffInfo.badgeBg} ${diffInfo.badgeColor}`}
            >
              <ClockIcon className="w-3 h-3" />
              <span>
                {language === "mm" ? diffInfo.label_mm : diffInfo.label_en} ({diffInfo.cookingTimeMinutes}m)
              </span>
            </span>
          </div>

          {/* Titles */}
          <div>
            <Link href={`/recipes/${recipe.id}`} className="block">
              <h3 className="text-base sm:text-lg font-bold text-stone-900 group-hover:text-[var(--color-primary)] transition-colors line-clamp-1">
                {primaryName}
              </h3>
            </Link>
            <p className="text-xs text-stone-500 font-medium line-clamp-1 mt-0.5">
              {secondaryName}
            </p>
          </div>
        </div>

        {/* Cost & Servings */}
        <div className="space-y-3 pt-2">
          <div className="p-2.5 rounded-2xl bg-stone-50 border border-stone-100 flex items-center justify-between">
            <div className="flex items-center gap-1.5 text-xs text-stone-600">
              <CoinsIcon className="w-4 h-4 text-[var(--color-primary)]" />
              <span className="font-medium">{t.est_cost_label}:</span>
            </div>
            <div>
              <span className="text-sm sm:text-base font-extrabold text-[var(--color-primary)]">
                {formattedCost}
              </span>
              <span className="text-xs font-semibold text-stone-500 ml-1">MMK</span>
            </div>
          </div>

          <div className="flex items-center justify-between text-xs text-stone-500 px-1">
            <div className="flex items-center gap-1">
              <UsersIcon className="w-3.5 h-3.5 text-stone-400" />
              <span>{recipe.servings || 4} {language === "mm" ? "ဦးစာ" : "servings"}</span>
            </div>
            {recipe.calories_kcal_per_serving && (
              <span className="text-[11px] font-medium text-stone-500">
                {Math.round(recipe.calories_kcal_per_serving)} kcal
              </span>
            )}
          </div>
        </div>
      </div>

      {/* Actions: View Recipe & Add to Weekly Planner */}
      <div className="p-3 bg-stone-50/80 border-t border-stone-100 grid grid-cols-2 gap-2 text-xs font-bold">
        <Link
          href={`/recipes/${recipe.id}`}
          className="py-2 px-3 rounded-xl text-center border border-stone-200 bg-white text-stone-700 hover:bg-stone-50 transition-colors"
        >
          {t.btn_view_recipe}
        </Link>

        <button
          type="button"
          onClick={handleAddToPlan}
          className={`py-2 px-3 rounded-xl text-center flex items-center justify-center gap-1 transition-all ${
            addedToPlan
              ? "bg-emerald-600 text-white shadow-xs"
              : "text-white shadow-xs active:scale-95"
          }`}
          style={!addedToPlan ? { backgroundColor: "var(--color-primary)" } : {}}
        >
          {addedToPlan ? (
            <>
              <CheckIcon className="w-3.5 h-3.5 text-white" />
              <span>{language === "mm" ? "ထည့်ပြီး ✓" : "Added ✓"}</span>
            </>
          ) : (
            <>
              <PlusIcon className="w-3.5 h-3.5" />
              <span>{language === "mm" ? "+ ဇယားသို့" : "+ To Plan"}</span>
            </>
          )}
        </button>
      </div>
    </div>
  );
}
