import json

with open("scripts/wb_metadata.json", "r", encoding="utf-8") as f:
    data = json.load(f)

variables = data.get("variables", [])
for v in variables:
    name = v.get("name")
    labl = v.get("labl")
    if any(k in name.lower() or k in str(labl).lower() for k in ["rice", "oil", "bean", "meat", "price", "chicken", "onion", "sugar", "salt"]):
        print(f"{name} -> {labl}")
