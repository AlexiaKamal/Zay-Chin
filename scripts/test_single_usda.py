import urllib.request
import json

url = "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=DEMO_KEY&query=cloves&pageSize=1"
try:
    with urllib.request.urlopen(url, timeout=10) as resp:
        print("Status:", resp.status)
        data = json.loads(resp.read().decode())
        print("Foods found:", len(data.get("foods", [])))
        if data.get("foods"):
            print("Top food:", data["foods"][0].get("description"), "FDC:", data["foods"][0].get("fdcId"))
except Exception as e:
    print("Error:", e)
