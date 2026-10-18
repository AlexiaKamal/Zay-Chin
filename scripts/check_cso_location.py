from bs4 import BeautifulSoup
import re

with open("scripts/cso_sample.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

# Look for titles, descriptions, footnotes, or location indicators
for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'span']):
    text = tag.get_text(strip=True)
    if any(k in text.lower() for k in ['market', 'yangon', 'naypyitaw', 'average', 'retail', 'wholesale', 'location', 'source']):
        print(f"[{tag.name}]: {text}")
