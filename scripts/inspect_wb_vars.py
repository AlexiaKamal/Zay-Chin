import json

with open("scripts/wb_metadata.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("DATA FILES:", data.get("data_files"))
variables = data.get("variables", [])
print(f"TOTAL VARIABLES: {len(variables)}")
for v in variables[:15]:
    print(v.get("name"), "::", v.get("labl"))
