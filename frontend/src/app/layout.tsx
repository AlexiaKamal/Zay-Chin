import React from "react";
import type { Metadata } from "next";
import "./globals.css";
import { AppProvider } from "@/context/AppContext";
import { ThemeProvider } from "@/components/ThemeProvider";
import { Navbar } from "@/components/layout/Navbar";
import { FestivalBanner } from "@/components/FestivalBanner";
import { ThemePreview } from "@/components/ThemePreview";
import { Footer } from "@/components/layout/Footer";

export const metadata: Metadata = {
  title: "Zay Chin (ဈေးခြင်း) — Living Seasons: Intelligent Myanmar Meal Planning & Seasonal Calendar",
  description: "Authentic Myanmar meal planning automatically adapted to Myanmar lunar calendar months, Thingyan, Thadingyut, and traditional seasonal festivals. Verified 2026 market prices and laboratory nutrition.",
  keywords: "Myanmar recipes, Burmese food, Myanmar lunar calendar, Living seasons, Thingyan, Thadingyut, Tazaungdaing, Waso, Daw San Lay, ချက်ပြုတ်နည်းများ, ဈေးခြင်း, မြန်မာ့ဆယ့်နှစ်လရာသီ",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="my">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Padauk:wght@400;700&display=swap"
          rel="stylesheet"
        />
      </head>
      <body className="min-h-screen bg-[var(--color-background)] text-[var(--color-text)] font-sans antialiased flex flex-col selection:bg-amber-100 selection:text-amber-900">
        <AppProvider>
          <ThemeProvider>
            <React.Suspense fallback={<div className="h-16 bg-white border-b border-stone-200" />}>
              <Navbar />
              <FestivalBanner />
            </React.Suspense>
            <main className="flex-grow">
              {children}
            </main>
            <Footer />
            <ThemePreview />
          </ThemeProvider>
        </AppProvider>
      </body>
    </html>
  );
}
