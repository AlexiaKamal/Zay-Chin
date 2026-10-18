from PIL import Image

# Let's crop p75 lower half to see if there is another recipe on p75
im75 = Image.open('recipe_crops/inspect_p75.png')
w, h = im75.size
# Top half of p75 was Fried Rice. Let's crop bottom half
im75.crop((0, int(h * 0.45), w, h)).save('recipe_crops/p75_bottom.png')

# Let's crop p76 top, middle, bottom
im76 = Image.open('recipe_crops/inspect_p76.png')
w, h = im76.size
im76.crop((0, 0, w, int(h * 0.55))).save('recipe_crops/p76_top.png')
im76.crop((0, int(h * 0.45), w, h)).save('recipe_crops/p76_bottom.png')

# Let's crop p77 top, middle, bottom
im77 = Image.open('recipe_crops/inspect_p77.png')
w, h = im77.size
im77.crop((0, 0, w, int(h * 0.55))).save('recipe_crops/p77_top.png')
im77.crop((0, int(h * 0.45), w, h)).save('recipe_crops/p77_bottom.png')

print("Sub-crops saved.")
