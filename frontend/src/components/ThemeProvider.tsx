"use client";

import React, { createContext, useContext, useState, useEffect, useMemo } from "react";
import { SeasonalTheme, MyanmarCalendarInfo } from "@/types/theme";
import { resolveActiveTheme, getAllThemes } from "@/themes/theme-resolver";
import { applyThemeVariables } from "@/lib/color-utils";

interface ThemeContextType {
  theme: SeasonalTheme;
  calendar: MyanmarCalendarInfo;
  isOverridden: boolean;
  reason: string;
  previewThemeId: string | null;
  setPreviewThemeId: (id: string | null) => void;
  previewDate: string | null;
  setPreviewDate: (date: string | null) => void;
  resetToLiveCalendar: () => void;
  allThemes: SeasonalTheme[];
}

const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [previewThemeId, setPreviewThemeIdState] = useState<string | null>(null);
  const [previewDate, setPreviewDateState] = useState<string | null>(null);
  const [mounted, setMounted] = useState(false);

  // Initialize from session storage if present (developer preview persistence)
  useEffect(() => {
    try {
      const savedTheme = sessionStorage.getItem("zaychin_preview_theme");
      const savedDate = sessionStorage.getItem("zaychin_preview_date");
      if (savedTheme) setPreviewThemeIdState(savedTheme);
      if (savedDate) setPreviewDateState(savedDate);
    } catch {
      // ignore in environments without sessionStorage
    }
    setMounted(true);
  }, []);

  const setPreviewThemeId = (id: string | null) => {
    setPreviewThemeIdState(id);
    try {
      if (id) sessionStorage.setItem("zaychin_preview_theme", id);
      else sessionStorage.removeItem("zaychin_preview_theme");
    } catch {}
  };

  const setPreviewDate = (date: string | null) => {
    setPreviewDateState(date);
    try {
      if (date) sessionStorage.setItem("zaychin_preview_date", date);
      else sessionStorage.removeItem("zaychin_preview_date");
    } catch {}
  };

  const resetToLiveCalendar = () => {
    setPreviewThemeId(null);
    setPreviewDate(null);
  };

  // Resolve active theme with memoization
  const resolved = useMemo(() => {
    return resolveActiveTheme({
      date: previewDate || undefined,
      overrideThemeId: previewThemeId,
    });
  }, [previewDate, previewThemeId]);

  // Apply CSS variables smoothly whenever resolved theme changes
  useEffect(() => {
    if (!mounted) return;
    applyThemeVariables(resolved.theme.extractedPalette);
  }, [resolved.theme, mounted]);

  const allThemes = useMemo(() => getAllThemes(), []);

  return (
    <ThemeContext.Provider
      value={{
        theme: resolved.theme,
        calendar: resolved.calendar,
        isOverridden: resolved.isOverridden,
        reason: resolved.reason,
        previewThemeId,
        setPreviewThemeId,
        previewDate,
        setPreviewDate,
        resetToLiveCalendar,
        allThemes,
      }}
    >
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error("useTheme must be used within a ThemeProvider");
  }
  return context;
}
