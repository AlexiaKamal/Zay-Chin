"use client";

import React, { Suspense, useState, useEffect, useMemo } from "react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { useApp } from "@/context/AppContext";
import { 
  CookingPotIcon, 
  CalendarIcon, 
  CoinsIcon, 
  PlusIcon, 
  MinusIcon, 
  SearchIcon 
} from "@/components/ui/Icons";

interface RawRecipeRecord {
  recipe_id: string;
  name_en: string;
  name_mm: string;
  category: string;
}
import { generateGroceryList } from "@/lib/api";
import { GroceryListResponse, GroceryItem } from "@/types";
import rawRecipes from "@/data/recipes.json";

function GroceryListContent() {
  const { language, city, t } = useApp();
  const searchParams = useSearchParams();

  // Recipe lookup map for 171 authentic Daw San Lay recipes
  const recipeLookup = useMemo(() => {
    const map = new Map<string, { id: string; name_en: string; name_mm: string; category: string }>();
    for (const r of (rawRecipes as unknown as RawRecipeRecord[])) {
      map.set(r.recipe_id, {
        id: r.recipe_id,
        name_en: r.name_en,
        name_mm: r.name_mm,
        category: r.category,
      });
    }
    return map;
  }, []);

  // Wizard Step State: 1 = Generate, 2 = Review (remove at-home items), 3 = Final List
  const [step, setStep] = useState<1 | 2 | 3>(1);

  // Core Data State
  const [householdSize, setHouseholdSize] = useState<number>(2);
  const [recipeIds, setRecipeIds] = useState<string[]>(["R0001", "R0002", "R0003", "R0004", "R0005"]);
  const [loading, setLoading] = useState<boolean>(true);
  const [groceryList, setGroceryList] = useState<GroceryListResponse | null>(null);

  // Checklist of items bought at market (for Step 3)
  const [checkedItems, setCheckedItems] = useState<Record<string, boolean>>({});

  // Review step: items sitting at home (true = sitting at home, do not buy)
  const [atHomeItems, setAtHomeItems] = useState<Record<string, boolean>>({});

  // Completion Pop-up Modal state
  const [showCelebration, setShowCelebration] = useState<boolean>(false);
  const [hasCelebrated, setHasCelebrated] = useState<boolean>(false);

  // Copy feedback
  const [copied, setCopied] = useState<boolean>(false);

  // Modal for adding extra dishes to the grocery list
  const [showAddModal, setShowAddModal] = useState<boolean>(false);
  const [recipeSearch, setRecipeSearch] = useState<string>("");

  const fetchGroceryList = async (recipes: string[], hh: number, currentCity: string) => {
    setLoading(true);
    try {
      const res = await generateGroceryList({
        city: currentCity,
        household_size: hh,
        recipe_ids: recipes,
      });
      setGroceryList(res);

      // Pre-seed pantry defaults for review step
      const initialAtHome: Record<string, boolean> = {};
      if (res && res.groups) {
        res.groups.forEach((g) => {
          g.items.forEach((item) => {
            if (item.is_pantry_staple) {
              initialAtHome[item.ingredient_id] = true;
            }
          });
        });
      }
      setAtHomeItems((prev) => (Object.keys(prev).length === 0 ? initialAtHome : prev));

      // Load saved checked items
      const savedChecked =
        localStorage.getItem(`zaychin_checked_${currentCity}`) ||
        localStorage.getItem("zaychin_grocery_checked");
      if (savedChecked) {
        try {
          setCheckedItems(JSON.parse(savedChecked));
        } catch {
          setCheckedItems({});
        }
      } else {
        setCheckedItems({});
      }
    } catch (err) {
      console.error("Error generating grocery list:", err);
    } finally {
      setLoading(false);
    }
  };

  // Function to load recipes & fetch list
  const syncAndFetch = (overrideRecipes?: string[], overrideHh?: number) => {
    const paramRecipes = searchParams.get("recipes");
    const paramHousehold = searchParams.get("household");

    let ids = overrideRecipes || [];

    // 1. Prefer localStorage (has latest plan from planner or additions)
    if (ids.length === 0) {
      const savedRecipesRaw = localStorage.getItem("zaychin_grocery_recipes");
      if (savedRecipesRaw) {
        try {
          const parsed = JSON.parse(savedRecipesRaw);
          if (Array.isArray(parsed) && parsed.length > 0) {
            ids = parsed;
          }
        } catch (e) {
          console.error("Error reading saved recipes:", e);
        }
      }
    }

    // 2. URL searchParams fallback
    if (ids.length === 0 && paramRecipes) {
      ids = paramRecipes.split(",").map((s) => s.trim()).filter(Boolean);
    }

    // 3. Default fallback
    if (ids.length === 0) {
      ids = ["R0001", "R0002", "R0003", "R0004", "R0005"];
    }

    let hh = overrideHh || 2;
    if (!overrideHh) {
      const savedHousehold = localStorage.getItem("zaychin_grocery_household");
      if (savedHousehold) {
        hh = parseInt(savedHousehold, 10) || 2;
      } else if (paramHousehold) {
        hh = parseInt(paramHousehold, 10) || 2;
      }
    }

    setHouseholdSize(hh);
    setRecipeIds(ids);
    fetchGroceryList(ids, hh, city);
  };

  // Initial load
  useEffect(() => {
    syncAndFetch();
  }, [city, searchParams]);

  // Reactive listener: Updates automatically whenever recipes or meal plans change
  useEffect(() => {
    const handleStorageChange = (e: StorageEvent) => {
      if (e.key === "zaychin_grocery_recipes" || e.key === "zaychin_grocery_household") {
        setCheckedItems({});
        localStorage.removeItem(`zaychin_checked_${city}`);
        localStorage.removeItem("zaychin_grocery_checked");
        syncAndFetch();
      }
    };

    const handleCustomUpdate = (e: Event) => {
      const custom = e as CustomEvent<{ recipeIds?: string[]; household?: number }>;
      setCheckedItems({});
      localStorage.removeItem(`zaychin_checked_${city}`);
      localStorage.removeItem("zaychin_grocery_checked");
      setHasCelebrated(false);
      setShowCelebration(false);
      if (custom.detail?.recipeIds) {
        syncAndFetch(custom.detail.recipeIds, custom.detail.household);
      } else {
        syncAndFetch();
      }
    };

    const handleWindowFocus = () => {
      const savedRecipesRaw = localStorage.getItem("zaychin_grocery_recipes");
      if (savedRecipesRaw) {
        try {
          const parsed = JSON.parse(savedRecipesRaw);
          if (Array.isArray(parsed) && JSON.stringify(parsed) !== JSON.stringify(recipeIds)) {
            syncAndFetch(parsed);
          }
        } catch (e) {}
      }
    };

    window.addEventListener("storage", handleStorageChange);
    window.addEventListener("zaychin_recipes_updated", handleCustomUpdate);
    window.addEventListener("focus", handleWindowFocus);

    return () => {
      window.removeEventListener("storage", handleStorageChange);
      window.removeEventListener("zaychin_recipes_updated", handleCustomUpdate);
      window.removeEventListener("focus", handleWindowFocus);
    };
  }, [recipeIds]);

  // Changing household size
  const handleHouseholdChange = (newHh: number) => {
    const val = Math.max(1, Math.min(20, newHh));
    setHouseholdSize(val);
    localStorage.setItem("zaychin_grocery_household", val.toString());
    fetchGroceryList(recipeIds, val, city);
  };

  // Adding a dish to the active grocery list
  const handleAddRecipe = (rId: string) => {
    if (recipeIds.includes(rId)) {
      setShowAddModal(false);
      return;
    }
    const updated = [...recipeIds, rId];
    setRecipeIds(updated);
    localStorage.setItem("zaychin_grocery_recipes", JSON.stringify(updated));
    setShowAddModal(false);
    setRecipeSearch("");
    fetchGroceryList(updated, householdSize, city);
  };

  // Removing a dish from the active grocery list
  const handleRemoveRecipe = (rId: string) => {
    if (recipeIds.length <= 1) return;
    const updated = recipeIds.filter((id) => id !== rId);
    setRecipeIds(updated);
    localStorage.setItem("zaychin_grocery_recipes", JSON.stringify(updated));
    fetchGroceryList(updated, householdSize, city);
  };

  // Sync from planner
  const handleSyncWithPlanner = () => {
    const saved = localStorage.getItem("zaychin_grocery_recipes");
    let ids = ["R0001", "R0002", "R0003", "R0004", "R0005"];
    if (saved) {
      try {
        const parsed = JSON.parse(saved);
        if (Array.isArray(parsed) && parsed.length > 0) ids = parsed;
      } catch (e) {}
    }
    setRecipeIds(ids);
    fetchGroceryList(ids, householdSize, city);
  };

  // Toggle item sitting at home (Step 2 Review)
  const toggleAtHome = (itemId: string) => {
    setAtHomeItems((prev) => ({
      ...prev,
      [itemId]: !prev[itemId],
    }));
  };

  // Toggle checklist item as bought (Step 3 Final)
  const toggleCheck = (itemId: string) => {
    setCheckedItems((prev) => {
      const next = { ...prev, [itemId]: !prev[itemId] };
      localStorage.setItem(`zaychin_checked_${city}`, JSON.stringify(next));
      localStorage.setItem("zaychin_grocery_checked", JSON.stringify(next));
      return next;
    });
  };

  // Clear all checked items
  const handleResetChecklist = () => {
    setCheckedItems({});
    localStorage.removeItem(`zaychin_checked_${city}`);
    localStorage.removeItem("zaychin_grocery_checked");
    setHasCelebrated(false);
    setShowCelebration(false);
  };

  // Financial & Item Computations
  const allRawItems: GroceryItem[] = groceryList ? groceryList.groups.flatMap((g) => g.items) : [];

  // Grocery cost before review = total store package purchase price of ALL items
  const groceryCostBeforeReview = useMemo(() => {
    return allRawItems.reduce((acc, item) => {
      if (item.is_zero_cost_utility) return acc;
      return acc + (item.retail_package_price_mmk || item.estimated_price_mmk || 0);
    }, 0);
  }, [allRawItems]);

  // Grocery cost after review = cost of items NOT sitting at home
  const groceryCostAfterReview = useMemo(() => {
    return allRawItems.reduce((acc, item) => {
      if (item.is_zero_cost_utility) return acc;
      if (atHomeItems[item.ingredient_id]) return acc; // excluded because already at home!
      return acc + (item.retail_package_price_mmk || item.estimated_price_mmk || 0);
    }, 0);
  }, [allRawItems, atHomeItems]);

  // Pantry Stock Savings = (grocery cost before review - grocery list after review)
  const pantryStockSavings = Math.max(0, groceryCostBeforeReview - groceryCostAfterReview);

  // Final items to buy (Step 3) - excludes items marked sitting at home
  const finalItemsToBuy = useMemo(() => {
    return allRawItems.filter((item) => !atHomeItems[item.ingredient_id] && !item.is_zero_cost_utility);
  }, [allRawItems, atHomeItems]);

  // Shopping checklist progress
  const totalCount = finalItemsToBuy.length;
  const purchasedCount = finalItemsToBuy.filter((i) => checkedItems[i.ingredient_id]).length;
  const progressPct = totalCount > 0 ? Math.round((purchasedCount / totalCount) * 100) : 0;

  // Trigger celebration pop-up when all items are checked as bought
  useEffect(() => {
    if (step === 3 && totalCount > 0 && purchasedCount === totalCount && !hasCelebrated) {
      setShowCelebration(true);
      setHasCelebrated(true);
    }
  }, [purchasedCount, totalCount, step, hasCelebrated]);

  const handleCopyClipboard = () => {
    if (!groceryList) return;
    let text = `🛒 Zay Chin (ဈေးခြင်း) — Final Grocery Shopping List (${city}, ${householdSize} Persons)\n`;
    text += `Dishes: ${recipeIds.map((id) => recipeLookup.get(id)?.name_en || id).join(", ")}\n\n`;

    groceryList.groups.forEach((g) => {
      const buyableItems = g.items.filter((i) => !atHomeItems[i.ingredient_id] && !i.is_zero_cost_utility);
      if (buyableItems.length === 0) return;

      const catName = language === "mm" ? g.category_name_mm : g.category_name_en;
      text += `📍 [${catName}]\n`;
      buyableItems.forEach((item) => {
        const isDone = checkedItems[item.ingredient_id] ? "✓" : "☐";
        const name = language === "mm" ? item.name_mm : item.name_en;
        const buyUnit = item.purchasable_unit_en || `${item.total_quantity} ${item.unit}`;
        const price = item.retail_package_price_mmk != null ? `${item.retail_package_price_mmk.toLocaleString()} MMK` : "Market Price";
        text += `  ${isDone} ${name} — Buy: ${buyUnit} (${price})\n`;
      });
      text += "\n";
    });

    text += `💰 Final Cashier Out-of-Pocket Cost: ${groceryCostAfterReview.toLocaleString()} MMK\n`;
    text += `🏠 Pantry Stock Savings: ${pantryStockSavings.toLocaleString()} MMK Saved (Items already at home)\n`;
    text += `Verified Retail Market Observations • Zero Hallucination\n`;

    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2500);
  };

  const handlePrint = () => {
    window.print();
  };

  // Filter recipes for add modal
  const filteredCandidates = useMemo(() => {
    const q = recipeSearch.trim().toLowerCase();
    const all = Array.from(recipeLookup.values());
    if (!q) return all.slice(0, 15);
    return all
      .filter((r) => r.name_en.toLowerCase().includes(q) || r.name_mm.includes(q) || r.category.toLowerCase().includes(q))
      .slice(0, 15);
  }, [recipeSearch, recipeLookup]);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-8 animate-in fade-in duration-300">
      {/* Header */}
      <div className="text-center max-w-3xl mx-auto space-y-3">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-bold bg-[var(--color-muted)] text-[var(--color-primary)] border border-[var(--color-border)] shadow-xs">
          <CoinsIcon className="w-4 h-4 text-[var(--color-primary)]" />
          <span>{language === "mm" ? "၃ ဆင့် ဈေးဝယ်စာရင်းနှင့် မီးဖိုချောင်အရန် ချွေတာမှု" : "3-Step Smart Grocery & Pantry Savings"}</span>
        </div>
        <h1 className="text-3xl sm:text-4xl font-extrabold text-[var(--color-text)] tracking-tight">
          {language === "mm" ? "ဈေးဝယ်စာရင်းနှင့် စတိုးဆိုင် ကုန်ကျစရိတ်" : "Smart Grocery List & Cashier Budget"}
        </h1>
        <p className="text-sm sm:text-base text-stone-600 leading-relaxed">
          {language === "mm"
            ? "၁။ ဈေးဝယ်စာရင်း ထုတ်ယူပါ → ၂။ အိမ်တွင်ရှိပြီးသား ပစ္စည်းများကို စစ်ထုတ်ပယ်ဖျက်ပါ → ၃။ မီးဖိုချောင်အရန် ချွေတာနိုင်မှုနှင့် နောက်ဆုံး ကျသင့်ငွေကို တိကျစွာ ရယူပါ။"
            : "1. Generate grocery list → 2. Review & remove items already at home → 3. Final grocery list with out-of-pocket cost and pantry stock savings."}
        </p>
      </div>

      {/* 3-Step Flow Stepper Navigation */}
      <div className="bg-white rounded-3xl p-4 sm:p-5 border border-[var(--color-border)] shadow-sm">
        <div className="grid grid-cols-3 gap-2 sm:gap-4">
          {/* Step 1 Pill */}
          <button
            type="button"
            onClick={() => setStep(1)}
            className={`p-3 sm:p-4 rounded-2xl text-left transition-all duration-200 border flex items-center gap-3 ${
              step === 1
                ? "bg-[var(--color-muted)] border-[var(--color-primary)] shadow-sm text-[var(--color-primary)]"
                : "border-transparent hover:bg-stone-50 text-stone-600"
            }`}
          >
            <div
              className={`w-8 h-8 rounded-xl flex items-center justify-center font-extrabold text-sm shrink-0 transition-colors ${
                step === 1 ? "bg-[var(--color-primary)] text-white shadow-xs" : "bg-stone-200 text-stone-700"
              }`}
            >
              1
            </div>
            <div className="min-w-0">
              <span className="text-[10px] sm:text-xs font-bold uppercase tracking-wider block opacity-75">
                {language === "mm" ? "အဆင့် ၁" : "Step 1"}
              </span>
              <span className="text-xs sm:text-sm font-extrabold block truncate">
                {language === "mm" ? "စာရင်း ထုတ်ယူမည်" : "Generate List"}
              </span>
            </div>
          </button>

          {/* Step 2 Pill */}
          <button
            type="button"
            onClick={() => setStep(2)}
            className={`p-3 sm:p-4 rounded-2xl text-left transition-all duration-200 border flex items-center gap-3 ${
              step === 2
                ? "bg-[var(--color-muted)] border-[var(--color-primary)] shadow-sm text-[var(--color-primary)]"
                : "border-transparent hover:bg-stone-50 text-stone-600"
            }`}
          >
            <div
              className={`w-8 h-8 rounded-xl flex items-center justify-center font-extrabold text-sm shrink-0 transition-colors ${
                step === 2 ? "bg-[var(--color-primary)] text-white shadow-xs" : "bg-stone-200 text-stone-700"
              }`}
            >
              2
            </div>
            <div className="min-w-0">
              <span className="text-[10px] sm:text-xs font-bold uppercase tracking-wider block opacity-75">
                {language === "mm" ? "အဆင့် ၂" : "Step 2"}
              </span>
              <span className="text-xs sm:text-sm font-extrabold block truncate">
                {language === "mm" ? "အိမ်ရှိပစ္စည်း စစ်ဆေးမည်" : "Review Pantry"}
              </span>
            </div>
          </button>

          {/* Step 3 Pill */}
          <button
            type="button"
            onClick={() => setStep(3)}
            className={`p-3 sm:p-4 rounded-2xl text-left transition-all duration-200 border flex items-center gap-3 ${
              step === 3
                ? "bg-[var(--color-muted)] border-[var(--color-primary)] shadow-sm text-[var(--color-primary)]"
                : "border-transparent hover:bg-stone-50 text-stone-600"
            }`}
          >
            <div
              className={`w-8 h-8 rounded-xl flex items-center justify-center font-extrabold text-sm shrink-0 transition-colors ${
                step === 3 ? "bg-[var(--color-primary)] text-white shadow-xs" : "bg-stone-200 text-stone-700"
              }`}
            >
              3
            </div>
            <div className="min-w-0">
              <span className="text-[10px] sm:text-xs font-bold uppercase tracking-wider block opacity-75">
                {language === "mm" ? "အဆင့် ၃" : "Step 3"}
              </span>
              <span className="text-xs sm:text-sm font-extrabold block truncate">
                {language === "mm" ? "နောက်ဆုံး ဈေးဝယ်စာရင်း" : "Final Grocery List"}
              </span>
            </div>
          </button>
        </div>
      </div>

      {/* ======================================================== */}
      {/* STEP 1: GENERATE GROCERY LIST (Recipes & Household Size) */}
      {/* ======================================================== */}
      {step === 1 && (
        <div className="space-y-6 animate-in fade-in duration-200">
          <div className="bg-white rounded-3xl p-6 sm:p-8 border border-[var(--color-border)] shadow-md space-y-6">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-stone-100 pb-5">
              <div>
                <div className="flex items-center gap-2">
                  <CookingPotIcon className="w-5 h-5 text-[var(--color-primary)]" />
                  <h2 className="text-lg font-extrabold text-stone-900">
                    {language === "mm" ? "ဈေးဝယ်စာရင်းတွင် ထည့်သွင်းထားသော ဟင်းလျာများ" : "Active Recipes in Grocery List"}
                  </h2>
                </div>
                <p className="text-xs text-stone-500 mt-1">
                  {language === "mm"
                    ? "ဟင်းလျာများ ထည့်သွင်း/ဖယ်ထုတ်နိုင်ပြီး မိသားစု ဦးရေအလိုက် စာရင်းကို အလိုအလျောက် တွက်ချက်ပေးပါသည်။"
                    : "Add or remove dishes, or adjust household size to scale all ingredient quantities."}
                </p>
              </div>

              {/* Household Size Stepper */}
              <div className="flex items-center gap-2 bg-stone-50 px-3.5 py-2 rounded-2xl border border-stone-200 shrink-0">
                <span className="text-xs font-bold text-stone-600">
                  {language === "mm" ? "စားသုံးသူ:" : "Household:"}
                </span>
                <button
                  type="button"
                  onClick={() => handleHouseholdChange(householdSize - 1)}
                  disabled={householdSize <= 1}
                  className="w-7 h-7 rounded-lg bg-white border border-stone-200 flex items-center justify-center font-bold text-stone-700 hover:bg-stone-100 disabled:opacity-40 transition-all active:scale-95"
                >
                  <MinusIcon className="w-3.5 h-3.5" />
                </button>
                <span className="text-xs font-extrabold text-[var(--color-primary)] w-12 text-center">
                  {householdSize} {language === "mm" ? "ဦး" : "pax"}
                </span>
                <button
                  type="button"
                  onClick={() => handleHouseholdChange(householdSize + 1)}
                  disabled={householdSize >= 20}
                  className="w-7 h-7 rounded-lg bg-white border border-stone-200 flex items-center justify-center font-bold text-stone-700 hover:bg-stone-100 disabled:opacity-40 transition-all active:scale-95"
                >
                  <PlusIcon className="w-3.5 h-3.5" />
                </button>
              </div>
            </div>

            {/* Recipe Chips List */}
            <div className="space-y-3">
              <div className="flex items-center justify-between">
                <span className="text-xs font-bold text-stone-500 uppercase tracking-wider">
                  {recipeIds.length} {language === "mm" ? "မျိုး ရွေးချယ်ထားပါသည်" : "Recipes Planned"}
                </span>
                <div className="flex items-center gap-2">
                  <button
                    type="button"
                    onClick={() => setShowAddModal(true)}
                    className="px-3 py-1.5 bg-emerald-50 hover:bg-emerald-100 text-[var(--color-primary)] font-bold text-xs rounded-xl border border-[var(--color-border)] transition-all active:scale-95 flex items-center gap-1"
                  >
                    <PlusIcon className="w-3.5 h-3.5" />
                    <span>{language === "mm" ? "+ ဟင်းလျာ ထည့်မည်" : "+ Add Dish"}</span>
                  </button>
                  <button
                    type="button"
                    onClick={handleSyncWithPlanner}
                    className="px-3 py-1.5 bg-stone-100 hover:bg-stone-200 text-stone-700 font-semibold text-xs rounded-xl transition-all active:scale-95 flex items-center gap-1"
                  >
                    <CalendarIcon className="w-3.5 h-3.5 text-[var(--color-primary)]" />
                    <span>{language === "mm" ? "ဇယားမှ ဆွဲယူမည်" : "Sync Planner"}</span>
                  </button>
                </div>
              </div>

              <div className="flex flex-wrap items-center gap-2">
                {recipeIds.map((rId) => {
                  const recipeInfo = recipeLookup.get(rId);
                  const name = recipeInfo ? (language === "mm" ? recipeInfo.name_mm : recipeInfo.name_en) : rId;
                  return (
                    <span
                      key={rId}
                      className="inline-flex items-center gap-2 px-3.5 py-2 rounded-xl bg-[var(--color-muted)]/40 text-stone-900 border border-[var(--color-border)] text-xs font-bold shadow-2xs"
                    >
                      <Link href={`/recipes/${rId}`} className="hover:underline hover:text-[var(--color-primary)]">
                        {name}
                      </Link>
                      {recipeIds.length > 1 && (
                        <button
                          type="button"
                          onClick={() => handleRemoveRecipe(rId)}
                          className="w-4 h-4 rounded-full bg-stone-200 hover:bg-red-200 hover:text-red-800 text-stone-600 flex items-center justify-center font-bold text-[10px] transition-colors"
                          title="Remove dish"
                        >
                          ×
                        </button>
                      )}
                    </span>
                  );
                })}
              </div>
            </div>

            {/* Step 1 Action Bar: Advance to Step 2 Review */}
            <div className="pt-4 border-t border-stone-100 flex flex-col sm:flex-row items-center justify-between gap-4">
              <div className="text-xs text-stone-500">
                {allRawItems.length} {language === "mm" ? "မျိုး စုစုပေါင်း ပါဝင်ပစ္စည်း လိုအပ်ပါသည်" : "total ingredients aggregated"}
              </div>
              <button
                type="button"
                onClick={() => setStep(2)}
                className="w-full sm:w-auto px-7 py-3 rounded-xl font-extrabold text-sm text-white shadow-md hover:shadow-lg transition-all active:scale-95 flex items-center justify-center gap-2 hover:opacity-95"
                style={{ backgroundColor: "var(--color-primary)" }}
              >
                <span>{language === "mm" ? "အိမ်ရှိပစ္စည်းများ စစ်ဆေးဖယ်ထုတ်ရန် (အဆင့် ၂ သို့) →" : "Review At-Home Items (Proceed to Step 2) →"}</span>
              </button>
            </div>
          </div>
        </div>
      )}

      {/* ======================================================================== */}
      {/* STEP 2: REVIEW THE LIST (Remove items that are already sitting at home) */}
      {/* ======================================================================== */}
      {step === 2 && (
        <div className="space-y-6 animate-in fade-in duration-200">
          {/* Review Instructions Banner */}
          <div className="bg-white rounded-3xl p-6 sm:p-7 border border-[var(--color-border)] shadow-md space-y-4">
            <div className="flex items-start gap-4">
              <div className="w-12 h-12 rounded-2xl bg-amber-100 text-amber-900 flex items-center justify-center text-2xl shrink-0 shadow-2xs">
                🏠
              </div>
              <div className="space-y-1">
                <h3 className="text-base sm:text-lg font-extrabold text-stone-900">
                  {language === "mm" ? "အဆင့် ၂ - အိမ်တွင်ရှိပြီးသား ပစ္စည်းများကို စစ်ထုတ်ပယ်ဖျက်ပါ" : "Step 2: Review & Remove Items Already Sitting at Home"}
                </h3>
                <p className="text-xs sm:text-sm text-stone-600 leading-relaxed">
                  {language === "mm"
                    ? "ဆား၊ ဆီ၊ သကြား၊ ငံပြာရည် စသည့် ဟင်းခတ်ပစ္စည်းများ သင့်မီးဖိုချောင်တွင် ရှိပြီးဖြစ်ပါက အမှန်ခြစ်ပါ။ စတိုးဆိုင်တွင် အသစ်ဝယ်ယူစရာ မလိုတော့သဖြင့် နောက်ဆုံး ဈေးဝယ်စာရင်းမှ အလိုအလျောက် ပယ်ဖျက်ပေးကာ ချွေတာနိုင်မှုကို တွက်ချက်ပေးပါသည်။"
                    : "Check the items you already have sitting in your kitchen cabinets or fridge. They will be removed from your final shopping trip and calculated as your pantry savings."}
                </p>
              </div>
            </div>

            {/* Live Savings Calculation Meter during review */}
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-3 border-t border-stone-100 text-center">
              <div className="p-3 bg-stone-50 rounded-2xl border border-stone-200">
                <span className="text-[11px] font-bold text-stone-400 block uppercase">
                  {language === "mm" ? "စစ်ဆေးခြင်းမပြုမီ စုစုပေါင်းစရိတ်" : "Cost Before Review"}
                </span>
                <span className="text-lg font-black text-stone-700">
                  {groceryCostBeforeReview.toLocaleString()} MMK
                </span>
              </div>
              <div className="p-3 bg-emerald-50/60 rounded-2xl border border-emerald-200">
                <span className="text-[11px] font-bold text-[var(--color-primary)] block uppercase">
                  {language === "mm" ? "မီးဖိုချောင်အရန် ချွေတာနိုင်မှု" : "Pantry Savings"}
                </span>
                <span className="text-lg font-black text-[var(--color-primary)]">
                  -{pantryStockSavings.toLocaleString()} MMK
                </span>
              </div>
              <div className="p-3 bg-[var(--color-muted)]/50 rounded-2xl border border-[var(--color-border)]">
                <span className="text-[11px] font-bold text-stone-900 block uppercase">
                  {language === "mm" ? "စစ်ဆေးပြီးနောက် ဝယ်ယူရမည့်စရိတ်" : "Cost After Review"}
                </span>
                <span className="text-lg font-black text-[var(--color-primary)]">
                  {groceryCostAfterReview.toLocaleString()} MMK
                </span>
              </div>
            </div>

            {/* Advance to Step 3 CTA Button */}
            <div className="pt-2 flex flex-col sm:flex-row items-center justify-between gap-3">
              <button
                type="button"
                onClick={() => setStep(1)}
                className="w-full sm:w-auto px-5 py-2.5 rounded-xl border border-stone-200 text-stone-600 hover:bg-stone-50 font-bold text-xs"
              >
                ← {language === "mm" ? "ဟင်းလျာများ ပြန်လည်ရွေးရန်" : "Back to Recipes"}
              </button>
              <button
                type="button"
                onClick={() => setStep(3)}
                className="w-full sm:w-auto px-7 py-3 rounded-xl font-extrabold text-sm text-white shadow-md hover:shadow-lg transition-all active:scale-95 flex items-center justify-center gap-2 hover:opacity-95"
                style={{ backgroundColor: "var(--color-primary)" }}
              >
                <span>{language === "mm" ? "အတည်ပြုပြီး နောက်ဆုံး ဈေးဝယ်စာရင်း ထုတ်မည် (အဆင့် ၃ သို့) →" : "Confirm & View Final Grocery List (Step 3) →"}</span>
              </button>
            </div>
          </div>

          {/* List of All Items for Review Toggle */}
          <div className="space-y-4">
            {groceryList?.groups.map((group) => {
              const groupName = language === "mm" ? group.category_name_mm : group.category_name_en;
              return (
                <div key={group.category_id} className="bg-white rounded-3xl border border-[var(--color-border)] overflow-hidden shadow-xs">
                  <div className="bg-stone-50/80 px-6 py-3.5 border-b border-stone-100 flex items-center justify-between">
                    <h3 className="font-extrabold text-sm text-stone-900">{groupName}</h3>
                    <span className="text-xs text-stone-400 font-medium">
                      {group.items.length} {language === "mm" ? "မျိုး" : "items"}
                    </span>
                  </div>

                  <div className="divide-y divide-stone-100">
                    {group.items.map((item) => {
                      const isSittingAtHome = !!atHomeItems[item.ingredient_id];
                      const itemName = language === "mm" ? item.name_mm : item.name_en;
                      const buyUnit = language === "mm"
                        ? (item.purchasable_unit_mm || `${item.purchasable_quantity || item.total_quantity} ${item.unit}`)
                        : (item.purchasable_unit_en || `${item.purchasable_quantity || item.total_quantity} ${item.unit}`);

                      return (
                        <div
                          key={item.ingredient_id}
                          className={`px-6 py-4 flex flex-col sm:flex-row sm:items-center justify-between gap-3 transition-colors ${
                            isSittingAtHome ? "bg-amber-50/30" : "hover:bg-stone-50/50"
                          }`}
                        >
                          <div className="flex items-start gap-3 min-w-0">
                            <input
                              type="checkbox"
                              checked={isSittingAtHome}
                              onChange={() => toggleAtHome(item.ingredient_id)}
                              className="w-5 h-5 mt-0.5 rounded-md border-stone-300 text-[var(--color-primary)] focus:ring-[var(--color-primary)] cursor-pointer"
                              id={`athome_${item.ingredient_id}`}
                            />
                            <div className="space-y-0.5">
                              <label
                                htmlFor={`athome_${item.ingredient_id}`}
                                className={`text-sm font-bold cursor-pointer transition-all ${
                                  isSittingAtHome ? "text-stone-500 line-through" : "text-stone-900"
                                }`}
                              >
                                {itemName}
                              </label>
                              <div className="text-xs text-stone-500 flex items-center gap-2">
                                <span>🛒 Buy Pack: {buyUnit}</span>
                                {item.is_pantry_staple && (
                                  <span className="text-[10px] bg-amber-100 text-amber-900 px-2 py-0.5 rounded-full font-bold">
                                    🏠 Pantry Staple
                                  </span>
                                )}
                              </div>
                            </div>
                          </div>

                          <div className="text-right shrink-0">
                            {isSittingAtHome ? (
                              <span className="text-xs font-bold text-amber-800 bg-amber-50 px-3 py-1 rounded-full border border-amber-200 inline-block">
                                ✓ {language === "mm" ? "အိမ်တွင်ရှိပြီး (ဝယ်ရန်မလို)" : "Sitting at Home (Excluded)"}
                              </span>
                            ) : item.retail_package_price_mmk != null ? (
                              <span className="text-sm font-extrabold text-stone-900 block">
                                {item.retail_package_price_mmk.toLocaleString()} MMK
                              </span>
                            ) : (
                              <span className="text-xs text-stone-400">Market Rate</span>
                            )}
                          </div>
                        </div>
                      );
                    })}
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* ========================================================================================= */}
      {/* STEP 3: FINAL GROCERY LIST WITH COST AND PANTRY STOCK SAVINGS (Checklist for wet market) */}
      {/* ========================================================================================= */}
      {step === 3 && (
        <div className="space-y-6 animate-in fade-in duration-200">
          {/* Financial Summary Cards: ONLY Out-of-pocket & Pantry Savings (Portion Cost REMOVED!) */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {/* Card 1: Final Cashier Out-of-Pocket Cost */}
            <div className="bg-gradient-to-br from-[var(--color-primary)] via-stone-900 to-[var(--color-text)] text-white rounded-3xl p-6 sm:p-7 shadow-lg space-y-2 relative overflow-hidden">
              <span className="text-[11px] font-bold text-amber-300 uppercase tracking-wider block">
                {language === "mm" ? "နောက်ဆုံး စတိုးဆိုင်/ဈေးတွင် အမှန်ဝယ်ယူရမည့် စရိတ်" : "Final Cashier Out-of-Pocket Cost"}
              </span>
              <div className="flex items-baseline gap-2">
                <span className="text-3xl sm:text-4xl font-black text-white">
                  {groceryCostAfterReview.toLocaleString()}
                </span>
                <span className="text-sm font-bold text-emerald-200">MMK</span>
              </div>
              <p className="text-xs text-white/80 leading-relaxed pt-1">
                {language === "mm"
                  ? "အိမ်တွင်ရှိပြီးသား ပစ္စည်းများကို စစ်ထုတ်ပြီးနောက် စတိုးဆိုင်/ဈေးတွင် အမှန်တကယ် ကျသင့်မည့်ငွေ။"
                  : "Actual cash out-of-pocket required after excluding items sitting at home."}
              </p>
            </div>

            {/* Card 2: Pantry Stock Savings Calculation (cost before review - cost after review) */}
            <div className="bg-[var(--color-muted)]/60 border border-[var(--color-border)] rounded-3xl p-6 sm:p-7 shadow-md space-y-2">
              <div className="flex items-center justify-between">
                <span className="text-[11px] font-bold text-[var(--color-primary)] uppercase tracking-wider block">
                  {language === "mm" ? "မီးဖိုချောင်အရန် ချွေတာနိုင်မှု (Pantry Stock Savings)" : "Pantry Stock Savings"}
                </span>
                <span className="text-xs bg-white text-[var(--color-primary)] font-extrabold px-2.5 py-0.5 rounded-full border border-[var(--color-border)] shadow-2xs">
                  {pantryStockSavings > 0 ? "Saved" : "0 MMK"}
                </span>
              </div>
              <div className="flex items-baseline gap-2">
                <span className="text-3xl sm:text-4xl font-black text-[var(--color-primary)]">
                  {pantryStockSavings.toLocaleString()}
                </span>
                <span className="text-sm font-bold text-[var(--color-primary)]/80">MMK Saved</span>
              </div>
              <p className="text-xs text-stone-600 leading-relaxed pt-1">
                {language === "mm"
                  ? `(စစ်ဆေးခြင်းမပြုမီ စရိတ် ${groceryCostBeforeReview.toLocaleString()} ကျပ် - စစ်ဆေးပြီးနောက် စရိတ် ${groceryCostAfterReview.toLocaleString()} ကျပ်) ဖြင့် တွက်ချက်ထားပါသည်။`
                  : `Calculated as: Initial store cost (${groceryCostBeforeReview.toLocaleString()} MMK) - Final grocery list cost (${groceryCostAfterReview.toLocaleString()} MMK).`}
              </p>
            </div>
          </div>

          {/* Action Control Bar & Progress Meter */}
          <div className="bg-white rounded-3xl p-5 sm:p-6 border border-[var(--color-border)] shadow-sm flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
            {/* Progress Meter */}
            <div className="flex-1 w-full sm:max-w-md space-y-2">
              <div className="flex justify-between text-xs font-bold">
                <span className="text-stone-700">
                  {language === "mm" ? "ဈေးဝယ်ပြီးစီးမှု (စျေးခြင်းထဲရောက်ရှိမှု)" : "Shopping Checklist Progress"}
                </span>
                <span className="text-[var(--color-primary)] font-extrabold">
                  {purchasedCount} / {totalCount} ({progressPct}%)
                </span>
              </div>
              <div className="w-full h-3 bg-stone-100 rounded-full overflow-hidden border border-stone-200">
                <div
                  className="h-full rounded-full transition-all duration-300"
                  style={{
                    width: `${progressPct}%`,
                    backgroundColor: "var(--color-primary)",
                  }}
                />
              </div>
            </div>

            {/* Action Buttons */}
            <div className="flex flex-wrap items-center gap-2.5">
              <button
                type="button"
                onClick={() => setStep(2)}
                className="px-3.5 py-2 rounded-xl border border-stone-200 bg-stone-50 hover:bg-stone-100 text-stone-700 text-xs font-bold transition-all"
              >
                ← {language === "mm" ? "အိမ်ရှိပစ္စည်းများ ပြန်လည်စစ်ရန်" : "Review Again"}
              </button>
              <button
                type="button"
                onClick={handleCopyClipboard}
                className="px-3.5 py-2 bg-stone-100 hover:bg-stone-200 text-stone-800 font-bold text-xs rounded-xl transition-all active:scale-95 flex items-center gap-1.5"
              >
                <span>{copied ? "✓" : "📋"}</span>
                <span>{copied ? (language === "mm" ? "ကူးယူပြီး!" : "Copied!") : (language === "mm" ? "ကူးယူမည်" : "Copy List")}</span>
              </button>
              <button
                type="button"
                onClick={handlePrint}
                className="px-3.5 py-2 bg-stone-100 hover:bg-stone-200 text-stone-800 font-bold text-xs rounded-xl transition-all active:scale-95 flex items-center gap-1.5"
              >
                <span>🖨️</span>
                <span>{language === "mm" ? "ပုံနှိပ် / PDF" : "Print / PDF"}</span>
              </button>
              <button
                type="button"
                onClick={handleResetChecklist}
                className="px-3.5 py-2 bg-stone-100 hover:bg-stone-200 text-stone-600 hover:text-red-600 text-xs font-bold rounded-xl transition-all flex items-center gap-1 active:scale-95"
                title={language === "mm" ? "အမှတ်အသားများ ဖျက်မည်" : "Reset checks"}
              >
                <span>↺</span>
                <span>{language === "mm" ? "အမှတ်အသားများ ဖျက်မည်" : "Reset checks"}</span>
              </button>
            </div>
          </div>

          {/* Categorized Grocery Aisles Shopping Checklist */}
          {groceryList && (
            <div className="space-y-6">
              {groceryList.groups.map((group) => {
                const groupBuyableItems = group.items.filter(
                  (item) => !atHomeItems[item.ingredient_id] && !item.is_zero_cost_utility
                );
                if (groupBuyableItems.length === 0) return null;

                const groupName = language === "mm" ? group.category_name_mm : group.category_name_en;
                const groupSubtotal = groupBuyableItems.reduce(
                  (sum, item) => sum + (item.retail_package_price_mmk || item.estimated_price_mmk || 0),
                  0
                );

                return (
                  <div
                    key={group.category_id}
                    className="bg-white rounded-3xl border border-[var(--color-border)] overflow-hidden shadow-xs hover:shadow-md transition-shadow"
                  >
                    {/* Aisle Banner */}
                    <div className="bg-stone-50/90 px-6 py-4 border-b border-stone-100 flex items-center justify-between">
                      <div className="flex items-center gap-2.5">
                        <div
                          className="w-7 h-7 rounded-lg text-white flex items-center justify-center font-bold text-xs shadow-2xs"
                          style={{ backgroundColor: "var(--color-primary)" }}
                        >
                          {groupBuyableItems.length}
                        </div>
                        <h3 className="font-extrabold text-base text-stone-900">{groupName}</h3>
                      </div>
                      <div className="text-xs font-bold text-[var(--color-primary)] bg-[var(--color-muted)]/50 px-3 py-1 rounded-full border border-[var(--color-border)]">
                        {groupSubtotal.toLocaleString()} MMK
                      </div>
                    </div>

                    {/* Items List */}
                    <div className="divide-y divide-stone-100">
                      {groupBuyableItems.map((item) => {
                        const isChecked = !!checkedItems[item.ingredient_id];
                        const itemName = language === "mm" ? item.name_mm : item.name_en;
                        const buyUnit = language === "mm"
                          ? (item.purchasable_unit_mm || `${item.purchasable_quantity || item.total_quantity} ${item.unit}`)
                          : (item.purchasable_unit_en || `${item.purchasable_quantity || item.total_quantity} ${item.unit}`);

                        return (
                          <div
                            key={item.ingredient_id}
                            className={`px-6 py-4 flex flex-col sm:flex-row sm:items-center justify-between gap-3 transition-colors ${
                              isChecked ? "bg-stone-50/70" : "hover:bg-[var(--color-muted)]/15"
                            }`}
                          >
                            <div className="flex items-start gap-3.5 min-w-0 flex-1">
                              <input
                                type="checkbox"
                                checked={isChecked}
                                onChange={() => toggleCheck(item.ingredient_id)}
                                className="w-5 h-5 mt-0.5 rounded-md border-stone-300 text-[var(--color-primary)] focus:ring-[var(--color-primary)] cursor-pointer"
                                aria-label={`Mark ${itemName} as purchased`}
                              />
                              <div className="space-y-1">
                                <span
                                  onClick={() => toggleCheck(item.ingredient_id)}
                                  className={`text-sm sm:text-base font-bold cursor-pointer transition-all ${
                                    isChecked ? "line-through text-stone-400" : "text-stone-900"
                                  }`}
                                >
                                  {itemName}
                                </span>
                                <div className="text-xs text-stone-600 flex flex-wrap items-center gap-2">
                                  <span className="font-semibold text-[var(--color-primary)] bg-[var(--color-muted)]/40 px-2 py-0.5 rounded-md border border-[var(--color-border)]">
                                    🛒 Buy: <strong>{buyUnit}</strong>
                                  </span>
                                  {item.package_description_en && (
                                    <span className="text-stone-400 text-[11px] italic">
                                      ({language === "mm" ? item.package_description_mm : item.package_description_en})
                                    </span>
                                  )}
                                </div>
                              </div>
                            </div>

                            <div className="text-right shrink-0">
                              {item.retail_package_price_mmk != null ? (
                                <span className={`text-sm sm:text-base font-black ${isChecked ? "text-stone-400" : "text-stone-900"}`}>
                                  {item.retail_package_price_mmk.toLocaleString()} MMK
                                </span>
                              ) : (
                                <span className="text-xs text-amber-700 bg-amber-50 px-2.5 py-1 rounded-full font-bold">
                                  Market Price
                                </span>
                              )}
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      )}

      {/* ========================================================= */}
      {/* ALL ITEMS CHECKED AS BOUGHT: CELEBRATION POP-UP MODAL      */}
      {/* ========================================================= */}
      {showCelebration && (
        <div className="fixed inset-0 z-50 bg-black/60 backdrop-blur-xs flex items-center justify-center p-4 animate-in fade-in duration-300">
          <div className="bg-white rounded-3xl p-6 sm:p-8 max-w-md w-full text-center space-y-5 shadow-2xl border border-[var(--color-border)] animate-in zoom-in-95 duration-200">
            <div className="w-16 h-16 rounded-full bg-emerald-100 text-emerald-800 text-3xl mx-auto flex items-center justify-center animate-bounce shadow-md">
              🎉
            </div>
            <div className="space-y-2">
              <span className="text-xs font-bold uppercase tracking-widest text-[var(--color-primary)] block">
                {language === "mm" ? "အောင်မြင်စွာ ပြီးမြောက်ပါပြီ!" : "Shopping Complete!"}
              </span>
              <h3 className="text-2xl font-black text-stone-900">
                {language === "mm" ? "အားလုံး ဝယ်ယူပြီးပါပြီ!" : "All Items Purchased!"}
              </h3>
              <p className="text-xs sm:text-sm text-stone-600 leading-relaxed">
                {language === "mm"
                  ? "ဈေးဝယ်စာရင်းပါ ပစ္စည်းများ အားလုံးကို ဈေးခြင်းထဲသို့ အောင်မြင်စွာ ထည့်သွင်းပြီးပါပြီ။ မီးဖိုချောင်အရန် ချွေတာမှုဖြင့် ဘတ်ဂျက်ကို ထိန်းသိမ်းနိုင်ခဲ့ပါသည်။"
                  : "Great job! You have checked off every single item on your grocery list and stayed strictly on budget."}
              </p>
            </div>

            <div className="p-4 bg-[var(--color-muted)]/50 rounded-2xl border border-[var(--color-border)] text-xs font-bold text-stone-800 space-y-1">
              <div className="flex justify-between">
                <span>Total Items Bought:</span>
                <span className="font-extrabold text-[var(--color-primary)]">{totalCount} items</span>
              </div>
              <div className="flex justify-between">
                <span>Pantry Savings Achieved:</span>
                <span className="font-extrabold text-emerald-700">+{pantryStockSavings.toLocaleString()} MMK</span>
              </div>
            </div>

            <div className="flex flex-col sm:flex-row gap-2 pt-2">
              <button
                type="button"
                onClick={() => setShowCelebration(false)}
                className="w-full py-3 rounded-xl bg-stone-100 hover:bg-stone-200 text-stone-700 font-bold text-xs"
              >
                {language === "mm" ? "ပိတ်မည်" : "Close"}
              </button>
              <Link
                href="/planner"
                className="w-full py-3 rounded-xl text-white font-bold text-xs flex items-center justify-center gap-1.5 shadow-md hover:opacity-95"
                style={{ backgroundColor: "var(--color-primary)" }}
              >
                <CalendarIcon className="w-4 h-4" />
                <span>{language === "mm" ? "အပတ်စဉ် ဇယားသို့" : "Back to Planner"}</span>
              </Link>
            </div>
          </div>
        </div>
      )}

      {/* Add Recipe Modal */}
      {showAddModal && (
        <div className="fixed inset-0 z-50 bg-black/50 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-white rounded-3xl p-6 max-w-lg w-full space-y-4 shadow-2xl border border-stone-200 animate-in fade-in zoom-in-95 duration-150">
            <div className="flex items-center justify-between">
              <h3 className="text-base font-extrabold text-stone-900 flex items-center gap-2">
                <CookingPotIcon className="w-5 h-5 text-[var(--color-primary)]" />
                <span>{language === "mm" ? "ဈေးဝယ်စာရင်းသို့ ဟင်းလျာ ထည့်သွင်းရန်" : "Add Dish to Grocery List"}</span>
              </h3>
              <button
                type="button"
                onClick={() => setShowAddModal(false)}
                className="w-8 h-8 rounded-full bg-stone-100 hover:bg-stone-200 text-stone-600 flex items-center justify-center font-bold text-sm"
              >
                ✕
              </button>
            </div>

            <div className="relative">
              <input
                type="text"
                placeholder={language === "mm" ? "ဟင်းအမည် ရှာရန် (ဥပမာ- ထောပတ်၊ မုန့်ဟင်းခါး)..." : "Search recipes by name or category..."}
                value={recipeSearch}
                onChange={(e) => setRecipeSearch(e.target.value)}
                className="w-full py-2.5 pl-9 pr-3 text-xs sm:text-sm bg-stone-50 border border-stone-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)]"
                autoFocus
              />
              <SearchIcon className="w-4 h-4 text-stone-400 absolute left-3 top-3" />
            </div>

            <div className="max-h-72 overflow-y-auto divide-y divide-stone-100 border border-stone-100 rounded-xl">
              {filteredCandidates.map((cand) => {
                const isAlreadyAdded = recipeIds.includes(cand.id);
                return (
                  <div key={cand.id} className="p-3 flex items-center justify-between hover:bg-stone-50 transition-colors">
                    <div>
                      <div className="text-xs sm:text-sm font-bold text-stone-900">
                        {language === "mm" ? cand.name_mm : cand.name_en}
                      </div>
                      <span className="text-[11px] text-stone-400">
                        {language === "mm" ? cand.name_en : cand.name_mm} • {cand.category}
                      </span>
                    </div>

                    <button
                      type="button"
                      disabled={isAlreadyAdded}
                      onClick={() => handleAddRecipe(cand.id)}
                      className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
                        isAlreadyAdded
                          ? "bg-stone-100 text-stone-400 cursor-not-allowed"
                          : "text-white active:scale-95 shadow-2xs hover:opacity-90"
                      }`}
                      style={!isAlreadyAdded ? { backgroundColor: "var(--color-primary)" } : {}}
                    >
                      {isAlreadyAdded ? (language === "mm" ? "ထည့်ပြီး" : "Added") : (language === "mm" ? "+ ထည့်မည်" : "+ Add")}
                    </button>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default function GroceryListPage() {
  return (
    <Suspense fallback={<div className="p-12 text-center text-stone-400">Loading grocery list...</div>}>
      <GroceryListContent />
    </Suspense>
  );
}