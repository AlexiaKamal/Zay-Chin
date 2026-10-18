from PIL import Image

im2 = Image.open('page_images/page_002.png')
w, h = im2.size
im2.crop((0, 0, int(w * 0.52), h)).save('recipe_crops/toc_002_left.png')
im2.crop((int(w * 0.48), 0, w, h)).save('recipe_crops/toc_002_right.png')

print("TOC page 2 cropped.")
