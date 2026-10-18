import urllib.request
from bs4 import BeautifulSoup
import re

url = "https://www.citymall.com.mm/citymall/en/search/?text=rice"
req = urllib.request.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        print("Citymall search status:", resp.status)
        print("Length:", len(html))
        soup = BeautifulSoup(html, "html.parser")
        items = soup.find_all(class_=re.compile(r'product|item|price', re.I))
        print("Found items count:", len(items))
        for it in items[:10]:
            print(it.get_text(strip=True)[:100])
except Exception as e:
    print("Citymall search error:", e)
