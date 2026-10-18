import json
import urllib.request
import urllib.parse

with open("ingredients.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

pilot_ingredients = catalog[:20]

print(f"Loaded {len(pilot_ingredients)} pilot ingredients:")
for ing in pilot_ingredients:
    print(f"- {ing['ingredient_id']}: {ing['name_mm']} / {ing['name_en']} ({ing['category']})")
