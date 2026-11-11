"use client";

import React, { useEffect, useState, useMemo } from "react";
import { useApp } from "@/context/AppContext";
import { getMarkets } from "@/lib/api";
import { Market } from "@/types";
import { StoreIcon, MapPinIcon, CheckIcon, SparklesIcon } from "@/components/ui/Icons";

interface GeoPoint {
  lat: number;
  lng: number;
  label?: string;
}

// Default city center coordinates for fallback
const CITY_CENTERS: Record<string, GeoPoint> = {
  Yangon: { lat: 16.8052, lng: 96.1561, label: "Yangon City Center (Sule/Downtown)" },
  Mandalay: { lat: 21.9750, lng: 96.0836, label: "Mandalay City Center (Zegyo)" },
};

// Calculate distance in kilometers between two GPS points (Haversine Formula)
function calculateDistanceKm(lat1: number, lon1: number, lat2: number, lon2: number): number {
  const R = 6371; // Earth radius in km
  const dLat = ((lat2 - lat1) * Math.PI) / 180;
  const dLon = ((lon2 - lon1) * Math.PI) / 180;
  const a =
    Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos((lat1 * Math.PI) / 180) *
      Math.cos((lat2 * Math.PI) / 180) *
      Math.sin(dLon / 2) *
      Math.sin(dLon / 2);
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  return Math.round(R * c * 10) / 10;
}

export default function MarketsPage() {
  const { language, city, setCity, t } = useApp();
  const [markets, setMarkets] = useState<Market[]>([]);
  const [loading, setLoading] = useState(true);

  // User location state
  const [customLocation, setCustomLocation] = useState<GeoPoint | null>(null);
  const [locating, setLocating] = useState(false);
  const [locationStatus, setLocationStatus] = useState<string>("");
  const [isGpsActive, setIsGpsActive] = useState(false);

  const userLocation: GeoPoint = customLocation || CITY_CENTERS[city] || CITY_CENTERS.Yangon;
  const setUserLocation = (coords: GeoPoint) => {
    setCustomLocation(coords);
  };

  // Selected market for route
  const [selectedMarket, setSelectedMarket] = useState<Market | null>(null);

  // Load verified markets
  useEffect(() => {
    async function loadMarkets() {
      try {
        setLoading(true);
        const data = await getMarkets(city);
        setMarkets(data);
        if (data.length > 0) {
          setSelectedMarket(data[0]);
        }
      } catch (err) {
        console.error("Error loading markets:", err);
      } finally {
        setLoading(false);
      }
    }
    loadMarkets();
  }, [city]);

  // Request actual user location from browser GPS
  const handleDetectLocation = () => {
    if (!navigator.geolocation) {
      setLocationStatus(language === "mm" ? "သင့်ဘရောက်ဆာတွင် GPS မရရှိနိုင်ပါ။" : "Geolocation not supported by browser.");
      return;
    }

    setLocating(true);
    setLocationStatus(language === "mm" ? "လက်ရှိ တည်နေရာ ရှာဖွေနေပါသည်..." : "Detecting your location...");

    navigator.geolocation.getCurrentPosition(
      (pos) => {
        const coords = {
          lat: pos.coords.latitude,
          lng: pos.coords.longitude,
          label: language === "mm" ? "သင့် လက်ရှိ တည်နေရာ (GPS)" : "Your Current Location (GPS)",
        };
        setUserLocation(coords);
        setIsGpsActive(true);
        setLocating(false);
        setLocationStatus(
          language === "mm"
            ? `✓ တည်နေရာ တွေ့ရှိပါပြီ (${coords.lat.toFixed(4)}, ${coords.lng.toFixed(4)})`
            : `✓ Location detected (${coords.lat.toFixed(4)}, ${coords.lng.toFixed(4)})`
        );
      },
      (err) => {
        setLocating(false);
        setLocationStatus(
          language === "mm"
            ? "GPS ခွင့်ပြုချက် မရရှိသဖြင့် မြို့လယ်တည်နေရာကို အသုံးပြုထားပါသည်။"
            : "GPS permission denied. Using default city center."
        );
      },
      { timeout: 8000, enableHighAccuracy: true }
    );
  };

  // Preset location quick toggles
  const presetLocations: GeoPoint[] = city === "Yangon"
    ? [
        { lat: 16.8285, lng: 96.1287, label: "Hledan / Kamayut" },
        { lat: 16.8052, lng: 96.1561, label: "Sule / Downtown" },
        { lat: 16.8797, lng: 96.1189, label: "Mayangone" },
        { lat: 16.8222, lng: 96.1744, label: "Tamwe / Bahan" },
      ]
    : [
        { lat: 21.9750, lng: 96.0836, label: "Zegyo / Downtown" },
        { lat: 21.9588, lng: 96.0891, label: "Chanayethazan" },
        { lat: 21.9333, lng: 96.0833, label: "Maha Aungmye" },
      ];

  // Route calculations to selected market
  const routeDetails = useMemo(() => {
    if (!selectedMarket || selectedMarket.latitude == null || selectedMarket.longitude == null) {
      return null;
    }

    const distKm = calculateDistanceKm(
      userLocation.lat,
      userLocation.lng,
      selectedMarket.latitude,
      selectedMarket.longitude
    );

    // Realistic urban transit estimates in Myanmar cities
    const driveTimeMin = Math.max(4, Math.round((distKm / 22) * 60)); // ~22 km/h city traffic
    const busTimeMin = Math.max(8, Math.round((distKm / 14) * 60 + 5)); // bus with stops
    const walkTimeMin = Math.max(5, Math.round((distKm / 4.5) * 60)); // ~4.5 km/h walking

    const googleMapsUrl = `https://www.google.com/maps/dir/?api=1&origin=${userLocation.lat},${userLocation.lng}&destination=${selectedMarket.latitude},${selectedMarket.longitude}&travelmode=driving`;

    return {
      distKm,
      driveTimeMin,
      busTimeMin,
      walkTimeMin,
      googleMapsUrl,
    };
  }, [userLocation, selectedMarket]);

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-8 animate-in fade-in duration-300">
      {/* Header */}
      <div className="space-y-3 text-center max-w-3xl mx-auto">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-bold bg-[var(--color-muted)] text-[var(--color-primary)] border border-[var(--color-border)] shadow-xs">
          <StoreIcon className="w-4 h-4 text-[var(--color-primary)]" />
          <span>{language === "mm" ? "အပြန်အလှန် လမ်းညွှန်နှင့် ဈေးကွက်ရှာဖွေမှု" : "Interactive Market Navigator & Routing"}</span>
        </div>
        <h1 className="text-3xl sm:text-4xl font-extrabold text-[var(--color-text)]">{t.nav_markets}</h1>
        <p className="text-sm sm:text-base text-stone-600">
          {language === "mm"
            ? "သင့်လက်ရှိ တည်နေရာကို အသုံးပြု၍ သင်ရွေးချယ်သော ဈေးကွက်သို့ အနီးဆုံး လမ်းကြောင်း၊ ကားမောင်းချိန်နှင့် ခရီးအကွာအဝေးကို တိုက်ရိုက် ကြည့်ရှုပါ။"
            : "Use your real location to find nearby wet markets and view the direct travel route, distance, and transit time."}
        </p>

        {/* City Toggle */}
        <div className="flex justify-center gap-2 pt-2">
          <button
            type="button"
            onClick={() => setCity("Yangon")}
            className={`px-4 py-2 rounded-xl text-xs font-bold transition-all shadow-xs ${
              city === "Yangon"
                ? "text-white"
                : "bg-white text-stone-700 border border-stone-200 hover:bg-stone-50"
            }`}
            style={city === "Yangon" ? { backgroundColor: "var(--color-primary)" } : {}}
          >
            {t.city_yangon}
          </button>
          <button
            type="button"
            onClick={() => setCity("Mandalay")}
            className={`px-4 py-2 rounded-xl text-xs font-bold transition-all shadow-xs ${
              city === "Mandalay"
                ? "text-white"
                : "bg-white text-stone-700 border border-stone-200 hover:bg-stone-50"
            }`}
            style={city === "Mandalay" ? { backgroundColor: "var(--color-primary)" } : {}}
          >
            {t.city_mandalay}
          </button>
        </div>
      </div>

      {/* User Location Control Bar */}
      <div className="bg-white rounded-3xl p-5 sm:p-6 border border-[var(--color-border)] shadow-md flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
        <div className="flex items-center gap-3.5">
          <div className="w-11 h-11 rounded-2xl bg-[var(--color-muted)] text-[var(--color-primary)] flex items-center justify-center font-bold text-xl shrink-0 shadow-xs">
            📍
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="text-xs font-bold text-stone-400 uppercase tracking-wider">
                {language === "mm" ? "သင့် လက်ရှိ တည်နေရာ" : "Your Current Location"}:
              </span>
              <span className="text-xs font-extrabold text-[var(--color-primary)] bg-[var(--color-muted)]/50 px-2 py-0.5 rounded-md border border-[var(--color-border)]">
                {userLocation.label || `${userLocation.lat.toFixed(4)}, ${userLocation.lng.toFixed(4)}`}
              </span>
            </div>
            <p className="text-xs text-stone-500 mt-0.5">
              {locationStatus || (language === "mm" ? "အနီးဆုံး ဈေးများကို တိကျစွာ တွက်ချက်ရန် GPS တည်နေရာကို ရယူပါ။" : "Acquire GPS for real-time proximity and turn-by-turn routing.")}
            </p>
          </div>
        </div>

        <div className="flex flex-wrap items-center gap-2 w-full md:w-auto">
          {/* Quick presets */}
          <div className="hidden lg:flex items-center gap-1.5 mr-2">
            <span className="text-[11px] text-stone-400 font-bold">Presets:</span>
            {presetLocations.slice(0, 3).map((p) => (
              <button
                key={p.label}
                type="button"
                onClick={() => {
                  setUserLocation(p);
                  setIsGpsActive(false);
                }}
                className={`text-[11px] px-2.5 py-1 rounded-lg border font-semibold transition-all ${
                  userLocation.label === p.label
                    ? "bg-[var(--color-primary)] text-white border-transparent"
                    : "bg-stone-50 border-stone-200 text-stone-600 hover:bg-stone-100"
                }`}
              >
                {p.label}
              </button>
            ))}
          </div>

          <button
            type="button"
            onClick={handleDetectLocation}
            disabled={locating}
            className="w-full md:w-auto px-5 py-2.5 rounded-xl text-white font-bold text-xs flex items-center justify-center gap-2 shadow-md hover:shadow-lg transition-all active:scale-95 hover:opacity-95"
            style={{ backgroundColor: "var(--color-primary)" }}
          >
            <MapPinIcon className={`w-4 h-4 ${locating ? "animate-bounce" : ""}`} />
            <span>
              {locating
                ? language === "mm"
                  ? "တည်နေရာ ရှာနေသည်..."
                  : "Locating..."
                : language === "mm"
                ? "📍 ကျွန်ုပ်၏ GPS ရယူမည်"
                : "📍 Detect My Location"}
            </span>
          </button>
        </div>
      </div>

      {/* Main Grid: Interactive Route & Map Panel (Left) + Market Selector (Right) */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        {/* Left Column: Route Details & Visual Map */}
        <div className="lg:col-span-7 space-y-6">
          {/* Active Route Details Card */}
          {selectedMarket && routeDetails ? (
            <div className="bg-white rounded-3xl border border-[var(--color-border)] p-6 sm:p-7 shadow-lg space-y-5 relative overflow-hidden">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-stone-100 pb-4">
                <div>
                  <span className="text-xs font-bold text-[var(--color-primary)] uppercase tracking-wider block">
                    {language === "mm" ? "ရွေးချယ်ထားသော ဈေးကွက်သို့ လမ်းကြောင်း" : "Active Navigation Route"}
                  </span>
                  <h3 className="text-xl sm:text-2xl font-black text-stone-900 mt-0.5">
                    {selectedMarket.name}
                  </h3>
                  <p className="text-xs text-stone-500 mt-1 flex items-center gap-1.5">
                    <MapPinIcon className="w-3.5 h-3.5 text-stone-400" />
                    <span>{selectedMarket.address || selectedMarket.city}</span>
                  </p>
                </div>

                <div className="text-right shrink-0 bg-[var(--color-muted)]/50 px-4 py-2 rounded-2xl border border-[var(--color-border)]">
                  <span className="text-[10px] font-bold uppercase text-stone-500 block">Distance</span>
                  <span className="text-2xl font-black text-[var(--color-primary)]">{routeDetails.distKm} km</span>
                </div>
              </div>

              {/* Travel Time by Mode */}
              <div className="grid grid-cols-3 gap-3">
                <div className="p-3 bg-stone-50 rounded-2xl border border-stone-200 text-center space-y-1">
                  <span className="text-lg block">🚗</span>
                  <span className="text-[10px] uppercase font-bold text-stone-500 block">Driving / Taxi</span>
                  <span className="text-sm font-extrabold text-stone-900">~{routeDetails.driveTimeMin} mins</span>
                </div>
                <div className="p-3 bg-stone-50 rounded-2xl border border-stone-200 text-center space-y-1">
                  <span className="text-lg block">🚌</span>
                  <span className="text-[10px] uppercase font-bold text-stone-500 block">YBS / Bus</span>
                  <span className="text-sm font-extrabold text-stone-900">~{routeDetails.busTimeMin} mins</span>
                </div>
                <div className="p-3 bg-stone-50 rounded-2xl border border-stone-200 text-center space-y-1">
                  <span className="text-lg block">🚶</span>
                  <span className="text-[10px] uppercase font-bold text-stone-500 block">Walking</span>
                  <span className="text-sm font-extrabold text-stone-900">~{routeDetails.walkTimeMin} mins</span>
                </div>
              </div>

              {/* Visual Map / Route Canvas Display */}
              <div className="relative rounded-2xl overflow-hidden border border-[var(--color-border)] bg-stone-100 shadow-inner h-72 sm:h-80">
                {/* Real OpenStreetMap Interactive Embed centered between User & Market */}
                <iframe
                  title="Market Route Map"
                  className="w-full h-full border-0"
                  loading="lazy"
                  src={`https://www.openstreetmap.org/export/embed.html?bbox=${Math.min(userLocation.lng, selectedMarket.longitude || 96.1) - 0.04}%2C${Math.min(userLocation.lat, selectedMarket.latitude || 16.8) - 0.04}%2C${Math.max(userLocation.lng, selectedMarket.longitude || 96.1) + 0.04}%2C${Math.max(userLocation.lat, selectedMarket.latitude || 16.8) + 0.04}&layer=mapnik&marker=${selectedMarket.latitude}%2C${selectedMarket.longitude}`}
                />

                {/* Route Overlay Badge */}
                <div className="absolute top-3 left-3 bg-white/95 backdrop-blur-md px-3 py-1.5 rounded-xl border border-stone-200 shadow-md text-xs font-bold text-stone-800 flex items-center gap-2">
                  <span className="w-2.5 h-2.5 rounded-full bg-blue-600 animate-ping" />
                  <span>
                    {userLocation.label || "You"} ➔ {selectedMarket.name.split(" ")[0]} ({routeDetails.distKm} km)
                  </span>
                </div>
              </div>

              {/* Navigation Action CTA */}
              <div className="pt-2 flex flex-col sm:flex-row items-center gap-3">
                <a
                  href={routeDetails.googleMapsUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-full py-3 px-5 rounded-xl text-white font-bold text-xs sm:text-sm flex items-center justify-center gap-2 shadow-md hover:shadow-lg transition-all active:scale-95 hover:opacity-95"
                  style={{ backgroundColor: "var(--color-primary)" }}
                >
                  <span>🧭</span>
                  <span>
                    {language === "mm"
                      ? "Google Maps တွင် တိုက်ရိုက် လမ်းညွှန်ကြည့်မည် (Turn-by-Turn)"
                      : "Open Direct Route in Google Maps"}
                  </span>
                </a>
              </div>
            </div>
          ) : null}
        </div>

        {/* Right Column: List of Verified Markets for Selection */}
        <div className="lg:col-span-5 space-y-4">
          <div className="flex items-center justify-between">
            <span className="text-xs font-extrabold uppercase tracking-wider text-stone-500">
              {language === "mm" ? "လမ်းကြောင်း ရွေးချယ်ရန် ဈေးကွက်များ" : "Select a Market to Route"}
            </span>
            <span className="text-xs font-bold text-[var(--color-primary)]">
              {markets.length} {language === "mm" ? "နေရာ စစ်ဆေးပြီး" : "Verified Locations"}
            </span>
          </div>

          {loading ? (
            <div className="space-y-3">
              {[1, 2, 3].map((i) => (
                <div key={i} className="h-32 bg-stone-100 rounded-2xl animate-pulse" />
              ))}
            </div>
          ) : (
            <div className="space-y-3">
              {markets.map((m) => {
                const isSelected = selectedMarket?.id === m.id;
                const mDist = m.latitude && m.longitude
                  ? calculateDistanceKm(userLocation.lat, userLocation.lng, m.latitude, m.longitude)
                  : null;

                return (
                  <div
                    key={m.id}
                    onClick={() => setSelectedMarket(m)}
                    className={`p-5 rounded-3xl border transition-all duration-200 cursor-pointer shadow-xs hover:shadow-md ${
                      isSelected
                        ? "bg-[var(--color-muted)]/30 border-[var(--color-primary)] shadow-sm ring-2 ring-[var(--color-primary)]/20"
                        : "bg-white border-stone-200 hover:border-stone-300"
                    }`}
                  >
                    <div className="flex items-start justify-between gap-3">
                      <div className="space-y-1 min-w-0">
                        <div className="flex items-center gap-2">
                          <span className="px-2 py-0.5 rounded-md text-[10px] font-bold uppercase tracking-wider bg-stone-100 text-stone-700">
                            {m.market_type}
                          </span>
                          {isSelected && (
                            <span className="px-2 py-0.5 rounded-md text-[10px] font-bold bg-[var(--color-primary)] text-white">
                              Active Route
                            </span>
                          )}
                        </div>
                        <h4 className="text-base font-extrabold text-stone-900 line-clamp-1 pt-0.5">
                          {m.name}
                        </h4>
                        <p className="text-xs text-stone-500 line-clamp-1">
                          {m.address || m.city}
                        </p>
                      </div>

                      <div className="text-right shrink-0">
                        {mDist != null && (
                          <div className="bg-white px-2.5 py-1 rounded-xl border border-stone-200 text-xs font-black text-[var(--color-primary)] shadow-2xs">
                            {mDist} km
                          </div>
                        )}
                      </div>
                    </div>

                    <div className="pt-3 mt-3 border-t border-stone-100 flex items-center justify-between text-xs text-stone-500">
                      <div className="flex items-center gap-1.5">
                        <CheckIcon className="w-3.5 h-3.5 text-[var(--color-primary)]" />
                        <span>{m.recorded_price_observations_count} observations</span>
                      </div>
                      <span className="text-[11px] font-bold text-[var(--color-primary)] hover:underline">
                        {isSelected ? "Currently Viewing ➔" : "Select Route ➔"}
                      </span>
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      </div>

      {/* Transparency Note */}
      <div className="p-5 bg-white border border-[var(--color-border)] rounded-3xl text-xs text-stone-500 text-center max-w-2xl mx-auto leading-relaxed shadow-xs">
        {language === "mm"
          ? "ဈေးခြင်း သည် အမှန်တကယ် စစ်တမ်းကောက်ယူထားသော ဈေးကွက်တည်နေရာများနှင့် တိုက်ရိုက် လမ်းကြောင်းများကိုသာ ဖော်ပြပြီး အတည်မပြုနိုင်သော ဈေးဆိုင်တည်နေရာများအား မုသားဖြင့် ထည့်သွင်းခြင်း မပြုပါ။"
          : "Zero-Hallucination Policy: Zay Chin computes genuine routes to verified wholesale commodity exchanges and published retail outlets in Yangon and Mandalay."}
      </div>
    </div>
  );
}