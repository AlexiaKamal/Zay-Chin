"use client";

import React from "react";
import Link from "next/link";
import { useApp } from "@/context/AppContext";
import { CookingPotIcon } from "@/components/ui/Icons";

export function Footer() {
  const { language, t } = useApp();

  return (
    <footer className="bg-stone-900 text-stone-300 border-t border-stone-800 mt-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 lg:py-16">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 lg:gap-12">
          {/* Brand & Purpose */}
          <div className="md:col-span-2 space-y-4">
            <div className="flex items-center gap-2.5">
              <div className="w-8 h-8 rounded-lg bg-emerald-700 flex items-center justify-center text-white">
                <CookingPotIcon className="w-5 h-5 text-amber-200" />
              </div>
              <span className="font-bold text-xl text-white">
                {language === "mm" ? "ဈေးခြင်း" : "Zay Chin"}
              </span>
            </div>
            <p className="text-sm text-stone-400 max-w-md leading-relaxed">
              {t.footer_desc}
            </p>
            <div className="p-3 bg-stone-800/60 rounded-xl border border-stone-700/60 text-xs text-stone-300 space-y-1">
              <span className="font-semibold text-emerald-400 block">
                {language === "mm" ? "ဟင်းချက်နည်း မူရင်းစာအုပ် ကိုးကားချက်" : "Original Cookbook Reference"}:
              </span>
              <p>
                {t.source_citation_text}
              </p>
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="font-semibold text-white text-sm tracking-wider uppercase mb-4">
              {language === "mm" ? "အဓိက ကဏ္ဍများ" : "Explore"}
            </h4>
            <ul className="space-y-2.5 text-sm">
              <li>
                <Link href="/recipes" className="hover:text-emerald-400 transition-colors">
                  {t.nav_recipes}
                </Link>
              </li>
              <li>
                <Link href="/planner" className="hover:text-emerald-400 transition-colors">
                  {t.nav_planner}
                </Link>
              </li>
              <li>
                <Link href="/grocery-list" className="hover:text-emerald-400 transition-colors">
                  {t.nav_grocery}
                </Link>
              </li>
              <li>
                <Link href="/markets" className="hover:text-emerald-400 transition-colors">
                  {t.nav_markets}
                </Link>
              </li>
            </ul>
          </div>

          {/* Data Sources */}
          <div>
            <h4 className="font-semibold text-white text-sm tracking-wider uppercase mb-4">
              {language === "mm" ? "အချက်အလက် ရင်းမြစ်များ" : "Data Sources"}
            </h4>
            <ul className="space-y-2 text-xs text-stone-400">
              <li>• Myanmar Central Statistical Organization (CSO)</li>
              <li>• Yangon Commodity Exchange (Bayintnaung)</li>
              <li>• Citymall Myanmar (City Mart Retail)</li>
              <li>• World Bank Microdata (Real Time Food Prices)</li>
              <li>• USDA FoodData Central & Thai FCD (INMU)</li>
            </ul>
          </div>
        </div>

        <div className="mt-12 pt-8 border-t border-stone-800 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-stone-500">
          <p>© 2026 Zay Chin (ဈေးခြင်း). {t.footer_rights}</p>
          <p className="text-stone-400">
            {language === "mm" ? "မြန်မာ ယူနီကုဒ် စံချိန်မီ စနစ်" : "Built with Standard Myanmar Unicode"}
          </p>
        </div>
      </div>
    </footer>
  );
}
