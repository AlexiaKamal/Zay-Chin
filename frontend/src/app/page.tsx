"use client";

import React, { useEffect, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useApp } from "@/context/AppContext";
import { getRecipes } from "@/lib/api";
import { RecipeSummary } from "@/types";
import { RecipeCard } from "@/components/recipes/RecipeCard";
import {
  CookingPotIcon,
  SearchIcon,
  CoinsIcon,
  FlameIcon,
  CalendarIcon,
  ShoppingBagIcon,
  SparklesIcon,
  CheckIcon,
  ChevronRightIcon,
} from "@/components/ui/Icons";

export default function HomePage() {
  const { language, city, t } = useApp();
  const router = useRouter();
  const [featuredRecipes, setFeaturedRecipes] = useState<RecipeSummary[]>([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadFeatured() {
      try {
        setLoading(true);
        // Load top 6 featured recipes for the selected city
        const data = await getRecipes({ page: 1, pageSize: 6, city });
        setFeaturedRecipes(data.recipes);
      } catch (err) {
        console.error("Error loading featured recipes:", err);
      } finally {
        setLoading(false);
      }
    }
    loadFeatured();
  }, [city]);

  const handleHeroSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      router.push(`/recipes?search=${encodeURIComponent(searchQuery.trim())}`);
    } else {
      router.push("/recipes");
    }
  };

  return (
    <div className="space-y-16 sm:space-y-24">
      {/* Hero Section */}
      <section className="relative overflow-hidden bg-gradient-to-b from-emerald-900 via-emerald-800 to-teal-950 text-white pt-16 pb-20 sm:pt-24 sm:pb-28">
        <div className="absolute inset-0 opacity-10 bg-[radial-gradient(#34d399_1px,transparent_1px)] [background-size:16px_16px]" />
        
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-8">
          {/* Badge */}
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-emerald-700/60 border border-emerald-500/40 text-emerald-200 text-xs sm:text-sm font-semibold backdrop-blur-xs">
            <SparklesIcon className="w-4 h-4 text-amber-300" />
            <span>
              {language === "mm"
                ? "စစ်မှန်သော ရိုးရာဟင်းလျာ ၁၇၁ မျိုး • ၂၀၂၆ ကာလပေါက်ဈေးနှုန်းများ"
                : "171 Authentic Recipes • Verified 2026 Market Pricing"}
            </span>
          </div>

          {/* Headline */}
          <h1 className="text-3xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight max-w-4xl mx-auto leading-tight sm:leading-snug">
            {t.hero_title}
          </h1>

          {/* Subtitle */}
          <p className="text-base sm:text-xl text-emerald-100/90 max-w-2xl mx-auto font-normal leading-relaxed">
            {t.hero_subtitle}
          </p>

          {/* Quick Search Form */}
          <div className="max-w-2xl mx-auto pt-2">
            <form onSubmit={handleHeroSearch} className="flex items-center bg-white rounded-2xl shadow-xl p-2 border border-emerald-300/50">
              <div className="pl-3 pr-2 text-stone-400">
                <SearchIcon className="w-5 h-5 text-emerald-700" />
              </div>
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder={t.search_placeholder}
                className="w-full py-2.5 text-sm sm:text-base text-stone-800 placeholder-stone-400 bg-transparent focus:outline-none"
              />
              <button
                type="submit"
                className="px-5 py-2.5 bg-emerald-700 hover:bg-emerald-800 text-white text-sm font-bold rounded-xl transition-all shadow-md shrink-0 flex items-center gap-1.5"
              >
                <span>{language === "mm" ? "ရှာဖွေမည်" : "Search"}</span>
              </button>
            </form>
          </div>

          {/* Action CTAs */}
          <div className="flex flex-wrap items-center justify-center gap-4 pt-2">
            <Link
              href="/planner"
              className="px-6 py-3.5 rounded-xl bg-amber-500 hover:bg-amber-600 text-stone-950 font-extrabold text-sm shadow-lg shadow-amber-600/30 transition-transform active:scale-95 flex items-center gap-2"
            >
              <CalendarIcon className="w-4 h-4" />
              <span>{t.btn_start_planning}</span>
            </Link>
            <Link
              href="/recipes"
              className="px-6 py-3.5 rounded-xl bg-emerald-800/80 hover:bg-emerald-800 text-white font-semibold text-sm border border-emerald-600 transition-colors flex items-center gap-2"
            >
              <CookingPotIcon className="w-4 h-4 text-emerald-300" />
              <span>{t.btn_explore_recipes}</span>
            </Link>
          </div>
        </div>
      </section>

      {/* Metrics Banner */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 p-6 bg-white rounded-2xl border border-stone-200 shadow-xs">
          <div className="text-center p-3">
            <div className="text-2xl sm:text-3xl font-extrabold text-emerald-800">171</div>
            <div className="text-xs sm:text-sm text-stone-600 font-medium mt-1">
              {language === "mm" ? "ဒေါ်စန်းလေး ဟင်းချက်နည်းများ" : "Authentic Myanmar Dishes"}
            </div>
          </div>
          <div className="text-center p-3 border-l border-stone-100">
            <div className="text-2xl sm:text-3xl font-extrabold text-emerald-800">221</div>
            <div className="text-xs sm:text-sm text-stone-600 font-medium mt-1">
              {language === "mm" ? "ဓာတ်ခွဲခန်း အာဟာရပရိုဖိုင်" : "Lab Nutrition Profiles"}
            </div>
          </div>
          <div className="text-center p-3 border-l border-stone-100">
            <div className="text-2xl sm:text-3xl font-extrabold text-emerald-800">134</div>
            <div className="text-xs sm:text-sm text-stone-600 font-medium mt-1">
              {language === "mm" ? "၂၀၂၆ ဈေးကွက် စစ်တမ်းမှတ်တမ်း" : "Verified 2026 Price Records"}
            </div>
          </div>
          <div className="text-center p-3 border-l border-stone-100">
            <div className="text-2xl sm:text-3xl font-extrabold text-emerald-800">0%</div>
            <div className="text-xs sm:text-sm text-stone-600 font-medium mt-1">
              {language === "mm" ? "လုပ်ကြံဈေးနှုန်း လုံးဝမပါ" : "Synthetic Hallucinated Pricing"}
            </div>
          </div>
        </div>
      </section>

      {/* Featured Recipes Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
        <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4">
          <div>
            <span className="text-xs font-bold text-emerald-700 tracking-wider uppercase">
              {language === "mm" ? "အထူးရွေးချယ်ထားသော ဟင်းလျာများ" : "Curated Selections"}
            </span>
            <h2 className="text-2xl sm:text-3xl font-extrabold text-stone-900 mt-1">
              {language === "mm" ? "နာမည်ကျော် မြန်မာ့ရိုးရာ ဟင်းချက်နည်းများ" : "Featured Authentic Myanmar Recipes"}
            </h2>
          </div>
          <Link
            href="/recipes"
            className="inline-flex items-center gap-1.5 text-sm font-bold text-emerald-700 hover:text-emerald-800 transition-colors"
          >
            <span>{language === "mm" ? "အားလုံး ကြည့်ရှုမည်" : "View All 171 Recipes"}</span>
            <ChevronRightIcon className="w-4 h-4" />
          </Link>
        </div>

        {loading ? (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {[1, 2, 3, 4, 5, 6].map((i) => (
              <div key={i} className="h-64 bg-stone-100 rounded-2xl animate-pulse" />
            ))}
          </div>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {featuredRecipes.map((r) => (
              <RecipeCard key={r.id} recipe={r} />
            ))}
          </div>
        )}
      </section>

      {/* How It Works Section */}
      <section className="bg-emerald-50/60 border-y border-emerald-100 py-16 sm:py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
          <div className="text-center max-w-2xl mx-auto space-y-3">
            <h2 className="text-2xl sm:text-3xl font-extrabold text-stone-900">
              {t.how_title}
            </h2>
            <p className="text-stone-600 text-sm sm:text-base">
              {t.how_subtitle}
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-white p-7 rounded-2xl border border-stone-200/80 shadow-xs space-y-4">
              <div className="w-12 h-12 rounded-xl bg-emerald-100 text-emerald-800 flex items-center justify-center font-extrabold text-lg">
                1
              </div>
              <h3 className="text-lg font-bold text-stone-900">
                {t.step1_title}
              </h3>
              <p className="text-sm text-stone-600 leading-relaxed">
                {t.step1_desc}
              </p>
            </div>

            <div className="bg-white p-7 rounded-2xl border border-stone-200/80 shadow-xs space-y-4">
              <div className="w-12 h-12 rounded-xl bg-amber-100 text-amber-800 flex items-center justify-center font-extrabold text-lg">
                2
              </div>
              <h3 className="text-lg font-bold text-stone-900">
                {t.step2_title}
              </h3>
              <p className="text-sm text-stone-600 leading-relaxed">
                {t.step2_desc}
              </p>
            </div>

            <div className="bg-white p-7 rounded-2xl border border-stone-200/80 shadow-xs space-y-4">
              <div className="w-12 h-12 rounded-xl bg-teal-100 text-teal-800 flex items-center justify-center font-extrabold text-lg">
                3
              </div>
              <h3 className="text-lg font-bold text-stone-900">
                {t.step3_title}
              </h3>
              <p className="text-sm text-stone-600 leading-relaxed">
                {t.step3_desc}
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Seasonal & Festival Recommendations Callout */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="bg-gradient-to-r from-amber-500/10 via-emerald-500/10 to-teal-500/10 rounded-3xl p-8 sm:p-12 border border-emerald-200 flex flex-col md:flex-row items-center justify-between gap-8">
          <div className="space-y-3 max-w-xl">
            <span className="px-3 py-1 rounded-full text-xs font-extrabold bg-amber-100 text-amber-900 inline-block">
              {language === "mm" ? "ရာသီပေါ်နှင့် ပွဲတော် အစားအစာများ" : "Seasonal & Cultural Delicacies"}
            </span>
            <h3 className="text-2xl sm:text-3xl font-extrabold text-stone-900">
              {language === "mm" ? "သင်္ကြန်၊ သီတင်းကျွတ်နှင့် ရာသီဥတုအလိုက် အထူးဟင်းလျာများ" : "Thingyan, Thadingyut & Seasonal Traditional Specialties"}
            </h3>
            <p className="text-sm text-stone-600 leading-relaxed">
              {language === "mm"
                ? "မိုးတွင်းဟင်းရည်များ၊ နွေရာသီ မန်ကျည်းရွက်သုပ်၊ မုန့်လုံးရေပေါ် နှင့် အလှူမင်္ဂလာပွဲ ထောပတ်ထမင်း အပါအဝင် ရာသီအလိုက် အသင့်တော်ဆုံး ဟင်းလျာများကို ဈေးခြင်း တွင် စီစဉ်နိုင်ပါသည်။"
                : "Explore seasonal monsoon soups, summer mango salads, Thingyan sweet dumplings, and ceremonial feast curries tagged with cultural contexts."}
            </p>
          </div>
          <Link
            href="/recipes"
            className="px-6 py-3.5 bg-emerald-800 hover:bg-emerald-900 text-white font-bold text-sm rounded-xl shadow-md shrink-0 transition-transform active:scale-95"
          >
            {language === "mm" ? "ရာသီပေါ်ဟင်းလျာများ ရှာဖွေမည်" : "Discover Seasonal Recipes"}
          </Link>
        </div>
      </section>
    </div>
  );
}
