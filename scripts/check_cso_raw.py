import urllib.request
import urllib.parse
import json

url = "https://www.csostat.gov.mm/Statistics/GetMarketPriceByCategory"
payload = urllib.parse.urlencode({"Category": "Rice", "Page": "1", "Language": "English"}).encode()
headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest"
}
req = urllib.request.Request(url, data=payload, headers=headers)
with urllib.request.urlopen(req, timeout=15) as resp:
    raw = resp.read().decode("utf-8")
    print("RAW TYPE:", type(raw))
    print("RAW SAMPLE:")
    print(raw[:500])
    try:
        j = json.loads(raw)
        print("IS JSON! Keys/content:", type(j), str(j)[:500])
    except:
        print("Not JSON")
