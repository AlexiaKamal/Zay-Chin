import re

with open("scripts/cso_sample.html", "r", encoding="utf-8") as f:
    html = f.read()

scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
print(scripts[22]) # Script 23 (0-indexed 22)
