# -*- coding: utf-8 -*-
"""
Process Batch 3: Recipes R0011 - R0020
Book pp. 80-84 (PDF pp. 46-48)
"""
import json
import subprocess

# Load existing data
with open('recipes.json', 'r', encoding='utf-8') as f:
    recipes = json.load(f)

with open('ingredients.json', 'r', encoding='utf-8') as f:
    ingredients = json.load(f)

with open('extraction_report.json', 'r', encoding='utf-8') as f:
    report = json.load(f)

existing_ing_ids = {i['ingredient_id']: i for i in ingredients}

# Define new catalog ingredients if any
new_ingredients = [
    {
        "ingredient_id": "I0040",
        "name_mm": "ဘဲဥ",
        "name_en": "Duck egg",
        "aliases_mm": ["ဘဲဥပြုတ်"],
        "aliases_en": ["boiled duck egg"],
        "category": "egg",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0041",
        "name_mm": "ငရုတ်သီးခြောက်",
        "name_en": "Dried red chili",
        "aliases_mm": ["ငရုတ်သီးခြောက်တောင့်", "ငရုတ်သီးခြောက်ထောင်း"],
        "aliases_en": ["pounded dry chili", "dried chili"],
        "category": "spice",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0042",
        "name_mm": "ခရမ်းချဉ်သီး",
        "name_en": "Tomato",
        "aliases_mm": ["ခရမ်းချဉ်သီးမှည့်", "ခမ်းချဉ်သီး"],
        "aliases_en": ["ripe tomato", "fresh tomato"],
        "category": "vegetable",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0043",
        "name_mm": "ဂျုံမှုန့်",
        "name_en": "Wheat flour",
        "aliases_mm": ["ဂျုံ"],
        "aliases_en": ["all-purpose flour", "flour"],
        "category": "grain",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0044",
        "name_mm": "ငရုတ်သီးစိမ်း",
        "name_en": "Green chili",
        "aliases_mm": ["ငရုတ်စိမ်း"],
        "aliases_en": ["fresh green chili"],
        "category": "vegetable",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0045",
        "name_mm": "ခရမ်းချဉ်သီးကက်ချပ်",
        "name_en": "Tomato ketchup",
        "aliases_mm": ["ကက်ချပ်", "ခရမ်းချဉ်သီးဆော့စ်"],
        "aliases_en": ["ketchup", "tomato sauce"],
        "category": "seasoning",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0046",
        "name_mm": "နာနတ်သီး",
        "name_en": "Pineapple",
        "aliases_mm": [],
        "aliases_en": ["fresh pineapple"],
        "category": "fruit",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0047",
        "name_mm": "အရိုးပြုတ်ရည်",
        "name_en": "Bone broth",
        "aliases_mm": ["ပြုတ်ရည်", "အသားပြုတ်ရည်"],
        "aliases_en": ["meat stock", "broth"],
        "category": "liquid",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0048",
        "name_mm": "ပဲငါးပိ",
        "name_en": "Fermented soybean paste",
        "aliases_mm": ["ပဲပိစပ်ငါးပိ"],
        "aliases_en": ["soybean paste", "tauchu"],
        "category": "seasoning",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0049",
        "name_mm": "ရှာလကာရည်",
        "name_en": "Vinegar",
        "aliases_mm": ["ရှာလကာ"],
        "aliases_en": ["white vinegar"],
        "category": "condiment",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0050",
        "name_mm": "ပဲငံပြာရည်",
        "name_en": "Soy sauce",
        "aliases_mm": ["ပဲငံပြာရည်အကြည်", "ပဲငံပြာရည်အနောက်"],
        "aliases_en": ["light soy sauce", "dark soy sauce"],
        "category": "seasoning",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0051",
        "name_mm": "ဂျုံပြောင်းမှုန့်",
        "name_en": "Cornstarch",
        "aliases_mm": ["ပြောင်းမှုန့်", "ပြောင်းဖူးမှုန့်"],
        "aliases_en": ["cornflour", "maize starch"],
        "category": "grain",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0052",
        "name_mm": "သခွားသီး",
        "name_en": "Cucumber",
        "aliases_mm": [],
        "aliases_en": ["fresh cucumber"],
        "category": "vegetable",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0053",
        "name_mm": "ကုလားပဲ",
        "name_en": "Chickpeas",
        "aliases_mm": ["ကုလားပဲခြမ်း", "ပဲဆန်"],
        "aliases_en": ["Bengal gram", "split chickpeas"],
        "category": "legume",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0054",
        "name_mm": "နံနံစေ့",
        "name_en": "Coriander seeds",
        "aliases_mm": ["နံနံစေ့မှုန့်", "နံနံစေ့ထောင်း"],
        "aliases_en": ["ground coriander", "coriander seed"],
        "category": "spice",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0055",
        "name_mm": "ဇီယာ",
        "name_en": "Cumin seeds",
        "aliases_mm": ["ဇီယာစေ့", "ဇီယာထောင်း"],
        "aliases_en": ["cumin", "ground cumin"],
        "category": "spice",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0056",
        "name_mm": "ကြက်အသည်း",
        "name_en": "Chicken liver",
        "aliases_mm": ["ကြက်သည်း"],
        "aliases_en": ["chicken livers"],
        "category": "meat",
        "default_unit": "g"
    }
]

for new_i in new_ingredients:
    if new_i['ingredient_id'] not in existing_ing_ids:
        ingredients.append(new_i)
        existing_ing_ids[new_i['ingredient_id']] = new_i

# Define Batch 3 recipes
batch3_recipes = [
    # R0011: ကြက်ဥခေါက်လိပ်အပွကြော် (Puffy Omelet)
    {
        "recipe_id": "R0011",
        "name_mm": "ကြက်ဥခေါက်လိပ်အပွကြော်",
        "name_en": "Puffy Omelet",
        "description_mm": None,
        "description_en": None,
        "category": "Egg dishes",
        "meal_types": ["breakfast", "lunch", "dinner"],
        "ingredients": [
            {
                "ingredient_id": "I0026",
                "name_mm": "ကြက်ဥ",
                "name_en": "Chicken egg",
                "original_name": "ကြက်ဥ",
                "quantity": 10.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁၀ လုံး",
                "normalized_quantity": 10.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေအေး",
                "quantity": 4.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၄ စပဇ",
                "normalized_quantity": 60.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ရေအေး",
                "preparation_note_en": "cold water"
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": None,
                "unit": "အနည်းငယ် (pinch)",
                "original_quantity_text": "အနည်းငယ်",
                "normalized_quantity": None,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0039",
                "name_mm": "ငရုတ်ကောင်းမှုန့်",
                "name_en": "Ground black pepper",
                "original_name": "ငရုတ်ကောင်း",
                "quantity": None,
                "unit": "အနည်းငယ် (pinch)",
                "original_quantity_text": "အနည်းငယ်",
                "normalized_quantity": None,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": 2.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၂ စပဇ",
                "normalized_quantity": 30.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": 25,
        "instructions_mm": [
            "ကြက်ဥအကာ (၁၀)လုံးကို မာတောင့်လာအောင် ခေါက်ပေးပါ။",
            "ကြက်ဥအနှစ် (၁၀)လုံးကိုမူ ပျစ်၍ လိမ္မော်အရောင်ရလာအောင် ဆားနှင့် ငရုတ်ကောင်းတို့ ထည့်ခေါက်ပါ။",
            "ခေါက်ထားသောကြက်ဥအကာထဲသို့ ထည့်ပါ။",
            "တစီစီ ဆူပွက်နေသော ဆီရှိရာ ဒယ်အိုးထဲသို့ လောင်းထည့်ပါ။",
            "မီးရှိန်ကို လျှော့ချပါ။ အောက်ဘက်တွင် အညိုနုရောင်ရသည်အထိ (၁၀)မိနစ်ခန့် ဖြည်းညင်းစွာ တည်ထားပါ။",
            "မကျက်သေးသော ထိပ်ပိုင်းမှ ပွပွရွရွဖြစ်ပြီး ပူပေါင်းများထနေကာ အရောင်စိုလက်နေဆဲ ရှိပါမည်။",
            "ထိပ်ဖက်တွင် အညိုနုရောင်ရ၍ လက်ချောင်းများနှင့် ဖြည်းဖြည်းဖိနှိပ်ကြည့်သောအခါ လက်ရာထင်မကျန်သည်အထိ (၁၀ မှ ၁၅ မိနစ်ခန့်) ထားရှိပါ။",
            "ဒယ်အိုးလက်ကိုင်နှင့် မျက်နှာချင်းဆိုင်ဘက်အကြား တစ်ဝက်နေရာ၌ ကြက်ဥမွှေကြော်ကို ကန့်လန့်ဖြတ်လျက် ၁/၂\" ခန့်နက်သော အတွန့်ကြောင်းကြီးတစ်ခု ပြုလုပ်ပါ။",
            "အောက်မှ စပက်ကျူလာကောက်တံပြား (သို့) ဓားပြားကို လျှောထည့်၍ အိုးကို ကြက်ဥကြော်များ ကွာကျလာအောင် ခေါက်လှုပ်ပေး၍ မကျိုးပဲစေဘဲ ခေါက်၍ယူပါ။",
            "ပန်းကန်ပေါ်သို့ ကြက်ဥခေါက်ကြော်အပွ အပေါ်ဘက်ခြမ်းကို အောက်ဘက်မှထား၍ လှည့်ထည့်ပါ။"
        ],
        "instructions_en": [
            "Beat the 10 egg whites until stiff peaks form.",
            "Beat the 10 egg yolks with salt and black pepper until thick and pale orange in color.",
            "Gently fold the beaten yolks into the stiff egg whites.",
            "Pour the mixture into a skillet with sizzling hot oil.",
            "Reduce heat and cook gently for about 10 minutes until the underside turns light golden brown.",
            "The uncooked top will remain fluffy and bubbly with a moist, glistening appearance.",
            "Continue cooking for 10 to 15 minutes until the top is lightly browned and springs back without leaving a finger impression when gently pressed.",
            "Cut a shallow score about 1/2-inch deep across the center of the omelet opposite the pan handle.",
            "Slide a spatula or palette knife underneath, gently shake the pan to loosen, and fold the omelet over without breaking it.",
            "Turn and slide the puffy folded omelet onto a serving platter with the upper side down."
        ],
        "tags": {
            "dietary": ["dairy-free", "gluten-free", "pescatarian", "vegetarian"],
            "seasonal": ["all-season"],
            "festival": [],
            "main_ingredients": ["egg"]
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
            "pdf_pages": [46],
            "printed_page_numbers": [80],
            "extraction_method": "manual_transcription_from_scanned_image"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "Printed on page 80 (top). Servings explicitly state (လူ ၁၀ ဦးစာ). Both times (10 mins base + 10-15 mins top) recorded.",
            "verified": True
        }
    },

    # R0012: ဘဲဥဆားစိမ် (Salted Eggs)
    {
        "recipe_id": "R0012",
        "name_mm": "ဘဲဥဆားစိမ်",
        "name_en": "Salted Eggs",
        "description_mm": None,
        "description_en": None,
        "category": "Preserves and pickles",
        "meal_types": ["breakfast", "lunch", "dinner"],
        "ingredients": [
            {
                "ingredient_id": "I0040",
                "name_mm": "ဘဲဥ",
                "name_en": "Duck egg",
                "original_name": "ဘဲဥ",
                "quantity": 10.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁၀ လုံး",
                "normalized_quantity": 10.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 27.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၇ ၁/၂ ကျပ်သား",
                "normalized_quantity": 449.1,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ",
                "quantity": 2.5,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၂ ၁/၂ နို့ဆီဘူး",
                "normalized_quantity": 750.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "servings": 10,
        "preparation_time_minutes": 20160, # 2 weeks curing time
        "cooking_time_minutes": 10,
        "instructions_mm": [
            "ဆားကို ရေထည့်ပြုတ်ပါ။ အအေးခံထားပါ။",
            "ဘဲဥကို အလုံးလိုက်သန့်စင်အောင် ရေဆေးပြီးနောက် သန့်စင်သောမြေအိုး (သို့) မြေခွက်ထဲသို့ထည့်ပါ။",
            "အပေါ်ယံမှနေ၍ ဆားရည်များကို ဘဲဥအလုံးများ ဖုံးအုပ်သွားသည်အထိ မြုပ်အောင်ထည့်ပါ။",
            "နှစ်ပတ်ခန့် စိမ်ထားပြီးလျှင် စားသုံး၍ရပြီဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Dissolve the salt in water by boiling, then allow the brine to cool completely.",
            "Wash the whole duck eggs thoroughly and place them into a clean earthenware pot or jar.",
            "Pour the cooled brine over the duck eggs until they are completely submerged.",
            "Leave to cure for about two weeks, after which the salted eggs are ready to consume."
        ],
        "tags": {
            "dietary": ["dairy-free", "gluten-free", "pescatarian", "vegetarian"],
            "seasonal": ["all-season"],
            "festival": [],
            "main_ingredients": ["duck egg", "salt"]
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
            "pdf_pages": [46],
            "printed_page_numbers": [80],
            "extraction_method": "manual_transcription_from_scanned_image"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "Printed on page 80 (bottom). Curing duration explicitly states two weeks (နှစ်ပတ်ခန့်).",
            "verified": True
        }
    },

    # R0013: ဘဲဥဟင်း (Duck Eggs Curry)
    {
        "recipe_id": "R0013",
        "name_mm": "ဘဲဥဟင်း",
        "name_en": "Duck Eggs Curry",
        "description_mm": None,
        "description_en": None,
        "category": "Egg dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
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
                "ingredient_id": "I0024",
                "name_mm": "နနွင်းမှုန့်",
                "name_en": "Turmeric powder",
                "original_name": "နနွင်း",
                "quantity": 0.5,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁/၂ လဖဇ",
                "normalized_quantity": 2.5,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ငရုတ်သီးခြောက်",
                "name_en": "Dried red chili",
                "original_name": "ငရုတ်သီးခြောက် (ထောင်းပြီး)",
                "quantity": 2.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၂ စပဇ",
                "normalized_quantity": 30.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ထောင်းပြီး",
                "preparation_note_en": "pounded"
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ (ထောင်းပြီး)",
                "quantity": 3.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၃ စပဇ",
                "normalized_quantity": 45.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ထောင်းပြီး",
                "preparation_note_en": "pounded"
            },
            {
                "ingredient_id": "I0042",
                "name_mm": "ခရမ်းချဉ်သီး",
                "name_en": "Tomato",
                "original_name": "ခရမ်းချဉ်သီး (လှီးပြီး)",
                "quantity": 1.0,
                "unit": "ခွက် (cup / g)",
                "original_quantity_text": "၁ ခွက်",
                "normalized_quantity": 240.0,
                "normalized_unit": "g",
                "preparation_note_mm": "လှီးပြီး",
                "preparation_note_en": "sliced"
            },
            {
                "ingredient_id": "I0040",
                "name_mm": "ဘဲဥ",
                "name_en": "Duck egg",
                "original_name": "ဘဲဥ (ပြုတ်ပြီး)",
                "quantity": 10.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁၀ လုံး",
                "normalized_quantity": 10.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ပြုတ်ပြီး",
                "preparation_note_en": "boiled"
            },
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေနွေး (ဆူဆူ)",
                "quantity": 1.0,
                "unit": "ခွက် (cup / g)",
                "original_quantity_text": "၁ ခွက်",
                "normalized_quantity": 240.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ဆူဆူ",
                "preparation_note_en": "boiling hot"
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
                "ingredient_id": "I0030",
                "name_mm": "ငံပြာရည်",
                "name_en": "Fish sauce",
                "original_name": "ငံပြာရည်",
                "quantity": 2.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၂ လဖဇ",
                "normalized_quantity": 10.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0031",
                "name_mm": "နံနံပင်",
                "name_en": "Coriander",
                "original_name": "နံနံပင်",
                "quantity": 3.0,
                "unit": "ပင် (piece)",
                "original_quantity_text": "၃ ပင်",
                "normalized_quantity": 3.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "servings": 10,
        "preparation_time_minutes": 15,
        "cooking_time_minutes": 20,
        "instructions_mm": [
            "ဆီပူအောင်တည်ပြီး နနွင်း၊ ငရုတ်သီး၊ ကြက်သွန်နီ ထည့်ဆီသတ်ပါ။",
            "ကြက်သွန်နွမ်းလျှင် ခရမ်းချဉ်သီးထည့်မွှေပါ။",
            "ဘဲဥပြုတ်ကို အပ်ချည်ကြိုးဖြင့် ထက်ခြမ်းခွဲပါ။",
            "ခရမ်းချဉ်သီးဆီပြန်လာလျှင် ရေနွေးဆူဆူကို ထည့်ပြီး ဆား၊ ငံပြာရည် ရော၍မွှေပါ။",
            "ပြီးလျှင် ဘဲဥခြမ်းများထည့်ပါ။",
            "(၅)မိနစ်ကြာလျှင် နံနံပင်အုပ်ကာ ဖိုမှချပြီးလျှင် တည်ခင်း၍ရပြီဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Heat the cooking oil and sauté the turmeric, pounded dry chili, and pounded onion until fragrant.",
            "When the onions soften, add the sliced tomatoes and stir well.",
            "Slice the boiled duck eggs cleanly in half using a thread.",
            "Once the tomatoes break down and the oil separates, add boiling water, salt, and fish sauce, stirring to combine.",
            "Add the halved duck eggs into the simmering curry sauce.",
            "After simmering for 5 minutes, garnish with fresh coriander, remove from heat, and serve."
        ],
        "tags": {
            "dietary": ["dairy-free", "gluten-free", "pescatarian"],
            "seasonal": ["all-season"],
            "festival": [],
            "main_ingredients": ["duck egg", "tomato"]
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
            "pdf_pages": [46],
            "printed_page_numbers": [81],
            "extraction_method": "manual_transcription_from_scanned_image"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "Printed on page 81 (top). Thread-slicing method for boiled eggs preserved.",
            "verified": True
        }
    },

    # R0014: အသားနှင့်ဘဲဥခေါက်လိပ်ကြော် (Mini Omelet with Minced Meat)
    {
        "recipe_id": "R0014",
        "name_mm": "အသားနှင့်ဘဲဥခေါက်လိပ်ကြော်",
        "name_en": "Mini Omelet with Minced Meat",
        "description_mm": None,
        "description_en": None,
        "category": "Egg dishes",
        "meal_types": ["breakfast", "lunch", "dinner"],
        "ingredients": [
            {
                "ingredient_id": "I0040",
                "name_mm": "ဘဲဥ",
                "name_en": "Duck egg",
                "original_name": "ဘဲဥ",
                "quantity": 5.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၅ လုံး",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0037",
                "name_mm": "ဝက်သားနုပ်နုပ်စဉ်း",
                "name_en": "Minced pork",
                "original_name": "ဝက်သား (နုပ်နုပ်စဉ်း)",
                "quantity": 15.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၅ ကျပ်သား",
                "normalized_quantity": 245.0,
                "normalized_unit": "g",
                "preparation_note_mm": "နုပ်နုပ်စဉ်း",
                "preparation_note_en": "finely minced"
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ (နုပ်နုပ်စဉ်း)",
                "quantity": 3.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၃ လုံး",
                "normalized_quantity": 3.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "နုပ်နုပ်စဉ်း",
                "preparation_note_en": "finely minced"
            },
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": 10.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁၀ စပဇ",
                "normalized_quantity": 150.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0039",
                "name_mm": "ငရုတ်ကောင်းမှုန့်",
                "name_en": "Ground black pepper",
                "original_name": "ငရုတ်ကောင်း",
                "quantity": 0.5,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁/၂ လဖဇ",
                "normalized_quantity": 2.5,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "servings": 10,
        "preparation_time_minutes": 15,
        "cooking_time_minutes": 15,
        "instructions_mm": [
            "ဒယ်အိုးတွင် ဆီ(၁)စားပွဲဇွန်းထည့်ကာ ကြက်သွန်နီကို ဖွဖွလေးကြော်ပါ။",
            "ဝက်သားပါ ရောထည့်၍ (၁)မိနစ်ခန့် ကြော်ပါ။ မီးလျှော့လိုက်ပါ။",
            "ဘဲဥကို ခေါက်ပြီး ဝက်သား၊ ဆား၊ ငရုတ်ကောင်း ရောမွှေပါ။",
            "ဒယ်အိုးကို အပူပြန်ပေးပြီး ဖြန့်ထည့်ပါ။",
            "ဒယ်အိုးနှင့်ကပ်လျက် အောက်ခြေအသားများ ရွှေဝါရောင်သမ်းလာလျှင် တစ်ဖက်မှနေ၍ ခေါက်၍ခေါက်လိုက်ကာ ဆယ်ယူပါ။",
            "ဤနည်းအတိုင်း ကျန်အရောများကို ဆက်၍ ကြော်သွားရပါမည်။",
            "ပြီးလျှင် တည်ခင်း၍ရပြီဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Heat 1 tablespoon of cooking oil in a skillet and gently sauté the finely minced onion.",
            "Add the minced pork and fry for about 1 minute, then reduce the heat.",
            "Beat the duck eggs and thoroughly blend in the cooked pork, salt, and black pepper.",
            "Reheat the skillet with oil and pour in a portion of the mixture, spreading evenly.",
            "When the underside touching the skillet turns golden yellow, roll and fold the omelet carefully from one edge, then remove from pan.",
            "Repeat this procedure with the remaining batter to make batch omelet rolls.",
            "Once all rolls are cooked, arrange on a serving dish and serve."
        ],
        "tags": {
            "dietary": ["dairy-free", "gluten-free"],
            "seasonal": ["all-season"],
            "festival": [],
            "main_ingredients": ["duck egg", "pork"]
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
            "pdf_pages": [46],
            "printed_page_numbers": [81],
            "extraction_method": "manual_transcription_from_scanned_image"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "Printed on page 81 (bottom). Original English subtitle 'MINI OMELET WITH MINCED MEAT' preserved.",
            "verified": True
        }
    },

    # R0015: ကြက်သားချိုချဉ်ကြော် (Sweet & Sour Fried Chicken)
    {
        "recipe_id": "R0015",
        "name_mm": "ကြက်သားချိုချဉ်ကြော်",
        "name_en": "Sweet and Sour Fried Chicken",
        "description_mm": None,
        "description_en": None,
        "category": "Poultry dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": 40.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၄၀ ကျပ်သား",
                "normalized_quantity": 653.2,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0028",
                "name_mm": "ကြက်သား",
                "name_en": "Chicken",
                "original_name": "ကြက်ရင်အုပ်သား",
                "quantity": 25.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၅ ကျပ်သား",
                "normalized_quantity": 408.2,
                "normalized_unit": "g",
                "preparation_note_mm": "ရင်အုပ်သား",
                "preparation_note_en": "chicken breast"
            },
            {
                "ingredient_id": "I0043",
                "name_mm": "ဂျုံမှုန့်",
                "name_en": "Wheat flour",
                "original_name": "ဂျုံမှုန့် (ဖုံးအုပ်ရန်)",
                "quantity": None,
                "unit": "အနည်းငယ် (g)",
                "original_quantity_text": "အနည်းငယ်",
                "normalized_quantity": None,
                "normalized_unit": "g",
                "preparation_note_mm": "ဖုံးအုပ်ရန်",
                "preparation_note_en": "for dusting / coating"
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ (လှီးပြီး)",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "လှီးပြီး",
                "preparation_note_en": "sliced"
            },
            {
                "ingredient_id": "I0044",
                "name_mm": "ငရုတ်သီးစိမ်း",
                "name_en": "Green chili",
                "original_name": "ငရုတ်သီးစိမ်း (လှီးပြီး)",
                "quantity": 1.0,
                "unit": "တောင့် (piece)",
                "original_quantity_text": "၁ တောင့်",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "လှီးပြီး",
                "preparation_note_en": "sliced"
            },
            {
                "ingredient_id": "I0045",
                "name_mm": "ခရမ်းချဉ်သီးကက်ချပ်",
                "name_en": "Tomato ketchup",
                "original_name": "ခရမ်းချဉ်သီးကက်ချပ်",
                "quantity": 0.5,
                "unit": "ခွက် (cup / g)",
                "original_quantity_text": "၁/၂ ခွက်",
                "normalized_quantity": 120.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0042",
                "name_mm": "ခရမ်းချဉ်သီး",
                "name_en": "Tomato",
                "original_name": "ခမ်းချဉ်သီးမှည့် (အနေတော်လှီး)",
                "quantity": 3.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၃ လုံး",
                "normalized_quantity": 3.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အနေတော်လှီး",
                "preparation_note_en": "medium sliced"
            },
            {
                "ingredient_id": "I0046",
                "name_mm": "နာနတ်သီး",
                "name_en": "Pineapple",
                "original_name": "နာနတ်သီး (အနေတော်လှီးပြီး)",
                "quantity": 0.25,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁/၄ လုံး",
                "normalized_quantity": 0.25,
                "normalized_unit": "piece",
                "preparation_note_mm": "အနေတော်လှီးပြီး",
                "preparation_note_en": "medium sliced"
            },
            {
                "ingredient_id": "I0047",
                "name_mm": "အရိုးပြုတ်ရည်",
                "name_en": "Bone broth",
                "original_name": "အရိုးပြုတ်ရည်",
                "quantity": 0.5,
                "unit": "ခွက် (cup / g)",
                "original_quantity_text": "၁/၂ ခွက်",
                "normalized_quantity": 120.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0048",
                "name_mm": "ပဲငါးပိ",
                "name_en": "Fermented soybean paste",
                "original_name": "ပဲငါးပိ",
                "quantity": 2.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၂ လဖဇ",
                "normalized_quantity": 10.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0049",
                "name_mm": "ရှာလကာရည်",
                "name_en": "Vinegar",
                "original_name": "ရှာလကာရည်",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "servings": 10,
        "preparation_time_minutes": 20,
        "cooking_time_minutes": 15,
        "instructions_mm": [
            "ဒယ်အိုးတွင် ဆီပူအောင်အလျင်လုပ်ပါ။",
            "၃/၄ လက်မအရွယ် ကြက်သားတုံးပြီး ဂျုံမှုန့်ဖြင့် ခပ်ဖွဖွနယ်ကာ ရွှေရောင်သမ်းရုံကလေးကြော်ပါ။",
            "(၅)မိနစ်မျှကြော်ပြီးလျှင် ဆယ်ယူကာ ဆီစစ်ထားပါ။",
            "လက်ကျန်ဆီပူထဲမှ ၃ စားခန့်သာ ချန်ထားပြီးကျန်ဆီများကို အိုးမှဖယ်ထုတ်ပါ။",
            "ကြက်သွန်နီနှင့် ငရုတ်သီးစိမ်းများကို ထည့်ပြီး (၁)မိနစ်ကြော်ပါ။",
            "ခရမ်းချဉ်သီးကက်ချပ် (စာ-၁၀၅မှ)ရောစပ်ပါ။",
            "ခရမ်းချဉ်သီး၊ နာနတ်သီး၊ အရိုးပြုတ်ရည်၊ ပဲငါးပိ၊ သကြား၊ ရှာလကာရည် ထည့်မွှေပါ။",
            "ပြီးမှ ကြက်သားထည့်ကာ ကြက်သွန်နီ နူးသည်အထိ (၂)မိနစ်ခန့် ဆက်ချက်လျှင် တည်ခင်း၍ ရပြီ ဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "First, thoroughly heat the cooking oil in a deep skillet or wok.",
            "Cut the chicken breast into 3/4-inch cubes, dust lightly with wheat flour, and fry until lightly golden.",
            "After frying for about 5 minutes, remove the chicken cubes and drain well.",
            "Retain about 3 tablespoons of hot oil in the pan and pour off the rest.",
            "Add the sliced onion and green chili, stir-frying for 1 minute.",
            "Stir in the tomato ketchup (prepared according to page 105).",
            "Add ripe tomato slices, pineapple chunks, bone broth, fermented soybean paste, sugar, and vinegar, stirring well to create the sauce.",
            "Finally add the fried chicken pieces and cook for about 2 minutes until the onions soften, then remove from heat and serve."
        ],
        "tags": {
            "dietary": ["dairy-free"],
            "seasonal": ["all-season"],
            "festival": [],
            "main_ingredients": ["chicken", "pineapple", "tomato"]
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
            "pdf_pages": [47],
            "printed_page_numbers": [82],
            "extraction_method": "manual_transcription_from_scanned_image"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "Printed on page 82 (top). Author references homemade tomato ketchup formula on book page 105.",
            "verified": True
        }
    },

    # R0016: ကြက်သားကြော် (Fried Chicken)
    {
        "recipe_id": "R0016",
        "name_mm": "ကြက်သားကြော်",
        "name_en": "Fried Chicken",
        "description_mm": None,
        "description_en": None,
        "category": "Poultry dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {
                "ingredient_id": "I0028",
                "name_mm": "ကြက်သား",
                "name_en": "Chicken",
                "original_name": "ကြက်ရင်အုပ်",
                "quantity": 60.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၆၀ ကျပ်သား",
                "normalized_quantity": 979.8,
                "normalized_unit": "g",
                "preparation_note_mm": "ရင်အုပ်သား",
                "preparation_note_en": "chicken breast"
            },
            {
                "ingredient_id": "I0050",
                "name_mm": "ပဲငံပြာရည်",
                "name_en": "Soy sauce",
                "original_name": "ပဲငံပြာရည်",
                "quantity": 3.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၃ စပဇ",
                "normalized_quantity": 45.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0049",
                "name_mm": "ရှာလကာရည်",
                "name_en": "Vinegar",
                "original_name": "ရှာလကာရည်",
                "quantity": 2.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၂ စပဇ",
                "normalized_quantity": 30.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0013",
                "name_mm": "ဂျင်း",
                "name_en": "Ginger",
                "original_name": "ချင်း (၁\")",
                "quantity": 1.0,
                "unit": "တုံး (piece)",
                "original_quantity_text": "၁ တုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ကြိတ်ခြေထားသည့်",
                "preparation_note_en": "crushed"
            },
            {
                "ingredient_id": "I0051",
                "name_mm": "ဂျုံပြောင်းမှုန့်",
                "name_en": "Cornstarch",
                "original_name": "ဂျုံပြောင်းမှုန့်",
                "quantity": 10.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁၀ စပဇ",
                "normalized_quantity": 150.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0052",
                "name_mm": "သခွားသီး",
                "name_en": "Cucumber",
                "original_name": "သခွားသီး",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "တွဲဖက်အဖြစ်",
                "preparation_note_en": "for garnish / side"
            },
            {
                "ingredient_id": "I0042",
                "name_mm": "ခရမ်းချဉ်သီး",
                "name_en": "Tomato",
                "original_name": "ခရမ်းချဉ်သီး",
                "quantity": 3.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၃ လုံး",
                "normalized_quantity": 3.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "တွဲဖက်အဖြစ်",
                "preparation_note_en": "for garnish / side"
            },
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "မြုပ်အောင်ကြော်ရန် ဆီလိုအပ်သရွေ့",
                "quantity": None,
                "unit": "လိုအပ်သရွေ့ (as needed)",
                "original_quantity_text": "မြုပ်အောင်ကြော်ရန် ဆီလိုအပ်သရွေ့",
                "normalized_quantity": None,
                "normalized_unit": "g",
                "preparation_note_mm": "မြုပ်အောင်ကြော်ရန်",
                "preparation_note_en": "for deep frying"
            }
        ],
        "servings": 10,
        "preparation_time_minutes": 120, # 2 hours marinating
        "cooking_time_minutes": 20,
        "instructions_mm": [
            "ကြက်သားကိုအတုံးကြီးတုံးကာ ပဲငံပြာရည်၊ သကြား၊ ရှာလကာရည်နှင့် ကြိတ်ခြေထားသည့်ချင်းတို့ဖြင့် (၂)နာရီကြာ စိမ့်ဝင်သွားအောင်စိမ်ထားပါ။",
            "မကြာခဏ ကြက်သားတုံးများကို စိမ်ရည်အတွင်း တစ်ဖက်စီလှည့်ပေးပါ။ ကြက်သားအတုံးအားလုံး အရည်များစိမ့်ဝင်နေပါစေ။",
            "ပြောင်းမှုန့်နှင့် ကြက်သားတုံးများကို အုပ်ပြီးနောက် ဆီများများတွင်မြုပ်အောင် ထည့်၍ကြော်ပါ။",
            "တွဲဖက်အဖြစ်- လှီးစိတ်ထားသော သခွားသီး၊ ခရမ်းချဉ်သီးတို့ဖြင့် တည်ခင်း၍ရပြီဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Cut the chicken into large pieces and marinate for 2 hours in a mixture of soy sauce, sugar, vinegar, and crushed ginger.",
            "Turn the chicken pieces frequently in the marinade to ensure every piece is thoroughly permeated with flavor.",
            "Thoroughly dredge the marinated chicken pieces in cornstarch and deep-fry in plenty of hot oil until golden and crisp.",
            "Serve garnished with sliced cucumbers and fresh tomato wedges."
        ],
        "tags": {
            "dietary": ["dairy-free"],
            "seasonal": ["all-season"],
            "festival": [],
            "main_ingredients": ["chicken"]
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
            "pdf_pages": [47],
            "printed_page_numbers": [82],
            "extraction_method": "manual_transcription_from_scanned_image"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "Printed on page 82 (bottom). 2-hour marinade specified in original text.",
            "verified": True
        }
    },

    # R0017: ကြက်သားကုလားပဲဟင်း (Chicken with Chick Pea Curry)
    {
        "recipe_id": "R0017",
        "name_mm": "ကြက်သားကုလားပဲဟင်း",
        "name_en": "Chicken with Chickpea Curry",
        "description_mm": None,
        "description_en": None,
        "category": "Poultry dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": 40.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၄၀ ကျပ်သား",
                "normalized_quantity": 653.2,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ (ပါးပါးလှီး)",
                "quantity": 4.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၄ လုံး",
                "normalized_quantity": 4.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ပါးပါးလှီး",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0014",
                "name_mm": "ကြက်သွန်ဖြူ",
                "name_en": "Garlic",
                "original_name": "ကြက်သွန်ဖြူ",
                "quantity": 4.0,
                "unit": "မြွှာ (piece)",
                "original_quantity_text": "၄ မြွှာ",
                "normalized_quantity": 4.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0025",
                "name_mm": "ငရုတ်သီးမှုန့်",
                "name_en": "Chili powder",
                "original_name": "ငရုတ်သီးမှုန့်",
                "quantity": 1.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁ ကျပ်သား",
                "normalized_quantity": 16.3,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0028",
                "name_mm": "ကြက်သား",
                "name_en": "Chicken",
                "original_name": "ကြက်သား",
                "quantity": 60.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၆၀ ကျပ်သား",
                "normalized_quantity": 979.8,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0024",
                "name_mm": "နနွင်းမှုန့်",
                "name_en": "Turmeric powder",
                "original_name": "နနွင်း",
                "quantity": 0.5,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁/၂ လဖဇ",
                "normalized_quantity": 2.5,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0013",
                "name_mm": "ဂျင်း",
                "name_en": "Ginger",
                "original_name": "ချင်း (၁\") အတုံး (ထောင်းပြီး)",
                "quantity": 3.0,
                "unit": "လွှာ (piece)",
                "original_quantity_text": "၃ လွှာ",
                "normalized_quantity": 3.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ထောင်းပြီး",
                "preparation_note_en": "pounded"
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 2.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ကျပ်သား",
                "normalized_quantity": 32.7,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0034",
                "name_mm": "ကရဝေးရွက်",
                "name_en": "Bay leaf",
                "original_name": "ကရဝေးရွက်",
                "quantity": 4.0,
                "unit": "ရွက် (piece)",
                "original_quantity_text": "၄ ရွက်",
                "normalized_quantity": 4.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0053",
                "name_mm": "ကုလားပဲ",
                "name_en": "Chickpeas",
                "original_name": "ကုလားပဲ",
                "quantity": 10.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၀ ကျပ်သား",
                "normalized_quantity": 163.3,
                "normalized_unit": "g",
                "preparation_note_mm": "တစ်ည ရေစိမ်ထားသော",
                "preparation_note_en": "soaked overnight"
            },
            {
                "ingredient_id": "I0012",
                "name_mm": "မဆလာ",
                "name_en": "Garam masala",
                "original_name": "မဆလာ",
                "quantity": 2.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၂ လဖဇ",
                "normalized_quantity": 10.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "servings": 10,
        "preparation_time_minutes": 480, # overnight chickpea soaking
        "cooking_time_minutes": 45,
        "instructions_mm": [
            "ကြက်သွန်နီတစ်ဝက်၊ ကြက်သွန်ဖြူ၊ ငရုတ်သီးမှုန့်နှင့် မဆလာတို့ကို ရောထောင်းထားပါ။",
            "ဆီပူတွင် ကျန်ကြက်သွန်နီကိုကြော်ကာ ဆီစစ်ပြီးဖယ်ထားပါ။",
            "အရွယ်ညီ တုံးတစ်ထားသည့် ကြက်သားကို နနွင်း၊ ချင်း၊ ဆား တစ်ဝက်တို့ဖြင့် နှံ့နှံ့စပ်စပ် နယ်ပေးပါ။",
            "ဆီအိုးပြန်တည်ကာ ကရဝေးကို ဆီသတ်ပါ။ ရနံ့ထွက်လာလျှင် ထောင်းထားသည်များထည့်၍ မွှေပေးပါ။",
            "ဟင်းခတ်အမွှေးအကြိုင်များ နွမ်းလာလျှင် ကြက်သားထည့်ပါ။ အသာအယာမွှေပေးပြီး ခေတ္တအဖုံးအုပ်ထားပါ။",
            "မီးမှန်မှန်ဖြင့် ရေခမ်းအောင်တည်ပါ။ ရေခမ်းပြီး အသားများ ကျစ်လာလျှင် လက်ကျန်ဆားနှင့် ရေနွေး (၁)ခွက်ခန့် ရောထည့်ပါ။",
            "ကြက်သွန်ကြော်ထည့်ပါ။ တစ်ည ရေစိမ်ထားသော ပဲဆန်များ နူးအောင်ပြုတ်ပြီးထည့်ပါ။ အဖုံးအုပ်ပြီး မီးအေးအေးဖြင့်ချက်ပါ။",
            "ရေခမ်းပြီး ဆီပြန်လာလျှင် အသားနှင့်ပဲများ နူး မနူးစမ်းကြည့်ပါ။ မနူးသေးလျှင် ရေနွေးအနည်းငယ် ထပ်ထည့်၍ ဆက်တည်ပါ။",
            "နူး၍ဆီပြန်လာလျှင် မဆလာမွှေးအုပ်ကာ အဖုံးဖုံးထားပြီးမှ ဖိုမှချကာ တည်ခင်း၍ရပြီဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Pound half of the sliced onions, garlic, chili powder, and half the garam masala into a spice paste.",
            "Fry the remaining sliced onions in hot oil until golden crisp, then drain and set aside.",
            "Cut the chicken into uniform pieces and marinate thoroughly with turmeric, pounded ginger, and half of the salt.",
            "Reheat the oil, sauté the bay leaves until fragrant, then add the pounded spice paste and stir well.",
            "When the aromatics soften and release fragrance, add the chicken pieces, stir gently, and cover briefly.",
            "Cook over steady heat until the chicken juices evaporate; once the chicken firms, add the remaining salt and about 1 cup of boiling water.",
            "Add the crisp fried onions and pre-boiled tender chickpeas (soaked overnight); cover tightly and simmer over low heat.",
            "When the water evaporates and oil returns, check for tenderness; if needed, add a splash of warm water and continue simmering.",
            "Once both chicken and chickpeas are tender with aromatic oil floating on top, sprinkle with fragrant garam masala, cover to rest, remove from heat, and serve."
        ],
        "tags": {
            "dietary": ["dairy-free", "gluten-free"],
            "seasonal": ["all-season"],
            "festival": [],
            "main_ingredients": ["chicken", "chickpea"]
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
            "pdf_pages": [47],
            "printed_page_numbers": [83],
            "extraction_method": "manual_transcription_from_scanned_image"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "Printed on page 83 (top). Overnight soaking of chickpeas documented.",
            "verified": True
        }
    },

    # R0018: ကြက်သားခပတ်ကင် (Barbecued Chicken Kebabs)
    {
        "recipe_id": "R0018",
        "name_mm": "ကြက်သားခပတ်ကင်",
        "name_en": "Barbecued Chicken Kebabs",
        "description_mm": None,
        "description_en": None,
        "category": "Poultry dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {
                "ingredient_id": "I0028",
                "name_mm": "ကြက်သား",
                "name_en": "Chicken",
                "original_name": "ကြက်ပေါင်သား",
                "quantity": 50.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅၀ ကျပ်သား",
                "normalized_quantity": 816.5,
                "normalized_unit": "g",
                "preparation_note_mm": "ပေါင်သား",
                "preparation_note_en": "chicken thigh"
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ (ဥကြီး)",
                "quantity": 1.0,
                "unit": "ဥ (piece)",
                "original_quantity_text": "၁ ဥ",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ဥကြီး",
                "preparation_note_en": "large bulb"
            },
            {
                "ingredient_id": "I0014",
                "name_mm": "ကြက်သွန်ဖြူ",
                "name_en": "Garlic",
                "original_name": "ကြက်သွန်ဖြူ",
                "quantity": 2.0,
                "unit": "မြွှာ (piece)",
                "original_quantity_text": "၂ မြွှာ",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0013",
                "name_mm": "ဂျင်း",
                "name_en": "Ginger",
                "original_name": "ချင်း (၁\") အတုံး",
                "quantity": 5.0,
                "unit": "လွှာ (piece)",
                "original_quantity_text": "၅ လွှာ",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0033",
                "name_mm": "သံပရာသီး",
                "name_en": "Lime",
                "original_name": "သံပရာသီး (အရည်ညှစ်)",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အရည်ညှစ်",
                "preparation_note_en": "juiced"
            },
            {
                "ingredient_id": "I0054",
                "name_mm": "နံနံစေ့",
                "name_en": "Coriander seeds",
                "original_name": "နံနံစေ့ (ထောင်းပြီး)",
                "quantity": 2.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၂ လဖဇ",
                "normalized_quantity": 10.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ထောင်းပြီး",
                "preparation_note_en": "pounded"
            },
            {
                "ingredient_id": "I0055",
                "name_mm": "ဇီယာ",
                "name_en": "Cumin seeds",
                "original_name": "ဇီယာ (ထောင်းပြီး)",
                "quantity": 2.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၂ လဖဇ",
                "normalized_quantity": 10.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ထောင်းပြီး",
                "preparation_note_en": "pounded"
            },
            {
                "ingredient_id": "I0012",
                "name_mm": "မဆလာ",
                "name_en": "Garam masala",
                "original_name": "မဆလာ",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0029",
                "name_mm": "ဒိန်ချဉ်",
                "name_en": "Curd",
                "original_name": "ဒိန်ချဉ်",
                "quantity": 0.5,
                "unit": "ခွက် (cup / g)",
                "original_quantity_text": "၁/၂ ခွက်",
                "normalized_quantity": 120.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0032",
                "name_mm": "ပူဒီနာ",
                "name_en": "Mint",
                "original_name": "ပူဒီနာရွက် (ထောင်းပြီး)",
                "quantity": 2.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၂ လဖဇ",
                "normalized_quantity": 10.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ထောင်းပြီး",
                "preparation_note_en": "pounded"
            }
        ],
        "servings": 10,
        "preparation_time_minutes": 120, # 2 hours marinating
        "cooking_time_minutes": 20,
        "instructions_mm": [
            "ကြက်ပေါင်တွင်ရှိသော အရေခွံနှင့် အဆီများကို ဖယ်ရှားကာ တစ်ကိုက်စာအရွယ်အတုံးများလှီးဖြတ်ပါ။",
            "ကြက်သွန်နီ၊ ကြက်သွန်ဖြူနှင့် ချင်းတို့ကို ညက်အောင်ထောင်းထားပါ။",
            "၎င်းတို့ကို ခွက်တစ်ခုတွင်ထည့်၍ သံပရာရည် ရောစပ်ပါ။ အမွှေးအကြိုင်များ၊ ဒိန်ချဉ်၊ ဆားနှင့် ပူဒီနာရွက်တို့ကိုပါ ရောစပ်ပါ။",
            "၎င်းအရောများထဲသို့ ကြက်သားတုံးများကို ဖုံးအုပ်သည်အထိ နစ်စိမ်ထားပါ။",
            "အခန်းအပူချိန်တွင် ကြက်သားတုံးများကို (၂)နာရီခန့်အကြာ စိမ်ထားရပါမည်။ (သို့) ဖြစ်နိုင်လျှင် ရေခဲသေတ္တာထဲတွင် တစ်ညသွင်းထား၍လည်း ရပါသည်။",
            "ဝါးတံစို့တွင် ကြက်သားတုံးများကို သီထိုးပြီး မီးသွေးမီးဖိုတွင် အသားတုံးများကျက်သည်အထိ ကင်ပါ။ (ဝါးတံစို့ချောင်းကို မီးမကင်ခင် ရေစိမ်ထားရန် မမေ့စေလိုပါ)။",
            "ပြီးလျှင် တည်ခင်း၍ရပြီ ဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Remove skin and excess fat from the chicken thighs, then cut into uniform bite-sized cubes.",
            "Pound the onion, garlic, and ginger into a smooth paste.",
            "Combine the paste in a bowl with fresh lime juice, coriander, cumin, garam masala, curd yogurt, salt, and pounded mint.",
            "Submerge the chicken cubes in the marinade until thoroughly coated.",
            "Marinate at room temperature for 2 hours, or preferably refrigerate overnight.",
            "Thread the marinated chicken onto bamboo skewers and grill over charcoal until tender and lightly charred (soak skewers in water beforehand).",
            "Once cooked through, transfer kebabs to a platter and serve hot."
        ],
        "tags": {
            "dietary": ["gluten-free"],
            "seasonal": ["all-season"],
            "festival": [],
            "main_ingredients": ["chicken", "yogurt", "mint"]
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
            "pdf_pages": [47],
            "printed_page_numbers": [83],
            "extraction_method": "manual_transcription_from_scanned_image"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "Printed on page 83 (bottom). Skewer soaking instruction explicitly included.",
            "verified": True
        }
    },

    # R0019: ကြက်အသည်းဟင်း (Curried Chicken Livers)
    {
        "recipe_id": "R0019",
        "name_mm": "ကြက်အသည်းဟင်း",
        "name_en": "Curried Chicken Livers",
        "description_mm": None,
        "description_en": None,
        "category": "Poultry dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {
                "ingredient_id": "I0056",
                "name_mm": "ကြက်အသည်း",
                "name_en": "Chicken liver",
                "original_name": "ကြက်သည်း",
                "quantity": 60.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၆၀ ကျပ်သား",
                "normalized_quantity": 979.8,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": 7.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၇ ၁/၂ ကျပ်သား",
                "normalized_quantity": 122.5,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ (ပါးပါးလှီး)",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.6,
                "normalized_unit": "g",
                "preparation_note_mm": "ပါးပါးလှီး",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0014",
                "name_mm": "ကြက်သွန်ဖြူ",
                "name_en": "Garlic",
                "original_name": "ကြက်သွန်ဖြူ (ပါးပါးလှီး)",
                "quantity": 3.0,
                "unit": "မြွှာ (piece)",
                "original_quantity_text": "၃ မြွှာ",
                "normalized_quantity": 3.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ပါးပါးလှီး",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0013",
                "name_mm": "ဂျင်း",
                "name_en": "Ginger",
                "original_name": "ချင်း (၁/၂\" ပါးပါးလှီး)",
                "quantity": 2.0,
                "unit": "လွှာ (piece)",
                "original_quantity_text": "၂ လွှာ",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ပါးပါးလှီး",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0024",
                "name_mm": "နနွင်းမှုန့်",
                "name_en": "Turmeric powder",
                "original_name": "နနွင်း",
                "quantity": 0.5,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁/၂ လဖဇ",
                "normalized_quantity": 2.5,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0025",
                "name_mm": "ငရုတ်သီးမှုန့်",
                "name_en": "Chili powder",
                "original_name": "ငရုတ်သီးမှုန့်",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0054",
                "name_mm": "နံနံစေ့",
                "name_en": "Coriander seeds",
                "original_name": "နံနံစေ့ (ထောင်း)",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ထောင်း",
                "preparation_note_en": "pounded"
            },
            {
                "ingredient_id": "I0055",
                "name_mm": "ဇီယာ",
                "name_en": "Cumin seeds",
                "original_name": "ဇီယာ (ထောင်း)",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ထောင်း",
                "preparation_note_en": "pounded"
            },
            {
                "ingredient_id": "I0042",
                "name_mm": "ခရမ်းချဉ်သီး",
                "name_en": "Tomato",
                "original_name": "ခရမ်းချဉ်သီးမှည့် (လှီးပြီး)",
                "quantity": 5.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၅ လုံး",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "လှီးပြီး",
                "preparation_note_en": "sliced"
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0012",
                "name_mm": "မဆလာ",
                "name_en": "Garam masala",
                "original_name": "မဆလာမှုန့်",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "servings": 10,
        "preparation_time_minutes": 15,
        "cooking_time_minutes": 25,
        "instructions_mm": [
            "သန့်စင်ပြီး ကြက်သည်းများကို တစ်ဝက်လှီးဖြတ်ပါ။",
            "ဆီအပူတွင် ကြက်သွန်နီကို ပျော့အောင်ကြော်ပါ။ ကြက်သွန်ဖြူနှင့် ချင်းတို့ပါထည့်ပြီး ရွှေရောင်သမ်းသည်အထိ မွှေပါ။",
            "နနွင်းမှုန့်၊ ငရုတ်သီးမှုန့်၊ နံနံစေ့နှင့် ဇီယာစေ့များကိုပါထည့်၍ (၂)မိနစ်မျှ မွှေပေးပါ။",
            "ခရမ်းချဉ်သီးနှင့် ဆားရောထည့်ပြီး အဖုံးပိတ်ကာ ဖြည်းညင်းစွာတည်ပါ။ ရံဖန်ရံခါ မွှေပေးပါ။",
            "ကြက်အသည်းများထည့်ပြီးမွှေကာ အဖုံးအုပ်၍ (၁၅)မိနစ်ခန့် ချက်ပါ။",
            "အချိန်စေ့လျှင် မဆလာမှုန့်ဖြူးပြီး ဆက်လက်၍ (၂)မိနစ်ကျော်ကျော် ဆူအောင်ဆက်ထားပါ။",
            "ကြက်သည်းဟင်းကို ပူပူနွေးနွေး အနေအထားဖြင့် တည်ခင်း၍ရပြီ ဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Trim and clean the chicken livers, then cut each in half.",
            "In hot oil, sauté the sliced onions until soft, then add garlic and ginger, stirring until lightly golden.",
            "Add the turmeric powder, chili powder, ground coriander, and cumin seeds, stirring for about 2 minutes.",
            "Add the sliced ripe tomatoes and salt; cover tightly and simmer gently, stirring occasionally.",
            "Add the chicken livers, stir gently to coat in aromatic sauce, cover, and cook for about 15 minutes.",
            "When the livers are cooked through, sprinkle with garam masala and let it simmer for over 2 minutes.",
            "Serve the chicken liver curry hot accompanied with rice."
        ],
        "tags": {
            "dietary": ["dairy-free", "gluten-free"],
            "seasonal": ["all-season"],
            "festival": [],
            "main_ingredients": ["chicken liver", "tomato"]
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
            "printed_page_numbers": [84],
            "extraction_method": "manual_transcription_from_scanned_image"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "Printed on page 84 (top). Servings (လူ ၁၀ ဦးစာ) verified.",
            "verified": True
        }
    },

    # R0020: ကြက်သားဟင်း (Chicken Curry)
    {
        "recipe_id": "R0020",
        "name_mm": "ကြက်သားဟင်း",
        "name_en": "Chicken Curry",
        "description_mm": None,
        "description_en": None,
        "category": "Poultry dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {
                "ingredient_id": "I0014",
                "name_mm": "ကြက်သွန်ဖြူ",
                "name_en": "Garlic",
                "original_name": "ကြက်သွန်ဖြူ (စဉ်းပြီး)",
                "quantity": 2.0,
                "unit": "မြွှာ (piece)",
                "original_quantity_text": "၂ မြွှာ",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "စဉ်းပြီး",
                "preparation_note_en": "minced"
            },
            {
                "ingredient_id": "I0013",
                "name_mm": "ဂျင်း",
                "name_en": "Ginger",
                "original_name": "ချင်း (၁\")",
                "quantity": 2.0,
                "unit": "လွှာ (piece)",
                "original_quantity_text": "၂ လွှာ",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0024",
                "name_mm": "နနွင်းမှုန့်",
                "name_en": "Turmeric powder",
                "original_name": "နနွင်းမှုန့်",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0055",
                "name_mm": "ဇီယာ",
                "name_en": "Cumin seeds",
                "original_name": "ဇီယာ (ထောင်းပြီး)",
                "quantity": 2.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၂ လဖဇ",
                "normalized_quantity": 10.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ထောင်းပြီး",
                "preparation_note_en": "pounded"
            },
            {
                "ingredient_id": "I0025",
                "name_mm": "ငရုတ်သီးမှုန့်",
                "name_en": "Chili powder",
                "original_name": "ငရုတ်သီးမှုန့်",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0039",
                "name_mm": "ငရုတ်ကောင်းမှုန့်",
                "name_en": "Ground black pepper",
                "original_name": "ငရုတ်ကောင်း",
                "quantity": 0.5,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁/၂ လဖဇ",
                "normalized_quantity": 2.5,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0029",
                "name_mm": "ဒိန်ချဉ်",
                "name_en": "Curd",
                "original_name": "ဒိန်ချဉ်",
                "quantity": 1.0,
                "unit": "ခွက် (cup / g)",
                "original_quantity_text": "၁ ခွက်",
                "normalized_quantity": 240.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0028",
                "name_mm": "ကြက်သား",
                "name_en": "Chicken",
                "original_name": "ကြက်သား",
                "quantity": 60.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၆၀ ကျပ်သား",
                "normalized_quantity": 979.8,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.6,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ (အလတ်) (ပါးပါးလှီးပြီး)",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ပါးပါးလှီးပြီး",
                "preparation_note_en": "thinly sliced"
            }
        ],
        "servings": 10,
        "preparation_time_minutes": 240, # 4 hours marinating
        "cooking_time_minutes": 35,
        "instructions_mm": [
            "ဇလုံကြီးတစ်လုံးထဲသို့ ကြက်သွန်ဖြူနှင့် ချင်း၊ နနွင်း၊ ငရုတ်သီးမှုန့်၊ ငရုတ်ကောင်း၊ ဇီယာ၊ ဆားနှင့် ဒိန်ချဉ်တို့ကို ရောစပ်ထည့်ပြီး အရွယ်ညီ တုံးတစ်ထားသော ကြက်သားတုံးများပေါင်းစပ်ကာ (၄)နာရီမျှ စိမ်ထားပါ။",
            "ရံဖန်ရံခါ အသားကို လှည့်ပြောင်းစိမ်ပေးပါ။",
            "ဆီပူပူတွင် ကြက်သွန်နီကို ရွှေရောင်သမ်းသည်အထိမွှေပါ။",
            "အရသာရည်စိမ်ထားသည့် ကြက်သားတုံးများနှင့် စိမ်ရေများကိုထည့်ပါ။",
            "အဖုံးအုပ်၍ မိနစ်(၃၀)ခန့်အကြာတွင် ကြက်သားများ နူးလာလျှင် တည်ခင်း၍ရပြီဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "In a large bowl, mix minced garlic, ginger, turmeric, chili powder, black pepper, cumin, salt, and curd yogurt; add uniform chicken cubes and marinate for 4 hours.",
            "Turn the chicken occasionally in the marinade to ensure even absorption.",
            "In hot oil, fry the thinly sliced onions until golden brown.",
            "Add the marinated chicken cubes along with all of the marinade liquid.",
            "Cover and simmer for about 30 minutes until the chicken is tender and thoroughly infused, then serve."
        ],
        "tags": {
            "dietary": ["gluten-free"],
            "seasonal": ["all-season"],
            "festival": [],
            "main_ingredients": ["chicken", "yogurt"]
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
            "printed_page_numbers": [84],
            "extraction_method": "manual_transcription_from_scanned_image"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "Printed on page 84 (bottom). 4-hour yogurt marinade method preserved.",
            "verified": True
        }
    }
]

# Append new recipes (avoid duplicate recipe_id)
existing_r_ids = {r['recipe_id'] for r in recipes}
for r in batch3_recipes:
    if r['recipe_id'] not in existing_r_ids:
        recipes.append(r)
        existing_r_ids.add(r['recipe_id'])

# Update extraction report
report['total_pages_processed'] = 12 # PDF pages 42-48
report['total_recipes_extracted'] = len(recipes)
report['complete_recipes'] = len(recipes)
report['unique_ingredients'] = len(ingredients)
report['general_notes'].append(
    f"Batch 3 completed: Recipes R0011 - R0020 spanning printed pages 80-84 (PDF pages 46-48). Added {len(new_ingredients)} new catalog ingredients (I0040 - I0056)."
)

# Save files
with open('recipes.json', 'w', encoding='utf-8') as f:
    json.dump(recipes, f, ensure_ascii=False, indent=2)

with open('ingredients.json', 'w', encoding='utf-8') as f:
    json.dump(ingredients, f, ensure_ascii=False, indent=2)

with open('extraction_report.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print(f"Batch 3 written successfully! Total recipes: {len(recipes)}, Total ingredients: {len(ingredients)}")
