"use client";

import React, { Suspense, useState, useEffect } from "react";
import Link from "next/link";
import { useApp } from "@/context/AppContext";
import { 
  CookingPotIcon, 
  SparklesIcon, 
  CalendarIcon, 
  CheckCircleIcon,
  CoinsIcon
} from "@/components/ui/Icons";
import { generateGroceryList } from "@/lib/api";
import { GroceryListResponse, GroceryItem } from "@/types";

function GroceryListContent() {
  const { language, city, setCity, t } = useApp();

  const [householdSize, setHouseholdSize] = useState<number>(2);
  const [loading, setLoading] = useState<boolean>(true);
  const [groceryList, setGroceryList] = useState<GroceryListResponse | null>(null);
  const [checkedItems, setCheckedItems] = useState<Record<string, boolean>>({});
  const [copied, setCopied] = useState<boolean>(false);

  useEffect(() => {
    // Read cached recipe IDs from meal plan export
    const savedRecipesRaw = localStorage.getItem("zaychin_grocery_recipes");
    const savedHousehold = localStorage.getItem("zaychin_grocery_household");

    let recipeIds = ["R0001", "R0002", "R0003", "R0004", "R0005"]; // Default starter recipes if none
    if (savedRecipesRaw) {
      try {
        const parsed = JSON.parse(savedRecipesRaw);
        if (Array.isArray(parsed) && parsed.length > 0) {
          recipeIds = parsed;
        }
      } catch (e) {
        console.error("Error reading saved recipes:", e);
      }
    }

    const hh = savedHousehold ? parseInt(savedHousehold, 10) : 2;
    setHouseholdSize(hh);

    fetchGroceryList(recipeIds, hh, city);
  }, [city]);

  const fetchGroceryList = async (recipes: string[], hh: number, currentCity: string) => {
    setLoading(true);
    try {
      const res = await generateGroceryList({
        city: currentCity,
        household_size: hh,
        recipe_ids: recipes,
      });
      setGroceryList(res);
      // Initialize checked state from localStorage if any
      const savedChecked = localStorage.getItem(`zaychin_checked_${currentCity}`);
      if (savedChecked) {
        try {
          setCheckedItems(JSON.parse(savedChecked));
        } catch (e) {}
      }
    } catch (err) {
      console.error("Failed to load grocery list:", err);
    } finally {
      setLoading(false);
    }
  };

  const toggleCheck = (itemId: string) => {
    setCheckedItems((prev) => {
      const next = { ...prev, [itemId]: !prev[itemId] };
      localStorage.setItem(`zaychin_checked_${city}`, JSON.stringify(next));
      return next;
    });
  };

  // Calculate purchase stats
  const allItems: GroceryItem[] = groceryList ? groceryList.groups.flatMap((g) => g.items) : [];
  const totalCount = allItems.length;
  const purchasedCount = allItems.filter((i) => checkedItems[i.ingredient_id]).length;
  const progressPct = totalCount > 0 ? Math.round((purchasedCount / totalCount) * 100) : 0;

  const handleCopyClipboard = () => {
    if (!groceryList) return;
    let text = `🛒 Zay Chin (ဈေးခြင်း) — Myanmar Grocery Shopping List (${city}, ${householdSize} Persons)\n\n`;
    groceryList.groups.forEach((g) => {
      const catName = language === "mm" ? g.category_name_mm : g.category_name_en;
      text += `📍 [${catName}] (Subtotal: ${g.subtotal_mmk.toLocaleString()} MMK)\n`;
      g.items.forEach((item) => {
        const isDone = checkedItems[item.ingredient_id] ? "✓" : "☐";
        const name = language === "mm" ? item.name_mm : item.name_en;
        const price = item.estimated_price_mmk != null ? `${item.estimated_price_mmk.toLocaleString()} MMK` : "Market Price";
        text += `  ${isDone} ${name} — ${item.total_quantity} ${item.unit} (${price})\n`;
      });
      text += "\n";
    });
    text += `💰 Total Estimated Budget: ${groceryList.estimated_total_mmk.toLocaleString()} MMK\n`;
    text += `Verified Market Observations • Zero Hallucinated Pricing\n`;

    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2500);
  };

  const handlePrint = () => {
    window.print();
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-8">
      {/* Header */}
      <div className="text-center max-w-3xl mx-auto space-y-3">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 text-xs font-bold">
          <CoinsIcon className="w-4 h-4 text-emerald-700" />
          <span>{language === "mm" ? "အဆင့်ဆင့် ပေါင်းစပ်ထားသော ဈေးဝယ်စာရင်း" : "Smart Grocery Checklist"}</span>
        </div>
        <h1 className="text-3xl sm:text-4xl font-extrabold text-stone-900 tracking-tight">
          {language === "mm" ? "ဈေးဝယ်စာရင်းနှင့် ကုန်ကျစရိတ်" : "Smart Grocery List & Budgeting"}
        </h1>
        <p className="text-sm sm:text-base text-stone-600">
          {language === "mm"
            ? "ရွေးချယ်ထားသော အပတ်စဉ် ဟင်းလျာများအတွက် လိုအပ်သည့် ပါဝင်ပစ္စည်းများကို ကဏ္ဍအလိုက် စနစ်တကျ ပေါင်းစည်းပေးပြီး ရန်ကုန်/မန္တလေး ကာလပေါက်ဈေးဖြင့် စုစုပေါင်း တွက်ချက်ပေးပါသည်။"
            : "Aggregates ingredients from your meal plan, scales exact metric amounts for your family, and applies current verified market prices."}
        </p>
      </div>

      {/* Action Control Bar */}
      {groceryList && (
        <div className="bg-white rounded-3xl p-6 sm:p-8 border border-stone-200/80 shadow-xs space-y-6">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
            <div>
              <div className="flex items-center gap-2 text-xs text-emerald-800 font-bold mb-1">
                <span>{city} Market Pricing</span>
                <span>•</span>
                <span>{householdSize} Persons</span>
                <span>•</span>
                <span>{totalCount} Total Items</span>
              </div>
              <div className="flex items-baseline gap-2">
                <span className="text-3xl sm:text-4xl font-extrabold text-stone-900">
                  {groceryList.estimated_total_mmk.toLocaleString()}
                </span>
                <span className="text-sm font-bold text-stone-500">MMK Total</span>
              </div>
            </div>

            {/* Progress Meter */}
            <div className="md:w-64 space-y-2">
              <div className="flex justify-between text-xs font-bold">
                <span className="text-stone-700">
                  {language === "mm" ? "ဝယ်ယူပြီးစီးမှု" : "Shopping Progress"}
                </span>
                <span className="text-emerald-700">{purchasedCount} / {totalCount} ({progressPct}%)</span>
              </div>
              <div className="w-full h-3 bg-stone-100 rounded-full overflow-hidden border border-stone-200">
                <div
                  className="h-full bg-emerald-600 rounded-full transition-all duration-300"
                  style={{ width: `${progressPct}%` }}
                />
              </div>
            </div>

            {/* Action Buttons */}
            <div className="flex flex-wrap items-center gap-2.5">
              <button
                type="button"
                onClick={handleCopyClipboard}
                className="px-4 py-2.5 bg-stone-100 hover:bg-stone-200 text-stone-800 font-bold text-xs rounded-xl transition-all active:scale-95 flex items-center gap-1.5"
              >
                <span>{copied ? "✓" : "📋"}</span>
                <span>{copied ? (language === "mm" ? "ကူးယူပြီး!" : "Copied!") : (language === "mm" ? "စာရင်း ကူးယူမည်" : "Copy List")}</span>
              </button>
              <button
                type="button"
                onClick={handlePrint}
                className="px-4 py-2.5 bg-stone-100 hover:bg-stone-200 text-stone-800 font-bold text-xs rounded-xl transition-all active:scale-95 flex items-center gap-1.5"
              >
                <span>🖨️</span>
                <span>{language === "mm" ? "ပုံနှိပ်မည် / PDF" : "Print / PDF"}</span>
              </button>
              <Link
                href="/planner"
                className="px-4 py-2.5 bg-emerald-800 hover:bg-emerald-900 text-white font-bold text-xs rounded-xl transition-all active:scale-95 flex items-center gap-1.5 shadow-sm"
              >
                <CalendarIcon className="w-3.5 h-3.5 text-amber-300" />
                <span>{language === "mm" ? "အပတ်စဉ် ဇယားသို့" : "Back to Planner"}</span>
              </Link>
            </div>
          </div>
        </div>
      )}

      {/* Categorized Grocery Aisles */}
      {loading ? (
        <div className="p-16 text-center text-stone-400 space-y-3">
          <div className="w-10 h-10 border-4 border-emerald-700 border-t-transparent rounded-full animate-spin mx-auto" />
          <p className="text-sm font-semibold">
            {language === "mm" ? "ဈေးဝယ်စာရင်း စုစည်းနေပါသည်..." : "Aggregating ingredients & market prices..."}
          </p>
        </div>
      ) : groceryList && groceryList.groups.length > 0 ? (
        <div className="space-y-6">
          {groceryList.groups.map((group) => {
            const groupName = language === "mm" ? group.category_name_mm : group.category_name_en;
            return (
              <div
                key={group.category_id}
                className="bg-white rounded-3xl border border-stone-200 overflow-hidden shadow-xs"
              >
                {/* Group Banner */}
                <div className="bg-stone-50/80 px-6 py-4 border-b border-stone-100 flex items-center justify-between">
                  <div className="flex items-center gap-2.5">
                    <div className="w-7 h-7 rounded-lg bg-emerald-100 text-emerald-800 flex items-center justify-center font-bold text-xs">
                      {group.items.length}
                    </div>
                    <h3 className="font-extrabold text-base text-stone-900">
                      {groupName}
                    </h3>
                  </div>
                  <div className="text-xs font-bold text-emerald-800 bg-emerald-50 px-3 py-1 rounded-full border border-emerald-200/60">
                    {group.subtotal_mmk.toLocaleString()} MMK
                  </div>
                </div>

                {/* Items Table */}
                <div className="divide-y divide-stone-100">
                  {group.items.map((item) => {
                    const isChecked = !!checkedItems[item.ingredient_id];
                    const itemName = language === "mm" ? item.name_mm : item.name_en;

                    return (
                      <div
                        key={item.ingredient_id}
                        onClick={() => toggleCheck(item.ingredient_id)}
                        className={`px-6 py-3.5 flex items-center justify-between gap-4 cursor-pointer select-none transition-colors ${
                          isChecked ? "bg-stone-50/60" : "hover:bg-emerald-50/20"
                        }`}
                      >
                        {/* Checkbox & Name */}
                        <div className="flex items-center gap-3.5 min-w-0">
                          <input
                            type="checkbox"
                            checked={isChecked}
                            onChange={() => {}}
                            className="w-5 h-5 rounded-md border-stone-300 text-emerald-800 focus:ring-emerald-700 cursor-pointer"
                          />
                          <div className="min-w-0">
                            <span
                              className={`text-sm font-bold block truncate transition-all ${
                                isChecked ? "line-through text-stone-400" : "text-stone-900"
                              }`}
                            >
                              {itemName}
                            </span>
                            <span className="text-xs text-stone-500 font-semibold">
                              {item.total_quantity} {item.unit}
                            </span>
                          </div>
                        </div>

                        {/* Price & Source */}
                        <div className="text-right shrink-0 space-y-0.5">
                          {item.is_zero_cost_utility ? (
                            <span className="text-xs font-bold text-teal-700 bg-teal-50 px-2 py-0.5 rounded-full inline-block">
                              {language === "mm" ? "အိမ်သုံးရေ (၀ ကျပ်)" : "Water (0 MMK)"}
                            </span>
                          ) : item.estimated_price_mmk != null ? (
                            <div>
                              <span className={`text-sm font-extrabold block ${isChecked ? "text-stone-400" : "text-stone-900"}`}>
                                {item.estimated_price_mmk.toLocaleString()} MMK
                              </span>
                              {item.observation_source && (
                                <span className="text-[10px] text-stone-400 block">
                                  {item.observation_source}
                                </span>
                              )}
                            </div>
                          ) : (
                            <span className="text-[11px] text-amber-700 bg-amber-50 px-2 py-0.5 rounded-full font-medium inline-block">
                              {language === "mm" ? "ကာလပေါက်ဈေး" : "Market Price"}
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
      ) : null}
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
