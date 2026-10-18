import re

with open("scripts/fao_html.html", "w", encoding="utf-8") if False else open("scripts/inspect_fao_items.py"):
    pass

import urllib.request
url = "https://www.fao.org/food-composition/tables-and-databases/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode("utf-8", errors="ignore")

idx = html.lower().find("myanmar")
while idx != -1:
    print("--- CONTEXT ---")
    print(html[max(0, idx-100):min(len(html), idx+300)])
    idx = html.lower().find("myanmar", idx+1)
