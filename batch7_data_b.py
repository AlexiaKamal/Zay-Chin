# -*- coding: utf-8 -*-
"""
Batch 7 Part B: Traditional Myanmar Sweets & Snacks (မုန့်ပဲသွားရည်စာများ)
Covers Fried & Steamed Snacks, Traditional Pancakes & Sweet Drinks
Recipes R0101 to R0117 (Book pp. 124-132 / PDF pp. 69-73).
"""

NEW_INGREDIENTS_BATCH7_B = [
    {
        "ingredient_id": "I0163",
        "name_mm": "ကောက်ညှင်း",
        "name_en": "Glutinous rice",
        "aliases_mm": ["ကောက်ညှင်းဆန်", "ကောက်ညှင်းဖြူ"],
        "aliases_en": ["sticky rice", "sweet rice"],
        "category": "dry_goods",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0164",
        "name_mm": "မုန့်ဖုတ်ဆော်ဒါ",
        "name_en": "Baking soda",
        "aliases_mm": ["ဆော်ဒါ", "ဆော်ဒါမှုန့်"],
        "aliases_en": ["sodium bicarbonate", "cooking soda"],
        "category": "dry_goods",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0165",
        "name_mm": "ထုံးကျောက်တက်ရည်",
        "name_en": "Limewater",
        "aliases_mm": ["ထုံးရည်ကြည်", "ထုံးကြည်ရည်"],
        "aliases_en": ["slaked limewater", "calcium hydroxide solution"],
        "category": "condiment",
        "default_unit": "ml"
    },
    {
        "ingredient_id": "I0166",
        "name_mm": "ငှက်ပျောဖက်",
        "name_en": "Banana leaves",
        "aliases_mm": ["ဖက်ရွက်", "တောင်စွန်ဖက်"],
        "aliases_en": ["wrapping leaves", "steaming leaves"],
        "category": "produce",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0167",
        "name_mm": "နို့ဆီ",
        "name_en": "Sweetened condensed milk",
        "aliases_mm": ["နို့ဆီဘူး"],
        "aliases_en": ["condensed milk"],
        "category": "dairy",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0168",
        "name_mm": "နို့စိမ်း",
        "name_en": "Evaporated milk",
        "aliases_mm": ["နို့စိမ်းဘူး"],
        "aliases_en": ["unsweetened condensed milk"],
        "category": "dairy",
        "default_unit": "ml"
    },
    {
        "ingredient_id": "I0169",
        "name_mm": "မုန့်လုပ်ဆောင်းဖတ်",
        "name_en": "Rice droplets (Cendol pods)",
        "aliases_mm": ["မုန့်လက်ဆောင်းဖတ်"],
        "aliases_en": ["cendol jelly", "rice pandan drops"],
        "category": "dry_goods",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0170",
        "name_mm": "မြေပဲ",
        "name_en": "Peanuts",
        "aliases_mm": ["မြေပဲစိမ်း", "မြေပဲစေ့"],
        "aliases_en": ["raw groundnuts", "peanuts"],
        "category": "dry_goods",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0171",
        "name_mm": "နှမ်း",
        "name_en": "Sesame seeds",
        "aliases_mm": ["နှမ်းစေ့", "နှမ်းလှော်"],
        "aliases_en": ["white sesame", "toasted sesame"],
        "category": "dry_goods",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0172",
        "name_mm": "မတ်ပဲ",
        "name_en": "Black gram",
        "aliases_mm": ["မတ်ပဲခြမ်း", "မတ်ပဲစေ့"],
        "aliases_en": ["urad dal", "black lentil"],
        "category": "dry_goods",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0173",
        "name_mm": "စားတော်ပဲ",
        "name_en": "Yellow split peas",
        "aliases_mm": ["စားတော်ပဲပြုတ်", "ပဲခြမ်း"],
        "aliases_en": ["marrowfat peas", "boiled yellow peas"],
        "category": "dry_goods",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0174",
        "name_mm": "ရနံ့မွှေးဆီ",
        "name_en": "Flavouring essence",
        "aliases_mm": ["ရနံ့မွှေး", "ဗနီလာ"],
        "aliases_en": ["food essence", "vanilla essence"],
        "category": "condiment",
        "default_unit": "ml"
    },
    {
        "ingredient_id": "I0175",
        "name_mm": "ရေခဲ",
        "name_en": "Ice cubes",
        "aliases_mm": ["ရေခဲတုံး", "ရေခဲမှုန့်"],
        "aliases_en": ["crushed ice", "cube ice"],
        "category": "condiment",
        "default_unit": "g"
    }
]

BATCH7_RECIPES_B = [
    {
        "recipe_id": "R0101",
        "title_mm": "မုန့်လက်ကောက်ကြော်",
        "title_en": "Bracelet Crispie (Mont Let Kauk Kyaw)",
        "alternative_titles_mm": ["မုန့်လက်ကောက်"],
        "alternative_titles_en": ["Burmese Doughnut Rings", "Mont Let Kauk"],
        "description_mm": "ကောက်ညှင်းနှင့် ဆန်ကြမ်းကို ရေစိမ်ကြိတ်၍ လက်ကောက်သဏ္ဌာန်ကွင်းပြုလုပ်ကာ ရွှေဝါရောင်ကြော်ပြီး ထန်းလျက်ရည်ပျစ်ပျစ်ဖြင့် တွဲဖက်တည်ခင်းသော မြန်မာ့ရိုးရာ မုန့်ကြော်ဖြစ်သည်။",
        "description_en": "Traditional Myanmar bracelet-shaped crispy rice doughnuts made from ground glutinous and regular rice, deep-fried to a golden crisp and served glazed or dipped in rich jaggery syrup.",
        "course": "dessert",
        "cuisine": "Myanmar",
        "servings": 20,
        "prep_time_minutes": None,
        "cooking_time_minutes": None,
        "total_time_minutes": None,
        "difficulty": "medium",
        "ingredients": [
            {
                "ingredient_id": "I0163",
                "name_mm": "ကောက်ညှင်း",
                "name_en": "Glutinous rice",
                "original_name": "ကောက်ညှင်း",
                "quantity": 5.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၅ နို့ဆီဘူး",
                "normalized_quantity": 1250.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ရေဆေးပြီး တစ်ညစိမ်ထားရန်",
                "preparation_note_en": "washed and soaked overnight"
            },
            {
                "ingredient_id": "I0001",
                "name_mm": "ဆန်",
                "name_en": "Rice",
                "original_name": "ဆန်ကြမ်း",
                "quantity": 1.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၁ နို့ဆီဘူး",
                "normalized_quantity": 250.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ကောက်ညှင်းနှင့် အတူရောစိမ်ထားရန်",
                "preparation_note_en": "soaked together with glutinous rice"
            },
            {
                "ingredient_id": "I0007",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 1.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ စပဇ",
                "normalized_quantity": 15.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0164",
                "name_mm": "မုန့်ဖုတ်ဆော်ဒါ",
                "name_en": "Baking soda",
                "original_name": "ဆော်ဒါ",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ",
                "quantity": None,
                "unit": "လိုအပ်သရွေ့ (as needed)",
                "original_quantity_text": "လိုအပ်သရွေ့",
                "normalized_quantity": None,
                "normalized_unit": "ml",
                "preparation_note_mm": "မုန့်နယ်ရန်",
                "preparation_note_en": "for kneading dough"
            },
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": None,
                "unit": "လိုအပ်သရွေ့ (as needed)",
                "original_quantity_text": "မြုပ်အောင်ကြော်ရန် ဆီလိုအပ်သရွေ့",
                "normalized_quantity": None,
                "normalized_unit": "ml",
                "preparation_note_mm": "မြုပ်အောင်ကြော်ရန်",
                "preparation_note_en": "for deep-frying"
            },
            {
                "ingredient_id": "I0054",
                "name_mm": "ထန်းလျက်",
                "name_en": "Jaggery",
                "original_name": "ထန်းလျက်ခဲ",
                "quantity": 50.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅၀ ကျပ်သား",
                "normalized_quantity": 816.5,
                "normalized_unit": "g",
                "preparation_note_mm": "ထန်းလျက်ရည်ပြုလုပ်ရန်",
                "preparation_note_en": "for jaggery dipping syrup"
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ",
                "quantity": 1.5,
                "unit": "နို့ဆီဘူး (ml)",
                "original_quantity_text": "၁ ၁/၂ နို့ဆီဘူး",
                "normalized_quantity": 450.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ထန်းလျက်ကျိုရန်",
                "preparation_note_en": "for dissolving jaggery"
            },
            {
                "ingredient_id": "I0007",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ထန်းလျက်ရည်ထဲထည့်ရန်",
                "preparation_note_en": "for jaggery syrup"
            }
        ],
        "instructions_mm": [
            "ကောက်ညှင်းနှင့် ဆန်ကြမ်းကို ရေဆေးပြီး တစ်ညစိမ်ကာ ကြိတ်ဆုံ၌ ကြိတ်ပြီး မုန့်အိတ်တွင် ထည့်၍ အလေးဖိကာ ရေစစ်ထားပါ။",
            "ရေစစ်သွားလျှင် ဇလုံတွင်ထည့်ပြီး ဆားနှင့် ဆော်ဒါထည့်ကာ ရေအနည်းငယ်ဖြင့် မုန့်နှစ်အစေးပေါက်ကာ ပျော့သည်အထိ နယ်ပါ။",
            "မုန့်ညက်နှစ်အပျော့ကို သံပရာသီးအလတ်အရွယ်ခန့် လုံးယူကာ လက်ဖဝါးနှစ်ဖက်ဖြင့် လိပ်ပေးပြီး အလျားလိုက်ရှည်ဆန့်ထွက်လာလျှင် လက်ကောက်သဏ္ဌာန်ဝိုင်း၍ အစွန်းနှစ်ဖက်ကို ထိစပ်ဆက်ပါ။",
            "ဒယ်အိုးတွင် ဆီများများထည့်၍ အပူပေးပြီး ပူလာသောအခါ မုန့်ကွင်းများကို တစ်ခုချင်း ဖြည်းဖြည်းလျှောထည့်ကာ မုန့်သားများပွပြီး ဝိုင်းဖောင်းလာအောင် သံယောက်မဖြင့် ဆီပတ်ပေးရင်း အညီအမျှ ရွှေဝါရောင်သမ်းအောင် ကြော်ပါ။",
            "ကျက်လျှင် ဆီစစ်ဆန်ခါတပ် ယောက်မဖြင့် ဆယ်ယူ ဆီစစ်ထားပါ။",
            "ထန်းလျက်ရည်အတွက် ထန်းလျက်၊ ရေ၊ ဆားတို့ကို အိုးတွင်ရော၍ ထန်းလျက်ပျော်သည်အထိ တည်ကာ အမှိုက်စစ်ပြီးနောက် မီးအေးအေးဖြင့် ကြက်မြီးတန်းသည့် အပျစ်အနေရောက်အောင် ကျို၍ အအေးခံကာ မုန့်လက်ကောက်ကြော်နှင့် တွဲဖက်တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "Wash glutinous rice and regular rice, soak overnight, grind finely with water, place in a cloth press bag, and weigh down to press out excess water.",
            "Transfer the strained rice dough into a mixing bowl, add salt and baking soda, and knead with a small amount of water until smooth, pliable, and elastic.",
            "Pinch dough portions roughly the size of a lime, roll between palms into long uniform ropes, form each rope into a circle (bracelet shape), and pinch the two ends firmly together to seal.",
            "Heat ample oil in a deep frying pan; when hot, slide the dough rings in gently one by one, basting continuously with hot oil using a spatula so they puff up evenly and fry to a golden crisp.",
            "Once cooked and crispy, remove with a slotted wire skimmer and drain well on a rack.",
            "For the syrup, simmer jaggery, water, and salt until dissolved, strain away impurities, then simmer on low heat until thick syrup forms a thin thread ('chicken-tail' consistency); cool and serve alongside the crispy bracelet cakes."
        ],
        "tags": {
            "dietary": ["vegetarian", "vegan"],
            "seasonal": ["all-year"],
            "festival": ["Thadingyut", "Tazaungdaing"],
            "main_ingredients": ["glutinous rice", "rice", "jaggery", "baking soda", "oil"]
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
            "pdf_pages": [69],
            "printed_page_numbers": [124],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "6:6 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0102",
        "title_mm": "မုန့်ဆီကြော်",
        "title_en": "Crispy Cake (Mont Hsi Gyaw)",
        "alternative_titles_mm": ["မုန့်ဆီကြော်"],
        "alternative_titles_en": ["Burmese Sweet Deep-Fried Rice Cake", "Mont Si Gyaw"],
        "description_mm": "ကောက်ညှင်း၊ ဆန်ကြမ်း၊ ထန်းလျက်ရည်နှင့် ဆော်ဒါတို့ကို ဖောက်ထားသော မုန့်ရည်ကို ဆီပူပူ၌ အပြားကြော်ပြီး မြေပဲလှော်နှင့် အုန်းသီးစိတ်တို့ ဖြူးကာ ရိုးရာအတိုင်း ပြုလုပ်သော ရိုးရာမုန့်ဆီကြော်ဖြစ်သည်။",
        "description_en": "Classic Myanmar sweet fried rice cake made from fermented batter of glutinous rice, regular rice, jaggery syrup, and baking soda, fried in oil and garnished with roasted peanuts and fresh coconut shreds.",
        "course": "dessert",
        "cuisine": "Myanmar",
        "servings": 20,
        "prep_time_minutes": 360,
        "cooking_time_minutes": None,
        "total_time_minutes": None,
        "difficulty": "medium",
        "ingredients": [
            {
                "ingredient_id": "I0163",
                "name_mm": "ကောက်ညှင်း",
                "name_en": "Glutinous rice",
                "original_name": "ကောက်ညှင်း",
                "quantity": 4.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၄ နို့ဆီဘူး",
                "normalized_quantity": 1000.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ရေစိမ်ပြီး အတူကြိတ်ရန်",
                "preparation_note_en": "soaked and ground with regular rice"
            },
            {
                "ingredient_id": "I0001",
                "name_mm": "ဆန်",
                "name_en": "Rice",
                "original_name": "ဆန်ကြမ်း",
                "quantity": 1.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၁ နို့ဆီဘူး",
                "normalized_quantity": 250.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ကောက်ညှင်းနှင့် အတူကြိတ်ရန်",
                "preparation_note_en": "ground together"
            },
            {
                "ingredient_id": "I0054",
                "name_mm": "ထန်းလျက်",
                "name_en": "Jaggery",
                "original_name": "ထန်းလျက်",
                "quantity": 40.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၄၀ ကျပ်သား",
                "normalized_quantity": 653.2,
                "normalized_unit": "g",
                "preparation_note_mm": "ကြက်မြီးတန်းအခြေအနေထိ ကျိုထားရန်",
                "preparation_note_en": "simmered to a thin syrup"
            },
            {
                "ingredient_id": "I0007",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 1.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ စပဇ",
                "normalized_quantity": 15.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0164",
                "name_mm": "မုန့်ဖုတ်ဆော်ဒါ",
                "name_en": "Baking soda",
                "original_name": "ဆော်ဒါ",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ",
                "quantity": None,
                "unit": "လိုအပ်သရွေ့ (as needed)",
                "original_quantity_text": "လိုအပ်သရွေ့",
                "normalized_quantity": None,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": None,
                "unit": "လိုအပ်သရွေ့ (as needed)",
                "original_quantity_text": "မြုပ်အောင်ကြော်ရန် ဆီလိုအပ်သရွေ့",
                "normalized_quantity": None,
                "normalized_unit": "ml",
                "preparation_note_mm": "ကြော်ရန်",
                "preparation_note_en": "for deep-frying"
            },
            {
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီး",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အမျှင်လှီးခြစ်ပြီး",
                "preparation_note_en": "finely shredded"
            },
            {
                "ingredient_id": "I0170",
                "name_mm": "မြေပဲ",
                "name_en": "Peanuts",
                "original_name": "မြေပဲ",
                "quantity": 10.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၀ ကျပ်သား",
                "normalized_quantity": 163.3,
                "normalized_unit": "g",
                "preparation_note_mm": "လှော်ပြီး လှီးထားရန်",
                "preparation_note_en": "roasted and chopped"
            }
        ],
        "instructions_mm": [
            "ကောက်ညှင်းနှင့် ဆန်ကြမ်းကို တစ်ညရေစိမ်ပြီး အတူရောကြိတ်ကာ မုန့်အိတ်တွင်ထည့်၍ အပေါ်မှ အလေးဖိကာ ရေစစ်ထားပါ။",
            "ထန်းလျက်ကို ကြက်မြီးတန်းအနေအထိ ကျိုပြီး အအေးခံထားပါ။",
            "အေးလျှင် မုန့်နှစ်၊ ဆား၊ ဆော်ဒါနှင့် ရေအနည်းငယ်ရော၍ ဖောက်ထားပြီး မုန့်ရည်တွင် အမြှုပ်ကလေးများ ပလုံစီလာသည်အထိ (သို့မဟုတ် ၆ နာရီခန့်) ဖောက်ထားပါ။",
            "မုန့်ကြော်ဒယ်ပြားကြီးတွင် ဆီအလုံအလောက်ထည့်ကာ အငွေ့ထွက်ပြီး ပူလာသည်အထိ စောင့်ပါ။",
            "ဆီကျက်လျှင် မုန့်ရည်ကို ဇွန်းကြီးတစ်ဇွန်းအပြည့်စာ ခပ်ယူ၍ မုန့်ကြော်ဒယ်အိုးပြားပေါ် လောင်းချပြီး မုန့်ရည်များကို ရနိုင်သည့်အကျယ်အထိ ဇွန်းဖြင့်ပင် ဖြန့်ပေးပါ။",
            "ဖြန့်ပြီးလျှင်ပြီးချင်း မုန့်မျက်နှာပြင်ပေါ်သို့ လှီးစိတ်ထားသည့် မြေပဲဆံလေးများကို ဖြန့်ဖြူးပေးပါ။",
            "မုန့်သားများ နီညိုလာကာ ကြွပ်ရွလာသည့်အခါတွင် ဝါးချွန်းတံဖြင့် မုန့်ဆီကြော်၏ အောက်ဘက်မှ ထိုးကာ ကလော်ယူပြီး ဆယ်မကာ လင်ဗန်းပေါ်သို့တင်၍ ဆီစစ်ထားပြီး စားခါနီးတွင် အုန်းသီးမျှင်ဖြူးပေးပါ။"
        ],
        "instructions_en": [
            "Soak glutinous rice and regular rice overnight, grind together finely, pack into a cloth bag, and weigh down to press out water.",
            "Simmer jaggery with water until it reaches a thin thread consistency, then let cool completely.",
            "Combine the strained dough, cooled jaggery syrup, salt, baking soda, and a splash of water, mix into a smooth batter, and leave to ferment for about 6 hours until bubbly.",
            "Heat ample oil in a wide flat-bottomed frying pan until aromatic and shimmering hot.",
            "Ladle one generous scoop of batter onto the hot pan, spreading it quickly outward with the back of the ladle to form a thin round pancake.",
            "Immediately scatter the chopped roasted peanuts across the wet surface before it sets.",
            "When the pancake turns deep reddish-brown and crisp, lift it up from beneath using a bamboo skewer, drain on a perforated tray, and top with fresh coconut shreds just before serving."
        ],
        "tags": {
            "dietary": ["vegetarian", "vegan"],
            "seasonal": ["all-year"],
            "festival": ["Thadingyut", "Tazaungdaing"],
            "main_ingredients": ["glutinous rice", "rice", "jaggery", "peanuts", "coconut", "oil"]
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
            "pdf_pages": [69],
            "printed_page_numbers": [124],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "7:7 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0103",
        "title_mm": "မုန့်လုံးကြီးကြော်",
        "title_en": "Deep Fried Gluten Ball (Mont Lon Gyi Gyaw)",
        "alternative_titles_mm": ["မုန့်လုံးကြီးကြော်", "မုန့်ကြက်ဥပုန်း"],
        "alternative_titles_en": ["Sweet Stuffed Sesame Rice Balls", "Mont Lone Gyi Kyaw"],
        "description_mm": "ကောက်ညှင်းမုန့်နှစ်ဖြင့် အုန်းသီးသကြားယိုဌာပနာကို အလယ်မှထည့်ကာ လုံးဝန်းစွာ ပိတ်ဆို့ပြီး ဆီပူတွင် ရွှေဝါရောင်သမ်းပြီး ဖောင်းကားလာသည်အထိ ကြော်ထားသော မြန်မာ့ရိုးရာ မုန့်လုံးကြီးကြော်ဖြစ်သည်။",
        "description_en": "Traditional Myanmar large deep-fried glutinous rice balls stuffed with sweet caramelized coconut filling, deep-fried until puffed, golden, and crispy on the outside with a chewy interior.",
        "course": "dessert",
        "cuisine": "Myanmar",
        "servings": 20,
        "prep_time_minutes": None,
        "cooking_time_minutes": None,
        "total_time_minutes": None,
        "difficulty": "medium",
        "ingredients": [
            {
                "ingredient_id": "I0163",
                "name_mm": "ကောက်ညှင်း",
                "name_en": "Glutinous rice",
                "original_name": "ကောက်ညှင်း",
                "quantity": 5.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၅ နို့ဆီဘူး",
                "normalized_quantity": 1250.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ရေစိမ်ပြီး ကြိတ်စစ်ထားရန်",
                "preparation_note_en": "soaked and ground"
            },
            {
                "ingredient_id": "I0001",
                "name_mm": "ဆန်",
                "name_en": "Rice",
                "original_name": "ဆန်ကြမ်း",
                "quantity": 1.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၁ နို့ဆီဘူး",
                "normalized_quantity": 250.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ကောက်ညှင်းနှင့် အတူကြိတ်ရန်",
                "preparation_note_en": "ground together"
            },
            {
                "ingredient_id": "I0007",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 1.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ စပဇ",
                "normalized_quantity": 15.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0164",
                "name_mm": "မုန့်ဖုတ်ဆော်ဒါ",
                "name_en": "Baking soda",
                "original_name": "ဆော်ဒါ",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ",
                "quantity": None,
                "unit": "လိုအပ်သရွေ့ (as needed)",
                "original_quantity_text": "လိုအပ်သရွေ့",
                "normalized_quantity": None,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": None,
                "unit": "လိုအပ်သရွေ့ (as needed)",
                "original_quantity_text": "မြုပ်အောင်ကြော်ရန် ဆီလိုအပ်သရွေ့",
                "normalized_quantity": None,
                "normalized_unit": "ml",
                "preparation_note_mm": "ကြော်ရန်",
                "preparation_note_en": "for deep-frying"
            },
            {
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီး",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အမျှင်ပုံခြစ်ပြီး ဌာပနာပြုလုပ်ရန်",
                "preparation_note_en": "shredded for sweet filling"
            },
            {
                "ingredient_id": "I0021",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 30.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၃၀ ကျပ်သား",
                "normalized_quantity": 489.9,
                "normalized_unit": "g",
                "preparation_note_mm": "ဌာပနာအတွက်",
                "preparation_note_en": "for sweet filling"
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ",
                "quantity": 2.0,
                "unit": "စားပွဲဇွန်း (tbsp / ml)",
                "original_quantity_text": "၂ စပဇ",
                "normalized_quantity": 30.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ဌာပနာကျိုရန်",
                "preparation_note_en": "for cooking filling"
            }
        ],
        "instructions_mm": [
            "ဌာပနာအတွက် အုန်းသီး၊ သကြားနှင့် ရေ ၂ စားပွဲဇွန်းတို့ကို အိုးတစ်လုံးတွင် ရောထည့်ပြီး မီးအေးအေးတွင်တင်ကာ မွှေပေးပါ။ အုန်းသီးမျှင်များ နွမ်းပြီး ယိုကဲ့သို့ စေးကပ်လာလျှင် ဆယ်ယူအအေးခံထားပါ။",
            "မုန့်လုံးကြီးကြော်အတွက် မုန့်ညက်သားကို မုန့်လက်ကောက်ကြော် မုန့်ညက်သားနည်းအတိုင်း စေးပိုင်နေအောင် ပြုလုပ်နယ်ထားပါ။",
            "မုန့်ညက်သားကို သံပရာသီးလုံးခန့်ယူကာ လက်ဝါးပေါ်တင်၍ တစ်ဖက်လက်ဝါးအကူအညီဖြင့် မထူမပါး ခပ်ပြားပြား ဝိုင်းသဏ္ဌာန် ပြုလုပ်ပါ။",
            "၎င်းအပြားပေါ်သို့ အုန်းယိုဌာပနာ သင့်ရုံထည့်ပြီး မုန့်အနားသားများဖြင့် အုပ်ကာ လုံအောင်ပိတ်ပြီး လုံးဝန်းသွားအောင် လုံးပါ။",
            "ဒယ်အိုးတွင် ဆီများများထည့်၍ အပူပေးပြီး ပူနေသောဆီထဲသို့ မုန့်လုံးကြီးများကို တစ်လုံးစီ ဖြည်းဖြည်းချင်းထည့်ကာ ဆီမြုပ်အောင် ကြော်ပါ။",
            "မုန့်လုံးများ ပွ၍ ဖောင်းကားလာပြီး မျက်နှာပြင်အားလုံး နီရောင်သမ်းလာအောင် ယောက်မဖြင့် လှန်လှောကြော်ပေးပါ။",
            "ကျက်လျှင် ဆယ်ယူပြီး ဆီစစ်ထားကာ နွေးနွေးထွေးထွေး တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "For the filling, combine shredded coconut, sugar, and 2 tablespoons of water in a saucepan over gentle heat, stirring until the coconut turns translucent and syrupy; set aside to cool.",
            "Prepare the elastic glutinous dough following the Mont Let Kauk dough preparation method until well-kneaded and cohesive.",
            "Pinch off a lime-sized ball of dough and flatten it into an even, circular disc between your palms.",
            "Place a spoonful of sweet coconut filling in the center, gather the edges over the filling to seal tightly, and roll smooth between palms into a round ball.",
            "Heat deep oil in a wok and gently lower the stuffed dough balls one by one into the hot oil.",
            "Fry with constant gentle rolling and basting as the balls puff up significantly and turn an even, appetizing golden brown.",
            "Lift out with a wire strainer, drain excess oil thoroughly, and serve warm."
        ],
        "tags": {
            "dietary": ["vegetarian", "vegan"],
            "seasonal": ["all-year"],
            "festival": ["Thadingyut"],
            "main_ingredients": ["glutinous rice", "rice", "coconut", "sugar", "oil"]
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
            "pdf_pages": [69],
            "printed_page_numbers": [125],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "7:7 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0104",
        "title_mm": "မုန့်သိုင်းခြုံ",
        "title_en": "Shredded Coconut Candy in Patty Cases (Mont Thaing Choun)",
        "alternative_titles_mm": ["မုန့်သိုင်းခြုံ"],
        "alternative_titles_en": ["Folded Sweet Coconut Crepe", "Mont Thaing Chan"],
        "description_mm": "ကောက်ညှင်း၊ ဆန်၊ ဘဲဥတို့ဖြင့် ပါးလွှာသော မုန့်ခွံကြော်ကာ အလယ်တွင် အုန်းသီးသကြားယို ဌာပနာထည့်၍ လေးထောင့်ရှည်သဏ္ဌာန် ခေါက်ရစ်ဖုတ်ထားသော မုန့်ဖြစ်သည်။",
        "description_en": "Crispy yet tender crepe parcels made from glutinous rice, rice flour, and duck eggs, filled with sweet cooked shredded coconut and folded into neat rectangular pouches.",
        "course": "dessert",
        "cuisine": "Myanmar",
        "servings": 20,
        "prep_time_minutes": None,
        "cooking_time_minutes": None,
        "total_time_minutes": None,
        "difficulty": "medium",
        "ingredients": [
            {
                "ingredient_id": "I0163",
                "name_mm": "ကောက်ညှင်း",
                "name_en": "Glutinous rice",
                "original_name": "ကောက်ညှင်း",
                "quantity": 2.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၂ နို့ဆီဘူး",
                "normalized_quantity": 500.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ရေစိမ်ပြီး ကြိတ်စစ်ထားရန်",
                "preparation_note_en": "soaked and ground"
            },
            {
                "ingredient_id": "I0001",
                "name_mm": "ဆန်",
                "name_en": "Rice",
                "original_name": "ဆန်ကြမ်း",
                "quantity": 2.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၂ နို့ဆီဘူး",
                "normalized_quantity": 500.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ကောက်ညှင်းနှင့် အတူကြိတ်ရန်",
                "preparation_note_en": "ground together"
            },
            {
                "ingredient_id": "I0007",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 0.5,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "အနည်းငယ်",
                "normalized_quantity": 2.5,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0021",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 20.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၀ ကျပ်သား",
                "normalized_quantity": 326.6,
                "normalized_unit": "g",
                "preparation_note_mm": "မုန့်ရည်ထဲထည့်ရန်",
                "preparation_note_en": "for crepe batter"
            },
            {
                "ingredient_id": "I0027",
                "name_mm": "ဘဲဥ",
                "name_en": "Duck egg",
                "original_name": "ဘဲဥ",
                "quantity": 4.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၄ လုံး",
                "normalized_quantity": 4.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခေါက်ထားရန်",
                "preparation_note_en": "beaten"
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ",
                "quantity": 3.0,
                "unit": "နို့ဆီဘူး (ml)",
                "original_quantity_text": "၃ နို့ဆီဘူး",
                "normalized_quantity": 900.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "မုန့်ရည်ဖျော်ရန်",
                "preparation_note_en": "for batter"
            },
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": None,
                "unit": "လိုအပ်သရွေ့ (as needed)",
                "original_quantity_text": "လိုအပ်သရွေ့",
                "normalized_quantity": None,
                "normalized_unit": "ml",
                "preparation_note_mm": "ဒယ်အိုးသုတ်ရန်",
                "preparation_note_en": "for greasing pan"
            },
            {
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီး",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "မျှင်ပြီး ဌာပနာအတွက်",
                "preparation_note_en": "shredded for filling"
            },
            {
                "ingredient_id": "I0021",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 30.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၃၀ ကျပ်သား",
                "normalized_quantity": 489.9,
                "normalized_unit": "g",
                "preparation_note_mm": "ဌာပနာအတွက်",
                "preparation_note_en": "for filling"
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ",
                "quantity": 2.0,
                "unit": "စားပွဲဇွန်း (tbsp / ml)",
                "original_quantity_text": "၂ စပဇ",
                "normalized_quantity": 30.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ဌာပနာကျိုရန်",
                "preparation_note_en": "for filling"
            }
        ],
        "instructions_mm": [
            "ဌာပနာအတွက် အုန်းသီးမျှင်၊ သကြားနှင့် ရေ ၂ စားပွဲဇွန်းတို့ကို မီးအေးအေးတွင်တင်၍ မွှေကာ ခပ်ထပ်ထပ်အနေတွင် ချပြီး အအေးခံထားပါ။",
            "ကောက်ညှင်းနှင့် ဆန်ကို တစ်ညရေစိမ်ပြီး အတူကြိတ်ကာ မုန့်အိတ်တွင်ထည့်၍ အပေါ်မှ အလေးဖိကာ ရေစစ်ထားပါ။",
            "ခွက်ထဲသို့ မုန့်နှစ်၊ ဆား၊ သကြား၊ ဘဲဥနှင့် ရေ ၃ နို့ဆီဘူး ရောစပ်ပြီး မပျစ်မကျဲ မုန့်ရည်အနေရလျှင် ခေတ္တထားလိုက်ပါ။",
            "မုန့်ဖုတ်အိုး အပြားဝိုင်းကြီးပေါ် ဆီအနည်းငယ်မျှ သုတ်လိမ်းကာ ပူအောင်လုပ်ပါ။",
            "အိုးဆီပူလာလျှင် သတ်မှတ်ထားသည့် ဇွန်းဖြင့် ခပ်ယူကာ မုန့်ရည်ကိုထည့်ပြီး ဇွန်းဖြင့် မထူမပါး လေးထောင့်ညီအောင် ဖြန့်ပေးပါ။",
            "မုန့်သား တင်းစပြုလျှင် အုန်းယိုကို အလယ်တွင် ဇွန်းတစ်ဇွန်းစာခန့်ထည့်ပြီး ယောက်မဖြင့် အနားသားကို လေးဘက်ညီ ဖုံးခေါက်ကာ လေးထောင့်ရှည်ရှည်လာလျှင် မုန့်သားကို အိုးကင်းပူတိုက်သကဲ့သို့ ဆီနုနု ဆွတ်ပေးပါ။",
            "မုန့်သား မတူးအောင် လှည့်ပေးပြီး ကျက်လျှင် အိုးမှချယူကာ ပန်းကန်တွင်ထည့်၍ တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "For the filling, simmer shredded coconut, sugar, and 2 tablespoons of water over low heat until sticky and fragrant, then set aside to cool.",
            "Soak glutinous rice and regular rice overnight, grind together finely, place in a cloth bag, and weigh down to press dry.",
            "In a bowl, mix the pressed rice flour, salt, sugar, beaten duck eggs, and 3 milk tins of water into a smooth, pourable crepe batter, and rest briefly.",
            "Lightly oil a wide flat griddle and heat gently over medium-low heat.",
            "Ladle batter onto the hot surface, spreading it evenly with the ladle into a thin rectangular or circular sheet.",
            "Once the crepe sets, place a spoonful of sweet coconut filling in the center, fold the edges inwards from all four sides over the filling to form a neat oblong packet, and lightly brush the surface with oil to crisp.",
            "Turn gently to cook without burning, remove when golden and set, and serve neatly on a platter."
        ],
        "tags": {
            "dietary": ["vegetarian"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["glutinous rice", "rice", "duck egg", "coconut", "sugar"]
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
            "pdf_pages": [69],
            "printed_page_numbers": [125],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "7:7 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0105",
        "title_mm": "မုန့်လင်မယား",
        "title_en": "Mini Couple Pancake (Mont Lin Mayar)",
        "alternative_titles_mm": ["မုန့်လင်မယား", "မုန့်အုတ်ခွက်"],
        "alternative_titles_en": ["Burmese Couple Pancakes", "Mont Lin Ma Yar"],
        "description_mm": "ဆန်နှင့် မတ်ပဲနှစ်ကို အပေါက်ခွက်ငယ်များပါသော မြေအိုးခွက်ပြားတွင် ဆီသုတ်ဖုတ်ပြီး ပဲပြုတ်၊ ကြက်သွန်မြိတ် (သို့မဟုတ် ငုံးဥ) ထည့်ကာ နှစ်ခြမ်းကို ကပ်၍ လင်မယားတွဲသဖွယ် ပြုလုပ်သော လူကြိုက်များသည့် ရိုးရာလမ်းဘေးမုန့်ဖြစ်သည်။",
        "description_en": "Iconic Myanmar street snack known as 'Husband and Wife Cakes', consisting of miniature crispy rice-and-urad-dal cakes cooked in dimpled cast-iron or earthenware pans, topped with boiled peas, scallions, or quail eggs, joined together in pairs and sprinkled with roasted sesame salt.",
        "course": "dessert",
        "cuisine": "Myanmar",
        "servings": 20,
        "prep_time_minutes": 180,
        "cooking_time_minutes": None,
        "total_time_minutes": None,
        "difficulty": "medium",
        "ingredients": [
            {
                "ingredient_id": "I0001",
                "name_mm": "ဆန်",
                "name_en": "Rice",
                "original_name": "ဆန်",
                "quantity": 4.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၄ နို့ဆီဘူး",
                "normalized_quantity": 1000.0,
                "normalized_unit": "g",
                "preparation_note_mm": "မတ်ပဲနှင့် ရေစိမ်ကြိတ်ရန်",
                "preparation_note_en": "soaked and ground with urad dal"
            },
            {
                "ingredient_id": "I0172",
                "name_mm": "မတ်ပဲ",
                "name_en": "Black gram",
                "original_name": "မတ်ပဲ",
                "quantity": 0.5,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၁/၂ နို့ဆီဘူး",
                "normalized_quantity": 125.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ဆန်နှင့် အတူကြိတ်ရန်",
                "preparation_note_en": "ground together"
            },
            {
                "ingredient_id": "I0007",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 1.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ စပဇ",
                "normalized_quantity": 15.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0164",
                "name_mm": "မုန့်ဖုတ်ဆော်ဒါ",
                "name_en": "Baking soda",
                "original_name": "ဆော်ဒါ",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0173",
                "name_mm": "စားတော်ပဲ",
                "name_en": "Yellow split peas",
                "original_name": "စားတော်ပဲပြုတ်",
                "quantity": None,
                "unit": "လိုအပ်သရွေ့ (as needed)",
                "original_quantity_text": "လိုအပ်သရွေ့",
                "normalized_quantity": None,
                "normalized_unit": "g",
                "preparation_note_mm": "ပြုတ်ထားရန်",
                "preparation_note_en": "boiled"
            },
            {
                "ingredient_id": "I0025",
                "name_mm": "ကြက်သွန်မြိတ်",
                "name_en": "Spring onion",
                "original_name": "ကြက်သွန်မြိတ်",
                "quantity": None,
                "unit": "လိုအပ်သရွေ့ (as needed)",
                "original_quantity_text": "လိုအပ်သရွေ့",
                "normalized_quantity": None,
                "normalized_unit": "g",
                "preparation_note_mm": "ရိတ်ရိတ်လှီးထားရန်",
                "preparation_note_en": "finely chopped"
            },
            {
                "ingredient_id": "I0141",
                "name_mm": "ငုံးဥ",
                "name_en": "Quail eggs",
                "original_name": "ငုံးဥ",
                "quantity": None,
                "unit": "လိုအပ်သရွေ့ (as needed)",
                "original_quantity_text": "အစိမ်း (နှစ်သက်လျှင် လိုအပ်သရွေ့)",
                "normalized_quantity": None,
                "normalized_unit": "piece",
                "preparation_note_mm": "အစိမ်းဖောက်ထည့်ရန်",
                "preparation_note_en": "raw, optional topping"
            },
            {
                "ingredient_id": "I0171",
                "name_mm": "နှမ်း",
                "name_en": "Sesame seeds",
                "original_name": "နှမ်းလှော်နှင့် ဆားထောင်း",
                "quantity": None,
                "unit": "လိုအပ်သရွေ့ (as needed)",
                "original_quantity_text": "လိုအပ်သရွေ့",
                "normalized_quantity": None,
                "normalized_unit": "g",
                "preparation_note_mm": "ဆားနှင့် ရောထောင်းထားရန်",
                "preparation_note_en": "toasted and pounded with salt"
            },
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": None,
                "unit": "လိုအပ်သရွေ့ (as needed)",
                "original_quantity_text": "ဆီထည့်သည်ဆိုရုံမျှ",
                "normalized_quantity": None,
                "normalized_unit": "ml",
                "preparation_note_mm": "မုန့်ခွက်များတွင် ဆီသုတ်ရန်",
                "preparation_note_en": "for brushing dimpled pan"
            }
        ],
        "instructions_mm": [
            "မတ်ပဲနှင့် ဆန်ကို တစ်ညရေစိမ်ပြီး အတူကြိတ်ကာ ရလာသည့် မုန့်နှစ်ကို အစေးပေါက်အောင် နယ်ပါ။",
            "မုန့်နှစ်တွင် ဆားနှင့် ဆော်ဒါရောစပ်ကာ ရေဖြင့် ခပ်ကျဲကျဲဖောက်ထားပြီး ၃ နာရီခန့် ထားပါ။",
            "ဒယ်အိုးပြားထူထူတွင် အဝိုင်းပုံစံ အောက်နက်နက် အလုံးပေါက်လေးများ ပါရှိသည့် အထူးစီမံထားသော အိုးကင်းပြားကို မီးဖိုပေါ်တင်၍ အပူပေးပါ။",
            "ပူလာလျှင် အောက်နက်ခွက်လေးများထဲသို့ ဆီထည့်သည်ဆိုရုံမျှ ထည့်ပေးပြီး ဖျော်စပ်ထားသည့် မုန့်နှစ်ရည်ကျဲကို ခွက်လေးများအပြည့် ထည့်ပါ။",
            "မုန့်မျက်နှာပြင်ပေါ်သို့ ကြက်သွန်မြိတ်နှင့် ပဲပြုတ်ဖြူးပါ (တချို့က ငုံးဥ အလုံးလိုက် ဖောက်ထည့်သည်)။",
            "အပေါ်မှ မုန့်ခွက်နှင့် ပုံစံကိုက်လုပ်ထားသည့် မြေအိုးအဖုံးလေး ဖုံးအုပ်ထားပါ။",
            "ကျက်လျှင် ဇွန်းငယ်ဖြင့် ကော်ယူပြီး အဖုံးဖုံးသကဲ့သို့ နှစ်ခုကို တွဲစပ်ကာ နှမ်းထောင်းဖြူး၍ တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "Soak rice and urad dal overnight, grind together finely, and knead the dough until elastic.",
            "Mix in salt and baking soda, thin with water into a runny batter, and allow to ferment for about 3 hours.",
            "Place a heavy multi-dimpled pan or traditional clay poffertjes-style stove over medium heat.",
            "Once heated, lightly grease each dimpled indentation with oil, then ladle the fermented batter to fill each cup.",
            "Scatter boiled yellow peas and finely sliced spring onions over each cake (or crack a whole quail egg into each cup if desired).",
            "Cover with matching individual or pan-wide clay lids to steam-bake until cooked through.",
            "When crisped at the bottom, scoop out pairs, press their flat faces together like a married couple, and serve warm dusted with toasted sesame salt."
        ],
        "tags": {
            "dietary": ["vegetarian"],
            "seasonal": ["all-year", "monsoon", "winter"],
            "festival": [],
            "main_ingredients": ["rice", "black gram", "yellow peas", "spring onion", "sesame seeds"]
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
            "pdf_pages": [70],
            "printed_page_numbers": [126],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "7:7 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0106",
        "title_mm": "ငှက်ပျောသီးကဗျာလွတ်ကြော်",
        "title_en": "Fried Plain Banana (Banana Fritter)",
        "alternative_titles_mm": ["ငှက်ပျောသီးကဗျာလွတ်ကြော်"],
        "alternative_titles_en": ["Batter-free Fried Bananas", "Caramelized Fried Bananas"],
        "description_mm": "ဖီးကြမ်းငှက်ပျောသီးအမှည့်ကို မုန့်နှစ်မပါဘဲ အလုံးလိုက် ဆီမြုပ်အောင် ကြော်ပြီးနောက် သကြားဖြူးကာ ရွှေညိုရောင် တည်ခင်းသော ရိုးရှင်းအရသာရှိသည့် ငှက်ပျောသီးကြော်ဖြစ်သည်။",
        "description_en": "Sweet and caramelized Myanmar deep-fried bananas prepared without any batter coating ('Kabya-lut'), deep-fried whole until richly browned, drained, and generously dusted with sugar.",
        "course": "dessert",
        "cuisine": "Myanmar",
        "servings": 20,
        "prep_time_minutes": None,
        "cooking_time_minutes": None,
        "total_time_minutes": None,
        "difficulty": "easy",
        "ingredients": [
            {
                "ingredient_id": "I0149",
                "name_mm": "ငှက်ပျောသီး",
                "name_en": "Banana",
                "original_name": "ဖီးကြမ်းငှက်ပျောသီး (အမှည့်)",
                "quantity": 20.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂၀ လုံး",
                "normalized_quantity": 20.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "မှည့်မှည့်ပျော့ပျော့ အခွံမခွာခင် အဝတ်ဖြင့် သုတ်သန့်စင်ထားရန်",
                "preparation_note_en": "ripe and soft, wiped clean"
            },
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": 20.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၀ ကျပ်သား",
                "normalized_quantity": 326.6,
                "normalized_unit": "g",
                "preparation_note_mm": "မြုပ်အောင်ကြော်ရန်",
                "preparation_note_en": "for deep-frying"
            },
            {
                "ingredient_id": "I0021",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.6,
                "normalized_unit": "g",
                "preparation_note_mm": "မုန့်မျက်နှာပြင်ပေါ် ဖြူးရန်",
                "preparation_note_en": "for dusting"
            }
        ],
        "instructions_mm": [
            "ဖီးကြမ်းငှက်ပျောသီး မှည့်မှည့်ပျော့ပျော့ကို အခွံမခွာခင် အလုံးလိုက် အဝတ်ဖြင့်သုတ်ကာ သန့်စင်ပြီးမှ အခွံများနွှာပြီး ခွက်တစ်ခုထဲသို့ ပုံမပျက် ထည့်ထားပါ။",
            "ဒယ်အိုးတွင် ဆီထည့်၍ အပူပေးပြီး ပူလာသည်အထိ စောင့်ပါ။",
            "ဆီပူလာလျှင် ငှက်ပျောသီးတစ်လုံးစီ ဖြည်းဖြည်းချင်းထည့်၍ ဆီမြုပ်အောင် ကြော်ပါ။",
            "နီရောင်သမ်းလာလျှင် ဆန်ခါပေါက်ပါသော ယောက်မပြားဖြင့် ဆယ်ယူပြီး ဆီစုပ်စက္ကူခင်းထားသော ဗန်းပေါ် ခေတ္တတင်ထားပါ။",
            "တည်ခင်းမည့် ပန်းကန်ပြားတွင် ငှက်ပျောသီးကြော်များကို စီ၍တင်ပြီး သကြားနှံ့အောင် ဖြူးပေးကာ တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "Wipe ripe, soft Fee-Gyan bananas clean with a cloth before peeling, then carefully remove peels without squashing the fruit.",
            "Heat cooking oil in a deep frying pan over medium heat until shimmering hot.",
            "Gently lower whole bananas into the hot oil one by one to deep-fry immersed.",
            "When the bananas turn richly browned and caramelized, lift out using a slotted skimmer and drain briefly on absorbent paper.",
            "Arrange the fried bananas neatly on a serving platter, dust generously with granulated sugar, and serve warm."
        ],
        "tags": {
            "dietary": ["vegetarian", "vegan"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["banana", "oil", "sugar"]
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
            "pdf_pages": [70],
            "printed_page_numbers": [126],
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
        "recipe_id": "R0107",
        "title_mm": "ကောက်ညှင်းဘိန်းမုန့်",
        "title_en": "Baked Gluten Rice Cake (Kauk Hnyinn Bein Mont)",
        "alternative_titles_mm": ["ကောက်ညှင်းဘိန်းမုန့်"],
        "alternative_titles_en": ["Burmese Glutinous Rice Pancake", "Kauk Hnyin Bein Moun"],
        "description_mm": "ကောက်ညှင်းနှင့် ဆန်ကို ရေစိမ်ကြိတ်၍ ထန်းလျက်ရည်နှင့် ရောစပ်ကာ အုန်းသီးလွှာ၊ မြေပဲဆံ၊ ဘိန်းစေ့တို့ ဖြူးပြီး အပေါ်မီးအောက်မီးဖြင့် ဖုတ်ထားသော မြန်မာ့ရိုးရာ ကောက်ညှင်းဘိန်းမုန့်ဖြစ်သည်။",
        "description_en": "Traditional Myanmar hearth-baked pancake made from glutinous rice batter sweetened with jaggery, topped generously with coconut ribbons, raw peanuts, and poppy seeds, baked with top and bottom fire coals.",
        "course": "dessert",
        "cuisine": "Myanmar",
        "servings": 20,
        "prep_time_minutes": None,
        "cooking_time_minutes": None,
        "total_time_minutes": None,
        "difficulty": "medium",
        "ingredients": [
            {
                "ingredient_id": "I0163",
                "name_mm": "ကောက်ညှင်း",
                "name_en": "Glutinous rice",
                "original_name": "ကောက်ညှင်း",
                "quantity": 1.0,
                "unit": "ပြည် (g)",
                "original_quantity_text": "၁ ပြည်",
                "normalized_quantity": 2000.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ဆန်နှင့် အတူရေစိမ်ကြိတ်ရန်",
                "preparation_note_en": "soaked and ground"
            },
            {
                "ingredient_id": "I0001",
                "name_mm": "ဆန်",
                "name_en": "Rice",
                "original_name": "ဆန်",
                "quantity": 2.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၂ နို့ဆီဘူး",
                "normalized_quantity": 500.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ကောက်ညှင်းနှင့် ရောကြိတ်ရန်",
                "preparation_note_en": "ground together"
            },
            {
                "ingredient_id": "I0007",
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
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီး",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အလွှာဖတ်လေးများ လုပ်ထားရန်",
                "preparation_note_en": "cut into thin ribbon flakes"
            },
            {
                "ingredient_id": "I0170",
                "name_mm": "မြေပဲ",
                "name_en": "Peanuts",
                "original_name": "မြေပဲ (အစိမ်း)",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.6,
                "normalized_unit": "g",
                "preparation_note_mm": "အခွံခွာ၍ ပါးပါးလှီးထားရန်",
                "preparation_note_en": "skinned and thinly sliced"
            },
            {
                "ingredient_id": "I0054",
                "name_mm": "ထန်းလျက်",
                "name_en": "Jaggery",
                "original_name": "ထန်းလျက်",
                "quantity": 80.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၈၀ ကျပ်သား",
                "normalized_quantity": 1306.4,
                "normalized_unit": "g",
                "preparation_note_mm": "အမြှုပ်ပွ၍ ပျစ်လာသည်အထိ ကျိုထားရန်",
                "preparation_note_en": "boiled to thick syrup"
            },
            {
                "ingredient_id": "I0073",
                "name_mm": "ထောပတ်",
                "name_en": "Butter",
                "original_name": "ထောပတ်",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.6,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0107",
                "name_mm": "ဘိန်းစေ့",
                "name_en": "Poppy seeds",
                "original_name": "ဘိန်းစေ့",
                "quantity": 5.0,
                "unit": "မတ်သား (g)",
                "original_quantity_text": "၅ မတ်သား",
                "normalized_quantity": 20.4,
                "normalized_unit": "g",
                "preparation_note_mm": "ဖြူးရန်",
                "preparation_note_en": "for topping"
            }
        ],
        "instructions_mm": [
            "ကောက်ညှင်းနှင့် ဆန်ကို တစ်ညရေစိမ်ပြီး အတူရောကြိတ်ကာ မုန့်အိတ်တွင်ထည့်၍ အပေါ်မှ အလေးဖိကာ ရေစစ်ထားပါ။",
            "အုန်းသီးကို အလွှာဖတ်လေးများ လုပ်ထားပြီး မြေပဲကို အခွံချွတ်၍ ပါးပါးလှီးထားပါ။",
            "ထန်းလျက်ကို အမြှုပ်ပွ၍ ပျစ်လာသည်တိုင်အောင် ကျိုပြီးနောက် အိုးတစ်လုံးထဲသို့ မုန့်နှစ်၊ ဆားတို့နှင့်အတူ ရောစပ်ကာ ဝါးဆန်ခါဖြင့် တိုက်ချထားပါ။",
            "မုန့်ဖုတ်ဗန်းထဲသို့ ပထမ ထောပတ်ထည့်ကာ အပူပေးပြီးနောက် မုန့်ရည်များ လောင်းထည့်ပါ။",
            "အုန်းသီးနှင့် မြေပဲကို မျက်နှာပြင်အနှံ့ ဖြူးပြီး အပေါ်မီးများများ၊ အောက်မီးနည်းနည်းဖြင့် ၅ မိနစ်ခန့် ဖုတ်ပါ။",
            "ဘရုတ်ရှ် (သို့) အဝတ်စပတ်ထားသည့် တုတ်တံကို ဆီတို့ပြီး မျက်နှာပြင်ကို ဆီရိုက်ပေးပါ။",
            "မျက်နှာပြင် နီရောင်သမ်းလာလျှင် ဘိန်းစေ့ဖြူးကာ ကျက်နပ်သည်အထိ ဆက်ဖုတ်ပြီး ချပါ။"
        ],
        "instructions_en": [
            "Soak glutinous rice and rice overnight, grind together finely, pack in a cloth bag, and weigh down to press out water.",
            "Cut coconut meat into thin ribbons; peel raw peanuts and slice thinly.",
            "Simmer jaggery until foamy and thick, then combine with the strained dough and salt, pressing through a bamboo strainer to make a smooth batter.",
            "Heat butter in a round baking pan, then pour in the batter.",
            "Scatter sliced coconut and peanuts evenly over the surface, and bake with abundant top coals and gentle bottom heat for about 5 minutes.",
            "Baste the top surface lightly with oil using a brush or cloth swab.",
            "When the surface turns rich reddish-golden, sprinkle with poppy seeds and continue baking until fully cooked and set."
        ],
        "tags": {
            "dietary": ["vegetarian"],
            "seasonal": ["all-year", "winter"],
            "festival": ["Tazaungdaing"],
            "main_ingredients": ["glutinous rice", "jaggery", "coconut", "peanuts", "poppy seeds", "butter"]
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
            "pdf_pages": [70],
            "printed_page_numbers": [127],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "7:7 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0108",
        "title_mm": "ဂျုံဘိန်းမုန့်",
        "title_en": "Baked Wheat Cake (Gyoun Bein Mont)",
        "alternative_titles_mm": ["ဂျုံဘိန်းမုန့်"],
        "alternative_titles_en": ["Burmese Wheat Flour Hearth Pancake", "Bein Moun"],
        "description_mm": "ဂျုံမှုန့်၊ အုန်းနို့၊ နို့ဆီ၊ နို့မှုန့်၊ ကြက်ဥ၊ ထောပတ်တို့ဖြင့် ချိုမွှေးစွာ ဖျော်စပ်ပြီး အုန်းသီးလွှာ၊ မြေပဲဆံ၊ ဘိန်းစေ့တို့ဖြင့် အပေါ်မီးအောက်မီးဖုတ်ထားသော မွှေးပျံ့သည့် ဂျုံဘိန်းမုန့်ဖြစ်သည်။",
        "description_en": "Rich and fragrant baked pancake made from wheat flour, coconut milk, condensed milk, milk powder, eggs, and butter, topped with coconut strips, peanuts, and poppy seeds.",
        "course": "dessert",
        "cuisine": "Myanmar",
        "servings": 20,
        "prep_time_minutes": None,
        "cooking_time_minutes": None,
        "total_time_minutes": None,
        "difficulty": "medium",
        "ingredients": [
            {
                "ingredient_id": "I0072",
                "name_mm": "ဂျုံမှုန့်",
                "name_en": "Wheat flour",
                "original_name": "ဂျုံ (ဆန်ခါချပြီး)",
                "quantity": 30.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၃၀ ကျပ်သား",
                "normalized_quantity": 489.9,
                "normalized_unit": "g",
                "preparation_note_mm": "ဆန်ခါချပြီး",
                "preparation_note_en": "sifted"
            },
            {
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီး",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ဦးရည်၊ နှောင်းရည် ညှစ်ပြီး တစ်ခြမ်းကို အလွှာဖတ်လုပ်ရန်",
                "preparation_note_en": "pressed for coconut milk, part sliced into ribbons"
            },
            {
                "ingredient_id": "I0170",
                "name_mm": "မြေပဲ",
                "name_en": "Peanuts",
                "original_name": "မြေပဲ (အစိမ်း)",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.6,
                "normalized_unit": "g",
                "preparation_note_mm": "ပါးပါးလှီးထားရန်",
                "preparation_note_en": "raw, thinly sliced"
            },
            {
                "ingredient_id": "I0021",
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
                "ingredient_id": "I0007",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 1.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ စပဇ",
                "normalized_quantity": 15.0,
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
                "preparation_note_mm": "ခေါက်ထားရန်",
                "preparation_note_en": "beaten"
            },
            {
                "ingredient_id": "I0167",
                "name_mm": "နို့ဆီ",
                "name_en": "Sweetened condensed milk",
                "original_name": "နို့ဆီ",
                "quantity": 8.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၈ စပဇ",
                "normalized_quantity": 120.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
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
            },
            {
                "ingredient_id": "I0174",
                "name_mm": "ရနံ့မွှေးဆီ",
                "name_en": "Flavouring essence",
                "original_name": "ရနံ့မွှေး",
                "quantity": 6.0,
                "unit": "စက် (drop)",
                "original_quantity_text": "၆ စက်",
                "normalized_quantity": 0.3,
                "normalized_unit": "ml",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0073",
                "name_mm": "ထောပတ်",
                "name_en": "Butter",
                "original_name": "ထောပတ်",
                "quantity": 3.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၃ ကျပ်သား",
                "normalized_quantity": 48.9,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0107",
                "name_mm": "ဘိန်းစေ့",
                "name_en": "Poppy seeds",
                "original_name": "ဘိန်းစေ့",
                "quantity": 5.0,
                "unit": "မတ်သား (g)",
                "original_quantity_text": "၅ မတ်သား",
                "normalized_quantity": 20.4,
                "normalized_unit": "g",
                "preparation_note_mm": "ဖြူးရန်",
                "preparation_note_en": "for topping"
            }
        ],
        "instructions_mm": [
            "အုန်းသီး ၁ လုံးနှင့် ၁ ခြမ်းကို ခြစ်၍ အုန်းနို့ဦးရည် ညှစ်ယူထားပြီး နှောင်းရည်ကိုလည်း သီးသန့်ထားကာ ကျန်အုန်းသီးခြမ်းကို အလွှာဖတ်လေးများ လှီးထားပါ။",
            "ဦးရည်နှင့် ဂျုံရည်ရောဖျော်ပြီး သကြားနှင့် ဆားကိုလည်း နှောင်းရည်ဖြင့် ရောကျိုကာ အမှိုက်စစ်ထားပါ။",
            "ကြက်ဥခေါက်၊ ဂျုံရည်ဖျော်ထဲသို့ နို့ဆီ၊ နို့မှုန့်၊ နှောင်းရည်၊ ရနံ့မွှေးတို့နှင့်အတူ ထည့်သွင်းရောစပ်ပြီး မပျစ်မကျဲ အနေတော် ဂျုံမုန့်နှစ်ရည်များကို ခေတ္တနှပ်ထားပါ။",
            "မုန့်ဖုတ်ဗန်းကို ထောပတ်ပါးပါးသုတ်ပြီး ဖျော်စပ်ထားသည့် ဂျုံမုန့်နှစ်ရည်များ လောင်းထည့်ပါ။",
            "မျက်နှာပြင်ပေါ်သို့ မြေပဲ၊ အုန်းသီးလွှာများ နှံ့အောင်ဖြူးပြီး အပေါ်မီးများများ၊ အောက်မီးနည်းနည်းဖြင့် ဖုတ်ပါ။",
            "မုန့်မျက်နှာပြင် မတင်းမီအချိန်တွင် ဘိန်းစေ့ဖြူးပေးပြီး လက်ကျန်ထောပတ်ကိုလည်း လောင်းဆမ်းပေးပါ။",
            "မီးပြန်တင်၍ ဖုတ်ကာ မျက်နှာပြင် နီရောင်သမ်းလာလျှင် ကျက်နပ်ပြီဖြစ်၍ ချယူအအေးခံကာ တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "Grate 1 1/2 coconuts and press to extract coconut cream (first press) and thin milk (second press); slice the remaining half coconut into thin ribbons.",
            "Mix coconut cream with the sifted wheat flour; dissolve sugar and salt in warm thin coconut milk and strain.",
            "Whisk beaten eggs, condensed milk, milk powder, flavouring essence, and the sweet thin coconut milk into the flour batter until smooth, then let rest briefly.",
            "Lightly grease a round baking pan with butter and pour in the batter.",
            "Scatter sliced peanuts and coconut ribbons evenly across the top, and bake with hot top coals and gentle bottom heat.",
            "Just before the crust sets completely, sprinkle poppy seeds and drizzle remaining melted butter across the surface.",
            "Return to bake until the top becomes a rich, lustrous golden-red crust, remove, slice, and serve."
        ],
        "tags": {
            "dietary": ["vegetarian"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["flour", "coconut", "condensed milk", "egg", "butter", "peanuts", "poppy seeds"]
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
            "pdf_pages": [70],
            "printed_page_numbers": [127],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "7:7 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0109",
        "title_mm": "ဆန်ဘိန်းမုန့်",
        "title_en": "Baked Rice Cake (Hsan Bein Mont)",
        "alternative_titles_mm": ["ဆန်ဘိန်းမုန့်"],
        "alternative_titles_en": ["Traditional Rice Flour Hearth Cake", "Hsan Bein Moun"],
        "description_mm": "ဆန်နု၊ ဆန်ကြမ်း၊ ထန်းလျက်ရည်နှင့် ဖီးကြမ်းငှက်ပျောသီးချေတို့ကို ရောမွှေဖောက်ကာ အုန်းသီးလွှာ၊ မြေပဲဆံ၊ ဘိန်းစေ့တို့ဖြူး၍ အပေါ်မီးပြင်းပြင်းဖြင့် ဖုတ်ထားသော မွှေးပျံ့သည့် ရိုးရာဆန်ဘိန်းမုန့်ဖြစ်သည်။",
        "description_en": "Rustic traditional baked rice cake made from soaked ground Ngakywe and Ngasein rice batter sweetened with jaggery, mashed Fee-Gyan banana, coconut strips, peanuts, and poppy seeds.",
        "course": "dessert",
        "cuisine": "Myanmar",
        "servings": 20,
        "prep_time_minutes": 360,
        "cooking_time_minutes": None,
        "total_time_minutes": None,
        "difficulty": "medium",
        "ingredients": [
            {
                "ingredient_id": "I0001",
                "name_mm": "ဆန်",
                "name_en": "Rice",
                "original_name": "ဆန်နု (ငကျွဲဆန်)",
                "quantity": 3.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၃ နို့ဆီဘူး",
                "normalized_quantity": 750.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ငစိန်ဆန်နှင့် ရေစိမ်ကြိတ်ရန်",
                "preparation_note_en": "soaked and ground"
            },
            {
                "ingredient_id": "I0001",
                "name_mm": "ဆန်",
                "name_en": "Rice",
                "original_name": "ဆန်ကြမ်း (ငစိန်ဆန်)",
                "quantity": 1.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၁ နို့ဆီဘူး",
                "normalized_quantity": 250.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ငကျွဲဆန်နှင့် ရောကြိတ်ရန်",
                "preparation_note_en": "ground together"
            },
            {
                "ingredient_id": "I0164",
                "name_mm": "မုန့်ဖုတ်ဆော်ဒါ",
                "name_en": "Baking soda",
                "original_name": "ဆော်ဒါမှုန့်",
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
                "name_mm": "ထန်းလျက်",
                "name_en": "Jaggery",
                "original_name": "ထန်းလျက်",
                "quantity": 35.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၃၅ ကျပ်သား",
                "normalized_quantity": 571.5,
                "normalized_unit": "g",
                "preparation_note_mm": "ကြက်မြီးတန်းအောင် ကျိုထားရန်",
                "preparation_note_en": "boiled to thin syrup"
            },
            {
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီး",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အလွှာဖတ်လေးများ ပြုလုပ်ထားရန်",
                "preparation_note_en": "cut into ribbons"
            },
            {
                "ingredient_id": "I0170",
                "name_mm": "မြေပဲ",
                "name_en": "Peanuts",
                "original_name": "မြေပဲ",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.6,
                "normalized_unit": "g",
                "preparation_note_mm": "အခွံခွာ၍ ပါးပါးလှီးထားရန်",
                "preparation_note_en": "peeled and sliced"
            },
            {
                "ingredient_id": "I0149",
                "name_mm": "ငှက်ပျောသီး",
                "name_en": "Banana",
                "original_name": "ငှက်ပျောသီး (ဖီးကြမ်း)",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ချေထည့်ရန်",
                "preparation_note_en": "mashed"
            },
            {
                "ingredient_id": "I0007",
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
                "ingredient_id": "I0107",
                "name_mm": "ဘိန်းစေ့",
                "name_en": "Poppy seeds",
                "original_name": "ဘိန်းစေ့",
                "quantity": 2.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂.၅ ကျပ်သား",
                "normalized_quantity": 40.8,
                "normalized_unit": "g",
                "preparation_note_mm": "ဖြူးရန်",
                "preparation_note_en": "for topping"
            }
        ],
        "instructions_mm": [
            "ဆန်များကို တစ်ည (သို့) ၆ နာရီကြာ ရေစိမ်ပြီး ကြိတ်ကာ မုန့်အိတ်တွင်ထည့်၍ အလေးဖိ ရေစစ်ထားပါ။",
            "ထန်းလျက်ကို ကြက်မြီးတန်းအောင် ကျိုထားပြီး အုန်းသီးကို အလွှာဖတ်လေးများ ပြုလုပ်ထားကာ မြေပဲကို အခွံချွတ်၍ ပါးပါးလှီးထားပါ။",
            "ညသိပ်ထားသော မုန့်နှစ်များထဲသို့ ကျိုပြီးသား ထန်းလျက်ရည်နှင့် ဆားကို ထည့်ပြီး လက်နှစ်ပြီး ပြန်ထုတ်လိုက်သောအခါ မုန့်အညီတင်ရုံမျှ ကျဲကျဲဖျော်ပါ။",
            "ပြီးလျှင် မုန့်နှစ်များကို နာနာမွှေပေးပြီး ဖီးကြမ်းငှက်ပျောသီးချေထည့်၍ တစ်ဖန် ပြန်မွှေကာ အမြှုပ်အနည်းငယ်ထလာလျှင် ဖုတ်ရန်အဆင်သင့်ဖြစ်ပါပြီ။",
            "မုန့်ဖုတ်ဗန်းကို အပူပေး ဆီသုတ်ပြီး မုန့်နှစ်ရည်များ ထည့်ပါ။",
            "မုန့်မျက်နှာပြင်ပေါ်သို့ အုန်းသီးဖတ်လွှာ၊ မြေပဲနှင့် ဘိန်းစေ့များ ဖြူးပါ။",
            "မီးအသင့်ထည့်ထားသည့် အပေါ်မီးတင် သံပြားကို မုန့်ဗန်းပေါ်တင်၍ အပေါ်မီးပြင်း၍ အောက်မီးမှာ မီးခဲများဖြင့် မီးရှိရုံသာထားဖုတ်ကာ မျက်နှာပြင်တင်း၍ နီလာလျှင် ကျက်နပ်ပြီဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Soak both rice varieties for 6 hours or overnight, grind finely, pack into a cloth bag, and weigh down to press out water.",
            "Simmer jaggery until a thin thread forms; slice coconut into thin ribbons, and peel and slice peanuts.",
            "Combine the overnight-rested rice flour with warm jaggery syrup and salt, mixing into a smooth batter that lightly coats a submerged finger.",
            "Whisk vigorously, fold in mashed Fee-Gyan banana, and mix again until fine bubbles appear on top.",
            "Preheat and lightly grease a round baking pan, then pour in the fermented batter.",
            "Scatter sliced coconut ribbons, sliced peanuts, and poppy seeds evenly over the batter.",
            "Cover with a metal tray piled with glowing coals to apply strong top heat while maintaining gentle embers below; bake until the crust turns firm, fragrant, and deep golden-brown."
        ],
        "tags": {
            "dietary": ["vegetarian", "vegan"],
            "seasonal": ["all-year", "winter"],
            "festival": ["Tazaungdaing"],
            "main_ingredients": ["rice", "jaggery", "coconut", "banana", "peanuts", "poppy seeds"]
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
            "pdf_pages": [71],
            "printed_page_numbers": [128],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "7:7 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0110",
        "title_mm": "မုန့်ပျားသလက်",
        "title_en": "Honey Comb Cake (Mont Pya Thalet)",
        "alternative_titles_mm": ["မုန့်ပျားသလက်"],
        "alternative_titles_en": ["Burmese Honeycomb Pancake", "Mont Pyar Tha Let"],
        "description_mm": "ဆန်ကြမ်းမုန့်နှစ်အဖြူရည်နှင့် ထန်းလျက်ကျိုရောမုန့်နှစ်ရည် နှစ်မျိုးစပ်၍ အပေါက်ငယ်များ ပျားသလက်သဖွယ် ဖြစ်ပေါ်စေကာ ကြော်ဖုတ်ထားသော ရိုးရာမုန့်ပျားသလက်ဖြစ်သည်။",
        "description_en": "Famous Myanmar honeycomb pancake cooked in a lidded earthen or cast-iron pot, characterized by a bubbly honeycomb texture formed from two batters (plain white and sweet jaggery-infused), crisp bottom, and soft puffed center.",
        "course": "dessert",
        "cuisine": "Myanmar",
        "servings": 20,
        "prep_time_minutes": 360,
        "cooking_time_minutes": None,
        "total_time_minutes": None,
        "difficulty": "medium",
        "ingredients": [
            {
                "ingredient_id": "I0001",
                "name_mm": "ဆန်",
                "name_en": "Rice",
                "original_name": "ဆန်ကြမ်း",
                "quantity": 4.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၄ နို့ဆီဘူး",
                "normalized_quantity": 1000.0,
                "normalized_unit": "g",
                "preparation_note_mm": "တစ်ညရေစိမ်ကြိတ်ရန်",
                "preparation_note_en": "soaked overnight and ground"
            },
            {
                "ingredient_id": "I0007",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 1.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ စပဇ",
                "normalized_quantity": 15.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0164",
                "name_mm": "မုန့်ဖုတ်ဆော်ဒါ",
                "name_en": "Baking soda",
                "original_name": "ဆော်ဒါ",
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
                "name_mm": "ထန်းလျက်",
                "name_en": "Jaggery",
                "original_name": "ထန်းလျက်",
                "quantity": 20.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၀ ကျပ်သား",
                "normalized_quantity": 326.6,
                "normalized_unit": "g",
                "preparation_note_mm": "ကြက်မြီးတန်းအောင် ကျိုထားရန်",
                "preparation_note_en": "boiled to thin syrup"
            },
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "မြေပဲဆီ",
                "quantity": 25.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၅ ကျပ်သား",
                "normalized_quantity": 408.3,
                "normalized_unit": "g",
                "preparation_note_mm": "မုန့်ဖုတ်အိုးသုတ်ရန်",
                "preparation_note_en": "for seasoning and greasing pot"
            }
        ],
        "instructions_mm": [
            "ဆန်ကို တစ်ညရေစိမ်ကြိတ်ပြီး ရလာသည့် မုန့်နှစ်ကို ဆားနှင့် ဆော်ဒါရောစပ်ကာ အသွင်နှစ်မျိုး ဖောက်ရပါမည်။",
            "တစ်မျိုးမှာ မုန့်နှစ်တွင် ရေရောပြီး ထမင်းရည်ပျစ်ပျစ်သဏ္ဌာန် ဖောက်ထား၍၊ ကျန်တစ်မျိုးမှာ ကြက်မြီးတန်းအောင် ကျိုထားသည့် ထန်းလျက်နှင့် မုန့်နှစ်ကို ရောပြီး အနည်းငယ်ကျဲကျဲသဏ္ဌာန် ဖောက်ထားပါ။",
            "မုန့်ဖုတ်စလောင်းနှင့် အရွယ်တူသည့် မုန့်ဖုတ်အိုးငယ်လေးကို မီးဖိုပေါ်တင်၍ အရင်ဆုံး ပူအောင်ပြုလုပ်ပါ။",
            "အိုးပူလျှင် အိုးအတွင်းမျက်နှာပြင်ကို ဆီတို့ထားသော အဝတ်ထုပ်ဖြင့် ဖိ၍သုတ်လိမ်းပါ။",
            "မုန့်နှစ်အဖြူရည်ကို ဇွန်းဖြင့် ခပ်ယူပြီး ငါးလက်မအရွယ်ခန့်ရအောင် ဖြန့်ထည့်ပြီးနောက် အပေါ်တွင် ထန်းလျက်ရည်ပါသော ခပ်ကျဲကျဲ မုန့်ရည်ကို အောက်ခံမုန့်သား အနားစွန်းချန်ပြီး ထည့်ပေးကာ မုန့်ဘေးနှုတ်ခမ်းသား ပါးပြီး အလယ်သား ထူနေစေရပါမည်။",
            "မုန့်အိုးကို စလောင်းဖုံးဖြင့် ဖုံးလိုက်ပြီး ၃ မိနစ်ခန့်နေလျှင် အဖုံးဖွင့်ကာ ဆီတို့တံဖြင့် မုန့်သားမျက်နှာပြင်ကို အနှံ့တို့ရိုက်ပေးပါ။",
            "မုန့်ကျက်လျှင် သံယောက်မဖြင့် ကော်ယူ၍ ပူပူနွေးနွေး တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "Soak rice overnight, grind finely, and mix the batter with salt and baking soda before dividing into two portions.",
            "Dilute the first portion with water to a thick congee consistency (white batter); mix the second portion with warm jaggery syrup to a thinner consistency (sweet jaggery batter).",
            "Preheat an individual round earthen baking pot with its matching domed lid over a steady fire.",
            "When hot, swab the interior surface firmly with an oil-soaked cloth pad.",
            "Ladle the white batter in first, swirling into a roughly 5-inch round disc, then pour the jaggery batter directly in the center leaving outer rims clear so edges crisp up while the center stays thick and spongy.",
            "Cover tightly with the lid to steam-bake; after about 3 minutes, open and gently dab the honeycomb-pitted surface with an oiled swab.",
            "Once bottom crust is crispy and browned, lift out with a metal spatula and serve fresh and hot."
        ],
        "tags": {
            "dietary": ["vegetarian", "vegan"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["rice", "jaggery", "peanut oil", "baking soda"]
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
            "pdf_pages": [71],
            "printed_page_numbers": [128],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "7:7 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0111",
        "title_mm": "မုန့်လုပ်ဆောင်း",
        "title_en": "Rice Pod Swirl in Sweet Coconut Milk (Mont Lok Saung)",
        "alternative_titles_mm": ["မုန့်လုပ်ဆောင်း", "မုန့်လက်ဆောင်း"],
        "alternative_titles_en": ["Burmese Cendol Drink", "Mont Lat Saung"],
        "description_mm": "ဆန်ကြမ်းနှင့် ဆွမ်းမွှေးရွက်၊ ထုံးကျောက်တက်ရည်တို့ဖြင့် အစက်ချ ပြုလုပ်ထားသော မုန့်လက်ဆောင်းဖတ်များကို မွှေးပျံ့သောအုန်းနို့၊ သကြားရည် (သို့မဟုတ်) ထန်းလျက်ရည်၊ ရေခဲတုံးတို့ဖြင့် ရောစပ်သောက်သုံးရသော မြန်မာ့သင်္ကြန်ရိုးရာ အအေးဖြစ်သည်။",
        "description_en": "Myanmar's quintessential Thingyan festival dessert drink featuring freshly pressed pandan rice droplets (cendol pods) served in rich coconut milk, sweet jaggery or sugar syrup, and crushed ice.",
        "course": "dessert",
        "cuisine": "Myanmar",
        "servings": 20,
        "prep_time_minutes": None,
        "cooking_time_minutes": None,
        "total_time_minutes": None,
        "difficulty": "medium",
        "ingredients": [
            {
                "ingredient_id": "I0001",
                "name_mm": "ဆန်",
                "name_en": "Rice",
                "original_name": "ဆန်ကြမ်း",
                "quantity": 4.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၄ နို့ဆီဘူး",
                "normalized_quantity": 1000.0,
                "normalized_unit": "g",
                "preparation_note_mm": "တစ်ညရေစိမ်ကြိတ်ပြီး ရေစစ်ထားရန်",
                "preparation_note_en": "soaked overnight, ground, and pressed dry"
            },
            {
                "ingredient_id": "I0165",
                "name_mm": "ထုံးကျောက်တက်ရည်",
                "name_en": "Limewater",
                "original_name": "ထုံးကျောက်တက်ရည်",
                "quantity": 1.0,
                "unit": "ဂါလံ (ml)",
                "original_quantity_text": "၁ ဂါလံ",
                "normalized_quantity": 4546.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ထုံးကို ရေဖျော်ပြီး ကျောက်ချဉ်ထည့်၍ ရေကြည်ခံထားသော အရည်",
                "preparation_note_en": "slaked lime dissolved in water with alum and cleared"
            },
            {
                "ingredient_id": "I0157",
                "name_mm": "ဆွမ်းမွှေးရွက်",
                "name_en": "Pandan leaves",
                "original_name": "ဆွမ်းမွှေးရွက်",
                "quantity": 10.0,
                "unit": "ရွက် (sheet)",
                "original_quantity_text": "၁၀ ရွက်",
                "normalized_quantity": 10.0,
                "normalized_unit": "sheet",
                "preparation_note_mm": "ထောင်း၍ အရည်စစ်ယူရန်",
                "preparation_note_en": "pounded and strained for green juice"
            },
            {
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီး",
                "quantity": 5.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၅ လုံး",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခြစ်ပြီး အုန်းနို့ညှစ်ရန်",
                "preparation_note_en": "grated for coconut milk"
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ",
                "quantity": 10.0,
                "unit": "နို့ဆီဘူး (ml)",
                "original_quantity_text": "၁၀ နို့ဆီဘူး",
                "normalized_quantity": 3000.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "အုန်းနို့ညှစ်ရန်",
                "preparation_note_en": "for extracting coconut milk"
            },
            {
                "ingredient_id": "I0007",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 1.5,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁.၅ စပဇ",
                "normalized_quantity": 22.5,
                "normalized_unit": "g",
                "preparation_note_mm": "အုန်းနို့ရည်ထဲထည့်ရန်",
                "preparation_note_en": "for coconut milk seasoning"
            },
            {
                "ingredient_id": "I0168",
                "name_mm": "နို့စိမ်း",
                "name_en": "Evaporated milk",
                "original_name": "နို့စိမ်း",
                "quantity": 1.0,
                "unit": "ဘူး (can / ml)",
                "original_quantity_text": "၁ ဘူး",
                "normalized_quantity": 380.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "အုန်းနို့ရည်ထဲထည့်ရန်",
                "preparation_note_en": "for coconut milk richness"
            },
            {
                "ingredient_id": "I0021",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 25.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၅ ကျပ်သား",
                "normalized_quantity": 408.3,
                "normalized_unit": "g",
                "preparation_note_mm": "သကြားရည်ကျိုရန်",
                "preparation_note_en": "for sugar syrup"
            },
            {
                "ingredient_id": "I0054",
                "name_mm": "ထန်းလျက်",
                "name_en": "Jaggery",
                "original_name": "ထန်းလျက်",
                "quantity": 25.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၅ ကျပ်သား",
                "normalized_quantity": 408.3,
                "normalized_unit": "g",
                "preparation_note_mm": "ထန်းလျက်ရည်ကျိုရန်",
                "preparation_note_en": "for jaggery syrup"
            }
        ],
        "instructions_mm": [
            "ဆန်ကို တစ်ညရေစိမ်ကြိတ်ပြီး ရေစစ်ထားကာ ဆွမ်းမွှေးရွက်ကို ညက်အောင်ထောင်းပြီး အဝတ်ထဲထည့်၍ အရည်စစ်ယူပါ။",
            "မုန့်နှစ်များကို အေးစက်စက်ဖြစ်အောင်နယ်ပြီး ထုံးကျောက်တက်ရည်နှင့်ရောကာ ဆွမ်းမွှေးရည်ထည့်ပြီးနောက် ဒယ်အိုးတွင် မုန့်များကျက်၍ ပျစ်ခဲလာသည်အထိ မွှေကျိုပါ။",
            "ရေအေးထည့်ထားသည့် ခံအိုးပေါ်တွင် အပေါက်ဖောက်ထားသည့် မုန့်လုပ်ဆောင်းသံဆန်ခါပြားကို တင်ပြီး ပူပူနွေးနွေး မုန့်ကျိုနှစ်များကို ခပ်တင်ကာ ဖိတုံးဖြင့် ဖိချပေးပါ။",
            "အပေါက်ငယ်များမှ ရေအေးထဲသို့ ကျလာသည့် မုန့်ဖတ်လေးများကို ဆန်ခါတပ်ယောက်မဖြင့် ဆယ်ယူကာ အဝတ်ခင်းထားသည့် ဇလုံထဲသို့ ထည့်သိမ်းပါ။",
            "အုန်းသီးကို ခြစ်ပြီး ရေ ၁၀ နို့ဆီဘူးဖြင့် အုန်းနို့ ၁၀ နို့ဆီဘူးရအောင် ညှစ်ယူကာ ဆားနှင့် နို့စိမ်းရောစပ်ပြီး အုန်းနို့ရည် ပြုလုပ်ထားပါ။",
            "သကြား ၂၅ ကျပ်သားကို ရေ ၂ နို့ဆီဘူးဖြင့် ကျို၍ သကြားရည်ပြုလုပ်ထားပြီး ထန်းလျက် ၂၅ ကျပ်သားကိုလည်း ရေ ၂ နို့ဆီဘူးဖြင့် ကျို၍ ထန်းလျက်ရည် သီးသန့်ပြုလုပ်ထားပါ။",
            "ဖန်ခွက် (သို့) ပန်းကန်လုံးတွင် မုန့်လုပ်ဆောင်းဖတ် အနေတော်ထည့်၊ ရေခဲတုံးလေးများထည့်၊ အုန်းနို့ရည်ထည့်ပြီး နှစ်သက်ရာ သကြားရည် (သို့) ထန်းလျက်ရည် ဆမ်းကာ အေးမြလန်းဆန်းစွာ တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "Soak rice overnight, grind finely, and press dry; pound pandan leaves and squeeze through cheesecloth to extract deep-green aromatic juice.",
            "Knead the pressed rice dough with limewater and pandan juice, then cook in a wok over medium heat, stirring continuously until the starch gelatinizes into a thick, glossy green paste.",
            "Position a perforated cendol press frame over a large basin filled with cold fresh water, ladle the piping-hot paste onto the plate, and press firmly with a block.",
            "As the warm paste extrudes into cold water, it instantly solidifies into tender teardrop-shaped rice droplets; scoop out with a fine skimmer and store chilled.",
            "Grate coconut and squeeze with 10 tins of water to obtain 10 tins of rich coconut milk, then season with salt and evaporated milk.",
            "Simmer sugar with 2 tins of water into sugar syrup, and simmer jaggery separately with 2 tins of water into rich jaggery syrup.",
            "To serve, place a generous portion of cendol droplets into serving glasses or bowls, add ice cubes, pour over seasoned coconut milk, and drizzle with jaggery or sugar syrup to taste."
        ],
        "tags": {
            "dietary": ["vegetarian", "gluten-free"],
            "seasonal": ["summer", "Thingyan"],
            "festival": ["Thingyan (Water Festival)"],
            "main_ingredients": ["rice", "coconut", "pandan leaf", "limewater", "jaggery", "evaporated milk"]
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
            "pdf_pages": [71],
            "printed_page_numbers": [129],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "7:7 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0112",
        "title_mm": "ရွှေရင်အေး",
        "title_en": "Assorted Cooler Sweet Drink (Shwe Yin Aye)",
        "alternative_titles_mm": ["ရွှေရင်အေး"],
        "alternative_titles_en": ["Myanmar Royal Sweet Cooler", "Shwe Yin Aye Dessert"],
        "description_mm": "မုန့်လက်ဆောင်းဖတ်၊ သာကူပျဉ်၊ ကောက်ညှင်းပေါင်း၊ အုန်းနို့ကျောက်ကျော၊ ပေါင်မုန့်လွှာတို့ကို အုန်းနို့ရည်မွှေးမွှေး၊ သကြားရည်၊ ရေခဲတုံးတို့ဖြင့် တွဲဖက်ပြင်ဆင်သော နာမည်ကျော် မြန်မာ့ရိုးရာ ရွှေရင်အေးအချိုပွဲဖြစ်သည်။",
        "description_en": "The ultimate regal Myanmar iced dessert bowl ('Shwe Yin Aye' or 'Golden Soothing Heart'), bringing together green pandan cendol pods, sago cake cubes, steamed sticky rice, coconut milk agar jelly, and sliced white bread, immersed in iced sweet coconut milk.",
        "course": "dessert",
        "cuisine": "Myanmar",
        "servings": 20,
        "prep_time_minutes": None,
        "cooking_time_minutes": None,
        "total_time_minutes": None,
        "difficulty": "medium",
        "ingredients": [
            {
                "ingredient_id": "I0169",
                "name_mm": "မုန့်လုပ်ဆောင်းဖတ်",
                "name_en": "Rice droplets (Cendol pods)",
                "original_name": "မုန့်လုပ်ဆောင်းဖတ်",
                "quantity": 2.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၂ နို့ဆီဘူး",
                "normalized_quantity": 500.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0156",
                "name_mm": "သာကူစေ့",
                "name_en": "Sago pearls",
                "original_name": "သာကူပျဉ်",
                "quantity": 1.0,
                "unit": "ဗန်း (tray / portion)",
                "original_quantity_text": "၁ ဗန်း",
                "normalized_quantity": 500.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ကျိုပြီး အတုံးလေးများ လှီးထားရန်",
                "preparation_note_en": "cooked sago set in tray, diced"
            },
            {
                "ingredient_id": "I0163",
                "name_mm": "ကောက်ညှင်း",
                "name_en": "Glutinous rice",
                "original_name": "ကောက်ညှင်းပေါင်း",
                "quantity": 40.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၄၀ ကျပ်သား",
                "normalized_quantity": 653.2,
                "normalized_unit": "g",
                "preparation_note_mm": "ပေါင်းပြီးသား",
                "preparation_note_en": "steamed sticky rice"
            },
            {
                "ingredient_id": "I0074",
                "name_mm": "ပေါင်မုန့်",
                "name_en": "Bread",
                "original_name": "ပေါင်မုန့်",
                "quantity": 20.0,
                "unit": "ချပ် (slice)",
                "original_quantity_text": "၂၀ ချပ်",
                "normalized_quantity": 20.0,
                "normalized_unit": "slice",
                "preparation_note_mm": "ပါးပါးလှီးထားရန်",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0147",
                "name_mm": "ကျောက်ကျောမှုန့်",
                "name_en": "Agar-agar powder",
                "original_name": "အုန်းနို့ကျောက်ကျော",
                "quantity": 1.0,
                "unit": "ဗန်း (tray / portion)",
                "original_quantity_text": "၁ ဗန်း",
                "normalized_quantity": 500.0,
                "normalized_unit": "g",
                "preparation_note_mm": "မထူမပါး လှီးထားရန်",
                "preparation_note_en": "prepared coconut milk agar jelly, sliced"
            },
            {
                "ingredient_id": "I0097",
                "name_mm": "အုန်းနို့",
                "name_en": "Coconut milk",
                "original_name": "အုန်းနို့ရည်",
                "quantity": 10.0,
                "unit": "နို့ဆီဘူး (ml)",
                "original_quantity_text": "၁၀ နို့ဆီဘူး",
                "normalized_quantity": 3000.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ဆားအနည်းငယ်ဖြင့် စပ်ထားသော အုန်းနို့ရည်",
                "preparation_note_en": "seasoned sweet coconut milk"
            },
            {
                "ingredient_id": "I0021",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြားရည်",
                "quantity": 20.0,
                "unit": "စားပွဲဇွန်း (tbsp / ml)",
                "original_quantity_text": "၂၀ စပဇ",
                "normalized_quantity": 300.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "သကြားရည်ကျိုထားရန်",
                "preparation_note_en": "thick sugar syrup"
            },
            {
                "ingredient_id": "I0175",
                "name_mm": "ရေခဲ",
                "name_en": "Ice cubes",
                "original_name": "ရေခဲ",
                "quantity": None,
                "unit": "လိုအပ်သရွေ့ (as needed)",
                "original_quantity_text": "လိုအပ်သရွေ့",
                "normalized_quantity": None,
                "normalized_unit": "g",
                "preparation_note_mm": "အတုံးသေးလေးများ",
                "preparation_note_en": "crushed or cubed"
            }
        ],
        "instructions_mm": [
            "မုန့်စားပန်းကန်လုံးစောက်တွင် မုန့်လုပ်ဆောင်းဖတ်ကို အလျင်ထည့်ပါ။",
            "၎င်းအပေါ်မှနေ၍ သာကူပျဉ်အတုံးလေးများကို ထည့်ပါ။",
            "ဆက်လက်၍ ကောက်ညှင်းပေါင်းနှင့် ပါးပါးလှီးထားသည့် ပေါင်မုန့်အချပ်တို့ကို ထည့်ပါ။",
            "အုန်းနို့ကျောက်ကျောကို မထူမပါးလှီး၍ ထည့်ပြီးနောက် အုန်းနို့ရည်လောင်းထည့်ကာ နောက်ဆုံးမှ သကြားရည် လောင်းဆမ်းပြင်ဆင်ပါ။",
            "ရေခဲကို အတုံးသေးလေးများ ပြုလုပ်ပြီး အပေါ်ယံမှ လွှမ်းခြုံပေးကာ အေးမြစွာ သုံးဆောင်နိုင်ပါသည်။ (ဒူးရင်းသီးပေါ်ချိန်တွင် နှစ်သက်ပါက အုန်းနို့ထဲတွင် ဒူးရင်းသီးအသားလွှာများ မွှေကြိတ်ထည့်နိုင်ပါသည်)။"
        ],
        "instructions_en": [
            "In a wide serving dessert bowl, place a portion of green cendol droplets first.",
            "Add diced squares of firm cooked sago pudding over the droplets.",
            "Add a portion of steamed glutinous rice and a slice of tender white bread.",
            "Arrange sliced coconut agar-agar jelly on top, ladle over fragrant coconut milk, and drizzle generously with thick sugar syrup.",
            "Cover the top with finely crushed ice and serve ice-cold. (During durian season, mashed durian pulp may be stirred into the coconut milk for extra aroma)."
        ],
        "tags": {
            "dietary": ["vegetarian"],
            "seasonal": ["summer", "Thingyan"],
            "festival": ["Thingyan (Water Festival)"],
            "main_ingredients": ["cendol", "sago", "glutinous rice", "bread", "agar-agar", "coconut milk", "sugar", "ice"]
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
            "pdf_pages": [72],
            "printed_page_numbers": [130],
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
        "recipe_id": "R0113",
        "title_mm": "သာကူပျဉ်",
        "title_en": "Flattened Pearl Sago (Thargu Byin)",
        "alternative_titles_mm": ["သာကူပျဉ်"],
        "alternative_titles_en": ["Set Sago Pudding Cake", "Thagu Byin"],
        "description_mm": "သာကူစေ့ကို ရေစိမ်ကျိုပြီး ဗန်းထဲတွင် အပြားခဲထားသော သာကူပျဉ်ဖြစ်ပြီး အုန်းနို့ရည်ဆမ်း၍ဖြစ်စေ၊ ရွှေရင်အေးတွင်ထည့်၍ဖြစ်စေ၊ အုန်းသီးမျှင်လူး၍ဖြစ်စေ သုံးဆောင်နိုင်ပါသည်။",
        "description_en": "Versatile Myanmar firm sago pudding cake made from simmered tapioca pearls set in flat trays, enjoyed either drenched in sweet coconut sauce, mixed into Shwe Yin Aye, or coated in freshly grated coconut.",
        "course": "dessert",
        "cuisine": "Myanmar",
        "servings": 20,
        "prep_time_minutes": 120,
        "cooking_time_minutes": None,
        "total_time_minutes": None,
        "difficulty": "easy",
        "ingredients": [
            {
                "ingredient_id": "I0156",
                "name_mm": "သာကူစေ့",
                "name_en": "Sago pearls",
                "original_name": "သာကူ",
                "quantity": 50.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅၀ ကျပ်သား",
                "normalized_quantity": 816.5,
                "normalized_unit": "g",
                "preparation_note_mm": "ရေဖြင့် ၂ နာရီစိမ်ထားရန်",
                "preparation_note_en": "soaked in water for 2 hours"
            },
            {
                "ingredient_id": "I0021",
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
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီး",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အုန်းနို့ဆမ်းလုပ်ရန်အတွက် အုန်းရည်ညှစ်ရန်",
                "preparation_note_en": "for coconut drizzle"
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ",
                "quantity": 1.5,
                "unit": "နို့ဆီဘူး (ml)",
                "original_quantity_text": "၁ ၁/၂ နို့ဆီဘူး",
                "normalized_quantity": 450.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "အုန်းနို့ညှစ်ရန်",
                "preparation_note_en": "for extracting milk"
            },
            {
                "ingredient_id": "I0021",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 25.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၅ ကျပ်သား",
                "normalized_quantity": 408.3,
                "normalized_unit": "g",
                "preparation_note_mm": "အုန်းနို့ဆမ်းထဲထည့်ရန်",
                "preparation_note_en": "for coconut sauce"
            },
            {
                "ingredient_id": "I0007",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": "အုန်းနို့ဆမ်းထဲထည့်ရန်",
                "preparation_note_en": "for coconut sauce"
            },
            {
                "ingredient_id": "I0154",
                "name_mm": "အစာအရောင်ဆိုးဆေး",
                "name_en": "Food coloring",
                "original_name": "အနီရောင်နှင့် အစိမ်းရောင်",
                "quantity": 0.5,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁/၂ လဖဇ",
                "normalized_quantity": 2.5,
                "normalized_unit": "g",
                "preparation_note_mm": "အရောင်နှစ်ထပ်လုပ်လိုပါက",
                "preparation_note_en": "optional for layered coloring"
            },
            {
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီး (ခြစ်ပြီးသန့်သန့်)",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အုန်းသီးမှုန့်လူးစားလိုပါက",
                "preparation_note_en": "grated for tossing"
            }
        ],
        "instructions_mm": [
            "သာကူကို ရေဖြင့် ၂ နာရီကြာ စိမ်ထားပြီးနောက် ဆူနေသော ရေနွေးထဲသို့ သာကူစေ့များ ထည့်၍ မွှေပေးပါ။",
            "သာကူမျက်စေ့ မပျောက်ခင် သကြားထည့်ပြီး ပျစ်ခဲစပြုလာလျှင် အသင့်ပြင်ထားသော မုန့်ဗန်းထဲသို့ ထည့်ကာ မျက်နှာပြင်ညှိပြီး အအေးခံထားပါ။",
            "အုန်းနို့ဆမ်း လုပ်စားလိုပါက အုန်းသီးကို ခြစ်ပြီး အုန်းရည်ညှစ်ကာ သကြား၊ ဆားတို့ရော၍ ပျစ်ပျစ်ကျိုပြီး တုံးထားသည့် သာကူပျဉ်ပေါ်တွင် ဆမ်း၍ စားသုံးနိုင်ပါသည်။",
            "ရွှေရင်အေးအတွက် ရည်စူး၍ ပြုလုပ်သည့် သာကူပျဉ်ဆိုပါက သကြားထည့်ကျိုရန် မလိုအပ်ပါ။",
            "အုန်းသီးမှုန့်လူး စားလိုပါက သာကူပျဉ်ကို အိုးနှစ်အိုးခွဲကျို၍ အနီနှင့် အစိမ်း အရောင်ခွဲထည့်ကာ ဗန်းတွင် နှစ်ထပ်လောင်းထည့် အအေးခံပြီးနောက် ဆနွင်းမကင်းပုံစံ လှီးဖြတ်ကာ အုန်းသီးခြစ်ဖြင့် လူးနယ်၍ တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Soak sago pearls in water for 2 hours, then stir into a pot of rapidly boiling water.",
            "Before the white cores completely dissolve, stir in sugar and cook until thick and glossy, then pour into a flat tray, smooth the surface, and cool until set.",
            "To serve with coconut sauce, grate coconut and extract milk, boil with sugar and salt until rich and syrupy, cut sago into diamond cubes, and drizzle with sauce.",
            "If making sago specifically for Shwe Yin Aye, omit the sugar during boiling.",
            "For coconut-tossed sago, divide into two pots tinted red and green, set into a two-layer tray to cool, slice like sanwin-makin, and toss generously in freshly grated coconut."
        ],
        "tags": {
            "dietary": ["vegetarian", "vegan", "gluten-free"],
            "seasonal": ["all-year"],
            "festival": ["Thingyan"],
            "main_ingredients": ["sago pearls", "sugar", "coconut"]
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
            "pdf_pages": [72],
            "printed_page_numbers": [130],
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
        "recipe_id": "R0114",
        "title_mm": "မုန့်လုံးရေပေါ်",
        "title_en": "Gluten Pellet Floating (Mont Lon Yay Baw)",
        "alternative_titles_mm": ["မုန့်လုံးရေပေါ်"],
        "alternative_titles_en": ["Burmese Floating Rice Balls", "Mont Lone Yay Paw"],
        "description_mm": "ကောက်ညှင်းမုန့်လုံးအတွင်း ထန်းလျက်ခဲစိတ်ကလေးများ ဌာပနာထည့်၍ ရေနွေးပွက်ပွက်ဆူတွင် ပြုတ်ကာ ရေပေါ်ပေါ်လာလျှင် ဆယ်ယူပြီး အုန်းသီးခြစ်ဖြင့် လူးဖြူးစားသုံးရသော သင်္ကြန်ရိုးရာ မုန့်လုံးရေပေါ်ဖြစ်သည်။",
        "description_en": "Iconic Myanmar Thingyan festival sweet consisting of glutinous rice dumplings stuffed with bite-sized chunks of jaggery, boiled until they float to the surface ('Yay Baw'), chilled in cold water, and topped with freshly grated coconut.",
        "course": "dessert",
        "cuisine": "Myanmar",
        "servings": 20,
        "prep_time_minutes": None,
        "cooking_time_minutes": None,
        "total_time_minutes": None,
        "difficulty": "easy",
        "ingredients": [
            {
                "ingredient_id": "I0163",
                "name_mm": "ကောက်ညှင်း",
                "name_en": "Glutinous rice",
                "original_name": "ကောက်ညှင်း",
                "quantity": 5.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၅ နို့ဆီဘူး",
                "normalized_quantity": 1250.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ဆန်နှင့် ရေစိမ်ကြိတ်စစ်ထားရန်",
                "preparation_note_en": "soaked and ground with rice"
            },
            {
                "ingredient_id": "I0001",
                "name_mm": "ဆန်",
                "name_en": "Rice",
                "original_name": "ဆန်ကြမ်း",
                "quantity": 1.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၁ နို့ဆီဘူး",
                "normalized_quantity": 250.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ကောက်ညှင်းနှင့် အတူကြိတ်ရန်",
                "preparation_note_en": "ground together"
            },
            {
                "ingredient_id": "I0007",
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
                "ingredient_id": "I0054",
                "name_mm": "ထန်းလျက်",
                "name_en": "Jaggery",
                "original_name": "ထန်းလျက်",
                "quantity": 20.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၀ ကျပ်သား",
                "normalized_quantity": 326.6,
                "normalized_unit": "g",
                "preparation_note_mm": "အတုံးငယ်လေးများ အချိုးကျ လှီးစိတ်ထားရန်",
                "preparation_note_en": "cut into small bite-sized cubes"
            },
            {
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီး",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခြစ်ပြီး",
                "preparation_note_en": "freshly grated"
            }
        ],
        "instructions_mm": [
            "ကောက်ညှင်းနှင့် ဆန်ကြမ်းကို တစ်ညရေစိမ်ပြီး ကြိတ်ခါတွင် ကြေညက်အောင် ကြိတ်ကာ အဝတ်အိတ်တွင် ထည့်၍ အလေးဖိ ရေစစ်ထားပါ။",
            "မုန့်နှစ်သားကို ဆားထည့်ပြီး အစေးပေါက်ကာ ပျော့ပျောင်းလာသည်အထိ နယ်ပါ။",
            "ရလာသည့် မုန့်ညက်သားကို ကွမ်းသီးလုံးအရွယ် အလုံးလေးများပြုလုပ်ပြီး အလယ်တွင် ထန်းလျက်တုံးလေးများ ဌာပနာထည့်ကာ လုံအောင် ပြန်ပိတ်လုံးပါ။",
            "အိုးကြီးတွင် ရေသုံးပုံနှစ်ပုံထည့်၍ ခပ်ပြင်းပြင်းတည်ကာ ပွက်ပွက်ဆူလာလျှင် မုန့်လုံးလေးများကို ဖြန့်ထည့်ပြုတ်ပါ။",
            "မုန့်လုံးလေးများ ကျက်နပ်လာလျှင် ရေမျက်နှာပြင်ပေါ်သို့ ထင်ရှားစွာ ပေါ်တက်လာပါမည်။",
            "ပေါ်လာသည့် မုန့်လုံးလေးများကို ဆန်ခါတပ်ယောက်မဖြင့် ဆယ်ယူပြီး ရေအေးထည့်ထားသည့် အိုးထဲသို့ ပြောင်းထည့်ကာ ကျန်မုန့်များကိုလည်း ဤနည်းအတိုင်း ဆက်လက်ပြုလုပ်ပါ။",
            "ကျက်ပြီး ရေအေးစိမ်ထားသည့် မုန့်လုံးများကို ပြန်ဆယ်ယူကာ ဆန်ခါစစ်ပေါ် တင်ထားပြီး ရေစစ်သွားလျှင် ပန်းကန်တွင်ပြင်၍ အုန်းသီးအမျှင်များ ဖြူးကာ စားသုံးနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Soak glutinous rice and regular rice overnight, grind extremely fine with water, place in a cloth press bag, and press under heavy weight.",
            "Knead the pressed dough thoroughly with salt until pliable, smooth, and cohesive.",
            "Pinch pieces roughly betel-nut sized, flatten slightly, insert a small cube of jaggery into the center, and roll between palms into a sealed, smooth ball.",
            "Fill a large pot two-thirds full with water and bring to a rolling boil over high heat, then drop the dumplings in evenly.",
            "As the dumplings cook through and the jaggery center melts, they will float clearly to the water surface.",
            "Scoop floating dumplings out using a wire strainer and plunge immediately into a bowl of cold fresh water; repeat for remaining batches.",
            "Transfer dumplings from the cold water onto a perforated drainer, arrange on banana leaves or platters, and generously top with freshly shredded coconut."
        ],
        "tags": {
            "dietary": ["vegetarian", "vegan", "gluten-free"],
            "seasonal": ["summer", "Thingyan"],
            "festival": ["Thingyan (Water Festival)"],
            "main_ingredients": ["glutinous rice", "rice", "jaggery", "coconut"]
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
            "pdf_pages": [72],
            "printed_page_numbers": [131],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "7:7 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0115",
        "title_mm": "အုန်းသီးမုန့်ဖက်ထုပ်",
        "title_en": "Pyramid Shape Hidden Treasure (Ohn Thee Mont Phet Thoke)",
        "alternative_titles_mm": ["အုန်းသီးမုန့်ဖက်ထုပ်"],
        "alternative_titles_en": ["Steamed Coconut Stuffed Rice Pyramids", "Mont Phet Htoke"],
        "description_mm": "ကောက်ညှင်းမုန့်နှစ်အတွင်း အုန်းသီးသကြားယို ဌာပနာထည့်ကာ ငှက်ပျောဖက်ဖြင့် ပိရမစ်ပုံသဏ္ဌာန် လိပ်ထုပ်၍ ရေနွေးငွေ့ဖြင့် ပေါင်းထားသော မြန်မာ့ရိုးရာ မုန့်ဖက်ထုပ်ဖြစ်သည်။",
        "description_en": "Traditional Myanmar pyramidal steamed parcels made from smooth glutinous rice dough filled with caramelized sweet shredded coconut and securely wrapped in fresh banana leaves before steaming.",
        "course": "dessert",
        "cuisine": "Myanmar",
        "servings": 20,
        "prep_time_minutes": None,
        "cooking_time_minutes": 60,
        "total_time_minutes": None,
        "difficulty": "medium",
        "ingredients": [
            {
                "ingredient_id": "I0163",
                "name_mm": "ကောက်ညှင်း",
                "name_en": "Glutinous rice",
                "original_name": "ကောက်ညှင်း",
                "quantity": 4.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၄ နို့ဆီဘူး",
                "normalized_quantity": 1000.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ဆန်နှင့် ရေစိမ်ကြိတ်စစ်ထားရန်",
                "preparation_note_en": "soaked and ground"
            },
            {
                "ingredient_id": "I0001",
                "name_mm": "ဆန်",
                "name_en": "Rice",
                "original_name": "ဆန်",
                "quantity": 1.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၁ နို့ဆီဘူး",
                "normalized_quantity": 250.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ကောက်ညှင်းနှင့် အတူကြိတ်ရန်",
                "preparation_note_en": "ground together"
            },
            {
                "ingredient_id": "I0007",
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
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီး",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခြစ်ပြီး သကြားနှင့် ယိုထိုးထားရန်",
                "preparation_note_en": "grated for sweet coconut filling"
            },
            {
                "ingredient_id": "I0021",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 40.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၄၀ ကျပ်သား",
                "normalized_quantity": 653.2,
                "normalized_unit": "g",
                "preparation_note_mm": "ဌာပနာအတွက်",
                "preparation_note_en": "for sweet filling"
            },
            {
                "ingredient_id": "I0166",
                "name_mm": "ငှက်ပျောဖက်",
                "name_en": "Banana leaves",
                "original_name": "တောင်စွန် (သို့) ငှက်ပျောဖက်",
                "quantity": 20.0,
                "unit": "ရွက် (sheet)",
                "original_quantity_text": "အနားညီ ၈\" အရွယ် ၂၀ ရွက်",
                "normalized_quantity": 20.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "မီးမြှိုက်သန့်စင်ထားသော ၈ လက်မအရွယ်",
                "preparation_note_en": "wilted over flame and cut to 8-inch squares"
            }
        ],
        "instructions_mm": [
            "ကောက်ညှင်းနှင့် ဆန်ကို ရေစိမ်ပြီး အတူရောကြိတ်ကာ မုန့်အိတ်တွင်ထည့်၍ အပေါ်မှ အလေးဖိ ရေစစ်ထားပါ။",
            "အုန်းသီးကို ခြစ်ပြီး သကြားနှင့်အတူ မီးအေးအေးတွင် ကပ်စီးစီးဖြစ်လာသည်အထိ ယိုထိုးထားပါ။",
            "မုန့်နှစ်တွင် ဆားထည့်ပြီး အစေးပေါက်လာကာ ပျော့လာသည်အထိ နယ်ပြီးနောက် သံပရာသီးအလတ်ကြီးအရွယ်ခန့် လုံးယူပါ။",
            "မုန့်လုံးတစ်လုံးကို ဘယ်လက်ဝါးပေါ်တင်ကာ အလယ်ကို ခွက်ပေးလိုက်ပြီး ညာလက်ဖြင့် အုန်းယိုကော်ယူကာ ဌာပနာသွတ်၍ အတွင်းအစာကို လုံအောင် ပြန်ပိတ်ပါ။",
            "၈ လက်မအရွယ် ဖက်ရွက်တစ်ရွက်ကိုယူကာ ကတော့ပုံ (သို့) ပိရမစ်ပုံသဏ္ဌာန် ပြုလုပ်ပြီး အစာသွတ်မုန့်ညက်သား ထည့်ကာ ဖက်အနားစလေးဖက်ကို ကတော့ထိပ်ပိတ်ပုံနည်းအတိုင်း လုံအောင် ပိတ်ထုပ်ပါ။",
            "ပေါင်းချောင်ထဲသို့ မုန့်ဖက်ထုပ်များ ပိတ်ထားသည့်ထိပ်ဘက်မှောက်ကာ အထုပ်များ ဘေးစောင်း စီထည့်ပြီး ပိတ်သည့်ဖက်သည် အိုးဘေးနံရံများနှင့် ထိနေစေရပါမည်။",
            "ရေပွက်ပွက်ဆူနေသော အိုးပေါ်တွင် မုန့်ဖက်ထုပ်ပေါင်းချောင်ကိုတင်ပြီး အဖုံးအုပ်၍ ၁ နာရီခန့်ကြာအောင် ထားပြီး ပေါင်းပါ။"
        ],
        "instructions_en": [
            "Soak glutinous rice and rice, grind together finely with water, place into a cloth bag, and weigh down to press dry.",
            "Grate coconut and cook with sugar over low heat, stirring until caramelized and sticky; let cool.",
            "Knead the pressed dough with salt until smooth and pliable, then divide into large lime-sized portions.",
            "Flatten a dough portion into a cup in your palm, fill the center with sweet coconut preserve, and seal the edges completely.",
            "Shape an 8-inch wilted banana leaf into a pyramid cone, insert the stuffed dough ball, and fold the four flap corners tightly shut.",
            "Arrange the parcels seam-side down into a bamboo steamer tier, lining them firmly against each other and the sides so steam does not dislodge the folds.",
            "Place over a pot of rolling boiling water, cover tightly, and steam for approximately 1 hour until tender and aromatic."
        ],
        "tags": {
            "dietary": ["vegetarian", "vegan", "gluten-free"],
            "seasonal": ["all-year"],
            "festival": ["Thadingyut", "Tazaungdaing"],
            "main_ingredients": ["glutinous rice", "coconut", "sugar", "banana leaves"]
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
            "pdf_pages": [72],
            "printed_page_numbers": [131],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "7:7 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0116",
        "title_mm": "သာကူမုန့်ဖက်ထုပ်",
        "title_en": "Pearl Sago Cone (Thargu Mont Phet Thoke)",
        "alternative_titles_mm": ["သာကူမုန့်ဖက်ထုပ်"],
        "alternative_titles_en": ["Steamed Sago Banana Leaf Parcels", "Thagu Mont Phet Htoke"],
        "description_mm": "သာကူစေ့အတွင်း အုန်းယိုဌာပနာထည့်၍ ငှက်ပျောဖက်ဖြင့် ကတော့ပုံထုပ်ကာ ရေနွေးငွေ့ဖြင့် မီးဖုတ်ပေါင်းထားသော မြန်မာ့ရိုးရာ သာကူမုန့်ဖက်ထုပ်ဖြစ်သည်။",
        "description_en": "Delicate steamed sago parcels filled with sweet caramelized coconut filling, enclosed in fragrant banana leaves folded into conical pyramid shapes and steamed until translucent.",
        "course": "dessert",
        "cuisine": "Myanmar",
        "servings": 20,
        "prep_time_minutes": None,
        "cooking_time_minutes": 20,
        "total_time_minutes": None,
        "difficulty": "medium",
        "ingredients": [
            {
                "ingredient_id": "I0156",
                "name_mm": "သာကူစေ့",
                "name_en": "Sago pearls",
                "original_name": "သာကူစေ့",
                "quantity": 50.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅၀ ကျပ်သား",
                "normalized_quantity": 816.5,
                "normalized_unit": "g",
                "preparation_note_mm": "ရေဆေးပြီး ရေစစ်ထားရန်",
                "preparation_note_en": "washed and drained"
            },
            {
                "ingredient_id": "I0007",
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
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီး",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခြစ်ပြီး ယိုထိုးရန်",
                "preparation_note_en": "grated for sweet filling"
            },
            {
                "ingredient_id": "I0021",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 30.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၃၀ ကျပ်သား",
                "normalized_quantity": 489.9,
                "normalized_unit": "g",
                "preparation_note_mm": "ယိုထိုးရန်",
                "preparation_note_en": "for sweet filling"
            },
            {
                "ingredient_id": "I0166",
                "name_mm": "ငှက်ပျောဖက်",
                "name_en": "Banana leaves",
                "original_name": "တောင်စွန် (သို့) ငှက်ပျောဖက်",
                "quantity": 20.0,
                "unit": "ရွက် (sheet)",
                "original_quantity_text": "အနားညီ ၈\" အရွယ် ၂၀ ရွက်",
                "normalized_quantity": 20.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "မီးပြပြီး ရေစိုအဝတ်ဖြင့် သုတ်ထားရန်",
                "preparation_note_en": "wilted over fire and wiped clean"
            }
        ],
        "instructions_mm": [
            "သာကူကို ရေဆေးပြီး ရေစစ်ထားကာ ငှက်ပျောဖက်ကို မီးပြ၍ စင်ကြယ်အောင် သုတ်ပြီး ရေစိုအဝတ်ဖြင့် ဖုံးထားပါ။",
            "အုန်းသီးနှင့် သကြားကို မီးအေးအေးတွင်တင်၍ အုန်းယို ထိုးထားပါ။",
            "ရေစစ်ထားသည့် သာကူကို ဆားထည့်နယ်ကာ အပုံ ၂၀ အညီအမျှရအောင် ပြုလုပ်ပါ။",
            "၈ လက်မအရွယ် ဖက်တစ်ရွက်ကိုယူကာ ကတော့ပုံ ပြုလုပ်ပြီး သာကူတစ်ပုံထဲမှ တစ်ဝက်ကို ပထမထည့်ကာ၊ ဒုတိယအနေဖြင့် အုန်းယိုထည့်ပြီး၊ နောက်ဆုံးတွင် ကျန်သာကူကို ထပ်ထည့်ပါ။",
            "ဖက်အနားစလေးဖက်ကို ကတော့ထိပ်ပိတ်ပုံနည်းအတိုင်း လုံအောင် ပိတ်ထုပ်ပါ။",
            "ပေါင်းချောင်ထဲသို့ အုန်းသီးမုန့်ဖက်ထုပ် ထည့်နည်းအတိုင်း ထည့်ပြီး ရေနွေးငွေ့ဖြင့် ပေါင်းပါ။",
            "ကျက်နပ်ရန်အတွက် ကြာမြင့်ချိန်မှာ မိနစ် ၂၀ ခန့်သာ ဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Rinse sago pearls and drain; gently wilt banana leaves over open flame, wipe clean, and keep under a moist towel.",
            "Simmer grated coconut and sugar over gentle heat until sticky and aromatic to make coconut preserve.",
            "Toss drained sago pearls with salt and divide into 20 equal portions.",
            "Roll an 8-inch banana leaf into a cone, spoon in half of one sago portion, add a core of coconut preserve, and top with the remaining sago.",
            "Fold the cone edges securely over the top to seal tightly into a pyramid.",
            "Stack firmly into a steamer basket with folds tucked underneath, exactly as done with coconut flour packets.",
            "Steam over rapid boiling water for about 20 minutes until the sago turns clear, glistening, and cooked through."
        ],
        "tags": {
            "dietary": ["vegetarian", "vegan", "gluten-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["sago pearls", "coconut", "sugar", "banana leaves"]
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
            "pdf_pages": [73],
            "printed_page_numbers": [132],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "7:7 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0117",
        "title_mm": "မုန့်ကျွဲသည်း",
        "title_en": "Brown Pudding with Shredded Coconut (Mont Kywe The)",
        "alternative_titles_mm": ["မုန့်ကျွဲသည်း"],
        "alternative_titles_en": ["Burmese Brown Rice Halwa", "Mont Kywe The"],
        "description_mm": "ဆန်ကြမ်းမုန့်နှစ်၊ ထန်းလျက်ရည်နှင့် ထုံးကျောက်တက်ရည်တို့ကို သမအောင်ရောမွှေကျိုပြီး ဗန်းထဲထည့်ကာ အုန်းသီးမျှင်ဖြူး၍ အအေးခံလှီးစိတ်သော ရှေးရိုးမြန်မာ့ မုန့်ကျွဲသည်းဖြစ်သည်။",
        "description_en": "Beloved traditional Myanmar firm brown rice pudding made from ground Ngasein rice batter cooked with rich jaggery syrup and limewater until glossy and set, sliced and blanketed with fresh coconut shreds.",
        "course": "dessert",
        "cuisine": "Myanmar",
        "servings": 20,
        "prep_time_minutes": 360,
        "cooking_time_minutes": None,
        "total_time_minutes": None,
        "difficulty": "medium",
        "ingredients": [
            {
                "ingredient_id": "I0001",
                "name_mm": "ဆန်",
                "name_en": "Rice",
                "original_name": "ဆန်ကြမ်း (ငစိန်)",
                "quantity": 2.5,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၂ ၁/၂ နို့ဆီဘူး",
                "normalized_quantity": 625.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ရေစိမ်ပြီး ကြိတ်စစ်ထားရန်",
                "preparation_note_en": "soaked and ground"
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ",
                "quantity": 3.5,
                "unit": "နို့ဆီဘူး (ml)",
                "original_quantity_text": "၃ ၁/၂ နို့ဆီဘူး",
                "normalized_quantity": 1050.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "မုန့်နှစ်ဖျော်ရန်",
                "preparation_note_en": "for dissolving dough"
            },
            {
                "ingredient_id": "I0054",
                "name_mm": "ထန်းလျက်",
                "name_en": "Jaggery",
                "original_name": "ထန်းလျက်",
                "quantity": 25.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၅ ကျပ်သား",
                "normalized_quantity": 408.3,
                "normalized_unit": "g",
                "preparation_note_mm": "ရေနှင့် ကျိုစစ်ထားရန်",
                "preparation_note_en": "simmered and strained"
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ",
                "quantity": 4.0,
                "unit": "နို့ဆီဘူး (ml)",
                "original_quantity_text": "၄ နို့ဆီဘူး",
                "normalized_quantity": 1200.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "ထန်းလျက်ကျိုရန်",
                "preparation_note_en": "for jaggery syrup"
            },
            {
                "ingredient_id": "I0165",
                "name_mm": "ထုံးကျောက်တက်ရည်",
                "name_en": "Limewater",
                "original_name": "ထုံးကျောက်တက်ရည်",
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
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 1.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ စပဇ",
                "normalized_quantity": 15.0,
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
                "unit": "စားပွဲဇွန်း (tbsp / ml)",
                "original_quantity_text": "၂ စပဇ",
                "normalized_quantity": 30.0,
                "normalized_unit": "ml",
                "preparation_note_mm": "မုန့်ဗန်းသုတ်ရန်",
                "preparation_note_en": "for greasing tray"
            },
            {
                "ingredient_id": "I0018",
                "name_mm": "အုန်းသီး",
                "name_en": "Coconut",
                "original_name": "အုန်းသီး",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အမျှင်ခြစ်ပြီး ဖြူးရန်",
                "preparation_note_en": "shredded for topping"
            }
        ],
        "instructions_mm": [
            "ဆန်ကို ရေဆေးပြီး တစ်ညရေစိမ်ကာ နောက်နေ့တွင် ကြိတ်ဆုံ၌ ကြိတ်ပြီး မုန့်အိတ်တွင် ထည့်၍ အလေးဖိ ရေစစ်ထားပါ။",
            "ထန်းလျက်ကို ရေ ၄ နို့ဆီဘူးဖြင့် ကျိုပြီး အမှိုက်စစ်ထားပါ။",
            "ရေစစ်ထားသော မုန့်နှစ်ကို ရေ ၃ ၁/၂ နို့ဆီဘူးဖြင့် ဖျော်ပါ။",
            "ဒယ်အိုးထဲသို့ မုန့်နှစ်ရည်၊ ဆား၊ ထန်းလျက်ရည်၊ ထုံးကျောက်တက်ရည်တို့ကို ရောဖျော်၍ မီးအသင့်အတင့်ဖြင့် သမအောင် မွှေကျိုပါ။",
            "ပျစ်ခဲစပြုလာလျှင် ဆီ ၂ စားပွဲဇွန်းသုတ်ထားသော မုန့်ဗန်းထဲသို့ လောင်းထည့်ပြီး မျက်နှာပြင်ညှိကာ အအေးခံထားပါ။",
            "အေးခဲသွားလျှင် နှစ်သက်သလို လေးထောင့်တုံးများ လှီးဖြတ်ကာ အုန်းသီးအမျှင်များ ဖြူး၍ တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Wash Ngasein rice, soak overnight, grind finely with water, place into a cloth bag, and press under heavy weight.",
            "Simmer jaggery in 4 tins of water until dissolved and strain through a cloth.",
            "Dilute the pressed rice dough with 3 1/2 tins of water into a smooth liquid.",
            "In a heavy wok or pot, combine diluted rice batter, salt, strained jaggery syrup, and limewater; cook over medium heat, stirring steadily.",
            "When the mixture thickens into a glossy, gelatinous mass, pour immediately into an oiled baking tray, smooth the top, and leave to cool and set.",
            "Once completely cold and firm, slice into diamond or square cakes, garnish generously with freshly shredded coconut, and serve."
        ],
        "tags": {
            "dietary": ["vegetarian", "vegan", "gluten-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["rice", "jaggery", "limewater", "coconut"]
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
            "pdf_pages": [73],
            "printed_page_numbers": [132],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "6:6 instruction parity verified.",
            "verified": True
        }
    }
]
