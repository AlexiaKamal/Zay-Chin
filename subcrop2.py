from PIL import Image

im78 = Image.open('recipe_crops/inspect_p78.png')
w, h = im78.size
im78.crop((0, 0, w, int(h * 0.55))).save('recipe_crops/p78_top.png')
im78.crop((0, int(h * 0.45), w, h)).save('recipe_crops/p78_bottom.png')

im79 = Image.open('recipe_crops/inspect_p79.png')
w, h = im79.size
im79.crop((0, 0, w, int(h * 0.55))).save('recipe_crops/p79_top.png')
im79.crop((0, int(h * 0.45), w, h)).save('recipe_crops/p79_bottom.png')

print("p78 and p79 crops saved.")
