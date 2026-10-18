import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

url = "https://inmu.mahidol.ac.th/thaifcd/foodsearch/food_name"
payload = urllib.parse.urlencode({
    "food_name": "rice",
    "page_no": "1",
    "status": "A"
}).encode()

req = urllib.request.Request(url, data=payload, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        soup = BeautifulSoup(html, "html.parser")
        tables = soup.find_all("table")
        print("Tables in search results:", len(tables))
        for t in tables:
            for r in t.find_all("tr")[:8]:
                cols = [td.get_text(strip=True) for td in r.find_all(["th", "td"])]
                if cols:
                    print(" | ".join(cols))
except Exception as e:
    print("Thai FCD search error:", e)
