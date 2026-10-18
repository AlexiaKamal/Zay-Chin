import urllib.request
import urllib.parse
import json
from bs4 import BeautifulSoup

url = "https://www.csostat.gov.mm/Statistics/GetMarketPriceByCategory"
categories = [
    ("Rice", "Kyat/Pyi"),
    ("Edible Oil", "Kyat/Viss"),
    ("Pulses", "Kyat/Viss"),
    ("Spices", "Kyat/Viss"),
    ("Fish and Prawn", "Kyat/Viss")
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest"
}

dates = ["12-10-2026", "13-10-2026", "14-10-2026", "15-10-2026", "16-10-2026"]
cso_all = []

for cat, unit in categories:
    payload = urllib.parse.urlencode({"Category": cat, "Page": "1", "Language": "English"}).encode()
    req = urllib.request.Request(url, data=payload, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read().decode("utf-8")
            html_snippet = json.loads(raw)
            soup = BeautifulSoup(html_snippet, "html.parser")
            rows = soup.find_all("tr")
            for r in rows:
                cols = [td.get_text(strip=True) for td in r.find_all("td")]
                if len(cols) >= 7 and cols[0].isdigit():
                    sr = cols[0]
                    commodity = cols[1]
                    price_series = {dates[i]: cols[2+i] for i in range(len(dates)) if 2+i < len(cols)}
                    cso_all.append({
                        "category": cat,
                        "unit": unit,
                        "commodity": commodity,
                        "prices": price_series
                    })
    except Exception as e:
        print(f"Error {cat}:", e)

print(f"Total CSO commodities extracted: {len(cso_all)}")
for item in cso_all:
    print(f"[{item['category']}] {item['commodity']} ({item['unit']}): {item['prices']}")

with open("scripts/cso_full_extracted.json", "w", encoding="utf-8") as f:
    json.dump(cso_all, f, indent=2, ensure_ascii=False)
