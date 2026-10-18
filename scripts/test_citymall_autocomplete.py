import urllib.request
import urllib.parse
import json

base_url = "https://www.citymall.com.mm/citymall/my/search/autocomplete/SearchBox"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "X-Requested-With": "XMLHttpRequest"
}

for term in ["ဆန်", "ဆီ", "ကြက်သွန်"]:
    query = urllib.parse.urlencode({"term": term})
    url = f"{base_url}?{query}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read().decode("utf-8")
            print(f"\n--- Term: {term} (Status: {resp.status}) ---")
            print(data[:400])
    except Exception as e:
        print(f"Error for {term}:", e)
