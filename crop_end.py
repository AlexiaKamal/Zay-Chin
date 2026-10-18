from PIL import Image

for p in [105, 106, 107, 108, 109]:
    im = Image.open(f'page_images/page_{p:03d}.png')
    w, h = im.size
    im.crop((0, 0, int(w*0.5), int(h*0.3))).save(f'recipe_crops/end_p{p}_left.png')
    im.crop((int(w*0.5), 0, w, int(h*0.3))).save(f'recipe_crops/end_p{p}_right.png')

print("End page crops saved.")
