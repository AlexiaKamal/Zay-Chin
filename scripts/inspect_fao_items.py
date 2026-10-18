import re
import json

with open("scripts/fao_sample.html", "w", encoding="utf-8") if False else open("scripts/find_fao_myanmar_link.py"):
    pass

import urllib.request
url = "https://www.fao.org/food-composition/tables-and-databases/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode("utf-8", errors="ignore")

# Find the items JSON or array in the page
match = re.search(r'var items = (\[.*?\]);', html, re.DOTALL)
if match:
    items = json.loads(match.group(1))
    print(f"Total map items: {len(items)}")
    for it in items:
        if "myanmar" in str(it).lower():
            print("MYANMAR ITEM:", it)
else:
    print("No items match found directly")
