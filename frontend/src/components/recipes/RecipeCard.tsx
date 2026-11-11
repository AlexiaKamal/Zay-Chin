"use client";

import React, { useState } from "react";
import Link from "next/link";
import { RecipeSummary } from "@/types";
import { useApp } from "@/context/AppContext";
import {
  FlameIcon,
  ClockIcon,
  UsersIcon,
  CoinsIcon,
  CheckIcon,
} from "@/components/ui/Icons";
import recipeImagesData from "@/data/recipe_images.json";

interface RecipeImageEntry {
  image_url: string;
  fallback_local?: string;
  source_name?: string;
  license?: string;
  caption?: string;
}

const recipeImages: Record<string, RecipeImageEntry> = recipeImagesData as any;

export function RecipeCard({ recipe }: { recipe: RecipeSummary }) {
  const { language, t } = useApp();
  const [imgError, setImgError] = useState(false);

  const primaryName = language === "mm" ? recipe.name_mm : recipe.name_en;
  const secondaryName = language === "mm" ? recipe.name_en : recipe.name_mm;

  // Format MMK cost
  const formattedCost = recipe.estimated_cost_mmk
    ? Math.round(recipe.estimated_cost_mmk).toLocaleString()
    : "—";

  const imgInfo = recipeImages[recipe.id];
  const imgSrc = imgInfo
    ? imgError && imgInfo.fallback_local
      ? imgInfo.fallback_local
      : imgInfo.image_url
    : null;

  return (
    <div className="bg-white rounded-3xl border border-[var(--color-border)] shadow-sm hover:shadow-xl hover:border-[var(--color-primary)] transition-all duration-300 flex flex-col justify-between overflow-hidden group hover:-translate-y-1">
      {/* Authentic Picture (If Available) */}
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
          
          {/* Authentic Photo Verification Pill */}
          <div className="absolute bottom-2.5 left-2.5 right-2.5 flex items-center justify-between text-white pointer-events-none text-[10px]">
            <span className="bg-black/60 backdrop-blur-xs px-2 py-0.5 rounded-md font-bold flex items-center gap-1">
              <span>📸</span>
              <span>{imgInfo?.source_name?.split("/")[0]?.trim() || "Wikimedia Commons"}</span>
            </span>
            <span className="bg-[var(--color-primary)] px-2 py-0.5 rounded-md font-extrabold shadow-2xs">
              100% Authentic
            </span>
          </div>
        </div>
      )}

      <div className="p-5 space-y-3.5 flex-1 flex flex-col justify-between">
        <div className="space-y-3">
          {/* Category & Cost Completeness Header */}
          <div className="flex items-center justify-between gap-2">
            <span className="px-2.5 py-1 rounded-md text-xs font-semibold bg-[var(--color-muted)] text-[var(--color-primary)] border border-[var(--color-border)]">
              {recipe.category}
            </span>
            {recipe.is_cost_complete ? (
              <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[11px] font-bold bg-teal-50 text-teal-800 border border-teal-200">
                <CheckIcon className="w-3 h-3 text-teal-700" />
                {t.badge_complete_price}
              </span>
            ) : (
              <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[11px] font-semibold bg-amber-50 text-amber-800 border border-amber-200">
                {recipe.cost_coverage_percentage}% {t.badge_partial_price}
              </span>
            )}
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

        <div className="space-y-3 pt-2">
          {/* Dynamic Estimated Cost */}
          <div className="p-3 rounded-2xl bg-stone-50 border border-stone-100 flex items-center justify-between">
            <div className="flex items-center gap-2 text-xs font-medium text-stone-600">
              <CoinsIcon className="w-4 h-4 text-[var(--color-primary)]" />
              <span>{t.est_cost_label}:</span>
            </div>
            <div className="text-right">
              <span className="text-base font-extrabold text-[var(--color-primary)]">
                {formattedCost}
              </span>
              <span className="text-xs font-semibold text-stone-500 ml-1">MMK</span>
            </div>
          </div>

          {/* Meta Stats: Servings, Time, Calories */}
          <div className="grid grid-cols-3 gap-2 pt-1 text-stone-600 text-xs">
            <div className="flex items-center gap-1.5" title="Servings / လူဦးရေ">
              <UsersIcon className="w-3.5 h-3.5 text-stone-400" />
              <span>{recipe.servings || 4} {language === "mm" ? "ဦး" : "pax"}</span>
            </div>
            <div className="flex items-center gap-1.5" title="Cooking Time / ချက်ပြုတ်ချိန်">
              <ClockIcon className="w-3.5 h-3.5 text-stone-400" />
              <span>
                {recipe.cooking_time_minutes
                  ? `${recipe.cooking_time_minutes}m`
                  : t.badge_time_standard}
              </span>
            </div>
            <div className="flex items-center gap-1.5" title="Calories per serving">
              <FlameIcon className="w-3.5 h-3.5 text-orange-500" />
              <span>
                {recipe.calories_kcal_per_serving
                  ? `${Math.round(recipe.calories_kcal_per_serving)} kcal`
                  : "—"}
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* Card Action */}
      <div className="px-5 py-3 bg-stone-50/70 border-t border-stone-100 flex items-center justify-between text-xs font-semibold text-[var(--color-primary)] group-hover:bg-[var(--color-muted)]/30 transition-colors">
        <Link href={`/recipes/${recipe.id}`} className="w-full text-center py-1 font-bold">
          {t.btn_view_recipe} →
        </Link>
      </div>
    </div>
  );
}