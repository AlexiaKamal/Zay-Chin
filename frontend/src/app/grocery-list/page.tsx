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

  // Pantry Staples Mode: exclude items already stocked in kitchen cabinets (salt, sugar, oil, seasonings)
  const [excludePantry, setExcludePantry] = useState<boolean>(true);
  const [pantryOverrides, setPantryOverrides] = useState<Record<string, boolean>>({});

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

  const toggleItemPantry = (itemId: string, currentInPantry: boolean) => {
    setPantryOverrides((prev) => ({
      ...prev,
      [itemId]: !currentInPantry,
    }));
  };

  const isItemInPantry = (item: GroceryItem): boolean => {
    if (pantryOverrides[item.ingredient_id] !== undefined) {
      return pantryOverrides[item.ingredient_id];
    }
    return excludePantry && !!item.is_pantry_staple;
  };

  // Calculate purchase stats
  const allItems: GroceryItem[] = groceryList ? groceryList.groups.flatMap((g) => g.items) : [];
  const totalCount = allItems.length;
  const purchasedCount = allItems.filter((i) => checkedItems[i.ingredient_id]).length;
  const progressPct = totalCount > 0 ? Math.round((purchasedCount / totalCount) * 100) : 0;

  // Active cashier out-of-pocket cost
  const activeStoreTotal = allItems.reduce((acc, item) => {
    if (item.is_zero_cost_utility) return acc;
    if (isItemInPantry(item)) return acc;
    return acc + (item.retail_package_price_mmk || item.estimated_price_mmk || 0);
  }, 0);

  const netPortionTotal = groceryList?.estimated_total_mmk || 0;
  const fullStoreTotal = groceryList?.retail_total_mmk || 0;
  const pantrySavings = Math.max(0, fullStoreTotal - activeStoreTotal);

  const handleCopyClipboard = () => {
    if (!groceryList) return;
    let text = `🛒 Zay Chin (ဈေးခြင်း) — Smart Grocery Shopping Checklist (${city}, ${householdSize} Persons)\n\n`;
    groceryList.groups.forEach((g) => {
      const catName = language === "mm" ? g.category_name_mm : g.category_name_en;
      text += `📍 [${catName}]\n`;
      g.items.forEach((item) => {
        const inPantry = isItemInPantry(item);
        const isDone = checkedItems[item.ingredient_id] ? "✓" : "☐";
        const name = language === "mm" ? item.name_mm : item.name_en;
        const buyUnit = item.purchasable_unit_en || `${item.total_quantity} ${item.unit}`;
        const price = inPantry
          ? "Already at Home (0 MMK)"
          : item.retail_package_price_mmk != null
          ? `${item.retail_package_price_mmk.toLocaleString()} MMK`
          : "Market Price";
        text += `  ${isDone} ${name} — Buy: ${buyUnit} [Recipe uses: ${item.total_quantity} ${item.unit}] (${price})\n`;
      });
      text += "\n";
    });
    text += `💰 Out-of-Pocket Store Total: ${activeStoreTotal.toLocaleString()} MMK\n`;
    text += `🍲 Prorated Recipe Portion Value: ${netPortionTotal.toLocaleString()} MMK\n`;
    text += `Verified Retail Market Observations (CSO, Citymall, YCE) • Zero Hallucination\n`;

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
          <span>{language === "mm" ? "လက်လီထုပ်ပိုးမှုနှင့် မီးဖိုချောင်အရန် တွက်ချက်မှု" : "Retail Packaging & Smart Budgeting"}</span>
        </div>
        <h1 className="text-3xl sm:text-4xl font-extrabold text-stone-900 tracking-tight">
          {language === "mm" ? "ဈေးဝယ်စာရင်းနှင့် စတိုးဆိုင် ကုန်ကျစရိတ်" : "Smart Grocery List & Cashier Budget"}
        </h1>
        <p className="text-sm sm:text-base text-stone-600 leading-relaxed">
          {language === "mm"
            ? "ဟင်းချက်ရာတွင် ဆား (၃) ဇွန်း၊ သခွားသီး (၀.၆) လုံးသာ သုံးသော်လည်း စတိုးဆိုင်တွင် ဆား ၁ ထုပ် (၄၀၀ ဂရမ်)၊ သခွားသီး ၁ လုံး အပြည့် ဝယ်ယူရပါသည်။ ဤစနစ်က လက်လီအထုပ်လိုက် အမှန်တကယ် ကျသင့်ငွေနှင့် မီးဖိုချောင်အရန် ချွေတာနိုင်မှုကို တိကျစွာ တွက်ချက်ပေးပါသည်။"
            : "You can't buy 3 tbsp of salt or 0.6 cucumber at the store. Zay Chin calculates real out-of-pocket store packages (e.g. 400g salt, integer produce) while letting you exclude pantry staples you already stock at home."}
        </p>
      </div>

      {/* 3-Way Financial Insight Banner */}
      {groceryList && (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {/* Card 1: Out-of-pocket store cashier cost */}
          <div className="bg-gradient-to-br from-emerald-900 to-teal-900 text-white rounded-3xl p-6 shadow-md space-y-2 relative overflow-hidden">
            <span className="text-[11px] font-bold text-amber-300 uppercase tracking-wider block">
              {language === "mm" ? "စတိုးဆိုင်/ဈေးတွင် အမှန်ဝယ်ယူရမည့် စရိတ်" : "Cashier Out-of-Pocket Total"}
            </span>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl sm:text-4xl font-black text-white">
                {activeStoreTotal.toLocaleString()}
              </span>
              <span className="text-sm font-bold text-emerald-200">MMK</span>
            </div>
            <p className="text-xs text-emerald-100/80 leading-relaxed pt-1">
              {language === "mm"
                ? "အလုံးလိုက်နှင့် လက်လီအထုပ်လိုက် အမှန်တကယ် ဝယ်ယူရမည့် ငွေပမာဏ။"
                : "Real money handed to the cashier for whole pieces and purchasable store packs."}
            </p>
          </div>

          {/* Card 2: Net Recipe Portion Consumption Value */}
          <div className="bg-white rounded-3xl p-6 border border-stone-200 shadow-xs space-y-2">
            <span className="text-[11px] font-bold text-stone-400 uppercase tracking-wider block">
              {language === "mm" ? "ချက်ပြုတ်စားသုံးမှု အမှန်တန်ဖိုး (Portion Cost)" : "Net Recipe Portion Value"}
            </span>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl sm:text-4xl font-black text-stone-900">
                {netPortionTotal.toLocaleString()}
              </span>
              <span className="text-sm font-bold text-stone-500">MMK</span>
            </div>
            <p className="text-xs text-stone-500 leading-relaxed pt-1">
              {language === "mm"
                ? "ဟင်းချက်ရာတွင် အမှန်တကယ် ကုန်ဆုံးသွားသည့် ဂရမ်/မီလီ ပမာဏတန်ဖိုး။"
                : "Exact prorated value of ingredients consumed in the cooked meals."}
            </p>
          </div>

          {/* Card 3: Pantry Staples Savings */}
          <div className="bg-emerald-50/70 border border-emerald-200/80 rounded-3xl p-6 space-y-2">
            <span className="text-[11px] font-bold text-emerald-800 uppercase tracking-wider block">
              {language === "mm" ? "မီးဖိုချောင်အရန် ချွေတာနိုင်မှု" : "Pantry Stock Savings"}
            </span>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl sm:text-4xl font-black text-emerald-800">
                {pantrySavings.toLocaleString()}
              </span>
              <span className="text-sm font-bold text-emerald-600">MMK Saved</span>
            </div>
            <p className="text-xs text-emerald-800/80 leading-relaxed pt-1">
              {language === "mm"
                ? "ဆား၊ ဆီ၊ သကြား စသည့် မီးဖိုချောင်အရန်များ အိမ်တွင်ရှိပြီးဖြစ်၍ သက်သာသွားသောငွေ။"
                : "Saved by utilizing recurring household pantry staples already in stock."}
            </p>
          </div>
        </div>
      )}

      {/* Pantry Staples Master Toggle Banner */}
      {groceryList && (
        <div className="bg-white rounded-3xl p-5 sm:p-6 border border-stone-200 shadow-xs flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <div className="flex items-center gap-3.5">
            <div className="w-10 h-10 rounded-2xl bg-amber-100 text-amber-900 flex items-center justify-center text-lg font-bold shrink-0">
              🏠
            </div>
            <div>
              <h3 className="text-sm sm:text-base font-extrabold text-stone-900">
                {language === "mm"
                  ? "မီးဖိုချောင်သုံး အရန်ပစ္စည်းများ စစ်ထုတ်မှု (Pantry Staples Mode)"
                  : "Smart Pantry Staples Mode"}
              </h3>
              <p className="text-xs text-stone-500 leading-relaxed">
                {language === "mm"
                  ? "အိမ်တွင် ဆား၊ ဆီ၊ သကြား၊ ငါးငံပြာရည် စသည့် ဟင်းခတ်ပစ္စည်းများ ရှိပြီးဖြစ်ပါသလား။ ချန်လှပ်ထားခြင်းဖြင့် မလိုလားအပ်သော ကုန်ကျစရိတ်ကို ဖယ်ထုတ်ပေးပါသည်။"
                  : "Automatically excludes recurring household staples (salt, sugar, cooking oil, soy sauce) from your shopping checkout."}
              </p>
            </div>
          </div>

          <div className="flex items-center gap-3 shrink-0">
            <button
              type="button"
              onClick={() => setExcludePantry(!excludePantry)}
              className={`px-4 py-2.5 rounded-xl text-xs font-bold transition-all shadow-xs flex items-center gap-2 ${
                excludePantry
                  ? "bg-emerald-800 text-white hover:bg-emerald-900"
                  : "bg-stone-100 text-stone-700 hover:bg-stone-200 border border-stone-200"
              }`}
            >
              <span>{excludePantry ? "✓" : "○"}</span>
              <span>
                {excludePantry
                  ? (language === "mm" ? "မီးဖိုချောင်အရန် ချန်လှပ်ထားသည်" : "Pantry Items Excluded")
                  : (language === "mm" ? "အထုပ်လိုက် အားလုံးဝယ်မည်" : "Include All Packages")}
              </span>
            </button>
          </div>
        </div>
      )}

      {/* Action Control Bar */}
      {groceryList && (
        <div className="bg-white rounded-3xl p-5 sm:p-6 border border-stone-200/80 shadow-xs flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          {/* Progress Meter */}
          <div className="flex-1 w-full sm:max-w-md space-y-2">
            <div className="flex justify-between text-xs font-bold">
              <span className="text-stone-700">
                {language === "mm" ? "ဈေးဝယ်ပြီးစီးမှု" : "Shopping Checklist Progress"}
              </span>
              <span className="text-emerald-800">
                {purchasedCount} / {totalCount} ({progressPct}%)
              </span>
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
                    const inPantry = isItemInPantry(item);
                    const itemName = language === "mm" ? item.name_mm : item.name_en;
                    const buyUnit = language === "mm"
                      ? (item.purchasable_unit_mm || `${item.purchasable_quantity || item.total_quantity} ${item.unit}`)
                      : (item.purchasable_unit_en || `${item.purchasable_quantity || item.total_quantity} ${item.unit}`);

                    return (
                      <div
                        key={item.ingredient_id}
                        className={`px-6 py-4 flex flex-col sm:flex-row sm:items-center justify-between gap-3 transition-colors ${
                          isChecked ? "bg-stone-50/70" : inPantry ? "bg-teal-50/20" : "hover:bg-emerald-50/20"
                        }`}
                      >
                        {/* Checkbox & Item Details */}
                        <div className="flex items-start gap-3.5 min-w-0 flex-1">
                          <input
                            type="checkbox"
                            checked={isChecked}
                            onChange={() => toggleCheck(item.ingredient_id)}
                            className="w-5 h-5 mt-0.5 rounded-md border-stone-300 text-emerald-800 focus:ring-emerald-700 cursor-pointer"
                            aria-label={`Mark ${itemName} as purchased`}
                          />
                          <div className="min-w-0 space-y-1">
                            <div className="flex flex-wrap items-center gap-2">
                              <span
                                onClick={() => toggleCheck(item.ingredient_id)}
                                className={`text-sm sm:text-base font-bold cursor-pointer transition-all ${
                                  isChecked ? "line-through text-stone-400" : "text-stone-900"
                                }`}
                              >
                                {itemName}
                              </span>
                              {item.is_pantry_staple && (
                                <span className="inline-flex items-center gap-1 text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-50 text-amber-800 border border-amber-200">
                                  <span>🏠</span>
                                  <span>{language === "mm" ? "မီးဖိုချောင်သုံး" : "Pantry Staple"}</span>
                                </span>
                              )}
                              {inPantry && (
                                <span className="inline-flex items-center gap-1 text-[10px] font-bold px-2 py-0.5 rounded-full bg-teal-50 text-teal-800 border border-teal-200">
                                  <span>✓</span>
                                  <span>{language === "mm" ? "အိမ်တွင်ရှိပြီး (၀ ကျပ်)" : "In Pantry (0 MMK)"}</span>
                                </span>
                              )}
                            </div>

                            {/* Dual Display: Store Purchasing Pack vs Recipe Requirement */}
                            <div className="text-xs text-stone-600 flex flex-wrap items-center gap-x-3 gap-y-1">
                              <span className="font-semibold text-emerald-900 bg-emerald-50 px-2 py-0.5 rounded-md border border-emerald-200/50">
                                🛒 {language === "mm" ? "ဝယ်ယူရန်" : "Buy"}: <strong>{buyUnit}</strong>
                              </span>
                              <span className="text-stone-400">
                                •
                              </span>
                              <span className="text-stone-500 font-medium">
                                🍲 {language === "mm" ? "ဟင်းချက်ရန် လိုအပ်ချက်" : "Recipe needed"}: {item.total_quantity} {item.unit}
                              </span>
                            </div>

                            {item.package_description_en && (
                              <p className="text-[11px] text-stone-400 italic">
                                {language === "mm" ? item.package_description_mm : item.package_description_en}
                              </p>
                            )}
                          </div>
                        </div>

                        {/* Price Column & Pantry Override Toggle */}
                        <div className="text-right shrink-0 space-y-1 sm:pl-4">
                          {item.is_zero_cost_utility ? (
                            <span className="text-xs font-bold text-teal-700 bg-teal-50 px-2.5 py-1 rounded-full inline-block">
                              {language === "mm" ? "အိမ်သုံးရေ (၀ ကျပ်)" : "Water (0 MMK)"}
                            </span>
                          ) : inPantry ? (
                            <div className="space-y-0.5">
                              <span className="text-xs font-bold text-teal-800 bg-teal-50 px-2.5 py-1 rounded-full border border-teal-200 inline-block">
                                0 MMK (Stocked)
                              </span>
                              <button
                                type="button"
                                onClick={() => toggleItemPantry(item.ingredient_id, inPantry)}
                                className="block text-[10px] text-stone-400 hover:text-emerald-800 hover:underline"
                              >
                                {language === "mm" ? "အသစ်ဝယ်ယူမည်လား?" : "Need to buy new?"}
                              </button>
                            </div>
                          ) : item.retail_package_price_mmk != null ? (
                            <div className="space-y-0.5">
                              <span className={`text-sm sm:text-base font-black block ${isChecked ? "text-stone-400" : "text-stone-900"}`}>
                                {item.retail_package_price_mmk.toLocaleString()} MMK
                              </span>
                              {item.estimated_price_mmk != null && (
                                <span className="text-[10px] text-stone-400 block font-normal">
                                  {language === "mm" ? "စားသုံးမှုတန်ဖိုး" : "Portion value"}: ~{item.estimated_price_mmk.toLocaleString()} MMK
                                </span>
                              )}
                              {item.is_pantry_staple && (
                                <button
                                  type="button"
                                  onClick={() => toggleItemPantry(item.ingredient_id, inPantry)}
                                  className="text-[10px] text-teal-700 hover:underline font-medium block"
                                >
                                  {language === "mm" ? "အိမ်တွင် ရှိပြီးဖြစ်သည်" : "Already have at home?"}
                                </button>
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
