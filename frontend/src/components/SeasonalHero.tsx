"use client";

import React, { useState } from "react";
import Image from "next/image";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useTheme } from "./ThemeProvider";
import { useApp } from "@/context/AppContext";
import {
  CalendarIcon,
  CookingPotIcon,
  SearchIcon,
  SparklesIcon,
  ChevronRightIcon,
  CheckIcon,
} from "./ui/Icons";

export function SeasonalHero() {
  const { theme, calendar, isOverridden } = useTheme();
  const { language, t } = useApp();
  const router = useRouter();
  const [searchQuery, setSearchQuery] = useState("");
  const [imgError, setImgError] = useState(false);

  const handleHeroSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      router.push(`/recipes?search=${encodeURIComponent(searchQuery.trim())}`);
    } else {
      router.push("/recipes");
    }
  };

  const formattedDate = language === "mm" ? calendar.formattedMm : calendar.formattedEn;
  const monthName = language === "mm" ? theme.burmeseMonthName : theme.englishMonthName;
  const festivalName = language === "mm" ? theme.festivalNameMm : theme.festivalNameEn;
  const greeting = language === "mm" ? theme.greetingMm : theme.greetingEn;
  const description = language === "mm" ? theme.descriptionMm : theme.descriptionEn;
  const altText = language === "mm" ? theme.artworkAltMm : theme.artworkAltEn;
  const traditions = language === "mm" ? theme.culturalTraditionsMm : theme.culturalTraditionsEn;

  // Use fallback image if artwork fails
  const artworkSource = imgError ? "/assets/seasons/default-theme.jpg" : theme.artworkUrl;

  return (
    <section className="relative overflow-hidden bg-[var(--color-background)] pt-8 pb-16 sm:pt-12 sm:pb-20 border-b border-[var(--color-border)] transition-colors duration-500">
      {/* Subtle organic seasonal ambient glow */}
      <div
        className="pointer-events-none absolute -top-24 right-0 w-96 h-96 rounded-full opacity-20 blur-3xl"
        style={{ backgroundColor: "var(--color-accent)" }}
      />
      <div
        className="pointer-events-none absolute top-48 -left-20 w-80 h-80 rounded-full opacity-15 blur-3xl"
        style={{ backgroundColor: "var(--color-primary)" }}
      />

      <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center">
          {/* Left Column: Cultural Calendar context & Content */}
          <div className="lg:col-span-7 space-y-6 text-left">
            {/* Calendar & Moon Phase Header Tag */}
            <div className="flex flex-wrap items-center gap-2">
              <span
                className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold text-white shadow-xs"
                style={{ backgroundColor: "var(--color-primary)" }}
              >
                <CalendarIcon className="w-3.5 h-3.5" />
                <span>{formattedDate}</span>
              </span>

              {theme.isFestival && (
                <span
                  className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-[var(--color-muted)] text-[var(--color-primary)] border border-[var(--color-border)]"
                >
                  <SparklesIcon className="w-3.5 h-3.5 text-amber-500" />
                  <span>{festivalName}</span>
                </span>
              )}

              {calendar.isSabbathDay && (
                <span className="px-2.5 py-1 rounded-full text-xs font-bold bg-amber-100 text-amber-900 border border-amber-200">
                  {language === "mm" ? "သီတင်းသီလ ဥပုသ်နေ့" : "Sabbath Day"}
                </span>
              )}
            </div>

            {/* Cultural Greeting Headline */}
            <div className="space-y-2">
              <span className="text-xs sm:text-sm font-extrabold uppercase tracking-widest text-[var(--color-primary)]">
                {language === "mm"
                  ? `မြန်မာ့ဆယ့်နှစ်လ ရာသီစက်ဝန်း • ${monthName}`
                  : `Living Seasons of Myanmar • ${monthName}`}
              </span>
              <h1 className="text-2xl sm:text-4xl lg:text-5xl font-extrabold text-[var(--color-text)] tracking-tight leading-tight sm:leading-snug">
                {greeting}
              </h1>
            </div>

            {/* Cultural Description & Context */}
            <p className="text-sm sm:text-base text-stone-600 leading-relaxed max-w-2xl">
              {description}
            </p>

            {/* 3 Seasonal Food Customs / Traditions */}
            {traditions && traditions.length > 0 && (
              <div className="p-4 rounded-2xl bg-[var(--color-surface)] border border-[var(--color-border)] shadow-xs space-y-2.5">
                <div className="text-xs font-bold text-[var(--color-primary)] uppercase tracking-wider">
                  {language === "mm" ? "ဤရာသီ၏ အထူးရိုးရာဓလေ့နှင့် စားသောက်ဖွယ်ရာများ" : "Seasonal Traditions & Featured Dishes"}
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs text-stone-700">
                  {traditions.map((item, idx) => (
                    <div key={idx} className="flex items-start gap-1.5">
                      <CheckIcon className="w-4 h-4 text-[var(--color-primary)] shrink-0 mt-0.5" />
                      <span className="leading-tight">{item}</span>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Quick Recipe Search Bar */}
            <div className="pt-1">
              <form
                onSubmit={handleHeroSearch}
                className="flex items-center bg-[var(--color-surface)] rounded-2xl shadow-sm p-1.5 border border-[var(--color-border)] focus-within:border-[var(--color-primary)] transition-colors"
              >
                <div className="pl-3 pr-2 text-stone-400">
                  <SearchIcon className="w-5 h-5 text-[var(--color-primary)]" />
                </div>
                <input
                  type="text"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  placeholder={
                    language === "mm"
                      ? `${monthName} ရာသီစာ ဟင်းလျာများ၊ ပါဝင်ပစ္စည်း ရှာရန်...`
                      : `Search seasonal dishes, ingredients (e.g. ထောပတ်ထမင်း, Catfish)...`
                  }
                  className="w-full py-2.5 text-sm sm:text-base text-[var(--color-text)] placeholder-stone-400 bg-transparent focus:outline-none"
                />
                <button
                  type="submit"
                  className="px-5 py-2.5 text-white text-sm font-bold rounded-xl transition-all shadow-xs shrink-0 flex items-center gap-1.5 hover:opacity-95"
                  style={{ backgroundColor: "var(--color-primary)" }}
                >
                  <span>{language === "mm" ? "ရှာဖွေမည်" : "Search"}</span>
                </button>
              </form>
            </div>

            {/* CTAs */}
            <div className="flex flex-wrap items-center gap-4 pt-1">
              <Link
                href="/planner"
                className="px-6 py-3.5 rounded-xl font-extrabold text-sm shadow-md transition-transform active:scale-95 flex items-center gap-2 hover:opacity-95"
                style={{
                  backgroundColor: "var(--color-primary)",
                  color: "var(--color-primary-foreground)",
                }}
              >
                <CalendarIcon className="w-4 h-4" />
                <span>{t.btn_start_planning}</span>
              </Link>
              <Link
                href="/recipes"
                className="px-6 py-3.5 rounded-xl font-semibold text-sm border border-[var(--color-border)] bg-[var(--color-surface)] text-[var(--color-text)] hover:bg-[var(--color-muted)] transition-colors flex items-center gap-2"
              >
                <CookingPotIcon className="w-4 h-4 text-[var(--color-primary)]" />
                <span>{t.btn_explore_recipes}</span>
              </Link>
            </div>
          </div>

          {/* Right Column: Prominent Authentic Seasonal Artwork */}
          <div className="lg:col-span-5">
            <div className="relative group rounded-3xl overflow-hidden border border-[var(--color-border)] bg-[var(--color-surface)] shadow-md transition-all duration-300 hover:shadow-lg">
              <div className="relative aspect-[4/3] w-full overflow-hidden bg-stone-100">
                <img
                  src={artworkSource}
                  alt={altText}
                  onError={() => setImgError(true)}
                  className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
                  loading="eager"
                />
                {/* Subtle gradient at bottom for badge contrast */}
                <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent pointer-events-none" />

                {/* Cultural Artwork Caption Overlay */}
                <div className="absolute bottom-3 left-3 right-3 text-white pointer-events-none">
                  <div className="text-xs font-bold leading-snug drop-shadow-md line-clamp-1">
                    {altText}
                  </div>
                  <div className="text-[10px] text-white/80 drop-shadow-xs line-clamp-1 mt-0.5">
                    {language === "mm" ? "စစ်မှန်သော ရိုးရာဓာတ်ပုံ" : "Authentic Photography"} • {theme.sourceAttribution} ({theme.license})
                  </div>
                </div>
              </div>

              {/* Bottom palette indicator bar */}
              <div className="p-3 bg-[var(--color-surface)] flex items-center justify-between text-xs text-stone-500 border-t border-[var(--color-border)]">
                <div className="flex items-center gap-2">
                  <span className="text-[11px] font-semibold">
                    {language === "mm" ? "ရာသီအလိုက် အရောင်အသွေး" : "Extracted Palette"}:
                  </span>
                  <div className="flex items-center gap-1">
                    <span
                      className="w-3.5 h-3.5 rounded-full border border-black/10 shadow-2xs"
                      style={{ backgroundColor: theme.extractedPalette.primary }}
                      title={`Primary: ${theme.extractedPalette.primary}`}
                    />
                    <span
                      className="w-3.5 h-3.5 rounded-full border border-black/10 shadow-2xs"
                      style={{ backgroundColor: theme.extractedPalette.accent }}
                      title={`Accent: ${theme.extractedPalette.accent}`}
                    />
                    <span
                      className="w-3.5 h-3.5 rounded-full border border-black/10 shadow-2xs"
                      style={{ backgroundColor: theme.extractedPalette.muted }}
                      title={`Muted: ${theme.extractedPalette.muted}`}
                    />
                  </div>
                </div>

                <span className="text-[11px] font-medium text-emerald-700">
                  {theme.extractedPalette.contrastWithBg}:1 WCAG AA
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
