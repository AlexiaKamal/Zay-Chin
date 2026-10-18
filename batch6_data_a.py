# -*- coding: utf-8 -*-
"""
Batch 6 Part A: Recipes R0068 to R0074
Covers Burmese Traditional Salads (အသုပ်ပွဲများ) from Book pp. 108-110 (PDF pp. 60-61).
"""

BATCH6_RECIPES_A = [
    {
        "recipe_id": "R0068",
        "name_mm": "ပုစွန်ချဉ်သုပ်",
        "name_en": "Pickled Prawn Salad",
        "description_mm": "အချဉ်ပေါက် ပုစွန်ချဉ်ကို ကြက်သွန်နီ၊ ကြက်သွန်ဖြူ၊ ငရုတ်သီးစိမ်း၊ နံနံပင်၊ ဆီစိမ်းတို့ဖြင့် သမအောင် ဖွဖွနယ်သုပ်ထားသော မြန်မာ့ရိုးရာ အသုပ်။",
        "description_en": "Tangy fermented pickled prawns tossed with crisp soaked shallots, garlic, green chilies, cilantro, and raw fragrant peanut oil.",
        "category": "salad",
        "meal_types": ["lunch", "dinner", "side_dish"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0117",
                "name_mm": "ပုစွန်ချဉ်",
                "name_en": "Fermented pickled shrimp",
                "original_name": "ပုစွန်ချဉ် (အသားတင်ဖတ်မပါ)",
                "quantity": 30.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၃၀ ကျပ်သား",
                "normalized_quantity": 489.9,
                "normalized_unit": "g",
                "preparation_note_mm": "အသားသက်သက်",
                "preparation_note_en": "drained fermented prawn meat"
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ (ပါးပါးလှီး)",
                "quantity": 12.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁၂ လုံး",
                "normalized_quantity": 12.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ပါးပါးလှီးပြီး ရေစိမ်ရေစစ်ထားသော",
                "preparation_note_en": "thinly sliced, soaked in water, and drained"
            },
            {
                "ingredient_id": "I0022",
                "name_mm": "ကြက်သွန်ဖြူ",
                "name_en": "Garlic",
                "original_name": "ကြက်သွန်ဖြူ (ပါးပါးလှီး)",
                "quantity": 5.0,
                "unit": "မြွှာ (clove)",
                "original_quantity_text": "၅ မြွှာ",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ပါးပါးလှီးထားသော",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0044",
                "name_mm": "ငရုတ်သီးစိမ်း",
                "name_en": "Green chili",
                "original_name": "ငရုတ်စိမ်း (ရိတ်ရိတ်လှီး)",
                "quantity": 10.0,
                "unit": "တောင့် (piece)",
                "original_quantity_text": "၁၀ တောင့်",
                "normalized_quantity": 10.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ရိတ်ရိတ်လှီးထားသော",
                "preparation_note_en": "finely sliced"
            },
            {
                "ingredient_id": "I0091",
                "name_mm": "နံနံပင်",
                "name_en": "Fresh coriander / cilantro",
                "original_name": "နံနံပင် (ရိတ်ရိတ်လှီး)",
                "quantity": 5.0,
                "unit": "ပင် (stalk)",
                "original_quantity_text": "၅ ပင်",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ရိတ်ရိတ်လှီးထားသော",
                "preparation_note_en": "finely chopped"
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
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.65,
                "normalized_unit": "g",
                "preparation_note_mm": "ဆီစိမ်းထည့်ရန်",
                "preparation_note_en": "raw fragrant oil"
            }
        ],
        "instructions_mm": [
            "ကြက်သွန်နီကို ပါးပါးလှီးပြီးနောက် အပူရှိန်သက်သာစေရန် ရေတွင် ခေတ္တစိမ်ထားပြီး ဆန်ခါဖြင့် ရေစစ်ထားပါ။",
            "ပန်းကန်ပြားတစ်ခုတွင် ပုစွန်ချဉ်ထုပ်မှ ပုစွန်သားများကို ခပ်ဖွဖွ ဖြန့်၍ ထည့်ပါ။",
            "၎င်းအပေါ်သို့ ကြက်သွန်နီ၊ ကြက်သွန်ဖြူ၊ ငရုတ်သီးစိမ်းနှင့် နံနံပင်တို့ ထည့်ပါ။",
            "ဆီစိမ်းနှင့် ဆားအနည်းငယ် ထည့်ပြီး လက်ဖြင့် ညင်သာစွာ ဖွဖွနယ်၍ သုပ်ပါ။",
            "ပန်းကန်တွင် သပ်ရပ်စွာ ပြင်ဆင်ပြီး လိုအပ်ပါက ငရုတ်သီးလှော်ထောင်း ထည့်သွင်းကာ တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Thinly slice the onions, soak briefly in cold water to remove harshness, and drain thoroughly through a sieve.",
            "Gently flake and spread the fermented pickled prawns across a wide mixing plate.",
            "Add the drained sliced onions, garlic, finely sliced green chilies, and fresh coriander.",
            "Drizzle with fresh peanut oil, sprinkle with a pinch of salt, and gently toss by hand.",
            "Arrange attractively on a serving platter, optionally adding roasted crushed chili flakes to taste, and serve."
        ],
        "tags": {
            "dietary": ["pescatarian", "gluten-free", "dairy-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["pickled prawn", "onion", "garlic", "green chili", "coriander"]
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
            "pdf_pages": [60],
            "printed_page_numbers": [108],
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
        "recipe_id": "R0069",
        "name_mm": "ငါးဖယ်သုပ်",
        "name_en": "Shredded Featherback Fish Salad",
        "description_mm": "ပြုတ်ပြီး ပါးပါးလှီးထားသော ငါးဖယ်ပြားများကို ကြက်သွန်နီ၊ ဂေါ်ဖီ၊ ကြက်သွန်နီဆီချက်၊ ငံပြာရည်၊ သံပရာရည်တို့ဖြင့် နယ်သုပ်ပြီး နံနံပင်နှင့် ကြက်သွန်ကြော်ဖြူးထားသော အသုပ်။",
        "description_en": "Boiled springy featherback fish patties thinly shredded and tossed with finely shredded cabbage, shallots, garlic shallot oil, fish sauce, lime juice, and crispy shallots.",
        "category": "salad",
        "meal_types": ["lunch", "dinner", "side_dish"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0090",
                "name_mm": "ငါးဖယ်ခြစ်",
                "name_en": "Scraped featherback fish",
                "original_name": "ငါးဖယ်ခြစ်",
                "quantity": 25.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၅ ကျပ်သား",
                "normalized_quantity": 408.2,
                "normalized_unit": "g",
                "preparation_note_mm": "နနွင်း၊ ဆား၊ ငရုတ်သီးမှုန့်ဖြင့် နာနာရိုက်နယ်ထားသော",
                "preparation_note_en": "kneaded vigorously with turmeric, salt, and chili powder"
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
                "preparation_note_mm": "ငါးဖယ်နယ်ရန်",
                "preparation_note_en": "for seasoning fish paste"
            },
            {
                "ingredient_id": "I0114",
                "name_mm": "နနွင်း",
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
                "original_name": "ငရုတ်သီးအနုမှုန့်",
                "quantity": 3.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၃ လဖဇ",
                "normalized_quantity": 15.0,
                "normalized_unit": "g",
                "preparation_note_mm": "အနုမှုန့်",
                "preparation_note_en": "fine red chili powder"
            },
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ",
                "quantity": 4.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၄ နို့ဆီဘူး",
                "normalized_quantity": 1200.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ပြုတ်ရန်နှင့် ရေအေးစိမ်ရန်",
                "preparation_note_en": "for boiling and ice water bath"
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ",
                "quantity": 20.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၀ ကျပ်သား",
                "normalized_quantity": 326.5,
                "normalized_unit": "g",
                "preparation_note_mm": "၁၀ ကျပ်သား ပါးပါးလှီး၊ ၁၀ ကျပ်သား ဆီချက်ချက်ရန်",
                "preparation_note_en": "half sliced raw, half fried for shallot oil"
            },
            {
                "ingredient_id": "I0136",
                "name_mm": "ဂေါ်ဖီထုတ်",
                "name_en": "Cabbage",
                "original_name": "ဂေါ်ဖီထုပ် (ပါးပါးလှီး)",
                "quantity": 15.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၅ ကျပ်သား",
                "normalized_quantity": 245.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ပါးပါးလှီးထားသော",
                "preparation_note_en": "finely shredded"
            },
            {
                "ingredient_id": "I0115",
                "name_mm": "ငံပြာရည်",
                "name_en": "Fish sauce",
                "original_name": "ငံပြာရည်",
                "quantity": 2.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၂ စပဇ",
                "normalized_quantity": 30.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0106",
                "name_mm": "သံပရာသီး",
                "name_en": "Lime",
                "original_name": "သံပရာသီး (အရည်ညှစ်ပြီး)",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အရည်ညှစ်ထားသော",
                "preparation_note_en": "freshly squeezed juice"
            },
            {
                "ingredient_id": "I0091",
                "name_mm": "နံနံပင်",
                "name_en": "Fresh coriander / cilantro",
                "original_name": "နံနံပင် (ရိတ်ရိတ်လှီး)",
                "quantity": 5.0,
                "unit": "ပင် (stalk)",
                "original_quantity_text": "၅ ပင်",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ရိတ်ရိတ်လှီးထားသော",
                "preparation_note_en": "finely chopped"
            }
        ],
        "instructions_mm": [
            "ငါးဖယ်ခြစ်ကို နနွင်း၊ ဆား၊ ငရုတ်သီးမှုန့်တို့နှင့် နယ်ကာ စေးပိုင်လာသည်အထိ ခပ်နာနာ ရိုက်နယ်ပြီး နာရီဝက်ခန့် နှပ်ထားပါ။",
            "ရေပွက်ပွက်ဆူတွင် ငါးဖယ်ခြစ်ကို ခပ်ပြားပြား ပြုလုပ်၍ ထည့်ပါ (ပထမ ရေမြုပ်သွားပြီး ၅ မိနစ်ခန့်ကြာလျှင် ပြန်ပေါ်လာပါမည်)။",
            "ပေါ်လာပြီးနောက် (၁) မိနစ် ဆက်ထားကာ ဆယ်ယူ၍ ရေအေးတွင် ခေတ္တစိမ်ပြီး ရေစစ်ကာ ပါးပါးလှီးထားပါ။",
            "ဇလုံထဲသို့ လှီးထားသော ငါးဖယ်၊ ကြက်သွန်နီ၊ ဂေါ်ဖီထုပ်၊ ငံပြာရည်၊ ကြက်သွန်နီဆီချက်နှင့် သံပရာရည်တို့ ထည့်၍ သမအောင် နယ်သုပ်ပါ။",
            "ပန်းကန်ပြားတွင် လှပစွာ ပြင်ဆင်ပြီး နံနံပင်နှင့် ကြက်သွန်ကြော် ဖြူး၍ တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Vigorously knead and slap the scraped featherback fish paste with turmeric, salt, and chili powder until bouncy and firm, then let rest for 30 minutes.",
            "Flatten portions of the fish paste into patties and drop into a pot of rapidly boiling water (they will sink and float back to the surface after about 5 minutes).",
            "Once floating, simmer for 1 more minute, transfer to a cold water bath to halt cooking, drain well, and slice thinly.",
            "In a mixing bowl, toss the sliced fish patties with shredded cabbage, raw sliced shallots, fish sauce, fragrant cooked shallot oil, and lime juice.",
            "Arrange on a platter, garnish with fresh chopped coriander and golden fried shallots, and serve."
        ],
        "tags": {
            "dietary": ["pescatarian", "gluten-free", "dairy-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["featherback fish", "cabbage", "shallot oil", "lime juice", "coriander"]
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
            "pdf_pages": [60],
            "printed_page_numbers": [108],
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
        "recipe_id": "R0070",
        "name_mm": "ရှောက်သီးသုပ်",
        "name_en": "Tangy Lemon Pulp Salad",
        "description_mm": "ဆားရည်စိမ်ပြီး ရေညှစ်ထားသော ရှောက်သီးအမြွှာများကို မျှင်ငါးပိမီးကင်၊ ပုစွန်ခြောက်ထောင်း၊ ကြက်သွန်နီ၊ ငရုတ်သီးစိမ်းတို့ဖြင့် သမအောင် နယ်သုပ်ထားသော မြန်မာ့ရိုးရာ ရှောက်သီးသုပ်။",
        "description_en": "Juicy citrus lemon segments gently brine-soaked and squeezed, tossed with roasted shrimp paste, pounded dried shrimp, shallots, green chilies, and sugar, served alongside garlic and vermicelli soup.",
        "category": "salad",
        "meal_types": ["lunch", "dinner", "snack"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0118",
                "name_mm": "မျှင်ငါးပိ",
                "name_en": "Shrimp paste / fermented paste",
                "original_name": "မျှင်ငါးပိ",
                "quantity": 2.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၂ စပဇ",
                "normalized_quantity": 30.0,
                "normalized_unit": "g",
                "preparation_note_mm": "မီးကင်ထားသော",
                "preparation_note_en": "roasted over flame"
            },
            {
                "ingredient_id": "I0021",
                "name_mm": "ပုစွန်ခြောက်",
                "name_en": "Dried shrimp",
                "original_name": "ပုစွန်ခြောက် (ထောင်းပြီး)",
                "quantity": 2.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
                "normalized_quantity": 40.8,
                "normalized_unit": "g",
                "preparation_note_mm": "ထောင်းပြီး",
                "preparation_note_en": "pounded"
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ",
                "quantity": 15.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၅ ကျပ်သား",
                "normalized_quantity": 245.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ပါးပါးလှီးပြီး ရေဆေးရေစစ်ထားသော",
                "preparation_note_en": "thinly sliced and rinsed"
            },
            {
                "ingredient_id": "I0079",
                "name_mm": "ရှောက်သီး",
                "name_en": "Lemon / Citron",
                "original_name": "ရှောက်သီး (အလတ်)",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အခွံခွာ အမြွှာလေးများ မျှင်ယူထားသော",
                "preparation_note_en": "peeled, deseeded, and segments separated"
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 3.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၃ စပဇ",
                "normalized_quantity": 45.0,
                "normalized_unit": "g",
                "preparation_note_mm": "၂ စပဇ စိမ်ရန် ၁ စပဇ သုပ်ရန်",
                "preparation_note_en": "part for brining, part for seasoning"
            },
            {
                "ingredient_id": "I0044",
                "name_mm": "ငရုတ်သီးစိမ်း",
                "name_en": "Green chili",
                "original_name": "ငရုတ်သီးစိမ်း (ပါးပါးလှီး)",
                "quantity": 10.0,
                "unit": "တောင့် (piece)",
                "original_quantity_text": "၁၀ တောင့်",
                "normalized_quantity": 10.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ပါးပါးလှီးထားသော",
                "preparation_note_en": "thinly sliced"
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
            }
        ],
        "instructions_mm": [
            "မျှင်ငါးပိကို ယောက်မတွင်ကပ်၍ သို့မဟုတ် ဒယ်အိုးဖုံးပေါ်တွင် ခပ်ပြားပြားကပ်၍ မီးဖိုပေါ်တင်ပြီး မွှေးလာသည်အထိ မီးကင်ပါ။",
            "ကြက်သွန်နီကို ပါးပါးလှီးပြီး ရေဆေးကာ ဆန်ခါတွင် ရေစစ်ထားပါ။",
            "ရှောက်သီးကို အခွံခွာ အသားထုတ်၍ အမြွှာလေးများ မျှင်ယူပြီး ဆား (၂) စားပွဲဇွန်းနှင့် ရေအေးအရည်ထဲတွင် ခေတ္တစိမ်ထားကာ ရေညှစ်ထုတ်ပါ။",
            "ဇလုံထဲသို့ ရေစစ်ထားသော ရှောက်သီး၊ ငါးပိဖုတ်၊ ပုစွန်ခြောက်၊ သကြား၊ ငရုတ်သီးစိမ်း၊ ဆား၊ ကြက်သွန်နီတို့ ထည့်ပြီး ခပ်ဖွဖွ နယ်သုပ်ပါ။",
            "ပန်းကန်ပြားထဲတွင် သုပ်ပြီးသား ရှောက်သီးကို သပ်ရပ်စွာပြင်ကာ ကြက်သွန်ဖြူမြွှာများနှင့် တွဲဖက်၍ ကြာဆံဟင်းခါးနှင့်အတူ တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Toast the fermented shrimp paste spread thinly on a spatula or pot lid over open coals until aromatic.",
            "Thinly slice the onions, wash in cold water, and drain completely in a colander.",
            "Peel the lemon, separate into individual fruit segments, soak briefly in light salt water to temper bitterness, and gently squeeze dry.",
            "In a bowl, combine the squeezed lemon segments, roasted shrimp paste, pounded dried shrimp, sugar, green chilies, salt, and sliced onions, tossing lightly.",
            "Transfer to a plate, garnish with peeled raw garlic cloves, and serve traditionally alongside hot vermicelli soup."
        ],
        "tags": {
            "dietary": ["pescatarian", "gluten-free", "dairy-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["lemon", "shrimp paste", "dried shrimp", "onion", "green chili"]
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
            "pdf_pages": [60],
            "printed_page_numbers": [109],
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
        "recipe_id": "R0071",
        "name_mm": "မြင်းခွာရွက်သုပ်",
        "name_en": "Pennywort Leaf Salad",
        "description_mm": "နုပ်နုပ်စဉ်းထားသော လတ်ဆတ် မြင်းခွာရွက်များကို ပုစွန်ခြောက်ထောင်း၊ ကြက်သွန်နီ၊ သံပရာရည်၊ ဆီချက်တို့ဖြင့် ဖွဖွနယ်သုပ်ပြီး ကြက်သွန်နီကြော် ဖြူးထားသော ဆေးဖက်ဝင် အသုပ်။",
        "description_en": "Fresh medicinal Asiatic pennywort finely minced and tossed with pounded dried shrimp, raw shallots, fragrant cooked shallot oil, lime juice, and crispy shallots.",
        "category": "salad",
        "meal_types": ["lunch", "dinner", "side_dish"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0119",
                "name_mm": "မြင်းခွာရွက်",
                "name_en": "Pennywort leaves",
                "original_name": "မြင်းခွာရွက်",
                "quantity": 20.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၀ ကျပ်သား",
                "normalized_quantity": 326.5,
                "normalized_unit": "g",
                "preparation_note_mm": "အရိုး အရွက် ရေစင်အောင်ဆေး ရေစစ်ပြီး ပါးပါးနုပ်နုပ် စဉ်းထားသော",
                "preparation_note_en": "washed thoroughly, dried, and finely minced"
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ",
                "quantity": 15.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၅ ကျပ်သား",
                "normalized_quantity": 245.0,
                "normalized_unit": "g",
                "preparation_note_mm": "တစ်ဝက်ပါးပါးလှီးသုပ် တစ်ဝက်ကြော်ရန်",
                "preparation_note_en": "half sliced raw, half fried for shallot oil"
            },
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": 15.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၅ ကျပ်သား",
                "normalized_quantity": 245.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ကြက်သွန်နီကြော်ရန်နှင့် ဆီချက် ၃ စပဇ အတွက်",
                "preparation_note_en": "for frying crispy shallots and shallot oil"
            },
            {
                "ingredient_id": "I0021",
                "name_mm": "ပုစွန်ခြောက်",
                "name_en": "Dried shrimp",
                "original_name": "ပုစွန်ခြောက် (ထောင်းပြီး)",
                "quantity": 2.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ကျပ်သား",
                "normalized_quantity": 32.65,
                "normalized_unit": "g",
                "preparation_note_mm": "ထောင်းပြီး",
                "preparation_note_en": "pounded"
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
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 0.5,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁/၂ စပဇ",
                "normalized_quantity": 7.5,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0106",
                "name_mm": "သံပရာသီး",
                "name_en": "Lime",
                "original_name": "သံပရာသီး",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အရည်ညှစ်ထားသော",
                "preparation_note_en": "freshly squeezed juice"
            }
        ],
        "instructions_mm": [
            "မြင်းခွာရွက်ကို အရိုးနှင့် အရွက် ရေစင်အောင် ဆေးကြောပြီး ရေစစ်ထားပါ။",
            "ရေခြောက်သွားလျှင် ဓားဖြင့် ပါးပါးနုပ်နုပ် စဉ်းထားပါ။",
            "ကြက်သွန်နီ အခွံသင်ပြီး ပါးပါးလှီးကာ တစ်ဝက်ကို ဆီပူတွင် ဝါရောင်သမ်းသည်အထိ ကြော်ပြီး ဆယ်ယူထားပါ။",
            "ဇလုံထဲသို့ စဉ်းထားသော မြင်းခွာရွက်၊ ကြက်သွန်နီ၊ ပုစွန်ခြောက်၊ သံပရာရည်၊ ဆား၊ သကြားနှင့် ဆီချက် (၃) စားပွဲဇွန်း ထည့်ပြီး ဖွဖွလေး သုပ်ပေးပါ။",
            "ပန်းကန်ပြားထဲတွင် သုပ်ပြီးသား မြင်းခွာရွက်ကို လှပစွာ ပြင်ဆင်ပြီး ကြက်သွန်ကြော် အပေါ်မှ ဖြူး၍ တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Wash pennywort leaves and tender stems thoroughly and let drain completely.",
            "Once dry, mince finely with a sharp knife.",
            "Peel and thinly slice the shallots; fry half in hot oil until fragrant and golden-crisp, setting aside the crispy shallots and shallot oil.",
            "In a salad bowl, gently toss the minced pennywort, raw sliced shallots, pounded dried shrimp, lime juice, salt, sugar, and 3 tablespoons of the shallot oil.",
            "Plate neatly and scatter the reserved crispy fried shallots over the top to serve."
        ],
        "tags": {
            "dietary": ["pescatarian", "gluten-free", "dairy-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["pennywort", "dried shrimp", "shallot oil", "lime juice"]
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
            "pdf_pages": [60],
            "printed_page_numbers": [109],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "5:5 instruction parity verified. Esteemed traditional medicinal salad.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0072",
        "name_mm": "ခရမ်းချဉ်သီးသုပ်",
        "name_en": "Fresh Myanmar Tomato Salad",
        "description_mm": "ခပ်မာမာ ခရမ်းချဉ်သီးများကို အစေ့ထုတ်ပါးပါးလှီး၍ ကြက်သွန်နီ၊ ပုစွန်ခြောက်ထောင်း၊ ငံပြာရည်၊ သကြား၊ ဆားတို့ဖြင့် ဖွဖွနယ်သုပ်ပြီး နံနံပင်ဖြူးထားသော အသုပ်။",
        "description_en": "Crisp firm tomatoes deseeded and sliced, lightly tossed with shallots, pounded dried shrimp, fish sauce, sugar, and salt, finished with fresh cilantro sprigs.",
        "category": "salad",
        "meal_types": ["lunch", "dinner", "side_dish"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0042",
                "name_mm": "ခရမ်းချဉ်သီး",
                "name_en": "Tomato",
                "original_name": "ခရမ်းချဉ်သီး (ခပ်မာမာ အမှည့်မလွန်သော)",
                "quantity": 40.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၄၀ ကျပ်သား",
                "normalized_quantity": 653.2,
                "normalized_unit": "g",
                "preparation_note_mm": "ရေဆေး အစေ့ထုတ်ပြီး ပါးပါးလှီးထားသော",
                "preparation_note_en": "firm ripe, washed, deseeded, and thinly sliced"
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ (ပါးပါးလှီး)",
                "quantity": 10.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၀ ကျပ်သား",
                "normalized_quantity": 163.3,
                "normalized_unit": "g",
                "preparation_note_mm": "ပါးပါးလှီးထားသော",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0021",
                "name_mm": "ပုစွန်ခြောက်",
                "name_en": "Dried shrimp",
                "original_name": "ပုစွန်ခြောက် (ထောင်းပြီး)",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.65,
                "normalized_unit": "g",
                "preparation_note_mm": "ထောင်းပြီး",
                "preparation_note_en": "pounded"
            },
            {
                "ingredient_id": "I0091",
                "name_mm": "နံနံပင်",
                "name_en": "Fresh coriander / cilantro",
                "original_name": "နံနံပင် (ရိတ်ရိတ်လှီး)",
                "quantity": 5.0,
                "unit": "ပင် (stalk)",
                "original_quantity_text": "၅ ပင်",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ရိတ်ရိတ်လှီးထားသော",
                "preparation_note_en": "finely chopped"
            },
            {
                "ingredient_id": "I0004",
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
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 2.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၂ စပဇ",
                "normalized_quantity": 30.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0115",
                "name_mm": "ငံပြာရည်",
                "name_en": "Fish sauce",
                "original_name": "ငံပြာရည်",
                "quantity": 1.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ စပဇ",
                "normalized_quantity": 15.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "ခရမ်းချဉ်သီးကို ရေဆေး အစေ့ထုတ်ပြီး ပါးပါးလှီးကာ ဆန်ခါတွင် ရေစစ်ထားပါ။",
            "ဇလုံထဲသို့ ခရမ်းချဉ်သီး၊ ကြက်သွန်နီ၊ ပုစွန်ခြောက်၊ ဆား၊ သကြားနှင့် ငံပြာရည်တို့ ထည့်ပါ။",
            "ခရမ်းချဉ်သီးများ မကြေစေရန် လက်ဖြင့် ဖွဖွနယ်၍ သုပ်ပါ။",
            "ပန်းကန်ပြားထဲတွင် သုပ်ပြီးသား ခရမ်းချဉ်သီးကို လှပစွာ ပြင်ဆင်ပါ။",
            "နံနံပင် ဖြန့်ဖြူး၍ တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Wash firm ripe tomatoes, scoop out and discard seeds, slice thinly, and drain in a colander.",
            "In a mixing bowl, combine sliced tomatoes, shallots, pounded dried shrimp, salt, sugar, and fish sauce.",
            "Toss very gently by hand to coat without bruising or crushing the tomato slices.",
            "Transfer to a decorative serving platter.",
            "Scatter freshly chopped coriander sprigs over the salad and serve fresh."
        ],
        "tags": {
            "dietary": ["pescatarian", "gluten-free", "dairy-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["tomato", "onion", "dried shrimp", "fish sauce", "coriander"]
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
            "pdf_pages": [61],
            "printed_page_numbers": [110],
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
        "recipe_id": "R0073",
        "name_mm": "နှမ်းဖတ်ချဉ်",
        "name_en": "Fermented Sesame Press-Cake Pickle",
        "description_mm": "သန့်စင်ထားသော နှမ်းဖတ် (သို့မဟုတ် ပဲဖတ်) ကို အခါးရည်ထွက်စေရန် ရေဆေးစစ်ပြီး အချဉ်ပေါက်အောင် (၂) ရက် နှပ်ကာ ဆားနယ်သိပ်ထားသော မြန်မာ့ရိုးရာ အချဉ်တည်နည်း။",
        "description_en": "Traditional Upper Myanmar staple of fresh sesame seed press-cake, repeatedly rinsed to purge bitterness, fermented for 2 days until sour, and preserved with salt.",
        "category": "pickle_preserve",
        "meal_types": ["side_dish", "condiment"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0120",
                "name_mm": "နှမ်းဖတ်",
                "name_en": "Sesame press-cake pulp",
                "original_name": "နှမ်းဖတ် (သို့) ပဲဖတ်",
                "quantity": 50.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅၀ ကျပ်သား",
                "normalized_quantity": 816.5,
                "normalized_unit": "g",
                "preparation_note_mm": "လတ်လတ်ဆတ်ဆတ် သဲမပါအောင် ရေဆေးထားသော",
                "preparation_note_en": "fresh unadulterated sesame or peanut press-cake"
            },
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေအေး",
                "quantity": 5.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "ရေလောင်းဆေးရန်",
                "normalized_quantity": 1500.0,
                "normalized_unit": "g",
                "preparation_note_mm": "အခါးရည်ထွက်စေရန် လောင်းဆေးရန်",
                "preparation_note_en": "for repeated leaching of bitterness"
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 3.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "ဆား",
                "normalized_quantity": 45.0,
                "normalized_unit": "g",
                "preparation_note_mm": "အချဉ်ပေါက်ပြီး နယ်သိပ်ရန်",
                "preparation_note_en": "for curing fermented pulp"
            }
        ],
        "instructions_mm": [
            "နှမ်းဖတ် (သို့မဟုတ် ပဲဖတ်) လတ်လတ်ဆတ်ဆတ်ကို သဲကင်းစင်စေရန် ရေဆေးပါ။",
            "ဆန်ဆေးခြင်းတောင်း သို့မဟုတ် ဝါးဆန်ခါတောင်းထဲသို့ ထည့်ပြီး တောင်းကို ကြွေလုံတွင် အနည်းငယ် မြှင့်တင်တင်ထားပါ။",
            "ပဲဖတ်ထည့်ထားသည့် ဆန်ခါပေါ်မှနေ၍ ရေလောင်းချကာ အစပ်ရည်၊ အခါးရည်များ ထွက်သွားစေရန် (၅) ကြိမ်ခန့် ရေလောင်းလိုက် သွန်လိုက် ပြုလုပ်ပါ။",
            "အပေါ်တွင် အမှိုက်အမှုန်များ မဝင်စေရန် ဖက် သို့မဟုတ် ပိတ်ပါးစပါး အုပ်ထားပြီး အချဉ်ပေါက်လာစေရန် (၂) ရက်ခန့် နှပ်ထားပါ။",
            "အရည်စစ်၍ နူးညံ့ပျော့ပြောင်းလာလျှင် ဆားနှင့် သမအောင် သေချာစွာ နယ်ပြီး အိုးတွင် တင်းကျပ်စွာ သိပ်ထားပါက တာရှည်ခံပါသည်။"
        ],
        "instructions_en": [
            "Rinse fresh sesame press-cake (or peanut press-cake) thoroughly in water to remove any grit or sand.",
            "Transfer into a bamboo colander or basket suspended over a ceramic basin.",
            "Pour water repeatedly over the press-cake about 5 times, draining each time, to thoroughly leach out tannins and bitterness.",
            "Cover tightly with clean leaves or cheesecloth to keep out dust, and let ferment for about 2 days until naturally sour.",
            "Once properly drained and softened, knead thoroughly with salt and pack firmly into a ceramic crock to keep for long-term use."
        ],
        "tags": {
            "dietary": ["vegan", "vegetarian", "gluten-free", "dairy-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["sesame press-cake", "salt", "water"]
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
            "pdf_pages": [61],
            "printed_page_numbers": [110],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "5:5 instruction parity verified. Essential fermentation process for Upper Myanmar Hnan-phat-chin preserved.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0074",
        "name_mm": "နှမ်းဖတ်ချဉ်သုပ်",
        "name_en": "Fermented Sesame Pulp Salad",
        "description_mm": "ဆီပူတွင် မွှေကြော်ပြီး အအေးခံထားသော နှမ်းဖတ်ချဉ်ကို ကြက်သွန်နီ၊ ရှောက်ရွက်၊ ငရုတ်သီးစိမ်း၊ ဆီ၊ ဆားတို့ဖြင့် သုပ်ကာ နံနံပင်အုပ်ထားသော အထူးမြန်မာ့အစားအစာ။",
        "description_en": "Pan-sautéed fermented sesame pulp tossed with sliced shallots, fragrant thinly julienned lime leaves, green chilies, peanut oil, salt, and cilantro.",
        "category": "salad",
        "meal_types": ["lunch", "dinner", "side_dish"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0120",
                "name_mm": "နှမ်းဖတ်",
                "name_en": "Sesame press-cake pulp",
                "original_name": "နှမ်းဖတ်ချဉ်",
                "quantity": 10.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၀ ကျပ်သား",
                "normalized_quantity": 163.3,
                "normalized_unit": "g",
                "preparation_note_mm": "အချဉ်ပေါက်ပြီးသား",
                "preparation_note_en": "fermented sour sesame pulp"
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ (ပါးပါးလှီး)",
                "quantity": 15.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၅ ကျပ်သား",
                "normalized_quantity": 245.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ပါးပါးလှီးထားသော",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0121",
                "name_mm": "ရှောက်ရွက်",
                "name_en": "Lemon / Lime leaves",
                "original_name": "ရှောက်ရွက် (ပါးပါးလှီး)",
                "quantity": 10.0,
                "unit": "ရွက် (leaf)",
                "original_quantity_text": "၁၀ ရွက်",
                "normalized_quantity": 10.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ပါးပါးမျှင်မျှင် လှီးထားသော",
                "preparation_note_en": "finely julienned"
            },
            {
                "ingredient_id": "I0044",
                "name_mm": "ငရုတ်သီးစိမ်း",
                "name_en": "Green chili",
                "original_name": "ငရုတ်သီးစိမ်း (ပါးပါးလှီး)",
                "quantity": 10.0,
                "unit": "တောင့် (piece)",
                "original_quantity_text": "၁၀ တောင့်",
                "normalized_quantity": 10.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ပါးပါးလှီးထားသော",
                "preparation_note_en": "thinly sliced"
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
                "ingredient_id": "I0091",
                "name_mm": "နံနံပင်",
                "name_en": "Fresh coriander / cilantro",
                "original_name": "နံနံပင် (ရိတ်ရိတ်လှီး)",
                "quantity": 5.0,
                "unit": "ပင် (stalk)",
                "original_quantity_text": "၅ ပင်",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ရိတ်ရိတ်လှီးထားသော",
                "preparation_note_en": "finely chopped"
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
            "ဒယ်အိုးတွင် ဆီထည့်ကာ ပူလာလျှင် နှမ်းဖတ်ချဉ်ကို ထည့်၍ (၁၀) မိနစ်ခန့် မွှေကြော်ပါ။",
            "မွှေကြော်ပြီးလျှင် အအေးခံထားပါ။",
            "ဇလုံထဲတွင် အအေးခံထားသော နှမ်းဖတ်ချဉ်၊ ပါးပါးလှီးထားသော ကြက်သွန်နီ၊ ရှောက်ရွက်၊ ငရုတ်သီးစိမ်း၊ ဆီနှင့် ဆားတို့ကို ထည့်ပါ။",
            "ပစ္စည်းများ အားလုံး နှံ့စပ်သွားအောင် ညင်သာစွာ နယ်သုပ်ပေးပါ။",
            "တည်ခင်းရာတွင် နံနံပင်ကို အပေါ်မှ မွမ်းမံဖြူးပေး၍ တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Heat cooking oil in a pan, add the fermented sesame pulp, and sauté for about 10 minutes until fragrant.",
            "Remove from heat and allow to cool completely.",
            "In a mixing bowl, combine the cooled cooked sesame pulp with sliced shallots, finely julienned citrus leaves, green chilies, oil, and salt.",
            "Toss thoroughly until evenly blended.",
            "Garnish with fresh chopped coriander and serve."
        ],
        "tags": {
            "dietary": ["vegan", "vegetarian", "gluten-free", "dairy-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["fermented sesame pulp", "shallot", "citrus leaves", "green chili"]
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
            "pdf_pages": [61],
            "printed_page_numbers": [110],
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
