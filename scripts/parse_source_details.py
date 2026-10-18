from bs4 import BeautifulSoup
import re

print("=== CSO (Central Statistical Organization) ANALYSIS ===")
try:
    with open("scripts/cso_sample.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    tables = soup.find_all("table")
    print(f"Total tables: {len(tables)}")
    for idx, table in enumerate(tables):
        rows = table.find_all("tr")
        print(f"\n--- Table {idx+1} (Rows: {len(rows)}) ---")
        for r in rows[:5]:
            cols = [re.sub(r'\s+', ' ', c.get_text(strip=True)) for c in r.find_all(['th', 'td'])]
            if cols:
                print(" | ".join(cols[:8]))
except Exception as e:
    print("CSO parse error:", e)

print("\n=== YCE (Yangon Commodity Exchange) ANALYSIS ===")
try:
    with open("scripts/yce_sample.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    tables = soup.find_all("table")
    print(f"Total tables: {len(tables)}")
    for idx, table in enumerate(tables):
        rows = table.find_all("tr")
        print(f"\n--- Table {idx+1} (Rows: {len(rows)}) ---")
        for r in rows[:6]:
            cols = [re.sub(r'\s+', ' ', c.get_text(strip=True)) for c in r.find_all(['th', 'td'])]
            if cols:
                print(" | ".join(cols[:8]))
except Exception as e:
    print("YCE parse error:", e)

print("\n=== World Bank Catalog 4501 ANALYSIS ===")
try:
    with open("scripts/wb_sample.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    text = soup.get_text()
    for kw in ["Coverage", "Geographic", "Periodicity", "License", "Access", "Download", "Citation", "Terms"]:
        matches = [line.strip() for line in text.split("\n") if kw.lower() in line.lower() and len(line.strip()) > 10]
        if matches:
            print(f"Keyword '{kw}':", matches[:2])
except Exception as e:
    print("WB parse error:", e)
