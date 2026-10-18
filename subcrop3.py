from PIL import Image

im46 = Image.open('page_images/page_046.png')
w, h = im46.size
# p80
p80 = im46.crop((0, 0, int(w * 0.52), h))
p80.save('recipe_crops/inspect_p80.png')
p80.crop((0, 0, p80.width, int(h * 0.55))).save('recipe_crops/p80_top.png')
p80.crop((0, int(h * 0.45), p80.width, h)).save('recipe_crops/p80_bottom.png')

# p81
p81 = im46.crop((int(w * 0.48), 0, w, h))
p81.save('recipe_crops/inspect_p81.png')
p81.crop((0, 0, p81.width, int(h * 0.55))).save('recipe_crops/p81_top.png')
p81.crop((0, int(h * 0.45), p81.width, h)).save('recipe_crops/p81_bottom.png')

print("Page 46 (p80, p81) cropped successfully.")
