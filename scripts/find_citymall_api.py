from bs4 import BeautifulSoup
import re

with open("scripts/citymall_sample.html", "w", encoding="utf-8") if False else open("scripts/inspect_citymall_cards.py") as _:
    pass

# Read HTML directly
import urllib.request
url = "https://www.citymall.com.mm/citymall/my/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        endpoints = set(re.findall(r'[\'"](/[^"\'\s>]*(?:api|search|product|category|occ)[^"\'\s>]*)[\'"]', html, re.I))
        print("Endpoints found:", list(endpoints)[:15])
except Exception as e:
    print("Error:", e)
