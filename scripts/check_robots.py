import urllib.request

for url in [
    "https://www.citymall.com.mm/robots.txt",
    "https://www.csostat.gov.mm/robots.txt",
    "https://www.yangoncommodityexchange.com/robots.txt"
]:
    print(f"\n--- {url} ---")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(resp.read().decode("utf-8", errors="ignore")[:500])
    except Exception as e:
        print("Error:", e)
