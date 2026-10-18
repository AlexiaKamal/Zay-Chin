# -*- coding: utf-8 -*-
"""
Batch 5 Part B: Recipes R0055 to R0067
Covers Pickles, Sauces, Jellies, Marmalade, and Chutneys from Book pp. 102-107 (PDF pp. 57-59).
"""

BATCH5_RECIPES_B = [
    {
        "recipe_id": "R0055",
        "name_mm": "သရက်သီးအခြောက်သနပ်",
        "name_en": "Dried Mango Achar Pickle",
        "description_mm": "ရေနွေးပြုတ်ထားသော သရက်သီးခြောက်ကို မန်ကျည်းနှစ်၊ မုန်ညင်းစေ့၊ သနပ်မဆလာ၊ ကြက်သွန်ဖြူ၊ ဂျင်းတို့ဖြင့် ဆီကျက်ဆီမြုပ်အောင် စီမံထားသော မြန်မာ့ရိုးရာ သရက်သီးခြောက်သနပ်။",
        "description_en": "Traditional Myanmar sun-dried mango pickle preserved in tamarind pulp, roasted mustard seeds, achar spices, garlic, ginger, and generous oil for long shelf life.",
        "category": "pickle_preserve",
        "meal_types": ["lunch", "dinner", "side_dish"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0102",
                "name_mm": "သရက်သီးခြောက်",
                "name_en": "Dried mango",
                "original_name": "သရက်သီးခြောက်",
                "quantity": 25.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၅ ကျပ်သား",
                "normalized_quantity": 408.2,
                "normalized_unit": "g",
                "preparation_note_mm": "ဆူးများခြစ်ပြီး အရှည် ၂\" အကျယ် ၁/၂\" လှီးထားသော",
                "preparation_note_en": "trimmed of fibrous prickles and sliced into 2 x 0.5 inch pieces"
            },
            {
                "ingredient_id": "I0012",
                "name_mm": "ရေနွေး",
                "name_en": "Hot water",
                "original_name": "ရေနွေး (သရက်သီးခြောက်မြုပ်ရုံ)",
                "quantity": 1.5,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "မြုပ်ရုံ",
                "normalized_quantity": 450.0,
                "normalized_unit": "g",
                "preparation_note_mm": "သရက်သီးခြောက်ပြုတ်ရန်",
                "preparation_note_en": "for scalding dried mango"
            },
            {
                "ingredient_id": "I0072",
                "name_mm": "မန်ကျည်းသီး",
                "name_en": "Tamarind",
                "original_name": "မန်ကျည်းသီး",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.65,
                "normalized_unit": "g",
                "preparation_note_mm": "ပြုတ်၍ အနှစ်တိုက်ထားသော",
                "preparation_note_en": "boiled with water and strained into smooth pulp"
            },
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ",
                "quantity": 1.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၁ နို့ဆီဘူး",
                "normalized_quantity": 300.0,
                "normalized_unit": "g",
                "preparation_note_mm": "မန်ကျည်းသီးပြုတ်ရန်",
                "preparation_note_en": "for boiling tamarind"
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.65,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0103",
                "name_mm": "သနပ်မဆလာ",
                "name_en": "Pickle masala",
                "original_name": "သနပ်မဆလာမှုန့်",
                "quantity": 2.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
                "normalized_quantity": 40.8,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0062",
                "name_mm": "မုန်ညင်းစေ့",
                "name_en": "Mustard seeds",
                "original_name": "မုန်ညင်းစေ့လှော် (အခွံချွတ်)",
                "quantity": 2.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
                "normalized_quantity": 40.8,
                "normalized_unit": "g",
                "preparation_note_mm": "လှော်ပြီး အခွံချွတ်ထားသော",
                "preparation_note_en": "roasted and dehulled"
            },
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": 30.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၃၀ ကျပ်သား",
                "normalized_quantity": 489.9,
                "normalized_unit": "g",
                "preparation_note_mm": "ဆီသတ်ရန်နှင့် ဆီမြုပ်အောင်ထားရန်",
                "preparation_note_en": "for tempering and submerging"
            },
            {
                "ingredient_id": "I0022",
                "name_mm": "ကြက်သွန်ဖြူ",
                "name_en": "Garlic",
                "original_name": "ကြက်သွန်ဖြူ (အခွံချွတ်)",
                "quantity": 7.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၇ ၁/၂ ကျပ်သား",
                "normalized_quantity": 122.5,
                "normalized_unit": "g",
                "preparation_note_mm": "အခွံချွတ်ပြီး ၁ ကျပ်သားဆီသတ် ကျန်အလုံးလိုက်ထည့်ရန်",
                "preparation_note_en": "peeled; part sautéed, remainder kept whole"
            },
            {
                "ingredient_id": "I0030",
                "name_mm": "ချင်း",
                "name_en": "Ginger",
                "original_name": "ချင်း",
                "quantity": 2.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
                "normalized_quantity": 40.8,
                "normalized_unit": "g",
                "preparation_note_mm": "ပါးပါးလှီးထားသော",
                "preparation_note_en": "finely julienned"
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ငရုတ်သီးခြောက်",
                "name_en": "Dried red chili",
                "original_name": "ငရုတ်သီးမှုန့်",
                "quantity": 2.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
                "normalized_quantity": 40.8,
                "normalized_unit": "g",
                "preparation_note_mm": "အမှုန့်",
                "preparation_note_en": "ground chili powder"
            }
        ],
        "instructions_mm": [
            "သရက်သီးခြောက်ရှိ ဆူးများကို ခြစ်ပစ်ပြီး အရှည် ၂ လက်မ၊ အကျယ် ၁/၂ လက်မခန့် အရွယ်လှီးပါ။",
            "သရက်သီးခြောက် မြုပ်ရုံ ရေနွေးဆူဆူဖြင့် (၁) မိနစ်ခန့် ပြုတ်ပြီးနောက် ရေငှဲ့ပစ်ပါ။",
            "မန်ကျည်းသီးနှင့် ရေရောပြုတ်ပြီး နူးလျှင် အနှစ်တိုက်ကာ ၎င်းအနှစ်ကို သကြားနှင့်အတူ ရေခန်းသည်အထိ ရောကျိုပါ။",
            "ကျိုထားသော မန်ကျည်းနှစ်နှင့် ပြုတ်ထားသည့် သရက်သီးခြောက်များကို သနပ်မဆလာ၊ မုန်ညင်းစေ့လှော်တို့ဖြင့် ရောနယ်ပါ။",
            "ဆီကျက်အောင်လုပ်ပြီး ကြက်သွန်ဖြူ (၁) ကျပ်သားခန့်နှင့် ဂျင်းတို့ကို ဆီသတ်ကာ ငရုတ်သီးမှုန့်နှင့် ရေ (၃) စားပွဲဇွန်းထည့်၍ မွှေပါ။",
            "ကျက်လျှင် နယ်ထားသည့် သရက်သီးနှင့် မန်ကျည်းနှစ်များ ထည့်၍ သမအောင် မွှေပေးပါ။",
            "အဝကျယ်၍ ခြောက်သွေ့သန့်စင်သော ပုလင်းထဲသို့ သနပ်များ အေးလျှင် ထည့်ပြီး ကျန်ကြက်သွန်ဖြူမြွှာများ ထည့်ကာ မှိုမတက်စေရန် ဆီမြုပ်အောင် ထားပါ။"
        ],
        "instructions_en": [
            "Scrape off any tough fibrous spikes from dried mango slices and cut into 2 x 0.5 inch pieces.",
            "Scald the dried mango pieces in boiling water for about 1 minute to soften slightly, then drain completely.",
            "Boil tamarind with 1 tin of water until soft, strain through a sieve into a thick puree, and simmer with sugar until thick and glossy.",
            "Toss the scalded dried mango pieces with the sweetened tamarind puree, pickle masala, and roasted dehulled mustard seeds.",
            "Heat oil in a pan, fry about 1 kyat-tha of garlic and the julienned ginger until fragrant, then stir in the chili powder moistened with 3 tablespoons of water.",
            "Once aromatic, add the spiced mango and tamarind mixture, stirring thoroughly over gentle heat until evenly incorporated.",
            "Allow the pickle to cool completely, transfer into a clean, dry, wide-mouthed glass jar, drop in the remaining whole garlic cloves, and ensure completely submerged under oil to prevent mold."
        ],
        "tags": {
            "dietary": ["vegan", "vegetarian", "gluten-free", "dairy-free"],
            "seasonal": ["summer", "all-year"],
            "festival": [],
            "main_ingredients": ["dried mango", "tamarind", "mustard seeds", "garlic", "pickle masala"]
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
            "pdf_pages": [57],
            "printed_page_numbers": [102],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "Traditional Myanmar sun-dried achar preservation technique. 7:7 instruction parity verified.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0056",
        "name_mm": "သရက်သီးအစိမ်းသနပ်",
        "name_en": "Green Mango Spiced Pickle",
        "description_mm": "ဆားနယ်နေလှန်းထားသော သရက်သီးစိမ်းတုံးများကို ပဲနံ့သာ၊ မုန်ညင်းစေ့၊ သနပ်မဆလာ၊ နနွင်း၊ ဂျင်းနှင့် ကြက်သွန်ဖြူ ဆီသတ်မွှေးဖြင့် ဆီမြုပ်စိမ်ထားသော သနပ်။",
        "description_en": "Crisp green mango cured in salt, sun-dried, and tossed with roasted fenugreek, mustard seeds, aromatic pickle masala, turmeric, ginger, and garlic steeped in hot oil.",
        "category": "pickle_preserve",
        "meal_types": ["lunch", "dinner", "side_dish"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0104",
                "name_mm": "သရက်သီးစိမ်း",
                "name_en": "Raw green mango",
                "original_name": "သရက်သီးအစိမ်း (၅)လုံး",
                "quantity": 50.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅၀ ကျပ်သား",
                "normalized_quantity": 816.5,
                "normalized_unit": "g",
                "preparation_note_mm": "ဂျစ်စတ် သို့မဟုတ် နှစ်သက်သည့်အရွယ် တုံးထားသော",
                "preparation_note_en": "cut into bite-sized chunks"
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 2.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
                "normalized_quantity": 40.8,
                "normalized_unit": "g",
                "preparation_note_mm": "တစ်ညသိပ်နယ်ထားရန်",
                "preparation_note_en": "for overnight salt curing"
            },
            {
                "ingredient_id": "I0105",
                "name_mm": "ပဲနံ့သာစေ့",
                "name_en": "Fenugreek seeds",
                "original_name": "ပဲနံ့သာစေ့ (လှော်ပြီး)",
                "quantity": 0.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ မူးသား",
                "normalized_quantity": 8.16,
                "normalized_unit": "g",
                "preparation_note_mm": "လှော်ပြီး မညက်တညက် ထောင်းထားသော",
                "preparation_note_en": "roasted and coarsely crushed"
            },
            {
                "ingredient_id": "I0062",
                "name_mm": "မုန်ညင်းစေ့",
                "name_en": "Mustard seeds",
                "original_name": "မုန်ညင်းစေ့ (လှော်ပြီး)",
                "quantity": 1.25,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ မတ်သား",
                "normalized_quantity": 20.4,
                "normalized_unit": "g",
                "preparation_note_mm": "လှော်ပြီး မညက်တညက် ထောင်းထားသော",
                "preparation_note_en": "roasted and coarsely crushed"
            },
            {
                "ingredient_id": "I0103",
                "name_mm": "သနပ်မဆလာ",
                "name_en": "Pickle masala",
                "original_name": "သနပ်မဆလာ",
                "quantity": 2.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
                "normalized_quantity": 40.8,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ငရုတ်သီးခြောက်",
                "name_en": "Dried red chili",
                "original_name": "ငရုတ်သီးမှုန့်",
                "quantity": 2.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
                "normalized_quantity": 40.8,
                "normalized_unit": "g",
                "preparation_note_mm": "အမှုန့်",
                "preparation_note_en": "ground chili powder"
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
                "preparation_note_mm": "ဆီမြုပ်ရန် လိုအပ်သရွေ့",
                "preparation_note_en": "for tempering and submerging"
            },
            {
                "ingredient_id": "I0114",
                "name_mm": "နနွင်း",
                "name_en": "Turmeric powder",
                "original_name": "နနွင်း",
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
                "original_name": "ချင်း (ပါးပါးလှီး)",
                "quantity": 2.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
                "normalized_quantity": 40.8,
                "normalized_unit": "g",
                "preparation_note_mm": "ပါးပါးလှီးထားသော",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0022",
                "name_mm": "ကြက်သွန်ဖြူ",
                "name_en": "Garlic",
                "original_name": "ကြက်သွန်ဖြူ",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.65,
                "normalized_unit": "g",
                "preparation_note_mm": "အလုံးလိုက် ထည့်ရန်",
                "preparation_note_en": "peeled whole cloves"
            }
        ],
        "instructions_mm": [
            "သရက်သီးစိမ်းကို နှစ်သက်သည့် အရွယ်တုံးကာ ရေအေးဖြင့် (၁၅) မိနစ်ခန့် စိမ်ပြီး ဆယ်ယူရေစစ်ထားပါ။",
            "ပြီးလျှင် ဆားနယ်ပြီး အင်တုံဖြင့် တစ်ညသိပ်ထားပြီး နောက်နေ့နံနက်တွင် နေလှန်းကာ တစ်ညပြန်စိမ်ထားပါ။",
            "ပဲနံ့သာစေ့နှင့် မုန်ညင်းစေ့လှော်တို့ကို မညက်တညက် ထောင်းကာ သရက်သီးနှင့် နယ်ပါ။",
            "သနပ်မဆလာနှင့် ငရုတ်သီးမှုန့်တစ်ဝက်ကိုပါ ရောထည့်ပြီး သန့်စင်ခြောက်သွေ့သည့် အိုးတွင် ခေတ္တဖိသိပ်ထားပါ။",
            "ဆီအိုးတည်၍ ပူလျှင် နနွင်းထည့်မွှေကာ ဂျင်းနှင့် လက်ကျန်ငရုတ်မှုန့် ထည့်မွှေပါ။",
            "နှပ်ထားသည့် သရက်သီးများနှင့် အမွှေးအကြိုင်ဆီတို့ကို ကောင်းစွာ ရောစပ်ပါ။",
            "အေးလျှင် ပုလင်းထဲသို့ထည့်ပြီး ကြက်သွန်ဖြူမြွှာများကို အလုံးလိုက်ထည့်ကာ ဆီမြုပ်အောင် ထားပါ။"
        ],
        "instructions_en": [
            "Cut raw green mangoes into bite-sized chunks, soak in cold water for about 15 minutes, and drain thoroughly.",
            "Toss with salt and let cure in a basin overnight; the following morning, sun-dry slightly and return to its brine for another night.",
            "Coarsely crush the roasted fenugreek and mustard seeds, and massage into the cured mango chunks.",
            "Mix in the pickle masala and half of the chili powder, and pack firmly into a clean dry pot to absorb spices.",
            "Heat cooking oil in a pan, bloom the turmeric, then sauté the sliced ginger and the remaining chili powder until fragrant.",
            "Pour the aromatic spiced oil over the seasoned mangoes and mix thoroughly.",
            "Once cooled, transfer into a clean glass jar, add whole garlic cloves, and keep completely submerged in oil."
        ],
        "tags": {
            "dietary": ["vegan", "vegetarian", "gluten-free", "dairy-free"],
            "seasonal": ["summer", "all-year"],
            "festival": [],
            "main_ingredients": ["green mango", "mustard seeds", "fenugreek", "garlic", "pickle masala"]
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
            "pdf_pages": [57],
            "printed_page_numbers": [102],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "7:7 instruction parity verified. Traditional two-day salt-curing technique preserved.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0057",
        "name_mm": "သံပရာသီးသနပ်",
        "name_en": "Spiced Lime Achar Pickle",
        "description_mm": "ဆားစိမ်သံပရာသီးများကို လေးစိတ်စိတ်ပြီး နှမ်းဆီပူတွင် ဇီယာ၊ မုန်ညင်းစေ့၊ ငရုတ်သီးမှုန့်၊ ရှာလကာရည်၊ ဂျင်း၊ ကြက်သွန်ဖြူတို့ဖြင့် စီမံထားသော သံပရာသီးသနပ်။",
        "description_en": "Whole salt-cured limes cut into quarters and preserved in aromatic toasted sesame oil infused with cumin, mustard seeds, chili, vinegar, ginger, and garlic, aged in the sun for two weeks.",
        "category": "pickle_preserve",
        "meal_types": ["lunch", "dinner", "side_dish"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0106",
                "name_mm": "သံပရာသီး",
                "name_en": "Lime",
                "original_name": "သံပရာသီး",
                "quantity": 25.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂၅ လုံး",
                "normalized_quantity": 25.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အလုံးလိုက် ရေဆေးခြောက်သွေ့အောင် ပြုလုပ်ထားသော",
                "preparation_note_en": "washed whole and dried completely"
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 28.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၈ ကျပ်သား",
                "normalized_quantity": 457.2,
                "normalized_unit": "g",
                "preparation_note_mm": "သံပရာသီး ဆားစိမ်ရန်",
                "preparation_note_en": "for salt curing layers"
            },
            {
                "ingredient_id": "I0067",
                "name_mm": "နှမ်းဆီ",
                "name_en": "Sesame oil",
                "original_name": "နှမ်းဆီ",
                "quantity": 35.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၃၅ ကျပ်သား",
                "normalized_quantity": 571.5,
                "normalized_unit": "g",
                "preparation_note_mm": "အချဉ်ဆီကျက်ချက်ရန်",
                "preparation_note_en": "pure sesame oil for pickle oil base"
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ငရုတ်သီးခြောက်",
                "name_en": "Dried red chili",
                "original_name": "ငရုတ်သီးမှုန့်",
                "quantity": 14.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၄ ကျပ်သား",
                "normalized_quantity": 228.6,
                "normalized_unit": "g",
                "preparation_note_mm": "အမှုန့်",
                "preparation_note_en": "ground chili powder"
            },
            {
                "ingredient_id": "I0055",
                "name_mm": "ဇီယာ",
                "name_en": "Cumin seeds",
                "original_name": "ဇီယာစေ့ (ထောင်းပြီး)",
                "quantity": 14.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၄ ကျပ်သား",
                "normalized_quantity": 228.6,
                "normalized_unit": "g",
                "preparation_note_mm": "ထောင်းပြီး",
                "preparation_note_en": "crushed cumin"
            },
            {
                "ingredient_id": "I0062",
                "name_mm": "မုန်ညင်းစေ့",
                "name_en": "Mustard seeds",
                "original_name": "မုန်ညင်းစေ့ (လှော်ပြီး)",
                "quantity": 8.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၈ ကျပ်သား",
                "normalized_quantity": 130.6,
                "normalized_unit": "g",
                "preparation_note_mm": "လှော်ပြီး",
                "preparation_note_en": "roasted"
            },
            {
                "ingredient_id": "I0049",
                "name_mm": "ရှာလကာရည်",
                "name_en": "Vinegar",
                "original_name": "ရှာလကာရည်",
                "quantity": 0.75,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၃/၄ နို့ဆီဘူး",
                "normalized_quantity": 225.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0022",
                "name_mm": "ကြက်သွန်ဖြူ",
                "name_en": "Garlic",
                "original_name": "ကြက်သွန်ဖြူ (ပါးပါးလှီး)",
                "quantity": 6.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၆ ကျပ်သား",
                "normalized_quantity": 98.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ပါးပါးလှီးထားသော",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0030",
                "name_mm": "ချင်း",
                "name_en": "Ginger",
                "original_name": "ချင်း (ပါးပါးလှီး)",
                "quantity": 4.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၄ ကျပ်သား",
                "normalized_quantity": 65.3,
                "normalized_unit": "g",
                "preparation_note_mm": "ပါးပါးလှီးထားသော",
                "preparation_note_en": "thinly sliced"
            }
        ],
        "instructions_mm": [
            "သံပရာသီး အလုံးလိုက်ကို ရေဆေးပြီး ခြောက်သွေ့အောင် သုတ်ထားပါ။",
            "ပုလင်းလွတ်ထဲသို့ ပထမ ဆားဖြန့်ထည့်ပြီး ၎င်းအပေါ်မှ သံပရာသီး ဖြန့်စီထည့်ကာ အပြန်အလှန်ထည့်၍ လနှင့်ချီ ဆားစိမ်ထားပါ။",
            "ဆားစိမ်ထားသော သံပရာသီးများကို လေးစိတ် စိတ်ဖြတ်ထားပါ။",
            "နှမ်းဆီပူတွင် ငရုတ်သီးမှုန့်၊ ဇီယာ၊ မုန်ညင်းစေ့၊ ရှာလကာရည်၊ ကြက်သွန်ဖြူနှင့် ဂျင်းတို့ကို ကျက်အောင် ချက်ပါ။",
            "ချက်ထားသော အမွှေးအကြိုင်အရောကို အအေးခံကာ သံပရာသီးစိတ်များပေါ်သို့ အပေါ်ယံမှ လောင်းဆမ်းပါ။",
            "၎င်းကို ပုလင်းထဲသို့ ထည့်ပြီး (၂) ပတ်ခန့် နေလှန်းပေးကာ ရက်စေ့လျှင် အရသာရှိစွာ စားသုံးနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Wash whole limes and dry them completely with a clean cloth.",
            "In a clean glass jar, alternate layers of salt and whole limes, cover tightly, and allow to cure for months until skins soften.",
            "Take out the cured limes and cut each into four wedges.",
            "In hot sesame oil, cook the ground chili, cumin seeds, roasted mustard seeds, vinegar, sliced garlic, and ginger until aromatic and cooked through.",
            "Allow the spiced aromatic oil to cool, then pour generously over the cut cured lime wedges to coat thoroughly.",
            "Pack into jars and place in the sun for about 2 weeks to age before serving."
        ],
        "tags": {
            "dietary": ["vegan", "vegetarian", "gluten-free", "dairy-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["lime", "sesame oil", "cumin", "mustard seeds", "garlic"]
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
            "pdf_pages": [57],
            "printed_page_numbers": [103],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "6:6 instruction parity verified. Traditional salt-cured aged lime achar method preserved.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0058",
        "name_mm": "မန်ကျည်းသီးသနပ်",
        "name_en": "Sweet and Tangy Tamarind Pickle",
        "description_mm": "နူးအိအောင်ပြုတ်ပြီး အနှစ်တိုက်ထားသော မန်ကျည်းနှစ်ကို သကြား၊ ဘိန်းစေ့၊ သနပ်မဆလာ၊ ဂျင်း၊ ကြက်သွန်ဖြူဆီသတ်တို့ဖြင့် ကျိုချက်ထားသော ရိုးရာ မန်ကျည်းသီးသနပ်။",
        "description_en": "Velvety boiled tamarind pulp simmered with sugar, poppy seeds, achar masala, sautéed ginger, crushed garlic, and chili oil into a rich, sweet-and-sour pickle.",
        "category": "pickle_preserve",
        "meal_types": ["lunch", "dinner", "side_dish"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0072",
                "name_mm": "မန်ကျည်းသီး",
                "name_en": "Tamarind",
                "original_name": "မန်ကျည်းသီး",
                "quantity": 30.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၃၀ ကျပ်သား",
                "normalized_quantity": 489.9,
                "normalized_unit": "g",
                "preparation_note_mm": "အမှိုက်ကင်းစင်အောင် ပြုလုပ်ထားသော",
                "preparation_note_en": "cleaned of debris and seeds"
            },
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေအေး",
                "quantity": 2.5,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၂ ၁/၂ နို့ဆီဘူး",
                "normalized_quantity": 750.0,
                "normalized_unit": "g",
                "preparation_note_mm": "မန်ကျည်းသီးပြုတ်ရန်",
                "preparation_note_en": "for boiling tamarind"
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
                "original_name": "ဘိန်းစေ့",
                "quantity": 2.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ကျပ်သား",
                "normalized_quantity": 32.65,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0103",
                "name_mm": "သနပ်မဆလာ",
                "name_en": "Pickle masala",
                "original_name": "သနပ်မဆလာ",
                "quantity": 2.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
                "normalized_quantity": 40.8,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": 25.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၅ ကျပ်သား",
                "normalized_quantity": 408.2,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0030",
                "name_mm": "ချင်း",
                "name_en": "Ginger",
                "original_name": "ချင်း (ပါးပါးလှီး)",
                "quantity": 1.25,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁ ၁/၄ ကျပ်သား",
                "normalized_quantity": 20.4,
                "normalized_unit": "g",
                "preparation_note_mm": "ပါးပါးလှီးထားသော",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ငရုတ်သီးခြောက်",
                "name_en": "Dried red chili",
                "original_name": "ငရုတ်သီးမှုန့်",
                "quantity": 2.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
                "normalized_quantity": 40.8,
                "normalized_unit": "g",
                "preparation_note_mm": "ရေ ၃ စပဇ ဖြင့် ဖျော်ထားသော",
                "preparation_note_en": "diluted with 3 tbsp water"
            },
            {
                "ingredient_id": "I0022",
                "name_mm": "ကြက်သွန်ဖြူ",
                "name_en": "Garlic",
                "original_name": "ကြက်သွန်ဖြူ",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.65,
                "normalized_unit": "g",
                "preparation_note_mm": "၁ ကျပ်သား ထုဆီသတ်၍ ကျန်အလုံးလိုက်ထည့်ရန်",
                "preparation_note_en": "part crushed for tempering, remainder whole"
            }
        ],
        "instructions_mm": [
            "အမှိုက်ကင်းစင်အောင် လုပ်ထားသည့် မန်ကျည်းသီးကို ရေဆေးပြီး ရေအေးဖြင့် နူးသည်အထိ ပြုတ်ပါ။",
            "နူးလျှင် အနှစ်တိုက်ပြီး ဆား၊ သကြားရောကာ ရေခန်း၍ ပျစ်လာသည်အထိ ကျိုပါ။",
            "ပျစ်လာလျှင် ဘိန်းစေ့နှင့် သနပ်မဆလာ ထည့်ပြီး သမအောင် မွှေပါ။",
            "ဆီကျက်အောင်ချက်ပြီး ဂျင်းဆီသတ်ကာ ကြွပ်လာလျှင် ကြက်သွန်ဖြူ (၁) ကျပ်သား ထုထည့်ပါ။",
            "ငရုတ်သီးမှုန့်ကို ရေဖြင့် ဖျော်၍ ထည့်မွှေပြီး ကျက်လာလျှင် မန်ကျည်းသီးအနှစ်များနှင့် ရောစပ်ပါ။",
            "ဆီအေးအောင် ဖိုမှချအအေးခံပြီး ကြက်သွန်ဖြူများ ထည့်ကာ သန့်စင်ခြောက်သွေ့သော ပုလင်းထဲသို့ထည့်၍ ဆီမြုပ်အောင် ထားပါ။"
        ],
        "instructions_en": [
            "Clean tamarind of debris, rinse, and boil in cold water until completely softened.",
            "Strain into a smooth thick puree, blend in salt and sugar, and simmer until reduced and thick.",
            "Once thickened, fold in the poppy seeds and pickle masala, stirring evenly.",
            "Heat oil in a pan, fry julienned ginger until crisp, then add 1 kyat-tha of crushed garlic.",
            "Mix chili powder with 3 tbsp water, pour into the hot oil, fry until aromatic, and fold into the tamarind puree.",
            "Remove from heat to cool completely, mix in the remaining garlic cloves, transfer to a clean dry jar, and submerge under oil."
        ],
        "tags": {
            "dietary": ["vegan", "vegetarian", "gluten-free", "dairy-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["tamarind", "poppy seeds", "garlic", "ginger", "pickle masala"]
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
            "pdf_pages": [57],
            "printed_page_numbers": [103],
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
        "recipe_id": "R0059",
        "name_mm": "ပန်းဂေါ်ဖီသနပ်",
        "name_en": "Spiced Cauliflower Pickle",
        "description_mm": "နေလှန်းနွမ်းစေပြီး ရှာလကာရည်၊ သကြား၊ ဆားတို့ဖြင့် နှပ်ထားသော ပန်းဂေါ်ဖီပွင့်များကို ဂျင်း၊ မဆလာ၊ မုန်ညင်းစေ့၊ ဇီယာ ဆီသတ်မွှေးဖြင့် ဆီမြုပ်စီမံထားသော သနပ်။",
        "description_en": "Cauliflower florets wilted in the sun, marinated in vinegar, sugar, and salt, then tossed in aromatic hot oil tempered with ginger, achar masala, mustard seeds, and cumin.",
        "category": "pickle_preserve",
        "meal_types": ["lunch", "dinner", "side_dish"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0108",
                "name_mm": "ပန်းဂေါ်ဖီ",
                "name_en": "Cauliflower",
                "original_name": "ပန်းဂေါ်ဖီပွင့်",
                "quantity": 30.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၃၀ ကျပ်သား",
                "normalized_quantity": 489.9,
                "normalized_unit": "g",
                "preparation_note_mm": "အခက်သေးသေးအရွယ် လှီးရေဆေးပြီး နေလှန်းထားသော",
                "preparation_note_en": "cut into small florets, washed, and sun-wilted"
            },
            {
                "ingredient_id": "I0049",
                "name_mm": "ရှာလကာရည်",
                "name_en": "Vinegar",
                "original_name": "ရှာလကာရည်",
                "quantity": 5.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၅ လဖဇ",
                "normalized_quantity": 25.0,
                "normalized_unit": "g",
                "preparation_note_mm": "တစ်ဝက်နှပ်ရန် တစ်ဝက်ဆီသတ်ရန်",
                "preparation_note_en": "half for marinating, half for cooking"
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
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": 15.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၅ ကျပ်သား",
                "normalized_quantity": 245.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0030",
                "name_mm": "ချင်း",
                "name_en": "Ginger",
                "original_name": "ချင်း (ပါးပါးလှီး)",
                "quantity": 1.25,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁ ၁/၄ ကျပ်သား",
                "normalized_quantity": 20.4,
                "normalized_unit": "g",
                "preparation_note_mm": "ပါးပါးလှီးထားသော",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0022",
                "name_mm": "ကြက်သွန်ဖြူ",
                "name_en": "Garlic",
                "original_name": "ကြက်သွန်ဖြူ",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.65,
                "normalized_unit": "g",
                "preparation_note_mm": "အခွံနွှာထားသော",
                "preparation_note_en": "peeled whole cloves"
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ငရုတ်သီးခြောက်",
                "name_en": "Dried red chili",
                "original_name": "ငရုတ်သီးမှုန့်",
                "quantity": 1.25,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁ ၁/၄ ကျပ်သား",
                "normalized_quantity": 20.4,
                "normalized_unit": "g",
                "preparation_note_mm": "အမှုန့်",
                "preparation_note_en": "ground chili powder"
            },
            {
                "ingredient_id": "I0103",
                "name_mm": "သနပ်မဆလာ",
                "name_en": "Pickle masala",
                "original_name": "သနပ်မဆလာ",
                "quantity": 2.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
                "normalized_quantity": 40.8,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0062",
                "name_mm": "မုန်ညင်းစေ့",
                "name_en": "Mustard seeds",
                "original_name": "မုန်ညင်းစေ့",
                "quantity": 2.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
                "normalized_quantity": 40.8,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0055",
                "name_mm": "ဇီယာ",
                "name_en": "Cumin seeds",
                "original_name": "ဇီယာ",
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
            "ပန်းဂေါ်ဖီပွင့်များကို အခက်သေးသေးအရွယ်လှီး ရေဆေးပြီး နေတစ်နေ့ လှန်းထားပါ။",
            "နွမ်းလျှင် ရှာလကာရည်တစ်ဝက်၊ သကြား၊ ဆားတို့ဖြင့် ရောနယ်ပြီး နှပ်ထားကာ နောက်နေ့တွင် နေ့ဝက်ခန့် နေထပ်လှန်းပေးပါ။",
            "ဆီပူအောင်လုပ်ပြီး ဂျင်းထည့်မွှေကာ ကျန်ရှာလကာရည်နှင့်အတူ ငရုတ်သီးမှုန့်၊ သနပ်မဆလာ ထည့်မွှေပါ။",
            "ဆူလာလျှင် နေလှန်းထားသော ဂေါ်ဖီပန်းများ ထည့်မွှေပါ။",
            "မုန်ညင်းစေ့နှင့် ဇီယာပါ ရောထည့်ပြီး အားလုံးသမအောင် မွှေကာ ဖိုမှချထားပါ။",
            "အေးစပြုလာလျှင် ကြက်သွန်ဖြူထည့်မွှေကာ သန့်ရှင်းခြောက်သွေ့သည့် ပုလင်းထဲသို့ထည့်ပြီး ဆီမြုပ်အောင် ထားပါ။"
        ],
        "instructions_en": [
            "Cut cauliflower into small florets, wash thoroughly, and dry in the sun for one day.",
            "Once wilted, toss with half the vinegar, sugar, and salt, marinate overnight, and sun-dry again for half a day.",
            "Heat cooking oil in a pan, fry ginger, then add the remaining vinegar, chili powder, and pickle masala.",
            "When simmering, add the wilted cauliflower florets and stir-fry gently.",
            "Add mustard seeds and cumin seeds, stirring well to distribute spices evenly, then remove from heat.",
            "When lukewarm, stir in whole garlic cloves, pack into a clean dry jar, and ensure completely submerged under oil."
        ],
        "tags": {
            "dietary": ["vegan", "vegetarian", "gluten-free", "dairy-free"],
            "seasonal": ["winter", "all-year"],
            "festival": [],
            "main_ingredients": ["cauliflower", "mustard seeds", "cumin", "garlic", "pickle masala"]
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
            "pdf_pages": [58],
            "printed_page_numbers": [104],
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
        "recipe_id": "R0060",
        "name_mm": "ပဲသီးစိမ်းသနပ်",
        "name_en": "Pickled String Beans Achar",
        "description_mm": "ဆားနှင့် ရှာလကာရည်တို့ဖြင့် နှပ်ထားသော ပဲသီးတောင့်များကို ပဲနံ့သာ၊ ဇီယာ၊ မဆလာ၊ ငရုတ်သီးမှုန့်ဆီသတ်တို့ဖြင့် ဆူအောင်မွှေပြီး ကြက်သွန်ဖြူဖြင့် ဆီမြုပ်သိမ်းဆည်းထားသော သနပ်။",
        "description_en": "Fresh string beans steeped in vinegar and salt, then tossed in hot spiced oil with roasted fenugreek, cumin, achar masala, and chili, bottled with crisp whole garlic cloves.",
        "category": "pickle_preserve",
        "meal_types": ["lunch", "dinner", "side_dish"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0015",
                "name_mm": "ပဲသီး",
                "name_en": "Green beans",
                "original_name": "ပဲသီးစိမ်းတောင့်",
                "quantity": 50.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅၀ ကျပ်သား",
                "normalized_quantity": 816.5,
                "normalized_unit": "g",
                "preparation_note_mm": "၁ လက်မအရွယ် ဖြတ်ထားသော",
                "preparation_note_en": "trimmed and cut into 1-inch lengths"
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
                "preparation_note_mm": "၁ စပဇ နှပ်ရန် ၁ စပဇ ဆီသတ်ရန်",
                "preparation_note_en": "part for steeping, part for cooking"
            },
            {
                "ingredient_id": "I0049",
                "name_mm": "ရှာလကာရည်",
                "name_en": "Vinegar",
                "original_name": "ရှာလကာရည်",
                "quantity": 0.75,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၃/၄ နို့ဆီဘူး",
                "normalized_quantity": 225.0,
                "normalized_unit": "g",
                "preparation_note_mm": "တစ်ဝက်နှပ်ရန် တစ်ဝက်ဆီသတ်ရန်",
                "preparation_note_en": "half for steeping, half for cooking"
            },
            {
                "ingredient_id": "I0105",
                "name_mm": "ပဲနံ့သာစေ့",
                "name_en": "Fenugreek seeds",
                "original_name": "ပဲနံ့သာစေ့ (လှော်ပြီး)",
                "quantity": 1.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ စပဇ",
                "normalized_quantity": 15.0,
                "normalized_unit": "g",
                "preparation_note_mm": "လှော်ပြီး",
                "preparation_note_en": "roasted"
            },
            {
                "ingredient_id": "I0055",
                "name_mm": "ဇီယာ",
                "name_en": "Cumin seeds",
                "original_name": "ဇီယာ (ထောင်းပြီး)",
                "quantity": 2.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၂ စပဇ",
                "normalized_quantity": 30.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ထောင်းပြီး",
                "preparation_note_en": "crushed"
            },
            {
                "ingredient_id": "I0103",
                "name_mm": "သနပ်မဆလာ",
                "name_en": "Pickle masala",
                "original_name": "သနပ်မဆလာ",
                "quantity": 2.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၂ စပဇ",
                "normalized_quantity": 30.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": 20.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၀ ကျပ်သား",
                "normalized_quantity": 326.5,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ငရုတ်သီးခြောက်",
                "name_en": "Dried red chili",
                "original_name": "ငရုတ်သီးမှုန့်",
                "quantity": 2.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ကျပ်သား",
                "normalized_quantity": 32.65,
                "normalized_unit": "g",
                "preparation_note_mm": "အမှုန့်",
                "preparation_note_en": "ground chili powder"
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
                "ingredient_id": "I0022",
                "name_mm": "ကြက်သွန်ဖြူ",
                "name_en": "Garlic",
                "original_name": "ကြက်သွန်ဖြူ",
                "quantity": 10.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၀ ကျပ်သား",
                "normalized_quantity": 163.3,
                "normalized_unit": "g",
                "preparation_note_mm": "ခွာထားသော အလုံးလိုက်",
                "preparation_note_en": "peeled whole cloves"
            }
        ],
        "instructions_mm": [
            "ပဲသီးစိမ်းကို (၁) လက်မအရွယ် ဖြတ်တောက်ကာ ကြွေဇလုံထဲသို့ ထည့်ပါ။",
            "ဆား (၁) စားပွဲဇွန်းနှင့် ရှာလကာရည် တစ်ဝက်ထည့်၍ နှံ့အောင်မွှေကာ (၁) နာရီခန့် နှပ်ထားပါ။",
            "ပဲနံ့သာစေ့၊ ဇီယာစေ့နှင့် သနပ်မဆလာတို့ကို ကြိုတင် ရောမွှေထားပါ။",
            "ဆီပူအောင်လုပ်ပြီး ငရုတ်သီးမှုန့်၊ မဆလာအရော၊ ဆား၊ သကြားနှင့် ကျန်ရှာလကာရည်တို့ ထည့်မွှေပါ။",
            "ဆူလာလျှင် နှပ်ထားသော ပဲသီးများထည့်ပြီး နှံ့စပ်အောင် မွှေကြော်ကာ ဖိုမှချ၍ အအေးခံထားပါ။",
            "အေးပြီးနောက် ခွာထားသော ကြက်သွန်ဖြူများ ထည့်ကာ သန့်စင်သော ပုလင်းထဲထည့်၍ ဆီမြုပ်အောင် ထားပါ။"
        ],
        "instructions_en": [
            "Trim string beans and cut into 1-inch lengths, placing them in a ceramic bowl.",
            "Add 1 tablespoon of salt and half the vinegar, toss thoroughly, and allow to steep for 1 hour.",
            "Pre-mix the roasted fenugreek, crushed cumin, and pickle masala.",
            "Heat oil in a pan, then stir in the chili powder, mixed spice blend, remaining salt, sugar, and the remaining vinegar.",
            "When the seasoned oil comes to a boil, toss in the steeped string beans, stir well for a minute to coat evenly, and take off the heat to cool.",
            "Once cool, mix in the peeled whole garlic cloves, transfer to a clean jar, and ensure completely submerged under oil."
        ],
        "tags": {
            "dietary": ["vegan", "vegetarian", "gluten-free", "dairy-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["green beans", "fenugreek", "cumin", "garlic", "pickle masala"]
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
            "pdf_pages": [58],
            "printed_page_numbers": [104],
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
        "recipe_id": "R0061",
        "name_mm": "ခရမ်းချဉ်သီးဆော့စ်",
        "name_en": "Homestyle Spiced Tomato Sauce",
        "description_mm": "ခရမ်းချဉ်သီးမှည့်များကို စပျစ်သီးခြောက်၊ ဂျင်း၊ ကြက်သွန်ဖြူ၊ ငရုတ်ပွခြောက်၊ ရှာလကာရည်နှင့် သကြားတို့ဖြင့် အနှစ်တိုက်ကျိုချက်ထားသော ရိုးရာဆော့စ်။",
        "description_en": "Rich homestyle tomato sauce slow-simmered with raisins, ginger, garlic, mild red chilies, vinegar, and sugar, strained and reduced into a thick dipping and cooking sauce.",
        "category": "condiment",
        "meal_types": ["sauce", "condiment"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0030",
                "name_mm": "ချင်း",
                "name_en": "Ginger",
                "original_name": "ချင်း",
                "quantity": 7.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၇ ကျပ်သား",
                "normalized_quantity": 114.3,
                "normalized_unit": "g",
                "preparation_note_mm": "ထောင်းထားသော",
                "preparation_note_en": "pounded"
            },
            {
                "ingredient_id": "I0033",
                "name_mm": "စပျစ်သီးခြောက်",
                "name_en": "Raisins",
                "original_name": "စပျစ်သီးခြောက်",
                "quantity": 55.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅၅ ကျပ်သား",
                "normalized_quantity": 898.1,
                "normalized_unit": "g",
                "preparation_note_mm": "ထောင်းထားသော",
                "preparation_note_en": "pounded"
            },
            {
                "ingredient_id": "I0022",
                "name_mm": "ကြက်သွန်ဖြူ",
                "name_en": "Garlic",
                "original_name": "ကြက်သွန်ဖြူ",
                "quantity": 7.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၇ ကျပ်သား",
                "normalized_quantity": 114.3,
                "normalized_unit": "g",
                "preparation_note_mm": "ထောင်းထားသော",
                "preparation_note_en": "pounded"
            },
            {
                "ingredient_id": "I0070",
                "name_mm": "ငရုတ်ပွခြောက်",
                "name_en": "Dried mild chili",
                "original_name": "ငရုတ်သီးပွခြောက်",
                "quantity": 5.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ၁/၂ ကျပ်သား",
                "normalized_quantity": 89.8,
                "normalized_unit": "g",
                "preparation_note_mm": "ထောင်းထားသော",
                "preparation_note_en": "pounded"
            },
            {
                "ingredient_id": "I0049",
                "name_mm": "ရှာလကာရည်",
                "name_en": "Vinegar",
                "original_name": "ရှာလကာရည်",
                "quantity": 0.75,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၃/၄ နို့ဆီဘူး",
                "normalized_quantity": 225.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0042",
                "name_mm": "ခရမ်းချဉ်သီး",
                "name_en": "Tomato",
                "original_name": "ခရမ်းချဉ်သီး",
                "quantity": 2.0,
                "unit": "ပိဿာ (kg)",
                "original_quantity_text": "၂ ပိဿာ",
                "normalized_quantity": 3265.8,
                "normalized_unit": "g",
                "preparation_note_mm": "လုံးစိတ်စိတ်ပြီး ပြုတ်ထားသော",
                "preparation_note_en": "quartered and boiled"
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 55.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅၅ ကျပ်သား",
                "normalized_quantity": 898.1,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 5.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ၁/၂ ကျပ်သား",
                "normalized_quantity": 89.8,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "ဂျင်း၊ စပျစ်သီးခြောက်၊ ကြက်သွန်ဖြူနှင့် ငရုတ်သီးပွခြောက်တို့ကို ညက်အောင်ထောင်း၍ ရှာလကာရည်တွင် ရောစပ်ပါ။",
            "ခရမ်းချဉ်သီးကို လုံးစိတ်ပြုတ်ပြီး ကြွေရည်သုတ်အိုးထဲသို့ ထည့်ပါ။",
            "သကြား၊ ဆားနှင့် ထောင်းထားသည့် အရာများကို ရေစပ်ကာ မီးအေးအေးဖြင့် ပျစ်လာသည်အထိ မွှေပေးပါ။",
            "ပြီးလျှင် ဆန်ခါဖြင့် စစ်ယူပြီး ရလာသည့်အရည်ကို ပျစ်လာသည်အထိ မီးအေးအေးဖြင့် ပြန်လည်တည်ပါ။",
            "အအေးခံပြီး သန့်စင်သော ပုလင်းထဲသို့ ထည့်ထားရပါမည်။ ၎င်းဆော့စ်ကို ကြော်ရာတွင်လည်းကောင်း ချက်ရာတွင်လည်းကောင်း အသုံးပြုနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Pound the ginger, raisins, garlic, and dried mild chilies into a paste and blend with vinegar.",
            "Quarter and boil the fresh tomatoes until soft, transferring them into an enamelled or non-reactive cooking pot.",
            "Add sugar, salt, and the spiced raisin paste, stirring slowly over gentle heat until reduced and thickened.",
            "Strain the sauce through a sieve to remove skins and seeds, then return the smooth liquid to low heat and reduce until velvety and thick.",
            "Allow to cool completely and pour into sterilized glass bottles; use as a dipping sauce or cooking condiment."
        ],
        "tags": {
            "dietary": ["vegan", "vegetarian", "gluten-free", "dairy-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["tomato", "raisins", "vinegar", "sugar", "chili"]
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
            "pdf_pages": [58],
            "printed_page_numbers": [105],
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
        "recipe_id": "R0062",
        "name_mm": "ခရမ်းချဉ်သီးကက်ချပ်",
        "name_en": "Preserved Spiced Tomato Ketchup",
        "description_mm": "ခရမ်းချဉ်သီးမှည့်ကို ဂျင်း၊ ကြက်သွန်ဖြူ၊ ရှာလကာရည်၊ သကြား၊ လေးညှင်း၊ သစ်ကြံပိုး၊ ဖာလာတို့ဖြင့် ပျစ်နှစ်အောင်ကျိုပြီး ဆိုဒီယမ်ဘင်ဆိုအိတ်ဖြင့် တာရှည်ခံအောင် ပြုလုပ်ထားသော ကက်ချပ်။",
        "description_en": "Thick spiced tomato ketchup cooked down with ginger, garlic, vinegar, sugar, whole cloves, cinnamon, cardamom, and food-safe sodium benzoate for a one-year shelf life.",
        "category": "condiment",
        "meal_types": ["sauce", "condiment"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0042",
                "name_mm": "ခရမ်းချဉ်သီး",
                "name_en": "Tomato",
                "original_name": "ခရမ်းချဉ်သီး",
                "quantity": 1.0,
                "unit": "ပိဿာ (kg)",
                "original_quantity_text": "၁ ပိဿာ",
                "normalized_quantity": 1632.9,
                "normalized_unit": "g",
                "preparation_note_mm": "ရေဆေးအခြောက်ခံပြီး နုပ်နုပ်စဉ်းထားသော",
                "preparation_note_en": "washed, dried, and finely chopped"
            },
            {
                "ingredient_id": "I0022",
                "name_mm": "ကြက်သွန်ဖြူ",
                "name_en": "Garlic",
                "original_name": "ကြက်သွန်ဖြူ (နုပ်နုပ်စဉ်း)",
                "quantity": 4.0,
                "unit": "မြွှာ (clove)",
                "original_quantity_text": "၄ မြွှာ",
                "normalized_quantity": 4.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "နုပ်နုပ်စဉ်းထားသော",
                "preparation_note_en": "finely minced"
            },
            {
                "ingredient_id": "I0030",
                "name_mm": "ချင်း",
                "name_en": "Ginger",
                "original_name": "ချင်း (ခုတ်စဉ်းပြီး)",
                "quantity": 2.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၂ လဖဇ",
                "normalized_quantity": 10.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ခုတ်စဉ်းပြီး",
                "preparation_note_en": "finely chopped"
            },
            {
                "ingredient_id": "I0049",
                "name_mm": "ရှာလကာရည်",
                "name_en": "Vinegar",
                "original_name": "ရှာလကာရည်",
                "quantity": 0.67,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၂/၃ နို့ဆီဘူး",
                "normalized_quantity": 200.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 15.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၅ ကျပ်သား",
                "normalized_quantity": 245.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ငရုတ်သီးခြောက်",
                "name_en": "Dried red chili",
                "original_name": "ငရုတ်သီးမှုန့်",
                "quantity": 1.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁ လဖဇ",
                "normalized_quantity": 5.0,
                "normalized_unit": "g",
                "preparation_note_mm": "အမှုန့်",
                "preparation_note_en": "ground chili powder"
            },
            {
                "ingredient_id": "I0109",
                "name_mm": "အချဉ်မှုန့်",
                "name_en": "Citric acid / Tartaric acid",
                "original_name": "အချဉ်မှုန့်",
                "quantity": 0.5,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁/၂ လဖဇ",
                "normalized_quantity": 2.5,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0110",
                "name_mm": "ဆိုဒီယမ်ဘင်ဆိုအိတ်",
                "name_en": "Sodium benzoate",
                "original_name": "ဆိုဒီယမ်ဘင်ဆိုအိတ်",
                "quantity": 0.5,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁/၂ လဖဇ",
                "normalized_quantity": 2.5,
                "normalized_unit": "g",
                "preparation_note_mm": "အစားအသောက်တာရှည်ခံဆေး",
                "preparation_note_en": "food-grade preservative"
            },
            {
                "ingredient_id": "I0012",
                "name_mm": "ရေနွေး",
                "name_en": "Hot water",
                "original_name": "ရေနွေး",
                "quantity": 2.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၂ စပဇ",
                "normalized_quantity": 30.0,
                "normalized_unit": "g",
                "preparation_note_mm": "တာရှည်ခံဆေးဖျော်ရန်",
                "preparation_note_en": "for dissolving preservative"
            },
            {
                "ingredient_id": "I0009",
                "name_mm": "လေးညှင်းပွင့်",
                "name_en": "Cloves",
                "original_name": "လေးညှင်းပွင့်",
                "quantity": 2.0,
                "unit": "ပွင့် (piece)",
                "original_quantity_text": "၂ ပွင့်",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0008",
                "name_mm": "သစ်ကြံပိုးခေါက်",
                "name_en": "Cinnamon bark",
                "original_name": "သစ်ကြံပိုး",
                "quantity": 0.5,
                "unit": "လက်မ (inch / g)",
                "original_quantity_text": "၁/၂ လက်မ",
                "normalized_quantity": 7.5,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0010",
                "name_mm": "ဖာလာစေ့",
                "name_en": "Cardamom pods",
                "original_name": "ဖာလာစေ့",
                "quantity": 1.0,
                "unit": "စေ့ (pod)",
                "original_quantity_text": "၁ စေ့",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 2.5,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၂ ၁/၂ လဖဇ",
                "normalized_quantity": 12.5,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "ရေဆေးအခြောက်ခံထားသည့် ခရမ်းချဉ်သီးကို နုပ်နုပ်စဉ်းပြီး ကြက်သွန်ဖြူ၊ ဂျင်းများ ရောစပ်ကာ မီးအေးအေးတွင် နူးပြီး ပျစ်လာသည်အထိ ချက်ပါ။",
            "ပျစ်လာလျှင် ဆန်ခါဖြင့် စစ်ကာ ရှာလကာရည်၊ သကြား၊ ငရုတ်သီးမှုန့်တို့ ရောပြီး ထပ်မံ၍ ပျစ်လာသည်အထိ ကျိုပေးပါ။",
            "အချဉ်မှုန့်နှင့် ဆိုဒီယမ်ဘင်ဆိုအိတ် အမှုန့်ကို ရေနွေးဆူဆူတွင် ရောစပ်ပြီး ခရမ်းချဉ်သီး အပျစ်ရည်များနှင့် ရောကာ ပြန်၍ ဆူအောင်တည်ပါ။",
            "လေးညှင်းပွင့်၊ သစ်ကြံပိုး၊ ဖာလာစေ့နှင့် ဆားတို့ကို ထည့်၍ မွှေပါ။",
            "ပြီးလျှင် ဖိုမှချ၍ အအေးခံကာ ပုလင်းထဲသို့ထည့်၍ အဖုံးကို လုံအောင် တင်းကျပ်စွာ ပိတ်ထားပါ။ တစ်ပတ်ကြာမှ စတင် အသုံးပြုနိုင်ပြီး တစ်နှစ်ကြာ ထားရှိနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Finely chop washed, dried tomatoes and simmer gently with minced garlic and ginger until thoroughly softened and pulpy.",
            "Pass through a fine sieve, combine the puree with vinegar, sugar, and chili powder, and reduce over low heat until thickened.",
            "Dissolve citric acid and sodium benzoate preservative in 2 tbsp hot water, stir into the tomato reduction, and bring back to a boil.",
            "Add whole cloves, cinnamon bark, cardamom pod, and salt, stirring well to infuse spices.",
            "Remove from heat to cool, pour into sterile bottles, and seal tightly; allow to age unopened for one week before use (keeps for up to one year)."
        ],
        "tags": {
            "dietary": ["vegan", "vegetarian", "gluten-free", "dairy-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["tomato", "vinegar", "sugar", "clove", "cinnamon"]
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
            "pdf_pages": [58],
            "printed_page_numbers": [105],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "5:5 instruction parity verified. Food preservation methodology transcribed accurately.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0063",
        "name_mm": "မာလကာသီးယို",
        "name_en": "Natural Guava Jelly",
        "description_mm": "မာလကာသီးပြုတ်ရည်ကို ပိတ်ပါးအိတ်ဖြင့် တစ်ညလုံး စစ်ထုတ်ပြီး သကြား၊ သံပရာရည်၊ ထောပတ်တို့ဖြင့် ကြွက်မြီးတန်းသည့်အထိ ဖြည်းညင်းစွာ ကျိုချက်ထားသော မာလကာသီး ဂျယ်လီယို။",
        "description_en": "Clear pectin-rich guava juice strained overnight through muslin, boiled with sugar, fresh lime juice, and a touch of butter until it forms a delicate, shimmering jelly.",
        "category": "dessert",
        "meal_types": ["breakfast", "snack", "dessert"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0111",
                "name_mm": "မာလကာသီး",
                "name_en": "Guava",
                "original_name": "မာလကာသီး",
                "quantity": 100.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁၀၀ လုံး",
                "normalized_quantity": 100.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အခွံခွာပြီး နူးသည်အထိ ပြုတ်ထားသော",
                "preparation_note_en": "peeled and boiled until soft"
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 3.75,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၃ ၃/၄ နို့ဆီဘူး",
                "normalized_quantity": 1125.0,
                "normalized_unit": "g",
                "preparation_note_mm": "မာလကာရည် ၄ နို့ဆီဘူးအတွက်",
                "preparation_note_en": "proportioned per 4 tins of strained juice"
            },
            {
                "ingredient_id": "I0106",
                "name_mm": "သံပရာသီး",
                "name_en": "Lime",
                "original_name": "သံပရာသီး (ညှစ်ပြီး)",
                "quantity": 5.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၅ လုံး",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အရည်ညှစ်ထားသော",
                "preparation_note_en": "freshly squeezed juice"
            },
            {
                "ingredient_id": "I0002",
                "name_mm": "ထောပတ်",
                "name_en": "Butter",
                "original_name": "ထောပတ်",
                "quantity": 0.5,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁/၂ စပဇ",
                "normalized_quantity": 7.5,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "မာလကာသီးကို အခွံခွာပြီး နူးသည်အထိ ရေဖြင့် ပြုတ်ပါ။",
            "ပိတ်ပါးအိတ်တွင် အားလုံးထည့်ကာ တစ်ညလုံး ရေစစ်ထားပါ။",
            "စစ်ထားသော မာလကာရည်ကို ရေအနည်းငယ်ခန်းအောင် တည်ပြီး ချိန်ဆရာတွင် မာလကာရည် (၄) နို့ဆီဘူး၌ သကြား (၃ ၃/၄) ဘူးစာ ရော၍ ပြန်တည်ပါ။",
            "ကျက်ကာနီးအချိန်တွင် သံပရာရည်နှင့် ထောပတ်ကို ရောထည့်မွှေပေးပါ။",
            "မီးအေးအေးဖြင့် ကျိုရာတွင် မာလကာရည်သည် ကြွက်မြီးတန်းသည့် အနေအထားသို့ ရောက်ရှိလာလျှင် ပုံစံခွက် သို့မဟုတ် ခွက်ထဲသို့ ထည့်ထားကာ အအေးခံ၍ အသုံးပြုနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Peel the guavas and boil in water until tender.",
            "Pour the boiled guavas into a cheesecloth jelly bag and let the clear pectin-rich juice drip overnight without squeezing.",
            "Simmer the strained guava juice slightly to reduce, measuring 3 3/4 tins of sugar for every 4 tins of juice, and bring to a gentle boil.",
            "Just before the setting point is reached, stir in the fresh lime juice and butter to clarify.",
            "Continue simmering over low heat until the liquid sheets or threads off the spoon ('rat-tail thread' test), then pour into molds or jars to set into clear jelly."
        ],
        "tags": {
            "dietary": ["vegetarian", "gluten-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["guava", "sugar", "lime juice", "butter"]
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
            "pdf_pages": [59],
            "printed_page_numbers": [106],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "5:5 instruction parity verified. Classic jelly-making technique with natural fruit pectin preserved.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0064",
        "name_mm": "လိမ္မော်-ရှောက်မားမလိတ်",
        "name_en": "Citrus Orange and Lemon Marmalade",
        "description_mm": "ပါးပါးလှီးထားသော လိမ္မော်ခွံနှင့် ရှောက်ခွံတို့ကို ရေဖြင့် စိမ်ပြုတ်ပြီး သကြားဖြင့် ကျောက်ကျောရည်ကဲ့သို့ ဂျယ်လီအနေအထား ရောက်သည်အထိ ကျိုချက်ထားသော မားမလိတ်ယို။",
        "description_en": "Fine shreds of sweet orange and fragrant lemon peel soaked and slow-simmered, then boiled with equal parts sugar until set into a glistening citrus marmalade.",
        "category": "dessert",
        "meal_types": ["breakfast", "snack", "dessert"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0112",
                "name_mm": "လိမ္မော်သီး",
                "name_en": "Orange",
                "original_name": "လိမ္မော်သီး",
                "quantity": 6.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၆ လုံး",
                "normalized_quantity": 6.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ပါးနိုင်သမျှ ပါးအောင်လှီးပြီး အစေ့ထုတ်ထားသော",
                "preparation_note_en": "thinly sliced and deseeded"
            },
            {
                "ingredient_id": "I0079",
                "name_mm": "ရှောက်သီး",
                "name_en": "Lemon / Citron",
                "original_name": "ရှောက်သီး",
                "quantity": 4.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၄ လုံး",
                "normalized_quantity": 4.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ပါးနိုင်သမျှ ပါးအောင်လှီးပြီး အစေ့ထုတ်ထားသော",
                "preparation_note_en": "thinly sliced and deseeded"
            },
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေ",
                "quantity": 3.0,
                "unit": "ဆ (ratio)",
                "original_quantity_text": "အသီး၏သုံးဆ",
                "normalized_quantity": 1500.0,
                "normalized_unit": "g",
                "preparation_note_mm": "အသီးထုထည်၏ ၃ ဆ ထည့်ရန်",
                "preparation_note_en": "three times the fruit volume"
            },
            {
                "ingredient_id": "I0005",
                "name_mm": "သကြား",
                "name_en": "Sugar",
                "original_name": "သကြား",
                "quantity": 1.0,
                "unit": "ဆ (ratio)",
                "original_quantity_text": "ပြုတ်ရည်တစ်ဆ သကြားတစ်ဆ",
                "normalized_quantity": 1000.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ပြုတ်ရည် ၁ နို့ဆီဘူးလျှင် သကြား ၁ နို့ဆီဘူး",
                "preparation_note_en": "equal parts by tin measure of boiled fruit liquid"
            }
        ],
        "instructions_mm": [
            "လိမ္မော်သီးနှင့် ရှောက်သီးကို ပါးနိုင်သမျှ ပါးအောင် လှီးပြီး အစေ့များ ထုတ်ပစ်ပါ။",
            "ရေကို အသီး၏ သုံးဆထည့်ပြီး (၁၂) နာရီ ကြာအောင် စိမ်ထားပါ။",
            "ပြီးမှ ၎င်းကို (၁) နာရီခန့် ကျိုပြီးနောက် (၁၂) နာရီကြာ ပြန်ထားကာ ထို့နောက် (၁) နာရီ ထပ်မံ ကျိုပါ။",
            "သစ်သီးကျိုထားသည့် ပြုတ်ရည် (၁) နို့ဆီဘူးဆိုပါက သကြား (၁) နို့ဆီဘူးနှုန်း ရောစပ်ပါ။",
            "ကျောက်ကျောရည်ကဲ့သို့ ဂျယ်လီအနေအထား ရလာသည်အထိ ကျိုပြီး ပန်းကန်ပြားငယ်တွင် အစက်ချ စမ်းသပ်ကာ အနေတော်ဖြစ်လျှင် ပုလင်းထဲထည့်၍ သုံးဆောင်နိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Slice the oranges and lemons as thinly as possible and discard all seeds.",
            "Add water equal to three times the volume of the sliced fruit and let soak for 12 hours.",
            "Simmer the fruit mixture for 1 hour, let stand for 12 hours, then simmer again for another hour until peels are completely tender.",
            "Measure the cooked fruit and liquid: for every 1 tin of boiled fruit liquid, add 1 tin of granulated sugar.",
            "Boil rapidly until the marmalade reaches setting point (test a small drop on a chilled saucer for jelly consistency), then pour into warm sterile jars to set."
        ],
        "tags": {
            "dietary": ["vegan", "vegetarian", "gluten-free", "dairy-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["orange", "lemon", "sugar"]
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
            "pdf_pages": [59],
            "printed_page_numbers": [106],
            "extraction_method": "manual_transcription_verified"
        },
        "data_quality": {
            "extraction_status": "complete",
            "confidence": 1.0,
            "review_notes": "5:5 instruction parity verified. Traditional two-stage soaking and boiling method preserved.",
            "verified": True
        }
    },
    {
        "recipe_id": "R0065",
        "name_mm": "သရက်သီးစိမ်းသနပ်ချို",
        "name_en": "Fresh Green Mango Sweet Chutney",
        "description_mm": "ထုထောင်းထားသော သရက်သီးစိမ်းများကို သကြား၊ ငရုတ်သီးမှုန့်၊ ထောင်းထားသော ပင်စိမ်း၊ ဂျင်းနှင့် ဆားတို့ဖြင့် သမအောင် နယ်စပ်ထားသော လတ်ဆတ် သရက်သီးသနပ်ချို။",
        "description_en": "Crushed crisp green mango tossed with sugar, mild red chili, freshly pounded holy basil, ginger, and salt for an instant sweet-and-spicy chutney.",
        "category": "chutney",
        "meal_types": ["lunch", "dinner", "side_dish"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0104",
                "name_mm": "သရက်သီးစိမ်း",
                "name_en": "Raw green mango",
                "original_name": "သရက်သီးစိမ်း (အလုံးကြီး)",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အခွံခွာ အစေ့ထုတ်ပြီး ရေအေး ၁ နာရီစိမ်ကာ ထုထောင်းထားသော",
                "preparation_note_en": "peeled, seeded, soaked 1 hour, and lightly pounded"
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
                "ingredient_id": "I0041",
                "name_mm": "ငရုတ်သီးခြောက်",
                "name_en": "Dried red chili",
                "original_name": "ငရုတ်သီးမှုန့်",
                "quantity": 0.25,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁/၄ လဖဇ",
                "normalized_quantity": 1.25,
                "normalized_unit": "g",
                "preparation_note_mm": "အမှုန့်",
                "preparation_note_en": "ground chili powder"
            },
            {
                "ingredient_id": "I0082",
                "name_mm": "ပင်စိမ်း",
                "name_en": "Basil",
                "original_name": "ပင်စိမ်း (ထောင်းပြီး)",
                "quantity": 2.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၂ လဖဇ",
                "normalized_quantity": 10.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ထောင်းပြီး",
                "preparation_note_en": "pounded holy basil"
            },
            {
                "ingredient_id": "I0030",
                "name_mm": "ချင်း",
                "name_en": "Ginger",
                "original_name": "ချင်း (ထောင်းပြီး)",
                "quantity": 2.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၂ လဖဇ",
                "normalized_quantity": 10.0,
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
            }
        ],
        "instructions_mm": [
            "သရက်သီးကို အခွံခွာ၍ အစေ့ထုတ်ပြီး အစိတ်များ ပြုလုပ်ကာ ရေအေးဖြင့် (၁) နာရီခန့် စိမ်ထားပါ။",
            "သရက်သီးအသားများကို ချောမွတ်လာအောင် ထုထောင်းထားပါ။",
            "ထုထားသော သရက်သီးအသားထဲသို့ သကြားနှင့် ငရုတ်သီးမှုန့်တို့ ထည့်၍ ရောမွှေပါ။",
            "ထောင်းထားသော ပင်စိမ်း၊ ဂျင်းနှင့် ဆားတို့ကို ထပ်မံထည့်သွင်းပါ။",
            "အားလုံး ကောင်းစွာ သမသွားသည်အထိ သမအောင် မွှေပေးပြီးလျှင် သုံးဆောင်နိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Peel the raw mangoes, remove stones, slice into pieces, and soak in cold water for about 1 hour.",
            "Lightly pound the soaked mango pieces until tender and bruised.",
            "Mix in the sugar and chili powder thoroughly.",
            "Add the freshly pounded holy basil, ginger, and salt.",
            "Stir and toss until well incorporated, then serve fresh as a condiment."
        ],
        "tags": {
            "dietary": ["vegan", "vegetarian", "gluten-free", "dairy-free"],
            "seasonal": ["summer", "all-year"],
            "festival": [],
            "main_ingredients": ["green mango", "basil", "ginger", "sugar"]
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
            "pdf_pages": [59],
            "printed_page_numbers": [107],
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
        "recipe_id": "R0066",
        "name_mm": "ခရမ်းသီးသနပ်ချို",
        "name_en": "Spiced Roasted Eggplant Chutney",
        "description_mm": "ပေါင်းထားသော ခရမ်းသီးအသားကို မုန်ညင်းဆီ၊ ကြက်သွန်နီ၊ ငရုတ်သီးမှုန့်၊ သံပရာရည်နှင့် နွားနို့ဒိန်ချဉ်တို့ဖြင့် မွှေခေါက်စပ်ထားသော အရသာထူးကဲသည့် ခရမ်းသီးသနပ်ချို။",
        "description_en": "Steamed tender eggplant mashed with pungent mustard oil, raw shallots, chili, lime juice, and creamy yogurt into a luscious, savory raita-style chutney.",
        "category": "chutney",
        "meal_types": ["lunch", "dinner", "side_dish"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0078",
                "name_mm": "ခရမ်းသီး",
                "name_en": "Eggplant",
                "original_name": "ခရမ်းသီး (အလုံးကြီး)",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ပေါင်း၍ အစေ့များထုတ်ထားသော",
                "preparation_note_en": "steamed soft and deseeded"
            },
            {
                "ingredient_id": "I0113",
                "name_mm": "မုန်ညင်းဆီ",
                "name_en": "Mustard oil",
                "original_name": "မုန်ညင်းဆီ",
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
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ (ပါးပါးလှီး)",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁ လုံး",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ပါးပါးလှီးထားသော",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ငရုတ်သီးခြောက်",
                "name_en": "Dried red chili",
                "original_name": "ငရုတ်သီးမှုန့်",
                "quantity": 2.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၂ လဖဇ",
                "normalized_quantity": 10.0,
                "normalized_unit": "g",
                "preparation_note_mm": "အမှုန့်",
                "preparation_note_en": "ground chili powder"
            },
            {
                "ingredient_id": "I0106",
                "name_mm": "သံပရာသီး",
                "name_en": "Lime",
                "original_name": "သံပရာရည် (ညှစ်ပြီး)",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "အရည်ညှစ်ထားသော",
                "preparation_note_en": "freshly squeezed juice"
            },
            {
                "ingredient_id": "I0029",
                "name_mm": "ဒိန်ချဉ်",
                "name_en": "Curd / Yogurt",
                "original_name": "နွားနို့ဒိန်ချဉ်",
                "quantity": 2.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၂ စပဇ",
                "normalized_quantity": 30.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "instructions_mm": [
            "ခရမ်းသီးကို ပေါင်း၍ အစေ့များ ထုတ်ပယ်ကာ အသားများကို သီးသန့် ယူထားပါ။",
            "ခရမ်းသီးအသားများကို မုန်ညင်းဆီနှင့် ဆားထည့်၍ ကောင်းစွာ ညက်သည်အထိ ခေါက်ခြေ၍ မွှေပေးပါ။",
            "ထို့နောက် ပါးပါးလှီးထားသော ကြက်သွန်နီနှင့် ငရုတ်သီးမှုန့်တို့ကို ထည့်သွင်းပါ။",
            "လတ်ဆတ်သော သံပရာရည်နှင့် နွားနို့ဒိန်ချဉ်တို့ကို ထည့်ပါ။",
            "အားလုံး နှံ့စပ်သွားအောင် သမအောင် မွှေပေးပြီးလျှင် စားသုံးနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Steam the eggplants until completely soft, scrape out and discard seeds, and collect the tender pulp.",
            "Mash and beat the eggplant pulp with mustard oil and salt until smooth and creamy.",
            "Fold in the thinly sliced shallots and chili powder.",
            "Add the freshly squeezed lime juice and plain yogurt.",
            "Whisk together until thoroughly blended and creamy, then serve."
        ],
        "tags": {
            "dietary": ["vegetarian", "gluten-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["eggplant", "yogurt", "mustard oil", "lime juice", "onion"]
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
            "pdf_pages": [59],
            "printed_page_numbers": [107],
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
        "recipe_id": "R0067",
        "name_mm": "မန်ကျည်းသီးသနပ်ချို",
        "name_en": "Sweet Spiced Tamarind Chutney",
        "description_mm": "အစေ့ထုတ်ထားသော မန်ကျည်းသီးမှည့်ကို ငရုတ်သီး၊ ကြက်သွန်ဖြူ၊ ဂျင်း၊ သစ်ကြံပိုး၊ စပျစ်သီးခြောက်၊ သကြားနှင့် ရှာလကာရည်တို့ဖြင့် ပျစ်နှစ်အောင် အဆက်မပြတ် မွှေကျိုထားသော တာရှည်ခံ သနပ်ချို။",
        "description_en": "Rich simmered tamarind chutney infused with raisins, whole spices, garlic, ginger, sugar, and vinegar, reduced until glossy and thick for long storage.",
        "category": "chutney",
        "meal_types": ["lunch", "dinner", "side_dish"],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "ingredients": [
            {
                "ingredient_id": "I0072",
                "name_mm": "မန်ကျည်းသီး",
                "name_en": "Tamarind",
                "original_name": "မန်ကျည်းသီးမှည့် (အစေ့ထုတ်)",
                "quantity": 55.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅၅ ကျပ်သား",
                "normalized_quantity": 898.1,
                "normalized_unit": "g",
                "preparation_note_mm": "အစေ့ထုတ်ထားသော",
                "preparation_note_en": "seeded ripe tamarind"
            },
            {
                "ingredient_id": "I0041",
                "name_mm": "ငရုတ်သီးခြောက်",
                "name_en": "Dried red chili",
                "original_name": "ငရုတ်သီးမှုန့်",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.65,
                "normalized_unit": "g",
                "preparation_note_mm": "အမှုန့်",
                "preparation_note_en": "ground chili powder"
            },
            {
                "ingredient_id": "I0022",
                "name_mm": "ကြက်သွန်ဖြူ",
                "name_en": "Garlic",
                "original_name": "ကြက်သွန်ဖြူ",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.65,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0030",
                "name_mm": "ချင်း",
                "name_en": "Ginger",
                "original_name": "ချင်း",
                "quantity": 4.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၄ ကျပ်သား",
                "normalized_quantity": 65.3,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0008",
                "name_mm": "သစ်ကြံပိုးခေါက်",
                "name_en": "Cinnamon bark",
                "original_name": "သစ်ကြံပိုး (ထောင်းပြီး)",
                "quantity": 2.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ကျပ်သား",
                "normalized_quantity": 32.65,
                "normalized_unit": "g",
                "preparation_note_mm": "ထောင်းပြီး",
                "preparation_note_en": "ground cinnamon"
            },
            {
                "ingredient_id": "I0033",
                "name_mm": "စပျစ်သီးခြောက်",
                "name_en": "Raisins",
                "original_name": "စပျစ်သီးခြောက် (သန့်ပြီး)",
                "quantity": 8.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၈ ကျပ်သား",
                "normalized_quantity": 130.6,
                "normalized_unit": "g",
                "preparation_note_mm": "သန့်စင်ထားသော",
                "preparation_note_en": "cleaned"
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
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
                "quantity": 27.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂၇ ၁/၂ ကျပ်သား",
                "normalized_quantity": 449.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0049",
                "name_mm": "ရှာလကာရည်",
                "name_en": "Vinegar",
                "original_name": "ရှာလကာရည်",
                "quantity": 2.5,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၂ ၁/၂ နို့ဆီဘူး",
                "normalized_quantity": 750.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ပစ္စည်းများမြုပ်အောင် လိုအပ်ပါက ထပ်ထည့်ရန်",
                "preparation_note_en": "to submerge ingredients"
            }
        ],
        "instructions_mm": [
            "အိုးတစ်လုံးတွင် အစေ့ထုတ်ထားသော မန်ကျည်းသီး၊ ငရုတ်သီးမှုန့်၊ ကြက်သွန်ဖြူ၊ ဂျင်း၊ သစ်ကြံပိုး၊ စပျစ်သီးခြောက်၊ ဆား၊ သကြားနှင့် ရှာလကာရည်တို့ ရော၍ မွှေပါ။",
            "ရှာလကာရည်သည် ပါဝင်သော ပစ္စည်းများအားလုံး မမြုပ်ပါက အနည်းငယ် ထပ်ထည့်ပေးပါ။",
            "လျင်မြန်စွာ ကျက်စေရန် မီးအရှိန် ကောင်းကောင်းဖြင့် စတင် မွှေပေးပါ။",
            "အရည်ပျစ်လာသည်အထိ မကပ်စေရန် ဂရုစိုက်၍ အဆက်မပြတ် မွှေပေးရပါမည်။",
            "ပြီးလျှင် ဖိုမှချကာ အအေးခံပြီး ပုလင်းထဲသို့ထည့်၍ တာရှည် အသုံးပြုနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "In a heavy cooking pot, combine seeded tamarind pulp, chili powder, garlic, ginger, ground cinnamon, cleaned raisins, salt, sugar, and vinegar.",
            "If the ingredients are not fully submerged by vinegar, add a little extra vinegar as needed.",
            "Bring to a vigorous simmer over steady heat, stirring frequently.",
            "Stir continuously without letting the bottom scorch until the chutney reduces to a thick, glossy jam-like consistency.",
            "Remove from heat, let cool completely, and bottle in clean jars for long-term storage."
        ],
        "tags": {
            "dietary": ["vegan", "vegetarian", "gluten-free", "dairy-free"],
            "seasonal": ["all-year"],
            "festival": [],
            "main_ingredients": ["tamarind", "raisins", "vinegar", "sugar", "cinnamon"]
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
            "pdf_pages": [59],
            "printed_page_numbers": [107],
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
