import pypdfium2 as pdfium
import os
from PIL import Image

pdf_filename = [f for f in os.listdir('.') if f.endswith('.pdf')][0]
pdf = pdfium.PdfDocument(pdf_filename)

for p_num in [89, 90]: # PDF pages 90 and 91 (0-indexed 89, 90)
    im = pdf[p_num].render(scale=1.5).to_pil()
    w, h = im.size
    im.crop((0, 0, int(w*0.52), h)).save(f"recipe_crops/p{p_num+1}_left.png")
    im.crop((int(w*0.48), 0, w, h)).save(f"recipe_crops/p{p_num+1}_right.png")

print("Rendered PDF pages 90 and 91.")
