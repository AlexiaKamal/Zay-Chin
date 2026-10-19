"use client";

import React, { createContext, useContext, useState, useEffect } from "react";
import { Language } from "@/types";
import { translations } from "@/lib/i18n";

interface AppContextType {
  language: Language;
  setLanguage: (lang: Language) => void;
  city: "Yangon" | "Mandalay";
  setCity: (city: "Yangon" | "Mandalay") => void;
  t: typeof translations.en;
}

const AppContext = createContext<AppContextType | undefined>(undefined);

export function AppProvider({ children }: { children: React.ReactNode }) {
  const [language, setLanguageState] = useState<Language>("mm");
  const [city, setCityState] = useState<"Yangon" | "Mandalay">("Yangon");
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

  const currentTranslations = translations[language] || translations.en;

  return (
    <AppContext.Provider
      value={{
        language,
        setLanguage,
        city,
        setCity,
        t: currentTranslations,
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
