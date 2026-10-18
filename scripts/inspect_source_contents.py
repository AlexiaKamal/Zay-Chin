import urllib.request
import json
import re

# 1. Test Open Food Facts with proper User-Agent header as required by OFF docs
off_url = "https://world.openfoodfacts.org/api/v2/search?categories_tags_en=rice&page_size=1"
off_req = urllib.request.Request(
    off_url,
    headers={"User-Agent": "ZayChin-ResearchApp/1.0 (contact: alexiachoi22@gmail.com) Python-urllib"}
)
try:
    with urllib.request.urlopen(off_req, timeout=10) as resp:
        print("[OFF] Status with custom User-Agent:", resp.status)
        data = json.loads(resp.read().decode())
        print("[OFF] Count of products:", data.get("count"))
except Exception as e:
    print("[OFF] Error:", e)

# 2. Inspect CSO MarketPrice content
cso_url = "https://www.csostat.gov.mm/Statistics/MarketPrice"
try:
    req = urllib.request.Request(cso_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        print("[CSO] HTML length:", len(html))
        # Look for tables, forms, select boxes, or links
        tables = re.findall(r'<table[^>]*>(.*?)</table>', html, re.DOTALL | re.IGNORECASE)
        print("[CSO] Tables found:", len(tables))
        selects = re.findall(r'<select[^>]*>(.*?)</select>', html, re.DOTALL | re.IGNORECASE)
        print("[CSO] Select dropdowns found:", len(selects))
        links = re.findall(r'href=[\'"]([^\'"]*(?:\.xlsx?|\.pdf|\.csv|MarketPrice)[^\'"]*)[\'"]', html, re.IGNORECASE)
        print("[CSO] Relevant links found:", links[:5])
        with open("scripts/cso_sample.html", "w", encoding="utf-8") as f:
            f.write(html)
except Exception as e:
    print("[CSO] Error:", e)

# 3. Inspect Yangon Commodity Exchange content
yce_url = "https://www.yangoncommodityexchange.com/local-prices"
try:
    req = urllib.request.Request(yce_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        print("[YCE] HTML length:", len(html))
        tables = re.findall(r'<table[^>]*>(.*?)</table>', html, re.DOTALL | re.IGNORECASE)
        print("[YCE] Tables found:", len(tables))
        with open("scripts/yce_sample.html", "w", encoding="utf-8") as f:
            f.write(html)
except Exception as e:
    print("[YCE] Error:", e)

# 4. Inspect World Bank Microdata 4501
wb_url = "https://microdata.worldbank.org/index.php/catalog/4501/study-description"
try:
    req = urllib.request.Request(wb_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        print("[WorldBank] HTML length:", len(html))
        title = re.findall(r'<title>(.*?)</title>', html, re.IGNORECASE)
        print("[WorldBank] Title:", title)
        with open("scripts/wb_sample.html", "w", encoding="utf-8") as f:
            f.write(html)
except Exception as e:
    print("[WorldBank] Error:", e)
