"use client";

import React, { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useApp } from "@/context/AppContext";
import {
  CookingPotIcon,
  GlobeIcon,
  MapPinIcon,
  MenuIcon,
  XIcon,
  SparklesIcon,
} from "@/components/ui/Icons";

export function Navbar() {
  const { language, setLanguage, city, setCity, t } = useApp();
  const pathname = usePathname();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const navLinks = [
    { href: "/", label: t.nav_home },
    { href: "/recipes", label: t.nav_recipes },
    { href: "/planner", label: t.nav_planner },
    { href: "/grocery-list", label: t.nav_grocery },
    { href: "/markets", label: t.nav_markets },
  ];

  return (
    <header className="sticky top-0 z-50 bg-white/90 backdrop-blur-md border-b border-stone-200 transition-all">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo & Brand */}
          <Link href="/" className="flex items-center gap-2.5 group">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-emerald-600 to-teal-800 flex items-center justify-center text-white shadow-md shadow-emerald-700/20 group-hover:scale-105 transition-transform">
              <CookingPotIcon className="w-6 h-6 text-amber-200" />
            </div>
            <div>
              <span className="font-extrabold text-xl tracking-tight text-stone-900 group-hover:text-emerald-700 transition-colors">
                {language === "mm" ? "ဈေးခြင်း" : "Zay Chin"}
              </span>
              <span className="hidden sm:inline-block ml-1.5 px-2 py-0.5 text-xs font-semibold rounded-full bg-emerald-50 text-emerald-800 border border-emerald-200/60">
                {language === "mm" ? "မြန်မာ့အစားအစာ" : "Myanmar Culinary"}
              </span>
            </div>
          </Link>

          {/* Desktop Navigation Links */}
          <nav className="hidden md:flex items-center gap-1 lg:gap-2">
            {navLinks.map((link) => {
              const isActive = pathname === link.href || (link.href !== "/" && pathname.startsWith(link.href));
              return (
                <Link
                  key={link.href}
                  href={link.href}
                  className={`px-3 py-2 rounded-lg text-sm font-medium transition-colors ${
                    isActive
                      ? "bg-emerald-50 text-emerald-800 font-semibold"
                      : "text-stone-600 hover:text-stone-900 hover:bg-stone-50"
                  }`}
                >
                  {link.label}
                </Link>
              );
            })}
          </nav>

          {/* Controls: City & Language */}
          <div className="hidden sm:flex items-center gap-3">
            {/* City Selector */}
            <div className="flex items-center bg-stone-100 rounded-lg p-1 border border-stone-200 text-xs">
              <MapPinIcon className="w-3.5 h-3.5 text-stone-500 ml-1.5 mr-1" />
              <button
                type="button"
                onClick={() => setCity("Yangon")}
                className={`px-2 py-1 rounded-md transition-all font-medium ${
                  city === "Yangon"
                    ? "bg-white text-emerald-900 shadow-xs font-bold"
                    : "text-stone-600 hover:text-stone-900"
                }`}
              >
                {t.city_yangon}
              </button>
              <button
                type="button"
                onClick={() => setCity("Mandalay")}
                className={`px-2 py-1 rounded-md transition-all font-medium ${
                  city === "Mandalay"
                    ? "bg-white text-emerald-900 shadow-xs font-bold"
                    : "text-stone-600 hover:text-stone-900"
                }`}
              >
                {t.city_mandalay}
              </button>
            </div>

            {/* Language Switcher */}
            <button
              type="button"
              onClick={() => setLanguage(language === "en" ? "mm" : "en")}
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-stone-200 text-xs font-semibold bg-stone-50 text-stone-700 hover:bg-stone-100 transition-colors shadow-xs"
              title="Switch language / ဘာသာစကားပြောင်းရန်"
            >
              <GlobeIcon className="w-3.5 h-3.5 text-emerald-700" />
              <span>{language === "en" ? "မြန်မာ" : "English"}</span>
            </button>
          </div>

          {/* Mobile menu button */}
          <div className="flex sm:hidden items-center gap-2">
            <button
              type="button"
              onClick={() => setLanguage(language === "en" ? "mm" : "en")}
              className="p-2 text-stone-600 hover:text-stone-900"
            >
              <span className="text-xs font-bold px-2 py-1 bg-stone-100 rounded">
                {language === "en" ? "MM" : "EN"}
              </span>
            </button>
            <button
              type="button"
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="p-2 rounded-lg text-stone-600 hover:text-stone-900 hover:bg-stone-100"
              aria-label="Open menu"
            >
              {mobileMenuOpen ? <XIcon className="w-6 h-6" /> : <MenuIcon className="w-6 h-6" />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Drawer */}
      {mobileMenuOpen && (
        <div className="sm:hidden border-b border-stone-200 bg-white px-4 pt-2 pb-4 space-y-2">
          {navLinks.map((link) => (
            <Link
              key={link.href}
              href={link.href}
              onClick={() => setMobileMenuOpen(false)}
              className="block px-3 py-2 rounded-md text-base font-medium text-stone-700 hover:bg-emerald-50 hover:text-emerald-800"
            >
              {link.label}
            </Link>
          ))}
          <div className="pt-3 border-t border-stone-100 flex items-center justify-between">
            <span className="text-xs font-medium text-stone-500">{t.city_select}:</span>
            <div className="flex gap-2">
              <button
                type="button"
                onClick={() => setCity("Yangon")}
                className={`px-3 py-1 rounded text-xs font-bold ${
                  city === "Yangon" ? "bg-emerald-700 text-white" : "bg-stone-100 text-stone-700"
                }`}
              >
                {t.city_yangon}
              </button>
              <button
                type="button"
                onClick={() => setCity("Mandalay")}
                className={`px-3 py-1 rounded text-xs font-bold ${
                  city === "Mandalay" ? "bg-emerald-700 text-white" : "bg-stone-100 text-stone-700"
                }`}
              >
                {t.city_mandalay}
              </button>
            </div>
          </div>
        </div>
      )}
    </header>
  );
}
