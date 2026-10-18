import pypdfium2 as pdfium
import os
from PIL import Image

pdf_filename = [f for f in os.listdir('.') if f.endswith('.pdf')][0]
pdf = pdfium.PdfDocument(pdf_filename)

# Let's sample every 2 pages from 80 to 104
for p_idx in range(80, 104, 2):
    page = pdf[p_idx]
    image = page.render(scale=1.0).to_pil()
    w, h = image.size
    # crop top 20%
    top = image.crop((0, 0, w, int(h * 0.25)))
    top.save(f"recipe_crops/header_p{p_idx+1:03d}.png")
    print(f"Rendered header for PDF p.{p_idx+1}")

print("Done sampling headers.")
