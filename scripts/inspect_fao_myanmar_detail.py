import urllib.request
from bs4 import BeautifulSoup

url = "https://www.fao.org/food-composition/tables-and-databases/detail/(myanmar--1967)-the-nutritive-value-of-burmese-foods/en"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        soup = BeautifulSoup(html, "html.parser")
        print("TITLE:", soup.title.get_text() if soup.title else "")
        main_content = soup.find("main") or soup.find("article") or soup.find("div", class_="content") or soup.body
        print("TEXT SAMPLE:")
        print(main_content.get_text(strip=True)[:1000])
        for a in soup.find_all("a"):
            h = a.get("href", "")
            if any(k in h.lower() for k in ["pdf", "download", "link", "fao", "http"]):
                print("LINK:", a.get_text().strip(), "->", h)
except Exception as e:
    print("Error:", e)
