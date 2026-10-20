import { MyanmarCalendarInfo } from "@/types/theme";

/**
 * Modern Myanmar Lunisolar Astronomical Calculations
 * Based on Dr. Yan Naing Aye's algorithm (ceMmDateTime)
 * Verified for Myanmar Lunisolar Calendar rules, Metonic intercalary cycles, and Thingyan solar transitions.
 */

// Month names in English and Burmese
export const MYANMAR_MONTHS_EN: { [key: number]: string } = {
  0: "First Waso",
  1: "Tagu",
  2: "Kason",
  3: "Nayon",
  4: "Waso",
  5: "Wagaung",
  6: "Tawthalin",
  7: "Thadingyut",
  8: "Tazaungmon",
  9: "Nadaw",
  10: "Pyatho",
  11: "Tabodwe",
  12: "Tabaung",
  13: "Late Tagu",
  14: "Late Kason",
};

export const MYANMAR_MONTHS_MM: { [key: number]: string } = {
  0: "ပထမဝါဆို",
  1: "တန်ခူး",
  2: "ကဆုန်",
  3: "နယုန်",
  4: "ဝါဆို",
  5: "ဝါခေါင်",
  6: "တော်သလင်း",
  7: "သီတင်းကျွတ်",
  8: "တန်ဆောင်မုန်း",
  9: "နတ်တော်",
  10: "ပြာသို",
  11: "တပို့တွဲ",
  12: "တပေါင်း",
  13: "နှောင်းတန်ခူး",
  14: "နှောင်းကဆုန်",
};

// Burmese numerals converter
export function toBurmeseNumber(num: number | string): string {
  const burmeseDigits = ["၀", "၁", "၂", "၃", "၄", "၅", "၆", "၇", "၈", "၉"];
  return num
    .toString()
    .split("")
    .map((char) => {
      const n = parseInt(char, 10);
      return !isNaN(n) ? burmeseDigits[n] : char;
    })
    .join("");
}

// Julian date conversion
export function w2j(
  y: number,
  m: number,
  d: number,
  h = 12,
  n = 0,
  s = 0,
  ct = 1
): number {
  const a = Math.floor((14 - m) / 12);
  y = y + 4800 - a;
  m = m + 12 * a - 3;
  let jd = d + Math.floor((153 * m + 2) / 5) + 365 * y + Math.floor(y / 4);
  if (ct === 1) {
    jd = jd - Math.floor(y / 100) + Math.floor(y / 400) - 32045;
  } else if (ct === 2) {
    jd = jd - 32083;
  }
  const fraction = (h - 12) / 24 + n / 1440 + s / 86400;
  return jd + fraction;
}

export function j2w(jd: number) {
  const j = Math.floor(jd + 0.5) - 1721119;
  const y = Math.floor((4 * j - 1) / 146097);
  const j2 = 4 * j - 1 - 146097 * y;
  const d1 = Math.floor(j2 / 4);
  const j3 = Math.floor((4 * d1 + 3) / 1461);
  const d2 = 4 * d1 + 3 - 1461 * j3;
  const d3 = Math.floor((d2 + 4) / 4);
  const m1 = Math.floor((5 * d3 - 3) / 153);
  const d = 5 * d3 - 3 - 153 * m1;
  const day = Math.floor((d + 5) / 5);
  let year = 100 * y + j3;
  let month = m1 < 10 ? m1 + 3 : m1 - 9;
  if (month > 2) {
    // normal
  } else {
    year += 1;
  }
  return { y: year, m: month, d: day };
}

// Era constants
function getMyConst(my: number) {
  let EI = 3;
  let WO = -0.5;
  let NM = 8;
  let EW = 0;

  if (my >= 1312) {
    // 3rd Era (Modern era, after ME 1312 / 1950 AD)
    EI = 3;
    WO = -0.5;
    NM = 8;
    if (my === 1377) WO += 1; // 1377 full moon offset
    if (my === 1344 || my === 1345) EW = 1;
  } else if (my >= 1217) {
    EI = 2;
    WO = -1;
    NM = 4;
    if (my === 1234) WO += 1;
    if (my === 1261) WO -= 1;
    if (my === 1263 || my === 1264) EW = 1;
  } else {
    EI = 1.3;
    WO = -0.85;
    NM = -1;
  }

  return { EI, WO, NM, EW };
}

// Watat (intercalary month) check
export function cal_watat(my: number) {
  const SY = 1577917828.0 / 4320000.0; // solar year (365.2587565)
  const LM = 1577917828.0 / 53433336.0; // lunar month (29.53058795)
  const MO = 1954168.050623; // beginning of 0 ME for MMT
  const c = getMyConst(my);
  const TA = (SY / 12 - LM) * (12 - c.NM);
  let ed = (SY * (my + 3739)) % LM;
  if (ed < TA) ed += LM;
  const fm = Math.round(SY * my + MO - ed + 4.5 * LM + c.WO);
  let watat = 0;
  if (c.EI >= 2) {
    const TW = LM - (SY / 12 - LM) * c.NM;
    if (ed >= TW) watat = 1;
  } else {
    watat = Math.floor(((my * 7 + 2) % 19) / 12);
  }
  watat ^= c.EW;
  return { fm, watat };
}

// Year type calculation
export function cal_my(my: number) {
  let yd = 0;
  let y1: { fm: number; watat: number };
  let fm = 0;
  const y2 = cal_watat(my);
  let myt = y2.watat;
  do {
    yd++;
    y1 = cal_watat(my - yd);
  } while (y1.watat === 0 && yd < 3);

  if (myt) {
    const nd = (y2.fm - y1.fm) % 354;
    myt = Math.floor(nd / 31) + 1;
    fm = y2.fm;
  } else {
    fm = y1.fm + 354 * yd;
  }
  const tg1 = y1.fm + 354 * yd - 102;
  return { myt, tg1, fm };
}

// Julian day number to Myanmar date
export function j2m(jdn: number) {
  const roundedJdn = Math.round(jdn);
  const SY = 1577917828.0 / 4320000.0;
  const MO = 1954168.050623;
  const my = Math.floor((roundedJdn - 0.5 - MO) / SY);
  const yo = cal_my(my);
  let dd = roundedJdn - yo.tg1 + 1;
  const b = Math.floor(yo.myt / 2);
  const c = Math.floor(1 / (yo.myt + 1));
  const myl = 354 + (1 - c) * 30 + b;
  const mmt = Math.floor((dd - 1) / myl);
  dd -= mmt * myl;
  const a = Math.floor((dd + 423) / 512);
  let mm = Math.floor((dd - b * a + c * a * 30 + 29.26) / 29.544);
  const e = Math.floor((mm + 12) / 16);
  const f = Math.floor((mm + 11) / 16);
  const md = dd - Math.floor(29.544 * mm - 29.26) - b * e + c * f * 30;
  mm += f * 3 - e * 4 + 12 * mmt;
  return { myt: yo.myt, my, mm, md };
}

// Moon phase (0=waxing, 1=full moon, 2=waning, 3=new moon)
export function cal_mp(md: number, mm: number, myt: number): 0 | 1 | 2 | 3 {
  const mml = cal_mml(mm, myt);
  const mp = Math.floor((md + 1) / 16) + Math.floor(md / 16) + Math.floor(md / mml);
  return Math.min(3, Math.max(0, mp)) as 0 | 1 | 2 | 3;
}

// Month length
export function cal_mml(mm: number, myt: number): number {
  let mml = 30 - (mm % 2);
  if (mm === 3) mml += Math.floor(myt / 2);
  return mml;
}

// Fortnight day (1-15)
export function cal_mf(md: number): number {
  return md - 15 * Math.floor(md / 16);
}

// Sabbath and sabbath eve check
export function isSabbath(md: number, mm: number, myt: number): { sabbath: boolean; eve: boolean } {
  const mml = cal_mml(mm, myt);
  const sabbath = md === 8 || md === 15 || md === 23 || md === mml;
  const eve = md === 7 || md === 14 || md === 22 || md === mml - 1;
  return { sabbath, eve };
}

// Thingyan calculation for a given Myanmar Year
export function getThingyanDays(my: number, mmt = 0) {
  const SY = 1577917828.0 / 4320000.0;
  const MO = 1954168.050623;
  const SE3 = 1312;
  const ja = SY * (my + mmt) + MO;
  const jk = my >= SE3 ? ja - 2.169918982 : ja - 2.1675;
  const akn = Math.round(jk); // Akya day
  const atn = Math.round(ja); // Atat day

  return {
    akyo: akn - 1,
    akya: akn,
    akyatStart: akn + 1,
    akyatEnd: atn - 1,
    atat: atn,
    newYear: atn + 1,
  };
}

/**
 * Normalizes Myanmar month number to standard 1-12 cycle:
 * 13 (Late Tagu) -> 1 (Tagu)
 * 14 (Late Kason) -> 2 (Kason)
 * 0 (First Waso) -> 4 (Waso season)
 */
export function normalizeMyanmarMonth(mm: number): number {
  if (mm === 13) return 1;
  if (mm === 14) return 2;
  if (mm === 0) return 4;
  return mm;
}

/**
 * Resolves current Myanmar calendar date in Myanmar time zone (Asia/Yangon: UTC +06:30).
 */
export function getMyanmarCalendarInfo(inputDate?: Date | string | null): MyanmarCalendarInfo {
  // Use Asia/Yangon time
  let date: Date;
  if (inputDate instanceof Date) {
    date = inputDate;
  } else if (typeof inputDate === "string" && inputDate.trim() !== "") {
    date = new Date(inputDate);
  } else {
    // Stable baseline date for SSR/prerender to prevent Next.js hydration mismatch
    date = new Date("2026-10-20T12:00:00Z");
  }

  // Adjust for Myanmar timezone (+06:30)
  // If running in browser or server, compute UTC + 6.5 hours
  const utcMillis = date.getTime() + date.getTimezoneOffset() * 60000;
  const mmtMillis = utcMillis + 6.5 * 3600000;
  const mmtDate = new Date(mmtMillis);

  const year = mmtDate.getFullYear();
  const month = mmtDate.getMonth() + 1;
  const day = mmtDate.getDate();
  const hour = mmtDate.getHours();
  const minute = mmtDate.getMinutes();

  const jd = w2j(year, month, day, hour, minute, 0, 1);
  const jdn = Math.round(jd);

  const m = j2m(jdn);
  const normalizedMonth = normalizeMyanmarMonth(m.mm);
  const mp = cal_mp(m.md, m.mm, m.myt);
  const mf = cal_mf(m.md);
  const sabbathInfo = isSabbath(m.md, m.mm, m.myt);

  const moonPhaseMap: { [key: number]: "Waxing" | "Full Moon" | "Waning" | "New Moon" } = {
    0: "Waxing",
    1: "Full Moon",
    2: "Waning",
    3: "New Moon",
  };

  const moonPhaseMmMap: { [key: number]: "လဆန်း" | "လပြည့်" | "လဆုတ်" | "လကွယ်" } = {
    0: "လဆန်း",
    1: "လပြည့်",
    2: "လဆုတ်",
    3: "လကွယ်",
  };

  const holidays: string[] = [];

  // Check Thingyan
  const mmtMonthType = Math.floor(m.mm / 13);
  const ty = getThingyanDays(m.my, mmtMonthType);
  let activeFestival: MyanmarCalendarInfo["activeFestival"] = null;

  if (jdn >= ty.akyo && jdn <= ty.newYear) {
    if (jdn === ty.akyo) {
      holidays.push("Thingyan Akyo (အကြိုနေ့)");
    } else if (jdn === ty.akya) {
      holidays.push("Thingyan Akya (အကျနေ့)");
    } else if (jdn >= ty.akyatStart && jdn <= ty.akyatEnd) {
      holidays.push("Thingyan Akyat (အကြတ်နေ့)");
    } else if (jdn === ty.atat) {
      holidays.push("Thingyan Atat (အတက်နေ့)");
    } else if (jdn === ty.newYear) {
      holidays.push("Myanmar New Year's Day (မြန်မာနှစ်ဆန်းတစ်ရက်နေ့)");
    }

    activeFestival = {
      id: "fest-thingyan",
      nameMm: "မဟာသင်္ကြန် ရေကစားပွဲတော်နှင့် နှစ်သစ်မင်္ဂလာ",
      nameEn: "Maha Thingyan Water Festival & New Year",
      descriptionMm: "အေးမြကြည်လင်သော မဟာသင်္ကြန်ရေစင်ဖြင့် အညစ်အကြေးများကို ဆေးကြော၍ နှစ်သစ်ကို ကြိုဆိုခြင်း။",
      descriptionEn: "Welcoming the auspicious Myanmar New Year with sacred water splashing and cultural merit.",
    };
  }

  // Check Kason Full Moon (Buddha Day / Nyaung Yay Thun)
  if (normalizedMonth === 2 && mp === 1) {
    holidays.push("Kason Full Moon Buddha Day (ကဆုန်လပြည့် ဗုဒ္ဓနေ့)");
    activeFestival = {
      id: "fest-kason-nyaung-yay",
      nameMm: "ကဆုန်လပြည့် ဗုဒ္ဓနေ့ ညောင်ရေသွန်းပွဲတော်",
      nameEn: "Kason Full Moon Buddha Day & Bo Tree Watering Festival",
      descriptionMm: "ဗုဒ္ဓမြတ်စွာဘုရား၏ ဖွား၊ ပွင့်၊ ဟော၊ စံ နေ့မြတ်တွင် ဗောဓိညောင်ပင်အား ရေစင်သွန်းလောင်း ပူဇော်ခြင်း။",
      descriptionEn: "Commemorating Buddha's birth, enlightenment, and parinirvana with devotional water blessing on Bodhi trees.",
    };
  }

  // Check Waso Full Moon (Dhammacakka Day / Robe Offering)
  if (normalizedMonth === 4 && mp === 1) {
    holidays.push("Waso Full Moon Dhammacakka Day (ဝါဆိုလပြည့် ဓမ္မစကြာနေ့)");
    activeFestival = {
      id: "fest-waso-lent",
      nameMm: "ဝါဆိုလပြည့် ဓမ္မစကြာနေ့ ဝါဆိုသင်္ကန်းကပ်လှူပွဲ",
      nameEn: "Waso Robe Offering & Dhammacakka Day",
      descriptionMm: "တရားဦးဓမ္မစကြာ ဟောကြားတော်မူသော နေ့မြတ်တွင် သံဃာတော်များအား ဝါဆိုသင်္ကန်း ဆက်ကပ်လှူဒါန်းခြင်း။",
      descriptionEn: "Offering consecrated Waso robes to monks at the commencement of the three-month Buddhist Lent.",
    };
  }

  // Check Thadingyut Festival of Lights (14th waxing, full moon 15, 1st waning 16)
  if (normalizedMonth === 7 && (m.md === 14 || m.md === 15 || m.md === 16)) {
    if (m.md === 14) holidays.push("Thadingyut Eve (အဖိတ်နေ့)");
    if (m.md === 15) holidays.push("Thadingyut Full Moon (သီတင်းကျွတ်လပြည့်နေ့)");
    if (m.md === 16) holidays.push("Thadingyut Day After (ဝါကျွတ်အခါတော်)");

    activeFestival = {
      id: "fest-thadingyut-lights",
      nameMm: "သီတင်းကျွတ် မီးထွန်းပွဲတော်နှင့် အဘိဓမ္မာအခါတော်နေ့",
      nameEn: "Thadingyut Festival of Lights & Abhidhamma Day",
      descriptionMm: "တာဝတိံသာနတ်ပြည်မှ သက်ဆင်းတော်မူသော မြတ်စွာဘုရားအား ဆီမီးရောင်စုံ ထွန်းညှိ၍ ဂါရဝပြု ကြိုဆိုသော မင်္ဂလာပွဲတော်။",
      descriptionEn: "Celebrating the end of Buddhist Lent with millions of glowing lanterns, candles, and paying respects to elders.",
    };
  }

  // Check Tazaungdaing Festival & Hot-Air Balloons (Tazaungmon 14th waxing, full moon 15)
  if (normalizedMonth === 8 && (m.md === 14 || m.md === 15)) {
    holidays.push("Tazaungdaing Festival (တန်ဆောင်တိုင်ပွဲတော်)");
    activeFestival = {
      id: "fest-tazaungdaing-balloons",
      nameMm: "တန်ဆောင်တိုင် ပွဲတော်နှင့် တောင်ကြီး မီးပုံးပျံပွဲတော်",
      nameEn: "Tazaungdaing Festival & Taunggyi Hot-Air Balloon Festival",
      descriptionMm: "စူဠာမဏိစေတီတော်ကို ရည်မှန်း၍ ကောင်းကင်ယံသို့ မီးပုံးပျံကြီးများ လွှတ်တင်ပူဇော်ပြီး မသိုးသင်္ကန်း ရက်ခတ်လှူဒါန်းသော ပွဲတော်။",
      descriptionEn: "Spectacular nocturnal hot-air balloon launches in Taunggyi and all-night Matho robe-weaving competitions.",
    };
  }

  // Check Tabodwe Htamane Feast (Tabodwe 14th waxing, full moon 15, 16)
  if (normalizedMonth === 11 && (m.md === 14 || m.md === 15 || m.md === 16)) {
    holidays.push("Tabodwe Htamane Feast (တပို့တွဲ ထမနဲပွဲ)");
    activeFestival = {
      id: "fest-tabodwe-htamane",
      nameMm: "တပို့တွဲလပြည့် မြန်မာ့ရိုးရာ ထမနဲထိုးပွဲတော်",
      nameEn: "Tabodwe Traditional Htamane Harvest Feast",
      descriptionMm: "ကောက်ညှင်း၊ နှမ်း၊ မြေပဲ၊ အုန်းသီးတို့ဖြင့် စုပေါင်းထိုးယောင်း၍ ဘုရားရှင်နှင့် သံဃာတော်များအား ဆွမ်းဦးကပ်လှူသော ပွဲတော်။",
      descriptionEn: "Communal stirring of sticky rice, sesame, and toasted peanuts in giant iron cauldrons for harvest thanksgiving.",
    };
  }

  const monthNameEn = MYANMAR_MONTHS_EN[m.mm] || "Tagu";
  const monthNameMm = MYANMAR_MONTHS_MM[m.mm] || "တန်ခူး";

  const yearTypeMap: { [key: number]: "common" | "little_watat" | "big_watat" } = {
    0: "common",
    1: "little_watat",
    2: "big_watat",
  };

  const formattedMm = `မြန်မာသက္ကရာဇ် ${toBurmeseNumber(m.my)} ခုနှစ်၊ ${monthNameMm}${moonPhaseMmMap[mp]} ${toBurmeseNumber(mf)} ရက်`;
  const formattedEn = `ME ${m.my}, ${monthNameEn} ${moonPhaseMap[mp]} ${mf}`;
  const gregorianDateStr = `${year}-${month.toString().padStart(2, "0")}-${day.toString().padStart(2, "0")}`;

  return {
    myanmarYear: m.my,
    sasanaYear: m.my + 1182,
    myanmarMonth: m.mm,
    normalizedMonth,
    monthDay: m.md,
    fortnightDay: mf,
    moonPhase: moonPhaseMap[mp],
    moonPhaseMm: moonPhaseMmMap[mp],
    monthNameEn,
    monthNameMm,
    yearType: yearTypeMap[m.myt] || "common",
    isWatatYear: m.myt > 0,
    isSabbathDay: sabbathInfo.sabbath,
    isSabbathEve: sabbathInfo.eve,
    holidays,
    activeFestival,
    gregorianDateStr,
    formattedMm,
    formattedEn,
  };
}
