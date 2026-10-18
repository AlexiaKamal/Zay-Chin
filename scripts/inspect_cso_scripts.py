import re

with open("scripts/cso_sample.html", "r", encoding="utf-8") as f:
    html = f.read()

scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
print(f"Total script tags: {len(scripts)}")
for idx, s in enumerate(scripts):
    if "ajax" in s.lower() or "fetch" in s.lower() or "marketprice" in s.lower() or "api" in s.lower() or "url" in s.lower() or "table" in s.lower():
        print(f"\n--- Script {idx+1} ---")
        print(s.strip()[:1000])
