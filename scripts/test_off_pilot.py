import urllib.request
import urllib.parse
import json
import time

test_queries = [
    ("I0009", "Cloves", "cloves"),
    ("I0010", "Cardamom pods", "cardamom"),
    ("I0011", "Bay leaves", "bay leaves"),
    ("I0012", "Hot water", "water"),
    ("I0013", "Red lentils", "red lentils"),
    ("I0014", "Carrot", "raw carrots"),
    ("I0015", "Green beans", "green beans"),
    ("I0016", "Green peas", "green peas"),
    ("I0017", "Water", "water"),
    ("I0018", "Coconut", "fresh coconut"),
    ("I0019", "Cooked rice", "cooked white rice"),
    ("I0020", "Chicken meat", "chicken breast raw")
]

headers = {
    "User-Agent": "ZayChin-ResearchApp/1.0 (contact: alexiachoi22@gmail.com)"
}

for ing_id, name, q in test_queries:
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={urllib.parse.quote(q)}&search_simple=1&action=process&json=1&page_size=1"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            products = data.get("products", [])
            if products:
                p = products[0]
                nutr = p.get("nutriments", {})
                print(f"[{ing_id}] {name} -> OFF Barcode: {p.get('code')}, Name: {p.get('product_name')}")
                print(f"       kcal: {nutr.get('energy-kcal_100g')}, P: {nutr.get('proteins_100g')}, F: {nutr.get('fat_100g')}, C: {nutr.get('carbohydrates_100g')}")
            else:
                print(f"[{ing_id}] {name} -> OFF: No products")
        time.sleep(1.0) # Respect rate limits
    except Exception as e:
        print(f"[{ing_id}] {name} -> OFF Error: {e}")
