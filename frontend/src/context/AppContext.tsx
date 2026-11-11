"use client";

import React, { createContext, useContext, useState, useEffect, useMemo } from "react";
import { Language } from "@/types";
import { translations } from "@/lib/i18n";

export interface UserProfile {
  name: string;
  email: string;
  age: number;
  height_cm: number;
  weight_kg: number;
  preference_meal: string;
  isLoggedIn: boolean;
}

export const DEFAULT_USER_PROFILE: UserProfile = {
  name: "မြမြ",
  email: "mya.mya@zaychin.mm",
  age: 28,
  height_cm: 162,
  weight_kg: 56,
  preference_meal: "ကြက်သားနှင့် ရိုးရာဟင်းရည်များ",
  isLoggedIn: true,
};

interface AppContextType {
  language: Language;
  setLanguage: (lang: Language) => void;
  city: "Yangon" | "Mandalay";
  setCity: (city: "Yangon" | "Mandalay") => void;
  t: typeof translations.en;
  userProfile: UserProfile;
  updateUserProfile: (profile: Partial<UserProfile>) => void;
  login: (email: string, name?: string) => void;
  logout: () => void;
  bmi: number;
  bmiCategory: {
    category: "underweight" | "normal" | "overweight" | "obese";
    label_en: string;
    label_mm: string;
    recommendation_en: string;
    recommendation_mm: string;
    color: string;
  };
}

const AppContext = createContext<AppContextType | undefined>(undefined);

export function AppProvider({ children }: { children: React.ReactNode }) {
  const [language, setLanguageState] = useState<Language>("mm");
  const [city, setCityState] = useState<"Yangon" | "Mandalay">("Yangon");
  const [userProfile, setUserProfileState] = useState<UserProfile>(DEFAULT_USER_PROFILE);
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    const savedLang = localStorage.getItem("zaychin_language") as Language;
    if (savedLang === "en" || savedLang === "mm") {
      setLanguageState(savedLang);
    }
    const savedCity = localStorage.getItem("zaychin_city") as "Yangon" | "Mandalay";
    if (savedCity === "Yangon" || savedCity === "Mandalay") {
      setCityState(savedCity);
    }
    const savedProfile = localStorage.getItem("zaychin_user_profile");
    if (savedProfile) {
      try {
        setUserProfileState(JSON.parse(savedProfile));
      } catch (e) {}
    }
    setMounted(true);
  }, []);

  const setLanguage = (lang: Language) => {
    setLanguageState(lang);
    localStorage.setItem("zaychin_language", lang);
  };

  const setCity = (c: "Yangon" | "Mandalay") => {
    setCityState(c);
    localStorage.setItem("zaychin_city", c);
  };

  const updateUserProfile = (partial: Partial<UserProfile>) => {
    setUserProfileState((prev) => {
      const next = { ...prev, ...partial };
      localStorage.setItem("zaychin_user_profile", JSON.stringify(next));
      return next;
    });
  };

  const login = (email: string, name?: string) => {
    updateUserProfile({
      email,
      name: name || email.split("@")[0],
      isLoggedIn: true,
    });
  };

  const logout = () => {
    updateUserProfile({ isLoggedIn: false });
  };

  // BMI calculations
  const heightM = (userProfile.height_cm || 165) / 100;
  const weightKg = userProfile.weight_kg || 60;
  const bmi = Math.round((weightKg / (heightM * heightM)) * 10) / 10;

  const bmiCategory = useMemo(() => {
    if (bmi < 18.5) {
      return {
        category: "underweight" as const,
        label_en: "Underweight (BMI < 18.5)",
        label_mm: "ပေါင်ချိန် လျော့နည်း (BMI < ၁၈.၅)",
        recommendation_en: "Calorie-dense, high-protein traditional curries with healthy fats (Butter rice, Danbauk, braised chicken).",
        recommendation_mm: "အာဟာရပြည့်ဝပြီး ကယ်လိုရီနှင့် ပရိုတင်းကြွယ်ဝသော မြန်မာ့ရိုးရာ ဟင်းလျာများ (ထောပတ်ထမင်း၊ ဒံပေါက်၊ အသားဆီပြန်ဟင်းများ)။",
        color: "text-amber-700 bg-amber-50 border-amber-200",
      };
    } else if (bmi <= 24.9) {
      return {
        category: "normal" as const,
        label_en: "Normal / Healthy Weight (BMI 18.5 - 24.9)",
        label_mm: "ပုံမှန်နှင့် ကျန်းမာသော ကိုယ်အလေးချိန် (BMI ၁၈.၅ - ၂၄.၉)",
        recommendation_en: "Balanced traditional diets: steamed rice, light fish or poultry curries, fresh vegetable salads, and clear soups.",
        recommendation_mm: "မျှတသော မြန်မာ့ရိုးရာ အစားအစာများ- ထမင်း၊ အသား/ငါး ဟင်းလျာ၊ လတ်ဆတ်သော အသုပ်နှင့် ဟင်းခါးများ။",
        color: "text-emerald-800 bg-emerald-50 border-emerald-200",
      };
    } else if (bmi <= 29.9) {
      return {
        category: "overweight" as const,
        label_en: "Overweight (BMI 25 - 29.9)",
        label_mm: "ကိုယ်အလေးချိန် အနည်းငယ်ပိုမို (BMI ၂၅ - ၂၉.၉)",
        recommendation_en: "Low-oil, fiber-rich Myanmar dishes: Roselle leaf soup (Chinbaung), bottle gourd clear soup, fresh Burmese salads, and steamed fish.",
        recommendation_mm: "ဆီလျှော့၊ အမျှင်ဓာတ်များသော ဟင်းလျာများ- ချဉ်ပေါင်ဟင်း၊ ဘူးသီးဟင်းခါး၊ ရိုးရာဟင်းသီးဟင်းရွက် အသုပ်များနှင့် ငါးပေါင်းဟင်းများ။",
        color: "text-orange-800 bg-orange-50 border-orange-200",
      };
    } else {
      return {
        category: "obese" as const,
        label_en: "Obese (BMI ≥ 30)",
        label_mm: "ကိုယ်အလေးချိန် သိသာစွာများပြား (BMI ≥ ၃၀)",
        recommendation_en: "Low-calorie, low-sodium traditional soups, boiled vegetable dips (To-sa-byit with Ngapi-ye), and lean white meats.",
        recommendation_mm: "ဆားနှင့်ဆီ လျှော့ချထားသော အရည်သောက်ဟင်းများ၊ တို့စရာနှင့် ငါးပိရည်၊ အဆီမပါသော အသားဟင်းများ။",
        color: "text-red-800 bg-red-50 border-red-200",
      };
    }
  }, [bmi]);

  const currentTranslations = translations[language] || translations.en;

  return (
    <AppContext.Provider
      value={{
        language,
        setLanguage,
        city,
        setCity,
        t: currentTranslations,
        userProfile,
        updateUserProfile,
        login,
        logout,
        bmi,
        bmiCategory,
      }}
    >
      {children}
    </AppContext.Provider>
  );
}

export function useApp() {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error("useApp must be used within an AppProvider");
  }
  return context;
}
