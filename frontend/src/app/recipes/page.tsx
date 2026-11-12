"use client";

import React, { useEffect, useState, useMemo, Suspense } from "react";
import { useSearchParams, useRouter } from "next/navigation";
import { useApp } from "@/context/AppContext";
import { getRecipes, getCategories } from "@/lib/api";
import { RecipeSummary, CategoryCount } from "@/types";
import { RecipeCard } from "@/components/recipes/RecipeCard";
import {
  SearchIcon,
  CookingPotIcon,
  XIcon,
  ClockIcon,
} from "@/components/ui/Icons";
import { computeRecipeDifficulty, DifficultyLevel } from "@/lib/recipe-difficulty";

function RecipeExplorerContent() {
  const { language, city, t, userProfile } = useApp();
  const searchParams = useSearchParams();
  const router = useRouter();

  const initialSearch = searchParams.get("search") || "";
  const initialCategory = searchParams.get("category") || "";

  const [search, setSearch] = useState(initialSearch);
  const [activeCategory, setActiveCategory] = useState(initialCategory);
  const [activeDifficulty, setActiveDifficulty] = useState<DifficultyLevel | "all">(
    userProfile?.cooking_time_preference && userProfile.cooking_time_preference !== "any"
      ? (userProfile.cooking_time_preference as DifficultyLevel)
      : "all"
  );
  const [recipes, setRecipes] = useState<RecipeSummary[]>([]);
  const [categories, setCategories] = useState<CategoryCount[]>([]);
  const [loading, setLoading] = useState(true);
  const [page, setPage] = useState(1);
  const pageSize = 12;

  // Load categories once
  useEffect(() => {
    async function loadCats() {
      try {
        const cats = await getCategories();
        setCategories(cats);
      } catch (err) {
        console.error("Error fetching categories:", err);
      }
    }
    loadCats();
  }, []);

  // Fetch all recipes for city
  useEffect(() => {
    async function loadData() {
      try {
        setLoading(true);
        // Fetch up to 200 recipes so client can accurately filter by difficulty & category
        const data = await getRecipes({
          page: 1,
          pageSize: 200,
          search: search.trim() || undefined,
          category: activeCategory || undefined,
          city,
        });
        setRecipes(data.recipes);
      } catch (err) {
        console.error("Error loading recipes:", err);
      } finally {
        setLoading(false);
      }
    }
    loadData();
  }, [search, activeCategory, city]);

  // Filter by Difficulty (Easy, Medium, Hard)
  const filteredRecipes = useMemo(() => {
    if (activeDifficulty === "all") return recipes;
    return recipes.filter((r) => {
      const diff = computeRecipeDifficulty(r);
      return diff.difficulty === activeDifficulty;
    });
  }, [recipes, activeDifficulty]);

  // Paginated slice
  const totalPages = Math.ceil(filteredRecipes.length / pageSize) || 1;
  const paginatedRecipes = useMemo(() => {
    const start = (page - 1) * pageSize;
    return filteredRecipes.slice(start, start + pageSize);
  }, [filteredRecipes, page, pageSize]);

  const handleClearFilters = () => {
    setSearch("");
    setActiveCategory("");
    setActiveDifficulty("all");
    setPage(1);
    router.push("/recipes");
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-10 space-y-6">
      {/* Page Header - Clean & Simple */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-stone-200/80 pb-4">
        <div>
          <h1 className="text-2xl sm:text-3xl font-black text-stone-900 tracking-tight">
            {language === "mm" ? "ဟင်းချက်နည်းများ ရှာဖွေရန်" : "Recipe Explorer"}
          </h1>
          <p className="text-xs sm:text-sm text-stone-500">
            {language === "mm"
              ? "ဒေါ်စန်းလေး၏ မြန်မာ့ရိုးရာ ၁၇၁ မျိုးသော ဟင်းချက်နည်းများနှင့် ဈေးနှုန်းများ"
              : "Explore 171 authentic Myanmar home recipes with real wet market prices"}
          </p>
        </div>

        <span className="text-xs font-bold text-stone-600 bg-stone-100 px-3 py-1.5 rounded-xl self-start sm:self-auto">
          {language === "mm" ? `စုစုပေါင်း ${filteredRecipes.length} မျိုး` : `${filteredRecipes.length} recipes`}
        </span>
      </div>

      {/* Simplified Controls: Search & Difficulty & Category */}
      <div className="bg-white p-4 sm:p-5 rounded-3xl border border-stone-200 shadow-xs space-y-4">
        {/* Search Bar */}
        <div className="relative">
          <SearchIcon className="w-5 h-5 absolute left-3.5 top-3.5 text-stone-400" />
          <input
            type="text"
            value={search}
            onChange={(e) => {
              setSearch(e.target.value);
              setPage(1);
            }}
            placeholder={
              language === "mm"
                ? "ဟင်းအမည် သို့မဟုတ် ပါဝင်ပစ္စည်းဖြင့် ရှာဖွေပါ (ဥပမာ - ကြက်သား၊ ချဉ်ပေါင်)..."
                : "Search by dish name or ingredient (e.g. Chicken, Roselle)..."
            }
            className="w-full pl-11 pr-10 py-3 text-sm rounded-2xl border border-stone-200 bg-stone-50/60 focus:bg-white focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] transition-all"
          />
          {search && (
            <button
              type="button"
              onClick={() => {
                setSearch("");
                setPage(1);
              }}
              className="absolute right-3.5 top-3.5 text-stone-400 hover:text-stone-600"
            >
              <XIcon className="w-4 h-4" />
            </button>
          )}
        </div>

        {/* Cooking Time / Difficulty Filter Pills */}
        <div className="space-y-1.5">
          <div className="flex items-center gap-1.5 text-xs font-bold text-stone-500 uppercase tracking-wider">
            <ClockIcon className="w-3.5 h-3.5" />
            <span>{language === "mm" ? "ချက်ပြုတ်ချိန်နှင့် အဆင့်" : "Cooking Difficulty"}:</span>
          </div>
          <div className="flex flex-wrap gap-2">
            {[
              { id: "all" as const, label_en: "All Difficulties", label_mm: "အားလုံး" },
              { id: "easy" as const, label_en: "🟢 Easy (≤ 25m)", label_mm: "🟢 လွယ်ကူ (≤ ၂၅ မိနစ်)" },
              { id: "medium" as const, label_en: "🟡 Medium (25-45m)", label_mm: "🟡 အလယ်အလတ် (၂၅-၄၅ မိနစ်)" },
              { id: "hard" as const, label_en: "🔴 Hard (45m+)", label_mm: "🔴 အချိန်ယူရ (၄၅ မိနစ်ထက်ကျော်)" },
            ].map((d) => (
              <button
                key={d.id}
                type="button"
                onClick={() => {
                  setActiveDifficulty(d.id);
                  setPage(1);
                }}
                className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all shadow-2xs ${
                  activeDifficulty === d.id
                    ? "text-white shadow-xs"
                    : "bg-stone-100 text-stone-700 hover:bg-stone-200"
                }`}
                style={activeDifficulty === d.id ? { backgroundColor: "var(--color-primary)" } : {}}
              >
                {language === "mm" ? d.label_mm : d.label_en}
              </button>
            ))}
          </div>
        </div>

        {/* Categories Pills */}
        <div className="space-y-1.5 pt-2 border-t border-stone-100">
          <span className="text-xs font-bold text-stone-500 uppercase tracking-wider block">
            {language === "mm" ? "အမျိုးအစား" : "Category"}:
          </span>
          <div className="flex flex-wrap gap-1.5 max-h-28 overflow-y-auto pr-1">
            <button
              type="button"
              onClick={() => {
                setActiveCategory("");
                setPage(1);
              }}
              className={`px-3 py-1 rounded-lg text-xs font-semibold transition-all ${
                activeCategory === ""
                  ? "bg-stone-900 text-white"
                  : "bg-stone-100 text-stone-700 hover:bg-stone-200"
              }`}
            >
              {language === "mm" ? "အားလုံး" : "All"}
            </button>
            {categories.map((c) => (
              <button
                key={c.category}
                type="button"
                onClick={() => {
                  setActiveCategory(activeCategory === c.category ? "" : c.category);
                  setPage(1);
                }}
                className={`px-3 py-1 rounded-lg text-xs font-semibold transition-all ${
                  activeCategory === c.category
                    ? "bg-stone-900 text-white"
                    : "bg-stone-100 text-stone-700 hover:bg-stone-200"
                }`}
              >
                {language === "mm" ? c.category_mm : c.category} ({c.count})
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Results Subheader */}
      <div className="flex items-center justify-between text-xs sm:text-sm text-stone-500">
        <span>
          {language === "mm"
            ? `${filteredRecipes.length} မျိုး တွေ့ရှိပါသည်`
            : `Showing ${paginatedRecipes.length} of ${filteredRecipes.length} recipes`}
        </span>
        {(search || activeCategory || activeDifficulty !== "all") && (
          <button
            type="button"
            onClick={handleClearFilters}
            className="text-xs font-bold hover:underline"
            style={{ color: "var(--color-primary)" }}
          >
            {language === "mm" ? "စစ်ထုတ်မှုများ အားလုံးရှင်းမည် ✕" : "Clear filters ✕"}
          </button>
        )}
      </div>

      {/* Recipe Grid (showImage={false} ensures NO PICTURES on Recipe Explorer page) */}
      {loading ? (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 sm:gap-6">
          {[1, 2, 3, 4, 5, 6, 7, 8].map((i) => (
            <div key={i} className="h-56 bg-stone-100 rounded-3xl animate-pulse" />
          ))}
        </div>
      ) : paginatedRecipes.length === 0 ? (
        <div className="text-center py-16 bg-white rounded-3xl border border-stone-200 p-8 space-y-4 shadow-xs">
          <CookingPotIcon className="w-12 h-12 text-stone-400 mx-auto" />
          <h3 className="text-lg font-bold text-stone-800">
            {language === "mm" ? "ကိုက်ညီသော ဟင်းချက်နည်း မတွေ့ရှိပါ" : "No recipes found"}
          </h3>
          <p className="text-xs sm:text-sm text-stone-500 max-w-sm mx-auto">
            {language === "mm"
              ? "အခြားအမည် သို့မဟုတ် ချက်ပြုတ်ချိန် အဆင့်ကို ပြောင်းလဲစစ်ထုတ်ကြည့်ပါ။"
              : "Try adjusting your search keywords or cooking difficulty filter."}
          </p>
          <button
            type="button"
            onClick={handleClearFilters}
            className="px-4 py-2 text-white text-xs font-bold rounded-xl shadow-xs"
            style={{ backgroundColor: "var(--color-primary)" }}
          >
            {language === "mm" ? "မူလအတိုင်း ပြန်ပြမည်" : "Reset Filters"}
          </button>
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 sm:gap-6">
          {paginatedRecipes.map((r) => (
            <RecipeCard key={r.id} recipe={r} showImage={false} />
          ))}
        </div>
      )}

      {/* Pagination Controls */}
      {totalPages > 1 && (
        <div className="flex items-center justify-center gap-2 pt-4">
          <button
            type="button"
            disabled={page <= 1}
            onClick={() => setPage(page - 1)}
            className="px-4 py-2 rounded-xl text-xs sm:text-sm font-bold border border-stone-200 bg-white hover:bg-stone-50 disabled:opacity-40 disabled:cursor-not-allowed transition-all"
          >
            {language === "mm" ? "← ရှေ့သို့" : "← Previous"}
          </button>
          <span className="text-xs sm:text-sm font-semibold text-stone-600 px-3">
            {language === "mm"
              ? `စာမျက်နှာ ${page} / ${totalPages}`
              : `Page ${page} of ${totalPages}`}
          </span>
          <button
            type="button"
            disabled={page >= totalPages}
            onClick={() => setPage(page + 1)}
            className="px-4 py-2 rounded-xl text-xs sm:text-sm font-bold border border-stone-200 bg-white hover:bg-stone-50 disabled:opacity-40 disabled:cursor-not-allowed transition-all"
          >
            {language === "mm" ? "နောက်သို့ →" : "Next →"}
          </button>
        </div>
      )}
    </div>
  );
}

export default function RecipeExplorerPage() {
  return (
    <Suspense
      fallback={
        <div className="max-w-7xl mx-auto p-12 text-center text-stone-400">
          Loading recipes...
        </div>
      }
    >
      <RecipeExplorerContent />
    </Suspense>
  );
}
