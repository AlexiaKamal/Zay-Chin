import json

with open('ingredients.json', encoding='utf-8') as f:
    ings = json.load(f)

words = ['စပါးလင်', 'ဆန်လှော်မှုန့်', 'မုန့်ဟင်းခါး', 'ခေါက်ဆွဲ', 'ငါးကျည်း', 'ငါးခူ', 'ငါးဖယ်', 'ငါးရွှေ', 'ပဒဲကော', 'ဆီတို့ဟူး', 'ကျောက်ပွင့်', 'ပန်းခြောက်', 'မှိုခြောက်', 'ကော်မှုန့်', 'ကြာဆံ', 'ကြွပ်ဆိုင်', 'မုန့်ကြွပ်']
for w in words:
    matches = [f"{i['ingredient_id']}: {i['name_mm']} ({i['name_en']})" for i in ings if w in i['name_mm'] or any(w in a for a in i['aliases_mm'])]
    print(f"{w} -> {matches if matches else 'NEW'}")
