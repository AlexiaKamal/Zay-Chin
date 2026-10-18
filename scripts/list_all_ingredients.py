import json

with open("ingredients.json", "r", encoding="utf-8") as f:
    ings = json.load(f)

print(f"Total: {len(ings)}")
with open("scripts/catalog_summary.txt", "w", encoding="utf-8") as out:
    for i in ings:
        line = f"{i['ingredient_id']}\t{i['category']}\t{i['name_mm']}\t{i['name_en']}\n"
        out.write(line)

print("Wrote scripts/catalog_summary.txt")
