from PIL import Image
import os

os.makedirs("b8_crops", exist_ok=True)

pages = [
    ('p073_right', 133),
    ('p074_left', 134),
    ('p074_right', 135),
    ('p075_left', 136),
    ('p075_right', 137),
]

for name, pg in pages:
    im = Image.open(f'recipe_crops/{name}.png')
    w, h = im.size
    top = im.crop((0, 0, w, int(h * 0.52)))
    bot = im.crop((0, int(h * 0.48), w, h))
    top.save(f'b8_crops/{name}_top.png')
    bot.save(f'b8_crops/{name}_bot.png')

print("Batch 8 One-Dish meal crops saved.")
