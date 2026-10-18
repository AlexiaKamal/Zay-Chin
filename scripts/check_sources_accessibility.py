import urllib.request
import urllib.error
import ssl
import json
import time

sources = [
    {
        "id": "SRC01",
        "name": "Myanmar Central Statistical Organization (CSO)",
        "url": "https://www.csostat.gov.mm/Statistics/MarketPrice",
        "type": "price"
    },
    {
        "id": "SRC02",
        "name": "Yangon Region Commodity Exchange",
        "url": "https://www.yangoncommodityexchange.com/local-prices",
        "type": "price"
    },
    {
        "id": "SRC03",
        "name": "Citymall Myanmar",
        "url": "https://www.citymall.com.mm/",
        "type": "price"
    },
    {
        "id": "SRC04",
        "name": "World Bank Myanmar Food Price Estimates",
        "url": "https://microdata.worldbank.org/index.php/catalog/4501/study-description",
        "type": "price"
    },
    {
        "id": "SRC05",
        "name": "USDA FoodData Central API",
        "url": "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=DEMO_KEY&query=rice&pageSize=1",
        "type": "nutrition"
    },
    {
        "id": "SRC06",
        "name": "FAO/INFOODS Food Composition Databases",
        "url": "https://www.fao.org/food-composition/tables-and-databases/",
        "type": "nutrition"
    },
    {
        "id": "SRC07",
        "name": "Thai Food Composition Database",
        "url": "https://inmu.mahidol.ac.th/thaifcd/",
        "type": "nutrition"
    },
    {
        "id": "SRC08",
        "name": "Open Food Facts API",
        "url": "https://world.openfoodfacts.org/api/v2/search?categories_tags_en=rice&page_size=1",
        "type": "nutrition"
    }
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,application/json,*/*;q=0.8"
}

results = []
# Create unverified context if needed for testing TLS certificates
ctx = ssl.create_default_context()

for s in sources:
    start_time = time.time()
    req = urllib.request.Request(s["url"], headers=headers)
    status = None
    error_msg = None
    content_type = None
    content_len = 0
    try:
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            status = resp.status
            content_type = resp.headers.get("Content-Type")
            data = resp.read()
            content_len = len(data)
    except urllib.error.HTTPError as e:
        status = e.code
        error_msg = f"HTTPError {e.code}: {e.reason}"
    except urllib.error.URLError as e:
        # Retry with relaxed SSL in case Myanmar gov certs have chain issues
        try:
            insecure_ctx = ssl._create_unverified_context()
            with urllib.request.urlopen(req, timeout=15, context=insecure_ctx) as resp:
                status = resp.status
                content_type = resp.headers.get("Content-Type")
                data = resp.read()
                content_len = len(data)
                error_msg = "Note: Required unverified SSL context"
        except Exception as e2:
            status = "ConnectionFailed"
            error_msg = f"URLError: {str(e2)}"
    except Exception as e:
        status = "Error"
        error_msg = str(e)
    
    elapsed = round(time.time() - start_time, 2)
    res = {
        "source_id": s["id"],
        "name": s["name"],
        "url": s["url"],
        "type": s["type"],
        "status": status,
        "content_type": content_type,
        "content_len_bytes": content_len,
        "response_time_sec": elapsed,
        "notes": error_msg or "Accessible"
    }
    results.append(res)
    print(f"[{s['id']}] {s['name']}: {status} ({elapsed}s) - {res['notes']}")

with open("scripts/source_accessibility_report.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
