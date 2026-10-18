# -*- coding: utf-8 -*-
"""
Process Batch 4: Recipes R0021 - R0042
Duck, Mutton, Beef, and Pork dishes.
Book pp. 85-95 (PDF pp. 48-53)
"""
import json

with open('recipes.json', 'r', encoding='utf-8') as f:
    recipes = json.load(f)

with open('ingredients.json', 'r', encoding='utf-8') as f:
    ingredients = json.load(f)

with open('extraction_report.json', 'r', encoding='utf-8') as f:
    report = json.load(f)

existing_ing_ids = {i['ingredient_id']: i for i in ingredients}

# Define new catalog ingredients
new_ingredients = [
    {
        "ingredient_id": "I0057",
        "name_mm": "ဘဲသား",
        "name_en": "Duck meat",
        "aliases_mm": ["ဘဲကောင်", "ဘဲအကောင်လိုက်"],
        "aliases_en": ["whole duck", "duck"],
        "category": "meat",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0058",
        "name_mm": "ကြက်သွန်မြိတ်",
        "name_en": "Spring onion",
        "aliases_mm": ["ကြက်သွန်မိတ်", "မိတ်"],
        "aliases_en": ["scallion", "green onion"],
        "category": "vegetable",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0059",
        "name_mm": "စမုန်ပွင့်",
        "name_en": "Star anise",
        "aliases_mm": ["စမုံပွင့်"],
        "aliases_en": ["star aniseed"],
        "category": "spice",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0060",
        "name_mm": "ရှယ်ရီအရက်",
        "name_en": "Cooking wine",
        "aliases_mm": ["အရက်", "တရုတ်ဝိုင်"],
        "aliases_en": ["sherry", "Shaoxing wine", "rice wine"],
        "category": "liquid",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0061",
        "name_mm": "ပဲငါးပိရည်",
        "name_en": "Fermented soybean sauce",
        "aliases_mm": ["ပဲပိစပ်ရည်"],
        "aliases_en": ["brown bean sauce"],
        "category": "seasoning",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0062",
        "name_mm": "မုန်ညင်းစေ့",
        "name_en": "Mustard seeds",
        "aliases_mm": ["မုံညင်းစေ့"],
        "aliases_en": ["yellow mustard seeds", "brown mustard seeds"],
        "category": "spice",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0063",
        "name_mm": "ကော်မှုန့်",
        "name_en": "Tapioca / starch flour",
        "aliases_mm": ["ကော်ရည်"],
        "aliases_en": ["starch powder"],
        "category": "grain",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0064",
        "name_mm": "ဘဲမြစ်",
        "name_en": "Duck gizzard",
        "aliases_mm": ["ဘဲအမြစ်"],
        "aliases_en": ["duck gizzards"],
        "category": "meat",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0065",
        "name_mm": "ငရုတ်စိမ်းပွ",
        "name_en": "Green bell pepper",
        "aliases_mm": ["ငရုတ်ပွစိမ်း", "ငရုတ်ပွ"],
        "aliases_en": ["green capsicum", "sweet pepper"],
        "category": "vegetable",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0066",
        "name_mm": "ကြက်ဆီ",
        "name_en": "Chicken fat",
        "aliases_mm": [],
        "aliases_en": ["rendered chicken fat"],
        "category": "oil",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0067",
        "name_mm": "နှမ်းဆီ",
        "name_en": "Sesame oil",
        "aliases_mm": ["နှမ်းဆီမွှေး"],
        "aliases_en": ["toasted sesame oil"],
        "category": "oil",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0068",
        "name_mm": "ဆိတ်သား",
        "name_en": "Mutton",
        "aliases_mm": ["ဆိတ်သားစဉ်းကော", "ဆိတ်ကီးမား"],
        "aliases_en": ["goat meat", "minced mutton"],
        "category": "meat",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0069",
        "name_mm": "သင်္ဘောသီး",
        "name_en": "Green papaya",
        "aliases_mm": ["သင်္ဘောသီးအကင်း"],
        "aliases_en": ["raw papaya", "young papaya"],
        "category": "fruit",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0070",
        "name_mm": "ငရုတ်ပွခြောက်",
        "name_en": "Dried mild chili",
        "aliases_mm": ["ငရုတ်သီးပွခြောက်"],
        "aliases_en": ["dried sweet chili"],
        "category": "spice",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0071",
        "name_mm": "ဂီးထောပတ်",
        "name_en": "Ghee",
        "aliases_mm": ["ဂီး"],
        "aliases_en": ["clarified butter"],
        "category": "dairy",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0072",
        "name_mm": "မန်ကျည်းသီး",
        "name_en": "Tamarind",
        "aliases_mm": ["မန်ကျည်းရည်", "မန်ကျည်းသီးမှည့်ရည်"],
        "aliases_en": ["tamarind pulp", "tamarind juice"],
        "category": "seasoning",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0073",
        "name_mm": "ဆိတ်ကလီစာ",
        "name_en": "Mutton offal",
        "aliases_mm": [],
        "aliases_en": ["mutton organ meats"],
        "category": "meat",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0074",
        "name_mm": "ပေါင်မုန့်",
        "name_en": "Bread",
        "aliases_mm": ["ပေါင်မုန့်ချပ်"],
        "aliases_en": ["sliced bread", "white bread"],
        "category": "grain",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0075",
        "name_mm": "ပေါင်မုန့်ကြွပ်မှုန့်",
        "name_en": "Breadcrumbs",
        "aliases_mm": ["မုန့်ကြွပ်အမှုန့်", "ပေါင်မုန့်ခြောက်မှုန့်"],
        "aliases_en": ["panko", "dried breadcrumbs"],
        "category": "grain",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0076",
        "name_mm": "အမဲသား",
        "name_en": "Beef",
        "aliases_mm": ["အမဲ", "အမဲစဉ်းကော", "အမဲတင်ပါးသား"],
        "aliases_en": ["minced beef", "beef rump"],
        "category": "meat",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0077",
        "name_mm": "ပဲစိမ်း",
        "name_en": "Green peas",
        "aliases_mm": ["ပဲစိမ်းလုံး"],
        "aliases_en": ["fresh peas", "sweet peas"],
        "category": "legume",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0078",
        "name_mm": "ခရမ်းသီး",
        "name_en": "Eggplant",
        "aliases_mm": ["ခရမ်းသီးရှည်"],
        "aliases_en": ["brinjal", "aubergine"],
        "category": "vegetable",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0079",
        "name_mm": "ရှောက်သီး",
        "name_en": "Lemon / Citron",
        "aliases_mm": ["ရှောက်ရည်"],
        "aliases_en": ["citron juice", "lemon juice"],
        "category": "fruit",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0080",
        "name_mm": "တရုတ်မှိုခြောက်",
        "name_en": "Dried Chinese mushrooms",
        "aliases_mm": ["မှိုခြောက်", "ရှီတာကီမှို"],
        "aliases_en": ["shiitake", "dried black mushrooms"],
        "category": "vegetable",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0081",
        "name_mm": "စမုန်နက်စေ့",
        "name_en": "Nigella seeds",
        "aliases_mm": ["စမုန်နက်"],
        "aliases_en": ["black cumin", "kalonji"],
        "category": "spice",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0082",
        "name_mm": "ပင်စိမ်း",
        "name_en": "Basil",
        "aliases_mm": ["ပင်စိမ်းရွက်"],
        "aliases_en": ["holy basil", "sweet basil"],
        "category": "herb",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0083",
        "name_mm": "စပါးလင်",
        "name_en": "Lemongrass",
        "aliases_mm": [],
        "aliases_en": ["lemon grass stalks"],
        "category": "herb",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0084",
        "name_mm": "ခရမ်းချဉ်သီးဆော့စ်",
        "name_en": "Tomato sauce",
        "aliases_mm": [],
        "aliases_en": ["tomato puree sauce"],
        "category": "seasoning",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0085",
        "name_mm": "ဝက်သား",
        "name_en": "Pork",
        "aliases_mm": ["ဝက်ပေါင်သား", "ဝက်သား (အဆီမဲ့)"],
        "aliases_en": ["pork meat", "lean pork"],
        "category": "meat",
        "default_unit": "g"
    }
]

for new_i in new_ingredients:
    if new_i['ingredient_id'] not in existing_ing_ids:
        ingredients.append(new_i)
        existing_ing_ids[new_i['ingredient_id']] = new_i

# Helper function to generate batch 4 recipes
batch4_recipes = [
    # R0021: ဘဲသားဆီပြန် (Duck Curry)
    {
        "recipe_id": "R0021",
        "name_mm": "ဘဲသားဆီပြန်",
        "name_en": "Duck Curry",
        "description_mm": None,
        "description_en": None,
        "category": "Poultry dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {
                "ingredient_id": "I0057",
                "name_mm": "ဘဲသား",
                "name_en": "Duck meat",
                "original_name": "ဘဲသား",
                "quantity": 80.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၈၀ ကျပ်သား",
                "normalized_quantity": 1306.3,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 3.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၃ လဖဇ",
                "normalized_quantity": 15.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0050",
                "name_mm": "ပဲငံပြာရည်",
                "name_en": "Soy sauce",
                "original_name": "ပဲငံပြာရည် (အကြည်)",
                "quantity": 3.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၃ လဖဇ",
                "normalized_quantity": 15.0,
                "normalized_unit": "g",
                "preparation_note_mm": "အကြည်",
                "preparation_note_en": "light"
            },
            {
                "ingredient_id": "I0050",
                "name_mm": "ပဲငံပြာရည်",
                "name_en": "Soy sauce",
                "original_name": "ပဲငံပြာရည် (အနောက်)",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": "အနောက်",
                "preparation_note_en": "dark"
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 2.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၂ လဖဇ",
                "normalized_quantity": 10.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ငရုတ်သီးခြောက်",
                "name_en": "Dried red chili",
                "original_name": "ငရုတ်သီးခြောက်",
                "quantity": 6.0,
                "unit": "တောင့် (piece)",
                "original_quantity_text": "၆ တောင့်",
                "normalized_quantity": 6.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ထောင်းထားသော",
                "preparation_note_en": "pounded"
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ (အလတ်)",
                "quantity": 4.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၄ လုံး",
                "normalized_quantity": 4.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ထောင်းထားသော",
                "preparation_note_en": "pounded"
            },
            {
                "ingredient_id": "I0014",
                "name_mm": "ကြက်သွန်ဖြူ",
                "name_en": "Garlic",
                "original_name": "ကြက်သွန်ဖြူ",
                "quantity": 5.0,
                "unit": "မြွှာ (piece)",
                "original_quantity_text": "၅ မြွှာ",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ထောင်းထားသော",
                "preparation_note_en": "pounded"
            },
            {
                "ingredient_id": "I0013",
                "name_mm": "ဂျင်း",
                "name_en": "Ginger",
                "original_name": "ချင်း",
                "quantity": 1.0,
                "unit": "လက်မ (piece)",
                "original_quantity_text": "၁ လက်မ",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ထောင်းထားသော",
                "preparation_note_en": "pounded"
            },
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": 10.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၀ ကျပ်သား",
                "normalized_quantity": 163.3,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေနွေး",
                "quantity": None,
                "unit": "အနည်းငယ် (g)",
                "original_quantity_text": "အနည်းငယ်",
                "normalized_quantity": None,
                "normalized_unit": "g",
                "preparation_note_mm": "ရေနွေး",
                "preparation_note_en": "hot water"
            }
        ],
        "servings": 10,
        "preparation_time_minutes": 20,
        "cooking_time_minutes": 45,
        "instructions_mm": [
            "ဘဲသားကို အနေတော်အရွယ်တုံးပြီး ဆား၊ ပဲငံပြာရည် အကြည်၊ အနောက်၊ သကြားတို့ဖြင့် အသားထဲစိမ့်ဝင်အောင် နယ်ထားပါ။",
            "ငရုတ်၊ ကြက်သွန်နီ၊ ကြက်သွန်ဖြူနှင့် ချင်းကို ညက်အောင်ထောင်းထားပါ။",
            "ဆီပူအောင်လုပ်ပြီး ပူလာလျှင် ညက်အောင်ထောင်းထားသည်များထည့်၍ ဆီသတ်ပါ။",
            "ကြက်သွန်နွမ်းလာလျှင် ဘဲသားတုံးများထည့်ပါ။ မွှေပါ။ ဆားထည့်ပါ။ အဖုံးအုပ်ထားပါ။",
            "ရေခမ်း၍ အိုးမှအသံမြည်လာလျှင် ရေနွေးအနည်းငယ်ကို ဘဲသားမြုပ်ရုံထည့်ပါ။",
            "အသားနူး၍ ဆီပြန်လာလျှင် တည်ခင်း၍ရပြီ ဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Cut the duck into medium pieces and marinate with salt, light soy sauce, dark soy sauce, and sugar.",
            "Finely pound the chili, onion, garlic, and ginger into an aromatic paste.",
            "Heat oil in a pot and sauté the pounded aromatic paste until fragrant.",
            "When the aromatics soften, add the marinated duck pieces, stir well, season, and cover.",
            "When the natural juices reduce and sizzle, add hot water just enough to cover the duck.",
            "Simmer until the duck is tender and the oil separates on top, then remove from heat and serve."
        ],
        "tags": {
            "dietary": ["dairy-free"],
            "seasonal": ["all-season"],
            "festival": [],
            "main_ingredients": ["duck"]
        },
        "nutrition": {
            "calories_kcal_per_serving": None,
            "protein_g_per_serving": None,
            "carbohydrates_g_per_serving": None,
            "fat_g_per_serving": None
        },
        "estimated_cost_mmk": None,
        "source": {
            "document": "ဟင်းချက်နည်းများ.pdf",
            "pdf_pages": [48],
            "printed_page_numbers": [85],
            "extraction_method": "manual_transcription_from_scanned_image"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "Printed on page 85 (top). Classic Myanmar duck oil-return curry.",
            "verified": True
        }
    },

    # R0022: အရည်ရွှမ်းဘဲပေါင်း (Succulent Duck)
    {
        "recipe_id": "R0022",
        "name_mm": "အရည်ရွှမ်းဘဲပေါင်း",
        "name_en": "Succulent Steamed Duck",
        "description_mm": None,
        "description_en": None,
        "category": "Poultry dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {
                "ingredient_id": "I0057",
                "name_mm": "ဘဲသား",
                "name_en": "Duck meat",
                "original_name": "ဘဲအကောင်လိုက် (ခပ်ဝဝ)",
                "quantity": 1.0,
                "unit": "ပိဿာ (kg)",
                "original_quantity_text": "၁ ပိဿာ",
                "normalized_quantity": 1632.9,
                "normalized_unit": "g",
                "preparation_note_mm": "အကောင်လိုက် (ခပ်ဝဝ)",
                "preparation_note_en": "whole plump duck"
            },
            {
                "ingredient_id": "I0058",
                "name_mm": "ကြက်သွန်မြိတ်",
                "name_en": "Spring onion",
                "original_name": "ကြက်သွန်မြိတ်",
                "quantity": 1.0,
                "unit": "ပင် (piece)",
                "original_quantity_text": "၁ ပင်",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "၁ လက်မအရှည်ဖြတ်ထားသော",
                "preparation_note_en": "cut into 1-inch lengths"
            },
            {
                "ingredient_id": "I0009",
                "name_mm": "လေးညှင်းပွင့်",
                "name_en": "Clove",
                "original_name": "လေးညှင်း",
                "quantity": 20.0,
                "unit": "ပွင့် (piece)",
                "original_quantity_text": "၂၀ ပွင့်",
                "normalized_quantity": 20.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0013",
                "name_mm": "ဂျင်း",
                "name_en": "Ginger",
                "original_name": "ချင်း",
                "quantity": 4.0,
                "unit": "လွှာ (piece)",
                "original_quantity_text": "၄ လွှာ",
                "normalized_quantity": 4.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0008",
                "name_mm": "သစ်ကြံပိုးခေါက်",
                "name_en": "Cinnamon",
                "original_name": "သစ်ကြံပိုး (၁\" ရှည်)",
                "quantity": 3.0,
                "unit": "ခု (piece)",
                "original_quantity_text": "၃ ခု",
                "normalized_quantity": 3.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "၁\" ရှည်",
                "preparation_note_en": "1-inch length"
            },
            {
                "ingredient_id": "I0059",
                "name_mm": "စမုန်ပွင့်",
                "name_en": "Star anise",
                "original_name": "စမုန်ပွင့်",
                "quantity": 4.0,
                "unit": "ပွင့် (piece)",
                "original_quantity_text": "၄ ပွင့်",
                "normalized_quantity": 4.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0060",
                "name_mm": "ရှယ်ရီအရက်",
                "name_en": "Cooking wine",
                "original_name": "ရှယ်ရီအရက်",
                "quantity": 3.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၃ စပဇ",
                "normalized_quantity": 45.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0061",
                "name_mm": "ပဲငါးပိရည်",
                "name_en": "Fermented soybean sauce",
                "original_name": "ပဲငါးပိရည်",
                "quantity": 5.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၅ စပဇ",
                "normalized_quantity": 75.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 2.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၂ လဖဇ",
                "normalized_quantity": 10.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "မြုပ်အောင်ကြော်ရန်ဆီ လိုအပ်သရွေ့",
                "quantity": None,
                "unit": "လိုအပ်သရွေ့ (as needed)",
                "original_quantity_text": "မြုပ်အောင်ကြော်ရန်ဆီ လိုအပ်သရွေ့",
                "normalized_quantity": None,
                "normalized_unit": "g",
                "preparation_note_mm": "မြုပ်အောင်ကြော်ရန်",
                "preparation_note_en": "for deep frying"
            }
        ],
        "servings": 10,
        "preparation_time_minutes": 180, # 3 hours marinating
        "cooking_time_minutes": 170, # 2.5 hours steaming + 20 mins frying
        "instructions_mm": [
            "ဘဲသားကို ပြင်ဆင်၍ ကျောဘက်မှခွဲချပါ။",
            "၁ လက်မအရှည်ဖြတ်ထားသော ကြက်သွန်မြိတ်၊ လေးညှင်း၊ ချင်းလွှာ၊ သစ်ကြံပိုး၊ စမုန်ပွင့်၊ ရှယ်ရီအရက်၊ ပဲငါးပိရည်နှင့် ဆားတို့ကို ရောစပ်ပြီး ဘဲမျက်နှာပြင်အားလုံးကို လူးနယ်ကာ (၃)နာရီကြာ စိမ့်ဝင်အောင်ထားပါ။",
            "အချိန်စေ့လျှင် စိမ်ပြီးဘဲကို ပေါင်းအိုးတစ်လုံးရှိ အိုးအတွင်း (သို့) အဖုံးပိတ်ထားသောအိုးကြီးအတွင်းရှိ အိုးလေးတွင်ထည့်ပြီး ရေပေါ်တွင်ထား၍ (၂)နာရီခွဲခန့် ပေါင်းပါ။",
            "နူးလာလျှင် ဆီကို အငွေ့ထွက်လာသည်အထိ အပူပေးပြီး ဘဲကို အညိုရောင်သမ်းသည်အထိ ဆီမြုပ်အောင် ကြော်ပါ။",
            "ပြီးလျှင် ဆယ်ယူအအေးခံကာ အလျားလိုက် နှစ်ပိုင်းခြမ်းပြီး ကန့်လန့်ဖြတ်အမြှောင်းများ ပိုင်းဖြတ်ကာ တည်ခင်း၍ရပြီ ဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Clean the duck and butterfly it along the backbone.",
            "Combine 1-inch spring onion pieces, cloves, sliced ginger, cinnamon, star anise, sherry wine, soybean paste sauce, and salt; rub thoroughly over the duck and marinate for 3 hours.",
            "Place the marinated duck in a steamer basket or heatproof bowl inside a covered pot, and steam over simmering water for 2.5 hours until tender.",
            "Once tender, heat oil until shimmering and deep-fry the duck until crisp and deep golden brown.",
            "Drain and let cool slightly, then halve lengthwise, chop crosswise into bite-sized strips, and serve."
        ],
        "tags": {
            "dietary": ["dairy-free"],
            "seasonal": ["all-season"],
            "festival": ["Chinese New Year"],
            "main_ingredients": ["duck"]
        },
        "nutrition": {
            "calories_kcal_per_serving": None,
            "protein_g_per_serving": None,
            "carbohydrates_g_per_serving": None,
            "fat_g_per_serving": None
        },
        "estimated_cost_mmk": None,
        "source": {
            "document": "ဟင်းချက်နည်းများ.pdf",
            "pdf_pages": [48],
            "printed_page_numbers": [85],
            "extraction_method": "manual_transcription_from_scanned_image"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "Printed on page 85 (bottom). Steaming (2.5 hours) followed by deep frying technique recorded.",
            "verified": True
        }
    }
]

# Let's load the remaining batch 4 recipes via a helper file or directly
print("Adding batch 4 recipes R0021-R0022...")
