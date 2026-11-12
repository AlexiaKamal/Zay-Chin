"use client";

import React, { useState } from "react";
import { useRouter } from "next/navigation";
import { useApp } from "@/context/AppContext";
import {
  CookingPotIcon,
  CheckIcon,
  ClockIcon,
  SparklesIcon,
  UsersIcon,
  FlameIcon,
} from "@/components/ui/Icons";

export default function LoginPage() {
  const { language, login, updateUserProfile, userProfile, setCity } = useApp();
  const router = useRouter();

  const [mode, setMode] = useState<"login" | "register">("login");
  const [signupStep, setSignupStep] = useState<number>(1); // 1 to 6

  // Form State
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [name, setName] = useState("");
  const [age, setAge] = useState<number>(25);
  const [height, setHeight] = useState<string>("165");
  const [weight, setWeight] = useState<string>("58");
  const [selectedCity, setSelectedCity] = useState<"Yangon" | "Mandalay">("Yangon");
  const [address, setAddress] = useState("");
  const [cookingTimePref, setCookingTimePref] = useState<"easy" | "medium" | "hard" | "any">("medium");
  const [mealPref, setMealPref] = useState<string>("curry");

  const [errorMessage, setErrorMessage] = useState("");
  const [successMessage, setSuccessMessage] = useState("");

  // Handle Returning User Login
  const handleLoginSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setErrorMessage("");

    if (!email || !password) {
      setErrorMessage(
        language === "mm"
          ? "အီးမေးလ်နှင့် စကားဝှက်ကို ဖြည့်သွင်းပေးပါ။"
          : "Please enter your email and password."
      );
      return;
    }

    login(email, userProfile.name || email.split("@")[0]);
    setSuccessMessage(
      language === "mm" ? "အောင်မြင်စွာ အကောင့်ဝင်ပြီးပါပြီ။" : "Successfully logged in!"
    );

    setTimeout(() => {
      router.push("/");
    }, 400);
  };

  // Complete Signup Wizard
  const handleFinishSignup = () => {
    updateUserProfile({
      email,
      name: name.trim() || email.split("@")[0],
      age: Number(age) || 25,
      height_cm: height ? Number(height) : undefined,
      weight_kg: weight ? Number(weight) : undefined,
      address: address.trim() || undefined,
      cooking_time_preference: cookingTimePref,
      preference_meal: mealPref,
      isLoggedIn: true,
    });

    if (selectedCity === "Yangon" || selectedCity === "Mandalay") {
      setCity(selectedCity);
    }

    setSuccessMessage(
      language === "mm"
        ? "အကောင့်သစ် အောင်မြင်စွာ ဖန်တီးပြီးပါပြီ။"
        : "Account successfully created!"
    );

    setTimeout(() => {
      router.push("/");
    }, 450);
  };

  const handleNextStep = () => {
    setErrorMessage("");
    if (signupStep === 1) {
      if (!email.trim() || !password.trim()) {
        setErrorMessage(
          language === "mm"
            ? "အီးမေးလ်နှင့် စကားဝှက်ကို ဖြည့်သွင်းပေးပါ။"
            : "Please fill in email and password."
        );
        return;
      }
      if (!email.includes("@")) {
        setErrorMessage(
          language === "mm"
            ? "မှန်ကန်သော အီးမေးလ်လိပ်စာကို ထည့်သွင်းပေးပါ။"
            : "Please enter a valid email address."
        );
        return;
      }
    } else if (signupStep === 2) {
      if (!name.trim()) {
        setErrorMessage(
          language === "mm" ? "သင့်အမည်ကို ထည့်သွင်းပေးပါ။" : "Please enter your name."
        );
        return;
      }
    }

    if (signupStep < 6) {
      setSignupStep((prev) => prev + 1);
    } else {
      handleFinishSignup();
    }
  };

  const handlePrevStep = () => {
    setErrorMessage("");
    if (signupStep > 1) {
      setSignupStep((prev) => prev - 1);
    }
  };

  // Meal preference options
  const mealPrefOptions = [
    {
      id: "curry",
      icon: "🍲",
      label_en: "Curries & Braised Dishes",
      label_mm: "ဆီပြန်ဟင်းနှင့် ဟင်းချက်များ",
      desc_en: "Chicken, pork, fish and rich home curries",
      desc_mm: "ကြက်၊ ဝက်၊ ငါးနှင့် အရသာရှိသော ရိုးရာဆီပြန်ဟင်းများ",
    },
    {
      id: "soup",
      icon: "🥣",
      label_en: "Soups & Clear Broths",
      label_mm: "ဟင်းချိုနှင့် ချဉ်ရည်ဟင်းများ",
      desc_en: "Roselle leaf, bottle gourd and refreshing broths",
      desc_mm: "ချဉ်ပေါင်၊ ဘူးသီးနှင့် လန်းဆန်းစေသော ဟင်းရည်များ",
    },
    {
      id: "salad",
      icon: "🥗",
      label_en: "Fresh Salads (Thoke)",
      label_mm: "ရိုးရာ အသုပ်စုံများ",
      desc_en: "Rice salad, tomato, pennywort and vibrant salads",
      desc_mm: "လက်သုပ်စုံ၊ ခရမ်းချဉ်သီးနှင့် မြင်းခွာရွက်သုပ်များ",
    },
    {
      id: "fried",
      icon: "🍳",
      label_en: "Fried & Stir-Fries",
      label_mm: "အကြော်အလှော်နှင့် ထမင်းကြော်",
      desc_en: "Fried rice, noodles, crispy golden fritters",
      desc_mm: "ထမင်းကြော်၊ ခေါက်ဆွဲကြော်နှင့် ရွှေဝါရောင်အကြော်များ",
    },
    {
      id: "healthy",
      icon: "🥦",
      label_en: "Healthy & Vegetarian",
      label_mm: "ကျန်းမာရေးနှင့် သက်သတ်လွတ်",
      desc_en: "Low oil, fiber-rich vegetables, steamed pulses",
      desc_mm: "ဆီလျှော့၊ အသီးအရွက်နှင့် ပဲဟင်းများ",
    },
    {
      id: "noodles",
      icon: "🍜",
      label_en: "Noodles & Traditional Snacks",
      label_mm: "ခေါက်ဆွဲနှင့် ရိုးရာမုန့်များ",
      desc_en: "Mohinga, coconut noodles, Shan noodles",
      desc_mm: "မုန့်ဟင်းခါး၊ အုန်းနို့ခေါက်ဆွဲ၊ ရှမ်းခေါက်ဆွဲ",
    },
  ];

  return (
    <div className="max-w-xl mx-auto px-4 py-8 sm:py-16 space-y-6">
      {/* Header Logo */}
      <div className="text-center space-y-2">
        <div
          className="w-14 h-14 rounded-2xl mx-auto flex items-center justify-center text-white shadow-md transition-transform hover:scale-105"
          style={{ backgroundColor: "var(--color-primary)" }}
        >
          <CookingPotIcon className="w-8 h-8 text-amber-200" />
        </div>
        <h1 className="text-2xl sm:text-3xl font-black text-stone-900 tracking-tight">
          {mode === "login"
            ? language === "mm"
              ? "ဈေးခြင်း အကောင့်ဝင်ရန်"
              : "Log In to Zay Chin"
            : language === "mm"
            ? "အကောင့်သစ် စတင်ဖွင့်မည်"
            : "Create your Zay Chin Account"}
        </h1>
        <p className="text-xs sm:text-sm text-stone-500">
          {language === "mm"
            ? "မြန်မာ့ရိုးရာ ဟင်းချက်နည်းများနှင့် ဈေးဝယ်စာရင်း စီစဉ်မှု"
            : "Authentic Myanmar meal planning and wet market grocery budgeting"}
        </p>
      </div>

      {/* Mode Switcher Tabs */}
      <div className="bg-stone-100 p-1.5 rounded-2xl grid grid-cols-2 text-xs sm:text-sm font-bold">
        <button
          type="button"
          onClick={() => {
            setMode("login");
            setErrorMessage("");
          }}
          className={`py-2.5 rounded-xl transition-all ${
            mode === "login"
              ? "bg-white text-stone-900 shadow-sm"
              : "text-stone-500 hover:text-stone-800"
          }`}
        >
          {language === "mm" ? "အကောင့်ဝင်မည်" : "Log In"}
        </button>
        <button
          type="button"
          onClick={() => {
            setMode("register");
            setErrorMessage("");
            setSignupStep(1);
          }}
          className={`py-2.5 rounded-xl transition-all ${
            mode === "register"
              ? "bg-white text-stone-900 shadow-sm"
              : "text-stone-500 hover:text-stone-800"
          }`}
        >
          {language === "mm" ? "အကောင့်သစ်ဖွင့်မည်" : "Sign Up"}
        </button>
      </div>

      {/* Feedback Messages */}
      {errorMessage && (
        <div className="p-3.5 bg-red-50 text-red-700 text-xs font-semibold rounded-2xl border border-red-200 animate-in fade-in">
          {errorMessage}
        </div>
      )}
      {successMessage && (
        <div className="p-3.5 bg-emerald-50 text-emerald-800 text-xs font-semibold rounded-2xl border border-emerald-200 flex items-center gap-2 animate-in fade-in">
          <CheckIcon className="w-4 h-4 text-emerald-600" />
          <span>{successMessage}</span>
        </div>
      )}

      {/* MODE 1: RETURNING USER LOGIN */}
      {mode === "login" && (
        <form
          onSubmit={handleLoginSubmit}
          className="bg-white p-6 sm:p-8 rounded-3xl border border-stone-200 shadow-xs space-y-4"
        >
          <div className="space-y-1.5">
            <label className="text-xs font-bold text-stone-700 block">
              {language === "mm" ? "အီးမေးလ် လိပ်စာ" : "Email Address"}
            </label>
            <input
              type="email"
              required
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="example@mail.com"
              className="w-full px-4 py-3 rounded-xl border border-stone-200 bg-stone-50/50 focus:bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] transition-all"
            />
          </div>

          <div className="space-y-1.5">
            <label className="text-xs font-bold text-stone-700 block">
              {language === "mm" ? "စကားဝှက်" : "Password"}
            </label>
            <input
              type="password"
              required
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="••••••••"
              className="w-full px-4 py-3 rounded-xl border border-stone-200 bg-stone-50/50 focus:bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] transition-all"
            />
          </div>

          <button
            type="submit"
            className="w-full py-3.5 mt-2 rounded-xl text-white font-bold text-sm shadow-md transition-all active:scale-98"
            style={{ backgroundColor: "var(--color-primary)" }}
          >
            {language === "mm" ? "အကောင့်ဝင်မည် →" : "Log In →"}
          </button>
        </form>
      )}

      {/* MODE 2: NEW USER SIGN UP WIZARD (ONE QUESTION PER STEP) */}
      {mode === "register" && (
        <div className="bg-white p-6 sm:p-8 rounded-3xl border border-stone-200 shadow-xs space-y-6">
          {/* Progress Bar & Step Indicator */}
          <div className="space-y-2">
            <div className="flex items-center justify-between text-xs font-bold text-stone-500">
              <span>
                {language === "mm" ? `မေးခွန်း ${signupStep} / ၆` : `Step ${signupStep} of 6`}
              </span>
              <span className="text-[var(--color-primary)]">
                {Math.round((signupStep / 6) * 100)}%
              </span>
            </div>
            <div className="w-full h-2 bg-stone-100 rounded-full overflow-hidden">
              <div
                className="h-full transition-all duration-300 rounded-full"
                style={{
                  width: `${(signupStep / 6) * 100}%`,
                  backgroundColor: "var(--color-primary)",
                }}
              />
            </div>
          </div>

          {/* QUESTION 1: EMAIL & PASSWORD */}
          {signupStep === 1 && (
            <div className="space-y-4">
              <div className="space-y-1">
                <h3 className="text-lg font-black text-stone-900">
                  {language === "mm" ? "အကောင့် အချက်အလက်များ" : "Create Account Credentials"}
                </h3>
                <p className="text-xs text-stone-500">
                  {language === "mm"
                    ? "အကောင့်ဝင်ရောက်ရန် အီးမေးလ်နှင့် စကားဝှက်ကို ထည့်သွင်းပါ"
                    : "Enter your email and create a password"}
                </p>
              </div>

              <div className="space-y-1.5">
                <label className="text-xs font-bold text-stone-700 block">
                  {language === "mm" ? "အီးမေးလ်" : "Email"}
                </label>
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="name@example.com"
                  className="w-full px-4 py-3 rounded-xl border border-stone-200 bg-stone-50/50 focus:bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] transition-all"
                />
              </div>

              <div className="space-y-1.5">
                <label className="text-xs font-bold text-stone-700 block">
                  {language === "mm" ? "စကားဝှက်" : "Password"}
                </label>
                <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="••••••••"
                  className="w-full px-4 py-3 rounded-xl border border-stone-200 bg-stone-50/50 focus:bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] transition-all"
                />
              </div>
            </div>
          )}

          {/* QUESTION 2: NAME & AGE */}
          {signupStep === 2 && (
            <div className="space-y-4">
              <div className="space-y-1">
                <h3 className="text-lg font-black text-stone-900">
                  {language === "mm" ? "သင့်အမည်နှင့် အသက်" : "Your Name & Age"}
                </h3>
                <p className="text-xs text-stone-500">
                  {language === "mm"
                    ? "သင့်အား ရင်းနှီးစွာ ခေါ်ဝေါ်နိုင်ရန် ဖြည့်စွက်ပေးပါ"
                    : "Help us personalize your cooking journey"}
                </p>
              </div>

              <div className="space-y-1.5">
                <label className="text-xs font-bold text-stone-700 block">
                  {language === "mm" ? "အမည်" : "Full Name"}
                </label>
                <input
                  type="text"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  placeholder={language === "mm" ? "ဥပမာ - မြမြ" : "e.g. Daw Mya"}
                  className="w-full px-4 py-3 rounded-xl border border-stone-200 bg-stone-50/50 focus:bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] transition-all"
                />
              </div>

              <div className="space-y-1.5">
                <label className="text-xs font-bold text-stone-700 block">
                  {language === "mm" ? "အသက်" : "Age"}
                </label>
                <select
                  value={age}
                  onChange={(e) => setAge(Number(e.target.value))}
                  className="w-full px-4 py-3 rounded-xl border border-stone-200 bg-stone-50/50 focus:bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] transition-all"
                >
                  {Array.from({ length: 65 }, (_, i) => i + 16).map((a) => (
                    <option key={a} value={a}>
                      {a} {language === "mm" ? "နှစ်" : "years old"}
                    </option>
                  ))}
                </select>
              </div>
            </div>
          )}

          {/* QUESTION 3: WEIGHT & HEIGHT (OPTIONAL) */}
          {signupStep === 3 && (
            <div className="space-y-4">
              <div className="space-y-1">
                <div className="flex items-center justify-between">
                  <h3 className="text-lg font-black text-stone-900">
                    {language === "mm" ? "အရပ်နှင့် ကိုယ်အလေးချိန်" : "Height & Weight"}
                  </h3>
                  <span className="text-[11px] font-bold px-2 py-0.5 rounded-md bg-stone-100 text-stone-500">
                    {language === "mm" ? "ရွေးချယ်ရန် (Optional)" : "Optional"}
                  </span>
                </div>
                <p className="text-xs text-stone-500">
                  {language === "mm"
                    ? "သင့်ကျန်းမာရေးနှင့် ကိုက်ညီသော ကယ်လိုရီနှင့် ဟင်းလျာများ တွက်ချက်ပေးရန်ဖြစ်ပါသည်"
                    : "Used to calculate your BMI and personalize healthy calorie recommendations"}
                </p>
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div className="space-y-1.5">
                  <label className="text-xs font-bold text-stone-700 block">
                    {language === "mm" ? "အရပ် (စင်တီမီတာ)" : "Height (cm)"}
                  </label>
                  <input
                    type="number"
                    min="100"
                    max="220"
                    value={height}
                    onChange={(e) => setHeight(e.target.value)}
                    placeholder="165"
                    className="w-full px-4 py-3 rounded-xl border border-stone-200 bg-stone-50/50 focus:bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] transition-all"
                  />
                </div>

                <div className="space-y-1.5">
                  <label className="text-xs font-bold text-stone-700 block">
                    {language === "mm" ? "ကိုယ်အလေးချိန် (ကီလို)" : "Weight (kg)"}
                  </label>
                  <input
                    type="number"
                    min="30"
                    max="200"
                    value={weight}
                    onChange={(e) => setWeight(e.target.value)}
                    placeholder="60"
                    className="w-full px-4 py-3 rounded-xl border border-stone-200 bg-stone-50/50 focus:bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] transition-all"
                  />
                </div>
              </div>
            </div>
          )}

          {/* QUESTION 4: ADDRESS / REGION (OPTIONAL) */}
          {signupStep === 4 && (
            <div className="space-y-4">
              <div className="space-y-1">
                <div className="flex items-center justify-between">
                  <h3 className="text-lg font-black text-stone-900">
                    {language === "mm" ? "နေရပ်လိပ်စာနှင့် မြို့" : "Location & City"}
                  </h3>
                  <span className="text-[11px] font-bold px-2 py-0.5 rounded-md bg-stone-100 text-stone-500">
                    {language === "mm" ? "ရွေးချယ်ရန် (Optional)" : "Optional"}
                  </span>
                </div>
                <p className="text-xs text-stone-500">
                  {language === "mm"
                    ? "သင့်အနီးဆုံး စည်ပင်ဈေးများ၏ ဈေးနှုန်းများကို ပြသပေးရန် ဖြစ်ပါသည်"
                    : "Helps us display local wet market commodity prices accurate to your region"}
                </p>
              </div>

              <div className="space-y-1.5">
                <label className="text-xs font-bold text-stone-700 block">
                  {language === "mm" ? "မြို့နယ် / ဒေသ ရွေးချယ်ပါ" : "Select City"}
                </label>
                <select
                  value={selectedCity}
                  onChange={(e) => setSelectedCity(e.target.value as "Yangon" | "Mandalay")}
                  className="w-full px-4 py-3 rounded-xl border border-stone-200 bg-stone-50/50 focus:bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] transition-all"
                >
                  <option value="Yangon">Yangon / ရန်ကုန်မြို့ (၂၂ ဈေးနှုန်း အချက်အလက်)</option>
                  <option value="Mandalay">Mandalay / မန္တလေးမြို့ (သီရိမာလာဈေး အပါအဝင်)</option>
                </select>
              </div>

              <div className="space-y-1.5">
                <label className="text-xs font-bold text-stone-700 block">
                  {language === "mm" ? "မြို့နယ် သို့မဟုတ် လမ်းအမည်" : "Township / Street Address"}
                </label>
                <input
                  type="text"
                  value={address}
                  onChange={(e) => setAddress(e.target.value)}
                  placeholder={language === "mm" ? "ဥပမာ - ကမာရွတ်မြို့နယ်" : "e.g. Kamayut, Yangon"}
                  className="w-full px-4 py-3 rounded-xl border border-stone-200 bg-stone-50/50 focus:bg-white text-sm focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] transition-all"
                />
              </div>
            </div>
          )}

          {/* QUESTION 5: HOW MUCH TIME TO SPEND COOKING */}
          {signupStep === 5 && (
            <div className="space-y-4">
              <div className="space-y-1">
                <h3 className="text-lg font-black text-stone-900">
                  {language === "mm"
                    ? "ဟင်းချက်ရန် အချိန် မည်မျှ အသုံးပြုလိုပါသလဲ။"
                    : "How much time do you want to spend cooking?"}
                </h3>
                <p className="text-xs text-stone-500">
                  {language === "mm"
                    ? "သင့်အချိန်နှင့် ကိုက်ညီသော ဟင်းချက်နည်းများကို ဦးစားပေး ဖော်ပြပေးပါမည်"
                    : "We'll prioritize recipes matching your schedule and daily routine"}
                </p>
              </div>

              <div className="space-y-3">
                {[
                  {
                    id: "easy" as const,
                    tag: "🟢 Easy",
                    tag_mm: "🟢 လွယ်ကူမြန်ဆန်",
                    time: "≤ 25 mins",
                    time_mm: "၂၅ မိနစ်အတွင်း",
                    desc_en: "Quick stir-fries, fresh salads, simple soups & egg dishes",
                    desc_mm: "အမြန်ချက် အကြော်၊ အသုပ်၊ ဟင်းချိုနှင့် ကြက်ဥဟင်းများ",
                  },
                  {
                    id: "medium" as const,
                    tag: "🟡 Medium",
                    tag_mm: "🟡 အလယ်အလတ်",
                    time: "25 – 45 mins",
                    time_mm: "၂၅ မှ ၄၅ မိနစ်",
                    desc_en: "Standard Myanmar poultry, fish curries, and coconut noodles",
                    desc_mm: "ကြက်၊ ငါး ဆီပြန်ဟင်းများနှင့် အုန်းနို့ခေါက်ဆွဲများ",
                  },
                  {
                    id: "hard" as const,
                    tag: "🔴 Hard / Elaborate",
                    tag_mm: "🔴 အချိန်ယူချက်ရသော ဟင်းများ",
                    time: "45+ mins",
                    time_mm: "၄၅ မိနစ်ထက်ကျော်",
                    desc_en: "Slow-simmered beef, mutton curries, Danbauk biryani & rich broths",
                    desc_mm: "အမဲသား၊ ဆိတ်သားဆီပြန်၊ ဒံပေါက်နှင့် အချိန်ယူချက်ပြုတ်ရသော ဟင်းများ",
                  },
                  {
                    id: "any" as const,
                    tag: "⚪ Any Time",
                    tag_mm: "⚪ အချိန်မရွေး အဆင်ပြေသည်",
                    time: "All recipes",
                    time_mm: "ဟင်းလျာအားလုံး",
                    desc_en: "Show all dishes regardless of cooking duration",
                    desc_mm: "ချက်ပြုတ်ချိန် ကန့်သတ်ချက်မထားဘဲ အားလုံးကြည့်မည်",
                  },
                ].map((opt) => (
                  <label
                    key={opt.id}
                    onClick={() => setCookingTimePref(opt.id)}
                    className={`block p-4 rounded-2xl border-2 cursor-pointer transition-all ${
                      cookingTimePref === opt.id
                        ? "border-[var(--color-primary)] bg-[var(--color-muted)]/20 shadow-xs"
                        : "border-stone-200 bg-white hover:border-stone-300"
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2">
                        <input
                          type="radio"
                          name="cookingTime"
                          checked={cookingTimePref === opt.id}
                          onChange={() => setCookingTimePref(opt.id)}
                          className="accent-[var(--color-primary)] w-4 h-4"
                        />
                        <span className="font-extrabold text-sm text-stone-900">
                          {language === "mm" ? opt.tag_mm : opt.tag}
                        </span>
                      </div>
                      <span className="text-xs font-bold px-2 py-0.5 rounded-md bg-stone-100 text-stone-600">
                        {language === "mm" ? opt.time_mm : opt.time}
                      </span>
                    </div>
                    <p className="text-xs text-stone-500 mt-1 pl-6">
                      {language === "mm" ? opt.desc_mm : opt.desc_en}
                    </p>
                  </label>
                ))}
              </div>
            </div>
          )}

          {/* QUESTION 6: MEAL PREFERENCES */}
          {signupStep === 6 && (
            <div className="space-y-4">
              <div className="space-y-1">
                <h3 className="text-lg font-black text-stone-900">
                  {language === "mm"
                    ? "မည်သည့် အစားအစာအမျိုးအစားကို ပိုမိုနှစ်သက်ပါသလဲ။"
                    : "What are your meal preferences?"}
                </h3>
                <p className="text-xs text-stone-500">
                  {language === "mm"
                    ? "ပင်မစာမျက်နှာတွင် သင့်စိတ်ကြိုက် ဟင်းလျာများကို ဦးစားပေး အကြံပြုပေးပါမည်"
                    : "We'll feature your favorite dish categories on your personalized home feed"}
                </p>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                {mealPrefOptions.map((opt) => (
                  <button
                    key={opt.id}
                    type="button"
                    onClick={() => setMealPref(opt.id)}
                    className={`p-3.5 rounded-2xl border-2 text-left transition-all ${
                      mealPref === opt.id
                        ? "border-[var(--color-primary)] bg-[var(--color-muted)]/25 shadow-xs"
                        : "border-stone-200 bg-white hover:border-stone-300"
                    }`}
                  >
                    <div className="text-2xl mb-1.5">{opt.icon}</div>
                    <h4 className="font-extrabold text-xs sm:text-sm text-stone-900">
                      {language === "mm" ? opt.label_mm : opt.label_en}
                    </h4>
                    <p className="text-[11px] text-stone-500 line-clamp-1 mt-0.5">
                      {language === "mm" ? opt.desc_mm : opt.desc_en}
                    </p>
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* Navigation Controls: Back / Next / Finish */}
          <div className="flex items-center justify-between pt-4 border-t border-stone-100">
            {signupStep > 1 ? (
              <button
                type="button"
                onClick={handlePrevStep}
                className="px-5 py-2.5 rounded-xl text-xs sm:text-sm font-bold border border-stone-200 text-stone-700 hover:bg-stone-50 transition-all"
              >
                {language === "mm" ? "← ရှေ့သို့" : "← Back"}
              </button>
            ) : (
              <div />
            )}

            <button
              type="button"
              onClick={handleNextStep}
              className="px-6 py-2.5 rounded-xl text-white text-xs sm:text-sm font-extrabold shadow-md transition-all active:scale-98"
              style={{ backgroundColor: "var(--color-primary)" }}
            >
              {signupStep === 6
                ? language === "mm"
                  ? "အကောင့်ပြီးမြောက်မည် ✓"
                  : "Finish & Start Cooking ✓"
                : language === "mm"
                ? "ရှေ့သို့ဆက်သွားမည် →"
                : "Next →"}
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
