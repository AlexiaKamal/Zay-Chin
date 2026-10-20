"use client";

import React, { useState } from "react";
import Link from "next/link";
import { useTheme } from "./ThemeProvider";
import { useApp } from "@/context/AppContext";
import { SparklesIcon, CalendarIcon, ChevronRightIcon, XIcon } from "./ui/Icons";

export function FestivalBanner() {
  const { theme, calendar, isOverridden } = useTheme();
  const { language } = useApp();
  const [dismissed, setDismissed] = useState(false);

  // Only render if a festival theme is currently active
  if (!theme.isFestival || dismissed) {
    return null;
  }

  const festivalName = language === "mm" ? theme.festivalNameMm : theme.festivalNameEn;
  const greeting = language === "mm" ? theme.greetingMm : theme.greetingEn;

  return (
    <aside
      aria-label="Active Cultural Festival Banner"
      className="relative overflow-hidden border-b border-[var(--color-border)] bg-[var(--color-muted)] text-[var(--color-text)] transition-all duration-300"
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 sm:py-3.5">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs sm:text-sm">
          {/* Badge & Festival info */}
          <div className="flex items-start sm:items-center gap-2.5">
            <span
              className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-white font-bold text-[11px] shrink-0 shadow-xs"
              style={{ backgroundColor: "var(--color-primary)" }}
            >
              <SparklesIcon className="w-3.5 h-3.5 text-amber-300" />
              <span>
                {language === "mm" ? "ရာသီပွဲတော် အထူးအပြင်အဆင်" : "Active Festival Theme"}
              </span>
            </span>

            <div className="leading-snug">
              <span className="font-extrabold text-[var(--color-primary)] mr-2">
                {festivalName}:
              </span>
              <span className="text-stone-700 font-medium">{greeting}</span>
            </div>
          </div>

          {/* Quick CTA and Dismiss */}
          <div className="flex items-center gap-3 shrink-0 self-end sm:self-auto">
            <Link
              href="/recipes"
              className="inline-flex items-center gap-1 font-bold text-[var(--color-primary)] hover:underline text-xs"
            >
              <span>{language === "mm" ? "ပွဲတော်ဟင်းလျာများ ကြည့်မည်" : "Explore Festival Recipes"}</span>
              <ChevronRightIcon className="w-3.5 h-3.5" />
            </Link>

            <button
              onClick={() => setDismissed(true)}
              title={language === "mm" ? "ပိတ်မည်" : "Dismiss"}
              className="p-1 rounded-md text-stone-500 hover:text-stone-800 hover:bg-black/5 transition-colors"
            >
              <XIcon className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>
    </aside>
  );
}
