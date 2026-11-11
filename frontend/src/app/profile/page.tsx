"use client";

import React, { useState } from "react";
import Link from "next/link";
import { useApp } from "@/context/AppContext";
import { 
  UserIcon, 
  CheckIcon, 
  SparklesIcon, 
  ScaleIcon, 
  FlameIcon,
  CookingPotIcon,
  ChevronRightIcon
} from "@/components/ui/Icons";

export default function ProfilePage() {
  const { language, userProfile, updateUserProfile, bmi, bmiCategory, logout } = useApp();

  const [name, setName] = useState(userProfile.name || "");
  const [age, setAge] = useState<number | "">(userProfile.age || 28);
  const [height, setHeight] = useState<number | "">(userProfile.height_cm || 165);
  const [weight, setWeight] = useState<number | "">(userProfile.weight_kg || 60);
  const [preferenceMeal, setPreferenceMeal] = useState(userProfile.preference_meal || "ကြက်သားနှင့် ဟင်းသီးဟင်းရွက်");
  const [savedSuccess, setSavedSuccess] = useState(false);

  // Live BMI calculation during edits
  const currentHeightM = (Number(height) || 165) / 100;
  const currentWeightKg = Number(weight) || 60;
  const liveBmi = Math.round((currentWeightKg / (currentHeightM * currentHeightM)) * 10) / 10;

  // BMR & Daily Calorie Estimate (Mifflin-St Jeor formula)
  const estimatedCalories = Math.round(10 * currentWeightKg + 6.25 * (currentHeightM * 100) - 5 * (Number(age) || 28) + 5);
  const estimatedProtein = Math.round(currentWeightKg * 1.2); // ~1.2g per kg

  const handleSave = (e: React.FormEvent) => {
    e.preventDefault();
    updateUserProfile({
      name,
      age: Number(age) || 28,
      height_cm: Number(height) || 165,
      weight_kg: Number(weight) || 60,
      preference_meal: preferenceMeal,
    });
    setSavedSuccess(true);
    setTimeout(() => setSavedSuccess(false), 2500);
  };

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-8 animate-in fade-in duration-300">
      {/* Page Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-[var(--color-border)] pb-6">
        <div className="flex items-center gap-4">
          <div
            className="w-14 h-14 rounded-2xl flex items-center justify-center text-white font-extrabold text-2xl shadow-md"
            style={{ backgroundColor: "var(--color-primary)" }}
          >
            {name ? name.slice(0, 1) : "👤"}
          </div>
          <div>
            <span className="text-xs font-bold uppercase tracking-wider text-[var(--color-primary)] block">
              {language === "mm" ? "အသုံးပြုသူ ကိုယ်ရေးမှတ်တမ်း" : "User Profile & Health Metrics"}
            </span>
            <h1 className="text-2xl sm:text-3xl font-black text-stone-900">
              {name || "User Profile"}
            </h1>
            <p className="text-xs text-stone-500">
              {userProfile.email}
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <Link
            href="/"
            className="px-4 py-2 rounded-xl text-xs font-bold border border-stone-200 bg-white hover:bg-stone-50 text-stone-700 transition-all flex items-center gap-1.5 shadow-2xs"
          >
            <span>{language === "mm" ? "ပင်မစာမျက်နှာ အကြံပြုချက်များ ကြည့်မည်" : "View Home Recommendations"}</span>
            <ChevronRightIcon className="w-3.5 h-3.5 text-stone-400" />
          </Link>
          <button
            type="button"
            onClick={logout}
            className="px-3.5 py-2 rounded-xl text-xs font-semibold text-stone-400 hover:text-red-600 transition-colors"
          >
            {language === "mm" ? "ထွက်မည်" : "Sign Out"}
          </button>
        </div>
      </div>

      {savedSuccess && (
        <div className="p-4 bg-emerald-50 border border-emerald-200 text-emerald-800 text-xs font-bold rounded-2xl flex items-center gap-2 shadow-xs animate-in zoom-in-95">
          <CheckIcon className="w-4 h-4 text-emerald-700" />
          <span>
            {language === "mm"
              ? "ကျန်းမာရေးနှင့် ကိုယ်ရေးမှတ်တမ်း အချက်အလက်များ အောင်မြင်စွာ သိမ်းဆည်းပြီးပါပြီ!"
              : "Profile & Health metrics successfully updated!"}
          </span>
        </div>
      )}

      {/* Health Overview Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {/* BMI Card */}
        <div className="bg-white rounded-3xl p-6 border border-[var(--color-border)] shadow-sm space-y-2">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold text-stone-400 uppercase tracking-wider">
              Body Mass Index (BMI)
            </span>
            <span className={`px-2.5 py-0.5 rounded-full text-[11px] font-bold border ${bmiCategory.color}`}>
              {language === "mm" ? bmiCategory.label_mm.split("(")[0] : bmiCategory.label_en.split("(")[0]}
            </span>
          </div>
          <div className="flex items-baseline gap-2">
            <span className="text-3xl sm:text-4xl font-black text-stone-900">{liveBmi}</span>
            <span className="text-xs text-stone-400 font-semibold">kg/m²</span>
          </div>
          <p className="text-xs text-stone-500 leading-relaxed pt-1">
            {language === "mm" ? bmiCategory.recommendation_mm : bmiCategory.recommendation_en}
          </p>
        </div>

        {/* Daily Calorie Target Card */}
        <div className="bg-white rounded-3xl p-6 border border-[var(--color-border)] shadow-sm space-y-2">
          <div className="flex items-center gap-1.5 text-xs font-bold text-orange-600">
            <FlameIcon className="w-4 h-4" />
            <span>Daily Calorie Needs</span>
          </div>
          <div className="flex items-baseline gap-2">
            <span className="text-3xl sm:text-4xl font-black text-stone-900">{estimatedCalories.toLocaleString()}</span>
            <span className="text-xs text-stone-400 font-semibold">kcal / day</span>
          </div>
          <p className="text-xs text-stone-500 leading-relaxed pt-1">
            {language === "mm"
              ? "သင့်အရပ်နှင့် ကိုယ်အလေးချိန်အလိုက် တစ်နေ့တာ အခြေခံလိုအပ်သော ကယ်လိုရီပမာဏ။"
              : "Calculated based on Mifflin-St Jeor formula for your age, height, and weight."}
          </p>
        </div>

        {/* Daily Protein Target Card */}
        <div className="bg-white rounded-3xl p-6 border border-[var(--color-border)] shadow-sm space-y-2">
          <div className="flex items-center gap-1.5 text-xs font-bold text-[var(--color-primary)]">
            <CookingPotIcon className="w-4 h-4" />
            <span>Daily Protein Target</span>
          </div>
          <div className="flex items-baseline gap-2">
            <span className="text-3xl sm:text-4xl font-black text-stone-900">{estimatedProtein}</span>
            <span className="text-xs text-stone-400 font-semibold">grams / day</span>
          </div>
          <p className="text-xs text-stone-500 leading-relaxed pt-1">
            {language === "mm"
              ? "ကြွက်သားတည်ဆောက်မှုနှင့် ကျန်းမာရေးအတွက် လိုအပ်သော ပရိုတင်းပမာဏ။"
              : "Recommended daily dietary protein allowance (1.2g/kg) to maintain lean mass."}
          </p>
        </div>
      </div>

      {/* Customization Form */}
      <form onSubmit={handleSave} className="bg-white p-6 sm:p-8 rounded-3xl border border-[var(--color-border)] shadow-md space-y-6">
        <div>
          <h2 className="text-lg font-extrabold text-stone-900">
            {language === "mm" ? "ကိုယ်ရေးအချက်အလက် ပြင်ဆင်ရန်" : "Customize Profile Information"}
          </h2>
          <p className="text-xs text-stone-500 mt-0.5">
            {language === "mm"
              ? "အောက်ပါ အချက်အလက်များအပေါ် အခြေခံ၍ ပင်မစာမျက်နှာတွင် သင့်အတွက် အသင့်တော်ဆုံး ဟင်းလျာများကို ရွေးချယ်ပေးပါမည်။"
              : "Zay Chin uses these parameters to curate personalized meal recommendations on your homepage."}
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
          {/* Name */}
          <div className="space-y-1.5">
            <label className="text-xs font-bold text-stone-700 block uppercase tracking-wider">
              {language === "mm" ? "အမည်" : "Name"}
            </label>
            <input
              type="text"
              required
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="w-full px-4 py-3 rounded-xl border border-stone-200 bg-stone-50 text-sm focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)]"
            />
          </div>

          {/* Age */}
          <div className="space-y-1.5">
            <label className="text-xs font-bold text-stone-700 block uppercase tracking-wider">
              {language === "mm" ? "အသက် (နှစ်)" : "Age (Years)"}
            </label>
            <input
              type="number"
              min="10"
              max="120"
              required
              value={age}
              onChange={(e) => setAge(e.target.value ? Number(e.target.value) : "")}
              className="w-full px-4 py-3 rounded-xl border border-stone-200 bg-stone-50 text-sm focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)]"
            />
          </div>

          {/* Height */}
          <div className="space-y-1.5">
            <div className="flex justify-between items-center">
              <label className="text-xs font-bold text-stone-700 uppercase tracking-wider">
                {language === "mm" ? "အရပ် (စင်တီမီတာ)" : "Height (cm)"}
              </label>
              <span className="text-[11px] text-stone-400 font-semibold">
                {Math.floor((Number(height) || 165) / 30.48)}&apos; {Math.round(((Number(height) || 165) % 30.48) / 2.54)}&quot;
              </span>
            </div>
            <input
              type="number"
              min="90"
              max="240"
              required
              value={height}
              onChange={(e) => setHeight(e.target.value ? Number(e.target.value) : "")}
              className="w-full px-4 py-3 rounded-xl border border-stone-200 bg-stone-50 text-sm focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] font-bold"
            />
          </div>

          {/* Weight */}
          <div className="space-y-1.5">
            <div className="flex justify-between items-center">
              <label className="text-xs font-bold text-stone-700 uppercase tracking-wider">
                {language === "mm" ? "ကိုယ်အလေးချိန် (ကီလိုဂရမ်)" : "Weight (kg)"}
              </label>
              <span className="text-[11px] text-stone-400 font-semibold">
                ~{Math.round((Number(weight) || 60) * 2.20462)} lbs
              </span>
            </div>
            <input
              type="number"
              min="25"
              max="250"
              required
              value={weight}
              onChange={(e) => setWeight(e.target.value ? Number(e.target.value) : "")}
              className="w-full px-4 py-3 rounded-xl border border-stone-200 bg-stone-50 text-sm focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] font-bold"
            />
          </div>
        </div>

        {/* Preference Meal */}
        <div className="space-y-2 pt-2">
          <label className="text-xs font-bold text-stone-700 block uppercase tracking-wider">
            {language === "mm" ? "နှစ်သက်သော ဟင်းလျာ အမျိုးအစား (Preference Meal)" : "Dietary & Meal Preferences"}
          </label>
          <div className="grid grid-cols-2 sm:grid-cols-3 gap-2">
            {[
              { id: "ကြက်သားနှင့် ဟင်းသီးဟင်းရွက်", label_mm: "ကြက်သားနှင့် ဟင်းသီးဟင်းရွက်", label_en: "Chicken & Veggies" },
              { id: "ငါးနှင့် ပင်လယ်စာ", label_mm: "ငါးနှင့် ပင်လယ်စာ", label_en: "Fish & Seafood" },
              { id: "သက်သတ်လွတ်", label_mm: "သက်သတ်လွတ်", label_en: "Vegetarian" },
              { id: "အဆီလျှော့ အရည်သောက်ဟင်း", label_mm: "အဆီလျှော့ အရည်သောက်ဟင်း", label_en: "Clear Soups (Low Cal)" },
              { id: "အသားဟင်းနှင့် ပရိုတင်းများ", label_mm: "အသားဟင်းနှင့် ပရိုတင်းများ", label_en: "High Protein Meats" },
              { id: "မြန်မာ့ရိုးရာ အသုပ်စုံ", label_mm: "မြန်မာ့ရိုးရာ အသုပ်စုံ", label_en: "Traditional Salads" },
            ].map((p) => (
              <button
                key={p.id}
                type="button"
                onClick={() => setPreferenceMeal(p.id)}
                className={`p-3 rounded-2xl text-xs font-bold text-left border transition-all ${
                  preferenceMeal === p.id
                    ? "bg-[var(--color-muted)] border-[var(--color-primary)] text-[var(--color-primary)] shadow-xs"
                    : "bg-stone-50 border-stone-200 text-stone-700 hover:bg-stone-100"
                }`}
              >
                {language === "mm" ? p.label_mm : p.label_en}
              </button>
            ))}
          </div>
        </div>

        {/* Action Button */}
        <div className="pt-4 border-t border-stone-100 flex items-center justify-end gap-3">
          <button
            type="submit"
            className="px-7 py-3 rounded-xl text-white font-extrabold text-xs sm:text-sm shadow-md hover:shadow-lg transition-all active:scale-95 flex items-center gap-2 hover:opacity-95"
            style={{ backgroundColor: "var(--color-primary)" }}
          >
            <CheckIcon className="w-4 h-4" />
            <span>{language === "mm" ? "အချက်အလက်များ သိမ်းဆည်းမည်" : "Save Changes"}</span>
          </button>
        </div>
      </form>
    </div>
  );
}
