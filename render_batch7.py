# -*- coding: utf-8 -*-
"""
Render PDF pages 64 to 73 (Book pp. 117-133) for Batch 7.
"""
import pypdfium2 as pdfium
from PIL import Image
import os

pdf_path = "ဟင္းခ်က္နည္းမ်ား.pdf"
os.makedirs("page_images", exist_ok=True)
os.makedirs("recipe_crops", exist_ok=True)

pdf = pdfium.PdfDocument(pdf_path)

# Pages 64 to 73 in 1-based indexing (63 to 72 in 0-based)
for page_num in range(64, 74):
    print(f"Rendering page {page_num}...")
    page = pdf[page_num - 1]
    pil_image = page.render(scale=1.5).to_pil()
    page_img_path = f"page_images/page_{page_num:03d}.png"
    pil_image.save(page_img_path)
    
    # Crop into left and right halves
    w, h = pil_image.size
    left_crop = pil_image.crop((0, 0, int(w * 0.52), h))
    right_crop = pil_image.crop((int(w * 0.48), 0, w, h))
    
    left_crop.save(f"recipe_crops/p{page_num:03d}_left.png")
    right_crop.save(f"recipe_crops/p{page_num:03d}_right.png")

print("Rendering complete!")
