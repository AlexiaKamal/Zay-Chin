# -*- coding: utf-8 -*-
"""
Batch 4 Part B: Recipes R0032 - R0042 (Mutton Cutlets, Beef dishes, and Pork dishes)
"""

recipes_b = [
    # R0032: ဆိတ်သားကတ်တလက် (Mutton Cutlets)
    {
        "recipe_id": "R0032",
        "name_mm": "ဆိတ်သားကတ်တလက်",
        "name_en": "Mutton Cutlets",
        "description_mm": None,
        "description_en": None,
        "category": "Mutton dishes",
        "meal_types": ["lunch", "dinner", "snack"],
        "ingredients": [
            {"ingredient_id": "I0068", "name_mm": "ဆိတ်သား", "name_en": "Mutton", "original_name": "ဆိတ်သား (စဉ်းပြီး)", "quantity": 75.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၇၅ ကျပ်သား", "normalized_quantity": 1224.7, "normalized_unit": "g", "preparation_note_mm": "စဉ်းပြီး", "preparation_note_en": "minced"},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "original_name": "ကြက်သွန်နီ (နုပ်နုပ်စဉ်း)", "quantity": 3.0, "unit": "လုံး (piece)", "original_quantity_text": "၃ လုံး", "normalized_quantity": 3.0, "normalized_unit": "piece", "preparation_note_mm": "နုပ်နုပ်စဉ်း", "preparation_note_en": "finely minced"},
            {"ingredient_id": "I0014", "name_mm": "ကြက်သွန်ဖြူ", "name_en": "Garlic", "original_name": "ကြက်သွန်ဖြူ (နုပ်နုပ်စဉ်း)", "quantity": 2.0, "unit": "လုံး (piece)", "original_quantity_text": "၂ လုံး", "normalized_quantity": 2.0, "normalized_unit": "piece", "preparation_note_mm": "နုပ်နုပ်စဉ်း", "preparation_note_en": "finely minced"},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "original_name": "ရေ", "quantity": 0.25, "unit": "နို့ဆီဘူး (g)", "original_quantity_text": "၁/၄ နို့ဆီဘူး", "normalized_quantity": 75.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0074", "name_mm": "ပေါင်မုန့်", "name_en": "Bread", "original_name": "ပေါင်မုန့်ချပ်", "quantity": 4.0, "unit": "ချပ် (piece)", "original_quantity_text": "၄ ချပ်", "normalized_quantity": 4.0, "normalized_unit": "piece", "preparation_note_mm": "ရေစွတ် စုပ်ခြေ", "preparation_note_en": "soaked and squeezed dry"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 1.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁ လဖဇ", "normalized_quantity": 5.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0044", "name_mm": "ငရုတ်သီးစိမ်း", "name_en": "Green chili", "original_name": "ငရုတ်သီးစိမ်း (နုပ်နုပ်စဉ်း)", "quantity": 5.0, "unit": "တောင့် (piece)", "original_quantity_text": "၅ တောင့်", "normalized_quantity": 5.0, "normalized_unit": "piece", "preparation_note_mm": "နုပ်နုပ်စဉ်း", "preparation_note_en": "finely minced"},
            {"ingredient_id": "I0031", "name_mm": "နံနံပင်", "name_en": "Coriander", "original_name": "နံနံပင် (နုပ်နုပ်စဉ်း)", "quantity": 2.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၂ လဖဇ", "normalized_quantity": 10.0, "normalized_unit": "g", "preparation_note_mm": "နုပ်နုပ်စဉ်း", "preparation_note_en": "finely minced"},
            {"ingredient_id": "I0026", "name_mm": "ကြက်ဥ", "name_en": "Chicken egg", "original_name": "ကြက်ဥ", "quantity": 2.0, "unit": "လုံး (piece)", "original_quantity_text": "၂ လုံး", "normalized_quantity": 2.0, "normalized_unit": "piece", "preparation_note_mm": "ခေါက်မွှေရန်", "preparation_note_en": "for egg wash"},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "original_name": "ရေအေး", "quantity": 0.5, "unit": "နို့ဆီဘူး (g)", "original_quantity_text": "၁/၂ နို့ဆီဘူး", "normalized_quantity": 150.0, "normalized_unit": "g", "preparation_note_mm": "ရေအေး", "preparation_note_en": "cold water"},
            {"ingredient_id": "I0071", "name_mm": "ဂီးထောပတ်", "name_en": "Ghee", "original_name": "ကြော်ရန်အတွက် ဂီးထောပတ်လိုအပ်သရွေ့", "quantity": None, "unit": "လိုအပ်သရွေ့ (as needed)", "original_quantity_text": "ကြော်ရန်အတွက် ဂီးထောပတ်လိုအပ်သရွေ့", "normalized_quantity": None, "normalized_unit": "g", "preparation_note_mm": "ကြော်ရန်အတွက်", "preparation_note_en": "for frying"},
            {"ingredient_id": "I0075", "name_mm": "ပေါင်မုန့်ကြွပ်မှုန့်", "name_en": "Breadcrumbs", "original_name": "ပေါင်မုန့်ကြွပ်မှုန့် အသားဖုံးအုပ်ရန်လိုအပ်သရွေ့", "quantity": None, "unit": "လိုအပ်သရွေ့ (as needed)", "original_quantity_text": "ပေါင်မုန့်ကြွပ်မှုန့် အသားဖုံးအုပ်ရန်လိုအပ်သရွေ့", "normalized_quantity": None, "normalized_unit": "g", "preparation_note_mm": "အသားဖုံးအုပ်ရန်", "preparation_note_en": "for breading"}
        ],
        "servings": 10,
        "preparation_time_minutes": 25,
        "cooking_time_minutes": 20,
        "instructions_mm": [
            "ဆိတ်သားစဉ်းကောကို ကြက်သွန်နီ၊ ကြက်သွန်ဖြူနှင့် ရေတို့ဖြင့် အသားများနူးပြီး အရည်ခန်းခြောက်သည်အထိ ချက်ပါ။",
            "ပေါင်မုန့်ချပ်များကို ရေစွတ်ပြီး စုပ်ခြေကာ ရောစပ်မွှေပါ။ ဆား၊ ငရုတ်သီးစိမ်း၊ နံနံပင်တို့ပါ ရောစပ်ပါ။",
            "စဉ်းကောအသားကို ဘဲဥပုံစံလုပ်ပြီး ရေနှင့် ကြက်ဥခေါက်မွှေတွင်နှစ်ကာ ပေါင်မုန့်ခြောက်အမှုန့် ဖုံးအုပ်ပါ။",
            "ဂီးထောပတ်ပူပူတွင် ရွှေညိုရောင်သမ်းသည်အထိကြော်ပြီးလျှင် တည်ခင်း၍ရပြီဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Simmer the minced mutton with onion, garlic, and water until tender and all liquid evaporates completely.",
            "Moisten bread slices with water, squeeze dry, crumble into the meat, and mix thoroughly with salt, green chilies, and coriander.",
            "Shape the mixture into oval cutlet patties, dip into egg wash diluted with water, and coat evenly with breadcrumbs.",
            "Deep-fry in hot ghee until golden brown and crisp, then drain and serve."
        ],
        "tags": {"dietary": [], "seasonal": ["all-season"], "festival": [], "main_ingredients": ["mutton", "bread", "egg", "ghee"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [51], "printed_page_numbers": [90], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 90 (bottom). Ghee-fried breaded cutlets.", "verified": True}
    },

    # R0033: ပဲ၊ အာလူးနှင့် အမဲသားကီးမား (Kheema with Potatoes and Peas)
    {
        "recipe_id": "R0033",
        "name_mm": "ပဲ၊ အာလူးနှင့် အမဲသားကီးမား",
        "name_en": "Kheema with Potatoes and Peas",
        "description_mm": None,
        "description_en": None,
        "category": "Beef dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "original_name": "ဆီ", "quantity": 10.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၁၀ စပဇ", "normalized_quantity": 150.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "original_name": "ကြက်သွန်နီ (လှီးပြီး)", "quantity": 5.0, "unit": "လုံး (piece)", "original_quantity_text": "၅ လုံး", "normalized_quantity": 5.0, "normalized_unit": "piece", "preparation_note_mm": "လှီးပြီး", "preparation_note_en": "sliced"},
            {"ingredient_id": "I0054", "name_mm": "နံနံစေ့", "name_en": "Coriander seeds", "original_name": "နံနံစေ့ (ထောင်းပြီး)", "quantity": 4.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၄ လဖဇ", "normalized_quantity": 20.0, "normalized_unit": "g", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0055", "name_mm": "ဇီယာ", "name_en": "Cumin seeds", "original_name": "ဇီယာစေ့ (ထောင်းပြီး)", "quantity": 1.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁ လဖဇ", "normalized_quantity": 5.0, "normalized_unit": "g", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0024", "name_mm": "နနွင်းမှုန့်", "name_en": "Turmeric powder", "original_name": "နနွင်းမှုန့်", "quantity": 1.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁ လဖဇ", "normalized_quantity": 5.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0013", "name_mm": "ဂျင်း", "name_en": "Ginger", "original_name": "ချင်း (၁\" လှီးပြီး)", "quantity": 2.0, "unit": "တုံး (piece)", "original_quantity_text": "၂ တုံး", "normalized_quantity": 2.0, "normalized_unit": "piece", "preparation_note_mm": "လှီးပြီး", "preparation_note_en": "sliced"},
            {"ingredient_id": "I0044", "name_mm": "ငရုတ်သီးစိမ်း", "name_en": "Green chili", "original_name": "ငရုတ်သီးစိမ်း (လှီးပြီး)", "quantity": 2.0, "unit": "တောင့် (piece)", "original_quantity_text": "၂ တောင့်", "normalized_quantity": 2.0, "normalized_unit": "piece", "preparation_note_mm": "လှီးပြီး", "preparation_note_en": "sliced"},
            {"ingredient_id": "I0012", "name_mm": "မဆလာ", "name_en": "Garam masala", "original_name": "မဆလာ", "quantity": 2.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၂ စပဇ", "normalized_quantity": 30.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0076", "name_mm": "အမဲသား", "name_en": "Beef", "original_name": "အမဲ (စဉ်းကောလုပ်ပြီး)", "quantity": 75.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၇၅ ကျပ်သား", "normalized_quantity": 1224.7, "normalized_unit": "g", "preparation_note_mm": "စဉ်းကောလုပ်ပြီး", "preparation_note_en": "minced"},
            {"ingredient_id": "I0020", "name_mm": "အာလူး", "name_en": "Potato", "original_name": "အာလူး (၄ စိတ်လှီး)", "quantity": 30.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၃၀ ကျပ်သား", "normalized_quantity": 489.9, "normalized_unit": "g", "preparation_note_mm": "၄ စိတ်လှီး", "preparation_note_en": "quartered"},
            {"ingredient_id": "I0077", "name_mm": "ပဲစိမ်း", "name_en": "Green peas", "original_name": "ပဲစိမ်း", "quantity": 30.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၃၀ ကျပ်သား", "normalized_quantity": 489.9, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 1.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁ လဖဇ", "normalized_quantity": 5.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None}
        ],
        "servings": 10,
        "preparation_time_minutes": 20,
        "cooking_time_minutes": 35,
        "instructions_mm": [
            "ဒယ်အိုးပြားတွင် ဆီထည့်၍ ပူအောင်လုပ်ပြီး ကြက်သွန်နီထည့်ကာ ခပ်ပျော့ပျော့အနေချက်ပါ။",
            "ဟင်းခတ်အမွှေးအကြိုင်များ ပေါင်းစပ်ထည့်ပြီး မီးအေးအေးတွင် (၅)မိနစ်ခန့် ကြော်ပါ။ ရေ (၁)စားပွဲဇွန်းထည့်ပြီး မွှေပါ။",
            "အမဲစဉ်းကောသားများ ရောထည့်ပြီး မီးရှိန်ကိုမြှင့်၍ အသားများ ညိုလာသည်အထိ ချက်ပါ။",
            "စဉ်းကောသားများ ညိုရောင်ဖြစ်လာလျှင် မီးရှိန်ပြန်လျှော့ကာ လှီးစိတ်ထားသည့် အာလူးနှင့် ဆားကိုထည့်မွှေပြီး (၅)မိနစ်ခန့် မီးအေးအေးဖြင့် ချက်ပါ။",
            "ပြီးမှ ပဲစိမ်းကို ရောထည့်ပါ။ အာလူးနှင့် ပဲများ နူးသည်အထိ ဆက်၍ချက်ပါ။ ပူပူနွေးနွေး တည်ခင်း၍ရပြီ ဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Heat oil in a wide pan and sauté sliced onions until soft and translucent.",
            "Add coriander, cumin, turmeric, ginger, chili, and garam masala; fry gently for 5 minutes, adding 1 tbsp water to prevent scorching.",
            "Add minced beef, increase heat, and cook while stirring until well browned.",
            "Reduce heat, fold in quartered potatoes and salt, cooking for 5 minutes over gentle heat.",
            "Stir in green peas and continue simmering until both potatoes and peas are tender; serve hot."
        ],
        "tags": {"dietary": ["dairy-free", "gluten-free"], "seasonal": ["all-season"], "festival": [], "main_ingredients": ["beef", "potato", "green pea"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [51], "printed_page_numbers": [91], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 91 (top). Classic beef keema matar aloo.", "verified": True}
    },

    # R0034: ခရမ်းသီးကတ်တလက် (Brinjal Cutlets)
    {
        "recipe_id": "R0034",
        "name_mm": "ခရမ်းသီးကတ်တလက်",
        "name_en": "Brinjal Cutlets Stuffed with Beef",
        "description_mm": None,
        "description_en": None,
        "category": "Beef dishes",
        "meal_types": ["lunch", "dinner", "snack"],
        "ingredients": [
            {"ingredient_id": "I0078", "name_mm": "ခရမ်းသီး", "name_en": "Eggplant", "original_name": "ခရမ်းသီးရှည် (အလုံးကြီး)", "quantity": 5.0, "unit": "လုံး (piece)", "original_quantity_text": "၅ လုံး", "normalized_quantity": 5.0, "normalized_unit": "piece", "preparation_note_mm": "အလုံးကြီး", "preparation_note_en": "large long brinjals"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 2.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၂ လဖဇ", "normalized_quantity": 10.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "original_name": "ဆီ", "quantity": 10.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၁၀ ကျပ်သား", "normalized_quantity": 163.3, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "original_name": "ကြက်သွန်နီ (နုပ်နုပ်စဉ်း)", "quantity": 3.0, "unit": "လုံး (piece)", "original_quantity_text": "၃ လုံး", "normalized_quantity": 3.0, "normalized_unit": "piece", "preparation_note_mm": "နုပ်နုပ်စဉ်း", "preparation_note_en": "finely minced"},
            {"ingredient_id": "I0044", "name_mm": "ငရုတ်သီးစိမ်း", "name_en": "Green chili", "original_name": "ငရုတ်သီးစိမ်း (နုပ်နုပ်စဉ်း)", "quantity": 5.0, "unit": "တောင့် (piece)", "original_quantity_text": "၅ တောင့်", "normalized_quantity": 5.0, "normalized_unit": "piece", "preparation_note_mm": "နုပ်နုပ်စဉ်း", "preparation_note_en": "finely minced"},
            {"ingredient_id": "I0014", "name_mm": "ကြက်သွန်ဖြူ", "name_en": "Garlic", "original_name": "ကြက်သွန်ဖြူ (နုပ်နုပ်စဉ်း)", "quantity": 3.0, "unit": "မြွှာ (piece)", "original_quantity_text": "၃ မြွှာ", "normalized_quantity": 3.0, "normalized_unit": "piece", "preparation_note_mm": "နုပ်နုပ်စဉ်း", "preparation_note_en": "finely minced"},
            {"ingredient_id": "I0024", "name_mm": "နနွင်းမှုန့်", "name_en": "Turmeric powder", "original_name": "နနွင်း", "quantity": 1.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁ လဖဇ", "normalized_quantity": 5.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0076", "name_mm": "အမဲသား", "name_en": "Beef", "original_name": "အမဲ (စဉ်းကောလုပ်ပြီး)", "quantity": 75.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၇၅ ကျပ်သား", "normalized_quantity": 1224.7, "normalized_unit": "g", "preparation_note_mm": "စဉ်းကောလုပ်ပြီး", "preparation_note_en": "minced"},
            {"ingredient_id": "I0026", "name_mm": "ကြက်ဥ", "name_en": "Chicken egg", "original_name": "ကြက်ဥ (ခေါက်ပြီး)", "quantity": 3.0, "unit": "လုံး (piece)", "original_quantity_text": "၃ လုံး", "normalized_quantity": 3.0, "normalized_unit": "piece", "preparation_note_mm": "ခေါက်ပြီး", "preparation_note_en": "beaten"},
            {"ingredient_id": "I0075", "name_mm": "ပေါင်မုန့်ကြွပ်မှုန့်", "name_en": "Breadcrumbs", "original_name": "မုန့်ကြွပ်အမှုန့်", "quantity": 7.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၇ စပဇ", "normalized_quantity": 105.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None}
        ],
        "servings": 10,
        "preparation_time_minutes": 25,
        "cooking_time_minutes": 35,
        "instructions_mm": [
            "ဆားထည့်ထားသော ရေဆူတွင် ခရမ်းသီးကို (၁၅)မိနစ်ခန့် ပြုတ်ပါ။ နူးလာပါလိမ့်မည်။ ပြီးလျှင် ရေကုန်အောင် စစ်ထားပါ။",
            "ဒယ်တွင် ဆီထည့်၍ ပူအောင်လုပ်ပါ။ ကြက်သွန်နီထည့်ပြီး ရွှေရောင်သမ်းသည်အထိ ကြော်ပါ။ ကြက်သွန်ဖြူ၊ ငရုတ်သီးစိမ်းနှင့် နနွင်းထည့်၍ (၂)မိနစ်ခန့် မွှေပေးပါ။ ပြီးလျှင် အမဲစဉ်းကောများ ထည့်ချက်ပါ။",
            "အားလုံး ညိုလာသည်အထိ မွှေပေးပါ။ အရသာအတွက် ဆားအနည်းငယ်ထည့်ပြီး မီးအေးအေးဖြင့် မိနစ်(၂၀)ခန့် ချက်ပါ။ အသားများ နူးလာပါလိမ့်မည်။",
            "ရေစစ်ထားသော ခရမ်းသီးကို အလယ်မှ အလျားလိုက် ထက်ခြမ်းခွဲပါ။ အတွင်းသားများကို သေချာစွာ အခွံမပြဲအောင် ဇွန်းဖြင့်ကလော်ထုတ်ယူပြီး အသားစဉ်းကောဖြင့် နှံ့အောင်ရောစပ်ပါ။",
            "ဆားအပေါ့အငံမြည်းပြီးနောက် ရောစပ်ထားသည်များကို ခရမ်းသီးအခွံတွင်းသို့ အနေတော်ထည့်ကာ ခေါက်ထားသော ကြက်ဥအရည်ကို မျက်နှာပြင်တွင် သုတ်လိမ်းပါ။",
            "၎င်းအပေါ်မှနေ၍ မုန့်ကြွပ်အကြွပ်အမှုန့်များ ဖုံးအုပ်ပါ။ ကြိုတင်အပူပေးထားသော လက်ကိုင်ပါဒယ်တွင် မျက်နှာပြင်မှောက်ပြီး ဆီပူထိုးပါ။ မျက်နှာပြင် ရွှေရောင်သမ်းလာလျှင် တည်ခင်း၍ရပြီဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Boil whole eggplants in salted water for 15 minutes until tender, then drain thoroughly.",
            "Heat oil in a pan, fry onions until golden, then sauté garlic, green chilies, and turmeric for 2 minutes; add minced beef and stir until browned.",
            "Season beef with salt and simmer gently for 20 minutes until tender.",
            "Halve boiled eggplants lengthwise and scoop out the flesh without tearing skins; mash flesh into the cooked beef.",
            "Spoon stuffing back into eggplant shells, brush surface with beaten egg, and coat generously with breadcrumbs.",
            "Place stuffed eggplants face-down in a hot oiled skillet to pan-fry until golden brown and crisp, then serve."
        ],
        "tags": {"dietary": ["dairy-free"], "seasonal": ["all-season"], "festival": [], "main_ingredients": ["eggplant", "beef", "breadcrumbs"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [51], "printed_page_numbers": [91], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 91 (bottom). Stuffed baked/pan-fried brinjal boat cutlet.", "verified": True}
    },

    # R0035: အမဲနှပ် (Braised Beef)
    {
        "recipe_id": "R0035",
        "name_mm": "အမဲနှပ်",
        "name_en": "Braised Beef",
        "description_mm": None,
        "description_en": None,
        "category": "Beef dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {"ingredient_id": "I0076", "name_mm": "အမဲသား", "name_en": "Beef", "original_name": "အမဲသား", "quantity": 80.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၈၀ ကျပ်သား", "normalized_quantity": 1306.3, "normalized_unit": "g", "preparation_note_mm": "ရေစိုအဝတ်ဖြင့် သန့်စင်ထားသော", "preparation_note_en": "wiped clean with damp cloth"},
            {"ingredient_id": "I0079", "name_mm": "ရှောက်သီး", "name_en": "Lemon / Citron", "original_name": "ရှောက်ရည်", "quantity": 5.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၅ စပဇ", "normalized_quantity": 75.0, "normalized_unit": "g", "preparation_note_mm": "ရှောက်ရည်", "preparation_note_en": "citron / lemon juice"},
            {"ingredient_id": "I0041", "name_mm": "ငရုတ်သီးခြောက်", "name_en": "Dried red chili", "original_name": "ငရုတ်သီးခြောက်", "quantity": 2.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၂ ကျပ်သား", "normalized_quantity": 32.7, "normalized_unit": "g", "preparation_note_mm": "ထောင်းထားသော", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "original_name": "ကြက်သွန်နီ", "quantity": 15.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၁၅ ကျပ်သား", "normalized_quantity": 245.0, "normalized_unit": "g", "preparation_note_mm": "ထောင်းထားသော", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0014", "name_mm": "ကြက်သွန်ဖြူ", "name_en": "Garlic", "original_name": "ကြက်သွန်ဖြူ", "quantity": 3.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၃ ကျပ်သား", "normalized_quantity": 49.0, "normalized_unit": "g", "preparation_note_mm": "ထောင်းထားသော", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0013", "name_mm": "ဂျင်း", "name_en": "Ginger", "original_name": "ချင်း (၁\")", "quantity": 2.0, "unit": "တုံး (piece)", "original_quantity_text": "၂ တုံး", "normalized_quantity": 2.0, "normalized_unit": "piece", "preparation_note_mm": "ထောင်းထားသော", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "original_name": "ဆီ", "quantity": 15.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၁၅ ကျပ်သား", "normalized_quantity": 245.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 2.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၂ လဖဇ", "normalized_quantity": 10.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0012", "name_mm": "မဆလာ", "name_en": "Garam masala", "original_name": "မဆလာမှုန့်", "quantity": 3.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၃ လဖဇ", "normalized_quantity": 15.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None}
        ],
        "servings": 10,
        "preparation_time_minutes": 20,
        "cooking_time_minutes": 75,
        "instructions_mm": [
            "အမဲသားကို ရေစိုအဝတ်ဖြင့် သန့်စင်အောင်ပြုလုပ်ပြီး ရှောက်ရည်ဖြင့် နယ်ပါ။",
            "ထောင်းထားသော ငရုတ်သီးခြောက်၊ ကြက်သွန်နီ၊ ကြက်သွန်ဖြူ၊ ချင်းတို့နှင့် ဆက်၍နယ်ပါ။",
            "ဆီထည့်ပါ။ ရေနွေးနည်းနည်းစီထည့်ပြီး မီးအေးအေးဖြင့် နူးသည်အထိနှပ်ပါ။",
            "နူးမှသာ ဆားနှင့် မဆလာမှုန့်ခတ်ပါ။ (အဖုံးအုပ်ထားပြီးနှပ်ရန် အထူးသတိပြုရပါမည်။)",
            "ပြီးလျှင် တည်ခင်း၍ရပြီဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Wipe beef clean with a damp cloth and massage thoroughly with lemon/citron juice.",
            "Rub with pounded dried chilies, onion, garlic, and ginger paste.",
            "Add cooking oil, gradually splash hot water, cover tightly, and braise slowly over very low heat until tender.",
            "Season with salt and garam masala only after the beef is tender (essential to keep covered during braising).",
            "Cook until rich oil coats the tender beef, then serve."
        ],
        "tags": {"dietary": ["dairy-free", "gluten-free"], "seasonal": ["all-season"], "festival": [], "main_ingredients": ["beef", "citron"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [52], "printed_page_numbers": [92], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 92 (top). Author notes seasoning with salt only after meat tenders.", "verified": True}
    },

    # R0036: အမဲသားနှင့်မှိုကြော် (Beef with Chinese Mushrooms)
    {
        "recipe_id": "R0036",
        "name_mm": "အမဲသားနှင့်မှိုကြော်",
        "name_en": "Beef with Chinese Mushrooms",
        "description_mm": None,
        "description_en": None,
        "category": "Beef dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {"ingredient_id": "I0051", "name_mm": "ဂျုံပြောင်းမှုန့်", "name_en": "Cornstarch", "original_name": "ပြောင်းကော်မှုန့်", "quantity": 3.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၃ လဖဇ", "normalized_quantity": 15.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0050", "name_mm": "ပဲငံပြာရည်", "name_en": "Soy sauce", "original_name": "ပဲငံပြာရည် (အကြည်)", "quantity": 3.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၃ စပဇ", "normalized_quantity": 45.0, "normalized_unit": "g", "preparation_note_mm": "အကြည်", "preparation_note_en": "light"},
            {"ingredient_id": "I0026", "name_mm": "ကြက်ဥ", "name_en": "Chicken egg", "original_name": "ကြက်ဥ (အကာ)", "quantity": 3.0, "unit": "လုံး (piece)", "original_quantity_text": "၃ လုံး", "normalized_quantity": 3.0, "normalized_unit": "piece", "preparation_note_mm": "အကာ", "preparation_note_en": "egg whites only"},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "original_name": "သကြား", "quantity": 3.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၃ လဖဇ", "normalized_quantity": 15.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0076", "name_mm": "အမဲသား", "name_en": "Beef", "original_name": "အမဲတင်ပါးသား", "quantity": 65.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၆၅ ကျပ်သား", "normalized_quantity": 1061.4, "normalized_unit": "g", "preparation_note_mm": "ခပ်ပါးပါးလှီးစိတ်", "preparation_note_en": "thinly sliced rump steak"},
            {"ingredient_id": "I0080", "name_mm": "တရုတ်မှိုခြောက်", "name_en": "Dried Chinese mushrooms", "original_name": "တရုတ်မှိုခြောက်", "quantity": 15.0, "unit": "ခု (piece)", "original_quantity_text": "၁၅ ခု", "normalized_quantity": 15.0, "normalized_unit": "piece", "preparation_note_mm": "ရေစိမ် ရေစစ် ပါးပါးလှီး", "preparation_note_en": "soaked, drained, and sliced into strips"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "original_name": "ဆီ", "quantity": 5.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၅ စပဇ", "normalized_quantity": 75.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0014", "name_mm": "ကြက်သွန်ဖြူ", "name_en": "Garlic", "original_name": "ကြက်သွန်ဖြူ (နုပ်နုပ်စဉ်း)", "quantity": 1.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၁ စပဇ", "normalized_quantity": 15.0, "normalized_unit": "g", "preparation_note_mm": "နုပ်နုပ်စဉ်း", "preparation_note_en": "finely minced"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 0.5, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁/၂ လဖဇ", "normalized_quantity": 2.5, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0039", "name_mm": "ငရုတ်ကောင်းမှုန့်", "name_en": "Ground black pepper", "original_name": "ငရုတ်ကောင်း", "quantity": 0.25, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁/၄ လဖဇ", "normalized_quantity": 1.25, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0060", "name_mm": "ရှယ်ရီအရက်", "name_en": "Cooking wine", "original_name": "တရုတ်ဝိုင်", "quantity": 5.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၅ စပဇ", "normalized_quantity": 75.0, "normalized_unit": "g", "preparation_note_mm": "တရုတ်ဝိုင်", "preparation_note_en": "Chinese rice wine"}
        ],
        "servings": 10,
        "preparation_time_minutes": 60,
        "cooking_time_minutes": 15,
        "instructions_mm": [
            "ဇလုံထဲသို့ ပြောင်းကော်မှုန့်နှင့် ပဲငံပြာရည်ထည့်မွှေပါ။ ကြက်ဥအကာနှင့် သကြားကို ထပ်ကာတလဲလဲ ခေါက်မွှေကာ ဇလုံထဲရှိ အရောများနှင့် ပေါင်းစပ်ခေါက်မွှေပါ။",
            "အမဲသားကို ခပ်ပါးပါးလှီးစိတ်ပြီး ပြုလုပ်ထားသည့် စိမ်ရေတွင်ထည့်၍ (၁)နာရီခန့် စိမ်ထားပါ။",
            "ထို့အတူ ပူနွေးသောရေတွင် မှိုကို (၁)နာရီခန့်စိမ်ကာ ရေစစ်ပြီး ခပ်ပါးပါးအချောင်းပုံ လှီးဖြတ်ထားပါ။",
            "ဒယ်အိုးထဲသို့ ဆီထည့်၍ အပူပေးပြီး အပိုင်းအစသေးများအဖြစ် ခုတ်စဉ်းထားသည့် ကြက်သွန်ဖြူထည့်မွှေပါ။",
            "အမဲသားနှင့် မှိုကိုလည်းထည့်ကာ ရွှေရောင်သမ်းပြီး အသားနူးသည်အထိမွှေကြော်ပါ။ ဆားနှင့် ငရုတ်ကောင်းခတ်ပါ။",
            "နောက်ဆုံးတွင် တရုတ်ဝိုင်ထည့်မွှေကာ ဖိုမှချပြီး အရည်များ မခြောက်ခန်းမီ ပန်းကန်ထဲထည့်ပါ။ ပြီးလျှင် တည်ခင်း၍ရပြီ ဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Whisk cornstarch, light soy sauce, egg whites, and sugar together to create a velveting marinade.",
            "Thinly slice beef rump steak and marinate in the mixture for 1 hour.",
            "Soak dried mushrooms in warm water for 1 hour, drain, and slice into thin strips.",
            "Heat oil in wok and sauté minced garlic until fragrant.",
            "Add marinated beef and mushrooms, stir-frying over high heat until browned and tender; season with salt and pepper.",
            "Splash in Chinese wine, toss briefly until aromatic and glazed with sauce, then transfer to a plate and serve."
        ],
        "tags": {"dietary": ["dairy-free"], "seasonal": ["all-season"], "festival": [], "main_ingredients": ["beef", "shiitake", "chinese wine"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [52], "printed_page_numbers": [92], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 92 (bottom). Chinese stir-fry with Shaoxing wine and dried shiitake.", "verified": True}
    },

    # R0037: အမဲသားဟင်း (Curried Beef)
    {
        "recipe_id": "R0037",
        "name_mm": "အမဲသားဟင်း",
        "name_en": "Curried Beef",
        "description_mm": None,
        "description_en": None,
        "category": "Beef dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "original_name": "ကြက်သွန်နီ (ပါးပါးလှီး)", "quantity": 8.0, "unit": "လုံး (piece)", "original_quantity_text": "၈ လုံး", "normalized_quantity": 8.0, "normalized_unit": "piece", "preparation_note_mm": "ပါးပါးလှီး", "preparation_note_en": "thinly sliced"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "original_name": "ဆီ", "quantity": 6.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၆ ကျပ်သား", "normalized_quantity": 98.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0024", "name_mm": "နနွင်းမှုန့်", "name_en": "Turmeric powder", "original_name": "နနွင်းမှုန့်", "quantity": 1.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁ လဖဇ", "normalized_quantity": 5.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0054", "name_mm": "နံနံစေ့", "name_en": "Coriander seeds", "original_name": "နံနံစေ့ (ထောင်းပြီး)", "quantity": 1.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁ လဖဇ", "normalized_quantity": 5.0, "normalized_unit": "g", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0081", "name_mm": "စမုန်နက်စေ့", "name_en": "Nigella seeds", "original_name": "စမုန်နက်စေ့ (ထောင်းပြီး)", "quantity": 1.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁ လဖဇ", "normalized_quantity": 5.0, "normalized_unit": "g", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0008", "name_mm": "သစ်ကြံပိုးခေါက်", "name_en": "Cinnamon", "original_name": "သစ်ကြံပိုး (၂\" အရွယ်)", "quantity": 2.0, "unit": "ခေါက် (piece)", "original_quantity_text": "၂ ခေါက်", "normalized_quantity": 2.0, "normalized_unit": "piece", "preparation_note_mm": "၂\" အရွယ်", "preparation_note_en": "2-inch size"},
            {"ingredient_id": "I0034", "name_mm": "ကရဝေးရွက်", "name_en": "Bay leaf", "original_name": "ကရဝေး", "quantity": 4.0, "unit": "ရွက် (piece)", "original_quantity_text": "၄ ရွက်", "normalized_quantity": 4.0, "normalized_unit": "piece", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0009", "name_mm": "လေးညှင်းပွင့်", "name_en": "Clove", "original_name": "လေးညှင်း", "quantity": 5.0, "unit": "ပွင့် (piece)", "original_quantity_text": "၅ ပွင့်", "normalized_quantity": 5.0, "normalized_unit": "piece", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0025", "name_mm": "ငရုတ်သီးမှုန့်", "name_en": "Chili powder", "original_name": "ငရုတ်သီးမှုန့်", "quantity": 2.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၂ လဖဇ", "normalized_quantity": 10.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0014", "name_mm": "ကြက်သွန်ဖြူ", "name_en": "Garlic", "original_name": "ကြက်သွန်ဖြူ", "quantity": 3.0, "unit": "မြွှာ (piece)", "original_quantity_text": "၃ မြွှာ", "normalized_quantity": 3.0, "normalized_unit": "piece", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0076", "name_mm": "အမဲသား", "name_en": "Beef", "original_name": "အမဲသား", "quantity": 65.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၆၅ ကျပ်သား", "normalized_quantity": 1061.4, "normalized_unit": "g", "preparation_note_mm": "၁\" စတုရန်းနှင့် ၁/၂\" အထူ လှီးထားသော", "preparation_note_en": "cut into 1-inch squares and 1/2-inch thick"},
            {"ingredient_id": "I0036", "name_mm": "နွားနို့", "name_en": "Cow milk", "original_name": "နွားနို့", "quantity": 1.0, "unit": "ခွက် (cup / g)", "original_quantity_text": "၁ ခွက်", "normalized_quantity": 240.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0029", "name_mm": "ဒိန်ချဉ်", "name_en": "Curd", "original_name": "ဒိန်ချဉ်", "quantity": 1.0, "unit": "ခွက် (cup / g)", "original_quantity_text": "၁ ခွက်", "normalized_quantity": 240.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "original_name": "ရေ", "quantity": 2.0, "unit": "ခွက် (cup / g)", "original_quantity_text": "၂ ခွက်", "normalized_quantity": 480.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0082", "name_mm": "ပင်စိမ်း", "name_en": "Basil", "original_name": "ပင်စိမ်း", "quantity": 4.0, "unit": "ရွက် (piece)", "original_quantity_text": "၄ ရွက်", "normalized_quantity": 4.0, "normalized_unit": "piece", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0083", "name_mm": "စပါးလင်", "name_en": "Lemongrass", "original_name": "စပါးလင် (ထုထားပြီး)", "quantity": 4.0, "unit": "တောင့် (piece)", "original_quantity_text": "၄ တောင့်", "normalized_quantity": 4.0, "normalized_unit": "piece", "preparation_note_mm": "ထုထားပြီး", "preparation_note_en": "bruised"},
            {"ingredient_id": "I0044", "name_mm": "ငရုတ်သီးစိမ်း", "name_en": "Green chili", "original_name": "ငရုတ်စိမ်း (ပါးပါးလှီး)", "quantity": 6.0, "unit": "တောင့် (piece)", "original_quantity_text": "၆ တောင့်", "normalized_quantity": 6.0, "normalized_unit": "piece", "preparation_note_mm": "ပါးပါးလှီး", "preparation_note_en": "thinly sliced"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 2.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၂ လဖဇ", "normalized_quantity": 10.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None}
        ],
        "servings": 10,
        "preparation_time_minutes": 25,
        "cooking_time_minutes": 60,
        "instructions_mm": [
            "ဆီပူတွင် ကြက်သွန်နီ ပထမထည့်မွှေပါ။ အညိုရောင်ရရှိလျှင် တစ်ဖက်သို့ ဖယ်ထားပါ။",
            "နနွင်းမှုန့်၊ နံနံစေ့၊ စမုန်နက်စေ့၊ သစ်ကြံပိုး၊ ကရဝေး၊ လေးညှင်း၊ ငရုတ်သီးမှုန့်၊ ကြက်သွန်ဖြူတို့ကို (၂)မိနစ်ခန့် ဆီသတ်ပြီး တစ်လက်မစတုရန်းနှင့် လက်မဝက်ခန့်အရွယ် လှီးထားသည့် အမဲသားထည့်ကြော်ပါ။",
            "ပြီးလျှင် အားလုံးကို အိုးတစ်လုံးတွင် ရောထည့်၍ နွားနို့၊ ဒိန်ချဉ်၊ ရေ၊ ပင်စိမ်း၊ စပါးလင်၊ ငရုတ်သီးစိမ်းနှင့် ဆားတို့ကို ပေါင်းစပ်ထည့်ကာရောမွှေပါ။",
            "အိုးအဖုံးကို တင်းကျပ်စွာပိတ်ပြီး မီးအေးအေးဖြင့် (၁)နာရီခန့် အသားနူးသည်အထိ ချက်ရပါမည်။ ပြီးလျှင် တည်ခင်း၍ရပြီ ဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Fry sliced onions in hot oil until rich brown and set aside.",
            "Sauté turmeric, coriander, nigella seeds, cinnamon, bay leaves, cloves, chili powder, and garlic for 2 minutes; add sliced beef squares and sear.",
            "Transfer all contents into a pot, stir in milk, yogurt, water, basil, bruised lemongrass, green chilies, and salt.",
            "Cover tightly and simmer gently over low heat for about 1 hour until the beef is meltingly tender, then serve."
        ],
        "tags": {"dietary": ["gluten-free"], "seasonal": ["all-season"], "festival": [], "main_ingredients": ["beef", "milk", "yogurt", "lemongrass"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [52], "printed_page_numbers": [93], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 93 (top). Fragrant beef braised with lemongrass and milk/yogurt.", "verified": True}
    },

    # R0038: အမဲသားအာလူးဟင်း (Beef Curry with Potatoes)
    {
        "recipe_id": "R0038",
        "name_mm": "အမဲသားအာလူးဟင်း",
        "name_en": "Beef Curry with Potatoes",
        "description_mm": None,
        "description_en": None,
        "category": "Beef dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "original_name": "ဆီ", "quantity": 10.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၁၀ စပဇ", "normalized_quantity": 150.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "original_name": "ကြက်သွန်နီ (ခုတ်စဉ်းပြီး)", "quantity": 5.0, "unit": "လုံး (piece)", "original_quantity_text": "၅ လုံး", "normalized_quantity": 5.0, "normalized_unit": "piece", "preparation_note_mm": "ခုတ်စဉ်းပြီး", "preparation_note_en": "chopped"},
            {"ingredient_id": "I0014", "name_mm": "ကြက်သွန်ဖြူ", "name_en": "Garlic", "original_name": "ကြက်သွန်ဖြူ (ခုတ်စဉ်းပြီး)", "quantity": 5.0, "unit": "မြွှာ (piece)", "original_quantity_text": "၅ မြွှာ", "normalized_quantity": 5.0, "normalized_unit": "piece", "preparation_note_mm": "ခုတ်စဉ်းပြီး", "preparation_note_en": "chopped"},
            {"ingredient_id": "I0025", "name_mm": "ငရုတ်သီးမှုန့်", "name_en": "Chili powder", "original_name": "ငရုတ်သီးခြောက်အမှုန့်", "quantity": 2.5, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၂ ၁/၂ လဖဇ", "normalized_quantity": 12.5, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0055", "name_mm": "ဇီယာ", "name_en": "Cumin seeds", "original_name": "ဇီယာ (ထောင်းပြီး)", "quantity": 2.5, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၂ ၁/၂ စပဇ", "normalized_quantity": 37.5, "normalized_unit": "g", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0054", "name_mm": "နံနံစေ့", "name_en": "Coriander seeds", "original_name": "နံနံစေ့ (ထောင်းပြီး)", "quantity": 3.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၃ စပဇ", "normalized_quantity": 45.0, "normalized_unit": "g", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0013", "name_mm": "ဂျင်း", "name_en": "Ginger", "original_name": "ချင်း(၁\" အရွယ်ခုတ်စဉ်းပြီး)", "quantity": 2.0, "unit": "တုံး (piece)", "original_quantity_text": "၂ တုံး", "normalized_quantity": 2.0, "normalized_unit": "piece", "preparation_note_mm": "ခုတ်စဉ်းပြီး", "preparation_note_en": "chopped"},
            {"ingredient_id": "I0076", "name_mm": "အမဲသား", "name_en": "Beef", "original_name": "အမဲသား (တုံးတစ်ပြီး)", "quantity": 0.25, "unit": "ပိဿာ (kg)", "original_quantity_text": "၁/၄ ပိဿာ", "normalized_quantity": 408.2, "normalized_unit": "g", "preparation_note_mm": "တုံးတစ်ပြီး", "preparation_note_en": "cubed"},
            {"ingredient_id": "I0084", "name_mm": "ခရမ်းချဉ်သီးဆော့စ်", "name_en": "Tomato sauce", "original_name": "ခရမ်းချဉ်သီးဆော့စ်", "quantity": 5.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၅ စပဇ", "normalized_quantity": 75.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 2.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၂ စပဇ", "normalized_quantity": 30.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0020", "name_mm": "အာလူး", "name_en": "Potato", "original_name": "အာလူး (ထက်ခြမ်းစိတ်ပြီး)", "quantity": 40.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၄၀ ကျပ်သား", "normalized_quantity": 653.2, "normalized_unit": "g", "preparation_note_mm": "ထက်ခြမ်းစိတ်ပြီး", "preparation_note_en": "halved"},
            {"ingredient_id": "I0044", "name_mm": "ငရုတ်သီးစိမ်း", "name_en": "Green chili", "original_name": "ငရုတ်သီးစိမ်း", "quantity": 10.0, "unit": "တောင့် (piece)", "original_quantity_text": "၁၀ တောင့်", "normalized_quantity": 10.0, "normalized_unit": "piece", "preparation_note_mm": "အတောင့်လိုက်", "preparation_note_en": "whole"}
        ],
        "servings": 10,
        "preparation_time_minutes": 25,
        "cooking_time_minutes": 75,
        "instructions_mm": [
            "ဒယ်အိုးပြားကြီးတွင် ဆီထည့်၍ ပူအောင်လုပ်ပြီး ကြက်သွန်နီကို အနည်းငယ် အရောင်ပြောင်းသည်အထိသာ ကြော်ပါ။",
            "ကြက်သွန်ဖြူ၊ ငရုတ်သီးမှုန့်၊ ဇီယာ၊ နံနံစေ့နှင့် ချင်းတို့ ထည့်ကာ မီးအေးအေးဖြင့် (၅)မိနစ်ထားပြီး မကြာခဏမွှေပေးပါ။ အိုးတွင်းရှိအရောများ ခြောက်ခန်းလာလျှင် ရေ(၅)စားပွဲဇွန်း ထည့်ပါ။",
            "အမဲသားများကို ထည့်ပြီးချက်ပါ။ အမဲသားတုံးများ ညိုရောင်ရလာသည်အထိ မွှေပေးပါ။",
            "ခရမ်းချဉ်သီးဆော့စ်၊ ဆားထည့်ပြီး ရေမြုပ်ရုံထည့်ကာ အသာအယာမွှေပေးပါ။ အဖုံးပိတ်၍ ဆူပွက်လာသည်အထိ (၁)နာရီခန့်ထားပါ။",
            "ပြီးလျှင် အာလူးနှင့် ငရုတ်စိမ်းအတောင့်လိုက်ကိုထည့်ပြီး အာလူးနူးသည်အထိ ခပ်ဖြည်းဖြည်းဆူအောင်ချက်ပါ။ ပြီးလျှင် တည်ခင်း၍ရပြီ ဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Heat oil in a large pan and fry chopped onions until lightly colored.",
            "Add garlic, chili powder, cumin, coriander, and ginger; cook gently for 5 minutes, stirring frequently and adding 5 tbsp water if it gets dry.",
            "Add beef cubes and stir-fry until nicely browned.",
            "Add tomato sauce, salt, and enough water to submerge beef; cover and simmer for about 1 hour.",
            "Add halved potatoes and whole green chilies; simmer slowly until potatoes are tender and gravy is richly thickened, then serve."
        ],
        "tags": {"dietary": ["dairy-free", "gluten-free"], "seasonal": ["all-season"], "festival": [], "main_ingredients": ["beef", "potato", "tomato"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [52], "printed_page_numbers": [93], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 93 (bottom). Wholesome beef and potato curry.", "verified": True}
    },

    # R0039: ဝက်သားတရုတ်ချက် (Chinese-Style Pork)
    {
        "recipe_id": "R0039",
        "name_mm": "ဝက်သားတရုတ်ချက်",
        "name_en": "Chinese-Style Pork",
        "description_mm": None,
        "description_en": None,
        "category": "Pork dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {"ingredient_id": "I0013", "name_mm": "ဂျင်း", "name_en": "Ginger", "original_name": "ချင်း (ညက်ညက်ထောင်း)", "quantity": 1.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၁ ကျပ်သား", "normalized_quantity": 16.3, "normalized_unit": "g", "preparation_note_mm": "ညက်ညက်ထောင်း", "preparation_note_en": "finely pounded"},
            {"ingredient_id": "I0014", "name_mm": "ကြက်သွန်ဖြူ", "name_en": "Garlic", "original_name": "ကြက်သွန်ဖြူ (ဓားပြားရိုက်)", "quantity": 2.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၂ ကျပ်သား", "normalized_quantity": 32.7, "normalized_unit": "g", "preparation_note_mm": "ဓားပြားရိုက်", "preparation_note_en": "crushed"},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "original_name": "ကြက်သွန်နီ (လေးစိတ်စိတ်)", "quantity": 5.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၅ ကျပ်သား", "normalized_quantity": 81.6, "normalized_unit": "g", "preparation_note_mm": "လေးစိတ်စိတ်", "preparation_note_en": "quartered"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 1.5, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၁ ၁/၂ စပဇ", "normalized_quantity": 22.5, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "original_name": "သကြား", "quantity": 1.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၁ စပဇ", "normalized_quantity": 15.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0050", "name_mm": "ပဲငံပြာရည်", "name_en": "Soy sauce", "original_name": "ပဲငံပြာရည် (အကြည်)", "quantity": 2.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၂ စပဇ", "normalized_quantity": 30.0, "normalized_unit": "g", "preparation_note_mm": "အကြည်", "preparation_note_en": "light"},
            {"ingredient_id": "I0050", "name_mm": "ပဲငံပြာရည်", "name_en": "Soy sauce", "original_name": "ပဲငံပြာရည် (အနောက်)", "quantity": 0.5, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၁/၂ စပဇ", "normalized_quantity": 7.5, "normalized_unit": "g", "preparation_note_mm": "အနောက်", "preparation_note_en": "dark"},
            {"ingredient_id": "I0085", "name_mm": "ဝက်သား", "name_en": "Pork", "original_name": "ဝက်သား (ပေါင်သား)", "quantity": 70.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၇၀ ကျပ်သား", "normalized_quantity": 1143.1, "normalized_unit": "g", "preparation_note_mm": "ပေါင်သား တုံးတစ်လှီးထားသော", "preparation_note_en": "pork leg / thigh cubed"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "original_name": "ဆီ", "quantity": 5.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၅ ကျပ်သား", "normalized_quantity": 81.6, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "original_name": "ရေနွေး", "quantity": None, "unit": "လိုအပ်သရွေ့ (as needed)", "original_quantity_text": "လိုအပ်သရွေ့", "normalized_quantity": None, "normalized_unit": "g", "preparation_note_mm": "ရေနွေး", "preparation_note_en": "hot water"}
        ],
        "servings": 10,
        "preparation_time_minutes": 20,
        "cooking_time_minutes": 50,
        "instructions_mm": [
            "ချင်း၊ ကြက်သွန်ဖြူ၊ ကြက်သွန်နီ၊ ဆား၊ သကြား၊ ပဲငံပြာရည်အကြည်နှင့် အနောက်တို့ကို တုံးတစ်လှီးထားသော ဝက်ပေါင်သားတုံးများနှင့် ရောကာ အသားထဲသို့ စိမ့်ဝင်သွားသည်အထိ နယ်ထားပါ။",
            "ဒန်အိုးထဲသို့ ဆီထည့်ပြီး ပူလာလျှင် နယ်ထားသော ဝက်သားတုံးများ ထည့်ကာ အဖုံးအုပ်၍ မီးအေးအေးဖြင့် တည်ပါ။",
            "အသားများမှ စိမ့်ရေများထွက်လာပြီး ဆီစိမ်းနံ့ပျောက်လာလျှင် အိုးဖင်မကပ်ရန် အိုးကို အသာအယာလှုပ်ပေးပါ။",
            "စိမ့်ရည်များခန်းပြီး အသံမြည်လာလျှင် အသားမြုပ်ရုံ ရေနွေးထည့်ကာ အဖုံးအုပ်တည်ပါ။ အသားမနူးသေးလျှင် ရေနွေးကို ပထမအကြိမ်ထက် နည်းငယ်လျှော့ပြီးထည့်ကာ ဆက်တည်ပါ။",
            "နှစ်ကြိမ်မျှ နှံ့အောင်မွှေပေးပါ။ ရေစပ်စပ်ဖြင့် အရသာချိုသောအဟင်းဖြစ်လာလျှင် တည်ခင်း၍ရပြီ ဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Marinate the cubed pork thigh with pounded ginger, crushed garlic, quartered onions, salt, sugar, light soy sauce, and dark soy sauce.",
            "Heat oil in a pot, add the marinated pork, cover, and cook over gentle heat.",
            "As natural juices emerge and the raw oil aroma subsides, gently shake the pot to prevent sticking.",
            "When juices reduce and sizzle, add hot water just to cover and braise covered; if still firm, add a little less hot water and continue braising.",
            "Stir twice to ensure even cooking; when a rich, slightly sweet sauce forms around tender pork, serve."
        ],
        "tags": {"dietary": ["dairy-free"], "seasonal": ["all-season"], "festival": [], "main_ingredients": ["pork", "soy sauce"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [53], "printed_page_numbers": [94], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 94 (top). Slow-braised sweet soy pork.", "verified": True}
    },

    # R0040: ဝက်သားနီချက် (Red-Golden Pork)
    {
        "recipe_id": "R0040",
        "name_mm": "ဝက်သားနီချက်",
        "name_en": "Red-Golden Pork",
        "description_mm": None,
        "description_en": None,
        "category": "Pork dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {"ingredient_id": "I0085", "name_mm": "ဝက်သား", "name_en": "Pork", "original_name": "ဝက်သား", "quantity": 1.0, "unit": "ပိဿာ (kg)", "original_quantity_text": "၁ ပိဿာ", "normalized_quantity": 1632.9, "normalized_unit": "g", "preparation_note_mm": "တစ်လက်မအရွယ် လေးထောင့်တုံး", "preparation_note_en": "cut into 1-inch cubes"},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "original_name": "ကြက်သွန်နီ", "quantity": 15.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၁၅ ကျပ်သား", "normalized_quantity": 245.0, "normalized_unit": "g", "preparation_note_mm": "ထောင်းပြီး အရည်ညှစ်", "preparation_note_en": "pounded and juiced"},
            {"ingredient_id": "I0014", "name_mm": "ကြက်သွန်ဖြူ", "name_en": "Garlic", "original_name": "ကြက်သွန်ဖြူ", "quantity": 4.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၄ ကျပ်သား", "normalized_quantity": 65.3, "normalized_unit": "g", "preparation_note_mm": "ထောင်းပြီး အရည်ညှစ်", "preparation_note_en": "pounded and juiced"},
            {"ingredient_id": "I0013", "name_mm": "ဂျင်း", "name_en": "Ginger", "original_name": "ချင်း", "quantity": 4.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၄ ကျပ်သား", "normalized_quantity": 65.3, "normalized_unit": "g", "preparation_note_mm": "ထောင်းပြီး အရည်ညှစ်", "preparation_note_en": "pounded and juiced"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "original_name": "ဆီ", "quantity": 10.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၁၀ ကျပ်သား", "normalized_quantity": 163.3, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 2.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၂ စပဇ", "normalized_quantity": 30.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "original_name": "သကြား", "quantity": 2.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၂ စပဇ", "normalized_quantity": 30.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None}
        ],
        "servings": 10,
        "preparation_time_minutes": 25,
        "cooking_time_minutes": 45,
        "instructions_mm": [
            "ဝက်သားကို တစ်လက်မအရွယ် လေးထောင့်တုံးလေးများ တုံးထားပါ။",
            "ကြက်သွန်နီ၊ ကြက်သွန်ဖြူနှင့် ချင်းတို့ကို ထောင်းကာ လေးထောင့်အဝတ်ပါးစတွင်ထည့်၍ အရည်ညှစ်ယူပါ။",
            "အိုးတစ်လုံးတွင် ဝက်သားတုံးများထည့်ပြီး ညှစ်ထားသော အရည်များ၊ ဆီနှင့် ဆား၊ သကြားများထည့်ကာ မီးအေးအေးဖြင့်ချက်ပါ။",
            "ဝက်သားနူးကာ နီချိန်တွင် ဝက်ဆီအဖတ်များကို ခြစ်ပါ။ ထောင်းထားသည့် အရည်ညှစ်ပြီး အမွှေးအကြိုင်များကို ရောစပ်ပါ။",
            "ဝက်သားများ ရွှေညိုရောင်သမ်းသည်အထိ ချက်ပြီးလျှင် တည်ခင်း၍ရပြီ ဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Cut the pork into 1-inch square cubes.",
            "Pound the onion, garlic, and ginger, place in a muslin cloth, and squeeze out all juice.",
            "In a pot, combine the pork cubes with the extracted aromatic juices, cooking oil, salt, and sugar; cook gently over low heat.",
            "As the pork becomes tender and takes on a reddish hue, scrape the rendered fat; stir in the reserved pounded aromatics.",
            "Cook until the pork cubes develop a deep golden-red caramelized glaze, then serve."
        ],
        "tags": {"dietary": ["dairy-free", "gluten-free"], "seasonal": ["all-season"], "festival": [], "main_ingredients": ["pork", "sugar"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [53], "printed_page_numbers": [94], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 94 (bottom). Unique aromatic juice extraction and two-stage browning technique.", "verified": True}
    },

    # R0041: ဝက်သားချိုချဉ်ကြော် (Sweet Sour Fried Pork)
    {
        "recipe_id": "R0041",
        "name_mm": "ဝက်သားချိုချဉ်ကြော်",
        "name_en": "Sweet and Sour Fried Pork",
        "description_mm": None,
        "description_en": None,
        "category": "Pork dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {"ingredient_id": "I0085", "name_mm": "ဝက်သား", "name_en": "Pork", "original_name": "ဝက်သား (အဆီမဲ့)", "quantity": 50.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၅၀ ကျပ်သား", "normalized_quantity": 816.5, "normalized_unit": "g", "preparation_note_mm": "အဆီမဲ့ အနားညီ ကုဗတုံးပုံ", "preparation_note_en": "lean, cut into even cubes"},
            {"ingredient_id": "I0050", "name_mm": "ပဲငံပြာရည်", "name_en": "Soy sauce", "original_name": "ပဲငံပြာရည်", "quantity": 2.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၂ စပဇ", "normalized_quantity": 30.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "original_name": "သကြား", "quantity": 2.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၂ လဖဇ", "normalized_quantity": 10.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0014", "name_mm": "ကြက်သွန်ဖြူ", "name_en": "Garlic", "original_name": "ကြက်သွန်ဖြူ (ထောင်းပြီး)", "quantity": 2.0, "unit": "မြွှာ (piece)", "original_quantity_text": "၂ မြွှာ", "normalized_quantity": 2.0, "normalized_unit": "piece", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0052", "name_mm": "သခွားသီး", "name_en": "Cucumber", "original_name": "သခွားသီး (အရွယ်လတ်)", "quantity": 1.0, "unit": "လုံး (piece)", "original_quantity_text": "၁ လုံး", "normalized_quantity": 1.0, "normalized_unit": "piece", "preparation_note_mm": "အံစာတုံးပုံစံ လှီး", "preparation_note_en": "diced into dice shapes"},
            {"ingredient_id": "I0049", "name_mm": "ရှာလကာရည်", "name_en": "Vinegar", "original_name": "ရှာလကာရည်", "quantity": 5.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၅ စပဇ", "normalized_quantity": 75.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "original_name": "သကြား", "quantity": 2.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၂ လဖဇ", "normalized_quantity": 10.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0013", "name_mm": "ဂျင်း", "name_en": "Ginger", "original_name": "ချင်း (၁\" နုပ်နုပ်စဉ်း)", "quantity": 1.0, "unit": "တုံး (piece)", "original_quantity_text": "၁ တုံး", "normalized_quantity": 1.0, "normalized_unit": "piece", "preparation_note_mm": "နုပ်နုပ်စဉ်း", "preparation_note_en": "finely minced"},
            {"ingredient_id": "I0051", "name_mm": "ဂျုံပြောင်းမှုန့်", "name_en": "Cornstarch", "original_name": "ပြောင်းကော်မှုန့်", "quantity": None, "unit": "လိုအပ်သရွေ့ (as needed)", "original_quantity_text": "လိုအပ်သရွေ့", "normalized_quantity": None, "normalized_unit": "g", "preparation_note_mm": "လူးရန်", "preparation_note_en": "for dredging"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "original_name": "ဆီ", "quantity": 5.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၅ စပဇ", "normalized_quantity": 75.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0049", "name_mm": "ရှာလကာရည်", "name_en": "Vinegar", "original_name": "ရှာလကာရည် (ဆော့စ်)", "quantity": 5.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၅ စပဇ", "normalized_quantity": 75.0, "normalized_unit": "g", "preparation_note_mm": "ဆော့စ်အတွက်", "preparation_note_en": "for sauce"},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "original_name": "သကြား (ဆော့စ်)", "quantity": 4.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၄ စပဇ", "normalized_quantity": 60.0, "normalized_unit": "g", "preparation_note_mm": "ဆော့စ်အတွက်", "preparation_note_en": "for sauce"},
            {"ingredient_id": "I0051", "name_mm": "ဂျုံပြောင်းမှုန့်", "name_en": "Cornstarch", "original_name": "ပြောင်းမှုန့် (ဆော့စ်)", "quantity": 3.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၃ စပဇ", "normalized_quantity": 45.0, "normalized_unit": "g", "preparation_note_mm": "ဆော့စ်အတွက်", "preparation_note_en": "for sauce"},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "original_name": "ရေနွေး", "quantity": 10.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၁၀ စပဇ", "normalized_quantity": 150.0, "normalized_unit": "g", "preparation_note_mm": "ရေနွေး", "preparation_note_en": "hot water"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "original_name": "ဆီ", "quantity": 2.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၂ လဖဇ", "normalized_quantity": 10.0, "normalized_unit": "g", "preparation_note_mm": "ဆော့စ်အတွက်", "preparation_note_en": "for sauce glaze"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 0.75, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၃/၄ စပဇ", "normalized_quantity": 11.25, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None}
        ],
        "servings": 10,
        "preparation_time_minutes": 60,
        "cooking_time_minutes": 15,
        "instructions_mm": [
            "ဝက်သားကို အနားညီ ကုဗတုံးပုံ လှီးပါ။ ခွက်တစ်ခုတွင် ဝက်သားတုံးများကို ပဲငံပြာရည်၊ သကြားနှင့် ကြက်သွန်ဖြူတို့ဖြင့် ရောစပ်ကာ (၁)နာရီခန့် စိမ်နှပ်ထားပါ။",
            "သခွားသီးကို အံစာတုံးပုံစံ လှီးကာ ရှာလကာရည်၊ သကြားနှင့် ချင်းတို့ဖြင့် ရောစပ်ကာ စိမ်ထားပါ။",
            "အသားတုံးများကို ပြောင်းကော်မှုန့်နှင့် လူးပြီး ဆီပူထဲတွင် ကျက်သည်အထိ ကြော်ပါ။ ဒယ်အိုး နှုတ်ခမ်းနားတွင် ဖယ်၍ထားပြီး သခွားသီးတုံးများထည့်ပြီး လျင်မြန်စွာမွှေကြော်ပါ။",
            "မွှေပြီးသည်နှင့်တစ်ပြိုင်နက် အိုးနှုတ်ခမ်းမှ အသားတုံးများကို ရောစပ်မွှေပြီး အသင့်ပြုလုပ်ထားသည့် ချိုချဉ်ဆော့စ်အရည်ဖြင့် ပေါင်းစပ်ကာ ဆူပွက်သည်အထိထားပါ။",
            "ဖိုမှချကာနီးအချိန်တွင် ဆီကို အပေါ်မှလောင်းဆမ်းကာ အသားများ ဆီရောင်တောက်အောင်လုပ်ပါ။ ပြီးလျှင် တည်ခင်း၍ရပြီဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Cut lean pork into uniform cubes; marinate with soy sauce, sugar, and garlic for 1 hour.",
            "Dice cucumber into cubes and pickle briefly with vinegar, sugar, and minced ginger.",
            "Dredge pork cubes in cornstarch and deep-fry until cooked and crispy; push to side of wok and flash-fry the pickled cucumber cubes.",
            "Combine pork and cucumber, pour over pre-mixed sweet and sour sauce (vinegar, sugar, cornstarch, hot water, salt), and bring to a bubbling glaze.",
            "Drizzle a little oil over the top right before dishing out to impart a brilliant sheen, then serve."
        ],
        "tags": {"dietary": ["dairy-free"], "seasonal": ["all-season"], "festival": [], "main_ingredients": ["pork", "cucumber", "vinegar"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [53], "printed_page_numbers": [95], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 95 (top). Quick cucumber pickle element and oil-glazing finish.", "verified": True}
    },

    # R0042: ဝက်သားဗင်ဒါလူ (Pork Vindaloo)
    {
        "recipe_id": "R0042",
        "name_mm": "ဝက်သားဗင်ဒါလူ",
        "name_en": "Pork Vindaloo",
        "description_mm": None,
        "description_en": None,
        "category": "Pork dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {"ingredient_id": "I0025", "name_mm": "ငရုတ်သီးမှုန့်", "name_en": "Chili powder", "original_name": "ငရုတ်သီးမှုန့်", "quantity": 5.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၅ လဖဇ", "normalized_quantity": 25.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0024", "name_mm": "နနွင်းမှုန့်", "name_en": "Turmeric powder", "original_name": "နနွင်းမှုန့်", "quantity": 2.5, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၂ ၁/၂ လဖဇ", "normalized_quantity": 12.5, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0055", "name_mm": "ဇီယာ", "name_en": "Cumin seeds", "original_name": "ဇီယာစေ့", "quantity": 5.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၅ လဖဇ", "normalized_quantity": 25.0, "normalized_unit": "g", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0062", "name_mm": "မုန်ညင်းစေ့", "name_en": "Mustard seeds", "original_name": "မုန်ညင်းစေ့", "quantity": 5.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၅ လဖဇ", "normalized_quantity": 25.0, "normalized_unit": "g", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0054", "name_mm": "နံနံစေ့", "name_en": "Coriander seeds", "original_name": "နံနံစေ့", "quantity": 5.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၅ စပဇ", "normalized_quantity": 75.0, "normalized_unit": "g", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0013", "name_mm": "ဂျင်း", "name_en": "Ginger", "original_name": "ချင်း ၂\" (နုပ်နုပ်စဉ်း)", "quantity": 1.0, "unit": "တုံး (piece)", "original_quantity_text": "၁ တုံး", "normalized_quantity": 1.0, "normalized_unit": "piece", "preparation_note_mm": "နုပ်နုပ်စဉ်း", "preparation_note_en": "finely minced"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 3.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၃ လဖဇ", "normalized_quantity": 15.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0049", "name_mm": "ရှာလကာရည်", "name_en": "Vinegar", "original_name": "ရှာလကာရည်", "quantity": 1.0, "unit": "ခွက် (cup / g)", "original_quantity_text": "၁ ခွက်", "normalized_quantity": 240.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "original_name": "ကြက်သွန်နီ (နုပ်နုပ်စဉ်း)", "quantity": 2.0, "unit": "လုံး (piece)", "original_quantity_text": "၂ လုံး", "normalized_quantity": 2.0, "normalized_unit": "piece", "preparation_note_mm": "နုပ်နုပ်စဉ်း", "preparation_note_en": "finely minced"},
            {"ingredient_id": "I0014", "name_mm": "ကြက်သွန်ဖြူ", "name_en": "Garlic", "original_name": "ကြက်သွန်ဖြူ (ဓားပြားရိုက်)", "quantity": 5.0, "unit": "မြွှာ (piece)", "original_quantity_text": "၅ မြွှာ", "normalized_quantity": 5.0, "normalized_unit": "piece", "preparation_note_mm": "ဓားပြားရိုက်", "preparation_note_en": "crushed"},
            {"ingredient_id": "I0085", "name_mm": "ဝက်သား", "name_en": "Pork", "original_name": "ဝက်သား (အဆီမဲ့)", "quantity": 1.0, "unit": "ပိဿာ (kg)", "original_quantity_text": "၁ ပိဿာ", "normalized_quantity": 1632.9, "normalized_unit": "g", "preparation_note_mm": "အဆီမဲ့ တုံးပြီး", "preparation_note_en": "lean, cubed"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "original_name": "ဆီ", "quantity": 10.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၁၀ ကျပ်သား", "normalized_quantity": 163.3, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None}
        ],
        "servings": 10,
        "preparation_time_minutes": 480, # overnight marinating
        "cooking_time_minutes": 45,
        "instructions_mm": [
            "ညက်အောင် ထောင်းထားပြီးဖြစ်သော အမွှေးအကြိုင်များကို ဆားနှင့် ရှာလကာရည်တို့ဖြင့် ရောစပ်မွှေပါ။",
            "ဇလုံတစ်ခုလုံးထဲသို့ ကြက်သွန်နီ၊ ကြက်သွန်ဖြူနှင့် တုံးပြီးဝက်သားများ ထည့်ပြီး အထက်က ရောစပ်မွှေထားသည်များကို ပေါင်းစပ်ကာ မွှေပြီးနောက် အဖုံးအုပ်၍ ရေခဲသေတ္တာထဲတွင် (သို့) အေးသောနေရာတွင် တစ်ညခန့်ထားပါ။",
            "ဒယ်အိုးသို့ ဆီထည့်ကာ အပူပေးပြီး တစ်ညသိပ်ထားသော ဝက်သားအရောများကို ထည့်ကာ မီးအေးအေးနှင့် (၄၅)မိနစ် (သို့) အသားနူးသည်အထိ ချက်ပါ။",
            "ပြီးလျှင် တည်ခင်း၍ရပြီဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Blend the finely pounded spices (cumin, mustard seeds, coriander) with chili powder, turmeric, salt, and vinegar into a rich vindaloo paste.",
            "In a large bowl, combine diced lean pork, minced onions, and crushed garlic with the vindaloo paste; mix thoroughly, cover, and marinate overnight in a cold place.",
            "Heat oil in a heavy pot, add the overnight-marinated pork along with all seasonings, and simmer gently over low heat for 45 minutes or until the pork is meltingly tender.",
            "Remove from heat and serve hot with rice."
        ],
        "tags": {"dietary": ["dairy-free", "gluten-free"], "seasonal": ["all-season"], "festival": [], "main_ingredients": ["pork", "vinegar", "mustard seed"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [53], "printed_page_numbers": [95], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 95 (bottom). Authentic overnight vinegar spice marinade vindaloo.", "verified": True}
    }
]
