import urllib.request
from bs4 import BeautifulSoup

url = "https://www.fao.org/food-composition/tables-and-databases/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        soup = BeautifulSoup(html, "html.parser")
        print("FAO title:", soup.title.get_text() if soup.title else "")
        links = []
        for a in soup.find_all("a"):
            href = a.get("href", "")
            text = a.get_text(strip=True)
            if any(k in href.lower() or k in text.lower() for k in ["asia", "myanmar", "aseanfoods", "fao/infoods", "database", "table", "download"]):
                links.append((text, href))
        print(f"Relevant FAO links found: {len(links)}")
        for t, h in links[:15]:
            print(f"  {t} -> {h}")
except Exception as e:
    print("FAO error:", e)
