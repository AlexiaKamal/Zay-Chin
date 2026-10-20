"use client";

import React, { useEffect, useState } from "react";
import Link from "next/link";
import { useApp } from "@/context/AppContext";
import { useTheme } from "@/components/ThemeProvider";
import { getRecipes } from "@/lib/api";
import { RecipeSummary } from "@/types";
import { RecipeCard } from "@/components/recipes/RecipeCard";
import { SeasonalHero } from "@/components/SeasonalHero";
import {
  SparklesIcon,
  ChevronRightIcon,
  CoinsIcon,
  CookingPotIcon,
  CalendarIcon,
  ShoppingBagIcon,
  MapPinIcon,
  CheckIcon,
} from "@/components/ui/Icons";

export default function HomePage() {
  const { language, city, t } = useApp();
  const { theme, calendar } = useTheme();

  const [seasonalRecipes, setSeasonalRecipes] = useState<RecipeSummary[]>([]);
  const [featuredRecipes, setFeaturedRecipes] = useState<RecipeSummary[]>([]);
  const [loadingSeasonal, setLoadingSeasonal] = useState(true);
  const [loadingFeatured, setLoadingFeatured] = useState(true);

  // Load Seasonal Recommendations based on active theme tags
  useEffect(() => {
    async function loadSeasonal() {
      try {
        setLoadingSeasonal(true);
        // Find recipes tagged with active seasonal or festival tags
        const primaryTag = theme.seasonalFoodTags[0] || "all-season";
        const isFestivalTag = theme.isFestival;

        const data = await getRecipes({
          page: 1,
          pageSize: 4,
          seasonal: !isFestivalTag ? primaryTag : undefined,
          festival: isFestivalTag ? primaryTag : undefined,
          city,
        });

        if (data.recipes.length > 0) {
          setSeasonalRecipes(data.recipes);
        } else {
          // Fallback to top curated recipes
          const fallbackData = await getRecipes({ page: 1, pageSize: 4, city });
          setSeasonalRecipes(fallbackData.recipes);
        }
      } catch (err) {
        console.error("Error loading seasonal recipes:", err);
      } finally {
        setLoadingSeasonal(false);
      }
    }

    loadSeasonal();
  }, [theme.id, city]);

  // Load General Featured Recipes
  useEffect(() => {
    async function loadFeatured() {
      try {
        setLoadingFeatured(true);
        const data = await getRecipes({ page: 1, pageSize: 6, city });
        setFeaturedRecipes(data.recipes);
      } catch (err) {
        console.error("Error loading featured recipes:", err);
      } finally {
        setLoadingFeatured(false);
      }
    }
    loadFeatured();
  }, [city]);

  const monthName = language === "mm" ? theme.burmeseMonthName : theme.englishMonthName;
  const festivalOrMonthTitle = theme.isFestival
    ? (language === "mm" ? theme.festivalNameMm : theme.festivalNameEn)
    : (language === "mm" ? `${theme.burmeseMonthName} ရာသီခါ` : `${theme.englishMonthName} Season`);

  return (
    <div className="space-y-16 sm:space-y-24 pb-20">
      {/* 1. Dynamic Seasonal Hero */}
      <SeasonalHero />

      {/* 2. Seasonal Food Recommendations (Active Lunar Month / Festival) */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
        <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4 border-b border-[var(--color-border)] pb-4">
          <div>
            <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-extrabold bg-[var(--color-muted)] text-[var(--color-primary)] border border-[var(--color-border)] mb-1.5">
              <SparklesIcon className="w-3.5 h-3.5" />
              <span>
                {language === "mm" ? "ရာသီပေါ်နှင့် ပွဲတော်အလိုက် အထူးအကြံပြုချက်" : "Living Season Recommendations"}
              </span>
            </div>
            <h2 className="text-2xl sm:text-3xl font-extrabold text-[var(--color-text)]">
              {language === "mm"
                ? `${festivalOrMonthTitle} အတွက် အသင့်တော်ဆုံး ဟင်းလျာများ`
                : `Curated Dishes for ${festivalOrMonthTitle}`}
            </h2>
            <p className="text-xs sm:text-sm text-stone-500 mt-1">
              {language === "mm"
                ? "စစ်မှန်သော ဒေါ်စန်းလေး ဟင်းချက်နည်းများမှ ဤရာသီဥတုနှင့် အကိုက်ညီဆုံး ဟင်းလျာများ"
                : "Authentic Myanmar dishes paired with seasonal weather and cultural feasts"}
            </p>
          </div>

          <Link
            href="/recipes"
            className="inline-flex items-center gap-1 text-xs sm:text-sm font-bold text-[var(--color-primary)] hover:underline shrink-0"
          >
            <span>{language === "mm" ? "ရာသီစာများ အားလုံးရှာမည်" : "Browse All Seasonal Dishes"}</span>
            <ChevronRightIcon className="w-4 h-4" />
          </Link>
        </div>

        {loadingSeasonal ? (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {[1, 2, 3, 4].map((i) => (
              <div key={i} className="h-64 bg-stone-100 rounded-2xl animate-pulse border border-stone-200" />
            ))}
          </div>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {seasonalRecipes.map((r) => (
              <RecipeCard key={r.id} recipe={r} />
            ))}
          </div>
        )}
      </section>

      {/* 3. Verified Pricing & Nutrition Metrics Banner */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 p-6 sm:p-8 bg-white rounded-3xl border border-[var(--color-border)] shadow-xs">
          <div className="text-center p-3">
            <div className="text-2xl sm:text-4xl font-extrabold text-[var(--color-primary)]">171</div>
            <div className="text-xs sm:text-sm text-stone-600 font-medium mt-1">
              {language === "mm" ? "ဒေါ်စန်းလေး ဟင်းချက်နည်းများ" : "Authentic Myanmar Dishes"}
            </div>
            <div className="text-[11px] text-stone-400 mt-0.5">ချက်ပြုတ်အတတ်ပညာ မူရင်း</div>
          </div>
          <div className="text-center p-3 border-l border-stone-100">
            <div className="text-2xl sm:text-4xl font-extrabold text-[var(--color-primary)]">12</div>
            <div className="text-xs sm:text-sm text-stone-600 font-medium mt-1">
              {language === "mm" ? "ဆယ့်နှစ်လ ရာသီစက်ဝန်း" : "Myanmar Lunar Seasons"}
            </div>
            <div className="text-[11px] text-stone-400 mt-0.5">Living Seasons Architecture</div>
          </div>
          <div className="text-center p-3 border-l border-stone-100">
            <div className="text-2xl sm:text-4xl font-extrabold text-[var(--color-primary)]">134</div>
            <div className="text-xs sm:text-sm text-stone-600 font-medium mt-1">
              {language === "mm" ? "၂၀၂၆ ဈေးကွက် စစ်တမ်းမှတ်တမ်း" : "Verified 2026 Price Records"}
            </div>
            <div className="text-[11px] text-stone-400 mt-0.5">CSO & Bayintnaung</div>
          </div>
          <div className="text-center p-3 border-l border-stone-100">
            <div className="text-2xl sm:text-4xl font-extrabold text-[var(--color-primary)]">100%</div>
            <div className="text-xs sm:text-sm text-stone-600 font-medium mt-1">
              {language === "mm" ? "စစ်မှန်သော ဓာတ်ပုံနှင့် အရောင်များ" : "Legit Visuals & WCAG AA"}
            </div>
            <div className="text-[11px] text-stone-400 mt-0.5">Zero AI Hallucination</div>
          </div>
        </div>
      </section>

      {/* 4. How Zay Chin Works (5-Step User Journey per Requirement 9) */}
      <section className="bg-[var(--color-muted)] border-y border-[var(--color-border)] py-16 sm:py-20 transition-colors duration-500">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
          <div className="text-center max-w-2xl mx-auto space-y-3">
            <span className="text-xs font-bold text-[var(--color-primary)] tracking-wider uppercase">
              {language === "mm" ? "လွယ်ကူရိုးရှင်းသော အဆင့်များ" : "Seamless User Journey"}
            </span>
            <h2 className="text-2xl sm:text-3xl font-extrabold text-[var(--color-text)]">
              {language === "mm" ? "ဈေးခြင်း မည်သို့ အလုပ်လုပ်သနည်း" : "How Zay Chin Works"}
            </h2>
            <p className="text-stone-600 text-xs sm:text-sm leading-relaxed">
              {language === "mm"
                ? "ရိုးရာမြန်မာ့အရသာမှသည် အိမ်ထောင်ရှင်များ တွက်ခြေကိုက် ဈေးဝယ်နိုင်စေမည့် ၅ ဆင့် လမ်းညွှန်"
                : "From culinary heritage to modern grocery efficiency in five intuitive steps."}
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-5 gap-4 lg:gap-6">
            {/* Step 1 */}
            <div className="bg-white p-5 rounded-2xl border border-[var(--color-border)] shadow-xs flex flex-col justify-between space-y-3">
              <div className="w-10 h-10 rounded-xl bg-amber-100 text-amber-900 flex items-center justify-center font-extrabold text-base">
                1
              </div>
              <div>
                <h3 className="text-sm font-bold text-stone-900 mb-1">
                  {language === "mm" ? "၁။ ဘတ်ဂျက် သတ်မှတ်ပါ" : "1. Set Your Budget"}
                </h3>
                <p className="text-xs text-stone-600 leading-relaxed">
                  {language === "mm"
                    ? "မိသားစု လူဦးရေနှင့် တစ်ပတ်စာ သုံးစွဲလိုသော ကျပ်ငွေပမာဏကို သတ်မှတ်ပါ။"
                    : "Specify your weekly household grocery spending target in MMK."}
                </p>
              </div>
              <div className="pt-2 text-[11px] font-semibold text-amber-800 flex items-center gap-1">
                <CoinsIcon className="w-3.5 h-3.5" />
                <span>{city} Market Rates</span>
              </div>
            </div>

            {/* Step 2 */}
            <div className="bg-white p-5 rounded-2xl border border-[var(--color-border)] shadow-xs flex flex-col justify-between space-y-3">
              <div className="w-10 h-10 rounded-xl bg-emerald-100 text-emerald-900 flex items-center justify-center font-extrabold text-base">
                2
              </div>
              <div>
                <h3 className="text-sm font-bold text-stone-900 mb-1">
                  {language === "mm" ? "၂။ ဟင်းလျာများ ရွေးပါ" : "2. Discover Meals"}
                </h3>
                <p className="text-xs text-stone-600 leading-relaxed">
                  {language === "mm"
                    ? "ရာသီဥတုနှင့် လိုက်ဖက်သော မြန်မာ့ရိုးရာ ဟင်းချက်နည်းများကို လေ့လာရှာဖွေပါ။"
                    : "Explore seasonal Myanmar curries, comforting broths, and fresh salads."}
                </p>
              </div>
              <div className="pt-2 text-[11px] font-semibold text-emerald-800 flex items-center gap-1">
                <CookingPotIcon className="w-3.5 h-3.5" />
                <span>171 Recipes</span>
              </div>
            </div>

            {/* Step 3 */}
            <div className="bg-white p-5 rounded-2xl border border-[var(--color-border)] shadow-xs flex flex-col justify-between space-y-3">
              <div className="w-10 h-10 rounded-xl bg-teal-100 text-teal-900 flex items-center justify-center font-extrabold text-base">
                3
              </div>
              <div>
                <h3 className="text-sm font-bold text-stone-900 mb-1">
                  {language === "mm" ? "၃။ တစ်ပတ်စာ စီစဉ်ပါ" : "3. Plan Your Week"}
                </h3>
                <p className="text-xs text-stone-600 leading-relaxed">
                  {language === "mm"
                    ? "နေ့စဉ် မနက်စာ၊ နေ့လယ်စာနှင့် ညစာဇယားကို အာဟာရပြည့်ဝစွာ အလိုအလျောက် ရေးဆွဲပါ။"
                    : "Generate optimized weekly meal schedules tailored to your nutrition."}
                </p>
              </div>
              <div className="pt-2 text-[11px] font-semibold text-teal-800 flex items-center gap-1">
                <CalendarIcon className="w-3.5 h-3.5" />
                <span>Auto-balanced</span>
              </div>
            </div>

            {/* Step 4 */}
            <div className="bg-white p-5 rounded-2xl border border-[var(--color-border)] shadow-xs flex flex-col justify-between space-y-3">
              <div className="w-10 h-10 rounded-xl bg-blue-100 text-blue-900 flex items-center justify-center font-extrabold text-base">
                4
              </div>
              <div>
                <h3 className="text-sm font-bold text-stone-900 mb-1">
                  {language === "mm" ? "၄။ ဈေးဝယ်စာရင်း ထုတ်ပါ" : "4. Generate Grocery List"}
                </h3>
                <p className="text-xs text-stone-600 leading-relaxed">
                  {language === "mm"
                    ? "လိုအပ်သော ပါဝင်ပစ္စည်းများကို အလေးချိန်နှင့် ဗူးအရေအတွက်အလိုက် စုစည်းရယူပါ။"
                    : "Get an aggregated shopping checklist grouped by wet-market stalls."}
                </p>
              </div>
              <div className="pt-2 text-[11px] font-semibold text-blue-800 flex items-center gap-1">
                <ShoppingBagIcon className="w-3.5 h-3.5" />
                <span>Stall-grouped</span>
              </div>
            </div>

            {/* Step 5 */}
            <div className="bg-white p-5 rounded-2xl border border-[var(--color-border)] shadow-xs flex flex-col justify-between space-y-3">
              <div className="w-10 h-10 rounded-xl bg-purple-100 text-purple-900 flex items-center justify-center font-extrabold text-base">
                5
              </div>
              <div>
                <h3 className="text-sm font-bold text-stone-900 mb-1">
                  {language === "mm" ? "၅။ အနီးဆုံးဈေးများ ရှာပါ" : "5. Find Nearby Markets"}
                </h3>
                <p className="text-xs text-stone-600 leading-relaxed">
                  {language === "mm"
                    ? "ရန်ကုန်နှင့် မန္တလေးမြို့ရှိ အဓိက လက်လီလက်ကား ဈေးကြီးများကို လမ်းညွှန်ရှာဖွေပါ။"
                    : "Discover verified local wet markets and wholesale centers near you."}
                </p>
              </div>
              <div className="pt-2 text-[11px] font-semibold text-purple-800 flex items-center gap-1">
                <MapPinIcon className="w-3.5 h-3.5" />
                <span>Yangon & Mandalay</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* 5. Featured Authentic Recipes */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
        <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4 border-b border-[var(--color-border)] pb-4">
          <div>
            <span className="text-xs font-bold text-[var(--color-primary)] tracking-wider uppercase">
              {language === "mm" ? "အထူးရွေးချယ်ထားသော ဟင်းလျာများ" : "Curated Selections"}
            </span>
            <h2 className="text-2xl sm:text-3xl font-extrabold text-[var(--color-text)] mt-1">
              {language === "mm" ? "နာမည်ကျော် မြန်မာ့ရိုးရာ ဟင်းချက်နည်းများ" : "Featured Authentic Myanmar Recipes"}
            </h2>
            <p className="text-xs sm:text-sm text-stone-500 mt-1">
              {language === "mm"
                ? "ဒေါ်စန်းလေး၏ မူရင်းချက်ပြုတ်နည်းအတိုင်း တိုင်းတာချက်များ၊ အာဟာရနှင့် ၂၀၂၆ ပေါက်ဈေး"
                : "Standardized cookbook measures, estimated ingredient costs, and laboratory nutrition"}
            </p>
          </div>
          <Link
            href="/recipes"
            className="inline-flex items-center gap-1 text-xs sm:text-sm font-bold text-[var(--color-primary)] hover:underline shrink-0"
          >
            <span>{language === "mm" ? "ဟင်းချက်နည်း ၁၇၁ မျိုးစလုံး ကြည့်မည်" : "View All 171 Recipes"}</span>
            <ChevronRightIcon className="w-4 h-4" />
          </Link>
        </div>

        {loadingFeatured ? (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {[1, 2, 3, 4, 5, 6].map((i) => (
              <div key={i} className="h-64 bg-stone-100 rounded-2xl animate-pulse border border-stone-200" />
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

      {/* 6. Cultural Heritage Callout */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="bg-gradient-to-r from-[var(--color-muted)] via-white to-[var(--color-muted)] rounded-3xl p-8 sm:p-12 border border-[var(--color-border)] flex flex-col md:flex-row items-center justify-between gap-8 shadow-xs">
          <div className="space-y-3 max-w-xl">
            <span
              className="px-3 py-1 rounded-full text-xs font-extrabold text-white inline-block shadow-2xs"
              style={{ backgroundColor: "var(--color-primary)" }}
            >
              {language === "mm" ? "ရာသီစက်ဝန်းနှင့် ရိုးရာဓလေ့" : "Living Seasons Heritage"}
            </span>
            <h3 className="text-2xl sm:text-3xl font-extrabold text-[var(--color-text)]">
              {language === "mm"
                ? "မြန်မာ့ပြက္ခဒိန်နှင့် ဟင်းလျာများ၏ သဟဇာတဖြစ်မှု"
                : "Harmonizing Food with the Myanmar Lunar Calendar"}
            </h3>
            <p className="text-sm text-stone-600 leading-relaxed">
              {language === "mm"
                ? "မိုးတွင်းဟင်းရည်များ၊ နွေရာသီ မန်ကျည်းရွက်သုပ်၊ မုန့်လုံးရေပေါ် နှင့် အလှူမင်္ဂလာပွဲ ထောပတ်ထမင်း အပါအဝင် မြန်မာ့ဆယ့်နှစ်လရာသီ၏ အစားအသောက်ယဉ်ကျေးမှုကို ဈေးခြင်း တွင် အပြည့်အဝ ဖော်ပြပေးထားပါသည်။"
                : "Explore how each Myanmar lunar month brings unique seasonal ingredients—from monsoon soups and summer mango salads to Thingyan sweet dumplings and ceremonial feast curries."}
            </p>
          </div>
          <Link
            href="/planner"
            className="px-6 py-3.5 text-white font-bold text-sm rounded-xl shadow-md shrink-0 transition-transform active:scale-95 hover:opacity-95"
            style={{ backgroundColor: "var(--color-primary)" }}
          >
            {language === "mm" ? "ယခုပဲ စတင်စီစဉ်မည်" : "Start Meal Planning"}
          </Link>
        </div>
      </section>
    </div>
  );
}
