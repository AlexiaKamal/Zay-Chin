import { ThemePalette } from "@/types/theme";

export interface RGB {
  r: number;
  g: number;
  b: number;
}

export function hexToRgb(hex: string): RGB {
  const clean = hex.replace("#", "").trim();
  if (clean.length === 3) {
    return {
      r: parseInt(clean[0] + clean[0], 16),
      g: parseInt(clean[1] + clean[1], 16),
      b: parseInt(clean[2] + clean[2], 16),
    };
  }
  return {
    r: parseInt(clean.substring(0, 2), 16) || 0,
    g: parseInt(clean.substring(2, 4), 16) || 0,
    b: parseInt(clean.substring(4, 6), 16) || 0,
  };
}

export function rgbToHex(r: number, g: number, b: number): string {
  const clamp = (v: number) => Math.min(255, Math.max(0, Math.round(v)));
  const toHex = (v: number) => clamp(v).toString(16).padStart(2, "0").toUpperCase();
  return `#${toHex(r)}${toHex(g)}${toHex(b)}`;
}

/**
 * Calculates WCAG 2.1 relative luminance for a color.
 * Formula: 0.2126 * R + 0.7152 * G + 0.0722 * B
 */
export function getRelativeLuminance(hex: string): number {
  const { r, g, b } = hexToRgb(hex);
  const srgb = [r / 255, g / 255, b / 255].map((val) => {
    return val <= 0.03928 ? val / 12.92 : Math.pow((val + 0.055) / 1.055, 2.4);
  });
  return 0.2126 * srgb[0] + 0.7152 * srgb[1] + 0.0722 * srgb[2];
}

/**
 * Calculates contrast ratio between two hex colors.
 * Formula: (Lighter + 0.05) / (Darker + 0.05)
 */
export function getContrastRatio(hex1: string, hex2: string): number {
  const lum1 = getRelativeLuminance(hex1);
  const lum2 = getRelativeLuminance(hex2);
  const lighter = Math.max(lum1, lum2);
  const darker = Math.min(lum1, lum2);
  const ratio = (lighter + 0.05) / (darker + 0.05);
  return Math.round(ratio * 100) / 100;
}

/**
 * Checks if color pair satisfies WCAG AA (>= 4.5:1 for normal text, >= 3:1 for large text).
 */
export function checkWcagAA(foreground: string, background: string, isLargeText = false): boolean {
  const ratio = getContrastRatio(foreground, background);
  return isLargeText ? ratio >= 3.0 : ratio >= 4.5;
}

/**
 * Adjusts color to guarantee WCAG compliance against a given background.
 * Darkens color if background is light, or lightens if background is dark.
 */
export function ensureContrast(color: string, background: string, targetRatio = 4.5): string {
  let currentRatio = getContrastRatio(color, background);
  if (currentRatio >= targetRatio) return color;

  const bgLum = getRelativeLuminance(background);
  let rgb = hexToRgb(color);
  const shouldDarken = bgLum > 0.5;

  let attempts = 0;
  while (currentRatio < targetRatio && attempts < 40) {
    attempts++;
    if (shouldDarken) {
      rgb = {
        r: Math.max(0, Math.round(rgb.r * 0.92)),
        g: Math.max(0, Math.round(rgb.g * 0.92)),
        b: Math.max(0, Math.round(rgb.b * 0.92)),
      };
    } else {
      rgb = {
        r: Math.min(255, Math.round(rgb.r * 1.08 + 10)),
        g: Math.min(255, Math.round(rgb.g * 1.08 + 10)),
        b: Math.min(255, Math.round(rgb.b * 1.08 + 10)),
      };
    }
    const candidate = rgbToHex(rgb.r, rgb.g, rgb.b);
    currentRatio = getContrastRatio(candidate, background);
    if (currentRatio >= targetRatio) {
      return candidate;
    }
  }

  return shouldDarken ? "#1F2937" : "#F9FAFB";
}

/**
 * Harmonizes an extracted primary and accent with Zay Chin's permanent warm neutral base.
 */
export function harmonizePalette(
  primaryInput: string,
  accentInput: string,
  backgroundBase = "#FFF9F0"
): ThemePalette {
  const primary = ensureContrast(primaryInput, backgroundBase, 4.5);
  const text = "#302C28"; // Permanent stable warm dark text
  const surface = "#FFFFFF";

  const accentRgb = hexToRgb(accentInput);

  // Soft muted tint derived from accent
  const muted = rgbToHex(
    255 * 0.88 + accentRgb.r * 0.12,
    249 * 0.88 + accentRgb.g * 0.12,
    240 * 0.88 + accentRgb.b * 0.12
  );

  // Subtle border tinted with accent
  const border = rgbToHex(
    232 * 0.82 + accentRgb.r * 0.18,
    222 * 0.82 + accentRgb.g * 0.18,
    208 * 0.82 + accentRgb.b * 0.18
  );

  const contrast = getContrastRatio(primary, backgroundBase);

  return {
    primary,
    primaryForeground: "#FFFFFF",
    accent: accentInput,
    background: backgroundBase,
    surface,
    text,
    muted,
    border,
    contrastWithBg: contrast,
    wcagCompliant: contrast >= 4.5,
  };
}

/**
 * Applies theme CSS variables to document :root with gentle CSS transitions.
 */
export function applyThemeVariables(palette: ThemePalette): void {
  if (typeof document === "undefined") return;

  const root = document.documentElement;
  root.style.setProperty("--color-primary", palette.primary);
  root.style.setProperty("--color-primary-foreground", palette.primaryForeground);
  root.style.setProperty("--color-accent", palette.accent);
  root.style.setProperty("--color-background", palette.background);
  root.style.setProperty("--color-surface", palette.surface);
  root.style.setProperty("--color-text", palette.text);
  root.style.setProperty("--color-muted", palette.muted);
  root.style.setProperty("--color-border", palette.border);
}
