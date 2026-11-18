"use client";

import React, { useState } from "react";
import { useTheme } from "./ThemeProvider";
import { useApp } from "@/context/AppContext";
import {
  SparklesIcon,
  XIcon,
  CheckIcon,
} from "./ui/Icons";

export function ThemePreview() {
  const {
    theme,
    isOverridden,
    setPreviewThemeId,
    resetToLiveCalendar,
    allThemes,
  } = useTheme();

  const { language } = useApp();
  const [isOpen, setIsOpen] = useState(false);

  const monthlyList = allThemes.filter((t) => !t.isFestival && t.myanmarMonth > 0);

  const handleSelectTheme = (id: string) => {
    setPreviewThemeId(id);
  };

  return (
    <>
      {/* Floating Trigger Button */}
      <div className="fixed bottom-5 right-5 z-40">
        <button
          onClick={() => setIsOpen(!isOpen)}
          className="flex items-center gap-2 px-4 py-2.5 rounded-full shadow-lg text-xs font-bold text-white transition-all transform hover:scale-105 active:scale-95 border border-white/20"
          style={{ backgroundColor: "var(--color-primary)" }}
          aria-label="Open Living Seasons Theme Preview"
        >
          <SparklesIcon className="w-4 h-4 text-amber-300" />
          <span>
            {language === "mm" ? "ရာသီအပြင်အဆင် စမ်းသပ်ရန်" : "Theme Preview"}
          </span>
          {isOverridden && (
            <span className="w-2 h-2 rounded-full bg-amber-400 animate-ping" />
          )}
        </button>
      </div>

      {/* Slide-over Preview Drawer */}
      {isOpen && (
        <div className="fixed inset-0 z-50 overflow-hidden flex justify-end">
          {/* Backdrop */}
          <div
            className="fixed inset-0 bg-black/40 backdrop-blur-2xs transition-opacity"
            onClick={() => setIsOpen(false)}
          />

          {/* Drawer Content */}
          <div className="relative w-full max-w-md bg-white h-full shadow-2xl flex flex-col z-10 border-l border-stone-200 overflow-y-auto">
            {/* Header */}
            <div
              className="p-4 sm:p-5 text-white flex items-center justify-between border-b"
              style={{ backgroundColor: "var(--color-primary)" }}
            >
              <div>
                <div className="flex items-center gap-2">
                  <SparklesIcon className="w-4 h-4 text-amber-300" />
                  <h2 className="text-base font-extrabold">
                    {language === "mm" ? "ရာသီစက်ဝန်း အပြင်အဆင် စမ်းသပ်မှု" : "Living Seasons Theme Studio"}
                  </h2>
                </div>
                <p className="text-xs text-white/80 mt-0.5">
                  {language === "mm" ? "ဒေသတွင်း ပြက္ခဒိန်နှင့် ရာသီအလိုက် အပြင်အဆင်များ" : "Developer manual inspection & contrast check"}
                </p>
              </div>

              <button
                onClick={() => setIsOpen(false)}
                className="p-1 rounded-lg text-white/80 hover:text-white hover:bg-white/10"
              >
                <XIcon className="w-5 h-5" />
              </button>
            </div>

            <div className="p-4 sm:p-5 space-y-6 flex-grow text-xs sm:text-sm text-stone-800">
              {/* Status Indicator */}
              <div className="p-3.5 rounded-xl bg-stone-50 border border-stone-200 space-y-2">
                <div className="flex items-center justify-between">
                  <span className="font-bold text-stone-600">
                    {language === "mm" ? "လက်ရှိ အပြင်အဆင် အခြေအနေ" : "Current Seasonal Theme"}
                  </span>
                  <span
                    className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800"
                  >
                    {language === "mm" ? theme.burmeseMonthName : theme.englishMonthName}
                  </span>
                </div>

                {isOverridden && (
                  <button
                    onClick={resetToLiveCalendar}
                    className="w-full mt-2 py-2 px-3 rounded-lg bg-stone-200 hover:bg-stone-300 text-stone-900 font-bold text-xs transition-colors"
                  >
                    {language === "mm" ? "↺ လက်ရှိရာသီသို့ ချက်ချင်း ပြန်ထားမည်" : "↺ Reset to Current Season"}
                  </button>
                )}
              </div>

              {/* All 12 Myanmar Lunar Month Themes */}
              <div className="space-y-2">
                <label className="block text-xs font-bold text-stone-700 uppercase tracking-wider">
                  {language === "mm" ? "ဆယ့်နှစ်လရာသီ အပြင်အဆင်များ (12 Lunar Months)" : "Select Lunar Season (12 Months)"}
                </label>
                <div className="grid grid-cols-2 sm:grid-cols-3 gap-2">
                  {monthlyList.map((m) => {
                    const isSelected = theme.id === m.id;
                    return (
                      <button
                        key={m.id}
                        onClick={() => handleSelectTheme(m.id)}
                        className={`p-2.5 rounded-xl border text-left transition-all ${
                          isSelected
                            ? "border-[var(--color-primary)] bg-[var(--color-muted)]/40 ring-2 ring-[var(--color-primary)]/20 shadow-2xs font-extrabold"
                            : "border-stone-200 bg-white hover:bg-stone-50"
                        }`}
                      >
                        <div className="text-xs text-stone-900 line-clamp-1">
                          {language === "mm" ? m.burmeseMonthName : m.englishMonthName}
                        </div>
                        <div className="flex items-center justify-between mt-2">
                          <span
                            className="w-3.5 h-3.5 rounded-full border border-black/10"
                            style={{ backgroundColor: m.extractedPalette.primary }}
                          />
                          {isSelected && <CheckIcon className="w-3.5 h-3.5 text-[var(--color-primary)]" />}
                        </div>
                      </button>
                    );
                  })}
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
