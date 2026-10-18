# -*- coding: utf-8 -*-
"""
Inspect headers and page numbers of Batch 7 pages.
"""
from PIL import Image
import os

os.makedirs("inspect_crops", exist_ok=True)

for p in range(64, 74):
    for side in ['left', 'right']:
        fn = f"recipe_crops/p{p:03d}_{side}.png"
        if not os.path.exists(fn):
            continue
        im = Image.open(fn)
        w, h = im.size
        # Crop header (top 15%)
        header = im.crop((0, 0, w, int(h * 0.15)))
        header.save(f"inspect_crops/p{p:03d}_{side}_hdr.png")
        
        # Crop middle title (around 45%-60%)
        mid = im.crop((0, int(h * 0.45), w, int(h * 0.60)))
        mid.save(f"inspect_crops/p{p:03d}_{side}_mid.png")
        
        # Crop footer (bottom 8%)
        footer = im.crop((0, int(h * 0.92), w, h))
        footer.save(f"inspect_crops/p{p:03d}_{side}_ftr.png")

print("Created inspection crops.")
