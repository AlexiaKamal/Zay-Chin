import urllib.request
import urllib.parse
import json
import time

queries = [
    ("I0001", "Rice", "rice white long grain raw unenriched", "raw"),
    ("I0002", "Butter", "butter without salt", "raw"),
    ("I0003", "Cooking oil", "oil peanut salad or cooking", "raw"),
    ("I0004", "Salt", "salt table", "raw"),
    ("I0005", "Sugar", "sugars granulated", "raw"),
    ("I0006", "Onion", "onions raw", "raw"),
    ("I0007", "Nutmeg", "spices nutmeg ground", "dried"),
    ("I0008", "Cinnamon bark", "spices cinnamon ground", "dried"),
    ("I0009", "Cloves", "spices cloves ground", "dried"),
    ("I0010", "Cardamom pods", "spices cardamom", "dried"),
    ("I0011", "Bay leaves", "spices bay leaf", "dried"),
    ("I0012", "Hot water", "water tap drinking", "boiled"),
    ("I0013", "Red lentils", "lentils raw", "raw"),
    ("I0014", "Carrot", "carrots mature raw", "raw"),
    ("I0015", "Green beans", "beans snap green raw", "raw"),
    ("I0016", "Green peas", "peas green raw", "raw"),
    ("I0017", "Water", "water tap drinking", "raw"),
    ("I0018", "Coconut", "nuts coconut meat raw", "raw"),
    ("I0019", "Cooked rice", "rice white long grain cooked", "cooked"),
    ("I0020", "Chicken meat", "chicken meat only raw", "raw")
]

base_url = "https://api.nal.usda.gov/fdc/v1/foods/search"
results = {}

for ing_id, name, q, form in queries:
    params = urllib.parse.urlencode({
        "api_key": "DEMO_KEY",
        "query": q,
        "dataType": "Foundation,SR Legacy",
        "pageSize": 3
    })
    url = f"{base_url}?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "ZayChin-Pilot/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            foods = data.get("foods", [])
            if foods:
                top = foods[0]
                results[ing_id] = {
                    "query": q,
                    "fdc_id": top.get("fdcId"),
                    "description": top.get("description"),
                    "data_type": top.get("dataType"),
                    "food_form": form,
                    "nutrients": {n.get("nutrientName"): (n.get("value"), n.get("unitName")) for n in top.get("foodNutrients", [])}
                }
                print(f"[{ing_id}] {name} -> Found FDC {top.get('fdcId')}: {top.get('description')}")
            else:
                print(f"[{ing_id}] {name} -> NOT FOUND")
        time.sleep(0.3)
    except Exception as e:
        print(f"[{ing_id}] {name} -> Error: {e}")

with open("scripts/usda_pilot_raw.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
