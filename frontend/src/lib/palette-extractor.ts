import { ThemePalette } from "@/types/theme";
import { rgbToHex, harmonizePalette } from "./color-utils";

/**
 * Extracts a palette from an Image element using an offscreen Canvas.
 * Used for developer preview of custom or uploaded artworks.
 */
export async function extractPaletteFromImage(
  imageSrc: string
): Promise<ThemePalette> {
  return new Promise((resolve, reject) => {
    if (typeof window === "undefined") {
      // Fallback for SSR
      resolve({
        primary: "#526C4E",
        primaryForeground: "#FFFFFF",
        accent: "#D7A15A",
        background: "#FFF9F0",
        surface: "#FFFFFF",
        text: "#302C28",
        muted: "#F1E9DA",
        border: "#E8DED0",
        contrastWithBg: 6.8,
        wcagCompliant: true,
      });
      return;
    }

    const img = new Image();
    img.crossOrigin = "anonymous";
    img.src = imageSrc;

    img.onload = () => {
      try {
        const canvas = document.createElement("canvas");
        const ctx = canvas.getContext("2d");
        if (!ctx) {
          throw new Error("Could not create canvas 2d context");
        }

        // Downscale to 64x64 for fast and smooth sampling
        const width = 64;
        const height = 64;
        canvas.width = width;
        canvas.height = height;
        ctx.drawImage(img, 0, 0, width, height);

        const imgData = ctx.getImageData(0, 0, width, height).data;
        const colorCounts: { [hex: string]: number } = {};

        // Sample every 4th pixel for speed
        for (let i = 0; i < imgData.length; i += 16) {
          const r = Math.round(imgData[i] / 24) * 24;
          const g = Math.round(imgData[i + 1] / 24) * 24;
          const b = Math.round(imgData[i + 2] / 24) * 24;
          const a = imgData[i + 3];

          // Skip transparent or near-black/near-white pixels
          if (a < 128) continue;
          const lum = 0.2126 * r + 0.7152 * g + 0.0722 * b;
          if (lum < 20 || lum > 240) continue;

          const hex = rgbToHex(r, g, b);
          colorCounts[hex] = (colorCounts[hex] || 0) + 1;
        }

        const sorted = Object.entries(colorCounts).sort((a, b) => b[1] - a[1]);

        let candidatePrimary = sorted[0]?.[0] || "#526C4E";
        let candidateAccent = sorted[1]?.[0] || "#D7A15A";

        // Find an accent that differs sufficiently from primary
        for (let i = 1; i < sorted.length; i++) {
          const hex = sorted[i][0];
          if (hex !== candidatePrimary) {
            candidateAccent = hex;
            break;
          }
        }

        const palette = harmonizePalette(candidatePrimary, candidateAccent, "#FFF9F0");
        resolve(palette);
      } catch (err) {
        console.warn("Client palette extraction fallback used:", err);
        resolve({
          primary: "#526C4E",
          primaryForeground: "#FFFFFF",
          accent: "#D7A15A",
          background: "#FFF9F0",
          surface: "#FFFFFF",
          text: "#302C28",
          muted: "#F1E9DA",
          border: "#E8DED0",
          contrastWithBg: 6.8,
          wcagCompliant: true,
        });
      }
    };

    img.onerror = () => {
      resolve({
        primary: "#526C4E",
        primaryForeground: "#FFFFFF",
        accent: "#D7A15A",
        background: "#FFF9F0",
        surface: "#FFFFFF",
        text: "#302C28",
        muted: "#F1E9DA",
        border: "#E8DED0",
        contrastWithBg: 6.8,
        wcagCompliant: true,
      });
    };
  });
}
