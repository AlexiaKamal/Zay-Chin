from PIL import Image
import os

os.makedirs('b9_zoom', exist_ok=True)

# p078_right (p143): Chicken sandwiches & Pizza
im = Image.open('recipe_crops/p078_right.png')
w, h = im.size
im.crop((0, 0, int(w*0.5), int(h*0.4))).save('b9_zoom/p143_chick_sand_ing.png')
im.crop((0, int(h*0.48), int(w*0.5), int(h*0.9))).save('b9_zoom/p143_pizza_ing.png')

# p079_left (p144): Plain cake & Fruit cake
im = Image.open('recipe_crops/p079_left.png')
w, h = im.size
im.crop((0, 0, int(w*0.45), int(h*0.4))).save('b9_zoom/p144_plain_cake_ing.png')
im.crop((0, int(h*0.48), int(w*0.45), int(h*0.9))).save('b9_zoom/p144_fruit_cake_ing.png')

# p079_right (p145): Doughnut & Caramel custard
im = Image.open('recipe_crops/p079_right.png')
w, h = im.size
im.crop((0, 0, int(w*0.5), int(h*0.45))).save('b9_zoom/p145_doughnut_ing.png')
im.crop((0, int(h*0.48), int(w*0.5), int(h*0.8))).save('b9_zoom/p145_caramel_ing.png')

# p080_left (p146): Bombay toast & Cheese straws
im = Image.open('recipe_crops/p080_left.png')
w, h = im.size
im.crop((0, 0, int(w*0.45), int(h*0.35))).save('b9_zoom/p146_toast_ing.png')
im.crop((0, int(h*0.38), int(w*0.45), int(h*0.75))).save('b9_zoom/p146_cheese_straws_ing.png')

# p080_right (p147): Samosas
im = Image.open('recipe_crops/p080_right.png')
w, h = im.size
im.crop((0, 0, int(w*0.5), int(h*0.5))).save('b9_zoom/p147_mutton_samosa_ing.png')
im.crop((0, int(h*0.5), int(w*0.5), int(h*0.95))).save('b9_zoom/p147_veg_samosa_ing.png')

# p081_left (p148): Paratha & Puri
im = Image.open('recipe_crops/p081_left.png')
w, h = im.size
im.crop((0, 0, int(w*0.45), int(h*0.45))).save('b9_zoom/p148_paratha_ing.png')
im.crop((0, int(h*0.5), int(w*0.45), int(h*0.85))).save('b9_zoom/p148_puri_ing.png')

# p081_right (p149): Satay & Peanut sauce
im = Image.open('recipe_crops/p081_right.png')
w, h = im.size
im.crop((0, 0, int(w*0.5), int(h*0.5))).save('b9_zoom/p149_satay_ing.png')
im.crop((0, int(h*0.5), int(w*0.5), int(h*0.9))).save('b9_zoom/p149_peanut_sauce_ing.png')

# p082_left (p150): Spring roll wrapping & fresh spring roll
im = Image.open('recipe_crops/p082_left.png')
w, h = im.size
im.crop((0, 0, int(w*0.45), int(h*0.25))).save('b9_zoom/p150_wrapping_ing.png')
im.crop((0, int(h*0.45), int(w*0.45), int(h*0.9))).save('b9_zoom/p150_spring_roll_ing.png')

# p082_right (p151): Steamed meat bun & Wontons
im = Image.open('recipe_crops/p082_right.png')
w, h = im.size
im.crop((0, 0, int(w*0.5), int(h*0.62))).save('b9_zoom/p151_bun_ing.png')
im.crop((0, int(h*0.65), int(w*0.5), int(h*0.95))).save('b9_zoom/p151_wonton_ing.png')

# p083_left (p152): Pea cubes & Fried noodles
im = Image.open('recipe_crops/p083_left.png')
w, h = im.size
im.crop((0, 0, int(w*0.45), int(h*0.35))).save('b9_zoom/p152_pea_cubes_ing.png')
im.crop((0, int(h*0.45), int(w*0.45), int(h*0.95))).save('b9_zoom/p152_fried_noodles_ing.png')

# p083_right (p153): Prawn toast & Cashews
im = Image.open('recipe_crops/p083_right.png')
w, h = im.size
im.crop((0, 0, int(w*0.45), int(h*0.5))).save('b9_zoom/p153_prawn_toast_ing.png')
im.crop((0, int(h*0.6), int(w*0.45), int(h*0.9))).save('b9_zoom/p153_cashews_ing.png')

# p084_left (p154): Papaya salad & Pumpkin custard
im = Image.open('recipe_crops/p084_left.png')
w, h = im.size
im.crop((0, 0, int(w*0.45), int(h*0.42))).save('b9_zoom/p154_papaya_salad_ing.png')
im.crop((0, int(h*0.45), int(w*0.45), int(h*0.75))).save('b9_zoom/p154_pumpkin_custard_ing.png')

print("All zoom crops generated successfully!")
