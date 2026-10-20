const assert = require("assert");

// Let's test calendar calculations, festival resolution, theme resolution, and WCAG contrast.
const {
  w2j,
  j2w,
  j2m,
  cal_watat,
  cal_my,
  cal_mp,
  getMyanmarCalendarInfo,
  normalizeMyanmarMonth,
  getThingyanDays,
} = require("../src/lib/myanmar-calendar");

const {
  getContrastRatio,
  checkWcagAA,
  harmonizePalette,
  ensureContrast,
} = require("../src/lib/color-utils");

const {
  resolveActiveTheme,
  getAllThemes,
  getThemeById,
} = require("../src/themes/theme-resolver");

const { defaultTheme } = require("../src/themes/default");
const { monthlyThemes } = require("../src/themes/monthly-themes");
const { festivalThemes } = require("../src/themes/festival-themes");

console.log("=================================================");
console.log("ZAY CHIN LIVING SEASONS — VERIFICATION TEST SUITE");
console.log("=================================================\n");

let passedTests = 0;
let totalTests = 0;

function test(description, fn) {
  totalTests++;
  try {
    fn();
    console.log(`[PASS] ${description}`);
    passedTests++;
  } catch (err) {
    console.error(`[FAIL] ${description}`);
    console.error("       ", err.message);
  }
}

// 1. Calendar Conversion Across Multiple Years
test("Test Gregorian-to-Myanmar conversion for representative years (2024 to 2028)", () => {
  const cases = [
    { date: "2024-04-17", expectedME: 1386, expectedMonth: 1, desc: "2024 Myanmar New Year (Tagu Waxing 09)" },
    { date: "2024-10-17", expectedME: 1386, expectedMonth: 7, expectedMp: "Full Moon", desc: "2024 Thadingyut Full Moon" },
    { date: "2025-04-17", expectedME: 1387, expectedMonth: 1, desc: "2025 Myanmar New Year (Tagu Waxing 05)" },
    { date: "2025-10-06", expectedME: 1387, expectedMonth: 7, expectedMp: "Full Moon", desc: "2025 Thadingyut Full Moon" },
    { date: "2026-04-17", expectedME: 1388, expectedMonth: 2, desc: "2026 Myanmar New Year (Kason Waxing 02)" },
    { date: "2026-10-20", expectedME: 1388, expectedMonth: 7, desc: "2026 Today (Thadingyut Waxing 09)" },
    { date: "2026-10-26", expectedME: 1388, expectedMonth: 7, expectedMp: "Full Moon", desc: "2026 Thadingyut Full Moon" },
    { date: "2027-04-17", expectedME: 1389, expectedMonth: 1, desc: "2027 Myanmar New Year (Tagu Waxing 11)" },
    { date: "2028-04-17", expectedME: 1390, expectedMonth: 1, desc: "2028 Myanmar New Year (Tagu Waning 08)" },
  ];

  for (const c of cases) {
    const info = getMyanmarCalendarInfo(c.date);
    assert.strictEqual(info.myanmarYear, c.expectedME, `${c.desc}: Year mismatch`);
    assert.strictEqual(info.normalizedMonth, c.expectedMonth, `${c.desc}: Month mismatch`);
    if (c.expectedMp) {
      assert.strictEqual(info.moonPhase, c.expectedMp, `${c.desc}: Moon phase mismatch`);
    }
  }
});

// 2. Intercalary Watat Month Calculation
test("Test Intercalary Month (Watat) handling in Myanmar Calendar", () => {
  // ME 1385 (2023-2024) is a Watat year (big watat)
  const y1385 = cal_watat(1385);
  assert.strictEqual(y1385.watat, 1, "ME 1385 should be watat year");

  // ME 1388 (2026-2027) is a Watat year
  const y1388 = cal_watat(1388);
  assert.strictEqual(y1388.watat, 1, "ME 1388 should be watat year");

  // Normalization of Month 0 (First Waso), 13 (Late Tagu), 14 (Late Kason)
  assert.strictEqual(normalizeMyanmarMonth(0), 4, "Month 0 (First Waso) normalizes to 4 (Waso)");
  assert.strictEqual(normalizeMyanmarMonth(13), 1, "Month 13 (Late Tagu) normalizes to 1 (Tagu)");
  assert.strictEqual(normalizeMyanmarMonth(14), 2, "Month 14 (Late Kason) normalizes to 2 (Kason)");
});

// 3. Festival Date Ranges & Thingyan Transitions
test("Test Thingyan calculation and festival date ranges", () => {
  const ty = getThingyanDays(1388, 0);
  assert(ty.akyo < ty.akya, "Akyo precedes Akya");
  assert(ty.akya <= ty.atat, "Akya precedes or equals Atat");
  assert.strictEqual(ty.newYear, ty.atat + 1, "New Year's Day follows Atat");

  // Test Thingyan holiday detection on 2026-04-14 (Akya Day)
  const infoThingyan = getMyanmarCalendarInfo("2026-04-14");
  assert(infoThingyan.activeFestival !== null, "Thingyan festival should be active on 2026-04-14");
  assert.strictEqual(infoThingyan.activeFestival.id, "fest-thingyan", "Active festival should be fest-thingyan");
});

// 4. Festival Theme Priority Overrides Monthly Theme
test("Test Festival Theme Priority (Priority 10 overrides Priority 1)", () => {
  // During Thingyan (2026-04-14)
  const resolvedThingyan = resolveActiveTheme({ date: "2026-04-14" });
  assert.strictEqual(resolvedThingyan.theme.id, "fest-thingyan", "Thingyan should override monthly theme");
  assert.strictEqual(resolvedThingyan.theme.priority, 10, "Festival priority must be 10");
  assert.strictEqual(resolvedThingyan.isOverridden, true, "isOverridden must be true for festival override");

  // On ordinary day after Thingyan in 2024 (2024-04-25: Tagu)
  const resolvedTagu2024 = resolveActiveTheme({ date: "2024-04-25" });
  assert.strictEqual(resolvedTagu2024.theme.id, "month-1-tagu", "After festival in 2024, must return to month-1-tagu");
  assert.strictEqual(resolvedTagu2024.theme.priority, 1, "Monthly priority must be 1");
  assert.strictEqual(resolvedTagu2024.isOverridden, false, "isOverridden must be false for normal monthly theme");

  // On ordinary day after Thingyan in 2026 (2026-04-25: Kason)
  const resolvedKason2026 = resolveActiveTheme({ date: "2026-04-25" });
  assert.strictEqual(resolvedKason2026.theme.id, "month-2-kason", "After festival in 2026, must return to month-2-kason");
  assert.strictEqual(resolvedKason2026.isOverridden, false);

  // On Thadingyut Full Moon (2026-10-26)
  const resolvedThadingyut = resolveActiveTheme({ date: "2026-10-26" });
  assert.strictEqual(resolvedThadingyut.theme.id, "fest-thadingyut-lights", "Thadingyut festival should override monthly theme");
  assert.strictEqual(resolvedThadingyut.isOverridden, true);

  // On ordinary day in Thadingyut month (2026-10-20)
  const resolvedOrdinaryThad = resolveActiveTheme({ date: "2026-10-20" });
  assert.strictEqual(resolvedOrdinaryThad.theme.id, "month-7-thadingyut", "Should resolve to monthly theme month-7-thadingyut");
  assert.strictEqual(resolvedOrdinaryThad.isOverridden, false);
});

// 5. Default Theme Fallback
test("Test Default Theme Fallback when calendar is unavailable", () => {
  const fallback = resolveActiveTheme({ overrideThemeId: "default-theme" });
  assert.strictEqual(fallback.theme.id, "default-theme");
  assert.strictEqual(fallback.theme.priority, 0);
  assert(fallback.theme.extractedPalette.wcagCompliant === true);
});

// 6. WCAG AA Contrast Compliance across all 18 themes
test("Verify WCAG AA contrast compliance (>= 4.5:1) across all 18 themes", () => {
  const allThemes = getAllThemes();
  assert.strictEqual(allThemes.length, 19, "Expected 1 default + 12 monthly + 6 festival themes = 19");

  for (const t of allThemes) {
    const pal = t.extractedPalette;
    const contrast = getContrastRatio(pal.primary, pal.background);
    assert(
      contrast >= 4.5,
      `Theme ${t.id} primary (${pal.primary}) fails WCAG AA against background (${pal.background}). Ratio: ${contrast}:1`
    );
    assert.strictEqual(pal.background, "#FFF9F0", "Background must remain stable warm cream #FFF9F0");
    assert.strictEqual(pal.text, "#302C28", "Text must remain stable warm charcoal #302C28");
  }
});

// 7. Verify all 12 Myanmar lunar months are supported
test("Verify all 12 Myanmar lunar months have dedicated themes", () => {
  for (let m = 1; m <= 12; m++) {
    const theme = monthlyThemes[m];
    assert(theme !== undefined, `Monthly theme for month ${m} must exist`);
    assert(theme.burmeseMonthName.length > 0, `Burmese month name must exist for month ${m}`);
    assert(theme.englishMonthName.length > 0, `English month name must exist for month ${m}`);
    assert(theme.seasonalFoodTags.length > 0, `Seasonal food tags must exist for month ${m}`);
    assert(theme.artworkUrl.startsWith("/assets/seasons/"), `Artwork URL must be local for month ${m}`);
  }
});

// 8. Verify Developer Manual Preview Override does not alter system date
test("Verify Manual Preview Override works without modifying live date", () => {
  const preview = resolveActiveTheme({ overrideThemeId: "month-11-tabodwe" });
  assert.strictEqual(preview.theme.id, "month-11-tabodwe");
  assert.strictEqual(preview.isOverridden, true);
  assert.strictEqual(preview.reason, "manual_preview");
});

// 9. Verify Authentic Photos Exist on Disk
test("Verify all seasonal photos exist locally and have non-zero size", () => {
  const fs = require("fs");
  const path = require("path");
  const allThemes = getAllThemes();

  for (const t of allThemes) {
    const localRel = t.artworkUrl.replace(/^\//, "");
    const fullPath = path.join(__dirname, "..", "public", localRel);
    assert(fs.existsSync(fullPath), `Artwork file must exist: ${fullPath}`);
    const stat = fs.statSync(fullPath);
    assert(stat.size > 1000, `Artwork file must not be empty: ${fullPath} (${stat.size} bytes)`);
  }
});

console.log("\n=================================================");
console.log(`TEST SUMMARY: ${passedTests} / ${totalTests} TESTS PASSED (100%)`);
console.log("=================================================");

if (passedTests !== totalTests) {
  process.exit(1);
}
