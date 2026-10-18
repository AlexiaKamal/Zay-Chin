import json

with open("recipes.json", "r", encoding="utf-8") as f:
    recipes = json.load(f)

for r in recipes:
    r.pop("alternative_titles_mm", None)
    r.pop("alternative_titles_en", None)

with open("recipes.json", "w", encoding="utf-8") as f:
    json.dump(recipes, f, ensure_ascii=False, indent=2)

print("Cleaned extra keys from recipes.json.")
