# -*- coding: utf-8 -*-
import json

ings = json.load(open('ingredients.json', encoding='utf-8'))

search_terms = [
    "အာလူး", "မုန်လာဥ", "ပန်းဂေါ်ဖီ", "ဘိုစားပဲ", "ထောပတ်", "နို့", "နွားနို့",
    "အမဲသား", "ကြက်သား", "ဆိတ်သား", "ပင်လယ်ငါး", "ငါး", "ဆား", "ဆန်",
    "ပန်းသီး", "သကြား", "ဘီစကစ်", "ငှက်ပျောသီး", "လိမ္မော်ရည်", "ပီလောပီနံ",
    "စပျစ်သီး", "ပေါင်မုန့်", "ဆီ", "ကြက်ဥ", "ဇာတိပ္ဖိုလ်", "သကာရည်", "ရှောက်",
    "ဂျုံ", "ဘေကင်ပေါင်ဒါ", "ငါးရံ့", "ကြက်သွန်နီ", "ကြက်သွန်ဖြူ", "မုန့်ကြွပ်",
    "ငရုတ်ကောင်း", "ဗနီလာ", "ချင်း", "ရေ", "ပဲငံပြာရည်", "ဂေါ်ဖီ", "ဆိတ်ရိုး"
]

results = {}
for term in search_terms:
    matches = []
    for i in ings:
        if term in i['name_mm'] or any(term in a for a in i.get('aliases_mm', [])):
            matches.append((i['ingredient_id'], i['name_mm'], i['name_en']))
    results[term] = matches

for term, matches in results.items():
    print(f"{term}: {matches}")
