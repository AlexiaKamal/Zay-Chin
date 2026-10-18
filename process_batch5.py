# -*- coding: utf-8 -*-
import json
from batch5_data_a import BATCH5_RECIPES_A
from batch5_data_b import BATCH5_RECIPES_B

NEW_INGREDIENTS = [
    {
        "ingredient_id": "I0086",
        "name_mm": "ငါးခူ",
        "name_en": "Catfish",
        "aliases_mm": ["ငါးခူသား"],
        "aliases_en": ["walking catfish"],
        "category": "fish_seafood",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0087",
        "name_mm": "ငါးသလောက်",
        "name_en": "Hilsa fish",
        "aliases_mm": ["ငါးသလောက်သား"],
        "aliases_en": ["hilsa", "ilisha"],
        "category": "fish_seafood",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0088",
        "name_mm": "ငါးကြင်း",
        "name_en": "Carp / Rohu",
        "aliases_mm": ["ငါးကြင်းသား"],
        "aliases_en": ["mrigal carp", "rohu"],
        "category": "fish_seafood",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0089",
        "name_mm": "ဆန်အရက်",
        "name_en": "Rice wine",
        "aliases_mm": ["အရက်"],
        "aliases_en": ["cooking rice wine", "shaoxing wine"],
        "category": "condiment",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0090",
        "name_mm": "ငါးဖယ်ခြစ်",
        "name_en": "Scraped featherback fish",
        "aliases_mm": ["ငါးဖယ်", "ငါးဖယ်သား"],
        "aliases_en": ["featherback fish paste", "clown knifefish"],
        "category": "fish_seafood",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0091",
        "name_mm": "နံနံပင်",
        "name_en": "Fresh coriander / cilantro",
        "aliases_mm": ["နံနံ"],
        "aliases_en": ["cilantro", "fresh coriander"],
        "category": "vegetable",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0092",
        "name_mm": "ဝက်အဆီ",
        "name_en": "Pork fat / Lard",
        "aliases_mm": ["ဝက်ဆီ"],
        "aliases_en": ["pork lard", "lard"],
        "category": "meat_poultry",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0093",
        "name_mm": "ပုစွန်",
        "name_en": "Prawn / Shrimp",
        "aliases_mm": ["ပုစွန်အသား", "ပုစွန်ထုပ်", "ပုစွန်ကြား"],
        "aliases_en": ["shrimp", "tiger prawn", "king prawn"],
        "category": "fish_seafood",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0094",
        "name_mm": "မျှစ်",
        "name_en": "Bamboo shoot",
        "aliases_mm": ["မျှစ်ချဉ်", "မျှစ်နုပ်နုပ်စဉ်း"],
        "aliases_en": ["bamboo shoots"],
        "category": "vegetable",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0095",
        "name_mm": "ကဏန်း",
        "name_en": "Crab",
        "aliases_mm": ["ကဏန်းလက်မ", "ကဏန်းသား"],
        "aliases_en": ["mud crab", "crab claws"],
        "category": "fish_seafood",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0096",
        "name_mm": "ဂျင်းဝိုင်",
        "name_en": "Ginger wine",
        "aliases_mm": [],
        "aliases_en": ["ginger cooking wine"],
        "category": "condiment",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0097",
        "name_mm": "အုန်းနို့",
        "name_en": "Coconut milk",
        "aliases_mm": ["အုန်းနို့ဦးရည်", "အုန်းနို့ရည်"],
        "aliases_en": ["thick coconut milk", "coconut cream"],
        "category": "dairy_liquid",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0098",
        "name_mm": "ဆလတ်ရွက်",
        "name_en": "Lettuce",
        "aliases_mm": ["ဆလတ်"],
        "aliases_en": ["salad lettuce"],
        "category": "vegetable",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0099",
        "name_mm": "ရေဂျူ",
        "name_en": "Jellyfish",
        "aliases_mm": ["ရေဂျူသား"],
        "aliases_en": ["edible jellyfish"],
        "category": "fish_seafood",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0100",
        "name_mm": "တရုတ်နံနံ",
        "name_en": "Chinese celery",
        "aliases_mm": ["တရုတ်နံနံပင်"],
        "aliases_en": ["celery"],
        "category": "vegetable",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0101",
        "name_mm": "မြေပဲလှော်",
        "name_en": "Roasted peanuts",
        "aliases_mm": ["မြေပဲဆန်လှော်"],
        "aliases_en": ["peanuts roasted"],
        "category": "nuts_seeds",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0102",
        "name_mm": "သရက်သီးခြောက်",
        "name_en": "Dried mango",
        "aliases_mm": [],
        "aliases_en": ["dry mango slices"],
        "category": "fruit",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0103",
        "name_mm": "သနပ်မဆလာ",
        "name_en": "Pickle masala",
        "aliases_mm": ["သနပ်မဆလာမှုန့်"],
        "aliases_en": ["achar masala"],
        "category": "spice",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0104",
        "name_mm": "သရက်သီးစိမ်း",
        "name_en": "Raw green mango",
        "aliases_mm": ["သရက်သီးအစိမ်း"],
        "aliases_en": ["unripe mango", "green mango"],
        "category": "fruit",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0105",
        "name_mm": "ပဲနံ့သာစေ့",
        "name_en": "Fenugreek seeds",
        "aliases_mm": ["ပဲနံ့သာ"],
        "aliases_en": ["methi seeds"],
        "category": "spice",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0106",
        "name_mm": "သံပရာသီး",
        "name_en": "Lime",
        "aliases_mm": ["သံပရာရည်"],
        "aliases_en": ["lime juice"],
        "category": "fruit",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0107",
        "name_mm": "ဘိန်းစေ့",
        "name_en": "Poppy seeds",
        "aliases_mm": [],
        "aliases_en": ["khus khus"],
        "category": "nuts_seeds",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0108",
        "name_mm": "ပန်းဂေါ်ဖီ",
        "name_en": "Cauliflower",
        "aliases_mm": ["ပန်းဂေါ်ဖီပွင့်"],
        "aliases_en": ["cauliflower florets"],
        "category": "vegetable",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0109",
        "name_mm": "အချဉ်မှုန့်",
        "name_en": "Citric acid / Tartaric acid",
        "aliases_mm": [],
        "aliases_en": ["sour salt", "tartaric acid"],
        "category": "condiment",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0110",
        "name_mm": "ဆိုဒီယမ်ဘင်ဆိုအိတ်",
        "name_en": "Sodium benzoate",
        "aliases_mm": [],
        "aliases_en": ["food preservative"],
        "category": "condiment",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0111",
        "name_mm": "မာလကာသီး",
        "name_en": "Guava",
        "aliases_mm": [],
        "aliases_en": ["guava fruit"],
        "category": "fruit",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0112",
        "name_mm": "လိမ္မော်သီး",
        "name_en": "Orange",
        "aliases_mm": [],
        "aliases_en": ["citrus orange"],
        "category": "fruit",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0113",
        "name_mm": "မုန်ညင်းဆီ",
        "name_en": "Mustard oil",
        "aliases_mm": [],
        "aliases_en": ["mustard seed oil"],
        "category": "oil",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0114",
        "name_mm": "နနွင်း",
        "name_en": "Turmeric powder",
        "aliases_mm": ["နနွင်းမှုန့်", "ဆနွင်း"],
        "aliases_en": ["turmeric", "haldi"],
        "category": "spice",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0115",
        "name_mm": "ငံပြာရည်",
        "name_en": "Fish sauce",
        "aliases_mm": ["ငါးငံပြာရည်"],
        "aliases_en": ["burmese fish sauce"],
        "category": "sauce",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0116",
        "name_mm": "ငရုတ်ချိုဆော့",
        "name_en": "Sweet chili sauce",
        "aliases_mm": ["ငရုတ်ချိုဆော့စ်"],
        "aliases_en": ["sweet chilli sauce"],
        "category": "sauce",
        "default_unit": "g"
    }
]

def main():
    # Load existing ingredients
    with open('ingredients.json', 'r', encoding='utf-8') as f:
        catalog = json.load(f)

    existing_ids = {i['ingredient_id'] for i in catalog}
    for new_ing in NEW_INGREDIENTS:
        if new_ing['ingredient_id'] not in existing_ids:
            catalog.append(new_ing)
            existing_ids.add(new_ing['ingredient_id'])

    with open('ingredients.json', 'w', encoding='utf-8') as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
    print(f"Updated ingredients.json. Total ingredients: {len(catalog)}")

    # Load existing recipes
    with open('recipes.json', 'r', encoding='utf-8') as f:
        recipes = json.load(f)

    existing_recipe_ids = {r['recipe_id'] for r in recipes}
    batch5 = BATCH5_RECIPES_A + BATCH5_RECIPES_B
    added_count = 0
    for r in batch5:
        if r['recipe_id'] not in existing_recipe_ids:
            recipes.append(r)
            existing_recipe_ids.add(r['recipe_id'])
            added_count += 1

    with open('recipes.json', 'w', encoding='utf-8') as f:
        json.dump(recipes, f, ensure_ascii=False, indent=2)
    print(f"Updated recipes.json. Added {added_count} recipes. Total recipes: {len(recipes)}")

    # Update extraction report
    with open('extraction_report.json', 'r', encoding='utf-8') as f:
        report = json.load(f)

    report['total_pages_processed'] = 25  # pp. 42-60 (19 PDF pages + prelims = 25 pages)
    report['total_recipes_extracted'] = len(recipes)
    report['complete_recipes'] = len(recipes)
    report['unique_ingredients'] = len(catalog)
    report['general_notes'].append(
        "Batch 5 completed: Recipes R0043 - R0067 (25 recipes) spanning printed pages 96-107 (PDF pages 54-59). "
        "Added 31 new catalog ingredients (I0086 - I0116). Covers Catfish, Steamed Hilsa, Featherback fish balls, "
        "Fried crab claws, Sweet-sour crab, Stuffed crab shells, Jellyfish salad, Prawn curries, Mango pickles, "
        "Lime pickle, Tamarind pickle, Cauliflower pickle, String bean pickle, Tomato sauce/ketchup, Guava jelly, "
        "Marmalade, and fruit chutneys."
    )

    with open('extraction_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print("Updated extraction_report.json successfully.")

if __name__ == '__main__':
    main()
