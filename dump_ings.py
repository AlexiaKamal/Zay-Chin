import json

with open('ingredients.json', 'r', encoding='utf-8') as f:
    ings = json.load(f)

with open('existing_ings.txt', 'w', encoding='utf-8') as out:
    for item in ings:
        out.write(f"{item['ingredient_id']} | {item['name_mm']} | {item['name_en']}\n")

print(f"Dumped {len(ings)} ingredients to existing_ings.txt")
