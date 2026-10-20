import { SeasonalTheme, MyanmarCalendarInfo } from "@/types/theme";
import { defaultTheme } from "./default";
import { monthlyThemes } from "./monthly-themes";
import { festivalThemes } from "./festival-themes";
import { getMyanmarCalendarInfo } from "@/lib/myanmar-calendar";

export interface ResolvedThemeResult {
  theme: SeasonalTheme;
  calendar: MyanmarCalendarInfo;
  isOverridden: boolean;
  reason: "festival_override" | "monthly_season" | "manual_preview" | "default_fallback";
}

/**
 * Returns all available seasonal and festival themes for manual preview or selection.
 */
export function getAllThemes(): SeasonalTheme[] {
  const list: SeasonalTheme[] = [
    defaultTheme,
    ...Object.values(monthlyThemes),
    ...Object.values(festivalThemes),
  ];
  return list;
}

/**
 * Finds a theme by its unique string ID.
 */
export function getThemeById(id: string): SeasonalTheme | undefined {
  if (id === defaultTheme.id) return defaultTheme;
  if (festivalThemes[id]) return festivalThemes[id];
  return Object.values(monthlyThemes).find((t) => t.id === id);
}

/**
 * Resolves the active theme based on current Myanmar lunar calendar,
 * active festival periods, or manual preview overrides.
 */
export function resolveActiveTheme(options?: {
  date?: Date | string;
  overrideThemeId?: string | null;
}): ResolvedThemeResult {
  const calendar = getMyanmarCalendarInfo(options?.date);

  // 1. Manual Developer Preview Override
  if (options?.overrideThemeId) {
    const overridden = getThemeById(options.overrideThemeId);
    if (overridden) {
      return {
        theme: overridden,
        calendar,
        isOverridden: true,
        reason: "manual_preview",
      };
    }
  }

  // 2. Active Festival Override (Priority 10)
  if (calendar.activeFestival) {
    const festivalTheme = festivalThemes[calendar.activeFestival.id];
    if (festivalTheme) {
      return {
        theme: festivalTheme,
        calendar,
        isOverridden: true,
        reason: "festival_override",
      };
    }
  }

  // 3. Normal Monthly Lunar Theme (Priority 1)
  const monthTheme = monthlyThemes[calendar.normalizedMonth];
  if (monthTheme) {
    return {
      theme: monthTheme,
      calendar,
      isOverridden: false,
      reason: "monthly_season",
    };
  }

  // 4. Safe Default Fallback (Priority 0)
  return {
    theme: defaultTheme,
    calendar,
    isOverridden: false,
    reason: "default_fallback",
  };
}
