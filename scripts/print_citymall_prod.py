import urllib.request
import urllib.parse
import json

base_url = "https://www.citymall.com.mm/citymall/my/search/autocomplete/SearchBox"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "X-Requested-With": "XMLHttpRequest"
}

query = urllib.parse.urlencode({"term": "ဆန်"})
req = urllib.request.Request(f"{base_url}?{query}", headers=headers)
with urllib.request.urlopen(req, timeout=15) as resp:
    data = json.loads(resp.read().decode("utf-8"))
    for p in data.get("products", [])[:5]:
        print("Product keys:", list(p.keys()))
        print("Name:", p.get("name"))
        print("Code:", p.get("code"))
        print("Price:", p.get("price"))
        print("Url:", p.get("url"))
