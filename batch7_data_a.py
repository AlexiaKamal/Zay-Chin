# -*- coding: utf-8 -*-
"""
Batch 7 Part A: Traditional Myanmar Sweets & Desserts (မုန့်ပဲသွားရည်စာများ)
Covers Agar-Agar Jellies (ကျောက်ကျောများ) & Sanwin Makin Cakes (ဆနွင်းမကင်းများ)
Recipes R0087 to R0100 (Book pp. 117-123 / PDF pp. 64-68).
"""

NEW_INGREDIENTS_BATCH7_A = [
    {
        "ingredient_id": "I0147",
        "name_mm": "ကျောက်ကျောမှုန့်",
        "name_en": "Agar-agar powder",
        "aliases_mm": ["ကျောက်ကျော", "ကျောက်ကျောထုပ်"],
        "aliases_en": ["agar powder", "china grass"],
        "category": "dry_goods",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0148",
        "name_mm": "ပန်းသီး",
        "name_en": "Apple",
        "aliases_mm": [],
        "aliases_en": ["fresh apple"],
        "category": "produce",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0149",
        "name_mm": "ငှက်ပျောသီး",
        "name_en": "Banana",
        "aliases_mm": ["သီးမွှေးငှက်ပျော", "ရခိုင်ငှက်ပျော"],
        "aliases_en": ["ripe banana", "cooking banana"],
        "category": "produce",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0150",
        "name_mm": "စတော်ဘယ်ရီ",
        "name_en": "Strawberry",
        "aliases_mm": ["စတော်ဘယ်ရီသီး"],
        "aliases_en": ["fresh strawberry"],
        "category": "produce",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0151",
        "name_mm": "သစ်ခွဖျော်ရည်",
        "name_en": "Orchid nectar syrup",
        "aliases_mm": ["သစ်ခွရည်"],
        "aliases_en": ["floral syrup", "scented nectar syrup"],
        "category": "condiment",
        "default_unit": "ml"
    },
    {
        "ingredient_id": "I0152",
        "name_mm": "လိုင်ချီး",
        "name_en": "Lychee syrup",
        "aliases_mm": ["လိုင်ချီးရည်", "လိုင်ချီးသီး"],
        "aliases_en": ["litchi syrup"],
        "category": "condiment",
        "default_unit": "ml"
    },
    {
        "ingredient_id": "I0153",
        "name_mm": "စပျစ်ရည်",
        "name_en": "Grape syrup",
        "aliases_mm": ["စပျစ်ဖျော်ရည်"],
        "aliases_en": ["grape juice syrup"],
        "category": "condiment",
        "default_unit": "ml"
    },
    {
        "ingredient_id": "I0154",
        "name_mm": "အစာအရောင်ဆိုးဆေး",
        "name_en": "Food coloring",
        "aliases_mm": ["အစိမ်းရောင်ဆေး", "အနီရောင်ဆေး"],
        "aliases_en": ["edible dye", "culinary coloring"],
        "category": "condiment",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0155",
        "name_mm": "ချောကလက်မှုန့်",
        "name_en": "Cocoa powder",
        "aliases_mm": ["ကိုကိုးမှုန့်"],
        "aliases_en": ["chocolate powder", "cacao powder"],
        "category": "dry_goods",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0156",
        "name_mm": "သာကူစေ့",
        "name_en": "Sago pearls",
        "aliases_mm": ["သာကူ"],
        "aliases_en": ["tapioca pearls", "pearl sago"],
        "category": "dry_goods",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0157",
        "name_mm": "ဆွမ်းမွှေးရွက်",
        "name_en": "Pandan leaves",
        "aliases_mm": ["ဆွမ်းမွှေး"],
        "aliases_en": ["screwpine leaves", "pandan"],
        "category": "herb",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0158",
        "name_mm": "ရွှေကြည်",
        "name_en": "Semolina",
        "aliases_mm": ["ရွှေကြည်မှုန့်", "ဆူဂျီ"],
        "aliases_en": ["sooji", "suji"],
        "category": "grain",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0159",
        "name_mm": "အာလူး",
        "name_en": "Potato",
        "aliases_mm": [],
        "aliases_en": ["fresh potato"],
        "category": "produce",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0160",
        "name_mm": "ကွေကာအုပ်",
        "name_en": "Rolled oats",
        "aliases_mm": ["အုတ်ဂျုံ"],
        "aliases_en": ["quaker oats", "oatmeal"],
        "category": "grain",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0161",
        "name_mm": "နို့မှုန့်",
        "name_en": "Milk powder",
        "aliases_mm": [],
        "aliases_en": ["dry milk powder", "powdered milk"],
        "category": "dairy",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0162",
        "name_mm": "ရွှေဖရုံသီး",
        "name_en": "Pumpkin",
        "aliases_mm": ["ရွှေဖရုံ"],
        "aliases_en": ["kabocha squash", "sweet pumpkin"],
        "category": "produce",
        "default_unit": "g"
    }
]

BATCH7_RECIPES_A = [
    {
        "recipe_id": "R0087",
        "name_mm": "သီးစုံကျောက်ကျော",
        "name_en": "Fruits Cocktail Agar",
        "description_mm": "နာနတ်သီး၊ သင်္ဘောသီး၊ ပန်းသီး၊ ငှက်ပျောသီး၊ စတော်ဘယ်ရီ လတ်လတ်ဆတ်ဆတ်များနှင့် သစ်ခွ၊ နာနတ်ဖျော်ရည်တို့ဖြင့် အလွှာနှစ်ထပ် ခမ်းနားစွာ ပြုလုပ်ထားသော သီးစုံကျောက်ကျော။",
        "description_en": "Vibrant two-layered fruit cocktail agar-agar jelly studded with fresh pineapple, papaya, apple, banana, strawberries, and scented fruit syrups.",
        "category": "dessert",
        "meal_types": ["snack", "dessert"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0012",
                "name_mm": "ရေနွေး",
                "name_en": "Hot water",
                "original_name": "ရေနွေး",
                "quantity": 6.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၆ နို့ဆီဘူး",
                "normalized_quantity": 1800.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 25.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၅ ကျပ်သား",
                "normalized_quantity": 408.23,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
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
                "ingredient_id": "I0046",
                "name_mm": "နာနတ်သီး",
                "name_en": "Pineapple",
                "original_name": "နာနတ်သီး (အလုံးသေး)",
                "quantity": 0.5,
                "unit": "ခြမ်း (half)",
                "original_quantity_text": "၁ ခြမ်း",
                "normalized_quantity": 0.5,
                "normalized_unit": "piece",
                "preparation_note_mm": "ပါးပါးလှီးထားသော",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0069",
                "name_mm": "သင်္ဘောသီး",
                "name_en": "Green papaya",
                "original_name": "သင်္ဘောသီး (အလုံးသေး)",
                "quantity": 0.5,
                "unit": "ခြမ်း (half)",
                "original_quantity_text": "၁ ခြမ်း",
                "normalized_quantity": 0.5,
                "normalized_unit": "piece",
                "preparation_note_mm": "အံစာတုံးပုံလှီးထားသော",
                "preparation_note_en": "diced"
            },
            {
                "ingredient_id": "I0148",
                "name_mm": "ပန်းသီး",
                "name_en": "Apple",
                "original_name": "ပန်းသီး",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခြစ်ဖြင့် အမျှင်ပုံခြစ်ထားသော",
                "preparation_note_en": "shredded"
            },
            {
                "ingredient_id": "I0149",
                "name_mm": "ငှက်ပျောသီး",
                "name_en": "Banana",
                "original_name": "သီးမွှေးငှက်ပျောသီး",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အဝိုင်းပုံလှီးထားသော",
                "preparation_note_en": "sliced into rounds"
            },
            {
                "ingredient_id": "I0150",
                "name_mm": "စတော်ဘယ်ရီ",
                "name_en": "Strawberry",
                "original_name": "စတော်ဘယ်ရီခြမ်း",
                "quantity": 5.0,
                "unit": "ခြမ်း (half)",
                "original_quantity_text": "၅ ခြမ်း",
                "normalized_quantity": 2.5,
                "normalized_unit": "piece",
                "preparation_note_mm": "ထက်ခြမ်းခွဲထားသော",
                "preparation_note_en": "halved"
            },
            {
                "ingredient_id": "I0147",
                "name_mm": "ကျောက်ကျောမှုန့်",
                "name_en": "Agar-agar powder",
                "original_name": "ကျောက်ကျောမှုန့် (၂၅) ဂရမ်",
                "quantity": 1.0,
                "unit": "ထုပ် (g)",
                "original_quantity_text": "၁ ထုပ်",
                "normalized_quantity": 25.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ (ကျောက်ကျောဖျော်ရန်)",
                "quantity": 0.5,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၁/၂ နို့ဆီဘူး",
                "normalized_quantity": 150.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ကျောက်ကျောဖျော်ရန်",
                "preparation_note_en": "for dissolving agar powder"
            },
            {
                "ingredient_id": "I0151",
                "name_mm": "သစ်ခွဖျော်ရည်",
                "name_en": "Orchid nectar syrup",
                "original_name": "သစ်ခွဖျော်ရည်",
                "quantity": 0.5,
                "unit": "ခွက် (cup / ml)",
                "original_quantity_text": "၁/၂ ခွက်",
                "normalized_quantity": 120.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0046",
                "name_mm": "နာနတ်သီး",
                "name_en": "Pineapple",
                "original_name": "နာနတ်ဖျော်ရည်",
                "quantity": 0.5,
                "unit": "ခွက် (cup / ml)",
                "original_quantity_text": "၁/၂ ခွက်",
                "normalized_quantity": 120.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ဖျော်ရည်",
                "preparation_note_en": "juice / syrup"
            }
        ],
        "instructions_mm": [
            "ရေနွေး၊ သကြား၊ ဆားတို့ကို ကျိုပြီး အမှိုက်စစ်ထားကာ သစ်သီးများကို လှီးစိတ်ပြင်ဆင်ထားပါ။",
            "ကျောက်ကျောမှုန့်ကို ရေဖြင့်ဖျော်ပြီး ဆူပွက်နေသော သကြားရည်ထဲသို့ ထည့်ကျိုပါ။",
            "ပွက်လျှင် အညီအမျှခွဲကာ သစ်ခွနှင့် နာနတ် တစ်အိုးစီ ရောမွှေပါ။",
            "မှန်ဗန်းထဲသို့ ပထမ သစ်ခွကျောက်ကျောရည်ကို လောင်းပြီး သစ်သီးတစ်ဝက်ကို အနှံ့ဖြန့်ထည့်ပါ။",
            "မျက်နှာပြင် တင်းစပြုလျှင် နာနတ်ကျောက်ကျောရည်ကို ထပ်လောင်းပြီး ကျန်သစ်သီးများ ထည့်ကာ အခန်းအပူချိန်တွင် အအေးခံ၍ တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Boil hot water, sugar, and salt together, strain impurities, and prepare all fresh fruits by chopping into shapes.",
            "Dissolve agar-agar powder in water and pour into the boiling sugar syrup, stirring until thoroughly dissolved.",
            "Divide the boiling agar liquid into two equal portions, stirring orchid syrup into one and pineapple syrup into the other.",
            "Pour the orchid agar mixture into a glass mold and evenly distribute half of the prepared mixed fruits over it.",
            "Once the surface sets slightly, pour over the pineapple agar mixture, add the remaining fruits, let cool at room temperature to set, and slice to serve."
        ],
        "tags": {
            "dietary": ["vegan", "vegetarian", "gluten-free", "dairy-free"],
            "seasonal": ["all-year", "summer"],
            "festival": [],
            "main_ingredients": ["agar-agar", "pineapple", "papaya", "apple", "banana", "strawberry"]
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
            "pdf_pages": [64],
            "printed_page_numbers": [117],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "5:5 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0088",
        "name_mm": "အုန်းနို့ကျောက်ကျော",
        "name_en": "Coconut Milk Agar",
        "description_mm": "အုန်းသီးလတ်လတ်ဆတ်ဆတ်မှ ညှစ်ယူထားသော အုန်းနို့ဦးရည်၊ နှောင်းရည်တို့ဖြင့် အောက်ကြည် အပေါ်နောက် နှစ်လွှာခွဲကာ မွှေးကြိုင်ချိုစိမ့်အောင် ပြုလုပ်ထားသော မြန်မာ့ရိုးရာ အုန်းနို့ကျောက်ကျော။",
        "description_en": "Classic Myanmar two-layer coconut milk agar jelly with a rich creamy coconut top layer and a crisp, clear sweet agar base.",
        "category": "dessert",
        "meal_types": ["snack", "dessert"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီး (ခြစ်ပြီး)",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခြစ်ပြီး ဦးရည်နှင့် နှောင်းရည် ညှစ်ယူထားသော",
                "preparation_note_en": "grated for extracting coconut cream and light milk"
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 30.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၃၀ ကျပ်သား",
                "normalized_quantity": 489.9,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
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
                "ingredient_id": "I0012",
                "name_mm": "ရေနွေး",
                "name_en": "Hot water",
                "original_name": "ရေနွေး",
                "quantity": 6.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၆ နို့ဆီဘူး",
                "normalized_quantity": 1800.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0147",
                "name_mm": "ကျောက်ကျောမှုန့်",
                "name_en": "Agar-agar powder",
                "original_name": "ကျောက်ကျောမှုန့် (၂၅) ဂရမ်",
                "quantity": 1.0,
                "unit": "ထုပ် (g)",
                "original_quantity_text": "၁ ထုပ်",
                "normalized_quantity": 25.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ (ကျောက်ကျောဖျော်ရန်)",
                "quantity": 0.5,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၁/၂ နို့ဆီဘူး",
                "normalized_quantity": 150.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ကျောက်ကျောဖျော်ရန်",
                "preparation_note_en": "for dissolving agar powder"
            }
        ],
        "instructions_mm": [
            "အုန်းသီးမှ ဦးရည်ညှစ်ဖယ်ထားပြီး ရေနွေးဖြင့် နှောင်းရည်ကို သကြား၊ ဆားတို့နှင့် ရောကျိုကာ အမှိုက်စစ်ပါ။",
            "ကျောက်ကျောမှုန့်ကို ရေဖျော်၍ ဦးရည်နှင့်အတူ ပွက်ပွက်ဆူနေသော သကြားရည်အိုးထဲသို့ ထည့်ကျိုပါ။",
            "ပွက်ပွက်ဆူလာလျှင် မှန်ဗန်းထဲသို့ လောင်းထည့်ပါ။",
            "အခန်းအပူချိန်တွင် အအေးခံထားပါက အလိုအလျောက် အုန်းနို့အဆီအလွှာနှင့် အောက်ခံကြည်လွှာ နှစ်ထပ် ကွဲထွက်သွားမည် ဖြစ်ပါသည်။",
            "ခဲသွားလျှင် လိုသလို လှီးစိတ်၍ တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Extract thick coconut cream and set aside, then squeeze thin coconut milk using hot water and simmer with sugar and salt, straining impurities.",
            "Dissolve agar-agar powder in water and add it along with the coconut cream into the briskly boiling syrup pot.",
            "Once boiling vigorously, pour the entire mixture into a glass baking dish.",
            "Allow to cool undisturbed at room temperature; it will naturally separate into a rich creamy coconut top and a translucent jelly base.",
            "Once completely set and firm, slice into diamond shapes and serve."
        ],
        "tags": {
            "dietary": ["vegan", "vegetarian", "gluten-free", "dairy-free"],
            "seasonal": ["all-year"],
            "festival": ["thingyan", "thadingyut"],
            "main_ingredients": ["coconut milk", "agar-agar", "sugar"]
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
            "pdf_pages": [64],
            "printed_page_numbers": [117],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "5:5 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0089",
        "name_mm": "စတော်ဘယ်ရီအုန်းနို့ကျောက်ကျော",
        "name_en": "Strawberry with Coconut Milk Agar",
        "description_mm": "အုန်းနို့မွှေးစိမ့်စိမ့်ကျောက်ကျောရည်ထဲတွင် စတော်ဘယ်ရီသီးအနီရဲရဲလေးများ စီတန်းထည့်သွင်း၍ လှပဆွဲဆောင်မှုရှိစေသော စတော်ဘယ်ရီအုန်းနို့ကျောက်ကျော။",
        "description_en": "Delightful coconut milk agar-agar jelly embedded with sweet whole red strawberries suspended between creamy and translucent layers.",
        "category": "dessert",
        "meal_types": ["snack", "dessert"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီး (ခြစ်ပြီး)",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခြစ်ပြီး",
                "preparation_note_en": "grated"
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 20.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၀ ကျပ်သား",
                "normalized_quantity": 326.6,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0012",
                "name_mm": "ရေနွေး",
                "name_en": "Hot water",
                "original_name": "ရေနွေး",
                "quantity": 6.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၆ နို့ဆီဘူး",
                "normalized_quantity": 1800.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
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
                "ingredient_id": "I0147",
                "name_mm": "ကျောက်ကျောမှုန့်",
                "name_en": "Agar-agar powder",
                "original_name": "ကျောက်ကျောမှုန့် (၂၅) ဂရမ်",
                "quantity": 1.0,
                "unit": "ထုပ် (g)",
                "original_quantity_text": "၁ ထုပ်",
                "normalized_quantity": 25.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ (ကျောက်ကျောဖျော်ရန်)",
                "quantity": 0.5,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၁/၂ နို့ဆီဘူး",
                "normalized_quantity": 150.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ကျောက်ကျောဖျော်ရန်",
                "preparation_note_en": "for dissolving agar powder"
            },
            {
                "ingredient_id": "I0150",
                "name_mm": "စတော်ဘယ်ရီ",
                "name_en": "Strawberry",
                "original_name": "စတော်ဘယ်ရီ (အရွယ်တော်)",
                "quantity": 20.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂၀ လုံး",
                "normalized_quantity": 20.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ထက်ခြမ်းခြမ်းထားသော",
                "preparation_note_en": "halved"
            }
        ],
        "instructions_mm": [
            "အုန်းနို့ရည်မှ ဦးရည်ဖယ်ထားပြီး နှောင်းရည်တွင် သကြား၊ ဆားထည့်၍ ကျိုပြီး အမှိုက်စစ်ထားပါ။",
            "ကျောက်ကျောကို ရေနှင့်ဖျော်ကာ ထည့်မွှေပြီး (၁) နို့ဆီဘူးစာ ခပ်ယူထားပြီးမှ အုန်းနို့ဦးရည်ကို ထည့်ကျိုပါ။",
            "ပွက်လျှင် မှန်ဗန်းထဲသို့ လောင်းထည့်ပါ။",
            "ထက်ခြမ်းခြမ်းထားသော စတော်ဘယ်ရီသီးများကို နေရာအနှံ့ ဖြန့်ထည့်ပါ။",
            "မျက်နှာပြင် တင်းစပြုလျှင် ချန်ထားသော ကျောက်ကျောရည်ကို ဖြန့်ထည့်ကာ အခန်းအပူချိန်တွင် အအေးခံ၍ တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Reserve coconut cream; simmer light coconut milk with sugar and salt, then strain to remove impurities.",
            "Mix agar powder with water, stir into the simmering broth, set aside 1 tin of clear agar liquid, then stir coconut cream into the main pot.",
            "Once boiling, pour the coconut agar into a glass dish.",
            "Evenly distribute the halved strawberries across the jelly surface.",
            "When slightly set, pour over the reserved clear agar liquid, let cool completely at room temperature, and slice to serve."
        ],
        "tags": {
            "dietary": ["vegan", "vegetarian", "gluten-free", "dairy-free"],
            "seasonal": ["winter", "all-year"],
            "festival": [],
            "main_ingredients": ["strawberry", "coconut milk", "agar-agar", "sugar"]
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
            "pdf_pages": [65],
            "printed_page_numbers": [118],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "5:5 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0090",
        "name_mm": "ရနံ့မွှေးကျောက်ကျော",
        "name_en": "Fragrant Agar",
        "description_mm": "လိမ္မော်၊ စတော်ဘယ်ရီ၊ လိုင်ချီး၊ စပျစ်၊ နာနတ်၊ သစ်ခွ ရနံ့ဖျော်ရည် ၆ မျိုးတို့ဖြင့် အရောင်အသွေးစုံလင်စွာ အလွှာလိုက် ကျိုချက်ထားသော ရနံ့မွှေးကျောက်ကျော။",
        "description_en": "Exquisite rainbow multi-layered agar jelly infused with 6 distinct fragrant fruit and floral essences: orange, strawberry, lychee, grape, pineapple, and orchid.",
        "category": "dessert",
        "meal_types": ["snack", "dessert"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ",
                "quantity": 6.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၆ နို့ဆီဘူး",
                "normalized_quantity": 1800.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0147",
                "name_mm": "ကျောက်ကျောမှုန့်",
                "name_en": "Agar-agar powder",
                "original_name": "ကျောက်ကျောမှုန့် (၂၅) ဂရမ်",
                "quantity": 1.0,
                "unit": "ထုပ် (g)",
                "original_quantity_text": "၁ ထုပ်",
                "normalized_quantity": 25.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ (ကျောက်ကျောဖျော်ရန်)",
                "quantity": 0.5,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၁/၂ နို့ဆီဘူး",
                "normalized_quantity": 150.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ကျောက်ကျောဖျော်ရန်",
                "preparation_note_en": "for dissolving agar powder"
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
                "ingredient_id": "I0112",
                "name_mm": "လိမ္မော်သီး",
                "name_en": "Orange",
                "original_name": "လိမ္မော်ရည် (ဖျော်ရည်အပျစ်)",
                "quantity": 6.0,
                "unit": "စားပွဲဇွန်း (tbsp / ml)",
                "original_quantity_text": "၆ စပဇ",
                "normalized_quantity": 90.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ဖျော်ရည်အပျစ်",
                "preparation_note_en": "concentrated syrup"
            },
            {
                "ingredient_id": "I0150",
                "name_mm": "စတော်ဘယ်ရီ",
                "name_en": "Strawberry",
                "original_name": "စတော်ဘယ်ရီ (ဖျော်ရည်အပျစ်)",
                "quantity": 6.0,
                "unit": "စားပွဲဇွန်း (tbsp / ml)",
                "original_quantity_text": "၆ စပဇ",
                "normalized_quantity": 90.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ဖျော်ရည်အပျစ်",
                "preparation_note_en": "concentrated syrup"
            },
            {
                "ingredient_id": "I0152",
                "name_mm": "လိုင်ချီး",
                "name_en": "Lychee syrup",
                "original_name": "လိုင်ချီး (ဖျော်ရည်အပျစ်)",
                "quantity": 6.0,
                "unit": "စားပွဲဇွန်း (tbsp / ml)",
                "original_quantity_text": "၆ စပဇ",
                "normalized_quantity": 90.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ဖျော်ရည်အပျစ်",
                "preparation_note_en": "concentrated syrup"
            },
            {
                "ingredient_id": "I0153",
                "name_mm": "စပျစ်ရည်",
                "name_en": "Grape syrup",
                "original_name": "စပျစ် (ဖျော်ရည်အပျစ်)",
                "quantity": 6.0,
                "unit": "စားပွဲဇွန်း (tbsp / ml)",
                "original_quantity_text": "၆ စပဇ",
                "normalized_quantity": 90.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ဖျော်ရည်အပျစ်",
                "preparation_note_en": "concentrated syrup"
            },
            {
                "ingredient_id": "I0046",
                "name_mm": "နာနတ်သီး",
                "name_en": "Pineapple",
                "original_name": "နာနတ် (ဖျော်ရည်အပျစ်)",
                "quantity": 6.0,
                "unit": "စားပွဲဇွန်း (tbsp / ml)",
                "original_quantity_text": "၆ စပဇ",
                "normalized_quantity": 90.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ဖျော်ရည်အပျစ်",
                "preparation_note_en": "concentrated syrup"
            },
            {
                "ingredient_id": "I0151",
                "name_mm": "သစ်ခွဖျော်ရည်",
                "name_en": "Orchid nectar syrup",
                "original_name": "သစ်ခွ (ဖျော်ရည်အပျစ်)",
                "quantity": 6.0,
                "unit": "စားပွဲဇွန်း (tbsp / ml)",
                "original_quantity_text": "၆ စပဇ",
                "normalized_quantity": 90.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ဖျော်ရည်အပျစ်",
                "preparation_note_en": "concentrated syrup"
            }
        ],
        "instructions_mm": [
            "ရေကို ဆူအောင်တည်ပြီး ရေဖျော်ထားသော ကျောက်ကျောနှင့် ဆားထည့်မွှေပါ။",
            "ကျောက်ကျောရည် (၁) ဘူးစီတွင် ဖျော်ရည်တစ်မျိုးစီကို သီးခြားစီ ရောစပ်ထားပါ။",
            "မှန်ဗန်းထဲသို့ ပထမဆုံး လိမ္မော်ရည်ကျောက်ကျောကို လောင်းထည့်ပါ။",
            "မျက်နှာပြင် တင်းစပြုလာလျှင် ဒုတိယ၊ တတိယနှင့် ကျန်ဖျော်ရည်ကျောက်ကျောများကို တစ်လွှာပြီးတစ်လွှာ ဆက်လက်လောင်းထည့်ပါ။",
            "အခန်းအပူချိန်တွင် (၁၅) မိနစ်ခန့် အအေးခံကာ နှစ်သက်သလို တုံး၍ တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Bring water to a boil, stir in dissolved agar-agar powder and salt, and simmer until clear.",
            "Portion 1 condensed milk tin of hot agar liquid into 6 separate bowls, stirring one concentrated fruit syrup into each.",
            "Pour the first orange-flavored agar layer into a glass dish as the base.",
            "When the surface is just set to the touch, gently pour each subsequent flavored layer in sequence over the back of a spoon.",
            "Let set at room temperature for about 15 minutes, slice into decorative cubes or diamonds, and serve."
        ],
        "tags": {
            "dietary": ["vegan", "vegetarian", "gluten-free", "dairy-free"],
            "seasonal": ["all-year", "summer"],
            "festival": [],
            "main_ingredients": ["agar-agar", "fruit syrups", "orange", "strawberry", "lychee", "grape", "pineapple"]
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
            "pdf_pages": [65],
            "printed_page_numbers": [118],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "5:5 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0091",
        "name_mm": "ကြက်ဥအမြှုပ်ကျောက်ကျော",
        "name_en": "Foamy Eggs Agar",
        "description_mm": "အုန်းနို့ကျောက်ကျောရည်တွင် ကြက်ဥအကာမြှုပ်များ လှပစွာ ပေါလောပေါ်နေစေပြီး အစိမ်းနှင့် အနီရောင်ဆေးစပ် ကျောက်ကျောတုံးလေးများဖြင့် အလှဆင်ထားသော ကြက်ဥအမြှုပ်ကျောက်ကျော။",
        "description_en": "Artistic Burmese agar jelly dessert featuring airy whipped egg foam clouds suspended in rich coconut jelly with colorful ruby and emerald jelly cubes.",
        "category": "dessert",
        "meal_types": ["snack", "dessert"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီး (ခြစ်ပြီး)",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခြစ်ပြီး",
                "preparation_note_en": "grated"
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 25.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၅ ကျပ်သား",
                "normalized_quantity": 408.23,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0012",
                "name_mm": "ရေနွေး",
                "name_en": "Hot water",
                "original_name": "ရေနွေး",
                "quantity": 6.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၆ နို့ဆီဘူး",
                "normalized_quantity": 1800.0,
                "normalized_unit": "ml",
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
                "ingredient_id": "I0147",
                "name_mm": "ကျောက်ကျောမှုန့်",
                "name_en": "Agar-agar powder",
                "original_name": "ကျောက်ကျောမှုန့် (၂၅) ဂရမ်",
                "quantity": 1.0,
                "unit": "ထုပ် (g)",
                "original_quantity_text": "၁ ထုပ်",
                "normalized_quantity": 25.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ (ကျောက်ကျောဖျော်ရန်)",
                "quantity": 0.5,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၁/၂ နို့ဆီဘူး",
                "normalized_quantity": 150.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ကျောက်ကျောဖျော်ရန်",
                "preparation_note_en": "for dissolving agar powder"
            },
            {
                "ingredient_id": "I0154",
                "name_mm": "အစာအရောင်ဆိုးဆေး",
                "name_en": "Food coloring",
                "original_name": "အစိမ်းရောင်ဆေး",
                "quantity": 0.25,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁/၄ လဖဇ",
                "normalized_quantity": 1.25,
                "normalized_unit": "g",
                "preparation_note_mm": "အစိမ်းရောင်",
                "preparation_note_en": "green"
            },
            {
                "ingredient_id": "I0154",
                "name_mm": "အစာအရောင်ဆိုးဆေး",
                "name_en": "Food coloring",
                "original_name": "အနီရောင်ဆေး",
                "quantity": 0.25,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁/၄ လဖဇ",
                "normalized_quantity": 1.25,
                "normalized_unit": "g",
                "preparation_note_mm": "အနီရောင်",
                "preparation_note_en": "red"
            },
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ (အရောင်ဖျော်ရန်)",
                "quantity": 4.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / ml)",
                "original_quantity_text": "၄ လဖဇ",
                "normalized_quantity": 20.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "အရောင်ဖျော်ရန်",
                "preparation_note_en": "for diluting food colors"
            },
            {
                "ingredient_id": "I0026",
                "name_mm": "ကြက်ဥ",
                "name_en": "Chicken egg",
                "original_name": "ကြက်ဥ",
                "quantity": 7.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၇ လုံး",
                "normalized_quantity": 7.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အကာသီးသန့် ခေါက်ထားသော",
                "preparation_note_en": "egg whites whipped until stiff"
            }
        ],
        "instructions_mm": [
            "အုန်းနို့ဦးရည်နှင့် နှောင်းရည်ကို ညှစ်ယူပြီး သကြား၊ ဆား၊ ရေဖျော်ကျောက်ကျောတို့နှင့် ရောကျိုပါ။",
            "ကျောက်ကျောရည် အနည်းငယ်စီကို အစိမ်းနှင့် အနီရောင်ဆိုးဆေး ရောဖျော်၍ သီးခြားစီ အအေးခံကာ အတုံးလေးများ လှီးထားပါ။",
            "ကြက်ဥအကာများကို ထူထဲပွထလာသည်အထိ ခေါက်ပြီး ကျန်ကျောက်ကျောရည်ပူပူထဲသို့ အလျင်အမြန် ထည့်မွှေပါ။",
            "ဗန်းထဲသို့ အမြှုပ်ကျောက်ကျောရည်ကို လောင်းထည့်ပြီး အစိမ်းနှင့် အနီရောင်ကျောက်ကျောတုံးလေးများကို အပေါ်မှ ဖြန့်ထည့်ပါ။",
            "အခန်းအပူချိန်တွင် အအေးခံကာ လှီးစိတ်၍ တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Extract coconut milk, simmer with sugar, salt, and dissolved agar-agar powder until boiling.",
            "Tint two small portions of agar liquid with green and red food colors separately, allow to set firmly, and cut into small jewel cubes.",
            "Whip egg whites into a stiff foam and quickly fold into the remaining warm coconut agar mixture.",
            "Pour the foamy agar mixture into a serving tray and scatter the red and green jewel jelly cubes across the top.",
            "Let set at room temperature, slice into decorative pieces, and serve."
        ],
        "tags": {
            "dietary": ["vegetarian", "gluten-free", "dairy-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["coconut milk", "egg whites", "agar-agar", "sugar"]
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
            "pdf_pages": [65],
            "printed_page_numbers": [119],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "5:5 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0092",
        "name_mm": "ချောကလက်ကျောက်ကျော",
        "name_en": "Chocolate Agar",
        "description_mm": "မွှေးပျံ့ချိုမြိန်သော အုန်းနို့ကျောက်ကျောရည်နှင့် ကိုကိုးချောကလက်ခါးသက်သက် အရသာတို့ ဟာမိုနီဖြစ်အောင် အလွှာနှစ်ထပ် ပေါင်းစပ်ဖန်တီးထားသော ချောကလက်ကျောက်ကျော။",
        "description_en": "Decadent two-toned dessert combining a creamy sweet coconut agar layer with a rich cocoa chocolate agar jelly.",
        "category": "dessert",
        "meal_types": ["snack", "dessert"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီး (ခြစ်ပြီး)",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခြစ်ပြီး",
                "preparation_note_en": "grated"
            },
            {
                "ingredient_id": "I0012",
                "name_mm": "ရေနွေး",
                "name_en": "Hot water",
                "original_name": "ရေနွေး",
                "quantity": 6.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၆ နို့ဆီဘူး",
                "normalized_quantity": 1800.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 30.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၃၀ ကျပ်သား",
                "normalized_quantity": 489.9,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
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
                "ingredient_id": "I0147",
                "name_mm": "ကျောက်ကျောမှုန့်",
                "name_en": "Agar-agar powder",
                "original_name": "ကျောက်ကျောမှုန့် (၂၅) ဂရမ်",
                "quantity": 1.0,
                "unit": "ထုပ် (g)",
                "original_quantity_text": "၁ ထုပ်",
                "normalized_quantity": 25.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ (ကျောက်ကျောဖျော်ရန်)",
                "quantity": 0.5,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၁/၂ နို့ဆီဘူး",
                "normalized_quantity": 150.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ကျောက်ကျောဖျော်ရန်",
                "preparation_note_en": "for dissolving agar powder"
            },
            {
                "ingredient_id": "I0155",
                "name_mm": "ချောကလက်မှုန့်",
                "name_en": "Cocoa powder",
                "original_name": "ချောကလက်မှုန့်",
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
            "အုန်းသီးမှ ဦးရည်ညှစ်ဖယ်ထားပြီး နှောင်းရည်ကို သကြား၊ ဆား၊ ရေဖျော်ကျောက်ကျောမှုန့်နှင့် ဦးရည်တို့ထည့်ကာ ပွက်ပွက်ဆူအောင် ကျိုပါ။",
            "ကျိုပြီးလျှင် အညီအမျှ နှစ်ခွက်ခွဲပါ။",
            "တစ်ဝက်ကို မှန်ဗန်းထဲသို့ လောင်းထည့်ထားပါ။",
            "ကျန်တစ်ဝက်ကို ချောကလက်မှုန့် ထည့်ဖျော်ပြီး အောက်လွှာမျက်နှာပြင် တင်းစပြုချိန်တွင် အပေါ်မှ ဖြန့်လောင်းထည့်ပါ။",
            "အခန်းအပူချိန်တွင် အအေးခံကာ လိုသလို လှီးစိတ်၍ တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Extract coconut milk, simmer with sugar, salt, dissolved agar-agar powder, and coconut cream until boiling.",
            "Remove from heat and divide the hot agar mixture into two equal halves.",
            "Pour the plain white coconut agar half into a glass dish as the first layer.",
            "Whisk cocoa powder thoroughly into the remaining warm agar half, and gently pour over the set coconut base.",
            "Allow to cool completely at room temperature, slice into squares, and serve."
        ],
        "tags": {
            "dietary": ["vegan", "vegetarian", "gluten-free", "dairy-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["coconut milk", "cocoa powder", "agar-agar", "sugar"]
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
            "pdf_pages": [65],
            "printed_page_numbers": [119],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "5:5 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0093",
        "name_mm": "နှစ်ထပ်သာကူကျောက်ကျော",
        "name_en": "Two Layers Sago Agar",
        "description_mm": "သာကူစေ့စိမ်းစိမ်းလေးများ ပြည့်နှက်နေသော အောက်ခံကျောက်ကျောလွှာနှင့် အပေါ်မှ အုန်းနို့ဦးရည်ဆိမ့်ဆိမ့်လွှာတို့ဖြင့် စီမံထားသော နှစ်ထပ်သာကူကျောက်ကျော။",
        "description_en": "Dual-layered Burmese agar jelly featuring emerald green chewy sago pearls set in sweet jelly below a rich creamy coconut topping.",
        "category": "dessert",
        "meal_types": ["snack", "dessert"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီး (ခြစ်ပြီး)",
                "quantity": 4.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၄ လုံး",
                "normalized_quantity": 4.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခြစ်ပြီး",
                "preparation_note_en": "grated"
            },
            {
                "ingredient_id": "I0012",
                "name_mm": "ရေနွေး",
                "name_en": "Hot water",
                "original_name": "ရေနွေး",
                "quantity": 6.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၆ နို့ဆီဘူး",
                "normalized_quantity": 1800.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 50.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅၀ ကျပ်သား",
                "normalized_quantity": 816.45,
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
                "ingredient_id": "I0147",
                "name_mm": "ကျောက်ကျောမှုန့်",
                "name_en": "Agar-agar powder",
                "original_name": "ကျောက်ကျော (မြန်မာ)",
                "quantity": 2.0,
                "unit": "ထုပ် (g)",
                "original_quantity_text": "၂ ထုပ်",
                "normalized_quantity": 50.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0156",
                "name_mm": "သာကူစေ့",
                "name_en": "Sago pearls",
                "original_name": "သာကူစေ့",
                "quantity": 10.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၀ ကျပ်သား",
                "normalized_quantity": 163.3,
                "normalized_unit": "g",
                "preparation_note_mm": "(၂) နာရီ စိမ်ပြီး ရေစစ်ထားသော",
                "preparation_note_en": "soaked for 2 hours and drained"
            },
            {
                "ingredient_id": "I0154",
                "name_mm": "အစာအရောင်ဆိုးဆေး",
                "name_en": "Food coloring",
                "original_name": "အစိမ်းရောင်ဆေး",
                "quantity": 0.25,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁/၄ လဖဇ",
                "normalized_quantity": 1.25,
                "normalized_unit": "g",
                "preparation_note_mm": "အစိမ်းရောင်",
                "preparation_note_en": "green"
            },
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ (အရောင်ဖျော်ရန်)",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / ml)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "အရောင်ဖျော်ရန်",
                "preparation_note_en": "for diluting color"
            }
        ],
        "instructions_mm": [
            "အုန်းနို့ဦးရည် ညှစ်ယူဖယ်ထားပြီး နှောင်းရည် (၄) နို့ဆီဘူးစာကို သကြား၊ ဆား၊ ကျောက်ကျောမှုန့်တို့နှင့် ရောကျိုကာ မီးအေးအေးဖြင့် ပျစ်လာသည်အထိ ကျိုပါ။",
            "ရေစိမ်ရေစစ်ထားသော သာကူစေ့များကို ပွက်ပွက်ဆူနေသော ကျောက်ကျောအိုးထဲ ထည့်မွှေပါ။",
            "သာကူစေ့များ မျက်စိပျောက်လျှင် တစ်ဝက်ကို မှန်ဗန်းထဲသို့ ဖြန့်လောင်းထည့်ပါ။",
            "ကျန်တစ်ဝက်တွင် အစိမ်းရောင်ဆေးဖျော်ထည့်မွှေပြီး မျက်နှာပြင်ပေါ်သို့ ထပ်၍ ဖြန့်လောင်းကာ အုန်းနို့ဦးရည်ကို အပေါ်မှ ဖြန့်ထည့်ပါ။",
            "အခန်းအပူချိန်တွင် အအေးခံကာ လှီးစိတ်၍ တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Extract coconut cream and set aside; simmer thin coconut milk with sugar, salt, and agar powder over low heat until slightly thickened.",
            "Add pre-soaked, drained sago pearls into the boiling agar liquid, stirring gently.",
            "Once sago pearls turn translucent, pour half into a glass dish as the first layer.",
            "Tint the remaining half with green coloring, pour over the base, and top with the rich coconut cream.",
            "Let set at room temperature, slice into diamond shapes, and serve."
        ],
        "tags": {
            "dietary": ["vegan", "vegetarian", "gluten-free", "dairy-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["sago pearls", "coconut milk", "agar-agar", "sugar"]
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
            "pdf_pages": [66],
            "printed_page_numbers": [120],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "5:5 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0094",
        "name_mm": "ကျောက်စိမ်းမုန့်",
        "name_en": "Jade Agar Cake",
        "description_mm": "ဆွမ်းမွှေးရွက်ရနံ့မွှေးမွှေး အစိမ်းရောင်အချိုလွှာနှင့် အုန်းနို့ဦးရည်ဆိမ့်ဆိမ့် အဖြူရောင်အဆိမ့်လွှာတို့ဖြင့် ကျောက်စိမ်းရောင်သမ်းကာ စီမံထားသော ကျောက်စိမ်းကျောက်ကျောမုန့်။",
        "description_en": "Aromatic Jade agar-agar cake combining fragrant emerald green pandan sweet jelly and creamy white coconut agar in harmonious contrast.",
        "category": "dessert",
        "meal_types": ["snack", "dessert"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီး (ခြစ်ပြီး)",
                "quantity": 6.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၆ လုံး",
                "normalized_quantity": 6.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခြစ်ပြီး",
                "preparation_note_en": "grated"
            },
            {
                "ingredient_id": "I0012",
                "name_mm": "ရေနွေး",
                "name_en": "Hot water",
                "original_name": "ရေနွေး",
                "quantity": 6.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၆ နို့ဆီဘူး",
                "normalized_quantity": 1800.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 50.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅၀ ကျပ်သား",
                "normalized_quantity": 816.45,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 1.5,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ ၁/၂ လဖဇ",
                "normalized_quantity": 7.5,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0157",
                "name_mm": "ဆွမ်းမွှေးရွက်",
                "name_en": "Pandan leaves",
                "original_name": "ဆွမ်းမွှေးရွက် (ထောင်းပြီး)",
                "quantity": 10.0,
                "unit": "ရွက် (leaf)",
                "original_quantity_text": "၁၀ ရွက်",
                "normalized_quantity": 10.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ထောင်းပြီး အရည်ညှစ်ထားသော",
                "preparation_note_en": "pounded to extract juice"
            },
            {
                "ingredient_id": "I0154",
                "name_mm": "အစာအရောင်ဆိုးဆေး",
                "name_en": "Food coloring",
                "original_name": "အစိမ်းရောင်ဆေး",
                "quantity": 0.5,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁/၂ လဖဇ",
                "normalized_quantity": 2.5,
                "normalized_unit": "g",
                "preparation_note_mm": "အစိမ်းရောင်",
                "preparation_note_en": "green"
            },
            {
                "ingredient_id": "I0147",
                "name_mm": "ကျောက်ကျောမှုန့်",
                "name_en": "Agar-agar powder",
                "original_name": "ကျောက်ကျောမှုန့် (မြန်မာ)",
                "quantity": 2.0,
                "unit": "ထုပ် (g)",
                "original_quantity_text": "၂ ထုပ်",
                "normalized_quantity": 50.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "အုန်းနို့ဦးရည်နှင့် နှောင်းရည်တို့ကို ညှစ်ယူထားပါ။",
            "အဖြူလွှာအတွက် နှောင်းရည် (၃) ဘူး၊ သကြား (၂၀) ကျပ်သား၊ ဆား (၁) လဖဇ၊ ကျောက်ကျောမှုန့် (၁) ထုပ်ကို အိုးတစ်လုံးတွင် ရောပါ။",
            "အစိမ်းလွှာအတွက် နှောင်းရည် (၃) ဘူး၊ သကြား (၃၀) ကျပ်သား၊ ဆား (၁/၂) လဖဇ၊ ဆွမ်းမွှေးရွက်ရည်၊ အစိမ်းရောင်ဆေးနှင့် ကျောက်ကျောမှုန့် (၁) ထုပ်တို့ကို အခြားအိုးတစ်လုံးတွင် ရောစပ်ကျိုပါ။",
            "မှန်ဗန်းထဲသို့ အဖြူရောင်ကျောက်ကျောရည်ကို အလျင်လောင်းထည့်ပြီး မျက်နှာပြင် ညီအောင်ညှိကာ အစိမ်းရောင်ကျောက်ကျောရည်ကို ဆက်တိုက်လောင်းထည့်ပါ။",
            "အခန်းအပူချိန်တွင် အအေးခံကာ လှီးစိတ်၍ တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Extract thick coconut cream and light coconut milk from the grated coconuts.",
            "In one pot, mix thin coconut milk, sugar, salt, and 1 packet of agar powder for the white layer.",
            "In a second pot, mix thin coconut milk, sugar, salt, extracted pandan leaf juice, green color, and 1 packet of agar powder for the green jade layer.",
            "Pour the white agar mixture into a glass mold, smooth the surface, then gently pour the green pandan agar layer directly over it.",
            "Allow to cool and set completely at room temperature, then slice and serve."
        ],
        "tags": {
            "dietary": ["vegan", "vegetarian", "gluten-free", "dairy-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["pandan leaves", "coconut milk", "agar-agar", "sugar"]
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
            "pdf_pages": [66],
            "printed_page_numbers": [120],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "5:5 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0095",
        "name_mm": "ငှက်ပျောသီးဆနွင်းမကင်း",
        "name_en": "Banana Cake",
        "description_mm": "ရခိုင်ငှက်ပျောသီးမှည့်မှည့်၊ အုန်းသီး၊ ဂျုံမှုန့်နှင့် ထောပတ်မွှေးမွှေးတို့ဖြင့် ဖုတ်ထားသော မြန်မာ့ရိုးရာ ငှက်ပျောသီးဆနွင်းမကင်း။",
        "description_en": "Traditional Myanmar baked banana semolina cake made with fragrant mashed ripe Rakhine bananas, coconut milk, wheat flour, and butter.",
        "category": "dessert",
        "meal_types": ["snack", "dessert"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0149",
                "name_mm": "ငှက်ပျောသီး",
                "name_en": "Banana",
                "original_name": "ရခိုင်ငှက်ပျော (မှည့်မှည့်ဝင်း)",
                "quantity": 60.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၆၀ လုံး",
                "normalized_quantity": 60.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ကြေညက်အောင် ခြေထားသော",
                "preparation_note_en": "mashed smoothly"
            },
            {
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီးအလုံးသေး (ခြစ်ပြီး)",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခြစ်ပြီး",
                "preparation_note_en": "grated"
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 25.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၅ ကျပ်သား",
                "normalized_quantity": 408.23,
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
                "ingredient_id": "I0002",
                "name_mm": "ထောပတ်",
                "name_en": "Butter",
                "original_name": "ထောပတ်",
                "quantity": 10.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၀ ကျပ်သား",
                "normalized_quantity": 163.3,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0043",
                "name_mm": "ဂျုံမှုန့်",
                "name_en": "Wheat flour",
                "original_name": "ဂျုံမှုန့် (ဆန်ကာချပြီး)",
                "quantity": 20.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၀ ကျပ်သား",
                "normalized_quantity": 326.6,
                "normalized_unit": "g",
                "preparation_note_mm": "ဆန်ကာချပြီး",
                "preparation_note_en": "sifted"
            },
            {
                "ingredient_id": "I0154",
                "name_mm": "အစာအရောင်ဆိုးဆေး",
                "name_en": "Food coloring",
                "original_name": "အနီရောင်ဆေး",
                "quantity": 0.75,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၃/၄ လဖဇ",
                "normalized_quantity": 3.75,
                "normalized_unit": "g",
                "preparation_note_mm": "အနီရောင်",
                "preparation_note_en": "red"
            },
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ (အရောင်ဖျော်ရန်)",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / ml)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "အရောင်ဖျော်ရန်",
                "preparation_note_en": "for diluting food color"
            }
        ],
        "instructions_mm": [
            "ငှက်ပျောသီးကို ကြေညက်အောင် ခြေပြီး အုန်းသီးမှ ဦးရည်တစ်ကြိမ် ညှစ်ယူကာ ကျန်အုန်းဖတ်များကို ငှက်ပျောသီးနှင့် ရောပါ။",
            "ဂျုံ၊ သကြား၊ ဆား၊ ထောပတ်တို့ကို ထည့်ပြီး နှံ့အောင် နယ်ပါ။",
            "အနီရောင်ဆေးကို ရေနှင့်ဖျော်၍ ထည့်ကာ နှံ့စပ်အောင် ထပ်နယ်ပါ။",
            "မုန့်ဖုတ်ဗန်းထဲသို့ မုန့်ဖတ်များကို ဖြန့်ထည့်ပြီး မျက်နှာပြင်ညှိကာ ချန်ထားသော ဦးရည်ကို ဖြန့်လောင်းပါ။",
            "အပေါ်မီးများများ၊ အောက်မီးနည်းနည်းဖြင့် ဖုတ်ပြီး မျက်နှာပြင် နီရောင်သမ်းလာပါက အအေးခံကာ လှီးစိတ်၍ တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Mash ripe bananas thoroughly; squeeze rich coconut cream from grated coconut and set aside, mixing the coconut pulp with the mashed bananas.",
            "Add flour, sugar, salt, and butter, kneading well into a smooth batter.",
            "Dissolve red food coloring in water and mix into the batter thoroughly.",
            "Spread the batter evenly in a greased baking pan, smooth the surface, and pour the reserved coconut cream over top.",
            "Bake with high top heat and low bottom heat until golden-red on top, allow to cool completely, and slice to serve."
        ],
        "tags": {
            "dietary": ["vegetarian"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["banana", "coconut", "wheat flour", "butter", "sugar"]
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
            "pdf_pages": [66],
            "printed_page_numbers": [121],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "5:5 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0096",
        "name_mm": "ရွှေကြည်ဆနွင်းမကင်း",
        "name_en": "Semolina Cake",
        "description_mm": "ရွှေကြည်မှုန့်၊ အုန်းနို့၊ ထောပတ်၊ ကြက်ဥတို့ဖြင့် ဆီပြန်အောင် မွှေကြော်ဖုတ်ပြီး ဘိန်းစေ့လေးများ ဖြူးထားသော အလွန်လူကြိုက်များသည့် ရွှေကြည်ဆနွင်းမကင်း။",
        "description_en": "The definitive traditional Burmese semolina cake, cooked with coconut milk, butter, beaten eggs, and sugar, baked until rich and topped with toasted poppy seeds.",
        "category": "dessert",
        "meal_types": ["snack", "dessert"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီး (ခြစ်ပြီး)",
                "quantity": 5.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၅ လုံး",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခြစ်ပြီး",
                "preparation_note_en": "grated"
            },
            {
                "ingredient_id": "I0012",
                "name_mm": "ရေနွေး",
                "name_en": "Hot water",
                "original_name": "ရေနွေး",
                "quantity": 10.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၁၀ နို့ဆီဘူး",
                "normalized_quantity": 3000.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0158",
                "name_mm": "ရွှေကြည်",
                "name_en": "Semolina",
                "original_name": "ရွှေကြည်",
                "quantity": 50.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅၀ ကျပ်သား",
                "normalized_quantity": 816.45,
                "normalized_unit": "g",
                "preparation_note_mm": "နီရောင်သန်းသည်အထိ လှော်ထားသော",
                "preparation_note_en": "dry-toasted until golden"
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 60.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၆၀ ကျပ်သား",
                "normalized_quantity": 979.74,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0026",
                "name_mm": "ကြက်ဥ",
                "name_en": "Chicken egg",
                "original_name": "ကြက်ဥ (ခေါက်ထား)",
                "quantity": 5.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၅ လုံး",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခေါက်ထားသော",
                "preparation_note_en": "beaten"
            },
            {
                "ingredient_id": "I0002",
                "name_mm": "ထောပတ်",
                "name_en": "Butter",
                "original_name": "ထောပတ်",
                "quantity": 20.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၀ ကျပ်သား",
                "normalized_quantity": 326.6,
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
                "normalized_quantity": 81.65,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0107",
                "name_mm": "ဘိန်းစေ့",
                "name_en": "Poppy seeds",
                "original_name": "ဘိန်းစေ့ (သန့်စင်ပြီး)",
                "quantity": 2.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
                "normalized_quantity": 40.82,
                "normalized_unit": "g",
                "preparation_note_mm": "သန့်စင်ပြီး",
                "preparation_note_en": "cleaned"
            }
        ],
        "instructions_mm": [
            "အုန်းနို့ဦးရည် ညှစ်ယူဖယ်ထားပြီး နှောင်းရည် (၁၀) ဘူးစာ ရအောင်လုပ်ကာ ရွှေကြည်ကို နီရောင်သန်းသည်အထိ လှော်ထားပါ။",
            "မုန့်အိုးတွင် ထောပတ်နှင့် ဆီထည့်၍ ပူလာလျှင် ရွှေကြည်နှင့် သကြားထည့်မွှေကာ နှောင်းရည်ထည့်၍ မပြတ်မွှေပါ။",
            "ကြက်ဥခေါက်ထားသည်များ ထည့်၍ ခပ်သွက်သွက်မွှေပြီး မုန့်သားများ အိုးတွင် ကပ်မနေဘဲ လုံးလာလျှင် ဆီပြန်ပြီ ဖြစ်ပါသည်။",
            "မုန့်ဗန်းထဲသို့ မုန့်သားများထည့်ကာ မျက်နှာပြင်ညှိပြီး ချန်ထားသော ဦးရည်ကို လောင်းကာ ဘိန်းစေ့များကို အပေါ်မှ ဖြန့်ဖြူးပါ။",
            "အပေါ်မီးများများ၊ အောက်မီးမရှိသလောက်ဖြင့် ဖုတ်ပြီး မျက်နှာပြင် နီရောင်သန်းလာပါက မီးဖယ်၍ အအေးခံကာ လှီးစိတ်တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Reserve thick coconut cream and extract 10 tins of thin coconut milk; dry-toast semolina until fragrant and golden.",
            "Heat butter and oil in a large wok, add toasted semolina, sugar, and thin coconut milk, stirring constantly over medium heat.",
            "Add beaten eggs and whisk briskly until the mixture thickens into a glossy paste that pulls away from the wok sides.",
            "Transfer into a baking tray, smooth surface, pour reserved coconut cream on top, and scatter poppy seeds evenly.",
            "Bake with strong overhead heat until the top is browned and fragrant; cool completely and cut into diamonds to serve."
        ],
        "tags": {
            "dietary": ["vegetarian"],
            "seasonal": ["all-year"],
            "festival": ["thadingyut", "tazaungdaing"],
            "main_ingredients": ["semolina", "coconut milk", "butter", "egg", "poppy seeds"]
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
            "pdf_pages": [66],
            "printed_page_numbers": [121],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "5:5 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0097",
        "name_mm": "အာလူးဆနွင်းမကင်း",
        "name_en": "Potato Cake",
        "description_mm": "အာလူးပြုတ်နူးနူး၊ အုန်းသီး၊ ဂျုံမှုန့်နှင့် ထောပတ်တို့ဖြင့် အချိုးညီဖုတ်ထားသော မွှေးပျံ့ဆိမ့်အိသည့် အာလူးဆနွင်းမကင်း။",
        "description_en": "Rich and tender Myanmar potato cake baked with boiled mashed potatoes, fresh coconut cream, wheat flour, and fragrant butter.",
        "category": "dessert",
        "meal_types": ["snack", "dessert"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0159",
                "name_mm": "အာလူး",
                "name_en": "Potato",
                "original_name": "အာလူး",
                "quantity": 1.0,
                "unit": "ပိဿာ (kg)",
                "original_quantity_text": "၁ ပိဿာ",
                "normalized_quantity": 1632.93,
                "normalized_unit": "g",
                "preparation_note_mm": "နူးအောင် ပြုတ်ပြီး အခွံခွာ၍ ကြေညက်အောင် ခြေထားသော",
                "preparation_note_en": "boiled until tender, peeled, and mashed"
            },
            {
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီးအလုံးသေး (ခြစ်ပြီး)",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခြစ်ပြီး ဦးရည်ဖယ်ထားသော",
                "preparation_note_en": "grated, with cream reserved"
            },
            {
                "ingredient_id": "I0043",
                "name_mm": "ဂျုံမှုန့်",
                "name_en": "Wheat flour",
                "original_name": "ဂျုံ (ဆန်ကာချပြီး)",
                "quantity": 20.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၀ ကျပ်သား",
                "normalized_quantity": 326.6,
                "normalized_unit": "g",
                "preparation_note_mm": "ဆန်ကာချပြီး",
                "preparation_note_en": "sifted"
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
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 40.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၄၀ ကျပ်သား",
                "normalized_quantity": 653.17,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
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
                "ingredient_id": "I0002",
                "name_mm": "ထောပတ်",
                "name_en": "Butter",
                "original_name": "ထောပတ်",
                "quantity": 15.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၅ ကျပ်သား",
                "normalized_quantity": 244.95,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "အာလူးကို နူးအောင်ပြုတ်ပြီး အေးလျှင် အခွံခွာ၍ ကြေညက်နေအောင် ခြေထားပါ။",
            "အုန်းဖတ်ကို ရေနွေးအနည်းငယ်ဖြန်းပြီး ညှစ်ကာ ဦးရည်ဖယ်ထားပါ။",
            "ဇလုံတစ်ခုထဲသို့ အာလူး၊ အုန်းဖတ်၊ ဂျုံ၊ ဆား၊ သကြား၊ ဆီ၊ ထောပတ် အားလုံးထည့်၍ သမအောင် နယ်ပါ။",
            "မုန့်ဖုတ်ဗန်းထဲသို့ ဖြန့်ထည့်ကာ မျက်နှာပြင်ညှိပြီး ချန်ထားသော ဦးရည်ကို ဖြန့်လောင်းပါ။",
            "မုန့်ဖုတ်ဖိုတွင် တစ်နာရီခန့် အချိန်ယူဖုတ်ပြီး မျက်နှာပြင် နီရောင်သမ်းလာလျှင် အအေးခံကာ အတုံး ၆၀ အရွယ်ညီ လှီး၍ တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Boil potatoes until fork-tender, let cool, peel, and mash until completely smooth.",
            "Moisten grated coconut with a little hot water, squeeze to extract thick cream, and reserve cream.",
            "In a large bowl, combine mashed potatoes, coconut pulp, sifted flour, salt, sugar, oil, and butter, kneading until uniform.",
            "Spread batter into a greased baking dish, smooth the top, and drizzle the reserved coconut cream over the surface.",
            "Bake for about 1 hour until the top crust turns golden-red; let cool and slice into 60 uniform bite-sized squares to serve."
        ],
        "tags": {
            "dietary": ["vegetarian"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["potato", "coconut", "butter", "wheat flour", "sugar"]
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
            "pdf_pages": [68],
            "printed_page_numbers": [122],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "5:5 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0098",
        "name_mm": "မုန်လာဥဝါဆနွင်းမကင်း",
        "name_en": "Carrot Cake",
        "description_mm": "မုန်လာဥဝါ (ကာရိုတ်) ခြစ်၊ အုန်းနို့၊ ဂျုံမှုန့်နှင့် ထောပတ်တို့ဖြင့် အချိုအရသာလေး ပြေပြစ်စေရန် ဖုတ်ထားသော မုန်လာဥဝါဆနွင်းမကင်း။",
        "description_en": "Traditional Myanmar carrot cake (sanwin makin) prepared with grated sweet carrots, fresh coconut milk, flour, butter, and sugar.",
        "category": "dessert",
        "meal_types": ["snack", "dessert"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0014",
                "name_mm": "မုန်လာဥနီ",
                "name_en": "Carrot",
                "original_name": "မုန်လာဥဝါ (အခွံသင်ပြီး)",
                "quantity": 1.0,
                "unit": "ပိဿာ (kg)",
                "original_quantity_text": "၁ ပိဿာ",
                "normalized_quantity": 1632.93,
                "normalized_unit": "g",
                "preparation_note_mm": "အခွံသင် ခြစ်ထားသော",
                "preparation_note_en": "peeled and finely grated"
            },
            {
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီးအလုံးသေး (ခြစ်ပြီး)",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခြစ်ပြီး",
                "preparation_note_en": "grated"
            },
            {
                "ingredient_id": "I0043",
                "name_mm": "ဂျုံမှုန့်",
                "name_en": "Wheat flour",
                "original_name": "ဂျုံ (ဆန်ကာချပြီး)",
                "quantity": 20.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၀ ကျပ်သား",
                "normalized_quantity": 326.6,
                "normalized_unit": "g",
                "preparation_note_mm": "ဆန်ကာချပြီး",
                "preparation_note_en": "sifted"
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 40.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၄၀ ကျပ်သား",
                "normalized_quantity": 653.17,
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
                "ingredient_id": "I0002",
                "name_mm": "ထောပတ်",
                "name_en": "Butter",
                "original_name": "ထောပတ်",
                "quantity": 15.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၅ ကျပ်သား",
                "normalized_quantity": 244.95,
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
                "normalized_quantity": 81.65,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "မုန်လာဥဝါကို ခြစ်ထားပြီး အုန်းသီးမှ ဦးရည်ညှစ်ဖယ်ကာ အုန်းဖတ်များကို ဇလုံတစ်ခုတွင် ထည့်ပါ။",
            "ဂျုံ၊ သကြား၊ ဆားတို့ကို အုန်းဖတ်နှင့် ရောစပ်ပြီး ခြစ်ထားသော မုန်လာဥဝါ၊ ဆီ၊ ထောပတ် ထပ်ထည့်၍ သမအောင် နယ်ပါ။",
            "ဆီသုတ်ထားသော မုန့်ဖုတ်ဗန်းထဲသို့ ဖြန့်ထည့်ကာ လက်ဖြင့် အသာဖိပြီး မျက်နှာပြင်ညှိပါ။",
            "ချန်ထားသော အုန်းနို့ဦးရည်ကို ဖြန့်လောင်းပြီး မုန့်ဖုတ်ဖိုတွင် တစ်နာရီခန့် အချိန်ယူဖုတ်ပါ။",
            "မျက်နှာပြင် နီရောင်သမ်းလာပြီး ကျက်နပ်ပါက အအေးခံပြီး လှီးစိတ်၍ တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Grate peeled carrots; extract coconut cream and set aside, placing grated coconut pulp into a mixing bowl.",
            "Combine flour, sugar, and salt with the coconut pulp, then incorporate grated carrots, oil, and butter into a well-blended mixture.",
            "Press the mixture evenly into an oiled baking pan, flattening and smoothing the top.",
            "Drizzle the reserved coconut cream over the surface and bake for about 1 hour until the top crust is richly browned.",
            "Remove from heat, let cool to room temperature, slice into uniform squares, and serve."
        ],
        "tags": {
            "dietary": ["vegetarian"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["carrot", "coconut", "wheat flour", "butter", "sugar"]
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
            "pdf_pages": [68],
            "printed_page_numbers": [122],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "5:5 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0099",
        "name_mm": "ကွေကာအုပ်ဆနွင်းမကင်း",
        "name_en": "Quaker Oats Pudding",
        "description_mm": "အာဟာရပြည့် ကွေကာအုပ်ဂျုံ၊ ကြက်ဥ၊ အုန်းနို့၊ နို့မှုန့်၊ သကြားနှင့် ထောပတ်မွှေးမွှေးတို့ဖြင့် ဖုတ်ထားသော အာဟာရပြည့် ကွေကာအုပ်ဆနွင်းမကင်း။",
        "description_en": "Nutritious and comforting baked oat pudding (sanwin makin) made with toasted Quaker oats, fresh coconut milk, beaten eggs, milk powder, and butter.",
        "category": "dessert",
        "meal_types": ["breakfast", "snack", "dessert"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0160",
                "name_mm": "ကွေကာအုပ်",
                "name_en": "Rolled oats",
                "original_name": "ကွေကာအုပ် (အထုပ်ကြီး)",
                "quantity": 1.5,
                "unit": "ထုပ် (g)",
                "original_quantity_text": "၁ ၁/၂ ထုပ်",
                "normalized_quantity": 600.0,
                "normalized_unit": "g",
                "preparation_note_mm": "လှော်ထားသော",
                "preparation_note_en": "toasted"
            },
            {
                "ingredient_id": "I0043",
                "name_mm": "ဂျုံမှုန့်",
                "name_en": "Wheat flour",
                "original_name": "ဂျုံ (ဆန်ကာစစ်ပြီး)",
                "quantity": 10.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၀ ကျပ်သား",
                "normalized_quantity": 163.3,
                "normalized_unit": "g",
                "preparation_note_mm": "ဆန်ကာစစ်ပြီး",
                "preparation_note_en": "sifted"
            },
            {
                "ingredient_id": "I0026",
                "name_mm": "ကြက်ဥ",
                "name_en": "Chicken egg",
                "original_name": "ကြက်ဥ",
                "quantity": 5.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၅ လုံး",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခေါက်ထားသော",
                "preparation_note_en": "beaten"
            },
            {
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီးကြီးကြီး (ခြစ်ပြီး)",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခြစ်ပြီး",
                "preparation_note_en": "grated"
            },
            {
                "ingredient_id": "I0012",
                "name_mm": "ရေနွေး",
                "name_en": "Hot water",
                "original_name": "ရေနွေး",
                "quantity": 7.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၇ နို့ဆီဘူး",
                "normalized_quantity": 2100.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 25.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၅ ကျပ်သား",
                "normalized_quantity": 408.23,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0161",
                "name_mm": "နို့မှုန့်",
                "name_en": "Milk powder",
                "original_name": "နို့မှုန့်",
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
                "quantity": 0.5,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁/၂ စပဇ",
                "normalized_quantity": 7.5,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0002",
                "name_mm": "ထောပတ်",
                "name_en": "Butter",
                "original_name": "ထောပတ်",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.65,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "ကွေကာအုပ်ကို လှော်ထားပြီး အုန်းနို့ဦးရည် (၁) ဘူးနှင့် နှောင်းရည် (၆) ဘူး ညှစ်ယူထားပါ။",
            "ဇလုံထဲတွင် နှောင်းရည်၊ ဂျုံ၊ သကြား၊ နို့မှုန့်၊ ဆားတို့ကို ရောစပ်မွှေပြီး အမှိုက်စစ်ကာ ဦးရည်နှင့် ကြက်ဥခေါက်ထားသည်များ ထည့်မွှေပါ။",
            "မုန့်ဖုတ်ဗန်းတွင် ထောပတ်သုတ်ပြီး အပူပေးကာ ဖျော်စပ်ထားသော မုန့်ရည်ထည့်ပြီး လှော်ထားသော ကွေကာအုပ်များကို မျက်နှာပြင်အနှံ့ ဖြူးပါ။",
            "အပေါ်မီးများများ၊ အောက်မီးနည်းနည်းဖြင့် ဖုတ်ပါ။",
            "မျက်နှာပြင်ရှိ ကွေကာအုပ်အဖတ်လေးများ နီရောင်သမ်းလာလျှင် ဖိုမှချပြီး အခန်းအပူချိန်တွင် အအေးခံကာ လှီးစိတ်တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Toast rolled oats until fragrant; extract 1 tin of rich coconut cream and 6 tins of light coconut milk.",
            "In a bowl, mix thin coconut milk, flour, sugar, milk powder, and salt, strain impurities, then whisk in the coconut cream and beaten eggs.",
            "Grease a preheated baking dish with butter, pour in the custard batter, and scatter the toasted oats evenly across the entire surface.",
            "Bake using high overhead heat and low bottom heat.",
            "When the oat flakes on the crust turn toasted golden-red, remove from oven, cool to room temperature, and slice to serve."
        ],
        "tags": {
            "dietary": ["vegetarian"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["rolled oats", "coconut milk", "egg", "milk powder", "butter", "sugar"]
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
            "pdf_pages": [68],
            "printed_page_numbers": [123],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "5:5 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0100",
        "name_mm": "ရွှေဖရုံသီးဆနွင်းမကင်း",
        "name_en": "Pumpkin Pudding",
        "description_mm": "ရွှေဖရုံသီးနူးနူး၊ ကျောက်ကျော၊ အုန်းနို့တို့ဖြင့် ပြုလုပ်ထားသော အောက်ခံအလွှာနှင့် အုန်းနို့ဦးရည်၊ ဂျုံ၊ ကြက်ဥ၊ နို့မှုန့်တို့ဖြင့် ပေါင်းစပ်ဖုတ်ထားသော အပေါ်ယံကပ်စတက်အလွှာ နှစ်ထပ် ရွှေဖရုံသီးဆနွင်းမကင်း။",
        "description_en": "Two-layered royal pumpkin dessert combining a smooth pumpkin-coconut agar pudding base with a rich baked golden egg custard topping.",
        "category": "dessert",
        "meal_types": ["snack", "dessert"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0162",
                "name_mm": "ရွှေဖရုံသီး",
                "name_en": "Pumpkin",
                "original_name": "ရွှေဖရုံသီး",
                "quantity": 1.5,
                "unit": "ပိဿာ (kg)",
                "original_quantity_text": "၁ ၁/၂ ပိဿာ",
                "normalized_quantity": 2449.4,
                "normalized_unit": "g",
                "preparation_note_mm": "အခွံခွာ အတုံးသေးတုံးပြီး နူးအိအောင် ပြုတ်၍ အနှစ်ရအောင် တိုက်ထားသော",
                "preparation_note_en": "peeled, cubed, boiled, and puréed"
            },
            {
                "ingredient_id": "I0147",
                "name_mm": "ကျောက်ကျောမှုန့်",
                "name_en": "Agar-agar powder",
                "original_name": "ကျောက်ကျောမှုန့် (မြန်မာဖြစ်)",
                "quantity": 1.0,
                "unit": "ထုပ် (g)",
                "original_quantity_text": "၁ ထုပ်",
                "normalized_quantity": 25.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီး (ခြစ်ပြီး)",
                "quantity": 3.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၃ လုံး",
                "normalized_quantity": 3.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခြစ်ပြီး",
                "preparation_note_en": "grated"
            },
            {
                "ingredient_id": "I0012",
                "name_mm": "ရေနွေး",
                "name_en": "Hot water",
                "original_name": "ရေနွေး",
                "quantity": 9.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၉ နို့ဆီဘူး",
                "normalized_quantity": 2700.0,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 60.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၆၀ ကျပ်သား (အောက်အလွှာ ၄၀၊ အပေါ်အလွှာ ၂၀)",
                "normalized_quantity": 979.74,
                "normalized_unit": "g",
                "preparation_note_mm": "အောက်အလွှာနှင့် အပေါ်အလွှာအတွက် ခွဲသုံးရန်",
                "preparation_note_en": "divided between base and topping"
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 2.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၂ စပဇ",
                "normalized_quantity": 30.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0002",
                "name_mm": "ထောပတ်",
                "name_en": "Butter",
                "original_name": "ထောပတ်",
                "quantity": 1.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ စပဇ",
                "normalized_quantity": 15.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0043",
                "name_mm": "ဂျုံမှုန့်",
                "name_en": "Wheat flour",
                "original_name": "ဂျုံမှုန့်",
                "quantity": 12.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၂ ၁/၂ ကျပ်သား",
                "normalized_quantity": 204.1,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0026",
                "name_mm": "ကြက်ဥ",
                "name_en": "Chicken egg",
                "original_name": "ကြက်ဥ",
                "quantity": 6.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၆ လုံး",
                "normalized_quantity": 6.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခေါက်ထားသော",
                "preparation_note_en": "beaten"
            },
            {
                "ingredient_id": "I0161",
                "name_mm": "နို့မှုန့်",
                "name_en": "Milk powder",
                "original_name": "နို့မှုန့်",
                "quantity": 10.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁၀ စပဇ",
                "normalized_quantity": 150.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "ရွှေဖရုံသီးကို နူးအောင်ပြုတ်၍ ဆန်ကာဖြင့် အနှစ်တိုက်ပြီး အုန်းသီးမှ ဦးရည် (၂) ဘူးနှင့် နှောင်းရည် (၇) ဘူး ညှစ်ယူထားပါ။",
            "အောက်အလွှာအတွက် ရွှေဖရုံသီးအနှစ်၊ နှောင်းရည် (၆) ဘူး၊ ကျောက်ကျောမှုန့်၊ ဆား၊ သကြားတို့ ရောမွှေကျိုပြီး ပျစ်လာလျှင် ထောပတ်ထည့်ကာ ဗန်းထဲသို့ ဖြန့်ထည့်၍ မျက်နှာပြင်ညှိပါ။",
            "အပေါ်အလွှာအတွက် ဦးရည် (၂) ဘူး၊ နှောင်းရည် (၁) ဘူးထဲသို့ ဂျုံမှုန့်၊ နို့မှုန့်၊ သကြား၊ ဆား၊ ကြက်ဥခေါက်တို့ကို သမအောင် ရောမွှေစစ်ထားပါ။",
            "အောက်အလွှာမျက်နှာပြင်ပေါ်သို့ အပေါ်အလွှာမုန့်ရည်ကို ဖြည်းဖြည်းချင်း လောင်းထည့်ပြီး အပေါ်မီးဖြင့် ဖုတ်ပါ။",
            "မျက်နှာပြင် တင်း၍ အနီရောင်သမ်းစပြုလာလျှင် မီးဖယ်ကာ အခန်းအပူချိန်တွင် အအေးခံပြီး လှီးစိတ်၍ တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Boil pumpkin until tender, mash through a sieve to make a fine purée; extract 2 tins of coconut cream and 7 tins of thin coconut milk.",
            "For the bottom layer, simmer pumpkin purée, 6 tins of thin coconut milk, agar powder, salt, and sugar until thick, stir in butter, pour into a baking dish, and smooth the top.",
            "For the custard topping, whisk together 2 tins of coconut cream, 1 tin of thin milk, flour, milk powder, sugar, salt, and beaten eggs, then strain smooth.",
            "Gently pour the custard mixture over the set pumpkin base and bake with top broiler heat.",
            "When the custard sets firm and browns with a golden crust, remove from oven, cool completely at room temperature, slice, and serve."
        ],
        "tags": {
            "dietary": ["vegetarian"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["pumpkin", "coconut milk", "egg", "agar-agar", "milk powder", "flour"]
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
            "pdf_pages": [68],
            "printed_page_numbers": [123],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "5:5 instruction parity verified.",
            "verified": True
        }
    }
]
