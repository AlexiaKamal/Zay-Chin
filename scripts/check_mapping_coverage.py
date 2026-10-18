import json
import sys
sys.path.append("scripts")
from nutrition_catalog_db import NUTRITION_MAPPING

with open("ingredients.json", "r", encoding="utf-8") as f:
    ings = json.load(f)

all_ids = [i["ingredient_id"] for i in ings]
mapped = [i for i in all_ids if i in NUTRITION_MAPPING]
unmapped = [i for i in all_ids if i not in NUTRITION_MAPPING]

print(f"Total ingredients: {len(all_ids)}")
print(f"Mapped: {len(mapped)}")
print(f"Unmapped: {len(unmapped)}")
for uid in unmapped:
    item = next(x for x in ings if x["ingredient_id"] == uid)
    print(f"- {uid}: {item['name_mm']} / {item['name_en']} ({item['category']})")
