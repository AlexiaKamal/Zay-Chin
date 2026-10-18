import urllib.request
from bs4 import BeautifulSoup
import re

url = "https://fdc.nal.usda.gov/download-datasets.html"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        soup = BeautifulSoup(html, "html.parser")
        print("USDA Download Datasets page title:", soup.title.get_text() if soup.title else "")
        links = []
        for a in soup.find_all("a"):
            h = a.get("href", "")
            t = a.get_text(strip=True)
            if any(k in h.lower() for k in ["zip", "csv", "json", "foundation", "sr-legacy"]):
                links.append((t, h))
        print(f"Download links found: {len(links)}")
        for t, h in links[:15]:
            print(f"  {t} -> {h}")
except Exception as e:
    print("Download page error:", e)
