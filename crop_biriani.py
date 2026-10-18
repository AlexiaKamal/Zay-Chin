from PIL import Image

im = Image.open('recipe_crops/p75_bottom.png')
w, h = im.size
# Crop left column (ingredients) and right column (instructions)
im.crop((0, 0, int(w * 0.45), h)).save('recipe_crops/biriani_ing.png')
im.crop((int(w * 0.42), 0, w, h)).save('recipe_crops/biriani_inst.png')
print("Biriani crops saved.")
