import urllib.request
from bs4 import BeautifulSoup
import re

url = "https://inmu.mahidol.ac.th/thaifcd/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        soup = BeautifulSoup(html, "html.parser")
        print("Thai FCD title:", soup.title.get_text() if soup.title else "No title")
        print("Links found:")
        for a in soup.find_all("a"):
            href = a.get("href", "")
            text = a.get_text(strip=True)
            if any(k in href.lower() or k in text.lower() for k in ["search", "food", "table", "download", "database"]):
                print(f"  {text} -> {href}")
except Exception as e:
    print("Thai FCD error:", e)
