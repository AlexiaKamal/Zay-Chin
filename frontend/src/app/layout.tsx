import React from "react";
import type { Metadata } from "next";
import "./globals.css";
import { AppProvider } from "@/context/AppContext";
import { Navbar } from "@/components/layout/Navbar";
import { Footer } from "@/components/layout/Footer";

export const metadata: Metadata = {
  title: "Zay Chin (ဈေးခြင်း) — Intelligent Myanmar Meal Planning & Budgeting",
  description: "Plan authentic Myanmar meals, calculate real-time grocery costs in MMK from verified market observations, and optimize nutrition with zero hallucinated pricing.",
  keywords: "Myanmar recipes, Burmese food, meal planner, Yangon grocery prices, Mandalay market, Zay Chin, Daw San Lay, ချက်ပြုတ်နည်းများ, ဈေးခြင်း",
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
      <body className="min-h-screen bg-[#faf8f5] text-stone-900 font-sans antialiased flex flex-col selection:bg-emerald-100 selection:text-emerald-900">
        <AppProvider>
          <React.Suspense fallback={<div className="h-16 bg-white border-b border-stone-200" />}>
            <Navbar />
          </React.Suspense>
          <main className="flex-grow">
            {children}
          </main>
          <Footer />
        </AppProvider>
      </body>
    </html>
  );
}
