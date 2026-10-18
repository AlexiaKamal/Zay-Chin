from PIL import Image

# PDF page 46 (printed pp 80, 81)
im46 = Image.open('page_images/page_046.png')
w, h = im46.size
# p80: Puffy Omelet, Salted Eggs
im46.crop((0, 0, int(w*0.52), int(h*0.55))).save('recipe_crops/r_p80_top.png')
im46.crop((0, int(h*0.45), int(w*0.52), h)).save('recipe_crops/r_p80_bottom.png')
# p81: Duck Eggs Curry, Mini Omelet with Minced Meat
im46.crop((int(w*0.48), 0, w, int(h*0.55))).save('recipe_crops/r_p81_top.png')
im46.crop((int(w*0.48), int(h*0.45), w, h)).save('recipe_crops/r_p81_bottom.png')

# PDF page 47 (printed pp 82, 83)
im47 = Image.open('page_images/page_047.png')
# p82: Chicken sweet & sour, Fried chicken
im47.crop((0, 0, int(w*0.52), int(h*0.55))).save('recipe_crops/r_p82_top.png')
im47.crop((0, int(h*0.45), int(w*0.52), h)).save('recipe_crops/r_p82_bottom.png')
# p83: Chicken chickpea curry, Chicken kebab
im47.crop((int(w*0.48), 0, w, int(h*0.55))).save('recipe_crops/r_p83_top.png')
im47.crop((int(w*0.48), int(h*0.45), w, h)).save('recipe_crops/r_p83_bottom.png')

# PDF page 48 (printed pp 84, 85)
im48 = Image.open('page_images/page_048.png')
# p84: Chicken liver curry, Chicken curry
im48.crop((0, 0, int(w*0.52), int(h*0.55))).save('recipe_crops/r_p84_top.png')
im48.crop((0, int(h*0.45), int(w*0.52), h)).save('recipe_crops/r_p84_bottom.png')

print("Batch 3 images cropped successfully.")
