import pypdfium2 as pdfium
import os
from PIL import Image

pdf_filename = [f for f in os.listdir('.') if f.endswith('.pdf')][0]
pdf = pdfium.PdfDocument(pdf_filename)
os.makedirs("recipe_crops", exist_ok=True)

# PDF pages 74 to 91 (0-indexed 73 to 90)
for p_num in range(73, 91):
    pdf_page_idx = p_num + 1
    im = pdf[p_num].render(scale=1.5).to_pil()
    w, h = im.size
    im.crop((0, 0, int(w * 0.52), h)).save(f"recipe_crops/p{pdf_page_idx:03d}_left.png")
    im.crop((int(w * 0.48), 0, w, h)).save(f"recipe_crops/p{pdf_page_idx:03d}_right.png")
    print(f"Rendered PDF page {pdf_page_idx}")

print("Batch 8 pages rendered.")
