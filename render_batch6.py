# -*- coding: utf-8 -*-
import pypdfium2 as pdfium
import os
from PIL import Image

pdf_filename = [f for f in os.listdir('.') if f.endswith('.pdf')][0]
pdf = pdfium.PdfDocument(pdf_filename)

# PDF pages 60 to 65 (0-indexed: 59 to 64)
# Printed pages 108 to 117
for p_num in range(59, 65):
    im = pdf[p_num].render(scale=1.5).to_pil()
    im.save(f"page_images/page_{p_num+1:03d}.png")
    w, h = im.size
    im.crop((0, 0, int(w*0.52), h)).save(f"recipe_crops/p{p_num+1:03d}_left.png")
    im.crop((int(w*0.48), 0, w, h)).save(f"recipe_crops/p{p_num+1:03d}_right.png")

print("Rendered and cropped PDF pages 60 to 65 successfully.")
