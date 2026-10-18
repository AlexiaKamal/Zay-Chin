import urllib.request
from bs4 import BeautifulSoup
import re

url = "https://www.fao.org/food-composition/tables-and-databases/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        soup = BeautifulSoup(html, "html.parser")
        myanmar_matches = soup.find_all(text=re.compile(r'myanmar|burma|asean', re.I))
        print("Myanmar/ASEAN matches:", len(myanmar_matches))
        for m in myanmar_matches:
            parent = m.parent
            print("Match:", m.strip(), "Link:", parent.get("href"))
except Exception as e:
    print("Error:", e)
