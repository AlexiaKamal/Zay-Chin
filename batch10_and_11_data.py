# -*- coding: utf-8 -*-
"""
Batches 10 & 11: Final Recipes of the Cookbook
Batch 10: ကလေးသူငယ်များအတွက် အစားအစာများ (Infant & Child Nutrition) - R0153 to R0163 (Book pp. 161-164 / PDF pp. 87-89)
Batch 11: လူမမာများအတွက် အစားအစာများ (Convalescent & Invalid Foods) - R0164 to R0171 (Book pp. 166-169 / PDF pp. 90-91)
"""

NEW_INGREDIENTS_FINAL = [
    {
        "ingredient_id": "I0214",
        "name_mm": "ဘိုစားပဲ",
        "name_en": "French beans (Green beans)",
        "aliases_mm": ["ဗိုလ်စားပဲ", "ပဲသီးတောင့်"],
        "aliases_en": ["green beans", "string beans", "snap beans"],
        "category": "vegetable",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0215",
        "name_mm": "ပင်လယ်ငါး",
        "name_en": "Marine fish",
        "aliases_mm": ["ပင်လယ်ငါးသား"],
        "aliases_en": ["sea fish", "white marine fish fillet"],
        "category": "seafood",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0216",
        "name_mm": "ဘီစကစ်",
        "name_en": "Plain baby biscuit",
        "aliases_mm": ["မုန့်ကြွပ်ချပ်", "အချိုမဲ့ဘီစကစ်"],
        "aliases_en": ["baby biscuit", "plain tea biscuit", "digestive biscuit"],
        "category": "dry_goods",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0217",
        "name_mm": "လိမ္မော်ရည်",
        "name_en": "Orange juice",
        "aliases_mm": ["လိမ္မော်သီးရည်"],
        "aliases_en": ["fresh orange juice"],
        "category": "liquid",
        "default_unit": "ml"
    },
    {
        "ingredient_id": "I0218",
        "name_mm": "ပီလောပီနံမှုန့်",
        "name_en": "Tapioca starch (Cassava flour)",
        "aliases_mm": ["ပီလောပီနံမုန့်ညက်"],
        "aliases_en": ["tapioca flour", "cassava starch"],
        "category": "dry_goods",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0219",
        "name_mm": "သကာရည်",
        "name_en": "Caramel syrup (Golden syrup)",
        "aliases_mm": ["သကြားသကာ"],
        "aliases_en": ["caramel syrup", "golden syrup", "sugar syrup"],
        "category": "seasoning",
        "default_unit": "ml"
    },
    {
        "ingredient_id": "I0220",
        "name_mm": "ငါးရံ့",
        "name_en": "Striped snakehead fish",
        "aliases_mm": ["ငါးရံ့သား"],
        "aliases_en": ["snakehead murrel", "striped snakehead", "freshwater snakehead"],
        "category": "fish_seafood",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0221",
        "name_mm": "ဆိတ်ရိုး",
        "name_en": "Mutton soup bone",
        "aliases_mm": ["ဆိတ်ရိုးခွေ"],
        "aliases_en": ["mutton bone", "mutton marrow bone"],
        "category": "meat",
        "default_unit": "piece"
    }
]

BATCH10_AND_11_RECIPES = [
    # --- BATCH 10: BABY FOODS (R0153 - R0163) ---
    {
        "recipe_id": "R0153",
        "name_mm": "ဟင်းသီးဟင်းရွက်အပျစ်",
        "name_en": "Baby Vegetable Purée",
        "description_mm": "အာလူး၊ မုန်လာဥဝါ၊ ပန်းဂေါ်ဖီနှင့် ဘိုစားပဲတို့ကို နူးအိအောင်ပြုတ်၍ ဆန်ခါတိုက်ကာ နို့၊ ထောပတ်တို့ဖြင့် ရောမွှေထားသော အာဟာရပြည့် ကလေးဟင်းသီးဟင်းရွက်အပျစ်။",
        "description_en": "Smooth and velvety infant vegetable purée prepared from steamed potatoes, carrots, cauliflower, and green beans, passed through a sieve and enriched with warm cow's milk and butter.",
        "category": "soup",
        "meal_types": ["breakfast", "lunch", "dinner"],
        "servings": 2,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0159",
                "name_mm": "အာလူး",
                "name_en": "Potato",
                "original_name": "အာလူး (လှီးပြီး)",
                "quantity": 3.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၃ ကျပ်သား (၁ လုံး)",
                "normalized_quantity": 48.9,
                "normalized_unit": "g",
                "preparation_note_mm": "လှီးပြီး",
                "preparation_note_en": "peeled and diced"
            },
            {
                "ingredient_id": "I0014",
                "name_mm": "မုန်လာဥနီ",
                "name_en": "Carrot",
                "original_name": "မုန်လာဥဝါ (လှီးပြီး)",
                "quantity": 2.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ကျပ်သား",
                "normalized_quantity": 32.7,
                "normalized_unit": "g",
                "preparation_note_mm": "လှီးပြီး",
                "preparation_note_en": "peeled and finely diced"
            },
            {
                "ingredient_id": "I0108",
                "name_mm": "ပန်းဂေါ်ဖီ",
                "name_en": "Cauliflower",
                "original_name": "ပန်းဂေါ်ဖီ (လှီးပြီး)",
                "quantity": 2.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ကျပ်သား",
                "normalized_quantity": 32.7,
                "normalized_unit": "g",
                "preparation_note_mm": "လှီးပြီး",
                "preparation_note_en": "florets chopped"
            },
            {
                "ingredient_id": "I0214",
                "name_mm": "ဘိုစားပဲ",
                "name_en": "French beans (Green beans)",
                "original_name": "ဘိုစားပဲ (လှီးပြီး)",
                "quantity": 2.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ကျပ်သား",
                "normalized_quantity": 32.7,
                "normalized_unit": "g",
                "preparation_note_mm": "လှီးပြီး",
                "preparation_note_en": "trimmed and chopped"
            },
            {
                "ingredient_id": "I0002",
                "name_mm": "ထောပတ်",
                "name_en": "Butter",
                "original_name": "ထောပတ်",
                "quantity": 0.75,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၃/၄ စပဇ",
                "normalized_quantity": 11.2,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0036",
                "name_mm": "နွားနို့",
                "name_en": "Cow milk",
                "original_name": "နွားနို့",
                "quantity": 6.0,
                "unit": "စားပွဲဇွန်း (tbsp / ml)",
                "original_quantity_text": "၆ စပဇ",
                "normalized_quantity": 90.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "အာလူး၊ မုန်လာဥဝါ၊ ပန်းဂေါ်ဖီပွင့်နှင့် ဘိုစားပဲတို့ကို စင်ကြယ်အောင်ဆေးကြောပြီး ရေအနည်းငယ်ဖြင့် အိုးဖုံးကို စေ့အောင်ပိတ်ကာ နူးအိသည်အထိ ပြုတ်ပါ။",
            "ရေခမ်းလုမတတ်အချိန်တွင် ဟင်းသီးဟင်းရွက်များ အားလုံးနူးအိပြီဖြစ်ရာ အာလူးနှင့် အသီးအရွက်များကို ဇွန်းဖြင့်ခြေ၍ ဆန်ခါတိုက်ချကာ စစ်ယူပါ။",
            "ရရှိလာသော ဟင်းသီးဟင်းရွက်နှစ်ထဲသို့ ထောပတ်နှင့် နွားနို့တို့ ထည့်သွင်းကာ သမအောင် မွှေလိုက်လျှင် ကလေးငယ်များ အလွယ်တကူ စားသုံးနိုင်သည့် ချောမွတ်ပျစ်ချွဲသော ဟင်းသီးဟင်းရွက်အပျစ် ရရှိပါမည်။"
        ],
        "instructions_en": [
            "Wash the potatoes, carrots, cauliflower florets, and green beans thoroughly, then simmer them in a tightly covered pot with a little water until completely tender.",
            "When the water has almost reduced and all the vegetables are soft, mash them thoroughly and press through a fine wire sieve to yield a silky purée.",
            "Stir the butter and warm cow's milk smoothly into the vegetable purée until rich, glossy, and spoonable for infants."
        ],
        "tags": {
            "dietary": ["vegetarian", "baby_food"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["potato", "carrot", "cauliflower", "green beans", "cow milk", "butter"]
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
            "pdf_pages": [87],
            "printed_page_numbers": [161],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "3:3 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0154",
        "name_mm": "အသားနှင့် ဟင်းသီးဟင်းရွက်အပျစ်",
        "name_en": "Baby Meat and Vegetable Purée",
        "description_mm": "အမဲသား၊ ကြက်သား သို့မဟုတ် ဆိတ်သားကို အာလူး၊ မုန်လာဥဝါ၊ ပန်းဂေါ်ဖီတို့ဖြင့် နူးအိအောင်ပြုတ်ပြီး ဆန်ခါတိုက်ကာ နို့၊ ထောပတ်မွှေထားသော ကလေးအာဟာရအပျစ်။",
        "description_en": "Wholesome and easily digestible meat and vegetable purée for growing toddlers, combining tender minced beef, chicken, or mutton simmered with root vegetables and enriched with milk and butter.",
        "category": "soup",
        "meal_types": ["lunch", "dinner"],
        "servings": 2,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0076",
                "name_mm": "အမဲသား",
                "name_en": "Beef",
                "original_name": "အမဲသား",
                "quantity": 2.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ကျပ်သား",
                "normalized_quantity": 32.7,
                "normalized_unit": "g",
                "preparation_note_mm": "နုပ်နုပ်စဉ်းရန်",
                "preparation_note_en": "lean, finely minced"
            },
            {
                "ingredient_id": "I0020",
                "name_mm": "ကြက်သား",
                "name_en": "Chicken meat",
                "original_name": "ကြက်သား",
                "quantity": 2.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ကျပ်သား",
                "normalized_quantity": 32.7,
                "normalized_unit": "g",
                "preparation_note_mm": "အရိုးအရေခွံဖယ်နုပ်နုပ်စဉ်းရန်",
                "preparation_note_en": "boneless skinless, finely minced"
            },
            {
                "ingredient_id": "I0068",
                "name_mm": "ဆိတ်သား",
                "name_en": "Mutton",
                "original_name": "ဆိတ်သား",
                "quantity": 2.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ကျပ်သား",
                "normalized_quantity": 32.7,
                "normalized_unit": "g",
                "preparation_note_mm": "အဆီဖယ်နုပ်နုပ်စဉ်းရန်",
                "preparation_note_en": "lean, finely minced"
            },
            {
                "ingredient_id": "I0159",
                "name_mm": "အာလူး",
                "name_en": "Potato",
                "original_name": "အာလူး (အသေး ၁ လုံး)",
                "quantity": 1.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁ ကျပ်သား (၁ လုံး)",
                "normalized_quantity": 16.3,
                "normalized_unit": "g",
                "preparation_note_mm": "အခွံနွှာလှီးထားရန်",
                "preparation_note_en": "peeled and diced"
            },
            {
                "ingredient_id": "I0014",
                "name_mm": "မုန်လာဥနီ",
                "name_en": "Carrot",
                "original_name": "မုန်လာဥဝါ",
                "quantity": 1.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁ ကျပ်သား",
                "normalized_quantity": 16.3,
                "normalized_unit": "g",
                "preparation_note_mm": "လှီးပြီး",
                "preparation_note_en": "finely chopped"
            },
            {
                "ingredient_id": "I0108",
                "name_mm": "ပန်းဂေါ်ဖီ",
                "name_en": "Cauliflower",
                "original_name": "ပန်းဂေါ်ဖီ",
                "quantity": 0.75,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၃/၄ ကျပ်သား",
                "normalized_quantity": 12.2,
                "normalized_unit": "g",
                "preparation_note_mm": "လှီးပြီး",
                "preparation_note_en": "chopped"
            },
            {
                "ingredient_id": "I0214",
                "name_mm": "ဘိုစားပဲ",
                "name_en": "French beans (Green beans)",
                "original_name": "ဘိုစားပဲ",
                "quantity": 0.75,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၃/၄ ကျပ်သား",
                "normalized_quantity": 12.2,
                "normalized_unit": "g",
                "preparation_note_mm": "လှီးပြီး",
                "preparation_note_en": "chopped"
            },
            {
                "ingredient_id": "I0002",
                "name_mm": "ထောပတ်",
                "name_en": "Butter",
                "original_name": "ထောပတ်",
                "quantity": 0.75,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၃/၄ လဖဇ",
                "normalized_quantity": 3.8,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0036",
                "name_mm": "နွားနို့",
                "name_en": "Cow milk",
                "original_name": "နွားနို့",
                "quantity": 6.0,
                "unit": "စားပွဲဇွန်း (tbsp / ml)",
                "original_quantity_text": "၆ စပဇ",
                "normalized_quantity": 90.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "အမဲသား၊ ကြက်သား သို့မဟုတ် ဆိတ်သားတို့ကို ရေစင်အောင်ဆေးကြော၍ နူးအိအောင် ပြုတ်ထားပါ။",
            "အာလူး၊ မုန်လာဥဝါ၊ ပန်းဂေါ်ဖီနှင့် ဘိုစားပဲတို့ကိုလည်း အခွံခွာ ရေစင်အောင်ဆေးပြီး အိုးအဖုံးကို စေ့နေအောင် ပိတ်ကာ နူးအိသည်အထိ ပြုတ်ပါ။",
            "အသားနှင့် အသီးအရွက်များ အားလုံးနူးအိသွားလျှင် အတူတကွ ခြေ၍ ဆန်ခါတိုက်ယူပြီး နွားနို့နှင့် ထောပတ်တို့ ထည့်မွှေကာ ကလေးငယ်များအတွက် ပျစ်ချွဲနူးညံ့သော အသားနှင့် ဟင်းသီးဟင်းရွက်အပျစ် ပြင်ဆင်ကျွေးမွေးပါ။"
        ],
        "instructions_en": [
            "Rinse the meat (beef, chicken, or mutton) thoroughly and simmer gently until tender.",
            "Peel, rinse, and chop the potatoes and vegetables; place into a tightly covered pot and simmer until very soft.",
            "Combine the tender meat and vegetables, mash thoroughly, and rub through a fine sieve; stir in warm cow's milk and butter to create a silky, nutrient-dense purée for young children."
        ],
        "tags": {
            "dietary": ["baby_food"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["chicken meat", "beef", "potato", "carrot", "cow milk", "butter"]
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
            "pdf_pages": [87],
            "printed_page_numbers": [161],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "3:3 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0155",
        "name_mm": "ငါးနှင့် ဟင်းသီးဟင်းရွက်အပျစ်",
        "name_en": "Baby Fish and Vegetable Purée",
        "description_mm": "ပင်လယ်ငါးသားစစ်စစ်ကို အသီးအရွက်စုံနှင့်အတူ နူးအိအောင်ပြုတ်၍ ဆန်ခါတိုက်ကာ နို့၊ ထောပတ်တို့ဖြင့် ရောစပ်ထားသော ကလေးငါးအာဟာရအပျစ်။",
        "description_en": "Delicate, brain-nourishing infant fish and vegetable purée made with boneless marine fish fillet, root vegetables, and green beans, puréed and enriched with milk and butter.",
        "category": "soup",
        "meal_types": ["lunch", "dinner"],
        "servings": 2,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0215",
                "name_mm": "ပင်လယ်ငါး",
                "name_en": "Marine fish",
                "original_name": "ပင်လယ်ငါး",
                "quantity": 10.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၀ ကျပ်သား",
                "normalized_quantity": 163.3,
                "normalized_unit": "g",
                "preparation_note_mm": "အရိုးအရေခွံဖယ်နုပ်နုပ်စဉ်းရန်",
                "preparation_note_en": "boneless skinless fillet, minced"
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": "အနည်းငယ်",
                "unit": "အနည်းငယ် (to taste)",
                "original_quantity_text": "ပါသည်ဆိုရုံ",
                "normalized_quantity": None,
                "normalized_unit": "to_taste",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0159",
                "name_mm": "အာလူး",
                "name_en": "Potato",
                "original_name": "အာလူး (သေးသေး ၁ လုံး)",
                "quantity": 1.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁ ကျပ်သား (၁ လုံး)",
                "normalized_quantity": 16.3,
                "normalized_unit": "g",
                "preparation_note_mm": "အခွံခွာလှီးပြီး",
                "preparation_note_en": "peeled and diced"
            },
            {
                "ingredient_id": "I0014",
                "name_mm": "မုန်လာဥနီ",
                "name_en": "Carrot",
                "original_name": "မုန်လာဥဝါ",
                "quantity": 1.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁ ကျပ်သား",
                "normalized_quantity": 16.3,
                "normalized_unit": "g",
                "preparation_note_mm": "လှီးပြီး",
                "preparation_note_en": "chopped"
            },
            {
                "ingredient_id": "I0108",
                "name_mm": "ပန်းဂေါ်ဖီ",
                "name_en": "Cauliflower",
                "original_name": "ပန်းဂေါ်ဖီ",
                "quantity": 0.75,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၃/၄ ကျပ်သား",
                "normalized_quantity": 12.2,
                "normalized_unit": "g",
                "preparation_note_mm": "လှီးပြီး",
                "preparation_note_en": "chopped"
            },
            {
                "ingredient_id": "I0214",
                "name_mm": "ဘိုစားပဲ",
                "name_en": "French beans (Green beans)",
                "original_name": "ဘိုစားပဲ",
                "quantity": 0.75,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၃/၄ ကျပ်သား",
                "normalized_quantity": 12.2,
                "normalized_unit": "g",
                "preparation_note_mm": "လှီးပြီး",
                "preparation_note_en": "chopped"
            },
            {
                "ingredient_id": "I0002",
                "name_mm": "ထောပတ်",
                "name_en": "Butter",
                "original_name": "ထောပတ်",
                "quantity": 0.75,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၃/၄ လဖဇ",
                "normalized_quantity": 3.8,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0036",
                "name_mm": "နွားနို့",
                "name_en": "Cow milk",
                "original_name": "နွားနို့",
                "quantity": 6.0,
                "unit": "စားပွဲဇွန်း (tbsp / ml)",
                "original_quantity_text": "၆ စပဇ",
                "normalized_quantity": 90.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "အသားထွင်ပြီး ပင်လယ်ငါးကို အရေခွံနှင့် အရိုးလုံးဝမပါစေဘဲ နုပ်နုပ်စဉ်းကာ ဆားပါသည်ဆိုရုံမျှဖြင့် သမအောင် နယ်ထားပါ။",
            "အာလူးနှင့် အသီးအရွက်များကို ရေပါရုံမျှဖြင့် အဖုံးအုပ်၍ နူးအိသည်အထိ ပြုတ်ပြီး နူးစပြုချိန်တွင် ငါးသားစဉ်းများကို နောက်ဆုံးမှ ထည့်ပြုတ်ပါ။",
            "အားလုံးနူးအိသွားလျှင် ရောခြေ၍ ဆန်ခါတိုက်ချကာ ထောပတ်နှင့် နို့တို့ ရောမွှေလိုက်လျှင် ပျစ်ချွဲနူးညံ့သော ငါးနှင့် ဟင်းသီးဟင်းရွက်အပျစ် ရရှိပါမည်။"
        ],
        "instructions_en": [
            "Debone and skin the sea fish fillet completely, finely mince the flesh, and season gently with just a tiny pinch of salt.",
            "Simmer the potatoes, carrots, cauliflower, and green beans with a splash of water until tender, then add the minced fish flesh at the end and poach gently until fully cooked.",
            "Mash the mixture thoroughly and pass through a fine sieve; blend in butter and warm milk to finish into a smooth, creamy fish purée."
        ],
        "tags": {
            "dietary": ["pescatarian", "baby_food"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["sea fish", "potato", "carrot", "cow milk", "butter"]
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
            "pdf_pages": [87],
            "printed_page_numbers": [161],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "3:3 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0156",
        "name_mm": "ကြက်သားသရေစာ",
        "name_en": "Baby Chicken Snack Porridge",
        "description_mm": "အရိုးအရေခွံမပါသော ကြက်သား၊ ဆန်၊ မုန်လာဥဝါ၊ ပန်းဂေါ်ဖီတို့ကို နူးအိအောင်ပြုတ်၍ ကြိတ်ခြေဆန်ခါချကာ နို့၊ ထောပတ်တို့ဖြင့် ပြုလုပ်ထားသော ကလေးသရေစာ။",
        "description_en": "Nourishing, savory chicken and rice porridge puréed with vegetables, butter, and milk into a wholesome feeding snack for infants.",
        "category": "soup",
        "meal_types": ["breakfast", "lunch", "snack"],
        "servings": 2,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0020",
                "name_mm": "ကြက်သား",
                "name_en": "Chicken meat",
                "original_name": "ကြက်သား",
                "quantity": 20.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၀ ကျပ်သား",
                "normalized_quantity": 326.6,
                "normalized_unit": "g",
                "preparation_note_mm": "အရိုးထွင်ပြီး အရေခွံမပါအောင် တုံးတစ်ထားရန်",
                "preparation_note_en": "boneless skinless chicken, cubed"
            },
            {
                "ingredient_id": "I0001",
                "name_mm": "ဆန်",
                "name_en": "Rice",
                "original_name": "ဆန်",
                "quantity": 0.5,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၁/၂ နို့ဆီဘူး",
                "normalized_quantity": 125.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ဆေးကြောပြုတ်ရန်",
                "preparation_note_en": "washed and simmered into congee"
            },
            {
                "ingredient_id": "I0014",
                "name_mm": "မုန်လာဥနီ",
                "name_en": "Carrot",
                "original_name": "မုန်လာဥဝါ",
                "quantity": 2.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ကျပ်သား",
                "normalized_quantity": 32.7,
                "normalized_unit": "g",
                "preparation_note_mm": "လှီးပြီး",
                "preparation_note_en": "chopped"
            },
            {
                "ingredient_id": "I0108",
                "name_mm": "ပန်းဂေါ်ဖီ",
                "name_en": "Cauliflower",
                "original_name": "ပန်းဂေါ်ဖီ",
                "quantity": 2.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ကျပ်သား",
                "normalized_quantity": 32.7,
                "normalized_unit": "g",
                "preparation_note_mm": "လှီးပြီး",
                "preparation_note_en": "chopped"
            },
            {
                "ingredient_id": "I0214",
                "name_mm": "ဘိုစားပဲ",
                "name_en": "French beans (Green beans)",
                "original_name": "ဘိုစားပဲ",
                "quantity": 2.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ကျပ်သား",
                "normalized_quantity": 32.7,
                "normalized_unit": "g",
                "preparation_note_mm": "လှီးပြီး",
                "preparation_note_en": "chopped"
            },
            {
                "ingredient_id": "I0002",
                "name_mm": "ထောပတ်",
                "name_en": "Butter",
                "original_name": "ထောပတ်",
                "quantity": 0.75,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၃/၄ လဖဇ",
                "normalized_quantity": 3.8,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0036",
                "name_mm": "နွားနို့",
                "name_en": "Cow milk",
                "original_name": "နွားနို့",
                "quantity": 6.0,
                "unit": "စားပွဲဇွန်း (tbsp / ml)",
                "original_quantity_text": "၆ စပဇ",
                "normalized_quantity": 90.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "အရိုးထွင်ပြီး အရေခွံလုံးဝမပါစေအောင် ပြုလုပ်ထားသော ကြက်သားတုံးများကို နူးအိသည်အထိ ပြုတ်ပါ။",
            "ဆန်ကိုလည်းကောင်း၊ ရေစင်အောင်ဆေးကြောပြီး တုံးတစ်ထားသော အသီးအရွက်များကိုလည်းကောင်း သီးခြားနူးအိအောင် ပြုတ်ထားပါ။",
            "ကျက်နူးသော ကြက်သား၊ ဆန်ပြုတ်နှင့် ဟင်းသီးဟင်းရွက် အားလုံးကို ရော၍ ကြိတ်ခြေကာ ဆန်ခါချပြီး ထောပတ်၊ နွားနို့တို့နှင့် သမအောင် မွှေလိုက်လျှင် ကလေးငယ်များအတွက် ပျစ်ချွဲအာဟာရပြည့် ကြက်သားသရေစာ ရရှိပါမည်။"
        ],
        "instructions_en": [
            "Debone and skin the chicken meat, cut into pieces, and simmer until tender.",
            "Cook the rice into soft rice congee, and boil the washed chopped carrots, cauliflower, and beans until very tender.",
            "Combine the tender chicken, soft rice, and vegetables, grind and rub through a wire sieve, then beat in butter and warm milk to form a delicious, digestible baby meal."
        ],
        "tags": {
            "dietary": ["baby_food"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["chicken meat", "rice", "carrot", "cow milk", "butter"]
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
            "pdf_pages": [88],
            "printed_page_numbers": [162],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "3:3 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0157",
        "name_mm": "ပန်းသီးအပျစ်",
        "name_en": "Baby Apple Purée (Applesauce)",
        "description_mm": "လတ်ဆတ်သောအနာလွတ်ပန်းသီးကို ရေအနည်းငယ်ဖြင့် အိုးဖုံးလုံအောင်ပိတ်ပြုတ်ကာ အခွံခွာ၍ သကြားအနည်းငယ်ဖြင့် ခြေထားသော သဘာဝပန်းသီးအပျစ်။",
        "description_en": "Classic gentle stewed apple purée for weaning babies, made by steaming whole fresh apples until soft, then peeling, sweetening slightly, and mashing smooth.",
        "category": "dessert",
        "meal_types": ["snack", "breakfast"],
        "servings": 1,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0148",
                "name_mm": "ပန်းသီး",
                "name_en": "Apple",
                "original_name": "ပန်းသီးအမှည့်",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အနာလွတ် အမှည့်",
                "preparation_note_en": "ripe, blemish-free"
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": "အနည်းငယ်",
                "unit": "အနည်းငယ် (to taste)",
                "original_quantity_text": "အနည်းငယ်",
                "normalized_quantity": None,
                "normalized_unit": "to_taste",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "အနာလွတ်ပန်းသီးကို ရေဆေးကြောပြီး ရေအနည်းငယ်ဖြင့် အိုးအဖုံးကို လုံအောင်ပိတ်၍ ပြုတ်ပါ။",
            "နူးလောက်သည့် အချိန်တွင် အိုးအဖုံးဖွင့်ကြည့်၍ ပန်းသီးကို ထုတ်ယူကာ အခွံကို ခွာဖယ်လိုက်ပါ။",
            "ပန်းသီးသားကို သကြားအနည်းငယ်ဖြင့် ရောကာ ဇွန်းဖြင့် ညက်ညက်ခြေပြီး ကလေးငယ်များအတွက် တိုက်ကျွေးနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Rinse a fresh, blemish-free ripe apple and place it into a pot with a splash of water, covering tightly with a lid to steam.",
            "Once tender, uncover the pot, remove the apple, and slip off the outer skin.",
            "Mash the soft apple pulp finely with a spoon together with a light sprinkle of sugar until smooth, then serve to the infant."
        ],
        "tags": {
            "dietary": ["vegetarian", "vegan", "baby_food"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["apple", "sugar"]
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
            "pdf_pages": [88],
            "printed_page_numbers": [162],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "3:3 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0158",
        "name_mm": "သီးနှံစုံ",
        "name_en": "Baby Fruit Mix",
        "description_mm": "အချိုမဲ့ဘီစကစ်ကို ငှက်ပျောသီး၊ လိမ္မော်ရည်တို့ဖြင့် ချောမွတ်အောင် ရောခြေထားသော ကလေးသဘာဝသစ်သီးသရေစာ။",
        "description_en": "Nutritious and appetizing baby fruit blend made by crushing unsweetened baby biscuits, stirring in fresh orange juice, and mashing with ripe or steamed banana.",
        "category": "dessert",
        "meal_types": ["snack", "breakfast"],
        "servings": 1,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0216",
                "name_mm": "ဘီစကစ်",
                "name_en": "Plain baby biscuit",
                "original_name": "ဘီစကစ် (အချိုမပါ)",
                "quantity": 2.0,
                "unit": "ချပ် (piece)",
                "original_quantity_text": "၂ ချပ်",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အချိုမပါ",
                "preparation_note_en": "unsweetened plain biscuit"
            },
            {
                "ingredient_id": "I0149",
                "name_mm": "ငှက်ပျောသီး",
                "name_en": "Banana",
                "original_name": "ငှက်ပျောသီးပြုတ် (သို့) အစိမ်း",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ပြုတ် သို့မဟုတ် အမှည့်အစိမ်း",
                "preparation_note_en": "steamed or ripe raw"
            },
            {
                "ingredient_id": "I0217",
                "name_mm": "လိမ္မော်ရည်",
                "name_en": "Orange juice",
                "original_name": "လိမ္မော်ရည်",
                "quantity": "အသင့်အတင့်",
                "unit": "အသင့်အတင့် (to taste)",
                "original_quantity_text": "အသင့်အတင့်",
                "normalized_quantity": 30.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "လတ်ဆတ်သော လိမ္မော်ရည်",
                "preparation_note_en": "freshly squeezed"
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": "အနည်းငယ်",
                "unit": "အနည်းငယ် (to taste)",
                "original_quantity_text": "အနည်းငယ်",
                "normalized_quantity": None,
                "normalized_unit": "to_taste",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "အချိုမဲ့ ဘီစကစ်ကို ပန်းကန်ထဲတွင် ကောင်းစွာ ကြိတ်ခြေထားပါ။",
            "ခြေထားသော ဘီစကစ်ထဲသို့ လိမ္မော်ရည်ကို စိုစွတ်ရုံမျှသာ ထည့်ကာ ငှက်ပျောသီး (သို့မဟုတ် ပန်းသီး) ဖြင့် ရောပြီး ချောမွတ်သည်အထိ သမအောင် မွှေပေးပါ။",
            "အချိုဓာတ် လိုအပ်ပါက သကြားအနည်းငယ် ထည့်သွင်းမွှေကာ ကလေးငယ်အား ကျွေးနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Finely crush the unsweetened baby biscuits in a clean bowl.",
            "Moisten the crushed biscuits with just enough fresh orange juice, add the soft banana (or apple), and mash until smooth and creamy.",
            "Taste and stir in a tiny pinch of sugar if needed, then feed directly to the baby."
        ],
        "tags": {
            "dietary": ["vegetarian", "baby_food"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["plain baby biscuit", "banana", "orange juice"]
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
            "pdf_pages": [88],
            "printed_page_numbers": [162],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "3:3 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0159",
        "name_mm": "ပီလောပီနံပူတင်း",
        "name_en": "Tapioca Pudding for Toddlers",
        "description_mm": "ပီလောပီနံမှုန့်၊ စပျစ်သီးခြောက်၊ ပေါင်မုန့်၊ နို့၊ ကြက်ဥနှင့် သကြားတို့ကို ဇာတိပ္ဖိုလ်သီးနံ့မွှေးကာ (၃) နာရီကြာ ပေါင်းထားသော မူကြိုအရွယ် ကလေးကြိုက် ပူတင်း။",
        "description_en": "Slow-steamed nursery pudding made with tapioca flour, soft bread, raisins, beaten egg, milk, and subtle nutmeg, gently steamed for three hours until rich and comforting.",
        "category": "dessert",
        "meal_types": ["dessert", "snack"],
        "servings": 6,
        "preparation_time_minutes": None,
        "cooking_time_minutes": 180,
        "ingredients": [
            {
                "ingredient_id": "I0218",
                "name_mm": "ပီလောပီနံမှုန့်",
                "name_en": "Tapioca starch (Cassava flour)",
                "original_name": "ပီလောပီနံမှုန့်",
                "quantity": 10.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၀ ကျပ်သား",
                "normalized_quantity": 163.3,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0033",
                "name_mm": "စပျစ်သီးခြောက်",
                "name_en": "Raisins",
                "original_name": "စပျစ်သီးခြောက်",
                "quantity": 15.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၅ ကျပ်သား",
                "normalized_quantity": 245.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0074",
                "name_mm": "ပေါင်မုန့်",
                "name_en": "Bread",
                "original_name": "ပေါင်မုန့်",
                "quantity": 7.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၇ ကျပ်သား",
                "normalized_quantity": 114.3,
                "normalized_unit": "g",
                "preparation_note_mm": "အတုံးသေးလှီးရန်",
                "preparation_note_en": "cubed"
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 10.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၀ ကျပ်သား",
                "normalized_quantity": 163.3,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": 4.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၄ ကျပ်သား",
                "normalized_quantity": 65.3,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0026",
                "name_mm": "ကြက်ဥ",
                "name_en": "Chicken egg",
                "original_name": "ကြက်ဥ",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခေါက်ထားရန်",
                "preparation_note_en": "beaten"
            },
            {
                "ingredient_id": "I0036",
                "name_mm": "နွားနို့",
                "name_en": "Cow milk",
                "original_name": "နို့",
                "quantity": 1.0,
                "unit": "နို့ဆီဘူး (ml)",
                "original_quantity_text": "၁ နို့ဆီဘူး",
                "normalized_quantity": 300.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0007",
                "name_mm": "ဇာတိပ္ဖိုလ်သီး",
                "name_en": "Nutmeg",
                "original_name": "ဇာတိပ္ဖိုလ်သီး (နုပ်နုပ်စဉ်း)",
                "quantity": "အနည်းငယ်",
                "unit": "အနည်းငယ် (to taste)",
                "original_quantity_text": "အနည်းငယ်",
                "normalized_quantity": None,
                "normalized_unit": "to_taste",
                "preparation_note_mm": "နုပ်နုပ်စဉ်းထားရန်",
                "preparation_note_en": "finely grated"
            },
            {
                "ingredient_id": "I0219",
                "name_mm": "သကာရည်",
                "name_en": "Caramel syrup (Golden syrup)",
                "original_name": "သကာရည်",
                "quantity": 1.0,
                "unit": "စားပွဲဇွန်း (tbsp / ml)",
                "original_quantity_text": "၁ စပဇ",
                "normalized_quantity": 15.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "ကြက်ဥကို ကောင်းစွာခေါက်ပြီး ပီလောပီနံမှုန့်၊ စပျစ်သီးခြောက်၊ ပေါင်မုန့်၊ သကြား၊ ဆီ၊ နို့၊ ဇာတိပ္ဖိုလ်သီးနှင့် သကာရည်တို့နှင့် ရောစပ်မွှေပေးပါ။",
            "သံပန်းကန် သို့မဟုတ် ပူတင်းခွက်တွင် ထောပတ်သုတ်၍ ရောစပ်ထားသော ပါဝင်ပစ္စည်းများကို အားလုံးထည့်ပြီး အပေါ်ယံတွင် ထောပတ်သုတ်စက္ကူ ဖုံးအုပ်ပါ။",
            "အဖုံးလုံအောင်ဖုံးပြီး ရေနွေးငွေ့ဖြင့် (၃) နာရီကြာ ပေါင်းပေးပါ။ ဤသည်မှာ မူကြိုအရွယ် ကလေးများ အလွန်နှစ်သက်သော အာဟာရပြည့် ပူတင်းဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Beat the egg thoroughly, then combine with tapioca flour, raisins, diced bread, sugar, oil, milk, grated nutmeg, and syrup.",
            "Grease a pudding mold or heatproof tin with butter, pour in the pudding mixture, and cover the surface with a sheet of buttered parchment paper.",
            "Seal with a tight lid and steam over simmering water for 3 hours until set; this makes a comforting, favorite treat for preschool toddlers."
        ],
        "tags": {
            "dietary": ["vegetarian", "baby_food"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["tapioca flour", "raisins", "bread", "cow milk", "egg", "sugar"]
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
            "pdf_pages": [88],
            "printed_page_numbers": [163],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "3:3 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0160",
        "name_mm": "ဆန်ပူတင်း",
        "name_en": "Nursery Rice Pudding",
        "description_mm": "ဆန်ကို နွားနို့၊ ထောပတ်၊ သကြားတို့ဖြင့် ပျော့ဖတ်သည်အထိ ချက်ပြီး ရှောက်ခွံရနံ့သင်းကာ အပေါ်ယံနီညိုရောင်သန်းအောင် ဖုတ်ထားသော ဆန်ပူတင်း။",
        "description_en": "Traditional creamy baked or steamed rice pudding, prepared by blanching rice, simmering with milk, butter, and sugar until tender, perfumed with lemon zest, and baked to a golden crust.",
        "category": "dessert",
        "meal_types": ["dessert", "snack"],
        "servings": 4,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0001",
                "name_mm": "ဆန်",
                "name_en": "Rice",
                "original_name": "ဆန်",
                "quantity": 4.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၄ ကျပ်သား",
                "normalized_quantity": 65.3,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 4.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၄ ကျပ်သား",
                "normalized_quantity": 65.3,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0036",
                "name_mm": "နွားနို့",
                "name_en": "Cow milk",
                "original_name": "နွားနို့",
                "quantity": 1.5,
                "unit": "နို့ဆီဘူး (ml)",
                "original_quantity_text": "၁ ၁/၂ နို့ဆီဘူး",
                "normalized_quantity": 450.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0002",
                "name_mm": "ထောပတ်",
                "name_en": "Butter",
                "original_name": "ထောပတ်",
                "quantity": 2.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ကျပ်သား",
                "normalized_quantity": 32.7,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0079",
                "name_mm": "ရှောက်သီး",
                "name_en": "Lemon / Citron",
                "original_name": "ရှောက်ခွံ (သို့) ငှက်ပျောရနံ့",
                "quantity": "အနည်းငယ်",
                "unit": "အနည်းငယ် (to taste)",
                "original_quantity_text": "အနည်းငယ်မျှ",
                "normalized_quantity": None,
                "normalized_unit": "to_taste",
                "preparation_note_mm": "ရှောက်ခွံခြစ်ထားရန် သို့မဟုတ် ငှက်ပျောရနံ့",
                "preparation_note_en": "lemon zest or banana essence"
            }
        ],
        "instructions_mm": [
            "ဆန်ကို ရေဖြင့် လျင်မြန်စွာဆေးပြီး ရေနွေးဆူဆူတွင် (၅) မိနစ်ခန့်စိမ်ကာ ထမင်းရေငှဲ့ပစ်ပါ။",
            "ရေစစ်ပြီးသော ဆန်ထဲသို့ နွားနို့၊ သကြား၊ ထောပတ်နှင့် ရှောက်ခွံရနံ့တို့ ရောစပ်ကာ ဆန်စေ့များ ပျော့ဖတ်နူးညံ့လာသည့် အနေအထားအထိ မွှေပေးပါ။",
            "မုန့်ဖုတ်ခွက်ထဲသို့ ထည့်၍ မီးအေးအေးဖြင့် ဖုတ်ပါ (သို့မဟုတ် ပေါင်းပါ)။ အပေါ်ယံ နီညိုရောင် သန်းလာလျှင် ကျက်နစ်ပါပြီ။"
        ],
        "instructions_en": [
            "Rinse the rice quickly in water, parboil in boiling water for 5 minutes, then drain off the water completely.",
            "Combine the drained rice with cow's milk, sugar, butter, and lemon zest or banana essence, simmering and stirring until the grains are swollen and soft.",
            "Transfer into a baking dish and bake over gentle heat (or steam) until the top turns a golden reddish-brown."
        ],
        "tags": {
            "dietary": ["vegetarian", "baby_food"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["rice", "cow milk", "butter", "sugar"]
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
            "pdf_pages": [88],
            "printed_page_numbers": [163],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "3:3 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0161",
        "name_mm": "ထောပတ်ကိတ်",
        "name_en": "Baby Butter Cake",
        "description_mm": "ထောပတ်၊ သကြား၊ ကြက်ဥ၊ နို့နှင့် ဂျုံမှုန့်တို့ကို စနစ်တကျ မွှေခေါက်၍ မီးအေးအေးဖြင့် ဖုတ်ထားသော နူးညံ့အိစက်သည့် ထောပတ်ကိတ်။",
        "description_en": "Delicate, melt-in-the-mouth butter sponge cake specially baked with fine wheat flour, fresh eggs, creamed butter, and milk, perfect for infants and afternoon tea.",
        "category": "dessert",
        "meal_types": ["dessert", "snack"],
        "servings": 6,
        "preparation_time_minutes": None,
        "cooking_time_minutes": 30,
        "ingredients": [
            {
                "ingredient_id": "I0002",
                "name_mm": "ထောပတ်",
                "name_en": "Butter",
                "original_name": "ထောပတ်",
                "quantity": 4.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၄ စပဇ",
                "normalized_quantity": 60.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 8.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၈ ကျပ်သား",
                "normalized_quantity": 130.6,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0026",
                "name_mm": "ကြက်ဥ",
                "name_en": "Chicken egg",
                "original_name": "ကြက်ဥ",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0043",
                "name_mm": "ဂျုံမှုန့်",
                "name_en": "Wheat flour",
                "original_name": "ဂျုံမှုန့်",
                "quantity": 7.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၇ ၁/၂ ကျပ်သား",
                "normalized_quantity": 122.5,
                "normalized_unit": "g",
                "preparation_note_mm": "ဆန်ခါချပြီး",
                "preparation_note_en": "sifted"
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 0.5,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁/၂ လဖဇ",
                "normalized_quantity": 2.5,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0194",
                "name_mm": "ဘေကင်ပေါင်ဒါ",
                "name_en": "Baking powder",
                "original_name": "ဘေကင်ပေါင်ဒါ",
                "quantity": 2.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၂ လဖဇ",
                "normalized_quantity": 10.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0036",
                "name_mm": "နွားနို့",
                "name_en": "Cow milk",
                "original_name": "နွားနို့",
                "quantity": 6.0,
                "unit": "စားပွဲဇွန်း (tbsp / ml)",
                "original_quantity_text": "၆ စပဇ",
                "normalized_quantity": 90.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "ထောပတ်ကို ခွက်တစ်ခုထဲတွင် ထည့်ပြီး ဇွန်းဖြင့် ကြိတ်ခြေပွတ်ပေးကာ သကြားကို ခပ်ဖြည်းဖြည်း တစ်စတစ်စ ထည့်၍ သမသွားအောင် ထပ်ခါတလဲလဲ ပွတ်တိုက်ပေးပါ။",
            "ဂျုံမှုန့်၊ ဆားနှင့် ဘေကင်ပေါင်ဒါတို့ကို ဆန်ခါဖြင့် (၃) ကြိမ်ခန့် စစ်ချထားပြီး ကြက်ဥထည့်ခေါက်ထားသော ထောပတ်သကြားနှစ်ထဲသို့ ဂျုံမှုန့်နှင့် နွားနို့ကို တစ်လှည့်စီ အနည်းငယ်စီ ထည့်၍ သမအောင် ရောမွှေပါ။",
            "အသင့်ပြင်ဆင်ထားသော ဆီသုတ်ပြီး ဆီစိမ်စက္ကူခင်းထားသည့် ကိတ်မုန့်ခွက်ထဲသို့ မုန့်နှစ်လောင်းထည့်ကာ မီးအေးအေးဖြင့် မုန့်ဖုတ်ဖိုတွင် နာရီဝက်ခန့် ဖုတ်ပါ။"
        ],
        "instructions_en": [
            "Cream the butter in a bowl with a wooden spoon, gradually adding sugar and beating continuously until light, pale, and fluffy.",
            "Sift the flour, salt, and baking powder three times; alternately fold the dry ingredients and cow's milk in small batches into the creamed egg and butter mixture until silky smooth.",
            "Pour into a greased cake tin lined with parchment paper and bake over gentle heat in a preheated oven for about 30 minutes until golden and springy."
        ],
        "tags": {
            "dietary": ["vegetarian", "baby_food"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["wheat flour", "butter", "sugar", "egg", "cow milk"]
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
            "pdf_pages": [88],
            "printed_page_numbers": [163],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "3:3 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0162",
        "name_mm": "ငါးရံ့ပေါင်း",
        "name_en": "Steamed Snakehead Fish for Kids",
        "description_mm": "အရိုးအရေခွံသန့်စင်ထားသော ငါးရံ့သားကို ကြက်သွန်နီ၊ ပေါင်မုန့်ကြွပ်၊ ကြက်ဥတို့ဖြင့် သမအောင်နယ်ကာ (၂) နာရီကြာ ပေါင်းထားသော နူးညံ့အရသာရှိသည့် ငါးပေါင်း။",
        "description_en": "Wholesome, tender steamed fish terrine made by blending boneless snakehead fish fillet with finely minced shallots, breadcrumbs, and egg, gently steamed in a buttered mold for two hours.",
        "category": "deep_fried",
        "meal_types": ["lunch", "dinner"],
        "servings": 4,
        "preparation_time_minutes": None,
        "cooking_time_minutes": 120,
        "ingredients": [
            {
                "ingredient_id": "I0220",
                "name_mm": "ငါးရံ့",
                "name_en": "Striped snakehead fish",
                "original_name": "ငါးရံ့",
                "quantity": 25.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၅ ကျပ်သား",
                "normalized_quantity": 408.3,
                "normalized_unit": "g",
                "preparation_note_mm": "အရိုးနှင့် အရေခွံ သန့်စင်ပြီး နုပ်နုပ်စဉ်းရန်",
                "preparation_note_en": "boneless skinless fillet, finely minced"
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ (ဥကြီး)",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "နုပ်နုပ်စဉ်းထားရန်",
                "preparation_note_en": "finely minced"
            },
            {
                "ingredient_id": "I0075",
                "name_mm": "ပေါင်မုန့်ကြွပ်မှုန့်",
                "name_en": "Breadcrumbs",
                "original_name": "မုန့်ကြွပ်မှုန့်",
                "quantity": 0.5,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၁/၂ နို့ဆီဘူး",
                "normalized_quantity": 125.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": "အနည်းငယ်",
                "unit": "အနည်းငယ် (to taste)",
                "original_quantity_text": "အနည်းငယ်",
                "normalized_quantity": None,
                "normalized_unit": "to_taste",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0039",
                "name_mm": "ငရုတ်ကောင်းမှုန့်",
                "name_en": "Ground black pepper",
                "original_name": "ငရုတ်ကောင်း",
                "quantity": "အနည်းငယ်",
                "unit": "အနည်းငယ် (to taste)",
                "original_quantity_text": "အနည်းငယ်",
                "normalized_quantity": None,
                "normalized_unit": "to_taste",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0026",
                "name_mm": "ကြက်ဥ",
                "name_en": "Chicken egg",
                "original_name": "ကြက်ဥ",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "အရိုးနှင့် အရေခွံ သန့်စင်ထားသော ငါးရံ့ကို နုပ်နုပ်စဉ်းပါ။ ကြက်သွန်နီကိုလည်း နုပ်နုပ်စဉ်းပြီး ပေါင်မုန့်ကြွပ်မှုန့်ဖြင့် ရောစပ်ပါ။",
            "ငါးသားစဉ်းပြီးထဲသို့ ကြက်သွန်နီ၊ မုန့်ကြွပ်မှုန့်၊ ဆား၊ ငရုတ်ကောင်းမှုန့်နှင့် ကြက်ဥတို့ ထည့်သွင်း၍ သမအောင် သေချာစွာ နယ်ပါ။",
            "ထောပတ်သုတ်ထားသော မုန့်ခွက်ထဲသို့ ထည့်ပြီး အပေါ်မှ ထောပတ်သုတ်ဆီစိမ်စက္ကူ ဖုံးအုပ်ကာ (၂) နာရီခန့် ပေါင်းလိုက်လျှင် ကလေးငယ်များ နှစ်သက်သော ငါးပေါင်း ရရှိပါမည်။"
        ],
        "instructions_en": [
            "Finely mince the skinned and deboned snakehead fish meat; finely mince the onion and blend with breadcrumbs.",
            "Mix the minced fish, breadcrumbs, onion, salt, black pepper, and beaten eggs together until thoroughly incorporated.",
            "Pack into a buttered baking dish, cover the top with a sheet of buttered parchment paper, and steam for about 2 hours until set and tender."
        ],
        "tags": {
            "dietary": ["pescatarian", "baby_food"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["striped snakehead fish", "breadcrumbs", "egg", "onion"]
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
            "pdf_pages": [89],
            "printed_page_numbers": [164],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "3:3 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0163",
        "name_mm": "နို့သစ်သီးဖျော်ရည်",
        "name_en": "Banana Milkshake for Kids",
        "description_mm": "ကျိုချက်ပြီး အအေးခံထားသော နို့ထဲသို့ ဖီးကြမ်းငှက်ပျောသီးခြေပြီးနှင့် ဗနီလာရနံ့ထည့်၍ နာနာခေါက်ခတ်ထားသော နို့သစ်သီးဖျော်ရည်။",
        "description_en": "Creamy, naturally sweet infant banana milkshake made with chilled boiled milk, mashed ripe banana, and fragrant vanilla essence, topped with frothed milk cream.",
        "category": "dessert",
        "meal_types": ["breakfast", "snack"],
        "servings": 2,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0036",
                "name_mm": "နွားနို့",
                "name_en": "Cow milk",
                "original_name": "နွားနို့",
                "quantity": 2.0,
                "unit": "နို့ဆီဘူး (ml)",
                "original_quantity_text": "၂ နို့ဆီဘူး",
                "normalized_quantity": 600.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ကျိုပြီး အအေးခံထားရန်",
                "preparation_note_en": "boiled and chilled"
            },
            {
                "ingredient_id": "I0149",
                "name_mm": "ငှက်ပျောသီး",
                "name_en": "Banana",
                "original_name": "ဖီးကြမ်းငှက်ပျောသီး",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခြေထားရန်",
                "preparation_note_en": "ripe, mashed"
            },
            {
                "ingredient_id": "I0213",
                "name_mm": "ဗနီလာရနံ့",
                "name_en": "Vanilla essence",
                "original_name": "ဗနီလာရနံ့",
                "quantity": 2.0,
                "unit": "စက် (drop / ml)",
                "original_quantity_text": "၁-၂ စက်",
                "normalized_quantity": 0.1,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "နို့ကို ကျိုချက်ပြီး ကောင်းစွာ အအေးခံထားပါ။ ဖီးကြမ်းငှက်ပျောသီးကို ဇွန်းဖြင့် ညက်ညက်ခြေထားပါ။",
            "အေးနေသော နို့၊ ခြေထားသော ငှက်ပျောသီးနှင့် ဗနီလာရနံ့တို့ကို ရောစပ်ကာ ပုလင်း သို့မဟုတ် ခွက်တွင် နာနာလှုပ်ခတ် ရိုက်ပေးပါ။",
            "ဖန်ခွက်တစ်ခုတွင် လက် ၃ လုံးအလိုခန့် အပြည့်မထည့်ဘဲ လောင်းထည့်ပြီး အပေါ်ယံတွင် မလိုင်ကို အမြှုပ်ပွအောင် ခေါက်တင်ကာ မွမ်းမံတည်ခင်းပါ။"
        ],
        "instructions_en": [
            "Boil the cow's milk and let it cool completely; mash the ripe Fee Gyan banana finely with a spoon.",
            "Combine the chilled milk, mashed banana, and vanilla essence, then shake or whisk vigorously until frothy and blended.",
            "Pour into glasses leaving about three fingers of headspace, and garnish the top with whipped frothy milk cream before serving."
        ],
        "tags": {
            "dietary": ["vegetarian", "baby_food"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["cow milk", "banana", "vanilla essence"]
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
            "pdf_pages": [89],
            "printed_page_numbers": [164],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "3:3 instruction parity verified.",
            "verified": True
        }
    },

    # --- BATCH 11: CONVALESCENT FOODS (R0164 - R0171) ---
    {
        "recipe_id": "R0164",
        "name_mm": "ကြက်စွပ်ပြုတ်",
        "name_en": "Convalescent Chicken Soup",
        "description_mm": "ကြက်နုနုကို ချင်း၊ ကြက်သွန်ဖြူ၊ ပဲငံပြာရည်၊ မုန်လာဥ၊ ဂေါ်ဖီထုပ်တို့ဖြင့် (၂) နာရီကြာ မီးအေးအေးငွေ့ငွေ့ကျိုပြီး နို့ဆမ်းစစ်ယူထားသော လူမမာအားဖြည့် ကြက်စွပ်ပြုတ်ကြည်။",
        "description_en": "Healing, nourishing chicken broth for invalids and convalescents, simmered gently for two hours with young chicken, ginger, garlic, radish, cabbage, and finished with boiled milk and pepper.",
        "category": "soup",
        "meal_types": ["lunch", "dinner"],
        "servings": 2,
        "preparation_time_minutes": None,
        "cooking_time_minutes": 120,
        "ingredients": [
            {
                "ingredient_id": "I0020",
                "name_mm": "ကြက်သား",
                "name_en": "Chicken meat",
                "original_name": "ကြက် (နုနု)",
                "quantity": 25.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၅ ကျပ်သား",
                "normalized_quantity": 408.3,
                "normalized_unit": "g",
                "preparation_note_mm": "အရေခွံခွာပြီး တုံးတစ်ထားရန်",
                "preparation_note_en": "skinned and portioned"
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
                "ingredient_id": "I0030",
                "name_mm": "ချင်း",
                "name_en": "Ginger",
                "original_name": "ချင်း (ခွဲ\" ထောင်းပြီး)",
                "quantity": 1.0,
                "unit": "လွှာ (piece)",
                "original_quantity_text": "၁ လွှာ",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ထောင်းပြီး",
                "preparation_note_en": "bruised and crushed"
            },
            {
                "ingredient_id": "I0022",
                "name_mm": "ကြက်သွန်ဖြူ",
                "name_en": "Garlic",
                "original_name": "ကြက်သွန်ဖြူ (ထောင်း)",
                "quantity": 2.0,
                "unit": "မြွှာ (clove)",
                "original_quantity_text": "၂ မြွှာ",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ထောင်းပြီး",
                "preparation_note_en": "crushed cloves"
            },
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ",
                "quantity": 1.5,
                "unit": "နို့ဆီဘူး (ml)",
                "original_quantity_text": "၁ ၁/၂ နို့ဆီဘူး",
                "normalized_quantity": 450.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0050",
                "name_mm": "ပဲငံပြာရည်",
                "name_en": "Soy sauce",
                "original_name": "ပဲငံပြာရည်",
                "quantity": 0.5,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / ml)",
                "original_quantity_text": "၁/၂ လဖဇ",
                "normalized_quantity": 2.5,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0133",
                "name_mm": "မုန်လာဥဖြူ",
                "name_en": "White radish",
                "original_name": "မုန်လာဥ",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0136",
                "name_mm": "ဂေါ်ဖီထုတ်",
                "name_en": "Cabbage",
                "original_name": "ဂေါ်ဖီထုပ်",
                "quantity": 1.0,
                "unit": "ရွက် (piece)",
                "original_quantity_text": "၁ ရွက်",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0047",
                "name_mm": "အရိုးပြုတ်ရည်",
                "name_en": "Bone broth",
                "original_name": "ပြုတ်ရည်",
                "quantity": 2.0,
                "unit": "နို့ဆီဘူး (ml)",
                "original_quantity_text": "၂ နို့ဆီဘူး",
                "normalized_quantity": 600.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0036",
                "name_mm": "နွားနို့",
                "name_en": "Cow milk",
                "original_name": "နွားနို့ (ကျိုပြီး)",
                "quantity": 0.5,
                "unit": "နို့ဆီဘူး (ml)",
                "original_quantity_text": "၁/၂ နို့ဆီဘူး",
                "normalized_quantity": 150.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ကျိုပြီး",
                "preparation_note_en": "boiled"
            }
        ],
        "instructions_mm": [
            "ရေဖြင့် လျင်မြန်စွာ ဆေးကြောထားသော ကြက်သားကို အရေခွံခွာ၍ တုံးတစ်ကာ ဆား၊ ချင်း၊ ကြက်သွန်ဖြူတို့ဖြင့် နယ်ပြီး ရေထည့်ကာ မီးအေးအေးဖြင့် ဖြည်းဖြည်းငွေ့ငွေ့ ဆူနေပါစေ။",
            "(၂) နာရီခန့် ကြာသောအခါ ပဲငံပြာရည်၊ မုန်လာဥနှင့် ဂေါ်ဖီထုပ်တို့ကို ထည့်ကာ နို့ထည့်ပြီး (၅) မိနစ်ခန့် ထား၍ ဖိုမှ ချပါ။",
            "ဟင်းချိုသောက် ပန်းကန်တွင် အဖတ်မပါစေဘဲ စစ်ထားသော ကြက်စွပ်ပြုတ် ရေကြည်ကို ပူပူနွေးနွေး ထည့်ပြီး ငရုတ်ကောင်းမှုန့် ပါသည်ဆိုရုံ ခတ်ကာ လူမမာထံ လင်ဗန်းဖြင့် တည်ခင်းကျွေးမွေးပါ။"
        ],
        "instructions_en": [
            "Quickly rinse the young chicken, skin and portion it, season with salt, crushed ginger, and garlic, then add water and bring to a slow, steady simmer over low heat.",
            "After gently simmering for about 2 hours, add the soy sauce, radish, and cabbage leaf, stir in the boiled milk, and take off the heat after 5 minutes.",
            "Strain the golden broth clearly without solids into a warm soup bowl, season with a delicate dusting of black pepper, and serve warm on a tray for the patient."
        ],
        "tags": {
            "dietary": ["convalescent_food"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["chicken meat", "ginger", "garlic", "cow milk", "white radish"]
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
            "pdf_pages": [90],
            "printed_page_numbers": [166],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "3:3 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0165",
        "name_mm": "ခရမ်းချဉ်သီးစွပ်ပြုတ်",
        "name_en": "Convalescent Tomato Soup",
        "description_mm": "ခရမ်းချဉ်သီးကို ပြုတ်ဆန်ခါတိုက်၍ ထောပတ်၊ ဂျုံမှုန့်၊ ပြုတ်ရည်၊ နို့တို့ဖြင့် ညက်ညောပျစ်နူးစွာ ကျိုချက်ထားသော လူမမာစား ခရမ်းချဉ်သီးစွပ်ပြုတ်။",
        "description_en": "Soothing, appetite-restoring cream of tomato soup for convalescents, prepared from sieved stewed tomatoes enriched with butter roux, clear broth, and fresh milk.",
        "category": "soup",
        "meal_types": ["lunch", "dinner"],
        "servings": 2,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0042",
                "name_mm": "ခရမ်းချဉ်သီး",
                "name_en": "Tomato",
                "original_name": "ခရမ်းချဉ်သီး",
                "quantity": 10.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၀ ကျပ်သား",
                "normalized_quantity": 163.3,
                "normalized_unit": "g",
                "preparation_note_mm": "ပြုတ်ပြီး ဆန်ခါတိုက်ရန်",
                "preparation_note_en": "stewed and strained through a sieve"
            },
            {
                "ingredient_id": "I0002",
                "name_mm": "ထောပတ်",
                "name_en": "Butter",
                "original_name": "ထောပတ်",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0043",
                "name_mm": "ဂျုံမှုန့်",
                "name_en": "Wheat flour",
                "original_name": "ဂျုံမှုန့် (ဆန်ခါချပြီး)",
                "quantity": 1.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ စပဇ",
                "normalized_quantity": 15.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ဆန်ခါချပြီး",
                "preparation_note_en": "sifted"
            },
            {
                "ingredient_id": "I0036",
                "name_mm": "နွားနို့",
                "name_en": "Cow milk",
                "original_name": "နွားနို့",
                "quantity": 0.17,
                "unit": "နို့ဆီဘူး (ml)",
                "original_quantity_text": "၁/၆ နို့ဆီဘူး",
                "normalized_quantity": 50.0,
                "normalized_unit": "ml",
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
                "ingredient_id": "I0047",
                "name_mm": "အရိုးပြုတ်ရည်",
                "name_en": "Bone broth",
                "original_name": "ပြုတ်ရည်",
                "quantity": 2.0,
                "unit": "နို့ဆီဘူး (ml)",
                "original_quantity_text": "၂ နို့ဆီဘူး",
                "normalized_quantity": 600.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "ခရမ်းချဉ်သီးကို ရေမြုပ်ရုံဖြင့် ပြုတ်ပြီး နူးစပြုလျှင် ရေစစ်ကာ ဆန်ခါတွင် ခြေ၍ အနှစ်ယူပြီး ပြုတ်ရည်ကို အသင့်ချန်ထားပါ။",
            "အိုးတွင် ထောပတ်ကို အရည်ဖျော်ပြီး ဂျုံမှုန့်ရော၍ မွှေကာ ခရမ်းချဉ်သီးအနှစ်နှင့် ပြုတ်ရည်တို့ကိုပါ ထည့်သွင်းမွှေပေးပါ။",
            "(၅) မိနစ်ခန့် ကြာသောအခါ နွားနို့၊ သကြားနှင့် ဆားတို့ကို ထည့်မွှေ၍ ပွက်ပွက်ဆူလျှင် ဖိုမှချကာ လူမမာစားချင်ဖွယ် နွေးနွေးထွေးထွေး တိုက်ကျွေးပါ။"
        ],
        "instructions_en": [
            "Boil the tomatoes in just enough water until tender, drain while reserving the cooking liquid, and press the pulp through a fine sieve.",
            "Melt the butter in a saucepan, stir in the flour to form a smooth roux, then gradually whisk in the tomato purée and reserved broth.",
            "After simmering for 5 minutes, stir in milk, sugar, and salt; as soon as it boils up, remove from heat and serve warm to stimulate the patient's appetite."
        ],
        "tags": {
            "dietary": ["vegetarian", "convalescent_food"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["tomato", "butter", "wheat flour", "cow milk", "bone broth"]
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
            "pdf_pages": [90],
            "printed_page_numbers": [166],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "3:3 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0166",
        "name_mm": "အာလူးစွပ်ပြုတ်",
        "name_en": "Convalescent Potato Soup",
        "description_mm": "အာလူးကြီးကို နူးအိအောင်ပြုတ်ခြေပြီး နွားနို့ပူပူ၊ ဆားတို့ဖြင့် ဆူအောင်ကျိုထားသော အစာကြေလွယ် လူမမာအာလူးစွပ်ပြုတ်။",
        "description_en": "Gentle, easily assimilable cream of potato soup for recovering patients, prepared from boiled mashed potatoes whisked with warm milk and lightly seasoned with salt.",
        "category": "soup",
        "meal_types": ["lunch", "dinner"],
        "servings": 1,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0159",
                "name_mm": "အာလူး",
                "name_en": "Potato",
                "original_name": "အာလူး (အလုံးကြီး)",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ကျက်အောင်ပြုတ် အခွံခွာခြေရန်",
                "preparation_note_en": "boiled, peeled, and mashed"
            },
            {
                "ingredient_id": "I0036",
                "name_mm": "နွားနို့",
                "name_en": "Cow milk",
                "original_name": "နွားနို့",
                "quantity": 0.17,
                "unit": "နို့ဆီဘူး (ml)",
                "original_quantity_text": "၁/၆ နို့ဆီဘူး",
                "normalized_quantity": 50.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ပူအောင်နွှေးထားရန်",
                "preparation_note_en": "warmed"
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": "အနည်းငယ်",
                "unit": "အနည်းငယ် (to taste)",
                "original_quantity_text": "အနည်းငယ်",
                "normalized_quantity": None,
                "normalized_unit": "to_taste",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "အာလူးကို ရေဆေးပြီး ကျက်အောင်ပြုတ်ကာ အခွံခွာ၍ ကြေညက်သွားအောင် ခြေထားပါ။",
            "နွားနို့ကို ပူအောင်လုပ်ပြီး ခြေထားသော အာလူးနှင့် ရောစပ်ကာ ဆားအနည်းငယ် ထည့်၍ ဆူသည်အထိ ပြုတ်ပါ။",
            "ပူပူနွေးနွေး တိုက်ကျွေးနိုင်ပြီး လူမမာ၏ အခြေအနေပေါ် မူတည်၍ ငရုတ်ကောင်း သို့မဟုတ် ထောပတ်ကြက်သွန်နီဆီသတ် အနည်းငယ် ထည့်သွင်း ကျွေးမွေးနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Wash the potato and boil until tender, peel off the skin, and mash completely until smooth.",
            "Heat the milk, whisk together with the mashed potato, season with a pinch of salt, and bring gently to a simmer.",
            "Serve piping hot to the patient; if permitted by the patient's recovery diet, a dusting of black pepper or a teaspoon of butter-sautéed shallot oil may be stirred in."
        ],
        "tags": {
            "dietary": ["vegetarian", "convalescent_food"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["potato", "cow milk", "salt"]
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
            "pdf_pages": [90],
            "printed_page_numbers": [167],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "3:3 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0167",
        "name_mm": "ဆိတ်ရိုးစွပ်ပြုတ်",
        "name_en": "Convalescent Mutton Bone Broth",
        "description_mm": "အသားကပ်ဆိတ်ရိုးကို ချင်း၊ ကြက်သွန်ဖြူ၊ ပဲငံပြာရည်တို့ဖြင့် (၃) နာရီကြာ မီးအေးအေးကျိုပြီး အာလူး၊ ပန်းဂေါ်ဖီ၊ မုန်လာဥဝါတို့ဖြင့် ချက်ထားသော လူမမာအားဖြည့် ဆိတ်ရိုးစွပ်ပြုတ်။",
        "description_en": "Deeply restorative mutton marrow bone soup for invalid recovery, slow-simmered for three hours with crushed marrow bones, aromatics, potatoes, carrots, and cauliflower.",
        "category": "soup",
        "meal_types": ["lunch", "dinner"],
        "servings": 2,
        "preparation_time_minutes": None,
        "cooking_time_minutes": 180,
        "ingredients": [
            {
                "ingredient_id": "I0221",
                "name_mm": "ဆိတ်ရိုး",
                "name_en": "Mutton soup bone",
                "original_name": "ဆိတ်ရိုး (ခပ်ကြီးကြီး)",
                "quantity": 1.0,
                "unit": "ရိုး (piece)",
                "original_quantity_text": "၁ ရိုး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ကွဲအောင်ထုရိုက်ထားရန်",
                "preparation_note_en": "cracked to expose marrow"
            },
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ",
                "quantity": "လိုအပ်သရွေ့",
                "unit": "လိုအပ်သရွေ့ (as needed)",
                "original_quantity_text": "လိုအပ်သရွေ့",
                "normalized_quantity": None,
                "normalized_unit": "to_taste",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0030",
                "name_mm": "ချင်း",
                "name_en": "Ginger",
                "original_name": "ချင်း (ထောင်းပြီး)",
                "quantity": 2.0,
                "unit": "လွှာ (piece)",
                "original_quantity_text": "၂ လွှာ",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ထောင်းပြီး",
                "preparation_note_en": "crushed"
            },
            {
                "ingredient_id": "I0022",
                "name_mm": "ကြက်သွန်ဖြူ",
                "name_en": "Garlic",
                "original_name": "ကြက်သွန်ဖြူ (ထောင်းပြီး)",
                "quantity": 2.0,
                "unit": "မြွှာ (clove)",
                "original_quantity_text": "၂ မြွှာ",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ထောင်းပြီး",
                "preparation_note_en": "crushed"
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 0.5,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁/၂ လဖဇ",
                "normalized_quantity": 2.5,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0050",
                "name_mm": "ပဲငံပြာရည်",
                "name_en": "Soy sauce",
                "original_name": "ပဲငံပြာရည်",
                "quantity": 0.5,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / ml)",
                "original_quantity_text": "၁/၂ လဖဇ",
                "normalized_quantity": 2.5,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0159",
                "name_mm": "အာလူး",
                "name_en": "Potato",
                "original_name": "အာလူး (ပါးပါးလှီးပြီး)",
                "quantity": 3.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၃ ကျပ်သား",
                "normalized_quantity": 49.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ပါးပါးလှီးပြီး",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0108",
                "name_mm": "ပန်းဂေါ်ဖီ",
                "name_en": "Cauliflower",
                "original_name": "ပန်းဂေါ်ဖီ (ပါးပါးလှီးပြီး)",
                "quantity": 3.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၃ ကျပ်သား",
                "normalized_quantity": 49.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ပါးပါးလှီးပြီး",
                "preparation_note_en": "sliced"
            },
            {
                "ingredient_id": "I0014",
                "name_mm": "မုန်လာဥနီ",
                "name_en": "Carrot",
                "original_name": "မုန်လာဥဝါ (တုံးတစ်ပြီး)",
                "quantity": 2.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ကျပ်သား",
                "normalized_quantity": 32.7,
                "normalized_unit": "g",
                "preparation_note_mm": "တုံးတစ်ပြီး",
                "preparation_note_en": "cubed"
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ (လှီးစိတ်ပြီး)",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "လှီးစိတ်ပြီး",
                "preparation_note_en": "quartered"
            }
        ],
        "instructions_mm": [
            "အရိုးနား ကပ်နေသော အသားများ ပါရှိသည့် ဆိတ်ရိုးကို ကွဲအောင် ထုရိုက်ပြီး ရေသင့်ရုံဖြင့် ချင်း၊ ကြက်သွန်ဖြူ၊ ဆားနှင့် ပဲငံပြာရည်တို့ ထည့်၍ မီးအေးအေးဖြင့် (၃) နာရီခန့် အိုးဖုံးမဖွင့်ဘဲ ကျိုပါ။",
            "ရိုးတွင်းခြင်ဆီများ ပေါ်ထွက် နူးအိလာပြီးနောက် အဖုံးဖွင့်၍ ဆိတ်ရိုးများကို ဆယ်ယူပစ်ပါ။",
            "စွပ်ပြုတ်ရည်ထဲသို့ အာလူး၊ ပန်းဂေါ်ဖီနှင့် မုန်လာဥဝါတို့ ထည့်၍ အားလုံးနူးလျှင် ကြက်သွန်နီ ထည့်ကာ ပွက်ပွက်ဆူလာသောအခါ ငရုတ်ကောင်းမှုန့် အနည်းငယ် ခတ်၍ တိုက်ကျွေးပါ။"
        ],
        "instructions_en": [
            "Crack the meaty mutton bone to expose the rich marrow, add water, crushed ginger, garlic, salt, and soy sauce, and simmer tightly covered over low heat for about 3 hours.",
            "Once the bone marrow and meat juices have thoroughly rendered into the stock, uncover and remove the spent bones.",
            "Add the sliced potatoes, cauliflower, and carrots to the broth, cook until tender, add the onions, and finish with a dusting of freshly ground black pepper before serving."
        ],
        "tags": {
            "dietary": ["convalescent_food"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["mutton bone", "potato", "cauliflower", "carrot", "ginger"]
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
            "pdf_pages": [90],
            "printed_page_numbers": [167],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "3:3 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0168",
        "name_mm": "ငါးကတ်တလက်",
        "name_en": "Convalescent Fish Cutlet",
        "description_mm": "ငါးရံ့အသားကို အာလူးပြုတ်ခြေ၊ ကြက်သွန်ဖြူ၊ ကြက်သွန်နီတို့ဖြင့် နယ်ပြီး အပြားဝိုင်းလုပ်ကာ ကြက်ဥအကာလူး မုန့်ကြွပ်ကပ်၍ ဆီအနည်းငယ်ဖြင့် ဝါအောင်ကြော်ထားသော ငါးကတ်တလက်။",
        "description_en": "Light and appetizing pan-fried fish patties for convalescents, prepared from tender boiled snakehead fish flaked with mashed potatoes, coated with egg white and breadcrumbs, and gently fried.",
        "category": "deep_fried",
        "meal_types": ["lunch", "dinner", "snack"],
        "servings": 2,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0220",
                "name_mm": "ငါးရံ့",
                "name_en": "Striped snakehead fish",
                "original_name": "ငါးရံ့",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.6,
                "normalized_unit": "g",
                "preparation_note_mm": "ပြုတ်၍ အရိုးစင်အောင်ထွင်ရန်",
                "preparation_note_en": "boiled and deboned"
            },
            {
                "ingredient_id": "I0159",
                "name_mm": "အာလူး",
                "name_en": "Potato",
                "original_name": "အာလူး (အလုံးကြီး)",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.6,
                "normalized_unit": "g",
                "preparation_note_mm": "ပြုတ်ပြီး အခွံနွှာထောင်းရန်",
                "preparation_note_en": "boiled, peeled, and mashed"
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 0.5,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁/၂ လဖဇ",
                "normalized_quantity": 2.5,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0039",
                "name_mm": "ငရုတ်ကောင်းမှုန့်",
                "name_en": "Ground black pepper",
                "original_name": "ငရုတ်ကောင်းမှုန့်",
                "quantity": "အနည်းငယ်",
                "unit": "တို့ (pinch / to taste)",
                "original_quantity_text": "၁ တို့",
                "normalized_quantity": None,
                "normalized_unit": "to_taste",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0022",
                "name_mm": "ကြက်သွန်ဖြူ",
                "name_en": "Garlic",
                "original_name": "ကြက်သွန်ဖြူ (နုပ်နုပ်စဉ်းပြီး)",
                "quantity": 2.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၂ လဖဇ",
                "normalized_quantity": 10.0,
                "normalized_unit": "g",
                "preparation_note_mm": "နုပ်နုပ်စဉ်းပြီး",
                "preparation_note_en": "finely minced"
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ (နုပ်နုပ်စဉ်းပြီး)",
                "quantity": 2.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၂ လဖဇ",
                "normalized_quantity": 10.0,
                "normalized_unit": "g",
                "preparation_note_mm": "နုပ်နုပ်စဉ်းပြီး",
                "preparation_note_en": "finely minced"
            },
            {
                "ingredient_id": "I0026",
                "name_mm": "ကြက်ဥ",
                "name_en": "Chicken egg",
                "original_name": "ကြက်ဥ (အကာရည်)",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အကာရည်သာသုံးရန်",
                "preparation_note_en": "egg white only"
            },
            {
                "ingredient_id": "I0075",
                "name_mm": "ပေါင်မုန့်ကြွပ်မှုန့်",
                "name_en": "Breadcrumbs",
                "original_name": "မုန့်ကြွပ်မှုန့်",
                "quantity": 3.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၃ စပဇ",
                "normalized_quantity": 45.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "ငါးတွင်ရှိသော အာဟာရဓာတ်များ မကျန်ရစ်စေရန် ငါးရံ့ကို ရေနည်းနည်းဖြင့် ပြုတ်၍ အရိုးစင်အောင် ထွင်ထားပါ။ အာလူးကိုလည်း ပြုတ်ပြီး အခွံနွှာကာ ညက်အောင် ထောင်းထားပါ။",
            "ထောင်းထားသော အာလူးနှင့် ငါးအသားတို့ကို သမအောင် ရောစပ်ပြီး ဆား၊ ငရုတ်ကောင်းမှုန့်၊ ကြက်သွန်နီ၊ ကြက်သွန်ဖြူတို့ဖြင့် နယ်ကာ အပြားဝိုင်းကလေးများ ပြုလုပ်ပါ။",
            "ပြုလုပ်ထားသော အပြားဝိုင်းများကို ကြက်ဥအကာရည်လူး၍ မုန့်ကြွပ်မှုန့် နှံ့အောင် ဖြူးကပ်ပြီး ဆီနည်းနည်းဖြင့် ရွှေဝါရောင်သန်းအောင် ကြော်ကာ လူမမာစားချင်ဖွယ် ပြင်ဆင်ကျွေးမွေးပါ။"
        ],
        "instructions_en": [
            "Poach the snakehead fish in minimal water to retain all nutrients, then flake and thoroughly debone; boil the potatoes until soft, peel, and mash finely.",
            "Mix the flaked fish and mashed potato together with salt, pepper, minced shallot, and garlic, kneading into smooth round patties.",
            "Dip each patty into beaten egg white, coat evenly in fine breadcrumbs, shallow-fry in a small amount of oil until golden brown, and present temptingly to the invalid."
        ],
        "tags": {
            "dietary": ["pescatarian", "convalescent_food"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["striped snakehead fish", "potato", "breadcrumbs", "egg", "shallots"]
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
            "pdf_pages": [91],
            "printed_page_numbers": [168],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "3:3 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0169",
        "name_mm": "ငါးဆန်ပြုတ်",
        "name_en": "Convalescent Fish Gruel (Fish Congee)",
        "description_mm": "ဆန်ကို ရေ (၄) ဆဖြင့် ကျိုပြီး ငါးရံ့အသားလွှာ၊ ပဲငံပြာရည်၊ ကြက်သွန်ဖြူကြော်၊ ငရုတ်ကောင်းတို့ဖြင့် ချက်ထားသော အစာကြေလွယ် သဘာဝငါးဆန်ပြုတ်။",
        "description_en": "Comforting, restorative rice congee simmered with thinly sliced fresh snakehead fish fillet, seasoned with light soy sauce, and garnished with golden garlic oil and black pepper without MSG.",
        "category": "soup",
        "meal_types": ["breakfast", "lunch", "dinner"],
        "servings": 2,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0220",
                "name_mm": "ငါးရံ့",
                "name_en": "Striped snakehead fish",
                "original_name": "ငါးရံ့ (အသားထွင်ပြီး)",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.6,
                "normalized_unit": "g",
                "preparation_note_mm": "အရေခွံဖယ် အရိုးမပါအောင် ခပ်ပါးပါးလှီးထားရန်",
                "preparation_note_en": "skinned, boneless fillet, thinly sliced"
            },
            {
                "ingredient_id": "I0001",
                "name_mm": "ဆန်",
                "name_en": "Rice",
                "original_name": "ဆန်",
                "quantity": 0.25,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၁/၄ နို့ဆီဘူး",
                "normalized_quantity": 62.5,
                "normalized_unit": "g",
                "preparation_note_mm": "ရေစင်အောင်ဆေးထားရန်",
                "preparation_note_en": "washed thoroughly"
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 0.75,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၃/၄ လဖဇ",
                "normalized_quantity": 3.8,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0050",
                "name_mm": "ပဲငံပြာရည်",
                "name_en": "Soy sauce",
                "original_name": "ပဲငံပြာရည်",
                "quantity": 0.5,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / ml)",
                "original_quantity_text": "၁/၂ လဖဇ",
                "normalized_quantity": 2.5,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0022",
                "name_mm": "ကြက်သွန်ဖြူ",
                "name_en": "Garlic",
                "original_name": "ကြက်သွန်ဖြူကြော် (ထောင်းပြီး)",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ကြော်ထောင်းထားရန်",
                "preparation_note_en": "fried and crushed"
            },
            {
                "ingredient_id": "I0039",
                "name_mm": "ငရုတ်ကောင်းမှုန့်",
                "name_en": "Ground black pepper",
                "original_name": "ငရုတ်ကောင်းမှုန့်",
                "quantity": "အနည်းငယ်",
                "unit": "တို့ (pinch / to taste)",
                "original_quantity_text": "၁ တို့",
                "normalized_quantity": None,
                "normalized_unit": "to_taste",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "ငါးရံ့ကို အရေခွံဖယ်ရှား၍ အရိုးမပါစေဘဲ ခပ်ပါးပါးလှီးထားပါ။ ဆန်ကို ရေစင်အောင်ဆေးပြီး ဆန်အထက်မှ ရေ (၄) ဆခန့် ထည့်ကာ ဆူပွက်အောင် တည်ပါ။",
            "ဆန်စေ့များ နူးအိလာသောအခါ လှီးထားသော ငါးရံ့အသားများကို ထည့်မွှေပြီး ပဲငံပြာရည်နှင့် ဆားတို့ ထည့်ကာ ပွက်ပွက်ဆူအောင် ချက်ပါ။",
            "ဆန်ပြုတ်ကျက်လျှင် ဆီချက်၊ ကြက်သွန်ဖြူကြော်နှင့် ငရုတ်ကောင်းမှုန့်တို့ အပေါ်မှ ဖြူး၍ တိုက်ကျွေးပါ (အချိုမှုန့် လုံးဝမသုံးပါနှင့်)။"
        ],
        "instructions_en": [
            "Skin and bone the snakehead fish, slicing the flesh thinly; wash the rice cleanly twice, add four times its volume of water, and bring to a simmer.",
            "When the rice grains have softened into a velvety congee, stir in the fish slices, soy sauce, and salt, simmering until the fish is delicately cooked through.",
            "Ladle into a bowl, garnish with a drizzle of garlic oil, crispy fried garlic, and black pepper, and serve warm without adding MSG."
        ],
        "tags": {
            "dietary": ["pescatarian", "convalescent_food"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["rice", "striped snakehead fish", "garlic oil", "black pepper"]
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
            "pdf_pages": [91],
            "printed_page_numbers": [168],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "3:3 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0170",
        "name_mm": "ပေါင်မုန့်ပူတင်း",
        "name_en": "Convalescent Bread Pudding",
        "description_mm": "ပေါင်မုန့်ချပ်ကို နွားနို့စိမ်ခြေ၍ သကြား၊ ကြက်ဥ၊ ထောပတ်တို့ဖြင့် ရောစပ်ကာ ဖုတ် သို့မဟုတ် ပေါင်းထားသော လူမမာစား ပေါင်မုန့်ပူတင်း။",
        "description_en": "Light and comforting invalid bread pudding made by soaking white bread in warm milk, beaten with egg, sugar, and butter, then gently baked or steamed in a small ramekin.",
        "category": "dessert",
        "meal_types": ["dessert", "snack"],
        "servings": 1,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0074",
                "name_mm": "ပေါင်မုန့်",
                "name_en": "Bread",
                "original_name": "ပေါင်မုန့် (လက်မဝက်ခန့်အထူ)",
                "quantity": 1.0,
                "unit": "ချပ် (piece)",
                "original_quantity_text": "၁ ချပ်",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "လက်မဝက်ခန့်အထူ",
                "preparation_note_en": "half-inch thick slice"
            },
            {
                "ingredient_id": "I0036",
                "name_mm": "နွားနို့",
                "name_en": "Cow milk",
                "original_name": "နွားနို့",
                "quantity": 0.17,
                "unit": "နို့ဆီဘူး (ml)",
                "original_quantity_text": "၁/၆ နို့ဆီဘူး",
                "normalized_quantity": 50.0,
                "normalized_unit": "ml",
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
                "ingredient_id": "I0026",
                "name_mm": "ကြက်ဥ",
                "name_en": "Chicken egg",
                "original_name": "ကြက်ဥ",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခေါက်ထားရန်",
                "preparation_note_en": "beaten"
            },
            {
                "ingredient_id": "I0002",
                "name_mm": "ထောပတ်",
                "name_en": "Butter",
                "original_name": "ထောပတ်",
                "quantity": 0.5,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁/၂ လဖဇ",
                "normalized_quantity": 2.5,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "ပေါင်မုန့်ကို နွားနို့နှင့် စိမ်ထားပြီး ပွလာသောအခါ ဇွန်းဖြင့် ကြေညက်အောင် ခြေပါ။",
            "ကျန်ရှိသော နို့ထဲသို့ သကြားထည့်၍ ရောစပ်ပြီး ကြက်ဥခေါက်ထားသည်နှင့် အမွှေးရနံ့တို့ကို ထည့်သွင်း မွှေပေးပါ။",
            "ထောပတ်သုတ်ထားသော မုန့်ဖုတ်ပန်းကန်ထဲသို့ အားလုံးရောထည့်ကာ မီးအေးအေးဖြင့် ဖုတ်ပါ (သို့မဟုတ် ပေါင်းပါ)။"
        ],
        "instructions_en": [
            "Soak the bread slice in a portion of warm milk, and mash thoroughly once softened.",
            "Dissolve the sugar into the remaining milk, then whisk together with the beaten egg and aromatic vanilla essence.",
            "Pour the mixture into a buttered baking cup and bake over gentle heat (or steam) until set and fragrant."
        ],
        "tags": {
            "dietary": ["vegetarian", "convalescent_food"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["bread", "cow milk", "egg", "sugar", "butter"]
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
            "pdf_pages": [91],
            "printed_page_numbers": [169],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "3:3 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0171",
        "name_mm": "ကြက်ဥပူတင်း",
        "name_en": "Convalescent Steamed Egg Custard",
        "description_mm": "ကြက်ဥကို သကြား၊ ဗနီလာရနံ့၊ နွားနို့တို့ဖြင့် ခေါက်မွှေပြီး ရေနွေးငွေ့ဖြင့် ချိုင့် (သို့) ပန်းကန်တွင် နူးညံ့အိစက်စွာ ပေါင်းထားသော ကြက်ဥပူတင်း။",
        "description_en": "The final recipe of the cookbook: delicate steamed egg custard for invalids, prepared by whisking fresh eggs with sugar, warm milk, and vanilla, then steamed until softly set and silky smooth.",
        "category": "dessert",
        "meal_types": ["dessert", "snack"],
        "servings": 2,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0026",
                "name_mm": "ကြက်ဥ",
                "name_en": "Chicken egg",
                "original_name": "ကြက်ဥ",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 1.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ စပဇ",
                "normalized_quantity": 15.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0213",
                "name_mm": "ဗနီလာရနံ့",
                "name_en": "Vanilla essence",
                "original_name": "ဗနီလာရနံ့",
                "quantity": 1.0,
                "unit": "စက် (drop / ml)",
                "original_quantity_text": "၁ စက်",
                "normalized_quantity": 0.05,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0036",
                "name_mm": "နွားနို့",
                "name_en": "Cow milk",
                "original_name": "နွားနို့",
                "quantity": 0.17,
                "unit": "နို့ဆီဘူး (ml)",
                "original_quantity_text": "၁/၆ နို့ဆီဘူး",
                "normalized_quantity": 50.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "ခွက်တစ်ခုထဲတွင် ကြက်ဥထည့်၍ နာနာခေါက်ပြီး ပွလာလျှင် သကြားထည့်ခေါက်ပါ။",
            "ဗနီလာရနံ့နှင့် နွားနို့ကို ရောစပ်ပြီး ကြက်ဥထဲသို့ ထည့်သွင်းကာ သမအောင် ရောခေါက်ပါ။",
            "အဖုံးပါသော ချိုင့် သို့မဟုတ် ပန်းကန်လုံးထဲသို့ ထည့်ပြီး အဖုံးလုံအောင်ဖုံးကာ ရေနွေးငွေ့ဖြင့် (သို့မဟုတ် နှစ်ထပ်ပေါင်းအိုးဖြင့်) နူးညံ့ချောမွတ်စွာ ကျက်နစ်သည်အထိ ပေါင်းပါ။"
        ],
        "instructions_en": [
            "Break the eggs into a bowl, whisk vigorously until frothy, then beat in the sugar.",
            "Mix the vanilla essence into the warm milk, and whisk smoothly into the beaten egg mixture.",
            "Pour into a covered lidded container or heatproof bowl covered with a weighted plate, and steam over gentle water (or in a double steamer) until softly set and silky."
        ],
        "tags": {
            "dietary": ["vegetarian", "convalescent_food"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["egg", "cow milk", "sugar", "vanilla essence"]
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
            "pdf_pages": [91],
            "printed_page_numbers": [169],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "3:3 instruction parity verified.",
            "verified": True
        }
    }
]
