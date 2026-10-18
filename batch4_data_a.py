# -*- coding: utf-8 -*-
"""
Batch 4 Part A: Recipes R0021 - R0031 (Duck and Mutton curries)
"""

recipes_a = [
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
            {"ingredient_id": "I0057", "name_mm": "ဘဲသား", "name_en": "Duck meat", "original_name": "ဘဲသား", "quantity": 80.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၈၀ ကျပ်သား", "normalized_quantity": 1306.3, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 3.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၃ လဖဇ", "normalized_quantity": 15.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0050", "name_mm": "ပဲငံပြာရည်", "name_en": "Soy sauce", "original_name": "ပဲငံပြာရည် (အကြည်)", "quantity": 3.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၃ လဖဇ", "normalized_quantity": 15.0, "normalized_unit": "g", "preparation_note_mm": "အကြည်", "preparation_note_en": "light"},
            {"ingredient_id": "I0050", "name_mm": "ပဲငံပြာရည်", "name_en": "Soy sauce", "original_name": "ပဲငံပြာရည် (အနောက်)", "quantity": 1.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁ လဖဇ", "normalized_quantity": 5.0, "normalized_unit": "g", "preparation_note_mm": "အနောက်", "preparation_note_en": "dark"},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "original_name": "သကြား", "quantity": 2.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၂ လဖဇ", "normalized_quantity": 10.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0041", "name_mm": "ငရုတ်သီးခြောက်", "name_en": "Dried red chili", "original_name": "ငရုတ်သီးခြောက်", "quantity": 6.0, "unit": "တောင့် (piece)", "original_quantity_text": "၆ တောင့်", "normalized_quantity": 6.0, "normalized_unit": "piece", "preparation_note_mm": "ထောင်းထားသော", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "original_name": "ကြက်သွန်နီ (အလတ်)", "quantity": 4.0, "unit": "လုံး (piece)", "original_quantity_text": "၄ လုံး", "normalized_quantity": 4.0, "normalized_unit": "piece", "preparation_note_mm": "ထောင်းထားသော", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0014", "name_mm": "ကြက်သွန်ဖြူ", "name_en": "Garlic", "original_name": "ကြက်သွန်ဖြူ", "quantity": 5.0, "unit": "မြွှာ (piece)", "original_quantity_text": "၅ မြွှာ", "normalized_quantity": 5.0, "normalized_unit": "piece", "preparation_note_mm": "ထောင်းထားသော", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0013", "name_mm": "ဂျင်း", "name_en": "Ginger", "original_name": "ချင်း", "quantity": 1.0, "unit": "လက်မ (piece)", "original_quantity_text": "၁ လက်မ", "normalized_quantity": 1.0, "normalized_unit": "piece", "preparation_note_mm": "ထောင်းထားသော", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "original_name": "ဆီ", "quantity": 10.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၁၀ ကျပ်သား", "normalized_quantity": 163.3, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "original_name": "ရေနွေး", "quantity": None, "unit": "အနည်းငယ် (g)", "original_quantity_text": "အနည်းငယ်", "normalized_quantity": None, "normalized_unit": "g", "preparation_note_mm": "ရေနွေး", "preparation_note_en": "hot water"}
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
        "tags": {"dietary": ["dairy-free"], "seasonal": ["all-season"], "festival": [], "main_ingredients": ["duck"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [48], "printed_page_numbers": [85], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 85 (top). Classic duck oil-return curry.", "verified": True}
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
            {"ingredient_id": "I0057", "name_mm": "ဘဲသား", "name_en": "Duck meat", "original_name": "ဘဲအကောင်လိုက် (ခပ်ဝဝ)", "quantity": 1.0, "unit": "ပိဿာ (kg)", "original_quantity_text": "၁ ပိဿာ", "normalized_quantity": 1632.9, "normalized_unit": "g", "preparation_note_mm": "အကောင်လိုက် (ခပ်ဝဝ)", "preparation_note_en": "whole plump duck"},
            {"ingredient_id": "I0058", "name_mm": "ကြက်သွန်မြိတ်", "name_en": "Spring onion", "original_name": "ကြက်သွန်မြိတ်", "quantity": 1.0, "unit": "ပင် (piece)", "original_quantity_text": "၁ ပင်", "normalized_quantity": 1.0, "normalized_unit": "piece", "preparation_note_mm": "၁ လက်မအရှည်ဖြတ်ထားသော", "preparation_note_en": "cut into 1-inch lengths"},
            {"ingredient_id": "I0009", "name_mm": "လေးညှင်းပွင့်", "name_en": "Clove", "original_name": "လေးညှင်း", "quantity": 20.0, "unit": "ပွင့် (piece)", "original_quantity_text": "၂၀ ပွင့်", "normalized_quantity": 20.0, "normalized_unit": "piece", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0013", "name_mm": "ဂျင်း", "name_en": "Ginger", "original_name": "ချင်း", "quantity": 4.0, "unit": "လွှာ (piece)", "original_quantity_text": "၄ လွှာ", "normalized_quantity": 4.0, "normalized_unit": "piece", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0008", "name_mm": "သစ်ကြံပိုးခေါက်", "name_en": "Cinnamon", "original_name": "သစ်ကြံပိုး (၁\" ရှည်)", "quantity": 3.0, "unit": "ခု (piece)", "original_quantity_text": "၃ ခု", "normalized_quantity": 3.0, "normalized_unit": "piece", "preparation_note_mm": "၁\" ရှည်", "preparation_note_en": "1-inch length"},
            {"ingredient_id": "I0059", "name_mm": "စမုန်ပွင့်", "name_en": "Star anise", "original_name": "စမုန်ပွင့်", "quantity": 4.0, "unit": "ပွင့် (piece)", "original_quantity_text": "၄ ပွင့်", "normalized_quantity": 4.0, "normalized_unit": "piece", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0060", "name_mm": "ရှယ်ရီအရက်", "name_en": "Cooking wine", "original_name": "ရှယ်ရီအရက်", "quantity": 3.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၃ စပဇ", "normalized_quantity": 45.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0061", "name_mm": "ပဲငါးပိရည်", "name_en": "Fermented soybean sauce", "original_name": "ပဲငါးပိရည်", "quantity": 5.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၅ စပဇ", "normalized_quantity": 75.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 2.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၂ လဖဇ", "normalized_quantity": 10.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "original_name": "မြုပ်အောင်ကြော်ရန်ဆီ လိုအပ်သရွေ့", "quantity": None, "unit": "လိုအပ်သရွေ့ (as needed)", "original_quantity_text": "မြုပ်အောင်ကြော်ရန်ဆီ လိုအပ်သရွေ့", "normalized_quantity": None, "normalized_unit": "g", "preparation_note_mm": "မြုပ်အောင်ကြော်ရန်", "preparation_note_en": "for deep frying"}
        ],
        "servings": 10,
        "preparation_time_minutes": 180,
        "cooking_time_minutes": 170,
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
        "tags": {"dietary": ["dairy-free"], "seasonal": ["all-season"], "festival": ["Chinese New Year"], "main_ingredients": ["duck"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [48], "printed_page_numbers": [85], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 85 (bottom). 2.5-hour steam then deep fry.", "verified": True}
    },

    # R0023: ဘဲသားအာလူးချက် (Duck and Potato Curry)
    {
        "recipe_id": "R0023",
        "name_mm": "ဘဲသားအာလူးချက်",
        "name_en": "Duck and Potato Curry",
        "description_mm": None,
        "description_en": None,
        "category": "Poultry dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {"ingredient_id": "I0057", "name_mm": "ဘဲသား", "name_en": "Duck meat", "original_name": "ဘဲသား", "quantity": 70.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၇၀ ကျပ်သား", "normalized_quantity": 1143.1, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 1.5, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁ ၁/၂ လဖဇ", "normalized_quantity": 7.5, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0050", "name_mm": "ပဲငံပြာရည်", "name_en": "Soy sauce", "original_name": "ပဲငံပြာရည် (အကြည်)", "quantity": 2.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၂ စပဇ", "normalized_quantity": 30.0, "normalized_unit": "g", "preparation_note_mm": "အကြည်", "preparation_note_en": "light"},
            {"ingredient_id": "I0050", "name_mm": "ပဲငံပြာရည်", "name_en": "Soy sauce", "original_name": "ပဲငံပြာရည် (အနောက်)", "quantity": 1.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၁ စပဇ", "normalized_quantity": 15.0, "normalized_unit": "g", "preparation_note_mm": "အနောက်", "preparation_note_en": "dark"},
            {"ingredient_id": "I0041", "name_mm": "ငရုတ်သီးခြောက်", "name_en": "Dried red chili", "original_name": "ငရုတ်သီးခြောက် (ထောင်းပြီး)", "quantity": 5.0, "unit": "တောင့် (piece)", "original_quantity_text": "၅ တောင့်", "normalized_quantity": 5.0, "normalized_unit": "piece", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0013", "name_mm": "ဂျင်း", "name_en": "Ginger", "original_name": "ချင်း (ထောင်းပြီး)", "quantity": 1.0, "unit": "လက်မ (piece)", "original_quantity_text": "၁ လက်မ", "normalized_quantity": 1.0, "normalized_unit": "piece", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "original_name": "ကြက်သွန်နီ (ထောင်းပြီး)", "quantity": 5.0, "unit": "လုံး (piece)", "original_quantity_text": "၅ လုံး", "normalized_quantity": 5.0, "normalized_unit": "piece", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0014", "name_mm": "ကြက်သွန်ဖြူ", "name_en": "Garlic", "original_name": "ကြက်သွန်ဖြူ (ထောင်းပြီး)", "quantity": 2.0, "unit": "မြွှာ (piece)", "original_quantity_text": "၂ မြွှာ", "normalized_quantity": 2.0, "normalized_unit": "piece", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "original_name": "ဆီ", "quantity": 10.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၁၀ ကျပ်သား", "normalized_quantity": 163.3, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "original_name": "ရေနွေး", "quantity": 1.0, "unit": "နို့ဆီဘူး (g)", "original_quantity_text": "၁ နို့ဆီဘူး", "normalized_quantity": 300.0, "normalized_unit": "g", "preparation_note_mm": "ရေနွေး", "preparation_note_en": "hot water"},
            {"ingredient_id": "I0020", "name_mm": "အာလူး", "name_en": "Potato", "original_name": "အာလူး (လေးစိတ်စိတ်)", "quantity": 30.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၃၀ ကျပ်သား", "normalized_quantity": 489.9, "normalized_unit": "g", "preparation_note_mm": "လေးစိတ်စိတ်", "preparation_note_en": "quartered"},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "original_name": "ရေနွေး", "quantity": 1.0, "unit": "နို့ဆီဘူး (g)", "original_quantity_text": "၁ နို့ဆီဘူး", "normalized_quantity": 300.0, "normalized_unit": "g", "preparation_note_mm": "ရေနွေး", "preparation_note_en": "hot water"},
            {"ingredient_id": "I0012", "name_mm": "မဆလာ", "name_en": "Garam masala", "original_name": "မဆလာ", "quantity": 1.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁ လဖဇ", "normalized_quantity": 5.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None}
        ],
        "servings": 10,
        "preparation_time_minutes": 20,
        "cooking_time_minutes": 50,
        "instructions_mm": [
            "အနေတော်အရွယ် တုံးထားသည့် ဘဲသားများကို ဆား၊ ပဲငံပြာရည်တို့ဖြင့် နယ်ထားပါ။",
            "အိုးတစ်လုံးတွင် နယ်ပြီးဘဲသား၊ ထောင်းပြီးအမွှေးအကြိုင်များနှင့် ဆီကို ရောထည့်ပြီး နယ်သားကျအောင် နယ်ကာ ရေနွေးထည့်ပါ။",
            "အဖုံးအုပ်၍ မီးအေးအေးဖြင့်တည်ပါ။ ရေခမ်း၍ အနံ့သင်းလာလျှင် အသားနူးမနူး ကြည့်ပါ။ မနူးသေးလျှင် ရေနွေးထပ်ထည့်ချက်ပါ။",
            "ရေခမ်း၍ အသားနူးကာနီးလျှင် အာလူးထည့်ကာ မွှေပေးပါ။ ရေနွေးထည့်ပါ။ အဖုံးအုပ်ချက်ပါ။",
            "ဆီပြန်ကာနီးလျှင် မဆလာမှုန့်ဖြူးပြီး အဖုံးပြန်အုပ်ထားပါ။ အာလူးနပ်၍ဆီပြန်လျှင် တည်ခင်း၍ရပြီဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Marinate medium-sized duck pieces with salt and soy sauces.",
            "In a pot, combine marinated duck, pounded aromatics, cooking oil, and hot water, mixing thoroughly.",
            "Cover and simmer over low heat; when water reduces and fragrant steam rises, test for tenderness, adding more hot water if needed.",
            "When duck is nearly tender and liquid reduces, add quartered potatoes, stir well, add remaining hot water, cover, and cook.",
            "Just before the oil returns, sprinkle garam masala over top, cover to rest, and serve once potatoes are fully tender and oil floats."
        ],
        "tags": {"dietary": ["dairy-free"], "seasonal": ["all-season"], "festival": [], "main_ingredients": ["duck", "potato"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [49], "printed_page_numbers": [86], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 86 (top). Hearty duck and potato stew.", "verified": True}
    },

    # R0024: ဘဲသားဗင်ဒါလူ (Duck Vindaloo)
    {
        "recipe_id": "R0024",
        "name_mm": "ဘဲသားဗင်ဒါလူ",
        "name_en": "Duck Vindaloo",
        "description_mm": None,
        "description_en": None,
        "category": "Poultry dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {"ingredient_id": "I0057", "name_mm": "ဘဲသား", "name_en": "Duck meat", "original_name": "ဘဲသား", "quantity": 80.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၈၀ ကျပ်သား", "normalized_quantity": 1306.3, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0055", "name_mm": "ဇီယာ", "name_en": "Cumin seeds", "original_name": "ဇီယာ", "quantity": 1.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၁ စပဇ", "normalized_quantity": 15.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0062", "name_mm": "မုန်ညင်းစေ့", "name_en": "Mustard seeds", "original_name": "မုန်ညင်းစေ့", "quantity": 0.5, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၁/၂ စပဇ", "normalized_quantity": 7.5, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0024", "name_mm": "နနွင်းမှုန့်", "name_en": "Turmeric powder", "original_name": "နနွင်းမှုန့်", "quantity": 1.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁ လဖဇ", "normalized_quantity": 5.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "original_name": "ကြက်သွန်နီ (ပါးပါးလှီး)", "quantity": 2.0, "unit": "လုံး (piece)", "original_quantity_text": "၂ လုံး", "normalized_quantity": 2.0, "normalized_unit": "piece", "preparation_note_mm": "ပါးပါးလှီး", "preparation_note_en": "thinly sliced"},
            {"ingredient_id": "I0013", "name_mm": "ဂျင်း", "name_en": "Ginger", "original_name": "ချင်း", "quantity": 2.0, "unit": "လက်မ (piece)", "original_quantity_text": "၂ လက်မ", "normalized_quantity": 2.0, "normalized_unit": "piece", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0014", "name_mm": "ကြက်သွန်ဖြူ", "name_en": "Garlic", "original_name": "ကြက်သွန်ဖြူ", "quantity": 6.0, "unit": "မြွှာ (piece)", "original_quantity_text": "၆ မြွှာ", "normalized_quantity": 6.0, "normalized_unit": "piece", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0041", "name_mm": "ငရုတ်သီးခြောက်", "name_en": "Dried red chili", "original_name": "ငရုတ်သီးခြောက် (ထောင်းပြီး)", "quantity": 8.0, "unit": "တောင့် (piece)", "original_quantity_text": "၈ တောင့်", "normalized_quantity": 8.0, "normalized_unit": "piece", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "original_name": "ဆီ", "quantity": 0.75, "unit": "ခွက် (cup / g)", "original_quantity_text": "၃/၄ ခွက်", "normalized_quantity": 180.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "original_name": "သကြား", "quantity": 2.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၂ လဖဇ", "normalized_quantity": 10.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0049", "name_mm": "ရှာလကာရည်", "name_en": "Vinegar", "original_name": "ရှာလကာရည်", "quantity": 3.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၃ စပဇ", "normalized_quantity": 45.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 1.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁ လဖဇ", "normalized_quantity": 5.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0042", "name_mm": "ခရမ်းချဉ်သီး", "name_en": "Tomato", "original_name": "ခရမ်းချဉ်သီးမှည့် (လှီးပြီး)", "quantity": 4.0, "unit": "လုံး (piece)", "original_quantity_text": "၄ လုံး", "normalized_quantity": 4.0, "normalized_unit": "piece", "preparation_note_mm": "လှီးပြီး", "preparation_note_en": "sliced"}
        ],
        "servings": 10,
        "preparation_time_minutes": 25,
        "cooking_time_minutes": 50,
        "instructions_mm": [
            "ဘဲသားကို အတုံးကြီးတုံးပါ။ ငရုတ်သီး၊ ကြက်သွန်နီနှင့် ခရမ်းချဉ်သီးမှလွဲ၍ အားလုံးကို အနှစ်ကဲ့သို့ လုပ်ထားပါ။",
            "ဆီပူတွင် ကြက်သွန်နီကို ထည့်မွှေပါ။ မကျက်တကျက်အချိန်တွင် ငရုတ်သီး ထည့်မွှေကာ နီရောင်သမ်းအောင် လုပ်ပါ။",
            "ကျန်အနှစ်လုပ်ထားသောအရာများကို ထည့်၍ ကြော်ပါ။ ဘဲသားကိုပါထည့်၍ ညိုလာသည်အထိထားပါ။",
            "ရေနွေး (၁)ခွက်ထည့်၍ အဖုံးအုပ်ကာ ဆူအောင်တည်ပါ။",
            "အသားနူးပြီး ဆူပွက်ပြီးလျှင် ရှာလကာရည်၊ သကြား၊ ခရမ်းချဉ်သီးနှင့် ဆားတို့ကို ထည့်ပြီး ဟင်းအိုးကို ဖြည်းဖြည်းဆူစေကာ အသားနူးပြီး ဟင်းအိုးမျက်နှာပြင်တွင် ဆီပြန်လာလျှင် တည်ခင်း၍ရပြီ ဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Cut the duck into large chunks; blend cumin, mustard seeds, turmeric, ginger, and garlic into a thick paste.",
            "In hot oil, sauté sliced onions; when half-cooked, stir in the chili to develop a deep red hue.",
            "Add the ground spice paste and fry; then add duck chunks and sear until nicely browned.",
            "Pour in 1 cup of hot water, cover, and bring to a simmer.",
            "Once simmering and duck softens, add vinegar, sugar, sliced tomatoes, and salt; simmer gently until duck is succulent and aromatic oil separates."
        ],
        "tags": {"dietary": ["dairy-free", "gluten-free"], "seasonal": ["all-season"], "festival": [], "main_ingredients": ["duck", "vinegar"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [49], "printed_page_numbers": [86], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 86 (bottom). Classic Anglo-Indian inspired vindaloo.", "verified": True}
    },

    # R0025: ဘဲသားနာနတ်သီး (Fried Duck with Pineapple)
    {
        "recipe_id": "R0025",
        "name_mm": "ဘဲသားနာနတ်သီး",
        "name_en": "Fried Duck with Pineapple",
        "description_mm": None,
        "description_en": None,
        "category": "Poultry dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {"ingredient_id": "I0057", "name_mm": "ဘဲသား", "name_en": "Duck meat", "original_name": "ဘဲကောင်", "quantity": 80.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၈၀ ကျပ်သား", "normalized_quantity": 1306.3, "normalized_unit": "g", "preparation_note_mm": "အရိုးထုတ်ပြီး ပါးပါးလွှာ", "preparation_note_en": "deboned and thinly sliced"},
            {"ingredient_id": "I0063", "name_mm": "ကော်မှုန့်", "name_en": "Tapioca / starch flour", "original_name": "ကော်မှုန့်", "quantity": 5.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၅ စပဇ", "normalized_quantity": 75.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0026", "name_mm": "ကြက်ဥ", "name_en": "Chicken egg", "original_name": "ကြက်ဥ", "quantity": 3.0, "unit": "လုံး (piece)", "original_quantity_text": "၃ လုံး", "normalized_quantity": 3.0, "normalized_unit": "piece", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0046", "name_mm": "နာနတ်သီး", "name_en": "Pineapple", "original_name": "နာနတ်သီး (အခွံခွာ)", "quantity": 10.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၁၀ ကျပ်သား", "normalized_quantity": 163.3, "normalized_unit": "g", "preparation_note_mm": "လက်တစ်လုံးခန့်လှီး", "preparation_note_en": "cut into finger-sized pieces"},
            {"ingredient_id": "I0014", "name_mm": "ကြက်သွန်ဖြူ", "name_en": "Garlic", "original_name": "ကြက်သွန်ဖြူ (အခွံခွာ)", "quantity": 5.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၅ ကျပ်သား", "normalized_quantity": 81.6, "normalized_unit": "g", "preparation_note_mm": "ဓားပြားရိုက်", "preparation_note_en": "crushed"},
            {"ingredient_id": "I0013", "name_mm": "ဂျင်း", "name_en": "Ginger", "original_name": "ချင်း (အခွံခွာ)", "quantity": 2.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၂ ကျပ်သား", "normalized_quantity": 32.7, "normalized_unit": "g", "preparation_note_mm": "ဓားပြားရိုက်", "preparation_note_en": "crushed"},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "original_name": "ကြက်သွန်နီ", "quantity": 2.0, "unit": "လုံး (piece)", "original_quantity_text": "၂ လုံး", "normalized_quantity": 2.0, "normalized_unit": "piece", "preparation_note_mm": "ရှစ်စိတ်စိတ်", "preparation_note_en": "cut into 8 wedges"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "original_name": "ဆီ", "quantity": 15.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၁၅ ကျပ်သား", "normalized_quantity": 245.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0050", "name_mm": "ပဲငံပြာရည်", "name_en": "Soy sauce", "original_name": "ပဲငံပြာရည်အကြည်", "quantity": 1.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၁ စပဇ", "normalized_quantity": 15.0, "normalized_unit": "g", "preparation_note_mm": "အကြည်", "preparation_note_en": "light"},
            {"ingredient_id": "I0050", "name_mm": "ပဲငံပြာရည်", "name_en": "Soy sauce", "original_name": "ပဲငံပြာရည်အနောက်", "quantity": 1.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁ လဖဇ", "normalized_quantity": 5.0, "normalized_unit": "g", "preparation_note_mm": "အနောက်", "preparation_note_en": "dark"},
            {"ingredient_id": "I0063", "name_mm": "ကော်မှုန့်", "name_en": "Tapioca / starch flour", "original_name": "ကော်မှုန့်", "quantity": 2.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၂ စပဇ", "normalized_quantity": 30.0, "normalized_unit": "g", "preparation_note_mm": "ကော်ရည်ဖျော်ရန်", "preparation_note_en": "for slurry"},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "original_name": "ရေ", "quantity": 2.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၂ စပဇ", "normalized_quantity": 30.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 1.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁ လဖဇ", "normalized_quantity": 5.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "original_name": "သကြား", "quantity": 1.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၁ စပဇ", "normalized_quantity": 15.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0058", "name_mm": "ကြက်သွန်မြိတ်", "name_en": "Spring onion", "original_name": "ကြက်သွန်မြိတ်", "quantity": 4.0, "unit": "ပင် (piece)", "original_quantity_text": "၄ ပင်", "normalized_quantity": 4.0, "normalized_unit": "piece", "preparation_note_mm": "၁ လက်မခွဲခန့် အစောင်းလှီး", "preparation_note_en": "cut diagonally into 1.5-inch pieces"}
        ],
        "servings": 10,
        "preparation_time_minutes": 25,
        "cooking_time_minutes": 15,
        "instructions_mm": [
            "ဘဲသားကို အရိုးထုတ်ပြီး ဓားနှင့် ပါးပါးလွှာ၍ ဆား၊ ကော်မှုန့်၊ ကြက်ဥတို့ဖြင့် နှံ့အောင်နယ်ပါ။",
            "နာနတ်သီးကို လက်တစ်လုံးခန့်လှီးပါ။ ကြက်သွန်ဖြူ၊ ချင်းတို့ကို ဓားပြားရိုက်ပါ။ ကြက်သွန်နီကို ရှစ်စိတ်စိတ်ပါ။ ကြက်သွန်မြိတ်ကို အရှည် ၁ လက်မခွဲခန့် အစောင်းကလေးဖြစ်အောင် လှီးပါ။",
            "ဒယ်အိုးတွင် ဆီထည့်၍ အပူပေးပါ။ ကျက်လျှင် ကြက်သွန်နီနှင့် ဘဲသားထည့်မွှေပါ။ ခေတ္တမွှေပြီးနောက် ဆယ်ယူဆီစစ်ထားပါ။",
            "ကျန်ဆီတွင် ဆီထပ်ထည့်ပြီး ချင်း၊ ကြက်သွန်ဖြူ ဆီသတ်ပါ။ ဘဲသား၊ ကြက်သွန်နီ၊ နာနတ်သီး၊ ပဲငံပြာရည်အကြည်၊ ပဲငံပြာရည်အနောက်၊ ကော်ရည်၊ ဆား၊ သကြား၊ ကြက်သွန်မြိတ်ထည့်ပြီး ရောစပ်မွှေပါ။",
            "(၁)မိနစ်မျှ မွှေနောက်လျှင် တည်ခင်း၍ရပြီ ဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Debone the duck, slice thinly, and coat thoroughly with salt, starch, and beaten egg.",
            "Cut pineapple into finger-sized pieces, crush garlic and ginger, cut onions into 8 wedges, and slice spring onions diagonally into 1.5-inch segments.",
            "Heat oil in a wok; stir-fry onions and velveted duck slices briefly, then drain.",
            "Add remaining oil to wok and sauté ginger and garlic; return duck, onions, pineapple, soy sauces, cornstarch slurry, salt, sugar, and spring onions, tossing briskly.",
            "Stir-fry for 1 minute until sauce glazes the ingredients, then serve immediately."
        ],
        "tags": {"dietary": ["dairy-free"], "seasonal": ["all-season"], "festival": [], "main_ingredients": ["duck", "pineapple"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [49], "printed_page_numbers": [87], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 87 (top). Chinese velveting technique used on duck.", "verified": True}
    },

    # R0026: ဘဲမြစ်ချိုချဉ်မွှေကြော် (Stir-Fried Sweet and Sour Duck Gizzards)
    {
        "recipe_id": "R0026",
        "name_mm": "ဘဲမြစ်ချိုချဉ်မွှေကြော်",
        "name_en": "Stir-Fried Sweet and Sour Duck Gizzards",
        "description_mm": None,
        "description_en": None,
        "category": "Poultry dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {"ingredient_id": "I0064", "name_mm": "ဘဲမြစ်", "name_en": "Duck gizzard", "original_name": "ဘဲအမြစ်", "quantity": 6.0, "unit": "ခု (piece)", "original_quantity_text": "၆ ခု", "normalized_quantity": 6.0, "normalized_unit": "piece", "preparation_note_mm": "သန့်စင်မွှမ်းထားသော", "preparation_note_en": "cleaned and cross-scored"},
            {"ingredient_id": "I0060", "name_mm": "ရှယ်ရီအရက်", "name_en": "Cooking wine", "original_name": "အရက်", "quantity": 1.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၁ စပဇ", "normalized_quantity": 15.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0065", "name_mm": "ငရုတ်စိမ်းပွ", "name_en": "Green bell pepper", "original_name": "ငရုတ်စိမ်းပွ", "quantity": 1.0, "unit": "တောင့် (piece)", "original_quantity_text": "၁ တောင့်", "normalized_quantity": 1.0, "normalized_unit": "piece", "preparation_note_mm": "အစေ့ထုတ် လှီးထားသော", "preparation_note_en": "seeded and diced"},
            {"ingredient_id": "I0046", "name_mm": "နာနတ်သီး", "name_en": "Pineapple", "original_name": "နာနတ်သီးကွင်း (ပါးပါးလှီးပြီး)", "quantity": 1.0, "unit": "ခွက် (cup / g)", "original_quantity_text": "၁ ခွက်", "normalized_quantity": 240.0, "normalized_unit": "g", "preparation_note_mm": "ပါးပါးလှီးပြီး", "preparation_note_en": "thinly sliced rings"},
            {"ingredient_id": "I0066", "name_mm": "ကြက်ဆီ", "name_en": "Chicken fat", "original_name": "ကြက်ဆီ", "quantity": 0.8, "unit": "နို့ဆီဘူး (g)", "original_quantity_text": "၄/၅ နို့ဆီဘူး", "normalized_quantity": 240.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0058", "name_mm": "ကြက်သွန်မြိတ်", "name_en": "Spring onion", "original_name": "ကြက်သွန်မြိတ် (၁\")", "quantity": 6.0, "unit": "ခု (piece)", "original_quantity_text": "၆ ခု", "normalized_quantity": 6.0, "normalized_unit": "piece", "preparation_note_mm": "၁\" အပိုင်း", "preparation_note_en": "1-inch sections"},
            {"ingredient_id": "I0041", "name_mm": "ငရုတ်သီးခြောက်", "name_en": "Dried red chili", "original_name": "ငရုတ်သီးမှည့် (ပါးပါးလှီးပြီး)", "quantity": 1.0, "unit": "တောင့် (piece)", "original_quantity_text": "၁ တောင့်", "normalized_quantity": 1.0, "normalized_unit": "piece", "preparation_note_mm": "ပါးပါးလှီးပြီး", "preparation_note_en": "thinly sliced ripe red chili"},
            {"ingredient_id": "I0013", "name_mm": "ဂျင်း", "name_en": "Ginger", "original_name": "ချင်း (၁\")", "quantity": 0.5, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၁/၂ စပဇ", "normalized_quantity": 7.5, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "original_name": "သကြား", "quantity": 2.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၂ စပဇ", "normalized_quantity": 30.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0049", "name_mm": "ရှာလကာရည်", "name_en": "Vinegar", "original_name": "ရှာလကာရည်", "quantity": 2.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၂ စပဇ", "normalized_quantity": 30.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0045", "name_mm": "ခရမ်းချဉ်သီးကက်ချပ်", "name_en": "Tomato ketchup", "original_name": "ခရမ်းချဉ်သီးကက်ချပ်", "quantity": 2.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၂ စပဇ", "normalized_quantity": 30.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "original_name": "ရေ", "quantity": 2.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၂ စပဇ", "normalized_quantity": 30.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 1.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁ လဖဇ", "normalized_quantity": 5.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0067", "name_mm": "နှမ်းဆီ", "name_en": "Sesame oil", "original_name": "နှမ်းဆီ", "quantity": 1.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁ လဖဇ", "normalized_quantity": 5.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0051", "name_mm": "ဂျုံပြောင်းမှုန့်", "name_en": "Cornstarch", "original_name": "ပြောင်းကော်မှုန့်", "quantity": 2.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၂ စပဇ", "normalized_quantity": 30.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None}
        ],
        "servings": 10,
        "preparation_time_minutes": 25,
        "cooking_time_minutes": 10,
        "instructions_mm": [
            "ဘဲမြစ်ကို အပေါ်ယံရှိ အဖြူအမြှေးများ ဖယ်ရှားသန့်စင်ပြီး လေးပိုင်းပိုင်းကာ အလျားလိုက်နှင့် ကန့်လန့်ဖြတ်မွှမ်းပါ။ ရေအေးဖြင့် နှစ်ခေါက်ဆေးပါ။ အရက်နှင့်ရော၍ မိနစ်(၂၀) စိမ်ထားပါ။",
            "ငရုတ်သီးစိမ်းပွကို အစေ့ထုတ်၍ တစ်ကိုက်စာအရွယ် လှီးထားပါ။ နာနတ်သီးလွှာများကို ဆား ၁/၂ စားပွဲဇွန်းရောကာ မိနစ်(၂၀)ထား၍ အရည်များထွက်အောင် အသာအယာညှစ်ပြီး စစ်ထားပါ။",
            "ဆီပူတွင် အမြစ်နှင့် ငရုတ်သီးစိမ်းထည့်၍ ဆီမြုပ်အောင်လုပ်ကာ စက္ကန့်(၃၀)ခန့်ကြော်ကာ ဆယ်ယူဆီစစ်ပါ။",
            "ဒယ်တွင် ဆီ (၃)စားပွဲဇွန်းထည့်ပြီး ပူလျှင် ကြက်သွန်မြိတ်၊ ငရုတ်သီးမှည့်နှင့် ချင်းထည့်ပါ။ နာနတ်သီးလွှာထည့်ပါ။",
            "အမြစ်၊ ငရုတ်သီးစိမ်းနှင့် ဆီ (၁)စားပွဲဇွန်းထည့်ပါ။ သကြား၊ ရှာလကာရည်၊ ခရမ်းချဉ်သီးကက်ချပ်၊ ရေ၊ ဆား၊ နှမ်းဆီ၊ ပြောင်းကော်မှုန့် ရောထည့်ပြီး အသာအယာ ဒယ်ကို ခလောက်ပါ (သို့) မွှေသည်ဆိုရုံမျှသာ ပြုလုပ်ပါ။ ပြီးလျှင် တည်ခင်း၍ရပြီ ဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Trim membrane from duck gizzards, quarter, and score with criss-cross pattern; rinse in cold water and soak in cooking wine for 20 minutes.",
            "Seed and dice green bell pepper; toss pineapple slices with 1/2 tbsp salt for 20 minutes, then squeeze gently and drain excess moisture.",
            "Flash-fry scored gizzards and bell pepper in hot chicken fat/oil for 30 seconds, then drain immediately.",
            "Heat 3 tbsp oil in wok, toss spring onions, red chili, and ginger; add drained pineapple.",
            "Return gizzards and peppers to wok; pour in sauce mixture of sugar, vinegar, ketchup, water, salt, sesame oil, and cornstarch, tossing briskly until glazed and serve."
        ],
        "tags": {"dietary": ["dairy-free"], "seasonal": ["all-season"], "festival": [], "main_ingredients": ["duck gizzard", "pineapple", "bell pepper"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [49], "printed_page_numbers": [87], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 87 (bottom). Criss-cross scoring technique for gizzards preserved.", "verified": True}
    },

    # R0027: ဆိတ်သားဆီပြန် (Mutton Curry)
    {
        "recipe_id": "R0027",
        "name_mm": "ဆိတ်သားဆီပြန်",
        "name_en": "Mutton Curry",
        "description_mm": None,
        "description_en": None,
        "category": "Mutton dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {"ingredient_id": "I0068", "name_mm": "ဆိတ်သား", "name_en": "Mutton", "original_name": "ဆိတ်သား", "quantity": 80.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၈၀ ကျပ်သား", "normalized_quantity": 1306.3, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0024", "name_mm": "နနွင်းမှုန့်", "name_en": "Turmeric powder", "original_name": "နနွင်း", "quantity": 0.25, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁/၄ လဖဇ", "normalized_quantity": 1.25, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0049", "name_mm": "ရှာလကာရည်", "name_en": "Vinegar", "original_name": "ရှာလကာရည်", "quantity": 3.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၃ စပဇ", "normalized_quantity": 45.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0069", "name_mm": "သင်္ဘောသီး", "name_en": "Green papaya", "original_name": "သင်္ဘောသီး (အကင်း)", "quantity": 1.0, "unit": "လုံး (piece)", "original_quantity_text": "၁ လုံး", "normalized_quantity": 1.0, "normalized_unit": "piece", "preparation_note_mm": "အကင်း ကွမ်းသီးလုံးခန့် ရေမဆေးဘဲ ထောင်းထည့်", "preparation_note_en": "unwashed betel-nut size raw green papaya pounded for tenderizer"},
            {"ingredient_id": "I0070", "name_mm": "ငရုတ်ပွခြောက်", "name_en": "Dried mild chili", "original_name": "ငရုတ်ပွခြောက်", "quantity": 10.0, "unit": "တောင့် (piece)", "original_quantity_text": "၁၀ တောင့်", "normalized_quantity": 10.0, "normalized_unit": "piece", "preparation_note_mm": "ရေစိမ် အစေ့ထုတ် ထောင်းထားသော", "preparation_note_en": "soaked, seeded, and pounded"},
            {"ingredient_id": "I0013", "name_mm": "ဂျင်း", "name_en": "Ginger", "original_name": "ချင်း", "quantity": 1.0, "unit": "လက်မ (piece)", "original_quantity_text": "၁ လက်မ", "normalized_quantity": 1.0, "normalized_unit": "piece", "preparation_note_mm": "ထောင်းထားသော", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "original_name": "ကြက်သွန်နီ", "quantity": 10.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၁၀ ကျပ်သား", "normalized_quantity": 163.3, "normalized_unit": "g", "preparation_note_mm": "ထောင်းထားသော", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0014", "name_mm": "ကြက်သွန်ဖြူ", "name_en": "Garlic", "original_name": "ကြက်သွန်ဖြူ", "quantity": 8.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၈ ကျပ်သား", "normalized_quantity": 130.6, "normalized_unit": "g", "preparation_note_mm": "ထောင်းထားသော", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0030", "name_mm": "ငံပြာရည်", "name_en": "Fish sauce", "original_name": "ငံပြာရည်", "quantity": 2.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၂ စပဇ", "normalized_quantity": 30.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0042", "name_mm": "ခရမ်းချဉ်သီး", "name_en": "Tomato", "original_name": "ခရမ်းချဉ်သီး (လှီးပြီး)", "quantity": 10.0, "unit": "လုံး (piece)", "original_quantity_text": "၁၀ လုံး", "normalized_quantity": 10.0, "normalized_unit": "piece", "preparation_note_mm": "လှီးပြီး", "preparation_note_en": "sliced"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "original_name": "ဆီ", "quantity": 3.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၃ ကျပ်သား", "normalized_quantity": 48.9, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "original_name": "ရေနွေး", "quantity": 3.0, "unit": "နို့ဆီဘူး (g)", "original_quantity_text": "၃ နို့ဆီဘူး", "normalized_quantity": 900.0, "normalized_unit": "g", "preparation_note_mm": "ရေနွေး", "preparation_note_en": "hot water"},
            {"ingredient_id": "I0012", "name_mm": "မဆလာ", "name_en": "Garam masala", "original_name": "မဆလာ", "quantity": 1.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၁ စပဇ", "normalized_quantity": 15.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 1.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၁ စပဇ", "normalized_quantity": 15.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None}
        ],
        "servings": 10,
        "preparation_time_minutes": 30,
        "cooking_time_minutes": 60,
        "instructions_mm": [
            "ဆိတ်သားကို အတုံးလိုက်ရေဆေးပြီး အရွယ်ညီတုံးကာ အသားမှ အရည်များကို လက်ဖြင့်ဆုပ်၍ညှစ်ပါ။ အိုးတစ်လုံးထဲထည့်ပြီး ရှာလကာရည်နှင့် သင်္ဘောသီးအကင်း ကွမ်းသီးလုံးခန့် ရေမဆေးဘဲ ထောင်းထည့်ထားပါ။",
            "ငရုတ်သီးပွ အခြောက်ကို ရေစိမ် အစေ့ထုတ် ညက်အောင်ထောင်းပါ။ ချင်း၊ ကြက်သွန်နီ၊ ကြက်သွန်ဖြူပါထည့်၍ ညက်အောင်ထောင်းထည့်ပါ။ နနွင်းထည့်ပါ။ ငံပြာရည်၊ ခရမ်းချဉ်သီးများထည့်ပါ။",
            "သမသွားအောင် နယ်ပြီး (၁၀)မိနစ်ခန့်နှပ်ထားပါ။ ပြီးလျှင် ဆီထည့်ပြီး အဖုံးအုပ်တည်ပါ။",
            "အသားထဲမှ စိမ့်ထွက်ရည်များ ခန်းစပြုလာလျှင် ရေနွေးထည့်ပါ။ အထက်အောက် လှန်ပေးပါ။ မဆလာမှုန့်နှင့် ဆား ထည့်မွှေပါ။ အဖုံးအုပ်၍ မီးအေးအေးဖြင့် ချက်ပါ။",
            "အသားများကျစ်၍ အရည်များခမ်းလျှင် နူး မနူးစမ်းကြည့်ပါ။ နူး၍ဆီပြန်လာလျှင် တည်ခင်း၍ရပြီ ဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Rinse and cut mutton into uniform cubes, squeezing out excess moisture; toss with vinegar and pounded raw green papaya (used unwashed as a natural meat tenderizer).",
            "Soak dried mild chilies, remove seeds, and pound with ginger, onion, and garlic into a fine paste; mix in turmeric, fish sauce, and sliced tomatoes.",
            "Massage everything into the mutton thoroughly and let rest for 10 minutes; add cooking oil, cover, and place on heat.",
            "When the mutton juices release and begin to reduce, add hot water; turn pieces over, stir in garam masala and salt, cover, and braise gently over low heat.",
            "Once meat is tender and liquid evaporates until glossy fragrant oil surfaces, remove from heat and serve."
        ],
        "tags": {"dietary": ["dairy-free", "gluten-free"], "seasonal": ["all-season"], "festival": [], "main_ingredients": ["mutton", "papaya", "tomato"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [50], "printed_page_numbers": [88], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 88 (top). Raw green papaya tenderizing method documented.", "verified": True}
    },

    # R0028: ဆိတ်သားလုံးဟင်း (Mutton Ball Curry)
    {
        "recipe_id": "R0028",
        "name_mm": "ဆိတ်သားလုံးဟင်း",
        "name_en": "Mutton Ball Curry",
        "description_mm": None,
        "description_en": None,
        "category": "Mutton dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {"ingredient_id": "I0068", "name_mm": "ဆိတ်သား", "name_en": "Mutton", "original_name": "ဆိတ်သား", "quantity": 80.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၈၀ ကျပ်သား", "normalized_quantity": 1306.3, "normalized_unit": "g", "preparation_note_mm": "အဆီ အရွတ် ကင်းစင် စဉ်းကောလုပ်ထားသော", "preparation_note_en": "lean and finely minced"},
            {"ingredient_id": "I0033", "name_mm": "သံပရာသီး", "name_en": "Lime", "original_name": "သံပရာသီး", "quantity": 1.0, "unit": "လုံး (piece)", "original_quantity_text": "၁ လုံး", "normalized_quantity": 1.0, "normalized_unit": "piece", "preparation_note_mm": "အရည်ညှစ်", "preparation_note_en": "juiced"},
            {"ingredient_id": "I0070", "name_mm": "ငရုတ်ပွခြောက်", "name_en": "Dried mild chili", "original_name": "ငရုတ်ပွခြောက် (ထောင်းပြီး)", "quantity": 10.0, "unit": "တောင့် (piece)", "original_quantity_text": "၁၀ တောင့်", "normalized_quantity": 10.0, "normalized_unit": "piece", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "original_name": "ကြက်သွန်နီ (ထောင်းပြီး)", "quantity": 10.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၁၀ ကျပ်သား", "normalized_quantity": 163.3, "normalized_unit": "g", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0014", "name_mm": "ကြက်သွန်ဖြူ", "name_en": "Garlic", "original_name": "ကြက်သွန်ဖြူ (ထောင်းပြီး)", "quantity": 8.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၈ ကျပ်သား", "normalized_quantity": 130.6, "normalized_unit": "g", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0013", "name_mm": "ဂျင်း", "name_en": "Ginger", "original_name": "ချင်း (ထောင်းပြီး)", "quantity": 1.0, "unit": "လက်မ (piece)", "original_quantity_text": "၁ လက်မ", "normalized_quantity": 1.0, "normalized_unit": "piece", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 2.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၂ လဖဇ", "normalized_quantity": 10.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0039", "name_mm": "ငရုတ်ကောင်းမှုန့်", "name_en": "Ground black pepper", "original_name": "ငရုတ်ကောင်းမှုန့်", "quantity": 0.25, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁/၄ လဖဇ", "normalized_quantity": 1.25, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0012", "name_mm": "မဆလာ", "name_en": "Garam masala", "original_name": "မဆလာ", "quantity": 3.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၃ လဖဇ", "normalized_quantity": 15.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0050", "name_mm": "ပဲငံပြာရည်", "name_en": "Soy sauce", "original_name": "ပဲငံပြာရည် (အကြည်)", "quantity": 1.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၁ စပဇ", "normalized_quantity": 15.0, "normalized_unit": "g", "preparation_note_mm": "အကြည်", "preparation_note_en": "light"},
            {"ingredient_id": "I0040", "name_mm": "ဘဲဥ", "name_en": "Duck egg", "original_name": "ဘဲဥ", "quantity": 2.0, "unit": "လုံး (piece)", "original_quantity_text": "၂ လုံး", "normalized_quantity": 2.0, "normalized_unit": "piece", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "original_name": "ဆီ", "quantity": 3.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၃ ကျပ်သား", "normalized_quantity": 48.9, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0034", "name_mm": "ကရဝေးရွက်", "name_en": "Bay leaf", "original_name": "ကရဝေး", "quantity": 5.0, "unit": "ရွက် (piece)", "original_quantity_text": "၅ ရွက်", "normalized_quantity": 5.0, "normalized_unit": "piece", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0042", "name_mm": "ခရမ်းချဉ်သီး", "name_en": "Tomato", "original_name": "ခရမ်းချဉ်သီး (လှီးပြီး)", "quantity": 10.0, "unit": "လုံး (piece)", "original_quantity_text": "၁၀ လုံး", "normalized_quantity": 10.0, "normalized_unit": "piece", "preparation_note_mm": "လှီးပြီး", "preparation_note_en": "sliced"},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "original_name": "ရေနွေး", "quantity": 2.0, "unit": "နို့ဆီဘူး (g)", "original_quantity_text": "၂ နို့ဆီဘူး", "normalized_quantity": 600.0, "normalized_unit": "g", "preparation_note_mm": "ရေနွေး", "preparation_note_en": "hot water"}
        ],
        "servings": 10,
        "preparation_time_minutes": 30,
        "cooking_time_minutes": 40,
        "instructions_mm": [
            "အဆီ၊ အရွတ်၊ အရိုးအကြွင်းမဲ့ ကင်းစင်သော ဆိတ်သားတုံးကို ရေဆေးပြီး ဆုပ်ညှစ်ထားပါ။ သံပရာရည်ဖြင့် နယ်ကာ (၁၀)မိနစ်ခန့် ထားပြီးနောက် ရေပြန်ဆေးပါ။ ညက်နေအောင် စဉ်းကောလုပ်ပါ။",
            "ဆိတ်သားထဲသို့ ဆားနှင့် ထောင်းထားသည်များအနက်မှ ငရုတ်သီးတစ်ဝက်၊ ချင်းတစ်ဝက်၊ ကြက်သွန်ဖြူ ၁/၃၊ ငရုတ်ကောင်းမှုန့် ၁/၃၊ မဆလာ ၁/၂ လက်ဖက်ရည်ဇွန်းနှင့် ပဲငံပြာရည်ထည့်ကာ အသားများ စေးပိုင်လာသည်တိုင်အောင်နယ်ပါ။ ဘဲဥထည့်ပါ။ နယ်သားကျလျှင် ဂုံညင်းအရွယ် အလုံးလေးများ လုံးပါ။",
            "ဆီပူအောင်လုပ်၍ ကြက်သွန်နီနှင့် ထောင်းထားသည့် လက်ကျန်များထည့်မွှေပါ။ အနံ့သင်းလာလျှင် ကရဝေးရွက်ထည့်ပါ။ ခရမ်းချဉ်သီးထည့်ပြီး မွှေပေးပါ။",
            "ဆီပြန်၍ အနံ့ထွက်လာလျှင် ဆိတ်သားလုံးများကို အသာအယာ မကြေမွစေရန် အသာမွှေပါ။ အသားလုံးများတင်းလာလျှင် ချန်ထားသောမဆလာ၊ ဆားတို့ကို ထည့်ပါ။ ရေနွေးထည့်ပါ။",
            "အသားနူးလျှင် တည်ခင်း၍ရပြီ ဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Trim all fat and sinew from mutton, squeeze dry, toss in lime juice for 10 minutes to eliminate gaminess, rinse, and finely mince.",
            "Knead minced mutton with salt, half the chili and ginger, 1/3 of the garlic, black pepper, 1/2 tsp garam masala, soy sauce, and duck eggs until sticky; shape into small marble-sized meatballs.",
            "Heat oil in pot and sauté remaining onion, garlic, and aromatics; add bay leaves and sliced tomatoes, cooking until softened into a rich gravy.",
            "Gently slide in the mutton meatballs, stirring delicately so they don't break; once firm, add remaining garam masala, salt, and hot water.",
            "Simmer until meatballs are tender and the gravy is rich and aromatic, then serve."
        ],
        "tags": {"dietary": ["dairy-free"], "seasonal": ["all-season"], "festival": [], "main_ingredients": ["mutton", "duck egg", "tomato"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [50], "printed_page_numbers": [88], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 88 (bottom). Lime juice pre-wash to eliminate odor.", "verified": True}
    },

    # R0029: ဆိတ်သားစဉ်းကောဟင်း (Mutton Kheema Curry)
    {
        "recipe_id": "R0029",
        "name_mm": "ဆိတ်သားစဉ်းကောဟင်း",
        "name_en": "Mutton Kheema Curry",
        "description_mm": None,
        "description_en": None,
        "category": "Mutton dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {"ingredient_id": "I0071", "name_mm": "ဂီးထောပတ်", "name_en": "Ghee", "original_name": "ဂီးထောပတ်", "quantity": 9.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၉ ကျပ်သား", "normalized_quantity": 147.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "original_name": "ကြက်သွန်နီ (နုပ်နုပ်စဉ်း)", "quantity": 4.0, "unit": "ဥ (piece)", "original_quantity_text": "၄ ဥ", "normalized_quantity": 4.0, "normalized_unit": "piece", "preparation_note_mm": "နုပ်နုပ်စဉ်း", "preparation_note_en": "finely minced"},
            {"ingredient_id": "I0068", "name_mm": "ဆိတ်သား", "name_en": "Mutton", "original_name": "ဆိတ်သား (နုပ်နုပ်စဉ်း)", "quantity": 80.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၈၀ ကျပ်သား", "normalized_quantity": 1306.3, "normalized_unit": "g", "preparation_note_mm": "နုပ်နုပ်စဉ်း", "preparation_note_en": "finely minced"},
            {"ingredient_id": "I0044", "name_mm": "ငရုတ်သီးစိမ်း", "name_en": "Green chili", "original_name": "ငရုတ်သီးစိမ်း (ပါးပါးလှီး)", "quantity": 10.0, "unit": "တောင့် (piece)", "original_quantity_text": "၁၀ တောင့်", "normalized_quantity": 10.0, "normalized_unit": "piece", "preparation_note_mm": "ပါးပါးလှီး", "preparation_note_en": "thinly sliced"},
            {"ingredient_id": "I0013", "name_mm": "ဂျင်း", "name_en": "Ginger", "original_name": "ချင်း (၁\" အရွယ် ပါးပါးလှီး)", "quantity": 2.0, "unit": "တုံး (piece)", "original_quantity_text": "၂ တုံး", "normalized_quantity": 2.0, "normalized_unit": "piece", "preparation_note_mm": "ပါးပါးလှီး", "preparation_note_en": "thinly sliced"},
            {"ingredient_id": "I0025", "name_mm": "ငရုတ်သီးမှုန့်", "name_en": "Chili powder", "original_name": "ငရုတ်သီးမှုန့်", "quantity": 2.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၂ လဖဇ", "normalized_quantity": 10.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 1.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁ လဖဇ", "normalized_quantity": 5.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "original_name": "ရေ", "quantity": 1.5, "unit": "နို့ဆီဘူး (g)", "original_quantity_text": "၁ ၁/၂ နို့ဆီဘူး", "normalized_quantity": 450.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0043", "name_mm": "ဂျုံမှုန့်", "name_en": "Wheat flour", "original_name": "ဂျုံ", "quantity": 2.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၂ စပဇ", "normalized_quantity": 30.0, "normalized_unit": "g", "preparation_note_mm": "ရေဖျော်ရန်", "preparation_note_en": "diluted in water"},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "original_name": "ရေ", "quantity": None, "unit": "အနည်းငယ် (g)", "original_quantity_text": "အနည်းငယ်", "normalized_quantity": None, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0072", "name_mm": "မန်ကျည်းသီး", "name_en": "Tamarind", "original_name": "မန်ကျည်းရည်", "quantity": 2.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၂ စပဇ", "normalized_quantity": 30.0, "normalized_unit": "g", "preparation_note_mm": "မှည့်ရည်", "preparation_note_en": "tamarind pulp juice"}
        ],
        "servings": 10,
        "preparation_time_minutes": 20,
        "cooking_time_minutes": 65,
        "instructions_mm": [
            "ဂီးထောပတ်ကို ဆူအောင်တည်ပြီး ကြက်သွန်နီကို ကြော်ပါ။",
            "ဆိတ်သားကိုပါ ထည့်၍ အညိုရောင်ရသည်အထိ အဆက်မပြတ်မွှေပါ။",
            "ငရုတ်သီးစိမ်းနှင့် ချင်း ထည့်ပါ။ ငရုတ်သီးမှုန့်၊ ဆားနှင့် ရေပါထည့်ပြီး (၁)နာရီခန့် ဖြည်းညင်းစွာ နှပ်ထားပါ။",
            "ဂျုံမှုန့်ကို ရေဖျော်ပြီး မန်ကျည်းသီးမှည့်ရည်နှင့်အတူ စဉ်းကောပေါ်သို့ ဖြန်းပေးရပါမည်။",
            "ပြီးလျှင် တည်ခင်း၍ရပြီ ဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Heat ghee in a pot and fry the minced onions until golden.",
            "Add the minced mutton and stir continuously over high heat until browned.",
            "Add sliced green chilies and ginger; then add chili powder, salt, and water, simmering gently for 1 hour.",
            "Dissolve wheat flour in a little water and drizzle over the kheema along with the tamarind juice to thicken.",
            "Simmer for a few minutes until silky and fragrant, then serve."
        ],
        "tags": {"dietary": [], "seasonal": ["all-season"], "festival": [], "main_ingredients": ["mutton", "ghee", "tamarind"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [50], "printed_page_numbers": [89], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 89 (top). Ghee and tamarind-thickened kheema.", "verified": True}
    },

    # R0030: ဆိတ်သားဗင်ဒါလူ (Mutton Vindaloo)
    {
        "recipe_id": "R0030",
        "name_mm": "ဆိတ်သားဗင်ဒါလူ",
        "name_en": "Mutton Vindaloo",
        "description_mm": None,
        "description_en": None,
        "category": "Mutton dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {"ingredient_id": "I0071", "name_mm": "ဂီးထောပတ်", "name_en": "Ghee", "original_name": "ဂီးထောပတ်", "quantity": 10.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၁၀ ကျပ်သား", "normalized_quantity": 163.3, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "original_name": "ကြက်သွန်နီ (လှီးပြီး)", "quantity": 5.0, "unit": "လုံး (piece)", "original_quantity_text": "၅ လုံး", "normalized_quantity": 5.0, "normalized_unit": "piece", "preparation_note_mm": "လှီးပြီး", "preparation_note_en": "sliced"},
            {"ingredient_id": "I0014", "name_mm": "ကြက်သွန်ဖြူ", "name_en": "Garlic", "original_name": "ကြက်သွန်ဖြူ (ထောင်းပြီး)", "quantity": 3.0, "unit": "မြွှာ (piece)", "original_quantity_text": "၃ မြွှာ", "normalized_quantity": 3.0, "normalized_unit": "piece", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0013", "name_mm": "ဂျင်း", "name_en": "Ginger", "original_name": "ချင်း (၁\") (ထောင်းပြီး)", "quantity": 2.0, "unit": "တုံး (piece)", "original_quantity_text": "၂ တုံး", "normalized_quantity": 2.0, "normalized_unit": "piece", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0054", "name_mm": "နံနံစေ့", "name_en": "Coriander seeds", "original_name": "နံနံစေ့ (ထောင်းပြီး)", "quantity": 8.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၈ စပဇ", "normalized_quantity": 120.0, "normalized_unit": "g", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0055", "name_mm": "ဇီယာ", "name_en": "Cumin seeds", "original_name": "ဇီယာစေ့ (ထောင်းပြီး)", "quantity": 4.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၄ လဖဇ", "normalized_quantity": 20.0, "normalized_unit": "g", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0039", "name_mm": "ငရုတ်ကောင်းမှုန့်", "name_en": "Ground black pepper", "original_name": "ငရုတ်ကောင်းစေ့ (ထောင်းပြီး)", "quantity": 0.5, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁/၂ လဖဇ", "normalized_quantity": 2.5, "normalized_unit": "g", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0062", "name_mm": "မုန်ညင်းစေ့", "name_en": "Mustard seeds", "original_name": "မုန်ညင်းစေ့ (ထောင်းပြီး)", "quantity": 2.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၂ လဖဇ", "normalized_quantity": 10.0, "normalized_unit": "g", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0069", "name_mm": "သင်္ဘောသီး", "name_en": "Green papaya", "original_name": "သင်္ဘောသီးအကင်း (ထောင်းပြီး)", "quantity": 1.0, "unit": "လုံး (piece)", "original_quantity_text": "၁ လုံး", "normalized_quantity": 1.0, "normalized_unit": "piece", "preparation_note_mm": "ထောင်းပြီး", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0068", "name_mm": "ဆိတ်သား", "name_en": "Mutton", "original_name": "ဆိတ်သား", "quantity": 80.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၈၀ ကျပ်သား", "normalized_quantity": 1306.3, "normalized_unit": "g", "preparation_note_mm": "တုံးထားသည့် တုံးကြီးများ", "preparation_note_en": "large chunks"},
            {"ingredient_id": "I0025", "name_mm": "ငရုတ်သီးမှုန့်", "name_en": "Chili powder", "original_name": "ငရုတ်သီးမှုန့်", "quantity": 4.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၄ စပဇ", "normalized_quantity": 60.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 1.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၁ လဖဇ", "normalized_quantity": 5.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0049", "name_mm": "ရှာလကာရည်", "name_en": "Vinegar", "original_name": "ရှာလကာရည်", "quantity": 8.0, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၈ လဖဇ", "normalized_quantity": 40.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "original_name": "ရေ", "quantity": None, "unit": "လိုအပ်သရွေ့ (as needed)", "original_quantity_text": "လိုအပ်သရွေ့", "normalized_quantity": None, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None}
        ],
        "servings": 10,
        "preparation_time_minutes": 30,
        "cooking_time_minutes": 60,
        "instructions_mm": [
            "ဂီးထောပတ်ကို အပူပေးပြီး ကြက်သွန်နီကို အညိုရောင်ရသည်အထိ ကြော်ပါ။",
            "ကြက်သွန်ဖြူနှင့် ချင်းကို ထည့်မွှေပါ။ ၂ မိနစ်ခန့်ရှိလျှင် ထောင်းထားသည့် ဟင်းခတ်အမွှေးအကြိုင်များ၊ သင်္ဘောသီးအကင်း၊ တုံးထားသည့် ဆိတ်သားတုံးကြီးများ၊ ငရုတ်သီးမှုန့်၊ ဆားနှင့် ရှာလကာရည် ရောစပ်ထည့်ပြီး ခြောက်သည်အထိကြော်ပါ။",
            "ရေလိုအပ်သရွေ့ထည့်ထားကာ အိုးအဖုံးကို တင်းကျပ်စွာပိတ်ပြီး အပေါ်မှနေ၍ အလေးဖိထားကာ မီးအေးအေးဖြင့် ဖြည်းညင်းစွာချက်ပါ။",
            "အသားစဉ်းကောများ နူးနပ်ကာ အရည်များစုပ်ယူသွားပြီး ဂီးထောပတ်သာကျန်သည်အထိ ချက်ရပါမည်။",
            "ပြီးလျှင် တည်ခင်း၍ရပြီ ဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Heat ghee in a heavy pot and fry the onions until rich golden brown.",
            "Add pounded garlic and ginger, cook for 2 minutes, then add the ground spice blend, pounded raw papaya, large mutton chunks, chili powder, salt, and vinegar, frying until dry.",
            "Add water as needed, seal the lid tightly with a weight on top, and braise very slowly over gentle heat.",
            "Cook until the mutton is deeply tender, all liquid is absorbed, and only fragrant clarified ghee remains.",
            "Transfer to a dish and serve."
        ],
        "tags": {"dietary": ["gluten-free"], "seasonal": ["all-season"], "festival": [], "main_ingredients": ["mutton", "ghee", "vinegar"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [50], "printed_page_numbers": [89], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 89 (bottom). Weighted lid slow braise with ghee.", "verified": True}
    },

    # R0031: ဆိတ်ကလီစာဟင်း (Mutton Offal Curry)
    {
        "recipe_id": "R0031",
        "name_mm": "ဆိတ်ကလီစာဟင်း",
        "name_en": "Mutton Offal Curry",
        "description_mm": None,
        "description_en": None,
        "category": "Mutton dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {"ingredient_id": "I0073", "name_mm": "ဆိတ်ကလီစာ", "name_en": "Mutton offal", "original_name": "ဆိတ်ကလီစာ", "quantity": 80.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၈၀ ကျပ်သား", "normalized_quantity": 1306.3, "normalized_unit": "g", "preparation_note_mm": "သန့်စင်ပြီး အနေတော်တုံး", "preparation_note_en": "cleaned and cut into medium pieces"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "original_name": "ဆား", "quantity": 2.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၂ စပဇ", "normalized_quantity": 30.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0024", "name_mm": "နနွင်းမှုန့်", "name_en": "Turmeric powder", "original_name": "နနွင်း", "quantity": 0.75, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "original_quantity_text": "၃/၄ လဖဇ", "normalized_quantity": 3.75, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0033", "name_mm": "သံပရာသီး", "name_en": "Lime", "original_name": "သံပရာသီး", "quantity": 1.0, "unit": "လုံး (piece)", "original_quantity_text": "၁ လုံး", "normalized_quantity": 1.0, "normalized_unit": "piece", "preparation_note_mm": "အရည်ညှစ်", "preparation_note_en": "juiced"},
            {"ingredient_id": "I0013", "name_mm": "ဂျင်း", "name_en": "Ginger", "original_name": "ချင်း (၁\")", "quantity": 2.0, "unit": "တုံး (piece)", "original_quantity_text": "၂ တုံး", "normalized_quantity": 2.0, "normalized_unit": "piece", "preparation_note_mm": "ထောင်းထားသော", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0070", "name_mm": "ငရုတ်ပွခြောက်", "name_en": "Dried mild chili", "original_name": "ငရုတ်သီးပွခြောက်", "quantity": 3.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၃ ကျပ်သား", "normalized_quantity": 49.0, "normalized_unit": "g", "preparation_note_mm": "ထောင်းထားသော", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "original_name": "ကြက်သွန်နီ", "quantity": 15.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၁၅ ကျပ်သား", "normalized_quantity": 245.0, "normalized_unit": "g", "preparation_note_mm": "ထောင်းထားသော", "preparation_note_en": "pounded"},
            {"ingredient_id": "I0055", "name_mm": "ဇီယာ", "name_en": "Cumin seeds", "original_name": "ဇီယာ", "quantity": 1.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၁ စပဇ", "normalized_quantity": 15.0, "normalized_unit": "g", "preparation_note_mm": "မညက်တညက်ထောင်း", "preparation_note_en": "coarsely crushed"},
            {"ingredient_id": "I0010", "name_mm": "ဖာလာစေ့", "name_en": "Cardamom", "original_name": "ဖာလာ", "quantity": 3.0, "unit": "စေ့ (piece)", "original_quantity_text": "၃ စေ့", "normalized_quantity": 3.0, "normalized_unit": "piece", "preparation_note_mm": "မညက်တညက်ထောင်း", "preparation_note_en": "coarsely crushed"},
            {"ingredient_id": "I0034", "name_mm": "ကရဝေးရွက်", "name_en": "Bay leaf", "original_name": "ကရဝေး", "quantity": 3.0, "unit": "ရွက် (piece)", "original_quantity_text": "၃ ရွက်", "normalized_quantity": 3.0, "normalized_unit": "piece", "preparation_note_mm": "မညက်တညက်ထောင်း", "preparation_note_en": "coarsely crushed"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "original_name": "ဆီ", "quantity": 15.0, "unit": "ကျပ်သား (g)", "original_quantity_text": "၁၅ ကျပ်သား", "normalized_quantity": 245.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "original_name": "ရေနွေး", "quantity": 1.0, "unit": "နို့ဆီဘူး (g)", "original_quantity_text": "၁ နို့ဆီဘူး", "normalized_quantity": 300.0, "normalized_unit": "g", "preparation_note_mm": "ရေနွေး", "preparation_note_en": "hot water"},
            {"ingredient_id": "I0012", "name_mm": "မဆလာ", "name_en": "Garam masala", "original_name": "မဆလာ", "quantity": 1.0, "unit": "စားပွဲဇွန်း (tbsp / g)", "original_quantity_text": "၁ စပဇ", "normalized_quantity": 15.0, "normalized_unit": "g", "preparation_note_mm": None, "preparation_note_en": None}
        ],
        "servings": 10,
        "preparation_time_minutes": 30,
        "cooking_time_minutes": 60,
        "instructions_mm": [
            "ဆိတ်ကလီစာကို သန့်စင်အောင် လုပ်ပြီး အနေတော်တုံးပါ။ ဆား၊ နနွင်း၊ သံပရာသီးရည်နှင့် နယ်ထားပါ။ ချင်း၊ ငရုတ်သီးအပွတောင့်နှင့် ကြက်သွန်နီကို ညက်အောင်ထောင်းပါ။ ဇီယာစေ့၊ ဖာလာစေ့၊ ကရဝေးတို့ကို မညက်တညက်ထောင်းထားပါ။",
            "ဆိတ်ကလီစာအိုးတွင် ထောင်းထားသည်များနှင့် ဆီကိုထည့်၍ နယ်ပြီး ရေနွေးထည့်ကာ အဖုံးအုပ်၍ တည်ပါ။",
            "ပထမရေခမ်းလျှင် နောက်ထပ်ရေနွေး အသားမြုပ်ရုံထည့်ပြီး ဆက်တည်ပါ။",
            "နူးစပြုလာလျှင် မဆလာအုပ်ပါ။",
            "ဆီပြန်လျှင် တည်ခင်း၍ရပြီ ဖြစ်ပါသည်။"
        ],
        "instructions_en": [
            "Thoroughly clean mutton offal, cut into bite-sized pieces, and marinate with salt, turmeric, and lime juice; finely pound ginger, mild chili, and onion; coarsely crush cumin, cardamom, and bay leaves.",
            "In a pot, combine offal with all aromatics and cooking oil, toss well, add 1 tin hot water, cover, and place on heat.",
            "When the first water reduces, add more hot water just enough to submerge the meat and continue braising.",
            "As the offal becomes tender, sprinkle garam masala over the top.",
            "When the sauce thickens and glossy aromatic oil surfaces, remove from heat and serve."
        ],
        "tags": {"dietary": ["dairy-free", "gluten-free"], "seasonal": ["all-season"], "festival": [], "main_ingredients": ["mutton offal"]},
        "nutrition": {"calories_kcal_per_serving": None, "protein_g_per_serving": None, "carbohydrates_g_per_serving": None, "fat_g_per_serving": None},
        "estimated_cost_mmk": None,
        "source": {"document": "ဟင်းချက်နည်းများ.pdf", "pdf_pages": [51], "printed_page_numbers": [90], "extraction_method": "manual_transcription_from_scanned_image"},
        "data_quality": {"extraction_status": "complete", "confidence": 1.0, "review_notes": "Printed on page 90 (top). Thorough lime marinade to deodorize offal.", "verified": True}
    }
]
