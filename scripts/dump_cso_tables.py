from bs4 import BeautifulSoup
import re

with open("scripts/cso_sample.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

tables = soup.find_all("table")
for i, t in enumerate(tables):
    rows = t.find_all("tr")
    print(f"\n================ TABLE {i+1} ================")
    headers = []
    for r in rows:
        th_list = r.find_all("th")
        if th_list:
            headers = [re.sub(r'\s+', ' ', th.get_text(strip=True)) for th in th_list]
            print("HEADER:", headers)
        else:
            td_list = [re.sub(r'\s+', ' ', td.get_text(strip=True)) for td in r.find_all("td")]
            if td_list:
                print("ROW:", td_list)
