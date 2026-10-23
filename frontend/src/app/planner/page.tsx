"use client";

import React, { Suspense, useState, useEffect } from "react";
import Link from "next/link";
import { useRouter, useSearchParams } from "next/navigation";
import { useApp } from "@/context/AppContext";
import { 
  CalendarIcon, 
  SparklesIcon, 
  CookingPotIcon, 
  CoinsIcon, 
  ScaleIcon, 
  SearchIcon,
  CheckCircleIcon
} from "@/components/ui/Icons";
import { generateMealPlan, getMealReplacementOptions } from "@/lib/api";
import { MealPlanGenerateResponse, MealSlotRecommendation, ReplacementOption } from "@/types";

const DAYS_EN = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
const DAYS_MM = ["တနင်္လာ", "အင်္ဂါ", "ဗုဒ္ဓဟူး", "ကြာသပတေး", "သောကြာ", "စနေ", "တနင်္ဂနွေ"];

function PlannerContent() {
  const { language, city, setCity, t } = useApp();
  const router = useRouter();
  const searchParams = useSearchParams();
  const addRecipeParam = searchParams.get("addRecipe");

  // Form State
  const [householdSize, setHouseholdSize] = useState<number>(2);
  const [weeklyBudget, setWeeklyBudget] = useState<number | "">("");
  const [mealsPerDay, setMealsPerDay] = useState<number>(3);
  const [selectedDietary, setSelectedDietary] = useState<string[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [plan, setPlan] = useState<MealPlanGenerateResponse | null>(null);

  // Replacement Modal State
  const [activeSlot, setActiveSlot] = useState<MealSlotRecommendation | null>(null);
  const [replacementCandidates, setReplacementCandidates] = useState<ReplacementOption[]>([]);
  const [loadingReplacements, setLoadingReplacements] = useState<boolean>(false);

  // Initial plan load
  useEffect(() => {
    fetchPlan();
  }, [city]);

  const fetchPlan = async (overrides?: any) => {
    setLoading(true);
    try {
      const budgetNum = weeklyBudget !== "" ? Number(weeklyBudget) : undefined;
      const res = await generateMealPlan({
        city,
        household_size: householdSize,
        weekly_budget_mmk: budgetNum,
        meals_per_day: mealsPerDay,
        dietary_preferences: selectedDietary,
        plan_duration_days: 7,
        ...overrides,
      });
      setPlan(res);
      if (res && res.schedule && res.schedule.length > 0) {
        const uniqueIds = Array.from(new Set(res.schedule.map((s) => s.recipe_id)));
        localStorage.setItem("zaychin_grocery_recipes", JSON.stringify(uniqueIds));
        localStorage.setItem("zaychin_grocery_household", householdSize.toString());
      }
    } catch (err) {
      console.error("Error generating meal plan:", err);
    } finally {
      setLoading(false);
    }
  };

  const handleToggleDietary = (key: string) => {
    setSelectedDietary((prev) =>
      prev.includes(key) ? prev.filter((k) => k !== key) : [...prev, key]
    );
  };

  const openReplaceModal = async (slot: MealSlotRecommendation) => {
    setActiveSlot(slot);
    setLoadingReplacements(true);
    try {
      const candidates = await getMealReplacementOptions({
        city,
        household_size: householdSize,
        day_of_week: slot.day_of_week,
        meal_type: slot.meal_type,
        current_recipe_id: slot.recipe_id,
        dietary_preferences: selectedDietary,
      });
      setReplacementCandidates(candidates);
    } catch (err) {
      console.error("Error fetching replacements:", err);
    } finally {
      setLoadingReplacements(false);
    }
  };

  const applyReplacement = (cand: ReplacementOption) => {
    if (!plan || !activeSlot) return;

    const updatedSchedule = plan.schedule.map((item) => {
      if (item.day_of_week === activeSlot.day_of_week && item.meal_type === activeSlot.meal_type) {
        return {
          ...item,
          recipe_id: cand.recipe_id,
          recipe_name_en: cand.name_en,
          recipe_name_mm: cand.name_mm,
          category: cand.category,
          estimated_cost_mmk: cand.estimated_cost_mmk,
          calories_kcal: cand.calories_kcal,
          protein_g: cand.protein_g,
          is_vegetarian: cand.is_vegetarian,
          is_vegan: cand.is_vegan,
          is_gluten_free: cand.is_gluten_free,
        };
      }
      return item;
    });

    // Recompute total cost
    const newTotal = updatedSchedule.reduce((acc, curr) => acc + curr.estimated_cost_mmk, 0);
    const variance = plan.target_budget_mmk ? plan.target_budget_mmk - newTotal : null;

    setPlan({
      ...plan,
      schedule: updatedSchedule,
      estimated_total_cost_mmk: Math.round(newTotal),
      budget_variance_mmk: variance !== null ? Math.round(variance) : null,
      is_budget_exceeded: variance !== null ? variance < 0 : false,
    });

    // Immediately sync to grocery list localStorage
    const uniqueIds = Array.from(new Set(updatedSchedule.map((s) => s.recipe_id)));
    localStorage.setItem("zaychin_grocery_recipes", JSON.stringify(uniqueIds));
    localStorage.setItem("zaychin_grocery_household", householdSize.toString());

    setActiveSlot(null);
  };

  const handleExportToGroceryList = () => {
    if (!plan) return;
    const uniqueIds = Array.from(new Set(plan.schedule.map((s) => s.recipe_id)));
    localStorage.setItem("zaychin_grocery_recipes", JSON.stringify(uniqueIds));
    localStorage.setItem("zaychin_grocery_household", householdSize.toString());
    router.push(`/grocery-list?household=${householdSize}&recipes=${uniqueIds.join(",")}&updated=${Date.now()}`);
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-8">
      {/* Header */}
      <div className="text-center max-w-3xl mx-auto space-y-3">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 text-xs font-bold">
          <CalendarIcon className="w-4 h-4 text-emerald-700" />
          <span>
            {language === "mm" ? "အပတ်စဉ် အစားအစာ စီစဉ်ရေး စနစ်" : "Intelligent 7-Day Meal Planner"}
          </span>
        </div>
        <h1 className="text-3xl sm:text-4xl font-extrabold text-stone-900 tracking-tight">
          {language === "mm" ? "မိသားစု အစားအစာ စီစဉ်မှုနှင့် ဘတ်ဂျက်" : "Myanmar Household Meal Planning"}
        </h1>
        <p className="text-sm sm:text-base text-stone-600">
          {language === "mm"
            ? "ဒေါ်စန်းလေး၏ မူရင်းဟင်းချက်နည်း ၁၇၁ မျိုးကို ရန်ကုန်နှင့် မန္တလေးမြို့ရှိ အမှန်တကယ် ကာလပေါက်ဈေးနှုန်းများဖြင့် တွက်ချက်ကာ အာဟာရပြည့်ဝသော ၇ ရက်စာ အစားအစာဇယား ရေးဆွဲပေးပါသည်။"
            : "Generate a custom 7-day schedule backed by authentic Myanmar recipes, lab nutrition values, and real MMK prices from verified wet markets."}
        </p>
      </div>

      {/* Controls Form Drawer */}
      <div className="bg-white rounded-3xl p-6 sm:p-8 border border-stone-200/80 shadow-xs space-y-6">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          {/* Household Size */}
          <div className="space-y-2">
            <label className="text-xs font-bold text-stone-700 uppercase tracking-wider block">
              {language === "mm" ? "စားသုံးသူ မိသားစုဝင် ဦးရေ" : "Household Members"}
            </label>
            <div className="flex items-center gap-2">
              <button
                type="button"
                onClick={() => setHouseholdSize(Math.max(1, householdSize - 1))}
                className="w-10 h-10 rounded-xl bg-stone-100 hover:bg-stone-200 font-bold text-lg text-stone-700 flex items-center justify-center transition-colors"
              >
                -
              </button>
              <div className="flex-1 py-2 px-3 bg-stone-50 border border-stone-200 rounded-xl text-center font-bold text-emerald-800">
                {householdSize} {language === "mm" ? "ဦး" : "Persons"}
              </div>
              <button
                type="button"
                onClick={() => setHouseholdSize(Math.min(10, householdSize + 1))}
                className="w-10 h-10 rounded-xl bg-stone-100 hover:bg-stone-200 font-bold text-lg text-stone-700 flex items-center justify-center transition-colors"
              >
                +
              </button>
            </div>
          </div>

          {/* City Selection */}
          <div className="space-y-2">
            <label className="text-xs font-bold text-stone-700 uppercase tracking-wider block">
              {language === "mm" ? "ဈေးဝယ်မည့် မြို့" : "Shopping Location"}
            </label>
            <div className="grid grid-cols-2 gap-2">
              <button
                type="button"
                onClick={() => setCity("Yangon")}
                className={`py-2.5 px-3 rounded-xl font-bold text-xs transition-all ${
                  city === "Yangon"
                    ? "bg-emerald-800 text-white shadow-sm"
                    : "bg-stone-100 hover:bg-stone-200 text-stone-700"
                }`}
              >
                {language === "mm" ? "ရန်ကုန်" : "Yangon"}
              </button>
              <button
                type="button"
                onClick={() => setCity("Mandalay")}
                className={`py-2.5 px-3 rounded-xl font-bold text-xs transition-all ${
                  city === "Mandalay"
                    ? "bg-emerald-800 text-white shadow-sm"
                    : "bg-stone-100 hover:bg-stone-200 text-stone-700"
                }`}
              >
                {language === "mm" ? "မန္တလေး" : "Mandalay"}
              </button>
            </div>
          </div>

          {/* Weekly Budget */}
          <div className="space-y-2">
            <label className="text-xs font-bold text-stone-700 uppercase tracking-wider block">
              {language === "mm" ? "အပတ်စဉ် သုံးစွဲလိုသော ဘတ်ဂျက် (ကျပ်)" : "Target Weekly Budget (MMK)"}
            </label>
            <div className="relative">
              <input
                type="number"
                placeholder={language === "mm" ? "ဥပမာ- 80000" : "e.g. 80,000"}
                value={weeklyBudget}
                onChange={(e) => setWeeklyBudget(e.target.value ? Number(e.target.value) : "")}
                className="w-full py-2.5 px-3 bg-stone-50 border border-stone-200 rounded-xl text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-emerald-700"
              />
              <span className="absolute right-3 top-2.5 text-xs text-stone-400 font-semibold">MMK</span>
            </div>
          </div>

          {/* Meals Per Day */}
          <div className="space-y-2">
            <label className="text-xs font-bold text-stone-700 uppercase tracking-wider block">
              {language === "mm" ? "တစ်နေ့လျှင် စားသုံးချိန်" : "Meals Per Day"}
            </label>
            <div className="grid grid-cols-2 gap-2">
              <button
                type="button"
                onClick={() => setMealsPerDay(3)}
                className={`py-2.5 px-3 rounded-xl font-bold text-xs transition-all ${
                  mealsPerDay === 3
                    ? "bg-emerald-800 text-white shadow-sm"
                    : "bg-stone-100 hover:bg-stone-200 text-stone-700"
                }`}
              >
                {language === "mm" ? "၃ ချိန် (နံနက်/နေ့/ည)" : "3 Meals"}
              </button>
              <button
                type="button"
                onClick={() => setMealsPerDay(2)}
                className={`py-2.5 px-3 rounded-xl font-bold text-xs transition-all ${
                  mealsPerDay === 2
                    ? "bg-emerald-800 text-white shadow-sm"
                    : "bg-stone-100 hover:bg-stone-200 text-stone-700"
                }`}
              >
                {language === "mm" ? "၂ ချိန် (နေ့/ည)" : "2 Meals"}
              </button>
            </div>
          </div>
        </div>

        {/* Dietary Rules & Submit */}
        <div className="pt-4 border-t border-stone-100 flex flex-col sm:flex-row items-center justify-between gap-4">
          <div className="flex flex-wrap items-center gap-2">
            <span className="text-xs font-bold text-stone-500 mr-2">
              {language === "mm" ? "အစားအသောက် စည်းကမ်း:" : "Dietary Filter:"}
            </span>
            {[
              { id: "vegetarian", label_en: "Vegetarian", label_mm: "သက်သတ်လွတ်" },
              { id: "vegan", label_en: "Vegan", label_mm: "တိရစ္ဆာန်ထွက်ပစ္စည်းမပါ" },
              { id: "gluten_free", label_en: "Gluten-Free", label_mm: "ဂျုံမှုန့်မပါ" },
            ].map((d) => {
              const active = selectedDietary.includes(d.id);
              return (
                <button
                  key={d.id}
                  type="button"
                  onClick={() => handleToggleDietary(d.id)}
                  className={`px-3 py-1.5 rounded-full text-xs font-semibold border transition-all ${
                    active
                      ? "bg-emerald-50 border-emerald-600 text-emerald-800"
                      : "bg-stone-50 border-stone-200 text-stone-600 hover:bg-stone-100"
                  }`}
                >
                  {language === "mm" ? d.label_mm : d.label_en}
                </button>
              );
            })}
          </div>

          <button
            type="button"
            onClick={() => fetchPlan()}
            disabled={loading}
            className="w-full sm:w-auto px-6 py-2.5 bg-emerald-800 hover:bg-emerald-900 text-white font-bold text-xs sm:text-sm rounded-xl shadow-md transition-all active:scale-95 flex items-center justify-center gap-2"
          >
            <SparklesIcon className="w-4 h-4 text-amber-300" />
            <span>
              {loading
                ? language === "mm"
                  ? "တွက်ချက်နေပါသည်..."
                  : "Calculating..."
                : language === "mm"
                ? "အပတ်စဉ် ဇယား အသစ်ပြန်ဆွဲမည်"
                : "Regenerate Plan"}
            </span>
          </button>
        </div>
      </div>

      {/* Plan Summary Bar */}
      {plan && (
        <div className="bg-gradient-to-r from-emerald-900 via-teal-900 to-emerald-950 text-white rounded-3xl p-6 sm:p-8 shadow-xl space-y-4">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
            <div>
              <div className="flex items-center gap-2 text-xs text-emerald-300 font-semibold mb-1">
                <span>{plan.city} Market Rates</span>
                <span>•</span>
                <span>{plan.household_size} Persons</span>
                <span>•</span>
                <span>7 Days ({plan.schedule.length} Meals)</span>
              </div>
              <h2 className="text-2xl sm:text-3xl font-extrabold text-white">
                {language === "mm" ? "ခန့်မှန်း အပတ်စဉ် စုစုပေါင်း ကုန်ကျစရိတ်" : "Estimated Weekly Budget Total"}
              </h2>
              <div className="flex items-baseline gap-2 mt-1">
                <span className="text-3xl sm:text-4xl font-extrabold text-amber-300">
                  {plan.estimated_total_cost_mmk.toLocaleString()}
                </span>
                <span className="text-sm font-semibold text-emerald-200">MMK / Week</span>
              </div>
            </div>

            {/* Quick Metrics */}
            <div className="grid grid-cols-2 gap-4 bg-white/10 backdrop-blur-md p-4 rounded-2xl border border-white/10 text-center">
              <div>
                <span className="text-[11px] text-emerald-200 block uppercase font-bold">
                  {language === "mm" ? "တစ်နေ့ ကယ်လိုရီ/ဦး" : "Daily Calories"}
                </span>
                <span className="text-lg font-extrabold text-white">
                  {plan.average_daily_calories_per_person} kcal
                </span>
              </div>
              <div>
                <span className="text-[11px] text-emerald-200 block uppercase font-bold">
                  {language === "mm" ? "တစ်နေ့ ပရိုတင်း/ဦး" : "Daily Protein"}
                </span>
                <span className="text-lg font-extrabold text-white">
                  {plan.average_daily_protein_per_person} g
                </span>
              </div>
            </div>

            {/* CTA: Export to Grocery List */}
            <div className="flex flex-col justify-center">
              <button
                type="button"
                onClick={handleExportToGroceryList}
                className="px-6 py-3.5 bg-amber-400 hover:bg-amber-300 text-stone-900 font-extrabold text-sm rounded-xl shadow-lg transition-transform active:scale-95 flex items-center justify-center gap-2"
              >
                <CookingPotIcon className="w-5 h-5 text-emerald-900" />
                <span>
                  {language === "mm" ? "ဈေးဝယ်စာရင်း အဆင်သင့်ရယူမည်" : "Generate Grocery List"}
                </span>
              </button>
            </div>
          </div>

          {/* Budget feedback banner */}
          {plan.target_budget_mmk && (
            <div className={`p-3 rounded-xl text-xs font-medium border ${
              plan.is_budget_exceeded 
                ? "bg-red-500/20 border-red-400/40 text-red-200" 
                : "bg-emerald-500/20 border-emerald-400/40 text-emerald-200"
            }`}>
              {language === "mm" ? plan.budget_status_message_mm : plan.budget_status_message_en}
            </div>
          )}

          {/* Real-World Retail Packaging Tip */}
          <div className="flex items-center gap-2 text-[11px] text-emerald-200/90 bg-emerald-950/60 p-3 rounded-xl border border-emerald-700/40">
            <span className="text-sm">🛒</span>
            <span>
              {language === "mm"
                ? "အကြံပြုချက်- အထက်ပါဘတ်ဂျက်သည် ဟင်းချက်စားသုံးမှု တန်ဖိုးဖြစ်ပါသည်။ လက်တွေ့စတိုးဆိုင်များတွင် အထုပ်လိုက်/အလုံးလိုက် (ဥပမာ ဆား ၁ ထုပ်၊ သခွားသီး ၁ လုံး) ဝယ်ယူစရိတ်နှင့် မီးဖိုချောင်အရန်ပစ္စည်း စာရင်းများကို 'ဈေးဝယ်စာရင်း အဆင်သင့်ရယူမည်' ခလုတ်ကို နှိပ်၍ ကြည့်ရှုနိုင်ပါသည်။"
                : "Real-World Tip: This weekly total reflects exact portion costs. Click 'Generate Grocery List' to view full store cashier checkout totals (whole packages like 400g salt packs) with your pantry staples toggle."}
            </span>
          </div>
        </div>
      )}

      {/* 7-Day Meal Calendar */}
      {loading ? (
        <div className="p-16 text-center text-stone-400 space-y-3">
          <div className="w-10 h-10 border-4 border-emerald-700 border-t-transparent rounded-full animate-spin mx-auto" />
          <p className="text-sm font-semibold">
            {language === "mm" ? "အစားအစာဇယား တွက်ချက်နေပါသည်..." : "Constructing optimized meal schedule..."}
          </p>
        </div>
      ) : plan ? (
        <div className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-7 gap-4">
            {[1, 2, 3, 4, 5, 6, 7].map((dayNum) => {
              const dayMeals = plan.schedule.filter((s) => s.day_of_week === dayNum);
              const daySummary = plan.daily_summaries.find((d) => d.day_of_week === dayNum);
              const dayEn = DAYS_EN[dayNum - 1];
              const dayMm = DAYS_MM[dayNum - 1];

              return (
                <div
                  key={dayNum}
                  className="bg-white rounded-3xl border border-stone-200 p-4 space-y-3 shadow-xs flex flex-col justify-between"
                >
                  {/* Day Header */}
                  <div className="border-b border-stone-100 pb-2 flex items-center justify-between">
                    <div>
                      <span className="font-extrabold text-sm text-emerald-800 block">
                        {language === "mm" ? dayMm : dayEn}
                      </span>
                      <span className="text-[11px] text-stone-400">Day {dayNum}</span>
                    </div>
                    {daySummary && (
                      <span className="text-[11px] font-bold text-stone-600 bg-stone-100 px-2 py-0.5 rounded-full">
                        {daySummary.total_cost_mmk.toLocaleString()} K
                      </span>
                    )}
                  </div>

                  {/* Meals list */}
                  <div className="space-y-3 flex-1">
                    {dayMeals.map((meal) => (
                      <div
                        key={meal.meal_type}
                        className="p-3 bg-stone-50/80 hover:bg-emerald-50/40 rounded-2xl border border-stone-100 space-y-2 transition-colors group"
                      >
                        <div className="flex items-center justify-between">
                          <span className="text-[10px] uppercase font-bold text-stone-400">
                            {meal.meal_type}
                          </span>
                          <span className="text-[11px] font-bold text-emerald-700">
                            {meal.estimated_cost_mmk.toLocaleString()} MMK
                          </span>
                        </div>

                        <Link
                          href={`/recipes/${meal.recipe_id}`}
                          className="font-bold text-xs text-stone-800 hover:text-emerald-700 block line-clamp-1 transition-colors"
                        >
                          {language === "mm" ? meal.recipe_name_mm : meal.recipe_name_en}
                        </Link>

                        <div className="flex items-center justify-between text-[10px] text-stone-500">
                          <span>{meal.calories_kcal} kcal</span>
                          <span>{meal.protein_g}g prot</span>
                        </div>

                        {/* Swap Button */}
                        <div className="pt-1 border-t border-stone-200/60 flex items-center justify-end">
                          <button
                            type="button"
                            onClick={() => openReplaceModal(meal)}
                            className="text-[11px] text-stone-500 hover:text-emerald-800 font-semibold transition-colors flex items-center gap-1"
                          >
                            <span>↻</span>
                            <span>{language === "mm" ? "အစားထိုးမည်" : "Swap"}</span>
                          </button>
                        </div>
                      </div>
                    ))}
                  </div>

                  {/* Day Footer Nutrition */}
                  {daySummary && (
                    <div className="pt-2 border-t border-stone-100 text-[10px] text-stone-500 flex justify-between">
                      <span>Total Cal:</span>
                      <span className="font-semibold">{daySummary.total_calories_kcal} kcal</span>
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>
      ) : null}

      {/* Meal Replacement Modal */}
      {activeSlot && (
        <div className="fixed inset-0 z-50 bg-stone-900/60 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-white rounded-3xl max-w-xl w-full p-6 shadow-2xl border border-stone-200 space-y-5 animate-in fade-in zoom-in-95 duration-200">
            <div className="flex items-center justify-between border-b border-stone-100 pb-3">
              <div>
                <span className="text-xs uppercase font-extrabold text-emerald-700 block">
                  {language === "mm" ? "အစားထိုး ဟင်းလျာ ရွေးချယ်ရန်" : "Swap Meal"}
                </span>
                <h3 className="text-lg font-extrabold text-stone-900">
                  {language === "mm" ? activeSlot.recipe_name_mm : activeSlot.recipe_name_en} (Day {activeSlot.day_of_week} {activeSlot.meal_type})
                </h3>
              </div>
              <button
                type="button"
                onClick={() => setActiveSlot(null)}
                className="w-8 h-8 rounded-full bg-stone-100 hover:bg-stone-200 flex items-center justify-center text-stone-500 font-bold"
              >
                ✕
              </button>
            </div>

            <p className="text-xs text-stone-600">
              {language === "mm"
                ? "အောက်ဖော်ပြပါ အစားထိုးဟင်းလျာများသည် သင့်သတ်မှတ်ချက်များနှင့် ကိုက်ညီပြီး ဈေးနှုန်းကွာခြားချက်ကို တိုက်ရိုက် နှိုင်းယှဉ်နိုင်ပါသည်:"
                : "Select an alternative recipe with dynamic MMK cost variance comparison:"}
            </p>

            {loadingReplacements ? (
              <div className="py-12 text-center text-stone-400 space-y-2">
                <div className="w-8 h-8 border-4 border-emerald-700 border-t-transparent rounded-full animate-spin mx-auto" />
                <p className="text-xs">Finding best options...</p>
              </div>
            ) : replacementCandidates.length === 0 ? (
              <div className="py-8 text-center text-xs text-stone-500">
                {language === "mm" ? "အစားထိုးရန် ဟင်းလျာ မတွေ့ရှိပါ။" : "No replacement options available."}
              </div>
            ) : (
              <div className="space-y-2.5 max-h-80 overflow-y-auto pr-1">
                {replacementCandidates.map((cand) => {
                  const diff = cand.cost_difference_mmk;
                  const diffColor = diff > 0 ? "text-amber-700 bg-amber-50" : "text-emerald-700 bg-emerald-50";
                  const diffLabel = diff > 0 ? `+${diff.toLocaleString()} K` : `${diff.toLocaleString()} K`;

                  return (
                    <div
                      key={cand.recipe_id}
                      className="p-3 rounded-2xl border border-stone-200 hover:border-emerald-600 flex items-center justify-between gap-3 transition-colors bg-stone-50/50"
                    >
                      <div className="space-y-1">
                        <span className="font-bold text-xs sm:text-sm text-stone-900 block">
                          {language === "mm" ? cand.name_mm : cand.name_en}
                        </span>
                        <div className="flex items-center gap-2 text-[10px] text-stone-500">
                          <span>{cand.category}</span>
                          <span>•</span>
                          <span>{cand.calories_kcal} kcal</span>
                          <span>•</span>
                          <span className="font-semibold text-stone-800">{cand.estimated_cost_mmk.toLocaleString()} MMK</span>
                        </div>
                      </div>

                      <div className="flex items-center gap-3 shrink-0">
                        <span className={`text-[11px] font-bold px-2 py-0.5 rounded-full ${diffColor}`}>
                          {diffLabel}
                        </span>
                        <button
                          type="button"
                          onClick={() => applyReplacement(cand)}
                          className="px-3.5 py-1.5 bg-emerald-800 hover:bg-emerald-900 text-white font-bold text-xs rounded-xl shadow-xs transition-transform active:scale-95"
                        >
                          {language === "mm" ? "ရွေးချယ်မည်" : "Choose"}
                        </button>
                      </div>
                    </div>
                  );
                })}
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default function PlannerPage() {
  return (
    <Suspense fallback={<div className="p-12 text-center text-stone-400">Loading planner...</div>}>
      <PlannerContent />
    </Suspense>
  );
}
