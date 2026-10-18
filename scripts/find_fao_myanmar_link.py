import urllib.request
from bs4 import BeautifulSoup
import re

url = "https://www.fao.org/food-composition/tables-and-databases/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode("utf-8", errors="ignore")

soup = BeautifulSoup(html, "html.parser")
for a in soup.find_all("a"):
    if "myanmar" in a.get_text().lower() or "myanmar" in a.get("href", "").lower():
        print("FAO MYANMAR LINK:", a.get_text().strip(), "->", a.get("href"))
