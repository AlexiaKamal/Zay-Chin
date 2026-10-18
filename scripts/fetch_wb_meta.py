import urllib.request
import json

url = "https://microdata.worldbank.org/metadata/export/4501/json"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        print("WB METADATA KEYS:", list(data.keys()))
        study = data.get("study_desc", {})
        print("STUDY TITLE:", study.get("title_statement"))
        print("STUDY ABSTRACT:", str(study.get("study_info", {}).get("abstract"))[:500])
        with open("scripts/wb_metadata.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
except Exception as e:
    print("Error:", e)
