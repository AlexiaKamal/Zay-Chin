from PIL import Image

# Let's crop the table of contents from page_003.png, page_004.png, page_005.png
for p_num in ['003', '004', '005']:
    im = Image.open(f'page_images/page_{p_num}.png')
    w, h = im.size
    im.crop((0, 0, int(w * 0.52), h)).save(f'recipe_crops/toc_{p_num}_left.png')
    im.crop((int(w * 0.48), 0, w, h)).save(f'recipe_crops/toc_{p_num}_right.png')

print("TOC crops saved.")
