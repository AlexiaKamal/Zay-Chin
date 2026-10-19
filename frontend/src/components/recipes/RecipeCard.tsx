"use client";

import React from "react";
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

export function RecipeCard({ recipe }: { recipe: RecipeSummary }) {
  const { language, t } = useApp();

  const primaryName = language === "mm" ? recipe.name_mm : recipe.name_en;
  const secondaryName = language === "mm" ? recipe.name_en : recipe.name_mm;

  // Format MMK cost
  const formattedCost = recipe.estimated_cost_mmk
    ? Math.round(recipe.estimated_cost_mmk).toLocaleString()
    : "—";

  return (
    <div className="bg-white rounded-2xl border border-stone-200 shadow-xs hover:shadow-md hover:border-emerald-300 transition-all flex flex-col justify-between overflow-hidden group">
      <div className="p-5 space-y-3.5">
        {/* Category & Cost Completeness Header */}
        <div className="flex items-center justify-between gap-2">
          <span className="px-2.5 py-1 rounded-md text-xs font-semibold bg-emerald-50 text-emerald-800 border border-emerald-100">
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
            <h3 className="text-lg font-bold text-stone-900 group-hover:text-emerald-700 transition-colors line-clamp-1">
              {primaryName}
            </h3>
          </Link>
          <p className="text-xs text-stone-500 font-medium line-clamp-1 mt-0.5">
            {secondaryName}
          </p>
        </div>

        {/* Dynamic Estimated Cost */}
        <div className="p-3 rounded-xl bg-stone-50 border border-stone-100 flex items-center justify-between">
          <div className="flex items-center gap-2 text-xs font-medium text-stone-600">
            <CoinsIcon className="w-4 h-4 text-emerald-700" />
            <span>{t.est_cost_label}:</span>
          </div>
          <div className="text-right">
            <span className="text-base font-extrabold text-emerald-800">
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

      {/* Card Action */}
      <div className="px-5 py-3 bg-stone-50/70 border-t border-stone-100 flex items-center justify-between text-xs font-semibold text-emerald-800 group-hover:bg-emerald-50 transition-colors">
        <Link href={`/recipes/${recipe.id}`} className="w-full text-center py-1">
          {t.btn_view_recipe} →
        </Link>
      </div>
    </div>
  );
}
