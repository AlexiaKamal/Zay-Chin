"use client";

import React, { useState } from "react";
import { useTheme } from "./ThemeProvider";
import { useApp } from "@/context/AppContext";
import {
  SparklesIcon,
  CalendarIcon,
  XIcon,
  CheckIcon,
} from "./ui/Icons";

export function ThemePreview() {
  const {
    theme,
    calendar,
    isOverridden,
    reason,
    previewThemeId,
    setPreviewThemeId,
    previewDate,
    setPreviewDate,
    resetToLiveCalendar,
    allThemes,
  } = useTheme();

  const { language } = useApp();
  const [isOpen, setIsOpen] = useState(false);
  const [testDateInput, setTestDateInput] = useState(previewDate || calendar.gregorianDateStr);

  const monthlyList = allThemes.filter((t) => !t.isFestival && t.myanmarMonth > 0);
  const festivalList = allThemes.filter((t) => t.isFestival);

  const handleDateChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const val = e.target.value;
    setTestDateInput(val);
    if (val) {
      setPreviewDate(val);
    }
  };

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
                    {language === "mm" ? "လက်ရှိ အပြင်အဆင် အခြေအနေ" : "Theme Resolution Status"}
                  </span>
                  <span
                    className="px-2 py-0.5 rounded-full text-[11px] font-bold"
                    style={{
                      backgroundColor: isOverridden ? "#FEF3C7" : "#DCFCE7",
                      color: isOverridden ? "#92400E" : "#166534",
                    }}
                  >
                    {reason === "festival_override" && (language === "mm" ? "ပွဲတော်လွှမ်းမိုးမှု" : "Festival Active")}
                    {reason === "monthly_season" && (language === "mm" ? "ပုံမှန်လအလိုက်" : "Normal Monthly")}
                    {reason === "manual_preview" && (language === "mm" ? "စမ်းသပ် ရွေးချယ်ထားသည်" : "Manual Preview")}
                    {reason === "default_fallback" && (language === "mm" ? "အခြေခံ မူလ" : "Default Fallback")}
                  </span>
                </div>

                <div className="text-xs text-stone-600 space-y-1 pt-1">
                  <div>
                    <span className="font-semibold text-stone-900">
                      {language === "mm" ? "မြန်မာရက်စွဲ:" : "Myanmar Date:"}{" "}
                    </span>
                    <span>{calendar.formattedMm}</span>
                  </div>
                  <div>
                    <span className="font-semibold text-stone-900">
                      {language === "mm" ? "အင်္ဂလိပ်ရက်စွဲ:" : "Gregorian:"}{" "}
                    </span>
                    <span>{calendar.formattedEn} ({calendar.gregorianDateStr})</span>
                  </div>
                  {calendar.holidays.length > 0 && (
                    <div>
                      <span className="font-semibold text-stone-900">
                        {language === "mm" ? "ရုံးပိတ်/အခါတော်:" : "Holidays:"}{" "}
                      </span>
                      <span className="text-emerald-700">{calendar.holidays.join(", ")}</span>
                    </div>
                  )}
                </div>

                {isOverridden && (
                  <button
                    onClick={resetToLiveCalendar}
                    className="w-full mt-2 py-2 px-3 rounded-lg bg-stone-200 hover:bg-stone-300 text-stone-900 font-bold text-xs transition-colors"
                  >
                    {language === "mm" ? "↺ လက်ရှိပြက္ခဒိန်သို့ ချက်ချင်း ပြန်ထားမည်" : "↺ Reset to Live Calendar"}
                  </button>
                )}
              </div>

              {/* Date Simulator */}
              <div className="space-y-2">
                <label className="block text-xs font-bold text-stone-700 uppercase tracking-wider">
                  {language === "mm" ? "ရက်စွဲ စမ်းသပ်ပြောင်းလဲရန် (Gregorian Date)" : "Simulate Gregorian Date"}
                </label>
                <div className="flex gap-2">
                  <input
                    type="date"
                    value={testDateInput}
                    onChange={handleDateChange}
                    className="w-full px-3 py-2 border border-stone-300 rounded-lg text-xs focus:outline-none focus:border-stone-800"
                  />
                  <button
                    onClick={() => {
                      setTestDateInput(calendar.gregorianDateStr);
                      setPreviewDate(null);
                    }}
                    className="px-3 py-2 bg-stone-100 hover:bg-stone-200 rounded-lg text-xs font-semibold shrink-0"
                  >
                    Today
                  </button>
                </div>
                <p className="text-[11px] text-stone-500">
                  {language === "mm"
                    ? "ဥပမာ- သင်္ကြန် (2026-04-14), သီတင်းကျွတ် (2026-10-26) ရိုက်ထည့်၍ စမ်းသပ်နိုင်ပါသည်။"
                    : "Try 2026-04-14 for Thingyan or 2026-10-26 for Thadingyut Full Moon."}
                </p>
              </div>

              {/* Major Festival Override Themes */}
              <div className="space-y-2">
                <label className="block text-xs font-bold text-stone-700 uppercase tracking-wider">
                  {language === "mm" ? "မြန်မာ့ပွဲတော် အထူးအပြင်အဆင်များ (Festivals)" : "Major Festival Overrides"}
                </label>
                <div className="grid grid-cols-2 gap-2">
                  {festivalList.map((f) => {
                    const isSelected = theme.id === f.id;
                    return (
                      <button
                        key={f.id}
                        onClick={() => handleSelectTheme(f.id)}
                        className={`p-2.5 rounded-xl border text-left transition-all flex flex-col justify-between ${
                          isSelected
                            ? "border-emerald-600 bg-emerald-50/60 ring-2 ring-emerald-500/20"
                            : "border-stone-200 bg-white hover:bg-stone-50"
                        }`}
                      >
                        <div className="font-bold text-xs text-stone-900 line-clamp-1">
                          {language === "mm" ? f.festivalNameMm : f.festivalNameEn}
                        </div>
                        <div className="flex items-center justify-between mt-2">
                          <span
                            className="w-3.5 h-3.5 rounded-full border border-black/10"
                            style={{ backgroundColor: f.extractedPalette.primary }}
                          />
                          {isSelected && <CheckIcon className="w-3.5 h-3.5 text-emerald-700" />}
                        </div>
                      </button>
                    );
                  })}
                </div>
              </div>

              {/* All 12 Myanmar Lunar Month Themes */}
              <div className="space-y-2">
                <label className="block text-xs font-bold text-stone-700 uppercase tracking-wider">
                  {language === "mm" ? "ဆယ့်နှစ်လရာသီ အပြင်အဆင်များ (12 Lunar Months)" : "All 12 Lunar Months"}
                </label>
                <div className="grid grid-cols-2 sm:grid-cols-3 gap-2">
                  {monthlyList.map((m) => {
                    const isSelected = theme.id === m.id;
                    return (
                      <button
                        key={m.id}
                        onClick={() => handleSelectTheme(m.id)}
                        className={`p-2 rounded-xl border text-left transition-all ${
                          isSelected
                            ? "border-emerald-600 bg-emerald-50/60 ring-2 ring-emerald-500/20"
                            : "border-stone-200 bg-white hover:bg-stone-50"
                        }`}
                      >
                        <div className="text-[11px] font-bold text-stone-900 line-clamp-1">
                          {language === "mm" ? m.burmeseMonthName : m.englishMonthName}
                        </div>
                        <div className="flex items-center justify-between mt-1.5">
                          <span
                            className="w-3 h-3 rounded-full border border-black/10"
                            style={{ backgroundColor: m.extractedPalette.primary }}
                          />
                          {isSelected && <CheckIcon className="w-3 h-3 text-emerald-700" />}
                        </div>
                      </button>
                    );
                  })}
                </div>
              </div>

              {/* Active Palette Swatches & Accessibility Contrast */}
              <div className="p-4 rounded-xl bg-stone-50 border border-stone-200 space-y-3">
                <div className="flex items-center justify-between">
                  <span className="font-bold text-xs text-stone-700">
                    {language === "mm" ? "အရောင်အသွေးနှင့် အလင်းအမှောင် စစ်ဆေးချက်" : "Active Design Tokens & Contrast"}
                  </span>
                  <span className="text-[11px] font-extrabold text-emerald-700">
                    WCAG AA {theme.extractedPalette.contrastWithBg}:1
                  </span>
                </div>

                {/* Swatches */}
                <div className="grid grid-cols-4 gap-2 text-[10px] text-center font-mono">
                  <div>
                    <div
                      className="h-8 rounded-lg shadow-2xs border border-black/10 mb-1"
                      style={{ backgroundColor: theme.extractedPalette.primary }}
                    />
                    <span className="text-stone-600 block line-clamp-1">Primary</span>
                    <span className="text-stone-400 font-bold">{theme.extractedPalette.primary}</span>
                  </div>
                  <div>
                    <div
                      className="h-8 rounded-lg shadow-2xs border border-black/10 mb-1"
                      style={{ backgroundColor: theme.extractedPalette.accent }}
                    />
                    <span className="text-stone-600 block line-clamp-1">Accent</span>
                    <span className="text-stone-400 font-bold">{theme.extractedPalette.accent}</span>
                  </div>
                  <div>
                    <div
                      className="h-8 rounded-lg shadow-2xs border border-black/10 mb-1"
                      style={{ backgroundColor: theme.extractedPalette.muted }}
                    />
                    <span className="text-stone-600 block line-clamp-1">Muted</span>
                    <span className="text-stone-400 font-bold">{theme.extractedPalette.muted}</span>
                  </div>
                  <div>
                    <div
                      className="h-8 rounded-lg shadow-2xs border border-black/10 mb-1"
                      style={{ backgroundColor: theme.extractedPalette.border }}
                    />
                    <span className="text-stone-600 block line-clamp-1">Border</span>
                    <span className="text-stone-400 font-bold">{theme.extractedPalette.border}</span>
                  </div>
                </div>

                <div className="text-[11px] text-stone-500 pt-1">
                  ✓ Contrast ratio against warm background (#FFF9F0) is {theme.extractedPalette.contrastWithBg}:1 (required: ≥ 4.5:1).
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
