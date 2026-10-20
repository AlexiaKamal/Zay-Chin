import { SeasonalTheme, ThemePalette } from "@/types/theme";

export const defaultPalette: ThemePalette = {
  primary: "#526C4E", // Warm Myanmar botanical olive green
  primaryForeground: "#FFFFFF",
  accent: "#D7A15A", // Warm amber gold
  background: "#FFF9F0", // Permanent cream foundation
  surface: "#FFFFFF",
  text: "#302C28", // Deep warm charcoal
  muted: "#F3ECE1",
  border: "#E8DED0",
  contrastWithBg: 6.82,
  wcagCompliant: true,
};

export const defaultTheme: SeasonalTheme = {
  id: "default-theme",
  myanmarMonth: 0,
  burmeseMonthName: "ရိုးရာအခြေခံ",
  englishMonthName: "Golden Heritage",
  festivalId: null,
  isFestival: false,
  greetingMm: "မင်္ဂလာပါ — မြန်မာ့ရိုးရာ အစားအစာနှင့် ရာသီအလိုက် ဈေးဝယ်စရိတ် တွက်ချက်ခြင်းမှ ကြိုဆိုပါသည်။",
  greetingEn: "Welcome to Zay Chin — Mindful Myanmar meal planning connected to traditional seasonal rhythms.",
  descriptionMm: "ဒေါ်စန်းလေး၏ နာမည်ကျော် 'ချက်ပြုတ်အတတ်ပညာ' စာအုပ်မှ ဟင်းချက်နည်းများကို ရန်ကုန်/မန္တလေး ၂၀၂၆ ကာလပေါက်ဈေးဖြင့် စနစ်တကျ စီစဉ်နိုင်ပါသည်။",
  descriptionEn: "Authentic Myanmar culinary recipes from Daw San Lay's classic cookbook, calculated with verified 2026 market pricing and laboratory nutrition.",
  artworkUrl: "/assets/seasons/default-theme.jpg",
  artworkAltMm: "ရွှေတိဂုံစေတီတော်မြတ်ကြီး — မြန်မာ့ယဉ်ကျေးမှု၏ အထွတ်အမြတ် သုခရိပ်မြုံ",
  artworkAltEn: "The sacred Shwedagon Pagoda — Timeless cultural sanctuary of Myanmar",
  sourceAttribution: "Wikimedia Commons / Creative Commons",
  license: "CC BY-SA 4.0",
  fallbackPalette: defaultPalette,
  extractedPalette: defaultPalette,
  priority: 0,
  seasonalFoodTags: ["all-year", "all-season", "ceremonial"],
  culturalTraditionsMm: [
    "အာဟာရပြည့်ဝသော ရိုးရာ ဟင်းချက်နည်း ၁၇၁ မျိုး",
    "၂၀၂၆ ခုနှစ် လက်ရှိ ကာလပေါက်ဈေးဖြင့် ဘတ်ဂျက်တွက်ချက်မှု",
    "မိသားစုအလိုက် အလေအလွင့်မရှိစေမည့် အစားအစာ စီစဉ်ရေး",
  ],
  culturalTraditionsEn: [
    "171 Verified authentic Myanmar family recipes",
    "Real-time 2026 market observation pricing in MMK",
    "Nutritional balance and food waste prevention",
  ],
  effectiveDateRule: "Fallback when specific seasonal or lunar calendar info is unavailable",
};
