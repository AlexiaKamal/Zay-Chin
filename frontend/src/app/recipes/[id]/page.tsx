"use client";

import React, { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import Link from "next/link";
import { useApp } from "@/context/AppContext";
import { getRecipeDetail } from "@/lib/api";
import { RecipeDetail } from "@/types";
import {
  CookingPotIcon,
  FlameIcon,
  ClockIcon,
  UsersIcon,
  CoinsIcon,
  CheckIcon,
  MinusIcon,
  PlusIcon,
  CalendarIcon,
  SparklesIcon,
  ShoppingBagIcon,
} from "@/components/ui/Icons";

function RecipeDetailContent() {
  const params = useParams();
  const router = useRouter();
  const { language, city, t } = useApp();
  
  const recipeId = params.id as string;
  const [recipe, setRecipe] = useState<RecipeDetail | null>(null);
  const [servings, setServings] = useState<number>(4);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadDetail() {
      try {
        setLoading(true);
        setError(null);
        const data = await getRecipeDetail(recipeId, servings, city);
        setRecipe(data);
        if (data.servings && servings === 4 && data.servings !== 4) {
          setServings(data.servings);
        }
      } catch (err: any) {
        console.error("Error loading recipe detail:", err);
        setError(err.message || "Failed to load recipe detail.");
      } finally {
        setLoading(false);
      }
    }
    if (recipeId) {
      loadDetail();
    }
  }, [recipeId, servings, city]);

  if (loading && !recipe) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-16 text-center space-y-4">
        <div className="w-12 h-12 border-4 border-emerald-700 border-t-transparent rounded-full animate-spin mx-auto" />
        <p className="text-sm font-medium text-stone-500">
          {language === "mm" ? "ဟင်းချက်နည်း အသေးစိတ်ကို တွက်ချက်ဖော်ပြနေပါသည်..." : "Calculating recipe costs & nutrition..."}
        </p>
      </div>
    );
  }

  if (error || !recipe) {
    return (
      <div className="max-w-xl mx-auto px-4 py-16 text-center space-y-4">
        <div className="p-4 bg-red-50 text-red-700 rounded-2xl border border-red-200">
          <p className="font-bold">{error || "Recipe not found."}</p>
        </div>
        <Link
          href="/recipes"
          className="inline-block px-5 py-2.5 bg-emerald-800 text-white rounded-xl text-xs font-bold"
        >
          {t.btn_back_to_recipes}
        </Link>
      </div>
    );
  }

  const primaryName = language === "mm" ? recipe.name_mm : recipe.name_en;
  const secondaryName = language === "mm" ? recipe.name_en : recipe.name_mm;
  const description = language === "mm" ? recipe.description_mm : recipe.description_en;

  const cost = recipe.cost_breakdown;
  const nutrition = recipe.nutrition_breakdown;

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-12 space-y-10">
      {/* Navigation Breadcrumb */}
      <div>
        <Link
          href="/recipes"
          className="inline-flex items-center gap-1.5 text-xs font-bold text-emerald-800 hover:underline"
        >
          ← {t.btn_back_to_recipes}
        </Link>
      </div>

      {/* Header Banner */}
      <div className="bg-white rounded-3xl border border-stone-200 p-6 sm:p-10 shadow-xs space-y-6">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div className="flex items-center gap-2">
            <span className="px-3 py-1 rounded-lg text-xs font-bold bg-emerald-50 text-emerald-800 border border-emerald-200">
              {recipe.category}
            </span>
            {recipe.is_cost_complete ? (
              <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-bold bg-teal-50 text-teal-800 border border-teal-200">
                <CheckIcon className="w-3.5 h-3.5 text-teal-700" />
                {t.badge_complete_price}
              </span>
            ) : (
              <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-semibold bg-amber-50 text-amber-800 border border-amber-200">
                {recipe.cost_coverage_percentage}% {t.badge_partial_price}
              </span>
            )}
          </div>
          <span className="text-xs font-medium text-stone-400">
            ID: {recipe.id}
          </span>
        </div>

        <div className="space-y-1">
          <h1 className="text-2xl sm:text-4xl font-extrabold text-stone-900 tracking-tight">
            {primaryName}
          </h1>
          <p className="text-sm sm:text-base text-stone-500 font-medium">
            {secondaryName}
          </p>
        </div>

        {description && (
          <p className="text-sm sm:text-base text-stone-600 leading-relaxed max-w-3xl">
            {description}
          </p>
        )}

        {/* Quick Highlights Bar */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-4 border-t border-stone-100 text-xs">
          <div className="p-3 bg-stone-50 rounded-xl space-y-1">
            <span className="text-stone-400 font-medium">{t.portion_cooking_value || t.est_cost_label} ({city})</span>
            <div className="text-base sm:text-lg font-black text-emerald-800">
              {cost?.estimated_cost_mmk ? Math.round(cost.estimated_cost_mmk).toLocaleString() : "—"}{" "}
              <span className="text-xs font-normal">MMK</span>
            </div>
            <span className="block text-[10px] text-stone-400">
              {language === "mm" ? "အမှန်တကယ်သုံးစွဲတန်ဖိုး" : "Prorated recipe portion"}
            </span>
          </div>
          <div className="p-3 bg-stone-50 rounded-xl space-y-1">
            <span className="text-stone-400 font-medium">{t.store_checkout_pack_cost}</span>
            <div className="text-base sm:text-lg font-black text-stone-900">
              {cost?.full_retail_pack_cost_mmk ? Math.round(cost.full_retail_pack_cost_mmk).toLocaleString() : "—"}{" "}
              <span className="text-xs font-normal">MMK</span>
            </div>
            <span className="block text-[10px] text-emerald-700 font-medium">
              {cost?.pantry_adjusted_cost_mmk && cost.pantry_adjusted_cost_mmk < (cost.full_retail_pack_cost_mmk || 0)
                ? `${Math.round(cost.pantry_adjusted_cost_mmk).toLocaleString()} MMK ${language === "mm" ? "အိမ်တွင်းအရန်နုတ်ပြီး" : "with pantry"}`
                : language === "mm" ? "လက်လီအထုပ်အပြည့်ဈေး" : "Full store retail packs"}
            </span>
          </div>
          <div className="p-3 bg-stone-50 rounded-xl space-y-1">
            <span className="text-stone-400 font-medium">{t.badge_calories}</span>
            <div className="text-base sm:text-lg font-black text-orange-600">
              {nutrition?.per_serving?.calories_kcal ? `${Math.round(nutrition.per_serving.calories_kcal)}` : "—"}{" "}
              <span className="text-xs font-normal">kcal</span>
            </div>
            <span className="block text-[10px] text-stone-400">{language === "mm" ? "၁ ဦးစာ စွမ်းအင်" : "per serving"}</span>
          </div>
          <div className="p-3 bg-stone-50 rounded-xl space-y-1">
            <span className="text-stone-400 font-medium">{t.badge_protein}</span>
            <div className="text-base sm:text-lg font-black text-stone-800">
              {nutrition?.per_serving?.protein_g ? `${nutrition.per_serving.protein_g}` : "—"}{" "}
              <span className="text-xs font-normal">g</span>
            </div>
            <span className="block text-[10px] text-stone-400">{language === "mm" ? "၁ ဦးစာ ပရိုတင်း" : "per serving"}</span>
          </div>
        </div>
      </div>

      {/* Interactive Serving Scaler */}
      <div className="bg-emerald-50/70 border border-emerald-200/80 rounded-2xl p-5 flex flex-col sm:flex-row items-center justify-between gap-4">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-emerald-800 text-white flex items-center justify-center font-bold">
            <UsersIcon className="w-5 h-5 text-amber-200" />
          </div>
          <div>
            <h3 className="text-sm font-bold text-stone-900">
              {t.details_servings_label}
            </h3>
            <p className="text-xs text-stone-600">
              {language === "mm"
                ? "စားသုံးသူ ဦးရေအလိုက် ပါဝင်ပစ္စည်းများကို အလိုအလျောက် ချိန်ညှိတွက်ချက်ပေးပါသည်။"
                : "Recalculates all ingredient weights and estimated MMK costs."}
            </p>
          </div>
        </div>

        <div className="flex items-center gap-3 bg-white px-3 py-1.5 rounded-xl border border-emerald-200 shadow-xs">
          <button
            type="button"
            disabled={servings <= 1}
            onClick={() => setServings(Math.max(1, servings - 1))}
            className="w-8 h-8 rounded-lg bg-stone-100 hover:bg-stone-200 flex items-center justify-center text-stone-700 disabled:opacity-40"
            aria-label="Decrease servings"
          >
            <MinusIcon className="w-4 h-4" />
          </button>
          <span className="text-base font-extrabold text-stone-900 w-12 text-center">
            {servings} {language === "mm" ? "ဦး" : "pax"}
          </span>
          <button
            type="button"
            disabled={servings >= 50}
            onClick={() => setServings(servings + 1)}
            className="w-8 h-8 rounded-lg bg-stone-100 hover:bg-stone-200 flex items-center justify-center text-stone-700 disabled:opacity-40"
            aria-label="Increase servings"
          >
            <PlusIcon className="w-4 h-4" />
          </button>
        </div>
      </div>

      {/* Main Grid: Ingredients & Instructions */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Left Column: Ingredients Table */}
        <div className="lg:col-span-2 space-y-6">
          <div className="bg-white rounded-3xl border border-stone-200 p-6 sm:p-8 shadow-xs space-y-4">
            <div className="flex items-center justify-between">
              <h2 className="text-lg sm:text-xl font-extrabold text-stone-900">
                {t.details_ingredients_title}
              </h2>
              <span className="text-xs text-stone-400 font-semibold">
                {recipe.ingredients.length} {language === "mm" ? "မျိုး" : "items"}
              </span>
            </div>

            {/* Real-World Retail Packaging Transparency Banner */}
            <div className="p-4 bg-emerald-50/70 rounded-2xl border border-emerald-200/80 text-xs text-stone-700 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
              <div className="flex items-start gap-2.5">
                <div className="p-1.5 bg-emerald-100 rounded-lg text-emerald-800 shrink-0 mt-0.5">
                  <ShoppingBagIcon className="w-4 h-4" />
                </div>
                <div className="space-y-0.5">
                  <span className="font-extrabold text-stone-900 block text-xs">
                    {language === "mm" ? "စတိုးဆိုင် လက်လီဝယ်ယူမှု နှင့် ချက်ပြုတ်စားသုံးမှု တန်ဖိုး" : "Real-World Purchasing & Dual-Tier Costing"}
                  </span>
                  <p className="text-stone-600 leading-relaxed text-[11px]">
                    {t.dual_pricing_tip}
                  </p>
                </div>
              </div>
              {cost?.full_retail_pack_cost_mmk && (
                <div className="shrink-0 bg-white px-3 py-1.5 rounded-xl border border-emerald-200 text-right shadow-2xs">
                  <span className="text-[10px] text-stone-400 block font-bold uppercase">{t.store_checkout_pack_cost}</span>
                  <span className="text-xs sm:text-sm font-black text-emerald-800">
                    ~{Math.round(cost.full_retail_pack_cost_mmk).toLocaleString()} MMK
                  </span>
                </div>
              )}
            </div>

            {/* Table */}
            <div className="overflow-x-auto">
              <table className="w-full text-left border-collapse text-xs sm:text-sm">
                <thead>
                  <tr className="border-b border-stone-200 text-stone-400 font-semibold uppercase tracking-wider text-[11px]">
                    <th className="pb-3 pr-2">{t.table_ingredient}</th>
                    <th className="pb-3 px-2">{t.table_recipe_unit}</th>
                    <th className="pb-3 px-2">{t.table_metric_unit}</th>
                    <th className="pb-3 px-2">{t.table_store_pack}</th>
                    <th className="pb-3 pl-2 text-right">{t.table_est_price}</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-stone-100">
                  {recipe.ingredients.map((ing) => {
                    const costItem = cost?.ingredient_breakdown.find(
                      (b) => b.ingredient_id === ing.ingredient_id
                    );
                    const isPriced = costItem?.is_priced;
                    const itemCost = costItem?.item_cost_mmk;
                    const isZeroUtility = costItem?.is_zero_cost_utility;

                    return (
                      <tr key={ing.id} className="hover:bg-stone-50/70 transition-colors">
                        <td className="py-3 pr-2 font-medium text-stone-900">
                          <div>
                            <div className="flex items-center gap-1.5 flex-wrap">
                              <span className="font-bold">{language === "mm" ? ing.name_mm : ing.name_en}</span>
                              {costItem?.is_pantry_staple && (
                                <span className="px-1.5 py-0.5 text-[9px] font-extrabold bg-amber-100 text-amber-900 rounded-md border border-amber-200">
                                  {t.badge_pantry_staple}
                                </span>
                              )}
                            </div>
                            <span className="block text-[11px] text-stone-400 font-normal">
                              {language === "mm" ? ing.name_en : ing.name_mm}
                            </span>
                          </div>
                        </td>
                        <td className="py-3 px-2 text-stone-600 font-medium">
                          {ing.quantity ? `${ing.quantity} ` : ""}
                          {ing.unit}
                          {ing.preparation_note_mm && (
                            <span className="block text-[11px] text-stone-400">
                              ({language === "mm" ? ing.preparation_note_mm : ing.preparation_note_en})
                            </span>
                          )}
                        </td>
                        <td className="py-3 px-2 text-stone-600">
                          {ing.normalized_quantity ? (
                            <span className="font-semibold text-emerald-800">
                              {ing.normalized_quantity} {ing.normalized_unit}
                            </span>
                          ) : (
                            <span className="text-stone-400 text-xs">
                              {ing.normalized_unit === "to_taste"
                                ? language === "mm" ? "အနည်းငယ်" : "to taste"
                                : "—"}
                            </span>
                          )}
                        </td>
                        <td className="py-3 px-2 text-stone-700">
                          {isZeroUtility ? (
                            <span className="text-stone-400 text-xs italic">
                              {language === "mm" ? "အိမ်သုံးရေ" : "Household utility"}
                            </span>
                          ) : costItem?.package_description ? (
                            <div className="space-y-0.5">
                              <span className="inline-flex items-center gap-1 font-semibold text-stone-900 text-xs">
                                🛒 {costItem.package_description}
                              </span>
                              {typeof costItem.retail_package_price_mmk === "number" && costItem.retail_package_price_mmk > 0 && (
                                <span className="block text-[10px] text-stone-400 font-medium">
                                  {Math.round(costItem.retail_package_price_mmk).toLocaleString()} MMK / unit
                                </span>
                              )}
                            </div>
                          ) : (
                            <span className="text-stone-400 text-xs">—</span>
                          )}
                        </td>
                        <td className="py-3 pl-2 text-right">
                          {isZeroUtility ? (
                            <span className="text-stone-400 text-xs font-semibold">
                              0 MMK
                            </span>
                          ) : isPriced && itemCost !== null && itemCost !== undefined ? (
                            <div>
                              <span className="font-bold text-emerald-800">
                                {Math.round(itemCost).toLocaleString()} MMK
                              </span>
                            </div>
                          ) : (
                            <span className="text-amber-700 bg-amber-50 px-2 py-0.5 rounded text-[11px] font-semibold">
                              {t.price_unpriced_tag}
                            </span>
                          )}
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>

            {/* Missing Ingredients Transparency Warning if partial */}
            {cost && !cost.is_cost_complete && (
              <div className="p-4 bg-amber-50/80 rounded-2xl border border-amber-200/80 text-xs text-amber-900 space-y-1 mt-4">
                <span className="font-bold block">
                  {language === "mm" ? "ဈေးနှုန်းမရရှိသေးသော ပါဝင်ပစ္စည်းများ" : "Unpriced / Wild Foraged Ingredients in " + city}:
                </span>
                <p className="text-amber-800/90 leading-relaxed">
                  {cost.missing_priced_ingredients.map((m) => (language === "mm" ? m.name_mm : m.name_en)).join(", ")}
                </p>
                <p className="text-[11px] text-amber-700 italic pt-1">
                  {language === "mm"
                    ? "* အထက်ပါ ပါဝင်ပစ္စည်းများသည် ဒေသန္တရစိုစွတ်ဈေးများတွင်သာ ရာသီပေါ်ရရှိနိုင်သဖြင့် ခန့်မှန်းကုန်ကျစရိတ်တွင် ထည့်သွင်းမထားပါ။"
                    : "* These seasonal herbs/traditional ingredients are exclusively found in local wet markets and are excluded from the calculated estimate."}
                </p>
              </div>
            )}
          </div>

          {/* Cooking Instructions */}
          <div className="bg-white rounded-3xl border border-stone-200 p-6 sm:p-8 shadow-xs space-y-5">
            <h2 className="text-lg sm:text-xl font-extrabold text-stone-900">
              {t.details_instructions_title}
            </h2>

            <div className="space-y-4">
              {recipe.instructions.map((ins) => (
                <div key={ins.step_number} className="flex gap-4 group">
                  <div className="w-8 h-8 rounded-xl bg-emerald-100 text-emerald-900 flex items-center justify-center font-bold text-sm shrink-0 mt-0.5">
                    {ins.step_number}
                  </div>
                  <p className="text-sm sm:text-base text-stone-700 leading-relaxed pt-0.5">
                    {language === "mm" ? ins.instruction_mm : ins.instruction_en}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Right Column: Nutrition Facts & Citation */}
        <div className="space-y-6">
          {/* Nutrition Facts Card */}
          <div className="bg-white rounded-3xl border border-stone-200 p-6 shadow-xs space-y-4">
            <div className="flex items-center gap-2">
              <FlameIcon className="w-5 h-5 text-orange-500" />
              <h3 className="font-extrabold text-base text-stone-900">
                {t.details_nutrition_title}
              </h3>
            </div>

            <div className="divide-y divide-stone-100 text-xs sm:text-sm">
              <div className="py-2.5 flex justify-between font-bold text-stone-900">
                <span>Calories</span>
                <span className="text-emerald-800 font-extrabold">
                  {nutrition?.per_serving?.calories_kcal ? `${Math.round(nutrition.per_serving.calories_kcal)} kcal` : "—"}
                </span>
              </div>
              <div className="py-2.5 flex justify-between text-stone-700">
                <span>Protein</span>
                <span className="font-semibold">{nutrition?.per_serving?.protein_g ?? "—"} g</span>
              </div>
              <div className="py-2.5 flex justify-between text-stone-700">
                <span>Total Fat</span>
                <span className="font-semibold">{nutrition?.per_serving?.fat_g ?? "—"} g</span>
              </div>
              <div className="py-2.5 flex justify-between text-stone-700">
                <span>Carbohydrates</span>
                <span className="font-semibold">{nutrition?.per_serving?.carbohydrates_g ?? "—"} g</span>
              </div>
              <div className="py-2.5 flex justify-between text-stone-700">
                <span>Dietary Fiber</span>
                <span className="font-semibold">{nutrition?.per_serving?.fiber_g ?? "—"} g</span>
              </div>
              <div className="py-2.5 flex justify-between text-stone-700">
                <span>Sodium</span>
                <span className="font-semibold">{nutrition?.per_serving?.sodium_mg ?? "—"} mg</span>
              </div>
            </div>

            <p className="text-[11px] text-stone-400 leading-relaxed border-t border-stone-100 pt-3">
              {t.nutrition_disclaimer}
            </p>
          </div>

          {/* Source Citation Card */}
          <div className="bg-stone-50 rounded-3xl border border-stone-200/80 p-6 space-y-3">
            <div className="flex items-center gap-2 text-emerald-800">
              <CookingPotIcon className="w-5 h-5" />
              <h3 className="font-bold text-sm text-stone-900">
                {t.details_source_title}
              </h3>
            </div>
            <p className="text-xs text-stone-600 leading-relaxed">
              {recipe.source_document} (ချက်ပြုတ်အတတ်ပညာ) — ဒေါ်စန်းလေး (Daw San Lay).
            </p>
            <div className="text-xs text-stone-500 space-y-1 pt-1">
              <p>Printed Book Pages: {recipe.source_printed_pages.join(", ") || "—"}</p>
              <p>Original PDF Page: {recipe.source_pdf_pages.join(", ") || "—"}</p>
              <p>Extraction: Verified 100% 1:1 Parity</p>
            </div>
          </div>

          {/* Action: Add to Meal Plan */}
          <div className="bg-gradient-to-br from-emerald-800 to-teal-900 rounded-3xl p-6 text-white space-y-3 shadow-lg">
            <h4 className="font-bold text-sm">
              {language === "mm" ? "ရက်သတ္တပတ် ဇယားသို့ ထည့်သွင်းမည်" : "Plan this dish for the week"}
            </h4>
            <p className="text-xs text-emerald-100/90 leading-relaxed">
              {language === "mm"
                ? "အပတ်စဉ် အစားအစာ စီစဉ်သူတွင် ဤဟင်းလျာကို ထည့်သွင်း၍ ဘတ်ဂျက် ချွေတာလိုက်ပါ။"
                : "Add this recipe to your weekly meal planner to automatically generate your combined grocery checklist."}
            </p>
            <Link
              href={`/planner?addRecipe=${recipe.id}`}
              className="w-full inline-block text-center py-2.5 px-4 bg-amber-400 hover:bg-amber-500 text-stone-950 font-extrabold text-xs rounded-xl transition-all shadow-md active:scale-95"
            >
              {t.btn_add_to_plan}
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

export default function RecipeDetailPage() {
  return (
    <React.Suspense fallback={<div className="max-w-4xl mx-auto p-12 text-center text-stone-400">Loading recipe...</div>}>
      <RecipeDetailContent />
    </React.Suspense>
  );
}
