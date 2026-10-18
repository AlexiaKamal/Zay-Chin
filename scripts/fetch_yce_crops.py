import urllib.request
from bs4 import BeautifulSoup

url = "https://www.yangoncommodityexchange.com/index.php/kitchen-crop"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        soup = BeautifulSoup(html, "html.parser")
        tables = soup.find_all("table")
        print(f"Tables found: {len(tables)}")
        for t in tables:
            for r in t.find_all("tr")[:10]:
                cols = [td.get_text(strip=True) for td in r.find_all(["th", "td"])]
                if cols:
                    print(" | ".join(cols))
        with open("scripts/yce_kitchen_crop.html", "w", encoding="utf-8") as f:
            f.write(html)
except Exception as e:
    print("Error:", e)
