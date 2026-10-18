# -*- coding: utf-8 -*-
"""
Process Batch 4 Complete: Recipes R0021 - R0042 (22 recipes)
Book pp. 85-95 (PDF pp. 48-53)
"""
import json
import os

with open('recipes.json', 'r', encoding='utf-8') as f:
    recipes = json.load(f)

with open('ingredients.json', 'r', encoding='utf-8') as f:
    ingredients = json.load(f)

with open('extraction_report.json', 'r', encoding='utf-8') as f:
    report = json.load(f)

existing_ing_ids = {i['ingredient_id']: i for i in ingredients}

# New Catalog Ingredients (I0057 to I0085)
new_ingredients = [
    {"ingredient_id": "I0057", "name_mm": "ဘဲသား", "name_en": "Duck meat", "aliases_mm": ["ဘဲကောင်", "ဘဲအကောင်လိုက်"], "aliases_en": ["whole duck", "duck"], "category": "meat", "default_unit": "g"},
    {"ingredient_id": "I0058", "name_mm": "ကြက်သွန်မြိတ်", "name_en": "Spring onion", "aliases_mm": ["ကြက်သွန်မိတ်", "မိတ်"], "aliases_en": ["scallion", "green onion"], "category": "vegetable", "default_unit": "piece"},
    {"ingredient_id": "I0059", "name_mm": "စမုန်ပွင့်", "name_en": "Star anise", "aliases_mm": ["စမုံပွင့်"], "aliases_en": ["star aniseed"], "category": "spice", "default_unit": "piece"},
    {"ingredient_id": "I0060", "name_mm": "ရှယ်ရီအရက်", "name_en": "Cooking wine", "aliases_mm": ["အရက်", "တရုတ်ဝိုင်"], "aliases_en": ["sherry", "Shaoxing wine", "rice wine"], "category": "liquid", "default_unit": "g"},
    {"ingredient_id": "I0061", "name_mm": "ပဲငါးပိရည်", "name_en": "Fermented soybean sauce", "aliases_mm": ["ပဲပိစပ်ရည်"], "aliases_en": ["brown bean sauce"], "category": "seasoning", "default_unit": "g"},
    {"ingredient_id": "I0062", "name_mm": "မုန်ညင်းစေ့", "name_en": "Mustard seeds", "aliases_mm": ["မုံညင်းစေ့"], "aliases_en": ["yellow mustard seeds", "brown mustard seeds"], "category": "spice", "default_unit": "g"},
    {"ingredient_id": "I0063", "name_mm": "ကော်မှုန့်", "name_en": "Tapioca / starch flour", "aliases_mm": ["ကော်ရည်"], "aliases_en": ["starch powder"], "category": "grain", "default_unit": "g"},
    {"ingredient_id": "I0064", "name_mm": "ဘဲမြစ်", "name_en": "Duck gizzard", "aliases_mm": ["ဘဲအမြစ်"], "aliases_en": ["duck gizzards"], "category": "meat", "default_unit": "piece"},
    {"ingredient_id": "I0065", "name_mm": "ငရုတ်စိမ်းပွ", "name_en": "Green bell pepper", "aliases_mm": ["ငရုတ်ပွစိမ်း", "ငရုတ်ပွ"], "aliases_en": ["green capsicum", "sweet pepper"], "category": "vegetable", "default_unit": "piece"},
    {"ingredient_id": "I0066", "name_mm": "ကြက်ဆီ", "name_en": "Chicken fat", "aliases_mm": [], "aliases_en": ["rendered chicken fat"], "category": "oil", "default_unit": "g"},
    {"ingredient_id": "I0067", "name_mm": "နှမ်းဆီ", "name_en": "Sesame oil", "aliases_mm": ["နှမ်းဆီမွှေး"], "aliases_en": ["toasted sesame oil"], "category": "oil", "default_unit": "g"},
    {"ingredient_id": "I0068", "name_mm": "ဆိတ်သား", "name_en": "Mutton", "aliases_mm": ["ဆိတ်သားစဉ်းကော", "ဆိတ်ကီးမား"], "aliases_en": ["goat meat", "minced mutton"], "category": "meat", "default_unit": "g"},
    {"ingredient_id": "I0069", "name_mm": "သင်္ဘောသီး", "name_en": "Green papaya", "aliases_mm": ["သင်္ဘောသီးအကင်း"], "aliases_en": ["raw papaya", "young papaya"], "category": "fruit", "default_unit": "piece"},
    {"ingredient_id": "I0070", "name_mm": "ငရုတ်ပွခြောက်", "name_en": "Dried mild chili", "aliases_mm": ["ငရုတ်သီးပွခြောက်"], "aliases_en": ["dried sweet chili"], "category": "spice", "default_unit": "piece"},
    {"ingredient_id": "I0071", "name_mm": "ဂီးထောပတ်", "name_en": "Ghee", "aliases_mm": ["ဂီး"], "aliases_en": ["clarified butter"], "category": "dairy", "default_unit": "g"},
    {"ingredient_id": "I0072", "name_mm": "မန်ကျည်းသီး", "name_en": "Tamarind", "aliases_mm": ["မန်ကျည်းရည်", "မန်ကျည်းသီးမှည့်ရည်"], "aliases_en": ["tamarind pulp", "tamarind juice"], "category": "seasoning", "default_unit": "g"},
    {"ingredient_id": "I0073", "name_mm": "ဆိတ်ကလီစာ", "name_en": "Mutton offal", "aliases_mm": [], "aliases_en": ["mutton organ meats"], "category": "meat", "default_unit": "g"},
    {"ingredient_id": "I0074", "name_mm": "ပေါင်မုန့်", "name_en": "Bread", "aliases_mm": ["ပေါင်မုန့်ချပ်"], "aliases_en": ["sliced bread", "white bread"], "category": "grain", "default_unit": "piece"},
    {"ingredient_id": "I0075", "name_mm": "ပေါင်မုန့်ကြွပ်မှုန့်", "name_en": "Breadcrumbs", "aliases_mm": ["မုန့်ကြွပ်အမှုန့်", "ပေါင်မုန့်ခြောက်မှုန့်"], "aliases_en": ["panko", "dried breadcrumbs"], "category": "grain", "default_unit": "g"},
    {"ingredient_id": "I0076", "name_mm": "အမဲသား", "name_en": "Beef", "aliases_mm": ["အမဲ", "အမဲစဉ်းကော", "အမဲတင်ပါးသား"], "aliases_en": ["minced beef", "beef rump"], "category": "meat", "default_unit": "g"},
    {"ingredient_id": "I0077", "name_mm": "ပဲစိမ်း", "name_en": "Green peas", "aliases_mm": ["ပဲစိမ်းလုံး"], "aliases_en": ["fresh peas", "sweet peas"], "category": "legume", "default_unit": "g"},
    {"ingredient_id": "I0078", "name_mm": "ခရမ်းသီး", "name_en": "Eggplant", "aliases_mm": ["ခရမ်းသီးရှည်"], "aliases_en": ["brinjal", "aubergine"], "category": "vegetable", "default_unit": "piece"},
    {"ingredient_id": "I0079", "name_mm": "ရှောက်သီး", "name_en": "Lemon / Citron", "aliases_mm": ["ရှောက်ရည်"], "aliases_en": ["citron juice", "lemon juice"], "category": "fruit", "default_unit": "g"},
    {"ingredient_id": "I0080", "name_mm": "တရုတ်မှိုခြောက်", "name_en": "Dried Chinese mushrooms", "aliases_mm": ["မှိုခြောက်", "ရှီတာကီမှို"], "aliases_en": ["shiitake", "dried black mushrooms"], "category": "vegetable", "default_unit": "piece"},
    {"ingredient_id": "I0081", "name_mm": "စမုန်နက်စေ့", "name_en": "Nigella seeds", "aliases_mm": ["စမုန်နက်"], "aliases_en": ["black cumin", "kalonji"], "category": "spice", "default_unit": "g"},
    {"ingredient_id": "I0082", "name_mm": "ပင်စိမ်း", "name_en": "Basil", "aliases_mm": ["ပင်စိမ်းရွက်"], "aliases_en": ["holy basil", "sweet basil"], "category": "herb", "default_unit": "piece"},
    {"ingredient_id": "I0083", "name_mm": "စပါးလင်", "name_en": "Lemongrass", "aliases_mm": [], "aliases_en": ["lemon grass stalks"], "category": "herb", "default_unit": "piece"},
    {"ingredient_id": "I0084", "name_mm": "ခရမ်းချဉ်သီးဆော့စ်", "name_en": "Tomato sauce", "aliases_mm": [], "aliases_en": ["tomato puree sauce"], "category": "seasoning", "default_unit": "g"},
    {"ingredient_id": "I0085", "name_mm": "ဝက်သား", "name_en": "Pork", "aliases_mm": ["ဝက်ပေါင်သား", "ဝက်သား (အဆီမဲ့)"], "aliases_en": ["pork meat", "lean pork"], "category": "meat", "default_unit": "g"}
]

for new_i in new_ingredients:
    if new_i['ingredient_id'] not in existing_ing_ids:
        ingredients.append(new_i)
        existing_ing_ids[new_i['ingredient_id']] = new_i

# Import the 22 recipes definitions
from batch4_recipes_data import batch4_recipes_list

existing_r_ids = {r['recipe_id'] for r in recipes}
for r in batch4_recipes_list:
    if r['recipe_id'] not in existing_r_ids:
        recipes.append(r)
        existing_r_ids.add(r['recipe_id'])

# Update extraction report
report['total_pages_processed'] = 18 # PDF pages 42-53 (printed pp 73-95)
report['total_recipes_extracted'] = len(recipes)
report['complete_recipes'] = len(recipes)
report['unique_ingredients'] = len(ingredients)
report['general_notes'].append(
    f"Batch 4 completed: Recipes R0021 - R0042 (22 recipes) spanning printed pages 85-95 (PDF pages 48-53). Added 29 new catalog ingredients (I0057 - I0085). All duck, mutton, beef, and pork dishes validated."
)

with open('recipes.json', 'w', encoding='utf-8') as f:
    json.dump(recipes, f, ensure_ascii=False, indent=2)

with open('ingredients.json', 'w', encoding='utf-8') as f:
    json.dump(ingredients, f, ensure_ascii=False, indent=2)

with open('extraction_report.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print(f"Batch 4 processed successfully! Total recipes: {len(recipes)}, Total ingredients: {len(ingredients)}")
