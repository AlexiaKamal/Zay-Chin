import urllib.request
from bs4 import BeautifulSoup
import re

url = "https://www.citymall.com.mm/citymall/en/search/?text=rice"
req = urllib.request.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
})
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode("utf-8", errors="ignore")

soup = BeautifulSoup(html, "html.parser")
# Find product titles and prices
products = []
cards = soup.find_all(class_=re.compile(r'product-item|product-card|item-card', re.I))
print(f"Cards found: {len(cards)}")
if not cards:
    # Try finding price tags and their parent containers
    prices = soup.find_all(text=re.compile(r'Ks|MMK|ကျပ်', re.I))
    print(f"Price texts found: {len(prices)}")
    for p in prices[:10]:
        parent = p.parent
        for _ in range(3):
            if parent.parent: parent = parent.parent
        print("SAMPLE CONTAINER TEXT:", re.sub(r'\s+', ' ', parent.get_text(strip=True))[:150])
else:
    for c in cards[:5]:
        print("CARD:", re.sub(r'\s+', ' ', c.get_text(strip=True))[:150])
