from PIL import Image
import os

os.makedirs("b8_inspect", exist_ok=True)

# List of pages for Batch 8:
pages = [('p073', 'right')]
for p in range(74, 92):
    pages.append((f'p{p:03d}', 'left'))
    pages.append((f'p{p:03d}', 'right'))

for p_prefix, side in pages:
    fn = f"recipe_crops/{p_prefix}_{side}.png"
    if not os.path.exists(fn):
        continue
    im = Image.open(fn)
    w, h = im.size
    
    # Top header
    hdr = im.crop((0, 0, w, int(h * 0.20)))
    hdr.save(f"b8_inspect/{p_prefix}_{side}_top.png")
    
    # Mid section
    mid = im.crop((0, int(h * 0.42), w, int(h * 0.62)))
    mid.save(f"b8_inspect/{p_prefix}_{side}_mid.png")
    
    # Footer (printed page number)
    ftr = im.crop((0, int(h * 0.90), w, h))
    ftr.save(f"b8_inspect/{p_prefix}_{side}_ftr.png")

print(f"Created inspection crops for {len(pages)} pages.")
