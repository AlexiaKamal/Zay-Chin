from bs4 import BeautifulSoup

with open("scripts/yce_sample.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

links = soup.find_all("a")
for a in links:
    href = a.get("href", "")
    text = a.get_text(strip=True)
    if "kitchen" in href.lower() or "kitchen" in text.lower() or "price" in href.lower() or "crop" in href.lower():
        print(f"LINK: {text} -> {href}")
