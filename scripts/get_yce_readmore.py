from bs4 import BeautifulSoup
import urllib.parse

with open("scripts/yce_kitchen_crop.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

for a in soup.find_all("a"):
    if "Read More" in a.get_text():
        print("READ MORE LINK:", a.get("href"))
        break
