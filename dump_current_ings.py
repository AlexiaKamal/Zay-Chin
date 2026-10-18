# -*- coding: utf-8 -*-
import json

ings = json.load(open('ingredients.json', encoding='utf-8'))
print(f"Total ingredients currently: {len(ings)}")

with open('all_current_ings.txt', 'w', encoding='utf-8') as f:
    for i in ings:
        f.write(f"{i['ingredient_id']} | {i['name_mm']} | {i['name_en']}\n")

print("Dumped to all_current_ings.txt")
