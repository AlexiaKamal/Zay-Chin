import urllib.request
import urllib.parse
import json

base_url = "https://api.nal.usda.gov/fdc/v1/foods/search"
query = urllib.parse.urlencode({
    "api_key": "DEMO_KEY",
    "query": "raw white rice",
    "dataType": "Foundation,SR Legacy",
    "pageSize": 1
})
req = urllib.request.Request(f"{base_url}?{query}", headers={"User-Agent": "ZayChin/1.0"})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        food = data["foods"][0]
        print("USDA FDC ID:", food.get("fdcId"))
        print("Description:", food.get("description"))
        print("Data Type:", food.get("dataType"))
        print("Food Nutrients count:", len(food.get("foodNutrients", [])))
        for n in food.get("foodNutrients", [])[:15]:
            print(f"Nutrient: {n.get('nutrientName')} ({n.get('nutrientNumber')}) = {n.get('value')} {n.get('unitName')}")
except Exception as e:
    print("USDA error:", e)
