"use client";

import React, { useEffect, useState, useTransition, Suspense } from "react";
import { useSearchParams, useRouter } from "next/navigation";
import { useApp } from "@/context/AppContext";
import { getRecipes, getCategories } from "@/lib/api";
import { RecipeSummary, CategoryCount } from "@/types";
import { RecipeCard } from "@/components/recipes/RecipeCard";
import {
  SearchIcon,
  CookingPotIcon,
  SparklesIcon,
  XIcon,
} from "@/components/ui/Icons";

function RecipeExplorerContent() {
  const { language, city, t } = useApp();
  const searchParams = useSearchParams();
  const router = useRouter();

  const initialSearch = searchParams.get("search") || "";
  const initialCategory = searchParams.get("category") || "";

  const [search, setSearch] = useState(initialSearch);
  const [activeCategory, setActiveCategory] = useState(initialCategory);
  const [activeDietary, setActiveDietary] = useState<string>("");
  const [recipes, setRecipes] = useState<RecipeSummary[]>([]);
  const [categories, setCategories] = useState<CategoryCount[]>([]);
  const [loading, setLoading] = useState(true);
  const [total, setTotal] = useState(0);
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

  // Fetch recipes whenever search, category, dietary, city, or page changes
  useEffect(() => {
    async function loadData() {
      try {
        setLoading(true);
        const data = await getRecipes({
          page,
          pageSize,
          search: search.trim() || undefined,
          category: activeCategory || undefined,
          dietary: activeDietary || undefined,
          city,
        });
        setRecipes(data.recipes);
        setTotal(data.total);
      } catch (err) {
        console.error("Error loading recipes:", err);
      } finally {
        setLoading(false);
      }
    }
    loadData();
  }, [search, activeCategory, activeDietary, city, page]);

  const handleClearFilters = () => {
    setSearch("");
    setActiveCategory("");
    setActiveDietary("");
    setPage(1);
    router.push("/recipes");
  };

  const totalPages = Math.ceil(total / pageSize);

  const dietaryOptions = [
    { id: "vegetarian", label: t.tag_vegetarian },
    { id: "vegan", label: t.tag_vegan },
    { id: "gluten-free", label: t.tag_gluten_free },
    { id: "convalescent_food", label: t.tag_convalescent },
    { id: "baby_food", label: t.tag_baby_food },
  ];

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-12 space-y-8">
      {/* Page Header */}
      <div className="space-y-2">
        <h1 className="text-2xl sm:text-4xl font-extrabold text-stone-900 tracking-tight">
          {t.explorer_title}
        </h1>
        <p className="text-sm sm:text-base text-stone-600">
          {t.explorer_subtitle}
        </p>
      </div>

      {/* Controls: Search & Filters */}
      <div className="space-y-4 bg-white p-5 rounded-2xl border border-stone-200 shadow-xs">
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
            placeholder={t.search_placeholder}
            className="w-full pl-11 pr-10 py-3 text-sm rounded-xl border border-stone-200 bg-stone-50/50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-emerald-600/30 focus:border-emerald-600 transition-all"
          />
          {search && (
            <button
              type="button"
              onClick={() => setSearch("")}
              className="absolute right-3.5 top-3.5 text-stone-400 hover:text-stone-600"
            >
              <XIcon className="w-4 h-4" />
            </button>
          )}
        </div>

        {/* Category Filter Pills */}
        <div className="space-y-1.5">
          <span className="text-xs font-bold text-stone-500 uppercase tracking-wider">
            {language === "mm" ? "အမျိုးအစားအလိုက် စစ်ထုတ်ရန်" : "Categories"}:
          </span>
          <div className="flex flex-wrap gap-2 pt-1">
            <button
              type="button"
              onClick={() => {
                setActiveCategory("");
                setPage(1);
              }}
              className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                activeCategory === ""
                  ? "bg-emerald-800 text-white shadow-xs"
                  : "bg-stone-100 text-stone-700 hover:bg-stone-200"
              }`}
            >
              {t.filter_all_categories} ({total})
            </button>
            {categories.map((c) => (
              <button
                key={c.category}
                type="button"
                onClick={() => {
                  setActiveCategory(activeCategory === c.category ? "" : c.category);
                  setPage(1);
                }}
                className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                  activeCategory === c.category
                    ? "bg-emerald-800 text-white shadow-xs"
                    : "bg-stone-100 text-stone-700 hover:bg-stone-200"
                }`}
              >
                {language === "mm" ? c.category_mm : c.category} ({c.count})
              </button>
            ))}
          </div>
        </div>

        {/* Dietary Filters */}
        <div className="space-y-1.5 pt-2 border-t border-stone-100">
          <span className="text-xs font-bold text-stone-500 uppercase tracking-wider">
            {language === "mm" ? "အစားအသောက် စည်းကမ်း" : "Dietary Preferences"}:
          </span>
          <div className="flex flex-wrap gap-2 pt-1">
            <button
              type="button"
              onClick={() => {
                setActiveDietary("");
                setPage(1);
              }}
              className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                activeDietary === ""
                  ? "bg-stone-800 text-white"
                  : "bg-stone-100 text-stone-700 hover:bg-stone-200"
              }`}
            >
              {t.filter_all_dietary}
            </button>
            {dietaryOptions.map((d) => (
              <button
                key={d.id}
                type="button"
                onClick={() => {
                  setActiveDietary(activeDietary === d.id ? "" : d.id);
                  setPage(1);
                }}
                className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all ${
                  activeDietary === d.id
                    ? "bg-stone-800 text-white"
                    : "bg-stone-100 text-stone-700 hover:bg-stone-200"
                }`}
              >
                {d.label}
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Results Header */}
      <div className="flex items-center justify-between text-sm text-stone-500">
        <span>
          {language === "mm"
            ? `တွေ့ရှိသော ဟင်းချက်နည်း: ${total} မျိုး (${city} ဈေးနှုန်းဖြင့်)`
            : `Showing ${recipes.length} of ${total} recipes (${city} pricing basis)`}
        </span>
        {(search || activeCategory || activeDietary) && (
          <button
            type="button"
            onClick={handleClearFilters}
            className="text-xs font-bold text-emerald-700 hover:underline"
          >
            {t.clear_filters}
          </button>
        )}
      </div>

      {/* Recipe Grid */}
      {loading ? (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {[1, 2, 3, 4, 5, 6, 7, 8].map((i) => (
            <div key={i} className="h-72 bg-stone-100 rounded-2xl animate-pulse" />
          ))}
        </div>
      ) : recipes.length === 0 ? (
        <div className="text-center py-16 bg-white rounded-2xl border border-stone-200 p-8 space-y-4">
          <CookingPotIcon className="w-12 h-12 text-stone-400 mx-auto" />
          <h3 className="text-lg font-bold text-stone-800">{t.no_recipes_found}</h3>
          <p className="text-sm text-stone-500 max-w-sm mx-auto">
            {language === "mm"
              ? "အခြားအမည် သို့မဟုတ် စစ်ထုတ်မှုများကို ပြောင်းလဲရှာဖွေကြည့်ပါ။"
              : "Try adjusting your search query or removing category/dietary filters."}
          </p>
          <button
            type="button"
            onClick={handleClearFilters}
            className="px-4 py-2 bg-emerald-800 text-white text-xs font-bold rounded-xl"
          >
            {t.clear_filters}
          </button>
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {recipes.map((r) => (
            <RecipeCard key={r.id} recipe={r} />
          ))}
        </div>
      )}

      {/* Pagination Controls */}
      {totalPages > 1 && (
        <div className="flex items-center justify-center gap-2 pt-6">
          <button
            type="button"
            disabled={page <= 1}
            onClick={() => setPage(page - 1)}
            className="px-4 py-2 rounded-lg text-sm font-semibold border border-stone-200 bg-white hover:bg-stone-50 disabled:opacity-40 disabled:cursor-not-allowed"
          >
            {language === "mm" ? "← ရှေ့သို့" : "← Previous"}
          </button>
          <span className="text-sm font-medium text-stone-600 px-3">
            {language === "mm" ? `စာမျက်နှာ ${page} / ${totalPages}` : `Page ${page} of ${totalPages}`}
          </span>
          <button
            type="button"
            disabled={page >= totalPages}
            onClick={() => setPage(page + 1)}
            className="px-4 py-2 rounded-lg text-sm font-semibold border border-stone-200 bg-white hover:bg-stone-50 disabled:opacity-40 disabled:cursor-not-allowed"
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
    <Suspense fallback={<div className="max-w-7xl mx-auto p-12 text-center text-stone-400">Loading recipe explorer...</div>}>
      <RecipeExplorerContent />
    </Suspense>
  );
}
