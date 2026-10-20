export interface ThemePalette {
  primary: string;
  primaryForeground: string;
  accent: string;
  background: string;
  surface: string;
  text: string;
  muted: string;
  border: string;
  contrastWithBg?: number;
  wcagCompliant?: boolean;
}

export interface SeasonalTheme {
  id: string;
  myanmarMonth: number; // 1 = Tagu, 2 = Kason, ..., 12 = Tabaung, 0 = default/intercalary
  burmeseMonthName: string;
  englishMonthName: string;
  festivalId?: string | null;
  isFestival: boolean;
  festivalNameMm?: string;
  festivalNameEn?: string;
  greetingMm: string;
  greetingEn: string;
  descriptionMm: string;
  descriptionEn: string;
  artworkUrl: string;
  artworkAltMm: string;
  artworkAltEn: string;
  sourceAttribution: string;
  license: string;
  fallbackPalette: ThemePalette;
  extractedPalette: ThemePalette;
  priority: number; // monthly = 1, festival = 10, default = 0
  seasonalFoodTags: string[];
  culturalTraditionsMm: string[];
  culturalTraditionsEn: string[];
  effectiveDateRule?: string;
}

export interface MyanmarCalendarInfo {
  myanmarYear: number;
  sasanaYear: number;
  myanmarMonth: number; // 1-12, or 0 (First Waso), 13 (Late Tagu), 14 (Late Kason)
  normalizedMonth: number; // 1-12
  monthDay: number; // 1-30
  fortnightDay: number; // 1-15
  moonPhase: "Waxing" | "Full Moon" | "Waning" | "New Moon";
  moonPhaseMm: "လဆန်း" | "လပြည့်" | "လဆုတ်" | "လကွယ်";
  monthNameEn: string;
  monthNameMm: string;
  yearType: "common" | "little_watat" | "big_watat";
  isWatatYear: boolean;
  isSabbathDay: boolean;
  isSabbathEve: boolean;
  holidays: string[];
  activeFestival: {
    id: string;
    nameMm: string;
    nameEn: string;
    descriptionMm: string;
    descriptionEn: string;
  } | null;
  gregorianDateStr: string;
  formattedMm: string;
  formattedEn: string;
}
