from bs4 import BeautifulSoup
import re

with open("scripts/wb_sample.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

for a in soup.find_all("a"):
    href = a.get("href", "")
    text = a.get_text(strip=True)
    if any(k in href.lower() for k in ["download", "data", "get-file", "csv", "xlsx", "zip"]):
        print(f"WB LINK: {text} -> {href}")
