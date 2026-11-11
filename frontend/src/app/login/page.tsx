"use client";

import React, { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useApp } from "@/context/AppContext";
import { CookingPotIcon, SparklesIcon, CheckIcon } from "@/components/ui/Icons";

export default function LoginPage() {
  const { language, login, updateUserProfile, userProfile } = useApp();
  const router = useRouter();

  const [mode, setMode] = useState<"login" | "register">("login");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [name, setName] = useState("");
  const [age, setAge] = useState<number | "">(28);
  const [height, setHeight] = useState<number | "">(165);
  const [weight, setWeight] = useState<number | "">(60);
  const [preferenceMeal, setPreferenceMeal] = useState("ကြက်သားနှင့် ဟင်းသီးဟင်းရွက်");
  const [successMsg, setSuccessMsg] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (!email) return;

    if (mode === "register") {
      updateUserProfile({
        email,
        name: name || email.split("@")[0],
        age: age ? Number(age) : 28,
        height_cm: height ? Number(height) : 165,
        weight_kg: weight ? Number(weight) : 60,
        preference_meal: preferenceMeal,
        isLoggedIn: true,
      });
      setSuccessMsg(language === "mm" ? "အကောင့် အောင်မြင်စွာ ဖွင့်ပြီးပါပြီ!" : "Account created successfully!");
    } else {
      login(email, name || userProfile.name);
      setSuccessMsg(language === "mm" ? "အောင်မြင်စွာ အကောင့်ဝင်ပြီးပါပြီ!" : "Logged in successfully!");
    }

    setTimeout(() => {
      router.push("/profile");
    }, 600);
  };

  return (
    <div className="max-w-md mx-auto px-4 py-16 space-y-8 animate-in fade-in duration-300">
      {/* Brand Header */}
      <div className="text-center space-y-3">
        <div
          className="w-14 h-14 rounded-2xl mx-auto flex items-center justify-center text-white shadow-lg"
          style={{ backgroundColor: "var(--color-primary)" }}
        >
          <CookingPotIcon className="w-8 h-8 text-amber-200" />
        </div>
        <h1 className="text-2xl sm:text-3xl font-black text-stone-900">
          {mode === "login"
            ? language === "mm"
              ? "ဈေးခြင်း အကောင့်သို့ ဝင်ရောက်ပါ"
              : "Welcome back to Zay Chin"
            : language === "mm"
            ? "အကောင့် အသစ် ဖွင့်ပါ"
            : "Create your Zay Chin Account"}
        </h1>
        <p className="text-xs sm:text-sm text-stone-600">
          {language === "mm"
            ? "သင့်ကျန်းမာရေးနှင့် ဘတ်ဂျက်အလိုက် အစားအသောက်များကို တိကျစွာ စီစဉ်နိုင်ပါပြီ။"
            : "Personalized meal planning and grocery budgeting based on your health profile."}
        </p>
      </div>

      {/* Tabs */}
      <div className="bg-stone-100 p-1 rounded-2xl grid grid-cols-2 text-xs font-bold">
        <button
          type="button"
          onClick={() => setMode("login")}
          className={`py-2.5 rounded-xl transition-all ${
            mode === "login" ? "bg-white text-stone-900 shadow-xs" : "text-stone-500 hover:text-stone-900"
          }`}
        >
          {language === "mm" ? "အကောင့်ဝင်ရန် (Sign In)" : "Sign In"}
        </button>
        <button
          type="button"
          onClick={() => setMode("register")}
          className={`py-2.5 rounded-xl transition-all ${
            mode === "register" ? "bg-white text-stone-900 shadow-xs" : "text-stone-500 hover:text-stone-900"
          }`}
        >
          {language === "mm" ? "အကောင့်သစ်ဖွင့်ရန် (Sign Up)" : "Sign Up"}
        </button>
      </div>

      {/* Success banner */}
      {successMsg && (
        <div className="p-3 bg-emerald-50 border border-emerald-200 text-emerald-800 text-xs font-bold rounded-xl text-center flex items-center justify-center gap-1.5 animate-in zoom-in-95">
          <CheckIcon className="w-4 h-4 text-emerald-700" />
          <span>{successMsg}</span>
        </div>
      )}

      {/* Form */}
      <form onSubmit={handleSubmit} className="bg-white p-6 sm:p-8 rounded-3xl border border-[var(--color-border)] shadow-md space-y-4">
        {mode === "register" && (
          <div className="space-y-1">
            <label className="text-xs font-bold text-stone-700 block">
              {language === "mm" ? "သင့် အမည်" : "Full Name"}
            </label>
            <input
              type="text"
              required
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder={language === "mm" ? "ဥပမာ- ဒေါ်မြမြ" : "e.g. Mya Mya"}
              className="w-full px-3.5 py-2.5 rounded-xl border border-stone-200 bg-stone-50 text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)]"
            />
          </div>
        )}

        <div className="space-y-1">
          <label className="text-xs font-bold text-stone-700 block">
            {language === "mm" ? "အီးမေးလ် လိပ်စာ" : "Email Address"}
          </label>
          <input
            type="email"
            required
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="mya.mya@example.com"
            className="w-full px-3.5 py-2.5 rounded-xl border border-stone-200 bg-stone-50 text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)]"
          />
        </div>

        <div className="space-y-1">
          <label className="text-xs font-bold text-stone-700 block">
            {language === "mm" ? "စကားဝှက်" : "Password"}
          </label>
          <input
            type="password"
            required
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="••••••••"
            className="w-full px-3.5 py-2.5 rounded-xl border border-stone-200 bg-stone-50 text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)]"
          />
        </div>

        {/* Health fields on registration */}
        {mode === "register" && (
          <div className="space-y-4 pt-3 border-t border-stone-100">
            <span className="text-[11px] font-extrabold uppercase tracking-wider text-[var(--color-primary)] block">
              {language === "mm" ? "ကျန်းမာရေးနှင့် အာဟာရ အချက်အလက်များ" : "Physical & Dietary Metrics"}
            </span>

            <div className="grid grid-cols-3 gap-2">
              <div className="space-y-1">
                <label className="text-[11px] font-bold text-stone-600 block">Age (အသက်)</label>
                <input
                  type="number"
                  value={age}
                  onChange={(e) => setAge(e.target.value ? Number(e.target.value) : "")}
                  className="w-full px-3 py-2 rounded-xl border border-stone-200 text-xs bg-stone-50 text-center font-bold"
                />
              </div>
              <div className="space-y-1">
                <label className="text-[11px] font-bold text-stone-600 block">Height (cm)</label>
                <input
                  type="number"
                  value={height}
                  onChange={(e) => setHeight(e.target.value ? Number(e.target.value) : "")}
                  className="w-full px-3 py-2 rounded-xl border border-stone-200 text-xs bg-stone-50 text-center font-bold"
                />
              </div>
              <div className="space-y-1">
                <label className="text-[11px] font-bold text-stone-600 block">Weight (kg)</label>
                <input
                  type="number"
                  value={weight}
                  onChange={(e) => setWeight(e.target.value ? Number(e.target.value) : "")}
                  className="w-full px-3 py-2 rounded-xl border border-stone-200 text-xs bg-stone-50 text-center font-bold"
                />
              </div>
            </div>

            <div className="space-y-1">
              <label className="text-xs font-bold text-stone-700 block">
                {language === "mm" ? "နှစ်သက်သော အစားအစာ (Preference Meal)" : "Meal Preference"}
              </label>
              <select
                value={preferenceMeal}
                onChange={(e) => setPreferenceMeal(e.target.value)}
                className="w-full px-3 py-2.5 rounded-xl border border-stone-200 bg-stone-50 text-xs font-medium focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)]"
              >
                <option value="ကြက်သားနှင့် ဟင်းသီးဟင်းရွက်">ကြက်သားနှင့် ဟင်းသီးဟင်းရွက် (Chicken & Veggies)</option>
                <option value="ငါးနှင့် ပင်လယ်စာ">ငါးနှင့် ပင်လယ်စာ (Fish & Seafood)</option>
                <option value="သက်သတ်လွတ်">သက်သတ်လွတ် (Vegetarian)</option>
                <option value="အဆီလျှော့ အရည်သောက်ဟင်း">အဆီလျှော့ အရည်သောက်ဟင်း (Low Calorie / Soups)</option>
                <option value="အသားဟင်းနှင့် ပရိုတင်းများ">အသားဟင်းနှင့် ပရိုတင်းများ (High Protein)</option>
                <option value="မြန်မာ့ရိုးရာ အသုပ်စုံ">မြန်မာ့ရိုးရာ အသုပ်စုံ (Burmese Salads)</option>
              </select>
            </div>
          </div>
        )}

        <button
          type="submit"
          className="w-full py-3 rounded-xl text-white font-extrabold text-xs sm:text-sm shadow-md hover:shadow-lg transition-all active:scale-95 flex items-center justify-center gap-1.5 hover:opacity-95 mt-4"
          style={{ backgroundColor: "var(--color-primary)" }}
        >
          <span>{mode === "login" ? (language === "mm" ? "အကောင့်ဝင်မည်" : "Sign In") : (language === "mm" ? "အကောင့်ဖွင့်ပြီး စတင်မည်" : "Create Account")}</span>
        </button>
      </form>
    </div>
  );
}
