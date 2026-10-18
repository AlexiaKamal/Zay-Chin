from PIL import Image

for p in range(1, 6):
    im = Image.open(f'page_images/page_{p:03d}.png')
    w, h = im.size
    im.crop((0, 0, int(w*0.52), h)).save(f'recipe_crops/full_toc_{p:03d}_left.png')
    im.crop((int(w*0.48), 0, w, h)).save(f'recipe_crops/full_toc_{p:03d}_right.png')

print("All TOC pages cropped.")
