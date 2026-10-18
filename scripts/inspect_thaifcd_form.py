import urllib.request
from bs4 import BeautifulSoup

url = "https://inmu.mahidol.ac.th/thaifcd/foodsearch/food_name"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        soup = BeautifulSoup(html, "html.parser")
        print("Thai FCD Food Name search page:")
        forms = soup.find_all("form")
        print("Forms found:", len(forms))
        for f in forms:
            print("Action:", f.get("action"), "Method:", f.get("method"))
            for inp in f.find_all(["input", "select"]):
                print("  Input:", inp.get("name"), inp.get("type"), inp.get("value"))
except Exception as e:
    print("Thai FCD error:", e)
