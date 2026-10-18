from PIL import Image

# Inspect p43 right half (printed p. 75)
im43 = Image.open('page_images/page_043.png')
w, h = im43.size
# printed page 75 is roughly w/2 to w
p75 = im43.crop((int(w * 0.48), 0, w, h))
p75.save('recipe_crops/inspect_p75.png')

# Inspect p44 (printed pp. 76 and 77)
im44 = Image.open('page_images/page_044.png')
p76 = im44.crop((0, 0, int(w * 0.52), h))
p76.save('recipe_crops/inspect_p76.png')

p77 = im44.crop((int(w * 0.48), 0, w, h))
p77.save('recipe_crops/inspect_p77.png')

# Inspect p45 (printed pp. 78 and 79)
im45 = Image.open('page_images/page_045.png')
p78 = im45.crop((0, 0, int(w * 0.52), h))
p78.save('recipe_crops/inspect_p78.png')

p79 = im45.crop((int(w * 0.48), 0, w, h))
p79.save('recipe_crops/inspect_p79.png')

print("Crops saved successfully.")
