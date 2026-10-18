import urllib.request
import urllib.parse
import json
import time

search_terms = [
    ("I0001", "Rice", "ဆန်"),
    ("I0002", "Butter", "Butter"),
    ("I0003", "Cooking oil", "Peanut Oil"),
    ("I0004", "Salt", "Salt"),
    ("I0005", "Sugar", "Sugar"),
    ("I0006", "Onion", "Onion"),
    ("I0007", "Nutmeg", "Nutmeg"),
    ("I0008", "Cinnamon", "Cinnamon"),
    ("I0009", "Cloves", "Cloves"),
    ("I0010", "Cardamom", "Cardamom"),
    ("I0011", "Bay leaves", "Bay leaves"),
    ("I0013", "Red lentils", "Lentil"),
    ("I0014", "Carrot", "Carrot"),
    ("I0015", "Green beans", "Green beans"),
    ("I0016", "Green peas", "Peas"),
    ("I0018", "Coconut", "Coconut"),
    ("I0020", "Chicken meat", "Chicken")
]

base_url = "https://www.citymall.com.mm/citymall/my/search/autocomplete/SearchBox"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

results = {}

for ing_id, name_en, term in search_terms:
    query = urllib.parse.urlencode({"term": term})
    url = f"{base_url}?{query}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            prods = data.get("products", [])
            extracted = []
            for p in prods[:3]:
                price_info = p.get("price", {})
                extracted.append({
                    "code": p.get("code"),
                    "name": p.get("name"),
                    "price_mmk": price_info.get("value"),
                    "formatted_price": price_info.get("formattedValue"),
                    "url": p.get("url"),
                    "weight": p.get("weight"),
                    "weight_unit": p.get("weightUnit"),
                    "brand": p.get("brandName")
                })
            results[ing_id] = extracted
            print(f"[{ing_id}] {name_en} ('{term}') -> Found {len(extracted)} products")
            if extracted:
                print(f"       Example: {extracted[0]['name']} : {extracted[0]['formatted_price']}")
        time.sleep(2.0) # Respect crawl delay
    except Exception as e:
        print(f"[{ing_id}] {name_en} Error:", e)

with open("scripts/citymall_pilot_extracted.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
