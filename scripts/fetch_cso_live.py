import urllib.request
import urllib.parse
import json
from bs4 import BeautifulSoup

url = "https://www.csostat.gov.mm/Statistics/GetMarketPriceByCategory"
categories = ["Rice", "Edible Oil", "Pulses", "Spices", "Fish and Prawn"]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest"
}

cso_data = {}

for cat in categories:
    payload = urllib.parse.urlencode({"Category": cat, "Page": "1", "Language": "English"}).encode()
    req = urllib.request.Request(url, data=payload, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read().decode("utf-8")
            # Usually the server returns HTML fragment (table rows) or JSON
            print(f"\n=== Category: {cat} (Length: {len(content)}) ===")
            soup = BeautifulSoup(content, "html.parser")
            rows = soup.find_all("tr")
            print(f"Rows count: {len(rows)}")
            cat_rows = []
            for r in rows:
                cols = [td.get_text(strip=True) for td in r.find_all("td")]
                if cols:
                    print("  ", cols)
                    cat_rows.append(cols)
            cso_data[cat] = cat_rows
    except Exception as e:
        print(f"Error fetching {cat}:", e)

with open("scripts/cso_extracted_prices.json", "w", encoding="utf-8") as f:
    json.dump(cso_data, f, indent=2, ensure_ascii=False)
