"use client";

import React, { useEffect, useState } from "react";
import { useApp } from "@/context/AppContext";
import { getMarkets } from "@/lib/api";
import { Market } from "@/types";
import { StoreIcon, MapPinIcon, CheckIcon } from "@/components/ui/Icons";

export default function MarketsPage() {
  const { language, city, setCity, t } = useApp();
  const [markets, setMarkets] = useState<Market[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadMarkets() {
      try {
        setLoading(true);
        const data = await getMarkets(city);
        setMarkets(data);
      } catch (err) {
        console.error("Error loading markets:", err);
      } finally {
        setLoading(false);
      }
    }
    loadMarkets();
  }, [city]);

  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-8">
      {/* Header */}
      <div className="space-y-3 text-center max-w-2xl mx-auto">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 text-xs font-bold">
          <StoreIcon className="w-4 h-4 text-emerald-700" />
          <span>{language === "mm" ? "စစ်မှန်သော ဈေးကွက်နေရာများ" : "Verified Market Directory"}</span>
        </div>
        <h1 className="text-3xl sm:text-4xl font-extrabold text-stone-900">{t.nav_markets}</h1>
        <p className="text-sm sm:text-base text-stone-600">
          {language === "mm"
            ? "ရန်ကုန်နှင့် မန္တလေးမြို့ရှိ ကုန်စည်ဒိုင်၊ လက်လီစူပါမားကတ်နှင့် ကာလပေါက်ဈေး စစ်တမ်းကောက်ယူရာ နေရာများ။"
            : "Search and compare wholesale commodity exchanges, supermarket branches, and regional market survey points in Yangon and Mandalay."}
        </p>

        {/* City Toggle */}
        <div className="flex justify-center gap-2 pt-2">
          <button
            type="button"
            onClick={() => setCity("Yangon")}
            className={`px-4 py-2 rounded-xl text-xs font-bold transition-all ${
              city === "Yangon"
                ? "bg-emerald-800 text-white shadow-md"
                : "bg-white text-stone-700 border border-stone-200 hover:bg-stone-50"
            }`}
          >
            {t.city_yangon}
          </button>
          <button
            type="button"
            onClick={() => setCity("Mandalay")}
            className={`px-4 py-2 rounded-xl text-xs font-bold transition-all ${
              city === "Mandalay"
                ? "bg-emerald-800 text-white shadow-md"
                : "bg-white text-stone-700 border border-stone-200 hover:bg-stone-50"
            }`}
          >
            {t.city_mandalay}
          </button>
        </div>
      </div>

      {/* Markets Grid */}
      {loading ? (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {[1, 2, 3, 4].map((i) => (
            <div key={i} className="h-44 bg-stone-100 rounded-3xl animate-pulse" />
          ))}
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {markets.map((m) => (
            <div
              key={m.id}
              className="bg-white rounded-3xl border border-stone-200 p-6 sm:p-7 shadow-xs hover:border-emerald-300 transition-all space-y-4"
            >
              <div className="flex items-start justify-between gap-3">
                <div className="space-y-1">
                  <span className="px-2.5 py-0.5 rounded-md text-[11px] font-bold uppercase tracking-wider bg-emerald-50 text-emerald-800 border border-emerald-100">
                    {m.market_type}
                  </span>
                  <h3 className="text-lg font-bold text-stone-900 pt-1">
                    {m.name}
                  </h3>
                  <p className="text-xs text-stone-500 font-medium">
                    {m.vendor_name || m.city}
                  </p>
                </div>
                <div className="w-10 h-10 rounded-xl bg-stone-50 border border-stone-200 flex items-center justify-center shrink-0">
                  <MapPinIcon className="w-5 h-5 text-emerald-700" />
                </div>
              </div>

              <p className="text-xs text-stone-600 leading-relaxed">
                {m.address || "Physical location in " + m.city}
              </p>

              <div className="pt-3 border-t border-stone-100 flex items-center justify-between text-xs text-stone-500">
                <div className="flex items-center gap-1.5">
                  <CheckIcon className="w-3.5 h-3.5 text-emerald-700" />
                  <span>
                    {m.recorded_price_observations_count}{" "}
                    {language === "mm" ? "ဈေးနှုန်းမှတ်တမ်းများ" : "Recorded Price Observations"}
                  </span>
                </div>
                {m.has_verified_coordinates && (
                  <span className="text-[11px] text-emerald-700 font-bold bg-emerald-50 px-2 py-0.5 rounded">
                    GPS Verified
                  </span>
                )}
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Transparency Note */}
      <div className="p-5 bg-stone-50 border border-stone-200 rounded-2xl text-xs text-stone-500 text-center max-w-2xl mx-auto leading-relaxed">
        {language === "mm"
          ? "ဈေးခြင်း သည် အမှန်တကယ် စစ်တမ်းကောက်ယူထားသော ဈေးကွက်တည်နေရာများကိုသာ ဖော်ပြပြီး အတည်မပြုနိုင်သော ဈေးဆိုင်တည်နေရာများအား မုသားဖြင့် ထည့်သွင်းခြင်း မပြုပါ။"
          : "Zero-Hallucination Policy: Zay Chin only indexes verified municipal commodity exchanges and published retail outlets. Fake coordinates and fictitious stalls are strictly prohibited."}
      </div>
    </div>
  );
}
