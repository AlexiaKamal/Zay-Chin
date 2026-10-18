# -*- coding: utf-8 -*-
"""
Batch 9: Foreign / Asian Snacks & Pastries (ပြည်ပအစားအစာများ)
Recipes R0128 to R0152 (Book pp. 138-155 / PDF pp. 76-84)
"""

NEW_INGREDIENTS = [
    {
        "ingredient_id": "I0190",
        "name_mm": "တဆေး",
        "name_en": "Yeast",
        "aliases_mm": [],
        "aliases_en": ["dry yeast", "active yeast"],
        "category": "dry_goods",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0191",
        "name_mm": "မာဂျရင်း",
        "name_en": "Margarine",
        "aliases_mm": [],
        "aliases_en": [],
        "category": "dairy",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0192",
        "name_mm": "မရိုးနိစ်ဆော့စ်",
        "name_en": "Mayonnaise",
        "aliases_mm": ["မရိုးနိစ်"],
        "aliases_en": ["mayo"],
        "category": "sauce",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0193",
        "name_mm": "ဒိန်ခဲ",
        "name_en": "Cheese",
        "aliases_mm": ["ချိစ်"],
        "aliases_en": ["cheddar cheese"],
        "category": "dairy",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0194",
        "name_mm": "ဘေကင်ပေါင်ဒါ",
        "name_en": "Baking powder",
        "aliases_mm": ["ပေါင်ဒါ"],
        "aliases_en": [],
        "category": "dry_goods",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0195",
        "name_mm": "ရှောက်ယို",
        "name_en": "Candied citron peel",
        "aliases_mm": [],
        "aliases_en": ["citron preserve"],
        "category": "dry_goods",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0196",
        "name_mm": "ဆိုဒါမှုန့်",
        "name_en": "Baking soda",
        "aliases_mm": ["ဆိုဒါ"],
        "aliases_en": ["bicarbonate of soda"],
        "category": "dry_goods",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0197",
        "name_mm": "သကြားမှုန့်",
        "name_en": "Icing sugar",
        "aliases_mm": ["အိုက်ဆင်သကြား"],
        "aliases_en": ["powdered sugar", "confectioner's sugar"],
        "category": "seasoning",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0198",
        "name_mm": "ဒိန်ချဉ်",
        "name_en": "Yogurt",
        "aliases_mm": ["ဒိန်ချင်"],
        "aliases_en": ["curd"],
        "category": "dairy",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0199",
        "name_mm": "အာတာဂျုံ",
        "name_en": "Atta flour",
        "aliases_mm": ["အာတာမုန့်ညက်"],
        "aliases_en": ["whole wheat atta"],
        "category": "grain",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0200",
        "name_mm": "ဂျုံချော",
        "name_en": "All-purpose flour (Maida)",
        "aliases_mm": ["မိုင်ဒါဂျုံ"],
        "aliases_en": ["maida flour", "refined flour"],
        "category": "grain",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0201",
        "name_mm": "မြေစာဥ",
        "name_en": "Water chestnut",
        "aliases_mm": [],
        "aliases_en": ["Chinese water chestnut"],
        "category": "vegetable",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0202",
        "name_mm": "အရက်",
        "name_en": "Cooking wine",
        "aliases_mm": ["ဟင်းချက်အရက်"],
        "aliases_en": ["Shaoxing wine", "Chinese cooking wine"],
        "category": "sauce",
        "default_unit": "ml"
    },
    {
        "ingredient_id": "I0203",
        "name_mm": "ဖက်ထုပ်ရွက်",
        "name_en": "Wonton wrappers",
        "aliases_mm": ["ဖက်ထုပ်ခွံ"],
        "aliases_en": ["wonton skins"],
        "category": "grain",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0204",
        "name_mm": "ပဲငါးပိရည်",
        "name_en": "Fermented bean paste sauce",
        "aliases_mm": ["ပဲငံပြာရည်အနှစ်"],
        "aliases_en": ["soybean paste"],
        "category": "sauce",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0205",
        "name_mm": "ရှယ်ရီအရက်",
        "name_en": "Sherry cooking wine",
        "aliases_mm": ["ရှယ်ရီဝိုင်"],
        "aliases_en": ["sherry wine"],
        "category": "liquid",
        "default_unit": "ml"
    },
    {
        "ingredient_id": "I0206",
        "name_mm": "သီဟိုဠ်စေ့",
        "name_en": "Cashew nuts",
        "aliases_mm": [],
        "aliases_en": ["cashews"],
        "category": "nut",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0207",
        "name_mm": "ပျားရည်",
        "name_en": "Honey",
        "aliases_mm": [],
        "aliases_en": [],
        "category": "seasoning",
        "default_unit": "ml"
    },
    {
        "ingredient_id": "I0208",
        "name_mm": "နှမ်းနက်စေ့",
        "name_en": "Black sesame seeds",
        "aliases_mm": ["နှမ်းနက်"],
        "aliases_en": ["black sesame"],
        "category": "nut",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0209",
        "name_mm": "မုန်ညင်းစေ့",
        "name_en": "Mustard seeds",
        "aliases_mm": [],
        "aliases_en": ["mustard seed"],
        "category": "spice",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0210",
        "name_mm": "ကော်ပြန့်ရွက်",
        "name_en": "Spring roll wrappers",
        "aliases_mm": ["ကော်ပြန့်ခွံ"],
        "aliases_en": ["spring roll sheets"],
        "category": "grain",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0211",
        "name_mm": "ခရုဆီ",
        "name_en": "Oyster sauce",
        "aliases_mm": [],
        "aliases_en": [],
        "category": "sauce",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0212",
        "name_mm": "ချယ်ရီသီး",
        "name_en": "Glacé cherries",
        "aliases_mm": ["ချယ်ရီယို"],
        "aliases_en": ["candied cherries"],
        "category": "fruit",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0213",
        "name_mm": "ဗနီလာရနံ့",
        "name_en": "Vanilla essence",
        "aliases_mm": ["ဗနီလာ"],
        "aliases_en": ["vanilla extract"],
        "category": "seasoning",
        "default_unit": "ml"
    }
]

BATCH9_RECIPES = [
    {
        "recipe_id": "R0128",
        "name_mm": "ပေါင်မုန့်",
        "name_en": "Bread",
        "description_mm": "ဂျုံမှုန့်၊ တဆေး၊ မာဂျရင်းနှင့် သကြားတို့ဖြင့် စနစ်တကျ နယ်နှပ်ဖုတ်လုပ်ထားသော အခြေခံ ပေါင်မုန့်လုံးကြီး။",
        "description_en": "Classic homemade yeast bread loaves made from wheat flour, yeast, margarine, sugar, and milk, baked to a golden crust.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Breakfast", "Snack"],
        "ingredients": [
            {"ingredient_id": "I0043", "name_mm": "ဂျုံမှုန့်", "name_en": "Wheat flour", "quantity": 2.75, "unit": "ပိဿာ (g)", "notes_mm": "၂ ပိဿာ ၇၅ ကျပ်သား (၄၄၈၈ ဂရမ်)", "notes_en": "2 viss 75 ticals (approx. 4488g)"},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "quantity": 24, "unit": "ကျပ်သား (g)", "notes_mm": "၃၉၁ ဂရမ်", "notes_en": "391g"},
            {"ingredient_id": "I0026", "name_mm": "ကြက်ဥ", "name_en": "Chicken egg", "quantity": 4, "unit": "လုံး (piece)", "notes_mm": None, "notes_en": None},
            {"ingredient_id": "I0191", "name_mm": "မာဂျရင်း", "name_en": "Margarine", "quantity": 24, "unit": "ကျပ်သား (g)", "notes_mm": "၃၉၁ ဂရမ်", "notes_en": "391g"},
            {"ingredient_id": "I0190", "name_mm": "တဆေး", "name_en": "Yeast", "quantity": 8, "unit": "ကျပ်သား (g)", "notes_mm": "၁၃၀ ဂရမ်", "notes_en": "130g"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "quantity": 3, "unit": "ကျပ်သား (g)", "notes_mm": "၄၉ ဂရမ်", "notes_en": "49g"},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "quantity": 8, "unit": "နို့ဆီဘူး (ml)", "notes_mm": "၂၄၀၀ မီလီလီတာ", "notes_en": "2400 ml"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "quantity": "အနည်းငယ်", "unit": "အနည်းငယ် (to taste)", "notes_mm": "ဗန်းသုတ်ရန်", "notes_en": "For greasing pans"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "မုန့်လုပ်ရန် ဂျုံမှုန့်များကို ဆန်ကာချထားပြီး တဆေးကောင်းစွာ ပျော်ဝင်သွားသည်အထိ ကောင်းစွာ မွှေပေးပါ။ ဂျုံမှုန့်ထဲတွင် ပထမ ဇွန်းဖြင့် နောက်လက်ဖြင့် ရောစပ်ကာ နယ်ပါ။",
            "မုန့်ညက်များကို ပန်းကန်လုံး၏ နှုတ်ခမ်းများမှ ခွာထုတ်၍ ဂျုံမှုန့်ပါးပါး ဖြူးထားသော ခုံပေါ်သို့ နယ်ရန် တင်ပါ။",
            "မုန့်ညက်ကို မိမိရှိရာဘက်ဆီသို့ ခေါက်ချိုးယူပြီး လက်ဖဝါးဖြင့် အပြင်သို့ ဖိတွန်းကာ မုန့်ညက်တုံးကို လေးပုံတစ်ပုံ လှည့်၍ ချောမွတ်ကာ ဆွဲဆန့်နိုင်ပြီး ခုံပေါ်တွင် မကပ်တော့သည်အထိ ထပ်ခါတလဲ ဖိနယ်ပေးရပါမည်။",
            "ဆီသုတ်ထားသော ပန်းကန်လုံးတွင် ထည့်၍ ဆီပေပြီးသော အခြမ်းဘက်ကို အပေါ်ဘက်သို့ ရောက်အောင် တစ်ဖက်လှန်ပေးကာ အဝတ်စိုဖြင့် အုပ်၍ ၈၀° မှ ၈၅° ပူနွေးသောနေရာတွင် နှစ်ဆခန့် ပွလာသည်အထိ ၁ ၁/၂ မှ ၂ နာရီခန့် ထားရမည်။",
            "လက်ချောင်း နှစ်ချောင်းကို မုန့်ညက်ပေါ် ဖိနှိပ်ကြည့်ပါက မုန့်ညက်နှစ်ဆ ပွပြီးသောအခါ ချိုင့်ခွက်အဖြစ် ကျန်နေခဲ့မည်။",
            "မုန့်ညက်နှစ်ထဲသို့ လက်သီးဆုပ်ကို ထိုးထည့်ပြီး ပန်းကန်လုံး နှုတ်ခမ်းပေါ် တက်လာသော အနားစွန်းမှ အလယ်သို့ ဆွဲယူလှန်ပေးကာ ထုထည် နှစ်ဆခန့် ပွလာအောင် ထပ်မံ၍ ၃၀ မှ ၄၅ မိနစ်ခန့် ထားပါ။",
            "မုန့်ညက်နှစ်ကို ပုံလောင်းရန်နှင့် ပုံသွင်းရန် အပိုင်းများ ခွဲရပါမည် (အရွယ်အစားမှာ ပြုလုပ်နည်းလမ်းညွှန်ကို လိုက်၍ အမျိုးမျိုးရှိသည်)။ အဖုံးအုပ်၍ ၁၀ မိနစ်ခန့် ဆက်လက်ထားပါ။",
            "မုန့်ညက်ကို ဘဲဥပုံပြား၍ လေအားလုံး ထွက်အောင် ဖိပြီး လက်သီးဆုပ်ထားသော လက်ချောင်း နောက်ဘက်နှင့် ဖိနယ်ပါ။",
            "မုန့်ညက်ကို အလျားလိုက် တစ်ဝက်ခေါက်ချိုး၍ လေထွက်အောင် ထပ်မံပြားအောင် ဖိပေးပါ။",
            "မုန့်ညက်ကို အဖျားနှစ်ဖက်မှမ၍ ဆွဲယူပြီး ၁၅ လက်မ x ၅ လက်မ အရွယ်ထိ ရှည်ထွက်လာအောင် စားပွဲနှင့် အကြိမ်များစွာ ရိုက်ခါ ပေးပါ။",
            "အဖျားနှစ်ဖက်ကို အလယ်သို့ ယူလာ၍ ထပ်ကာထပ်ကာ လက်ခေါက်ဖြင့် တင်းကျပ်စွာ ဖိနှိပ်၍ ကောင်းစွာ ဖိပြီး နောက်ဘက်သို့ လှိမ့်၍ ရှေ့သို့ တင်းကျပ်စွာ တွန်းပါ။",
            "မုန့်ခွက်ထဲသို့ အနားသတ်ထားသော အစွန်းကို အောက်ဘက်တွင် ထား၍ ထည့်ကာ ၅၀ မှ ၆၀ မိနစ်ခန့် ပွလာအောင် ထားပြီး ၄၅၀°F အပူပေးထားသော မီးဖိုထဲတွင် ရွှေဝါရောင် သန်းလာသည်အထိ ဖုတ်ပါ။"
        ],
        "instructions_en": [
            "Sift the flour for bread making and stir well until the yeast is completely dissolved; mix into the flour first using a spoon, then knead with your hands.",
            "Scrape the dough cleanly away from the edges of the mixing bowl and place onto a lightly floured board ready for kneading.",
            "Fold the dough toward yourself, push firmly outward with the palms of your hands, rotate the dough a quarter turn, and repeatedly knead until smooth, elastic, and no longer sticking to the board.",
            "Place into a greased bowl, flip so the greased side faces upward, cover with a damp cloth, and rest in a warm spot at 80°–85°F for 1.5 to 2 hours until doubled in volume.",
            "Press two fingertips into the dough; when the dough has properly doubled in size, the indentations will stay depressed.",
            "Punch your fist straight into the center of the dough, pull the risen edges from the rim inward to fold, and rest for another 30 to 45 minutes to rise again.",
            "Divide the dough into portions for molding into loaves according to the desired sizes; cover and let rest for about 10 minutes.",
            "Flatten the dough into an oval shape to expel all trapped air, pressing down firmly using the knuckles of your clenched fists.",
            "Fold the dough lengthwise in half and press down firmly once more to remove any remaining trapped air bubbles.",
            "Hold the dough by both ends, stretch it out to roughly 15 by 5 inches, and slap it against the table surface several times.",
            "Bring both ends to the center, press firmly with the heels of your hands to seal, roll backward, and push firmly forward into a tight loaf shape.",
            "Place seam side down into greased loaf pans, let rise for 50 to 60 minutes until doubled, and bake in a preheated oven at 450°F until richly golden brown."
        ],
        "tags": ["Bread", "Baking", "Yeast", "Homemade Bread", "Breakfast"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 138},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook pp. 138-142 with visual reference"}
    },
    {
        "recipe_id": "R0129",
        "name_mm": "ကြက်သားညှပ်ပေါင်မုန့်",
        "name_en": "Chicken Sandwiches",
        "description_mm": "ပြုတ်ထားသော ကြက်ရင်အုပ်သား၊ မရိုးနီးစ်ဆော့စ်နှင့် ထောပတ်အနှစ်တို့ဖြင့် သုတ်လိမ်းပြုလုပ်ထားသော အသားညှပ်ပေါင်မုန့်။",
        "description_en": "Tender poached chicken breast mixed with a seasoned mayonnaise and butter spread, layered between sandwich bread slices.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Breakfast", "Snack", "Lunch"],
        "ingredients": [
            {"ingredient_id": "I0074", "name_mm": "ပေါင်မုန့်", "name_en": "Bread", "quantity": 20, "unit": "ချပ် (slice)", "notes_mm": "ပုံမှန်လှီးထား", "notes_en": "Regular sliced"},
            {"ingredient_id": "I0039", "name_mm": "ငရုတ်ကောင်းမှုန့်", "name_en": "Ground black pepper", "quantity": 0.25, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၁/၄ လဖဇ", "notes_en": "1/4 tsp"},
            {"ingredient_id": "I0192", "name_mm": "မရိုးနိစ်ဆော့စ်", "name_en": "Mayonnaise", "quantity": 4, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၄ လဖဇ", "notes_en": "4 tsp"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "quantity": 0.5, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၁/၂ လဖဇ", "notes_en": "1/2 tsp"},
            {"ingredient_id": "I0028", "name_mm": "ကြက်ရင်အုပ်သား", "name_en": "Chicken breast", "quantity": 2, "unit": "အုပ် (breast)", "notes_mm": "၂ အုပ်", "notes_en": "2 whole breasts"},
            {"ingredient_id": "I0002", "name_mm": "ထောပတ်", "name_en": "Butter", "quantity": 0.17, "unit": "နို့ဆီဘူး (g)", "notes_mm": "၁/၆ နို့ဆီဘူး (၅၀ ဂရမ်)", "notes_en": "1/6 tin (approx. 50g salted butter)"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "မရိုးနီးစ်ဆော့စ်၊ ထောပတ်၊ ငရုတ်ကောင်းနှင့် ဆားတို့ကို အနှစ်ကျအောင် သမအောင် ရောမွှေပါ။",
            "ကြက်သားကို ဆား၊ ရေတို့ဖြင့် နူးသည်အထိ ပြုတ်ကာ အမျှင်များ လျှီးစိတ်ပါ။",
            "ပေါင်မုန့်ချပ်ပေါ်တွင် ထောပတ်မရိုးနီးစ်အနှစ်များ သုတ်လိမ်းပြီး ကြက်သားဖတ်များ ဖြန့်တင်ကာ ပေါင်မုန့်တစ်ချပ်ဖြင့် ပိုးအုပ်ပြီး အနားသားများ လှီးဖြတ်၍ တြိဂံပုံ သို့မဟုတ် လေးထောင့်ပုံ လှီးကာ တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "Mix mayonnaise, softened butter, black pepper, and salt together until smooth and well blended.",
            "Poach chicken breast in water with a pinch of salt until tender, then slice or shred finely.",
            "Spread the seasoned butter-mayonnaise paste onto bread slices, layer evenly with shredded chicken, top with another slice of bread, trim crusts, and slice into triangles or finger sandwiches to serve."
        ],
        "tags": ["Sandwich", "Chicken", "Mayonnaise", "Snack", "Finger Food"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 143},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 143"}
    },
    {
        "recipe_id": "R0130",
        "name_mm": "ခရမ်းချဉ်သီးဒိန်ခဲပီဇာမုန့်",
        "name_en": "Tomato and Cheese Pizza",
        "description_mm": "တဆေးဖြင့် နှပ်ထားသော ဂျုံမုန့်ပြားပေါ်တွင် ခရမ်းချဉ်သီးဆော့စ်၊ ကြက်သွန်နီနှင့် ခြစ်ထားသော ဒိန်ခဲတို့ တင်၍ ဖုတ်ထားသော ပီဇာမုန့်။",
        "description_en": "Homemade pizza featuring a yeast crust topped with savory cooked tomato sauce, sliced onions, and melted grated cheese.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Lunch", "Dinner", "Snack"],
        "ingredients": [
            {"ingredient_id": "I0190", "name_mm": "တဆေး", "name_en": "Yeast", "quantity": 0.5, "unit": "ကျပ်သား (g)", "notes_mm": "၁/၂ ကျပ်သား (၈ ဂရမ်)", "notes_en": "0.5 tical (approx. 8g)"},
            {"ingredient_id": "I0043", "name_mm": "ဂျုံမှုန့်", "name_en": "Wheat flour", "quantity": 35, "unit": "ကျပ်သား (g)", "notes_mm": "ဆန်ကာချပြီး (၅၇၁ ဂရမ်)", "notes_en": "Sifted (approx. 571g)"},
            {"ingredient_id": "I0012", "name_mm": "ရေနွေး", "name_en": "Hot water", "quantity": 0.17, "unit": "နို့ဆီဘူး (ml)", "notes_mm": "ရေနွေးနွေး ၁/၆ နို့ဆီဘူး (၅၀ မီလီလီတာ)", "notes_en": "Lukewarm water 1/6 tin (50 ml)"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "quantity": 1, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၁ လဖဇ (မုန့်သားအတွက်)", "notes_en": "1 tsp (for dough)"},
            {"ingredient_id": "I0002", "name_mm": "ထောပတ်", "name_en": "Butter", "quantity": 10, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၁၀ လဖဇ (၅၀ ဂရမ်)", "notes_en": "10 tsp (approx. 50g)"},
            {"ingredient_id": "I0042", "name_mm": "ခရမ်းချဉ်သီး", "name_en": "Tomato", "quantity": 65, "unit": "ကျပ်သား (g)", "notes_mm": "လှီးပြီး (၁၀၆၀ ဂရမ်)", "notes_en": "Sliced (approx. 1060g)"},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "quantity": 2, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၂ လဖဇ", "notes_en": "2 tsp"},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "quantity": 10, "unit": "ကျပ်သား (g)", "notes_mm": "လှီးပြီး (၁၆၃ ဂရမ်)", "notes_en": "Sliced (approx. 163g)"},
            {"ingredient_id": "I0039", "name_mm": "ငရုတ်ကောင်းမှုန့်", "name_en": "Ground black pepper", "quantity": 0.5, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၁/၂ လဖဇ", "notes_en": "1/2 tsp"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "quantity": 1, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၁ လဖဇ (အဆာအတွက်)", "notes_en": "1 tsp (for topping sauce)"},
            {"ingredient_id": "I0193", "name_mm": "ဒိန်ခဲ", "name_en": "Cheese", "quantity": 0.5, "unit": "နို့ဆီဘူး (g)", "notes_mm": "ခြစ်ထား ၁/၂ နို့ဆီဘူး (၁၅၀ ဂရမ်)", "notes_en": "Grated cheese 1/2 tin (approx. 150g)"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "တဆေးကို ရေနွေးနွေးဖြင့် (၁၀) မိနစ်ခန့် ပွလာအောင် စိမ်ထားပါ။ ဂျုံမှုန့်၊ ဖောက်ထားသော တဆေးနှင့် ထောပတ်တို့ကို စေးပိုင်ချောမွတ်နေအောင် နယ်ထားပါ။",
            "ဂျုံအလုံးလုပ်၍ ပွအောင် (၂) နာရီခန့် ထားလျှင် နှစ်ဆ ပွလာပါမည်။ ဂျုံမှုန့်ဖြူးထားသော စားပွဲပေါ်သို့ ဂျုံလုံးတင်ပြီး ညင်သာစွာ ဖိကာ အဝိုင်းပြား သို့မဟုတ် လေးထောင့်ပြား ပြုလုပ်ပါ။",
            "ခရမ်းချဉ်သီးကို နူးသည်အထိ ချက်ပြီး ဆန်ကာဖြင့် စစ်ပါ၊ ဆား၊ ငရုတ်ကောင်းနှင့် သကြားထည့်၍ ပျစ်လာသည်အထိ ရောမွှေကာ အအေးခံထားပါ။",
            "ပီဇာမုန့်ညက်ပြားပေါ်သို့ ခရမ်းချဉ်သီးအနှစ် လောင်းထည့်ပြီး အပေါ်မှ ကြက်သွန်နီလှီးထားသည်များနှင့် ခြစ်ထားသော ဒိန်ခဲများ ဖြူးထည့်ပြီး မိနစ် (၂၀) ခန့် မီးဖိုတွင် ဖုတ်ပါ။"
        ],
        "instructions_en": [
            "Proof yeast in lukewarm water for about 10 minutes until frothy; knead flour, proofed yeast, salt, and butter together until a smooth, pliable dough forms.",
            "Shape into a ball, cover, and let rise for about 2 hours until doubled in bulk; roll gently on a floured surface into flat rounds or rectangles.",
            "Simmer sliced tomatoes until tender, pass through a sieve to make puree, simmer with salt, pepper, and sugar until thick, and let cool.",
            "Spread the tomato puree over the pizza bases, scatter sliced onions and grated cheese generously over the top, and bake in a preheated oven for about 20 minutes until melted and bubbling."
        ],
        "tags": ["Pizza", "Baking", "Cheese", "Tomato", "Italian-Inspired"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 143},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 143"}
    },
    {
        "recipe_id": "R0131",
        "name_mm": "ပလိန်းကိတ်",
        "name_en": "Plain Cake",
        "description_mm": "ဂျုံမှုန့်၊ မာဂျရင်း၊ သကြား၊ ကြက်ဥနှင့် ဗနီလာရနံ့တို့ဖြင့် ရိုက်မွှေဖုတ်လုပ်ထားသော ဂန္ထဝင် ပလိန်းကိတ်မုန့်။",
        "description_en": "Classic plain sponge cake made with creamed margarine and sugar, eggs, sifted flour, baking powder, and aromatic vanilla.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Snack", "Tea Time"],
        "ingredients": [
            {"ingredient_id": "I0043", "name_mm": "ဂျုံမှုန့်", "name_en": "Wheat flour", "quantity": 75, "unit": "ကျပ်သား (g)", "notes_mm": "ဆန်ကာချပြီး (၁၂၂၄ ဂရမ်)", "notes_en": "Sifted (approx. 1224g)"},
            {"ingredient_id": "I0194", "name_mm": "ဘေကင်ပေါင်ဒါ", "name_en": "Baking powder", "quantity": 2, "unit": "ကျပ်သား (g)", "notes_mm": "၃၃ ဂရမ်", "notes_en": "33g"},
            {"ingredient_id": "I0191", "name_mm": "မာဂျရင်း", "name_en": "Margarine", "quantity": 57, "unit": "ကျပ်သား (g)", "notes_mm": "၉၃၀ ဂရမ်", "notes_en": "930g"},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "quantity": 57, "unit": "ကျပ်သား (g)", "notes_mm": "၉၃၀ ဂရမ်", "notes_en": "930g"},
            {"ingredient_id": "I0213", "name_mm": "ဗနီလာရနံ့", "name_en": "Vanilla essence", "quantity": 1, "unit": "ကျပ်သား (g)", "notes_mm": "၁၆ ဂရမ်", "notes_en": "16g"},
            {"ingredient_id": "I0026", "name_mm": "ကြက်ဥ", "name_en": "Chicken egg", "quantity": 22, "unit": "လုံး (piece)", "notes_mm": "၂၂ လုံး", "notes_en": "22 eggs"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "မုန့်ခွက်များကို မာဂျရင်းသုတ်ပြီး အောက်ခံစက္ကူဖြတ်ထည့်ကာ အသင့်ပြုလုပ်ထားပါ။ လျှပ်စစ်မုန့်ဖုတ်ဖိုကို အပူချိန် ၃၅၀°F အထိ ဖွင့်ထားပါ။",
            "ဆန်ကာချထားသော ဂျုံမှုန့်ပေါ်သို့ ဘေကင်ပေါင်ဒါကို ဖြန့်ထည့်ထားပါ။",
            "မာဂျရင်းနှင့် သကြားကို သကြားကြေပြီး ပွလာသည်အထိ လက်ဖြင့် မွှေပါ။ ဗနီလာရနံ့များ ထည့်ပြီး မိနစ် (၂၀) ခန့် ဆက်ရိုက်ပါ။",
            "ဖြူ၍ ပွလာလျှင် ကြက်ဥတစ်လုံးချင်း ထည့်၍ သမအောင် မွှေပြီး ဂျုံနှင့် ဘေကင်ပေါင်ဒါတို့ကိုပါ ရောထည့်ပြီး မုန့်ညက်ပျစ်ပျစ် အနေရလာအောင် ရောစပ်ပါ။",
            "မုန့်ခွက်အတွင်းသို့ ထည့်ပြီး မုန့်ဖုတ်ဖိုထဲ သွင်း၍ (၄၅) မိနစ်ခန့် ဖုတ်ပါ။"
        ],
        "instructions_en": [
            "Grease cake pans with margarine, line bottoms with parchment paper, and preheat oven to 350°F.",
            "Sift flour and baking powder together thoroughly.",
            "Cream margarine and sugar together by hand until pale, light, and fluffy; stir in vanilla essence and continue beating for about 20 minutes.",
            "Beat in eggs one at a time until completely blended, then gently fold in the sifted flour and baking powder mixture to produce a smooth, thick batter.",
            "Pour batter into the prepared pans and bake in the preheated oven for about 45 minutes until golden and cooked through."
        ],
        "tags": ["Cake", "Baking", "Sponge Cake", "Dessert", "Tea Time"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 144},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 144"}
    },
    {
        "recipe_id": "R0132",
        "name_mm": "သစ်သီးကိတ်မုန့်",
        "name_en": "Fruit Cake",
        "description_mm": "ချယ်ရီသီး၊ စပျစ်သီးခြောက်နှင့် ရှောက်ယိုတို့ ပါဝင်သော ရောင်စုံ သစ်သီးစုံ ကိတ်မုန့်။",
        "description_en": "Rich fruit cake loaded with diced glacé cherries, raisins, candied citron peel, creamed margarine, eggs, and vanilla.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Snack", "Tea Time"],
        "ingredients": [
            {"ingredient_id": "I0154", "name_mm": "အစာအရောင်ဆိုးဆေး", "name_en": "Food coloring", "quantity": "အနည်းငယ်", "unit": "အနည်းငယ် (to taste)", "notes_mm": "အစိမ်းနှင့် အနီရောင်", "notes_en": "Green and red coloring"},
            {"ingredient_id": "I0212", "name_mm": "ချယ်ရီသီး", "name_en": "Glacé cherries", "quantity": 7, "unit": "ကျပ်သား (g)", "notes_mm": "၁၁၄ ဂရမ်", "notes_en": "114g"},
            {"ingredient_id": "I0033", "name_mm": "စပျစ်သီးခြောက်", "name_en": "Raisins", "quantity": 10, "unit": "ကျပ်သား (g)", "notes_mm": "၁၆၃ ဂရမ်", "notes_en": "163g"},
            {"ingredient_id": "I0195", "name_mm": "ရှောက်ယို", "name_en": "Candied citron peel", "quantity": 10, "unit": "ကျပ်သား (g)", "notes_mm": "၁၆၃ ဂရမ်", "notes_en": "163g"},
            {"ingredient_id": "I0043", "name_mm": "ဂျုံမှုန့်", "name_en": "Wheat flour", "quantity": 75, "unit": "ကျပ်သား (g)", "notes_mm": "ဆန်ကာချပြီး (၁၂၂၄ ဂရမ်)", "notes_en": "Sifted (approx. 1224g)"},
            {"ingredient_id": "I0194", "name_mm": "ဘေကင်ပေါင်ဒါ", "name_en": "Baking powder", "quantity": 2, "unit": "ကျပ်သား (g)", "notes_mm": "၃၃ ဂရမ်", "notes_en": "33g"},
            {"ingredient_id": "I0026", "name_mm": "ကြက်ဥ", "name_en": "Chicken egg", "quantity": 22, "unit": "လုံး (piece)", "notes_mm": "၂၂ လုံး", "notes_en": "22 eggs"},
            {"ingredient_id": "I0191", "name_mm": "မာဂျရင်း", "name_en": "Margarine", "quantity": 57, "unit": "ကျပ်သား (g)", "notes_mm": "၉၃၀ ဂရမ်", "notes_en": "930g"},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "quantity": 57, "unit": "ကျပ်သား (g)", "notes_mm": "၉၃၀ ဂရမ်", "notes_en": "930g"},
            {"ingredient_id": "I0213", "name_mm": "ဗနီလာရနံ့", "name_en": "Vanilla essence", "quantity": 1, "unit": "ကျပ်သား (g)", "notes_mm": "၁၆ ဂရမ်", "notes_en": "16g"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "မုန့်ခွက်များကို မာဂျရင်းသုတ်ပြီး အောက်ခံစက္ကူဖြတ်ထည့်ကာ အသင့်ပြုလုပ်ထားပါ။ လျှပ်စစ်မုန့်ဖုတ်ဖိုကို အပူချိန် ၃၅၀°F အထိ ဖွင့်ထားပါ။",
            "ချယ်ရီ၊ စပျစ်သီးခြောက်၊ ရှောက်ယိုတို့ကို အစိမ်းရောင်နှင့် အနီရောင် ရောစပ်ကာ အသင့်ပြင်ထားပါ။",
            "မာဂျရင်းနှင့် သကြားကို ကြေပြီး ပွလာသည်အထိ လက်ဖြင့် မွှေပါ။ ဗနီလာရနံ့ထည့်ပြီး မိနစ် (၂၀) ခန့် ဆက်မွှေပါ။",
            "ပွလာလျှင် ကြက်ဥတစ်လုံးချင်း ထည့်မွှေပြီး ဂျုံနှင့် ဘေကင်ပေါင်ဒါတို့ကို ရောထည့်ကာ သစ်သီးများပါ ရောနယ်ပြီး သမအောင် မွှေပါ။",
            "မုန့်ခွက်အတွင်း ထည့်၍ (၄၅) မိနစ်ခန့် မုန့်ဖုတ်ဖိုတွင် ဖုတ်ပါ။"
        ],
        "instructions_en": [
            "Grease baking pans with margarine, line bottoms with parchment paper, and preheat oven to 350°F.",
            "Dice the cherries, raisins, and candied peel, tossing them lightly to mix.",
            "Cream margarine and sugar together until pale and fluffy; add vanilla essence and continue beating for about 20 minutes.",
            "Beat in eggs one at a time, fold in sifted flour and baking powder, and gently incorporate the prepared mixed candied fruits.",
            "Pour into prepared pans and bake in the oven for about 45 minutes until richly browned and baked through."
        ],
        "tags": ["Fruit Cake", "Baking", "Festive", "Dessert", "Tea Time"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 144},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 144"}
    },
    {
        "recipe_id": "R0133",
        "name_mm": "ဒိုးနတ်",
        "name_en": "Doughnut",
        "description_mm": "ဂျုံမှုန့်၊ ဒိန်ချဉ်၊ ထောပတ်နှင့် ကြက်ဥတို့ဖြင့် နယ်ပြီး အဝိုင်းပုံဖော်ကာ ကြော်ထားသော ဒိုးနတ်မုန့်ကြော်။",
        "description_en": "Classic fried ring doughnuts made with flour, yogurt, butter, and eggs, fried to a golden brown and dusted with sugar.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Snack", "Breakfast"],
        "ingredients": [
            {"ingredient_id": "I0043", "name_mm": "ဂျုံမှုန့်", "name_en": "Wheat flour", "quantity": 0.83, "unit": "နို့ဆီဘူး (g)", "notes_mm": "၅/၆ နို့ဆီဘူး (၂၅၀ ဂရမ်)", "notes_en": "5/6 tin (approx. 250g)"},
            {"ingredient_id": "I0213", "name_mm": "ဗနီလာရနံ့", "name_en": "Vanilla essence", "quantity": 0.33, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၁/၃ လဖဇ", "notes_en": "1/3 tsp"},
            {"ingredient_id": "I0196", "name_mm": "ဆိုဒါမှုန့်", "name_en": "Baking soda", "quantity": 0.25, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၁/၄ လဖဇ", "notes_en": "1/4 tsp"},
            {"ingredient_id": "I0194", "name_mm": "ဘေကင်ပေါင်ဒါ", "name_en": "Baking powder", "quantity": 0.5, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၁/၂ လဖဇ", "notes_en": "1/2 tsp"},
            {"ingredient_id": "I0026", "name_mm": "ကြက်ဥ", "name_en": "Chicken egg", "quantity": 1, "unit": "လုံး (piece)", "notes_mm": "အသေး ၁ လုံး", "notes_en": "1 small egg"},
            {"ingredient_id": "I0197", "name_mm": "သကြားမှုန့်", "name_en": "Icing sugar", "quantity": 9, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "၉ စပဇ", "notes_en": "9 tbsp"},
            {"ingredient_id": "I0198", "name_mm": "ဒိန်ချဉ်", "name_en": "Yogurt", "quantity": 3, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "၃ စပဇ", "notes_en": "3 tbsp"},
            {"ingredient_id": "I0002", "name_mm": "ထောပတ်", "name_en": "Butter", "quantity": 1, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "၁ စပဇ", "notes_en": "1 tbsp"},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "quantity": 0.17, "unit": "နို့ဆီဘူး (g)", "notes_mm": "၁/၆ နို့ဆီဘူး (၅၀ ဂရမ်)", "notes_en": "1/6 tin (approx. 50g)"},
            {"ingredient_id": "I0002", "name_mm": "ထောပတ်", "name_en": "Butter", "quantity": "လိုအပ်သရွေ့", "unit": "လိုအပ်သရွေ့ (as needed)", "notes_mm": "ကြော်ရန်", "notes_en": "Butter/oil for frying as needed"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "ဂျုံမှုန့်၊ ဆိုဒါနှင့် ဘေကင်ပေါင်ဒါတို့ကို ခေါက်မွှေထားသော ကြက်ဥ၊ သကြားမှုန့်၊ ဒိန်ချဉ်၊ ထောပတ်၊ ဗနီလာရနံ့တို့ဖြင့် ရောစပ်ကာ ချောမွတ်လာသည်အထိ နယ်ပါ။",
            "၁/၂ လက်မ အထူအလိပ် လိပ်ကာ ဒိုးနတ်ပုံစံ အဝိုင်းပုံ လှီးဖြတ် ပြုလုပ်ပါ။",
            "ပူနေသော ထောပတ် သို့မဟုတ် ဆီတွင် မုန့် ၄ (သို့) ၅ ခု ထည့်၍ နှစ်ဆခန့် ပွလာအောင် ရွှေဝါရောင်သန်းလာသည်အထိ မီးအေးအေးဖြင့် လှန်လှော ကြော်ပေးပါ။",
            "ဆယ်ယူပြီး ဆီစစ်ကာ သကြားမှုန့် ချက်ချင်း ဖြူးပေးပြီး လက်ဖက်ရည်၊ ကော်ဖီတို့ဖြင့် တွဲဖက် တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "Combine sifted flour, baking soda, and baking powder with beaten egg, powdered sugar, yogurt, butter, and vanilla; knead until a smooth dough forms.",
            "Roll the dough out to roughly 1/2-inch thickness and cut into ring doughnuts with center holes.",
            "Fry 4 to 5 doughnuts at a time in hot butter or oil over gentle heat, turning until doubled in puff and evenly golden brown.",
            "Remove, drain on paper towels, dust immediately with icing sugar, and serve warm with tea or coffee."
        ],
        "tags": ["Doughnut", "Pastry", "Fried Snack", "Tea Time", "Sweet"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 145},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 145"}
    },
    {
        "recipe_id": "R0134",
        "name_mm": "သကြားရည်အုပ်ပူတင်း",
        "name_en": "Caramel-Coated Custard",
        "description_mm": "သကြားတူးရည်ဖြင့် အောက်ခံသုတ်လိမ်းထားသော ခွက်ထဲတွင် ကြက်ဥ၊ နွားနို့နှင့် သကြားတို့ ပေါင်းခံထားသော ကာရာမယ် ပူတင်း။",
        "description_en": "Silky steamed egg and milk custard baked over a deep amber caramel base that coats the pudding when inverted.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Dessert", "Snack"],
        "ingredients": [
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "quantity": 0.5, "unit": "နို့ဆီဘူး (g)", "notes_mm": "သကြားရည်အတွက် ၃/၆ နို့ဆီဘူး (၁၅၀ ဂရမ်)", "notes_en": "For caramel 1/2 tin (approx. 150g)"},
            {"ingredient_id": "I0012", "name_mm": "ရေနွေး", "name_en": "Hot water", "quantity": 2, "unit": "စားပွဲဇွန်း (tbsp / ml)", "notes_mm": "၂ စပဇ", "notes_en": "2 tbsp"},
            {"ingredient_id": "I0026", "name_mm": "ကြက်ဥ", "name_en": "Chicken egg", "quantity": 6, "unit": "လုံး (piece)", "notes_mm": "၆ လုံး", "notes_en": "6 eggs"},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "quantity": 0.5, "unit": "နို့ဆီဘူး (g)", "notes_mm": "ပူတင်းအတွက် ၁/၂ နို့ဆီဘူး (၁၅၀ ဂရမ်)", "notes_en": "For custard 1/2 tin (approx. 150g)"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "quantity": 0.25, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၁/၄ လဖဇ", "notes_en": "1/4 tsp"},
            {"ingredient_id": "I0036", "name_mm": "နွားနို့", "name_en": "Cow milk", "quantity": 1.83, "unit": "နို့ဆီဘူး (ml)", "notes_mm": "၁ ၅/၆ နို့ဆီဘူး (၅၅၀ မီလီလီတာ)", "notes_en": "1 5/6 tins (approx. 550 ml)"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "မုန့်ဖုတ်အိုးတွင် သကြား ၁/၂ ခွက်နှင့် ရေနွေးထည့်ပြီး မီးဖိုပေါ်တွင် တင်ကာ နီညိုရောင် သန်းလာအောင် ကာရာမယ် ပြုလုပ်ပါ။",
            "မီးဖိုမှ ဖယ်ပြီး အိုးအတွင်း အောက်ခြေ ပတ်လည်တွင် သကြားတူးရေ နှံ့အောင်ထားပြီး အအေးခံပါ။",
            "ကြက်ဥ၊ သကြား၊ ဆားနှင့် နွားနို့တို့ကို သမအောင် မွှေပြီး သကြားတူးရေ အေးခဲနေသည့် အပေါ်တွင် ကြက်ဥအရောများကို လောင်းထည့်ပါ။",
            "အဖုံးပိတ်ကာ တဖြည်းဖြည်း ဆူပွက်နေသော ရေဆူအိုးတွင် (၄၅) မိနစ်ခန့် ပေါင်းပြီး အအေးခံကာ ပန်းကန်ပြားထဲသို့ မှောက်ချ တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "In a saucepan or mold, cook sugar and hot water together over medium heat until melted into a rich amber caramel.",
            "Remove from heat, swirl gently to coat the bottom and sides of the mold, and let cool until set.",
            "Whisk eggs, sugar, salt, and milk until smooth; strain the custard mixture into the caramel-coated mold.",
            "Cover tightly, steam over gently simmering water for about 45 minutes until set, chill thoroughly, and invert onto a plate to serve."
        ],
        "tags": ["Pudding", "Custard", "Caramel", "Dessert", "Steamed"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 145},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 145"}
    },
    {
        "recipe_id": "R0135",
        "name_mm": "ကြက်ဥနှစ်ပေါင်မုန့်ကြော်",
        "name_en": "Bombay Toast",
        "description_mm": "ကြက်ဥနှင့် နွားနို့တွင် စိမ်ပြီး ဒယ်အိုးတွင် ရွှေဝါရောင်သန်းသည်အထိ ကြော်ကာ သကြားဖြူးထားသော ပေါင်မုန့်ကြော်။",
        "description_en": "French toast or Bombay toast made by soaking bread in egg and milk, pan-frying until golden, and dusting with sugar.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Breakfast", "Snack"],
        "ingredients": [
            {"ingredient_id": "I0074", "name_mm": "ပေါင်မုန့်", "name_en": "Bread", "quantity": 10, "unit": "ချပ် (slice)", "notes_mm": "ပုံမှန်လှီးထား ၁၀ ချပ်", "notes_en": "Regular sliced 10 pieces"},
            {"ingredient_id": "I0036", "name_mm": "နွားနို့", "name_en": "Cow milk", "quantity": 5, "unit": "စားပွဲဇွန်း (tbsp / ml)", "notes_mm": "၅ စပဇ", "notes_en": "5 tbsp"},
            {"ingredient_id": "I0026", "name_mm": "ကြက်ဥ", "name_en": "Chicken egg", "quantity": 5, "unit": "လုံး (piece)", "notes_mm": "ခေါက်ထား ၅ လုံး", "notes_en": "5 eggs, beaten"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "quantity": "အနည်းငယ်", "unit": "အနည်းငယ် (to taste)", "notes_mm": None, "notes_en": None},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "quantity": 10, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "၁၀ စပဇ", "notes_en": "10 tbsp"},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "quantity": 10, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "၁၀ စပဇ", "notes_en": "10 tbsp"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "နွားနို့၊ ကြက်ဥနှင့် ဆားအနည်းငယ်ကို ရောမွှေပါ။",
            "ပေါင်မုန့်ချပ်များကို ကြက်ဥ နွားနို့အရောတွင် စိုစွတ်သည်အထိ နှစ်စိမ်လိုက်ပါ။",
            "ဆီပူတွင် ပေါင်မုန့်များကို အညိုရောင် သန်းသည်အထိ မီးအလယ်အလတ်ဖြင့် ကြော်ပြီး သကြားဖြူးကာ ပူပူနွေးနွေး တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "Whisk milk, beaten eggs, and a pinch of salt together in a shallow dish.",
            "Dip each bread slice into the egg and milk mixture until thoroughly saturated.",
            "Fry in hot oil over medium heat until golden brown on both sides, drain, sprinkle generously with sugar, and serve hot."
        ],
        "tags": ["Toast", "French Toast", "Breakfast", "Snack", "Sweet"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 146},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 146"}
    },
    {
        "recipe_id": "R0136",
        "name_mm": "ဒိန်ခဲချောင်း",
        "name_en": "Cheese Straws",
        "description_mm": "ဂျုံမှုန့်၊ ဒိန်ခဲအမာခြစ်၊ မာဂျရင်းနှင့် ကြက်ဥအနှစ်တို့ဖြင့် နယ်ပြီး အချောင်းလေးများ ပြုလုပ်ကာ ဖုတ်ထားသော အဆာပြေမုန့်။",
        "description_en": "Crisp and flaky savory baked cheese straws made with grated hard cheese, flour, margarine, pepper, and egg yolk.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Snack", "Tea Time"],
        "ingredients": [
            {"ingredient_id": "I0043", "name_mm": "ဂျုံမှုန့်", "name_en": "Wheat flour", "quantity": 10, "unit": "ကျပ်သား (g)", "notes_mm": "၁၆၃ ဂရမ်", "notes_en": "163g"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "quantity": "အနည်းငယ်", "unit": "အနည်းငယ် (to taste)", "notes_mm": None, "notes_en": None},
            {"ingredient_id": "I0039", "name_mm": "ငရုတ်ကောင်းမှုန့်", "name_en": "Ground black pepper", "quantity": "အနည်းငယ်", "unit": "အနည်းငယ် (to taste)", "notes_mm": None, "notes_en": None},
            {"ingredient_id": "I0191", "name_mm": "မာဂျရင်း", "name_en": "Margarine", "quantity": 5, "unit": "ကျပ်သား (g)", "notes_mm": "၈၂ ဂရမ်", "notes_en": "82g"},
            {"ingredient_id": "I0193", "name_mm": "ဒိန်ခဲ", "name_en": "Cheese", "quantity": 5, "unit": "ကျပ်သား (g)", "notes_mm": "ဒိန်ခဲအမာ ခြစ်ပြီး (၈၂ ဂရမ်)", "notes_en": "Hard cheese, grated (82g)"},
            {"ingredient_id": "I0026", "name_mm": "ကြက်ဥ", "name_en": "Chicken egg", "quantity": 1, "unit": "လုံး (piece)", "notes_mm": "အနှစ် ၁ လုံး", "notes_en": "1 egg yolk"},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "quantity": 1.25, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / ml)", "notes_mm": "၁ မှ ၁ ၁/၂ လဖဇ", "notes_en": "1 - 1.5 tsp"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "ဆန်ကာစစ်ပြီး ဂျုံကို ခွက်တစ်ခုတွင် ထည့်ပါ၊ ဆား၊ ငရုတ်ကောင်းမှုန့်၊ မာဂျရင်းတို့ကို ရောစပ်မွှေပြီး ပေါင်မုန့်ခြောက်ကဲ့သို့ အမှုန့်လေးများ ဖြစ်လာအောင် ပွတ်ချေပါ။",
            "ဒိန်ခဲ၊ ကြက်ဥအနှစ်နှင့် ရေ အနည်းငယ် ရောစပ်ပြီး မုန့်ညက်များ နူးညံ့လာသည်အထိ ခပ်ဖွဖွ နယ်ပေးပါ။",
            "မုန့်ညက်များကို လိပ်ကာ ၁/၈ လက်မ အထူ၊ ၂ လက်မခန့် အရှည်ရှိ ဒိန်ခဲချောင်းလေးများ ပြုလုပ်ပါ။",
            "ဆီသုတ်ထားသော မုန့်ဗန်းပေါ်တွင် စီတန်းထည့်ပြီး အပူချိန် ၂၀၀°C ရှိ မုန့်ဖုတ်ဖိုတွင် ရွှေဝါရောင် သန်းသည်အထိ ဖုတ်ပါ။"
        ],
        "instructions_en": [
            "Sift flour into a bowl; rub in salt, pepper, and margarine until the mixture resembles fine breadcrumbs.",
            "Mix in grated hard cheese, egg yolk, and cold water; gather lightly into a soft dough.",
            "Roll the dough out to 1/8-inch thickness and cut into strips about 2 inches long.",
            "Arrange on a greased baking sheet and bake in an oven at 200°C until crisp and golden brown."
        ],
        "tags": ["Cheese Straws", "Baking", "Savory Snack", "Appetizer"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 146},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 146"}
    },
    {
        "recipe_id": "R0137",
        "name_mm": "ဆိတ်သားစမူဆာ",
        "name_en": "Mutton Samosas",
        "description_mm": "ဆိတ်သားနုပ်နုပ်စဉ်း၊ အမွှေးအကြိုင်များနှင့် ခရမ်းချဉ်သီးတို့ဖြင့် အဆာသွတ်ပြီး ရွှေဝါရောင် အကြွပ်ကြော်ထားသော ဆိတ်သားစမူဆာ။",
        "description_en": "Crisp pastry cones filled with savory spiced minced mutton, onions, garlic, and fresh herbs, deep-fried until crunchy.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Snack", "Tea Time", "Appetizer"],
        "ingredients": [
            {"ingredient_id": "I0043", "name_mm": "ဂျုံမှုန့်", "name_en": "Wheat flour", "quantity": 2, "unit": "နို့ဆီဘူး (g)", "notes_mm": "အပြင်ခွံအတွက် ၂ နို့ဆီဘူး (၆၀၀ ဂရမ်)", "notes_en": "For pastry 2 tins (approx. 600g)"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "quantity": 1, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "အပြင်ခွံအတွက် ၁ လဖဇ", "notes_en": "For pastry 1 tsp"},
            {"ingredient_id": "I0071", "name_mm": "ဂီးထောပတ်", "name_en": "Ghee", "quantity": 5, "unit": "ကျပ်သား (g)", "notes_mm": "၈၂ ဂရမ်", "notes_en": "82g"},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "quantity": 7, "unit": "စားပွဲဇွန်း (tbsp / ml)", "notes_mm": "၇ စပဇ", "notes_en": "7 tbsp"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "quantity": 3, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "အဆာသတ်ရန် ၃ စပဇ", "notes_en": "For filling 3 tbsp"},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "quantity": 3, "unit": "လုံး (piece)", "notes_mm": "နုပ်နုပ်စဉ်း ၃ လုံး", "notes_en": "Minced 3 onions"},
            {"ingredient_id": "I0022", "name_mm": "ကြက်သွန်ဖြူ", "name_en": "Garlic", "quantity": 3, "unit": "လုံး (piece)", "notes_mm": "ထုထောင်း ၃ လုံး", "notes_en": "Crushed 3 cloves"},
            {"ingredient_id": "I0044", "name_mm": "ငရုတ်သီးစိမ်း", "name_en": "Green chili", "quantity": 3, "unit": "တောင့် (pod)", "notes_mm": "နုပ်နုပ်စဉ်း ၃ တောင့်", "notes_en": "Minced 3 pods"},
            {"ingredient_id": "I0041", "name_mm": "ငရုတ်သီးခြောက်", "name_en": "Dried red chili", "quantity": 0.5, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "ငရုတ်မှုန့် ၁/၂ လဖဇ", "notes_en": "Chili powder 0.5 tsp"},
            {"ingredient_id": "I0068", "name_mm": "ဆိတ်သား", "name_en": "Mutton", "quantity": 35, "unit": "ကျပ်သား (g)", "notes_mm": "နုပ်နုပ်စဉ်း (၅၇၁ ဂရမ်)", "notes_en": "Minced (approx. 571g)"},
            {"ingredient_id": "I0042", "name_mm": "ခရမ်းချဉ်သီး", "name_en": "Tomato", "quantity": 3, "unit": "လုံး (piece)", "notes_mm": "အခွံနွှာ လှီးစိတ် ၃ လုံး", "notes_en": "Peeled and chopped 3 tomatoes"},
            {"ingredient_id": "I0091", "name_mm": "နံနံပင်", "name_en": "Fresh coriander / cilantro", "quantity": 3, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "လှီးစိတ် ၃ လဖဇ", "notes_en": "Chopped 3 tsp"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "quantity": "အနည်းငယ်", "unit": "အနည်းငယ် (to taste)", "notes_mm": "အဆာအတွက်", "notes_en": "For filling to taste"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "quantity": "လိုအပ်သရွေ့", "unit": "လိုအပ်သရွေ့ (as needed)", "notes_mm": "မြုပ်အောင်ကြော်ရန်", "notes_en": "For deep frying"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "အပြင်ခွံအတွက် ဂျုံမှုန့်နှင့် ဆား ရောထည့်ပြီး ဂီးဖြင့် ဂျုံမှုန့် အစေ့များ ထွက်လာသည်အထိ နယ်ကာ ရေဖြည်းဖြည်းထည့်ပြီး ပျော့ပျောင်းလာသည်အထိ နယ်ပြီး အဝတ်စိုဖြင့် အုပ်ထားပါ။",
            "ဒယ်အိုးထဲသို့ ဆီထည့်ပြီး ကြက်သွန်နီ၊ ကြက်သွန်ဖြူတို့ကို ရွှေရောင်သန်းသည်အထိ ကြော်ကာ ငရုတ်သီး၊ ငရုတ်မှုန့်နှင့် ဆိတ်သားစဉ်းတို့ကို ထည့်မွှေပြီး ခရမ်းချဉ်သီး၊ နံနံပင်၊ ဆားတို့ ထည့်ကာ ရေခမ်းခြောက်သည်အထိ မိနစ် (၂၀) ခန့် ချက်ပြီး အအေးခံပါ။",
            "မုန့်ညက်သားကို ဂျုံမှုန့်ဖြူးပြီး ပါးလွှာစွာ လှိမ့်ကာ ထက်ခြမ်းခြမ်းပြီး ကတော့ပုံစံ ခေါက်ကာ ဆိတ်သားအဆာများ ထည့်သွင်းပြီး အစွန်းကို ရေဆွတ်ကာ တင်းကျပ်စွာ ပိတ်ပါ။",
            "ဆီများများဖြင့် ရွှေဝါရောင်သန်းပြီး ကြွပ်ရွလာသည်အထိ မီးအလယ်အလတ်ဖြင့် အကြွပ်ကြော်ပါ။"
        ],
        "instructions_en": [
            "For pastry, mix flour and salt, rub in ghee until crumbly, gradually add water, knead into a pliable smooth dough, and cover with a damp cloth.",
            "Heat oil in a skillet, sauté onions and garlic until golden; add chilies, chili powder, and minced mutton; add tomatoes, cilantro, and salt, cooking for about 20 minutes until completely dry, then cool.",
            "Roll out dough portions thinly, cut in half, shape each half into a cone, fill with the spiced minced mutton, moisten edges with water, and press firmly to seal.",
            "Deep fry in plenty of hot oil over medium heat until golden brown and crispy; drain on paper towels and serve."
        ],
        "tags": ["Samosa", "Mutton", "Fried Snack", "Tea Time", "Appetizer"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 147},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 147"}
    },
    {
        "recipe_id": "R0138",
        "name_mm": "ဟင်းသီးဟင်းရွက်စမူဆာ",
        "name_en": "Vegetable Samosas",
        "description_mm": "အာလူး၊ ပဲစိမ်း၊ မုန်ညင်းစေ့နှင့် အမွှေးအကြိုင်များဖြင့် သတ်သတ်လွတ် အဆာသွတ် ကြော်ထားသော ဟင်းသီးဟင်းရွက် စမူဆာ။",
        "description_en": "Crisp vegetarian samosas stuffed with spiced potatoes, green peas, mustard seeds, ginger, cilantro, and lemon juice.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Snack", "Tea Time", "Appetizer"],
        "ingredients": [
            {"ingredient_id": "I0043", "name_mm": "ဂျုံမှုန့်", "name_en": "Wheat flour", "quantity": 2, "unit": "နို့ဆီဘူး (g)", "notes_mm": "အပြင်ခွံအတွက် ၂ နို့ဆီဘူး (၆၀၀ ဂရမ်)", "notes_en": "For pastry 2 tins (approx. 600g)"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "quantity": 1, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "အပြင်ခွံအတွက် ၁ လဖဇ", "notes_en": "For pastry 1 tsp"},
            {"ingredient_id": "I0071", "name_mm": "ဂီးထောပတ်", "name_en": "Ghee", "quantity": 5, "unit": "ကျပ်သား (g)", "notes_mm": "၈၂ ဂရမ်", "notes_en": "82g"},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "quantity": 7, "unit": "စားပွဲဇွန်း (tbsp / ml)", "notes_mm": "၇ စပဇ", "notes_en": "7 tbsp"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "quantity": 3, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "အဆာသတ်ရန် ၃ စပဇ", "notes_en": "For filling 3 tbsp"},
            {"ingredient_id": "I0209", "name_mm": "မုန်ညင်းစေ့", "name_en": "Mustard seeds", "quantity": 3, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၃ လဖဇ", "notes_en": "3 tsp"},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "quantity": 3, "unit": "လုံး (piece)", "notes_mm": "ဥသေး နုပ်နုပ်စဉ်း ၃ လုံး", "notes_en": "Small onions, minced 3 pieces"},
            {"ingredient_id": "I0044", "name_mm": "ငရုတ်သီးစိမ်း", "name_en": "Green chili", "quantity": 3, "unit": "တောင့် (pod)", "notes_mm": "နုပ်စဉ်း ၃ တောင့်", "notes_en": "Minced 3 pods"},
            {"ingredient_id": "I0114", "name_mm": "နနွင်း", "name_en": "Turmeric powder", "quantity": 0.5, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၁/၂ လဖဇ", "notes_en": "1/2 tsp"},
            {"ingredient_id": "I0030", "name_mm": "ချင်း", "name_en": "Ginger", "quantity": 3, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "ခြစ်ပြီး ၃ လဖဇ", "notes_en": "Grated 3 tsp"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "quantity": "အနည်းငယ်", "unit": "အနည်းငယ် (to taste)", "notes_mm": None, "notes_en": None},
            {"ingredient_id": "I0077", "name_mm": "ပဲစိမ်း", "name_en": "Green peas", "quantity": 0.83, "unit": "နို့ဆီဘူး (g)", "notes_mm": "၅/၆ နို့ဆီဘူး (၂၅၀ ဂရမ်)", "notes_en": "5/6 tin (approx. 250g)"},
            {"ingredient_id": "I0159", "name_mm": "အာလူး", "name_en": "Potato", "quantity": 3, "unit": "လုံး (piece)", "notes_mm": "ပြုတ်ပြီး တုံးထား ၃ လုံး", "notes_en": "Boiled and cubed 3 potatoes"},
            {"ingredient_id": "I0091", "name_mm": "နံနံပင်", "name_en": "Fresh coriander / cilantro", "quantity": 1, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "လှီးဖြတ် ၁ လဖဇ", "notes_en": "Chopped 1 tsp"},
            {"ingredient_id": "I0106", "name_mm": "သံပရာသီး", "name_en": "Lime", "quantity": 3, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / ml)", "notes_mm": "ရှောက်ရည် ၃ လဖဇ", "notes_en": "Lemon/lime juice 3 tsp"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "quantity": "လိုအပ်သရွေ့", "unit": "လိုအပ်သရွေ့ (as needed)", "notes_mm": "မြုပ်အောင်ကြော်ရန်", "notes_en": "For deep frying"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "အပြင်ခွံအတွက် ဂျုံမှုန့်၊ ဆား၊ ဂီးနှင့် ရေတို့ဖြင့် နူးညံ့ပျော့ပျောင်းသော မုန့်ညက်သား ရအောင် နယ်ပြီး အဝတ်စိုဖြင့် ဖုံးအုပ်ထားပါ။",
            "အဆာအတွက် ဆီပူတွင် မုန်ညင်းစေ့ထည့်ပြီး ပေါက်ကွဲလာလျှင် ကြက်သွန်နီ၊ ငရုတ်စိမ်း၊ နနွင်း၊ ချင်း၊ ဆား၊ ပဲစိမ်း၊ အာလူးပြုတ်တုံးလေးများနှင့် နံနံပင်တို့ကို ထည့်ကြော်ကာ ရှောက်ရည်ထည့်ပြီး အအေးခံပါ။",
            "မုန့်ညက်ပြားကို ကတော့ပုံ ခေါက်ပြီး ဟင်းသီးဟင်းရွက်အဆာ ထည့်ကာ အနားများကို ရေဆွတ်၍ တင်းကျပ်စွာ ပိတ်ပါ။",
            "ဆီပူတွင် ရွှေဝါရောင် သန်းပြီး ကြွပ်ရွလာသည်အထိ မီးအလယ်အလတ်ဖြင့် ကြော်ပါ။"
        ],
        "instructions_en": [
            "For pastry, combine flour, salt, ghee, and water, kneading into a smooth soft dough, and cover with a damp cloth.",
            "For filling, heat oil, add mustard seeds until crackling; add onions, green chilies, turmeric, ginger, salt, green peas, boiled potato cubes, and cilantro; stir-fry, add lemon juice, and let cool.",
            "Roll pastry thin, cut into halves, shape into cones, fill with the spiced vegetable mixture, moisten edges, and press firmly to seal.",
            "Deep fry in hot oil over medium heat until golden brown and crisp; drain and serve hot."
        ],
        "tags": ["Vegetarian", "Samosa", "Potato", "Fried Snack", "Tea Time"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 147},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 147"}
    },
    {
        "recipe_id": "R0139",
        "name_mm": "ပရာတာ",
        "name_en": "Paratha",
        "description_mm": "အာတာဂျုံ၊ ဂျုံချောနှင့် ဂီးထောပတ်တို့ဖြင့် အလွှာများဖြစ်အောင် လိပ်၍ ဒယ်အိုးတွင် ဖုတ်ကြော်ထားသော အလွှာပရာတာ။",
        "description_en": "Layered flaky flatbread made from a blend of atta and maida flour, layered with ghee, and pan-toasted on a hot tawa.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Breakfast", "Snack", "Dinner"],
        "ingredients": [
            {"ingredient_id": "I0199", "name_mm": "အာတာဂျုံ", "name_en": "Atta flour", "quantity": 55, "unit": "ကျပ်သား (g)", "notes_mm": "၈၉၈ ဂရမ်", "notes_en": "898g"},
            {"ingredient_id": "I0200", "name_mm": "ဂျုံချော", "name_en": "All-purpose flour (Maida)", "quantity": 10, "unit": "ကျပ်သား (g)", "notes_mm": "၁၆၃ ဂရမ်", "notes_en": "163g"},
            {"ingredient_id": "I0071", "name_mm": "ဂီးထောပတ်", "name_en": "Ghee", "quantity": 15, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "နယ်ရန် ၁၅ လဖဇ (၇၅ ဂရမ်)", "notes_en": "15 tsp for dough (approx. 75g)"},
            {"ingredient_id": "I0071", "name_mm": "ဂီးထောပတ်", "name_en": "Ghee", "quantity": 5, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "ပျော်အောင်လုပ်ပြီး သုတ်ရန် ၅ လဖဇ", "notes_en": "5 tsp melted ghee for layering"},
            {"ingredient_id": "I0199", "name_mm": "အာတာဂျုံ", "name_en": "Atta flour", "quantity": 10, "unit": "ကျပ်သား (g)", "notes_mm": "ဖြူးရန်အတွက် (၁၆၃ ဂရမ်)", "notes_en": "For dusting (163g)"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "quantity": "လိုအပ်သရွေ့", "unit": "လိုအပ်သရွေ့ (as needed)", "notes_mm": None, "notes_en": None},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "quantity": "လိုအပ်သရွေ့", "unit": "လိုအပ်သရွေ့ (as needed)", "notes_mm": None, "notes_en": None},
            {"ingredient_id": "I0071", "name_mm": "ဂီးထောပတ်", "name_en": "Ghee", "quantity": "လိုအပ်သရွေ့", "unit": "လိုအပ်သရွေ့ (as needed)", "notes_mm": "ကြော်ရန်", "notes_en": "For cooking"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "အာတာဂျုံ၊ ဂျုံချောနှင့် ဆားတို့ကို ရော၍ ဆန်ကာချပါ၊ အလယ်ခေါင်တွင် တွင်းပြုလုပ်ပြီး ဂီးထောပတ် ထည့်ကာ ရေကို ဖြည်းဖြည်းချင်း ထည့်၍ နူးညံ့ပျော့ပျောင်းလာသည်အထိ နယ်ပြီး အဝတ်စိုဖြင့် ဖုံးအုပ်ကာ (၁) နာရီခန့် ထားပါ။",
            "ဂျုံလုံး ၁၅ လုံးခန့် အရွယ်တူ လုံးပြီး အာတာဂျုံဖြူးကာ အချင်း ၄ လက်မခန့် ပြားအောင် လှိမ့်ပြီး ဂီးသုတ်ကာ အလယ်မှ လိပ်ယူ၍ ကတော့ပုံ သို့မဟုတ် ခရုပတ်ပုံ ပြုလုပ်ကာ တစ်ဖန် ၇ လက်မ အကျယ် ပြားအောင် ပြန်လိပ်ပါ။",
            "အပူပေးထားသော ဒယ်ပြားတွင် ပရာတာကို တင်၍ အဖုလေးများ ထွက်လာသည်အထိ မီးအလတ်ဖြင့် မုန့်ဖုတ်ပါ။",
            "မုန့်အနားသားဘေးသို့ ဂီးလောင်းထည့်ပြီး မျက်နှာပြင် နှစ်ဖက်စလုံး ညိုရောင်သန်းသည်အထိ လှန်လှောကြော်ပြီး အသင့်တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "Sift atta, all-purpose flour, and salt together; make a well in the center, add ghee and water gradually, knead into a soft dough, cover with a damp cloth, and rest for 1 hour.",
            "Divide into 15 equal balls; roll each to 4 inches, brush with ghee, roll up into a spiral cone, flatten again, and roll out into a 7-inch round layered flatbread.",
            "Place the paratha onto a hot dry griddle and cook over medium heat until small bubbles form on the surface.",
            "Drizzle ghee around the edges and surfaces, flipping back and forth until both sides are speckled golden brown and flaky; serve hot."
        ],
        "tags": ["Paratha", "Flatbread", "Indian-Inspired", "Breakfast", "Flaky"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 148},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 148"}
    },
    {
        "recipe_id": "R0140",
        "name_mm": "ပူရီ",
        "name_en": "Puri",
        "description_mm": "ဂျုံကြမ်း၊ ရေနွေးနှင့် ဂီးတို့ဖြင့် နယ်ပြီး ဆီပူတွင် ဖောင်းကြွရွှေဝါရောင် ကြော်ထားသော အိန္ဒိယရိုးရာ ပူရီမုန့်။",
        "description_en": "Golden, puffed, deep-fried Indian flatbreads made from wheat flour, warm water, and melted ghee.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Breakfast", "Snack"],
        "ingredients": [
            {"ingredient_id": "I0043", "name_mm": "ဂျုံမှုန့်", "name_en": "Wheat flour", "quantity": 1.33, "unit": "နို့ဆီဘူး (g)", "notes_mm": "ဂျုံအကြမ်း ၁ ၁/၃ နို့ဆီဘူး (၄၀၀ ဂရမ်)", "notes_en": "Coarse flour 1 1/3 tins (approx. 400g)"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "quantity": 0.75, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၃/၄ လဖဇ", "notes_en": "3/4 tsp"},
            {"ingredient_id": "I0012", "name_mm": "ရေနွေး", "name_en": "Hot water", "quantity": 0.17, "unit": "နို့ဆီဘူး (ml)", "notes_mm": "၁/၆ နို့ဆီဘူး (၅၀ မီလီလီတာ)", "notes_en": "1/6 tin (50 ml)"},
            {"ingredient_id": "I0071", "name_mm": "ဂီးထောပတ်", "name_en": "Ghee", "quantity": 2, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "အရည်ဖျော် ၂ လဖဇ", "notes_en": "Melted 2 tsp"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "quantity": "လိုအပ်သရွေ့", "unit": "လိုအပ်သရွေ့ (as needed)", "notes_mm": "မြုပ်အောင်ကြော်ရန်", "notes_en": "For deep frying"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "လုံတံခွက်ထဲသို့ ဂျုံမှုန့်နှင့် ဆား ရောထည့်ပြီး အလယ်ခေါင် တွင်းထဲသို့ ရေနွေးနှင့် ဂီးထည့်ကာ (၁၀) မိနစ်ခန့် ချောမွတ် ပျော့ပျောင်းလာသည်အထိ နယ်ပါ။",
            "မိနစ် (၃၀) ခန့် ရေစိုအဝတ်ဖြင့် ဖုံးအုပ်ကာ နှပ်ထားပါ။",
            "မုန့်ညက်ကို အလုံး (၁၆) ခု အရွယ်ညီ ခွဲယူပြီး ဆီသုတ်ထားသော သစ်သားပြားပေါ်တွင် တင်ကာ ပါးလွှာဝိုင်းစက်သော အပြားငယ်များ ဖြစ်အောင် လှိမ့်ပေးပါ။",
            "ဆီပူပူတွင် ပူရီမုန့်များကို တစ်ခုချင်း ထည့်ပြီး အလျင်အမြန် ဖောင်းကြွ ရွှေဝါရောင်သန်းလာသည်အထိ နှစ်ဖက်လှန်ကြော်ကာ ဆီစစ်ပြီး ပူပူနွေးနွေး တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "Place coarse flour and salt in a bowl, make a well in the center, add warm water and melted ghee, and knead for about 10 minutes until smooth and soft.",
            "Cover with a damp cloth and rest the dough for about 30 minutes.",
            "Divide into 16 equal balls; place on an oiled board and roll out into thin, even circular discs.",
            "Slip one puri at a time into deep hot oil; gently press until puffed into a golden ball, flip to fry the other side, drain immediately, and serve piping hot."
        ],
        "tags": ["Puri", "Deep Fried", "Indian-Inspired", "Breakfast", "Puffy Bread"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 148},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 148"}
    },
    {
        "recipe_id": "R0141",
        "name_mm": "ကြက်ဆာတေး",
        "name_en": "Chicken Satay",
        "description_mm": "စပါးလင်၊ ဇီယာ၊ နံနံစေ့နှင့် မြေပဲလှော် မွှေးရနံ့တို့ဖြင့် နှပ်ပြီး မီးသွေးပေါ်တွင် သီတံဖြင့် ကင်ထားသော ကြက်သားဆာတေး။",
        "description_en": "Skewered chicken cubes marinated in an aromatic blend of lemongrass, cumin, coriander seeds, turmeric, and peanuts, grilled over charcoal.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Snack", "Dinner", "Appetizer"],
        "ingredients": [
            {"ingredient_id": "I0020", "name_mm": "ကြက်သား", "name_en": "Chicken meat", "quantity": 30, "unit": "ကျပ်သား (g)", "notes_mm": "အရိုးမဲ့ ၃၀ ကျပ်သား (၄၉၀ ဂရမ်)", "notes_en": "Boneless 30 ticals (approx. 490g)"},
            {"ingredient_id": "I0083", "name_mm": "စပါးလင်", "name_en": "Lemongrass", "quantity": 1, "unit": "ချောင်း (stalk)", "notes_mm": "၁ ချောင်း", "notes_en": "1 stalk"},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "quantity": 1, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၁ လဖဇ", "notes_en": "1 tsp"},
            {"ingredient_id": "I0055", "name_mm": "ဇီယာ", "name_en": "Cumin seeds", "quantity": 1, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "ဇီယာစေ့ ၁ လဖဇ", "notes_en": "Cumin seeds 1 tsp"},
            {"ingredient_id": "I0054", "name_mm": "နံနံစေ့", "name_en": "Coriander seeds", "quantity": 1, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၁ လဖဇ", "notes_en": "1 tsp"},
            {"ingredient_id": "I0008", "name_mm": "သစ်ကြံပိုးခေါက်", "name_en": "Cinnamon bark", "quantity": 0.5, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "သစ်ကြံပိုးမှုန့် ၁/၂ လဖဇ", "notes_en": "Cinnamon powder 1/2 tsp"},
            {"ingredient_id": "I0078", "name_mm": "မြေပဲလှော်", "name_en": "Roasted peanuts", "quantity": 2, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "၂ စပဇ", "notes_en": "2 tbsp"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "quantity": 2, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "၂ စပဇ", "notes_en": "2 tbsp"},
            {"ingredient_id": "I0114", "name_mm": "နနွင်း", "name_en": "Turmeric powder", "quantity": 1, "unit": "ခု (piece)", "notes_mm": "နနွင်းတက် (၁ လက်မ)", "notes_en": "Fresh turmeric root (1 inch)"},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "quantity": 8, "unit": "လုံး (piece)", "notes_mm": "၈ လုံး", "notes_en": "8 onions"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "quantity": "အနည်းငယ်", "unit": "အနည်းငယ် (to taste)", "notes_mm": "အရသာအတွက်", "notes_en": "To taste"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "ကြက်သားကို အနားညီ အတုံးလေးများ လှီးဖြတ်ထားပါ။",
            "စပါးလင်၊ ဇီယာစေ့၊ နံနံစေ့၊ နနွင်းတက်၊ ကြက်သွန်နီ၊ သစ်ကြံပိုးမှုန့်၊ မြေပဲလှော်၊ သကြား၊ ဆားနှင့် ဆီတို့ကို ညက်အောင် ထောင်းစပ်ပါ။",
            "အမွှေးအကြိုင် အရောထဲတွင် ကြက်သားတုံးများကို နယ်စိမ်ပြီး သစ်သားတံစို့တွင် ၅ တုံးစီ သီထိုးပါ။",
            "မီးသွေးမီးဖိုတွင် ကင်ပြီး ကင်နေစဉ် စပါးလင်ခက်ဖြင့် ဆီသုတ်လိမ်းပေးကာ အသားကျက်သည်အထိ လှန်လှော ကင်ပြီး မြေပဲဆော့စ်ဖြင့် တွဲဖက် တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "Cut boneless chicken meat into uniform bite-sized cubes.",
            "Finely pound lemongrass, cumin seeds, coriander seeds, fresh turmeric, onions, cinnamon powder, roasted peanuts, sugar, salt, and oil into a marinade paste.",
            "Coat chicken cubes thoroughly in the aromatic marinade paste and thread 5 pieces onto each bamboo skewer.",
            "Grill over glowing charcoal, basting regularly with oil using a bruised lemongrass stalk, turning until cooked through and slightly charred; serve with peanut sauce."
        ],
        "tags": ["Satay", "Chicken", "Grilled", "Street Food", "Skewers"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 149},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 149"}
    },
    {
        "recipe_id": "R0142",
        "name_mm": "မြေပဲဆော့စ်",
        "name_en": "Peanut Sauce",
        "description_mm": "မြေပဲလှော်ထောင်း၊ စပါးလင်၊ ချင်း၊ ပတဲကော၊ မန်ကျည်းမှည့်ရည်နှင့် ငရုတ်သီးတို့ဖြင့် ကျိုချက်ထားသော ဆာတေးမြေပဲဆော့စ်။",
        "description_en": "Rich and spicy peanut dipping sauce made with ground roasted peanuts, lemongrass, ginger, galangal, tamarind, and chili.",
        "category": "အချဉ်၊ အနှစ်နှင့် ဆော့စ်များ",
        "meal_types": ["Snack", "Dinner"],
        "ingredients": [
            {"ingredient_id": "I0078", "name_mm": "မြေပဲလှော်", "name_en": "Roasted peanuts", "quantity": 20, "unit": "ကျပ်သား (g)", "notes_mm": "၃၂၇ ဂရမ်", "notes_en": "327g"},
            {"ingredient_id": "I0083", "name_mm": "စပါးလင်", "name_en": "Lemongrass", "quantity": 1, "unit": "ချောင်း (stalk)", "notes_mm": "၁ ချောင်း", "notes_en": "1 stalk"},
            {"ingredient_id": "I0030", "name_mm": "ချင်း", "name_en": "Ginger", "quantity": 1, "unit": "ခု (piece)", "notes_mm": "၁ လက်မ", "notes_en": "1 inch piece"},
            {"ingredient_id": "I0180", "name_mm": "ပဒဲကော", "name_en": "Galangal", "quantity": 1, "unit": "တက် (segment)", "notes_mm": "ပတဲကော ၁ လက်မ", "notes_en": "1 inch segment"},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "quantity": 1, "unit": "လုံး (piece)", "notes_mm": "၁ လုံး", "notes_en": "1 onion"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "quantity": 3, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "၃ စပဇ", "notes_en": "3 tbsp"},
            {"ingredient_id": "I0041", "name_mm": "ငရုတ်သီးခြောက်", "name_en": "Dried red chili", "quantity": 3, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "ငရုတ်သီးမှုန့် ၃ စပဇ", "notes_en": "Chili powder 3 tbsp"},
            {"ingredient_id": "I0072", "name_mm": "မန်ကျည်းသီး", "name_en": "Tamarind", "quantity": 0.17, "unit": "နို့ဆီဘူး (ml)", "notes_mm": "မန်ကျည်းမှည့်ရည် ၁/၆ နို့ဆီဘူး (၅၀ မီလီလီတာ)", "notes_en": "Tamarind pulp liquid 1/6 tin (50 ml)"},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "quantity": 0.17, "unit": "နို့ဆီဘူး (g)", "notes_mm": "၁/၆ နို့ဆီဘူး (၅၀ ဂရမ်)", "notes_en": "1/6 tin (approx. 50g)"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "quantity": "အနည်းငယ်", "unit": "အနည်းငယ် (to taste)", "notes_mm": "အရသာအတွက်", "notes_en": "To taste"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "မြေပဲလှော်ကို ညက်အောင် ကြိတ်ချေထားပါ၊ စပါးလင်၊ ချင်းနှင့် ပတဲကောတို့ကိုလည်း ညက်နေအောင် ကြိတ်ထားပါ။",
            "ဆီပူတွင် ကြက်သွန်နီကို ဆီသတ်ပြီး ငရုတ်သီးမှုန့်နှင့် ကြိတ်ထားသော အမွှေးအကြိုင်များ ထည့်ကာ မန်ကျည်းမှည့်ရည်၊ သကြား၊ ဆားနှင့် ကြိတ်ထားသော မြေပဲလှော်တို့ကို ထည့်မွှေပါ။",
            "မီးအေးအေးဖြင့် ဆူပွက်ပျစ်ခဲလာသည်အထိ တည်ပြီးနောက် ပန်းကန်တွင် ထည့်ကာ လှီးစိတ်ထားသော သခွားသီး၊ ကြက်သွန်နီတို့ဖြင့် တွဲဖက် တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "Finely grind roasted peanuts; finely crush lemongrass, ginger, and galangal together into a paste.",
            "Heat oil in a pan, sauté onions until fragrant; stir in chili powder, crushed aromatics, tamarind juice, sugar, salt, and ground peanuts.",
            "Simmer over low heat until the sauce thickens into a glossy, rich dip; pour into serving bowls and garnish with sliced cucumbers and shallots."
        ],
        "tags": ["Peanut Sauce", "Dip", "Satay Sauce", "Condiment", "Spicy Sweet"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 149},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 149"}
    },
    {
        "recipe_id": "R0143",
        "name_mm": "ကော်ပြန့်လိပ်အခွံ",
        "name_en": "Spring Roll Wrappings",
        "description_mm": "ဂျုံမှုန့်နှင့် ရေအေးတို့ဖြင့် ပျော့ပျောင်းစေးကပ်အောင် နယ်ပြီး ဒယ်ပြားပူတွင် ပါးလွှာစွာ သုတ်ကပ်ပြုလုပ်သော ကော်ပြန့်လိပ်အခွံ။",
        "description_en": "Delicate homemade spring roll wrappers made from an elastic wheat flour dough lightly dabbed onto a hot griddle.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Snack", "Lunch"],
        "ingredients": [
            {"ingredient_id": "I0043", "name_mm": "ဂျုံမှုန့်", "name_en": "Wheat flour", "quantity": 25, "unit": "ကျပ်သား (g)", "notes_mm": "၄၀၈ ဂရမ်", "notes_en": "408g"},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "quantity": "လိုအပ်သရွေ့", "unit": "လိုအပ်သရွေ့ (as needed)", "notes_mm": "ရေအေး (သားရေပြားကဲ့သို့ ပျော့ပျောင်းစွဲကပ်သည်အထိ)", "notes_en": "Cold water as needed to form an elastic dough"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "ဇလုံတစ်ခုတွင် ဆန်ကာချထားသော ဂျုံမှုန့်ကို ရေအေး နည်းနည်းစီ ထည့်၍ သားရေပြားကဲ့သို့ ပျော့ပျောင်းစွဲကပ်သည်အထိ သမအောင် နယ်ပြီး (၁၅) မိနစ်ခန့် နှပ်ထားပါ။",
            "ဒယ်ပြား အဝိုင်းကို အပူပေးပြီး နယ်ထားသော ဂျုံမုန့်ညက်လုံးကို လက်ဖြင့်ကိုင်ကာ ဒယ်ပြားပေါ်သို့ ၆ လက်မခန့် အဝိုင်းပါးပါး ကပ်သုတ်ပြီး ချက်ချင်း ပြန်ဆွဲမပါ။",
            "မုန့်သား အနားများ တွန့်လိပ်လာပြီး ဝါလာပါက ညင်သာစွာ ဆွဲခွာယူပြီး အဝတ်စဖြင့် ဖုံးအုပ်ထားကာ ထပ်ခါထပ်ခါ ပြုလုပ်ပါ။"
        ],
        "instructions_en": [
            "Sift flour into a bowl, gradually add cold water while kneading vigorously until an elastic, stretchy dough forms, and let rest for 15 minutes.",
            "Heat an ungreased flat griddle; holding the dough ball in one hand, dab and sweep across the hot surface to leave a thin 6-inch round film, then immediately lift.",
            "As soon as the edges curl up and the wrapper dries, peel it off swiftly, cover with a clean cloth to stay soft, and repeat."
        ],
        "tags": ["Spring Roll", "Wrappers", "Homemade", "Dim Sum", "Baking"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 150},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 150"}
    },
    {
        "recipe_id": "R0144",
        "name_mm": "ကော်ပြန့်စိမ်း",
        "name_en": "Fresh Spring Rolls",
        "description_mm": "ပုစွန်၊ ဝက်သား၊ မှိုခြောက်၊ မျှစ်နှင့် မြေစာဥတို့ဖြင့် ကြော်ချက်ထားသော အဆာများကို ကော်ပြန့်ရွက်ဖြင့် လိပ်ထားသော ကော်ပြန့်စိမ်း။",
        "description_en": "Fresh spring rolls wrapped around a savory filling of minced prawns, lean pork strips, dried mushrooms, bamboo shoots, and water chestnuts.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Snack", "Lunch", "Appetizer"],
        "ingredients": [
            {"ingredient_id": "I0093", "name_mm": "ပုစွန်", "name_en": "Prawn / Shrimp", "quantity": 15, "unit": "ကျပ်သား (g)", "notes_mm": "အခွံနွှာပြီး (၂၄၅ ဂရမ်)", "notes_en": "Peeled (approx. 245g)"},
            {"ingredient_id": "I0080", "name_mm": "တရုတ်မှိုခြောက်", "name_en": "Dried Chinese mushrooms", "quantity": 6, "unit": "ပွင့် (flower / head)", "notes_mm": "၆ ပွင့်", "notes_en": "6 heads"},
            {"ingredient_id": "I0085", "name_mm": "ဝက်သား", "name_en": "Pork", "quantity": 15, "unit": "ကျပ်သား (g)", "notes_mm": "အဆီမဲ့ဝက်သား (၂၄၅ ဂရမ်)", "notes_en": "Lean pork (245g)"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "quantity": 2, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၂ လဖဇ", "notes_en": "2 tsp"},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "quantity": 0.5, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၁/၂ လဖဇ", "notes_en": "1/2 tsp"},
            {"ingredient_id": "I0051", "name_mm": "ဂျုံပြောင်းမှုန့်", "name_en": "Cornstarch", "quantity": 2, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "ပြောင်းမှုန့် ၂ လဖဇ", "notes_en": "Cornstarch 2 tsp"},
            {"ingredient_id": "I0050", "name_mm": "ပဲငံပြာရည်", "name_en": "Soy sauce", "quantity": 2, "unit": "စားပွဲဇွန်း (tbsp / ml)", "notes_mm": "၂ စပဇ", "notes_en": "2 tbsp total"},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "quantity": 2, "unit": "လုံး (piece)", "notes_mm": "၂ လုံး", "notes_en": "2 onions"},
            {"ingredient_id": "I0094", "name_mm": "မျှစ်", "name_en": "Bamboo shoot", "quantity": 0.5, "unit": "ခွက် (cup)", "notes_mm": "ပြုတ်ပြီး ၁/၂ ခွက်", "notes_en": "Boiled 1/2 cup"},
            {"ingredient_id": "I0201", "name_mm": "မြေစာဥ", "name_en": "Water chestnut", "quantity": 6, "unit": "ဥ (corm)", "notes_mm": "၆ ဥ", "notes_en": "6 corms"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "quantity": 0.25, "unit": "ခွက် (cup)", "notes_mm": "၁/၄ ခွက်", "notes_en": "1/4 cup"},
            {"ingredient_id": "I0030", "name_mm": "ချင်း", "name_en": "Ginger", "quantity": 1, "unit": "လွှာ (slice)", "notes_mm": "၁ လွှာ", "notes_en": "1 slice"},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "quantity": "အနည်းငယ်", "unit": "အနည်းငယ် (to taste)", "notes_mm": None, "notes_en": None},
            {"ingredient_id": "I0210", "name_mm": "ကော်ပြန့်ရွက်", "name_en": "Spring roll wrappers", "quantity": 10, "unit": "လွှာ (sheet)", "notes_mm": "၁၀ လွှာ", "notes_en": "10 sheets"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "ပုစွန်ကို ရေအနည်းငယ်ဖြင့် ပြုတ်ကာ အခွံနွှာပြီး စဉ်းထားပါ၊ ဝက်သားကို အမျှင်လှီး၍ ဆား၊ သကြား၊ ပြောင်းမှုန့်၊ ပဲငံပြာရည်တို့ဖြင့် နယ်ထားပါ။",
            "မှိုခြောက်၊ ကြက်သွန်နီ၊ မျှစ်၊ မြေစာဥတို့ကို အမျှင်ရှည်များ လှီးထားပါ။",
            "ဒယ်အိုးတွင် ဆီပူပြီး ကြက်သွန်နီ၊ မျှစ်၊ ပဲပင်ပေါက်၊ မြေစာဥ၊ ပဲငံပြာရည်တို့ ထည့်မွှေကာ ဝက်သားနှင့် ပုစွန်တို့ကို ထည့်၍ ကျက်အောင် ကြော်ပြီး အအေးခံပါ။",
            "ကော်ပြန့်လိပ်အခွံပေါ်တွင် အဆာ ၁ စားပွဲဇွန်း တင်၍ အောက်အနားကို ခေါက်ကာ ဘေးနှစ်ဖက် သွင်းလိပ်ပြီး ထိပ်စွန်းကို ဂျုံရည်သုတ်၍ ကပ်ကာ ဆလပ်ရွက်၊ အချဉ်ဆော့စ်တို့ဖြင့် တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "Simmer prawns in a little water, peel and mince; slice lean pork into fine strips and marinate with salt, sugar, cornstarch, and soy sauce.",
            "Julienne the soaked dried mushrooms, onions, boiled bamboo shoots, and water chestnuts.",
            "Heat oil in a wok, sauté onions, bamboo shoots, water chestnuts, and seasonings; add marinated pork and prawns, stir-fry until thoroughly cooked, and cool.",
            "Place 1-2 tbsp filling on each wrapper, fold up the bottom edge, tuck in both sides, roll up tightly, seal the tip with flour paste, and serve with fresh lettuce and dipping sauce."
        ],
        "tags": ["Spring Roll", "Fresh Spring Roll", "Prawn", "Pork", "Appetizer"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 150},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 150"}
    },
    {
        "recipe_id": "R0145",
        "name_mm": "အသားပေါက်စီ",
        "name_en": "Steamed Meat Bun",
        "description_mm": "ရေနွေးဆူဆူဖြင့် နယ်ထားသော ဂျုံသားထဲတွင် ဝက်သားစဉ်း၊ မှိုခြောက်၊ ကြက်သွန်မြိတ်နှင့် အမွှေးအကြိုင်များ သွတ်ပြီး ပေါင်းထားသော အသားပေါက်စီ။",
        "description_en": "Steamed Chinese-style meat buns stuffed with seasoned minced pork, dried mushrooms, scallions, cilantro, and sesame oil.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Breakfast", "Snack", "Dim Sum"],
        "ingredients": [
            {"ingredient_id": "I0043", "name_mm": "ဂျုံမှုန့်", "name_en": "Wheat flour", "quantity": 10, "unit": "ကျပ်သား (g)", "notes_mm": "အပြင်ခွံအတွက် (၁၆၃ ဂရမ်)", "notes_en": "For dough (163g)"},
            {"ingredient_id": "I0012", "name_mm": "ရေနွေး", "name_en": "Hot water", "quantity": 0.67, "unit": "နို့ဆီဘူး (ml)", "notes_mm": "ရေနွေးဆူဆူ ၂/၃ နို့ဆီဘူး (၂၀၀ မီလီလီတာ)", "notes_en": "Boiling water 2/3 tin (200 ml)"},
            {"ingredient_id": "I0175", "name_mm": "ရေခဲ", "name_en": "Ice cubes", "quantity": 0.17, "unit": "နို့ဆီဘူး (ml)", "notes_mm": "ရေခဲရေ ၁/၆ နို့ဆီဘူး (၅၀ မီလီလီတာ)", "notes_en": "Ice cold water 1/6 tin (50 ml)"},
            {"ingredient_id": "I0085", "name_mm": "ဝက်သား", "name_en": "Pork", "quantity": 14, "unit": "ကျပ်သား (g)", "notes_mm": "အဆီလွတ်အသား (၂၂၈ ဂရမ်)", "notes_en": "Lean meat (228g)"},
            {"ingredient_id": "I0085", "name_mm": "ဝက်သား", "name_en": "Pork", "quantity": 3, "unit": "ကျပ်သား (g)", "notes_mm": "အဆီပါအသား (၄၉ ဂရမ်)", "notes_en": "Fatty meat (49g)"},
            {"ingredient_id": "I0080", "name_mm": "တရုတ်မှိုခြောက်", "name_en": "Dried Chinese mushrooms", "quantity": 2, "unit": "ပွင့် (flower / head)", "notes_mm": "၂ ပွင့်", "notes_en": "2 heads"},
            {"ingredient_id": "I0025", "name_mm": "ကြက်သွန်မြိတ်", "name_en": "Spring onion", "quantity": 2, "unit": "ပင် (stalk)", "notes_mm": "ရိတ်ရိတ်လှီး ၂ ပင်", "notes_en": "Finely sliced 2 stalks"},
            {"ingredient_id": "I0091", "name_mm": "နံနံပင်", "name_en": "Fresh coriander / cilantro", "quantity": 1, "unit": "ပင် (stalk)", "notes_mm": "ရိတ်ရိတ်လှီး ၁ ပင်", "notes_en": "Finely sliced 1 stalk"},
            {"ingredient_id": "I0051", "name_mm": "ဂျုံပြောင်းမှုန့်", "name_en": "Cornstarch", "quantity": 1, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၁ လဖဇ", "notes_en": "1 tsp"},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "quantity": 2, "unit": "စားပွဲဇွန်း (tbsp / ml)", "notes_mm": "၂ စပဇ", "notes_en": "2 tbsp"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "quantity": 0.5, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၁/၂ လဖဇ", "notes_en": "1/2 tsp"},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "quantity": 1, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၁ လဖဇ", "notes_en": "1 tsp"},
            {"ingredient_id": "I0023", "name_mm": "ပဲငံပြာရည်အကြည်", "name_en": "Light soy sauce", "quantity": 1, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / ml)", "notes_mm": "၁ လဖဇ", "notes_en": "1 tsp"},
            {"ingredient_id": "I0202", "name_mm": "အရက်", "name_en": "Cooking wine", "quantity": 1, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / ml)", "notes_mm": "၁ လဖဇ", "notes_en": "1 tsp"},
            {"ingredient_id": "I0067", "name_mm": "နှမ်းဆီ", "name_en": "Sesame oil", "quantity": "အနည်းငယ်", "unit": "အနည်းငယ် (to taste)", "notes_mm": None, "notes_en": None},
            {"ingredient_id": "I0039", "name_mm": "ငရုတ်ကောင်းမှုန့်", "name_en": "Ground black pepper", "quantity": "အနည်းငယ်", "unit": "အနည်းငယ် (to taste)", "notes_mm": None, "notes_en": None}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "မုန့်အပြင်ခွံအတွက် ဂျုံမှုန့်ထဲသို့ ရေနွေးဆူဆူကို လျင်မြန်စွာ ထည့်၍ သစ်သားတုတ်ဖြင့် မွှေပြီး ရေခဲရေ ထည့်ကာ ချောမွတ်ပျော့ပျောင်းလာသည်အထိ နယ်ပါ။",
            "အဆာအတွက် အသားစဉ်းများ၊ ရေစိမ်ပြီး ပါးပါးလှီးထားသော မှိုခြောက်၊ ကြက်သွန်မြိတ်၊ နံနံပင်၊ ပြောင်းမှုန့်ရည်၊ ဆား၊ သကြား၊ ပဲငံပြာရည်၊ အရက်၊ နှမ်းဆီ၊ ငရုတ်ကောင်းမှုန့်တို့ကို သမအောင် စေးပိုင်သည်အထိ နယ်ပါ။",
            "ဂျုံလုံးကို ၂၄ မှ ၃၂ တုံးခန့် လှီးဖြတ်ပြီး တစ်တုံးစီကို အပြားဝိုင်း လှိမ့်ကာ အလယ်တွင် အသားအဆာ ထည့်ပြီး ပေါက်စီပုံစံ အနားသား ခေါက်တွန့်၍ လုံးပါ။",
            "ပေါင်းချောင်ထဲတွင် ညီညာစွာ ထည့်ပြီး ရေဆူအိုးပေါ်တွင် မီးပြင်းပြင်းဖြင့် (၁၅) မိနစ်ခန့် ပေါင်းပြီး ပူပူနွေးနွေး တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "For dough, quickly pour boiling water into flour, stir vigorously with chopsticks, add ice-cold water, and knead on a floured surface until smooth and elastic.",
            "For filling, mix minced lean and fatty meat with sliced dried mushrooms, scallions, cilantro, cornstarch slurry, salt, sugar, light soy sauce, cooking wine, sesame oil, and white pepper until sticky.",
            "Divide dough into 24 to 32 pieces, roll into round discs, spoon meat filling into the center, pleat edges upward to enclose, and twist firmly to seal.",
            "Arrange buns in a steamer lined with paper, steam over rapidly boiling water on high heat for about 15 minutes, and serve piping hot."
        ],
        "tags": ["Baozi", "Steamed Bun", "Dim Sum", "Pork", "Breakfast"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 151},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 151"}
    },
    {
        "recipe_id": "R0146",
        "name_mm": "ဖက်ထုပ်ကြော်",
        "name_en": "Savoury Wontons",
        "description_mm": "ဝက်သားစဉ်း၊ ကြက်သွန်နီ၊ ခရုဆီနှင့် နံနံပင်တို့ဖြင့် အဆာသွတ်ပြီး ရွှေဝါရောင် ကြွပ်ရွအောင် ကြော်ထားသော ဖက်ထုပ်ကြော်။",
        "description_en": "Crisp golden fried wontons filled with seasoned minced pork, garlic, shallots, oyster sauce, and cilantro.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Snack", "Appetizer", "Dim Sum"],
        "ingredients": [
            {"ingredient_id": "I0085", "name_mm": "ဝက်သား", "name_en": "Pork", "quantity": 25, "unit": "ကျပ်သား (g)", "notes_mm": "အဆီလွတ်ဝက်သား (၄၀၈ ဂရမ်)", "notes_en": "Lean pork (408g)"},
            {"ingredient_id": "I0006", "name_mm": "ကြက်သွန်နီ", "name_en": "Onion", "quantity": 3, "unit": "လုံး (piece)", "notes_mm": "ဥသေး ခုတ်စဉ်း ၃ လုံး", "notes_en": "Small onions, minced 3 pieces"},
            {"ingredient_id": "I0022", "name_mm": "ကြက်သွန်ဖြူ", "name_en": "Garlic", "quantity": 3, "unit": "မြွှာ (clove)", "notes_mm": "ထုထား ၃ မြွှာ", "notes_en": "Crushed 3 cloves"},
            {"ingredient_id": "I0211", "name_mm": "ခရုဆီ", "name_en": "Oyster sauce", "quantity": 1.5, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "၁ ၁/၂ စပဇ", "notes_en": "1.5 tbsp"},
            {"ingredient_id": "I0091", "name_mm": "နံနံပင်", "name_en": "Fresh coriander / cilantro", "quantity": 1.5, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "စဉ်းထား ၁ ၁/၂ လဖဇ", "notes_en": "Minced 1.5 tsp"},
            {"ingredient_id": "I0026", "name_mm": "ကြက်ဥ", "name_en": "Chicken egg", "quantity": 3, "unit": "လုံး (piece)", "notes_mm": "၃ လုံး", "notes_en": "3 eggs"},
            {"ingredient_id": "I0203", "name_mm": "ဖက်ထုပ်ရွက်", "name_en": "Wonton wrappers", "quantity": 100, "unit": "လွှာ (sheet)", "notes_mm": "၁၀၀ လွှာ", "notes_en": "100 sheets"},
            {"ingredient_id": "I0026", "name_mm": "ကြက်ဥ", "name_en": "Chicken egg", "quantity": 1, "unit": "လုံး (piece)", "notes_mm": "ကြက်ဥအနှစ် (ပိတ်ရန်)", "notes_en": "Egg yolk for sealing"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "quantity": "လိုအပ်သရွေ့", "unit": "လိုအပ်သရွေ့ (as needed)", "notes_mm": "မြုပ်အောင်ကြော်ရန်", "notes_en": "For deep frying"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "ဝက်သားစဉ်းကို ကြက်သွန်နီ၊ ကြက်သွန်ဖြူ၊ ခရုဆီ၊ နံနံပင်၊ ကြက်ဥတို့ဖြင့် သမအောင် ရောစပ်နယ်ပါ။",
            "ဖက်ထုပ်ရွက် တစ်ချပ်စီပေါ်တွင် အဆာ ၁ လက်ဖက်ရည်ဇွန်းခန့် ထည့်ပြီး အနားစွန်းကို ကြက်ဥအနှစ်ရည်ဖြင့် သုတ်ကာ လေးထောင့် သို့မဟုတ် တြိဂံပုံ ခေါက်ပိတ်ပါ။",
            "ဆီမြုပ်အောင် ထည့်ထားသော ဒယ်အိုးတွင် ရွှေဝါရောင် သန်းလာသည်အထိ ၂ မိနစ်ခန့် မီးအလယ်ဖြင့် ကြော်ပြီး ဆီစစ်ကာ အချဉ်ဆော့စ်ဖြင့် တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "Combine minced lean pork with chopped shallots, garlic, oyster sauce, cilantro, and beaten eggs until sticky and uniform.",
            "Place 1 tsp of filling in the center of each wonton wrapper, brush edges lightly with beaten egg yolk, and fold into triangles or ingots, pinching firmly to seal.",
            "Deep fry in hot oil over medium heat for about 2 minutes until bubbly and golden crisp; drain on paper towels and serve with sweet chili sauce."
        ],
        "tags": ["Wonton", "Fried Wonton", "Dim Sum", "Pork", "Appetizer"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 151},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 151"}
    },
    {
        "recipe_id": "R0147",
        "name_mm": "ပဲပြားတို့ဟူး",
        "name_en": "Pea Cubes",
        "description_mm": "ပဲစေ့အခြောက်ကို ပြုတ်ကာ ဆန်ကာတိုက်ပြီး ပြောင်းကော်မှုန့်နှင့် သကြားတို့ဖြင့် ကျိုချက် အအေးခံထားသော ပဲပြားတို့ဟူးတုံး။",
        "description_en": "Firm pea jelly cubes made from strained yellow split pea puree, cornstarch, and sugar, chilled and sliced into bite-sized cubes.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Snack", "Dessert"],
        "ingredients": [
            {"ingredient_id": "I0013", "name_mm": "ပဲနီလေး", "name_en": "Red lentils", "quantity": 14, "unit": "ကျပ်သား (g)", "notes_mm": "ပဲစေ့အခြောက် (၂၂၈ ဂရမ်)", "notes_en": "Dried split peas (228g)"},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "quantity": 77, "unit": "ကျပ်သား (g)", "notes_mm": "ရေအေး ၇၇ ကျပ်သား (၁၂၅၆ ဂရမ်/မီလီလီတာ)", "notes_en": "Cold water 77 ticals (approx. 1256 ml)"},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "quantity": 5, "unit": "ကျပ်သား (g)", "notes_mm": "၈၂ ဂရမ်", "notes_en": "82g"},
            {"ingredient_id": "I0051", "name_mm": "ဂျုံပြောင်းမှုန့်", "name_en": "Cornstarch", "quantity": 2, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "ပြောင်းကော်မှုန့် ၂ စပဇ", "notes_en": "Cornstarch 2 tbsp"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "ပဲစေ့များကို မိနစ် ၂၀ ခန့် ဆူစေပြီး တစ်ည ရေစိမ်ထားပါ၊ နောက်တစ်နေ့တွင် ရေစစ်ကာ အိအိနူးသည်အထိ ၂ နာရီခန့် ပြုတ်ပါ။",
            "ပဲများကို ဆန်ကာတိုက်ချပြီး သကြားနှင့် ပြောင်းကော်မှုန့်များ ထည့်၍ မီးဖိုပေါ်တင်ကာ ၁၅ မိနစ်ခန့် အဆက်မပြတ် မွှေပေးပါ။",
            "ကော်ကဲ့သို့ ခဲလာလျှင် အောက်မကပ်သော ဒယ်ပြား သို့မဟုတ် ဗန်းထဲသို့ ၁ လက်မခန့် အထူရအောင် လောင်းထည့်ပါ။",
            "အအေးခံပြီးနောက် ၁ လက်မ အရွယ် ကုဗတုံးလေးများ လှီးဖြတ်ကာ တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "Boil dried peas for 20 minutes, soak overnight, drain, and boil again for about 2 hours until very tender.",
            "Pass the boiled peas through a fine sieve, stir in sugar and cornstarch, and cook over medium heat, stirring continuously for about 15 minutes.",
            "When the mixture thickens into a glossy paste, pour into a flat non-stick tray to a thickness of about 1 inch.",
            "Allow to cool and set completely at room temperature, then slice into 1-inch cubes and serve."
        ],
        "tags": ["Tofu", "Pea Cubes", "Snack", "Vegetarian", "Jelly"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 152},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 152"}
    },
    {
        "recipe_id": "R0148",
        "name_mm": "ခေါက်ဆွဲကြော်",
        "name_en": "Fried Noodles",
        "description_mm": "ကြက်ဥခေါက်ဆွဲခြောက်၊ ဝက်သား၊ မျှစ်၊ ဟင်းနုနွယ်၊ သခွားသီးနှင့် ပဲငါးပိ ရှယ်ရီအရက်ဆော့စ်တို့ဖြင့် ကြော်ထားသော တရုတ်စတိုင် ခေါက်ဆွဲကြော်။",
        "description_en": "Chinese-style stir-fried egg noodles with shredded pork, bamboo shoots, spinach, cucumber, and a savory fermented bean paste sherry sauce.",
        "category": "တစ်ပွဲပြင်အစားအစာများ",
        "meal_types": ["Lunch", "Dinner"],
        "ingredients": [
            {"ingredient_id": "I0178", "name_mm": "ဂျုံခေါက်ဆွဲ", "name_en": "Wheat noodles", "quantity": 30, "unit": "ကျပ်သား (g)", "notes_mm": "ကြက်ဥခေါက်ဆွဲခြောက် ၃၀ ကျပ်သား (၄၉၀ ဂရမ်)", "notes_en": "Dried egg noodles (490g)"},
            {"ingredient_id": "I0085", "name_mm": "ဝက်သား", "name_en": "Pork", "quantity": 25, "unit": "ကျပ်သား (g)", "notes_mm": "အဆီနည်းဝက်သား (၄၀၈ ဂရမ်)", "notes_en": "Lean pork (408g)"},
            {"ingredient_id": "I0051", "name_mm": "ဂျုံပြောင်းမှုန့်", "name_en": "Cornstarch", "quantity": 3, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "ပြောင်းကော်မှုန့် ၃ လဖဇ", "notes_en": "Cornstarch 3 tsp"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "quantity": 5, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "၅ စပဇ", "notes_en": "5 tbsp"},
            {"ingredient_id": "I0012", "name_mm": "ရေနွေး", "name_en": "Hot water", "quantity": 0.17, "unit": "နို့ဆီဘူး (ml)", "notes_mm": "၁/၆ နို့ဆီဘူး (၅၀ မီလီလီတာ)", "notes_en": "1/6 tin (50 ml)"},
            {"ingredient_id": "I0094", "name_mm": "မျှစ်", "name_en": "Bamboo shoot", "quantity": 5, "unit": "ကျပ်သား (g)", "notes_mm": "အမျှင်လှီးထား (၈၂ ဂရမ်)", "notes_en": "Julienned (82g)"},
            {"ingredient_id": "I0038", "name_mm": "ဟင်းနုနွယ်", "name_en": "Spinach", "quantity": 5, "unit": "ကျပ်သား (g)", "notes_mm": "အမျှင်လှီးထား (၈၂ ဂရမ်)", "notes_en": "Shredded (82g)"},
            {"ingredient_id": "I0052", "name_mm": "သခွားသီး", "name_en": "Cucumber", "quantity": 1, "unit": "လုံး (piece)", "notes_mm": "အမျှင်လှီးထား ၁ လုံး", "notes_en": "Julienned 1 cucumber"},
            {"ingredient_id": "I0204", "name_mm": "ပဲငါးပိရည်", "name_en": "Fermented bean paste sauce", "quantity": 3, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "၃ စပဇ", "notes_en": "3 tbsp"},
            {"ingredient_id": "I0205", "name_mm": "ရှယ်ရီအရက်", "name_en": "Sherry cooking wine", "quantity": 1, "unit": "စားပွဲဇွန်း (tbsp / ml)", "notes_mm": "၁ စပဇ", "notes_en": "1 tbsp"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "quantity": 0.5, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "၁/၂ စပဇ", "notes_en": "0.5 tbsp"},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "quantity": 2, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "၂ စပဇ", "notes_en": "2 tbsp"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "ခေါက်ဆွဲခြောက်များကို ကပ်စေးမသွားဘဲ ပျော့ပျောင်းလာအောင် ၅ မိနစ်ခန့် ပြုတ်ပြီး ဆန်ကာဖြင့် ဆယ်ကာ ရေအေးထဲတွင် ဆေးကြောစစ်ထားပါ။",
            "ဝက်သားကို အမျှင်လှီး၍ ပြောင်းကော်ရည်ဖြင့် နယ်ထားပါ၊ မျှစ်၊ ဟင်းနုနွယ်၊ သခွားသီးတို့ကို အမျှင်ရှည်များ လှီးဖြတ်ထားပါ။",
            "ဒယ်အိုးတွင် ဆီပူပြီး ခေါက်ဆွဲများကို ၅ မိနစ်ခန့် မွှေကြော်ပြီး ဆယ်ယူထားပါ။ ကျန်ဆီတွင် ဝက်သား၊ မျှစ်၊ ဟင်းနုနွယ်၊ သခွားသီးတို့ကို ထည့်ကြော်ပြီး ပဲငါးပိရည်၊ ရှယ်ရီအရက်၊ ဆား၊ သကြားတို့ဖြင့် စပ်ထားသော ဆော့စ်ကို ထည့်မွှေပါ။",
            "အသားကျက်ပြီး အရောင်ပြောင်းလာပါက ခေါက်ဆွဲပေါ်သို့ လောင်းထည့်ကာ ပူပူနွေးနွေး တွဲဖက် သုံးဆောင်ပါ။"
        ],
        "instructions_en": [
            "Boil dried egg noodles for about 5 minutes until tender yet firm, drain through a colander, rinse under cold water, and drain well.",
            "Julienne pork and coat with cornstarch slurry; cut bamboo shoots, spinach, and cucumber into thin matchsticks.",
            "Heat oil in a wok, stir-fry noodles for about 5 minutes, and remove; in the remaining oil, stir-fry pork, bamboo shoots, spinach, and cucumber, then add the mixed bean paste sherry sauce.",
            "When the pork and vegetables are cooked through and glossy with sauce, toss together with the fried noodles or spoon over, and serve hot."
        ],
        "tags": ["Fried Noodles", "Noodles", "Pork", "Stir Fry", "Chinese-Style"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 152},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 152"}
    },
    {
        "recipe_id": "R0149",
        "name_mm": "ပုစွန်ကပ်ပေါင်မုန့်ကြော်",
        "name_en": "Prawns with Toast",
        "description_mm": "နှပ်ထားသော ပုစွန်ကို ပေါင်မုန့်ချပ်ပေါ်တွင် မုန့်နှစ်ဖြင့် ကပ်ကာ နှမ်းနက်နှင့် နံနံရွက်တင်၍ ရွှေဝါရောင် ကြွပ်ရွအောင် ကြော်ထားသော ပုစွန်ပေါင်မုန့်ကြော်။",
        "description_en": "Crisp Chinese-style prawn toast featuring butterflied marinated prawns mounted on bread with egg-white paste, sesame seeds, and cilantro.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Snack", "Appetizer", "Dim Sum"],
        "ingredients": [
            {"ingredient_id": "I0093", "name_mm": "ပုစွန်", "name_en": "Prawn / Shrimp", "quantity": 42, "unit": "ကျပ်သား (g)", "notes_mm": "၁၂ ကောင် (၆၈၅ ဂရမ်)", "notes_en": "12 large prawns (approx. 685g)"},
            {"ingredient_id": "I0025", "name_mm": "ကြက်သွန်မြိတ်", "name_en": "Spring onion", "quantity": 2, "unit": "ပင် (stalk)", "notes_mm": "ထုထား ၂ ပင်", "notes_en": "Crushed 2 stalks"},
            {"ingredient_id": "I0030", "name_mm": "ချင်း", "name_en": "Ginger", "quantity": 2, "unit": "လွှာ (slice)", "notes_mm": "ထုထား ၂ လွှာ", "notes_en": "Crushed 2 slices"},
            {"ingredient_id": "I0039", "name_mm": "ငရုတ်ကောင်းမှုန့်", "name_en": "Ground black pepper", "quantity": 0.25, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၁/၄ လဖဇ", "notes_en": "1/4 tsp"},
            {"ingredient_id": "I0004", "name_mm": "ဆား", "name_en": "Salt", "quantity": 0.5, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၁/၂ လဖဇ", "notes_en": "1/2 tsp"},
            {"ingredient_id": "I0074", "name_mm": "ပေါင်မုန့်", "name_en": "Bread", "quantity": 6, "unit": "ချပ် (slice)", "notes_mm": "ပေါင်မုန့်ဖြူ ၆ ချပ်", "notes_en": "White bread 6 slices"},
            {"ingredient_id": "I0026", "name_mm": "ကြက်ဥ", "name_en": "Chicken egg", "quantity": 4, "unit": "လုံး (piece)", "notes_mm": "ကြက်ဥအကာသား ၄ လုံး", "notes_en": "4 egg whites"},
            {"ingredient_id": "I0043", "name_mm": "ဂျုံမှုန့်", "name_en": "Wheat flour", "quantity": 2, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "၂ စပဇ", "notes_en": "2 tbsp"},
            {"ingredient_id": "I0051", "name_mm": "ဂျုံပြောင်းမှုန့်", "name_en": "Cornstarch", "quantity": 1, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "ပြောင်းကော်မှုန့် ၁ စပဇ", "notes_en": "Cornstarch 1 tbsp"},
            {"ingredient_id": "I0208", "name_mm": "နှမ်းနက်စေ့", "name_en": "Black sesame seeds", "quantity": 0.5, "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)", "notes_mm": "၁/၂ လဖဇ", "notes_en": "1/2 tsp"},
            {"ingredient_id": "I0091", "name_mm": "နံနံပင်", "name_en": "Fresh coriander / cilantro", "quantity": 24, "unit": "ခု (piece)", "notes_mm": "နံနံညွန့် ၂၄ ခု", "notes_en": "24 cilantro sprigs"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "quantity": 8, "unit": "နို့ဆီဘူး (ml)", "notes_mm": "ကြော်ရန် ၈ နို့ဆီဘူး (၂၄၀၀ မီလီလီတာ)", "notes_en": "For frying 8 tins (2400 ml)"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "ပုစွန်ကို အမြီးပိုင်း မပျက်အောင် အခွံနွှာပြီး အကြောဖယ်ကာ ရေဆေးစစ်ထားပါ၊ ကျောဘက်ကို ဓားဖြင့် အသာဖောက်၍ ပြန့်အောင် လုပ်ပြီး ကြက်သွန်မြိတ်၊ ချင်း၊ ငရုတ်ကောင်း၊ ဆားတို့ဖြင့် မိနစ် ၂၀ နှပ်ထားပါ။",
            "ပေါင်မုန့်ချပ်များကို အနားသား ဖယ်ပြီး လေးထောင့် သို့မဟုတ် တြိဂံ ၄ ပိုင်းစီ ဖြတ်ထားပါ၊ ကြက်ဥအကာ၊ ဂျုံမှုန့်၊ ပြောင်းကော်မှုန့်တို့ကို သမအောင် မွှေထားပါ။",
            "ပေါင်မုန့်ချပ်ပေါ်တွင် မုန့်နှစ်အရော သုတ်လိမ်းပြီး နှပ်ထားသော ပုစွန်တစ်ကောင်စီ တင်ကာ အပေါ်မှ နှမ်းနက်စေ့နှင့် နံနံရွက် ညှပ်ကပ်ပါ။",
            "ဆီပူတွင် ပုစွန်ဘက်ကို အောက်မှောက်ထည့်ကာ မီးအေးအေးဖြင့် ၁ မိနစ်ခန့် ကြော်ပြီး အထက်အောက် လှန်ကာ ရွှေဝါရောင် သန်းလာပါက ဆယ်ယူ ဆီစစ်ပြီး တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "Peel prawns leaving tails intact, devein, butterfly flat along the back, and marinate with crushed scallions, ginger, pepper, and salt for 20 minutes.",
            "Trim crusts from bread and cut into 4 squares or triangles; whisk egg whites, flour, and cornstarch together into a smooth paste.",
            "Spread paste onto bread slices, press a butterflied prawn on top, and garnish with black sesame seeds and a fresh cilantro sprig.",
            "Slide prawn-side down into hot oil, fry over gentle heat for about 1 minute until crisp, flip to brown bread side, drain on paper towels, and serve hot."
        ],
        "tags": ["Prawn Toast", "Seafood", "Fried Snack", "Dim Sum", "Appetizer"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 153},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 153"}
    },
    {
        "recipe_id": "R0150",
        "name_mm": "သီဟိုဠ်စေ့အကြွပ်",
        "name_en": "Crispy Cashews",
        "description_mm": "သကြားနှင့် ပျားရည်ရည်တွင် ပြုတ်ပြီး ဆီတွင် ရွှေညိုရောင်သန်းသည်အထိ ကြော်ထားသော သီဟိုဠ်စေ့ကြွပ်။",
        "description_en": "Candied crispy cashew nuts boiled in honey and sugar syrup, then deep-fried until crunchy, glossy, and golden brown.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Snack", "Tea Time"],
        "ingredients": [
            {"ingredient_id": "I0206", "name_mm": "သီဟိုဠ်စေ့", "name_en": "Cashew nuts", "quantity": 5, "unit": "ကျပ်သား (g)", "notes_mm": "၈၂ ဂရမ်", "notes_en": "82g"},
            {"ingredient_id": "I0017", "name_mm": "ရေ", "name_en": "Water", "quantity": 0.17, "unit": "နို့ဆီဘူး (ml)", "notes_mm": "၁/၆ နို့ဆီဘူး (၅၀ မီလီလီတာ)", "notes_en": "1/6 tin (50 ml)"},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "quantity": 3, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "၃ စပဇ", "notes_en": "3 tbsp"},
            {"ingredient_id": "I0207", "name_mm": "ပျားရည်", "name_en": "Honey", "quantity": 3, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "၃ စပဇ", "notes_en": "3 tbsp"},
            {"ingredient_id": "I0003", "name_mm": "ဆီ", "name_en": "Cooking oil", "quantity": 2.5, "unit": "နို့ဆီဘူး (ml)", "notes_mm": "ကြော်ရန် ၂ ၁/၂ နို့ဆီဘူး (၇၅၀ မီလီလီတာ)", "notes_en": "For frying 2.5 tins (750 ml)"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "ဒယ်အိုးတွင် သီဟိုဠ်စေ့၊ ရေ၊ သကြား၊ ပျားရည်တို့ကို ရောထည့်ပြီး မီးအသင့်အတင့်ဖြင့် ရေဆူလာသည်အထိ ၅ မိနစ်ခန့် တည်ပြီး ရေစစ်ပါ။",
            "ကြော်ဆီကို အပူပေးပြီး မီးအေးအေးဖြင့် သီဟိုဠ်စေ့များ မြုပ်အောင်ထည့်ကာ ၈ မိနစ်ခန့် မကြာခဏ မွှေပေးရင်း ရွှေညိုရောင် သန်းသည်အထိ ကြော်ပါ။",
            "ဆယ်ယူပြီး ဆီစစ်ထားပါ၊ အေးလာပါက ကြွပ်ရွနေသော သီဟိုဠ်စေ့ကြွပ်များကို အဆာပြေအဖြစ် သုံးဆောင်နိုင်ပါသည်။"
        ],
        "instructions_en": [
            "In a saucepan, combine raw cashews, water, sugar, and honey; boil over medium heat for about 5 minutes, then drain thoroughly.",
            "Heat frying oil over medium-low heat, add the coated cashews, and deep-fry for about 8 minutes, stirring continuously until evenly golden brown.",
            "Remove with a slotted spoon and spread onto paper to drain; allow to cool completely into crunchy, glossy candied cashews."
        ],
        "tags": ["Cashews", "Snack", "Sweet", "Nuts", "Crispy"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 153},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 153"}
    },
    {
        "recipe_id": "R0151",
        "name_mm": "ယိုးဒယားသင်္ဘောသီးသုပ်",
        "name_en": "Green Papaya Salad (Thai)",
        "description_mm": "သင်္ဘောသီးစိမ်းခြစ်၊ ငရုတ်သီးစိမ်း၊ ကြက်သွန်ဖြူ၊ ပုစွန်ခြောက်၊ မြေပဲလှော်နှင့် သံပရာရည် ငံပြာရည်တို့ဖြင့် ဆုံတွင် ထောင်းသုပ်ထားသော ယိုးဒယားစတိုင် သင်္ဘောသီးသုပ်။",
        "description_en": "Authentic Thai-style Som Tum green papaya salad pounded in a mortar with garlic, chilies, dried shrimp, roasted peanuts, lime juice, and fish sauce.",
        "category": "အသုပ်များ",
        "meal_types": ["Lunch", "Dinner", "Snack"],
        "ingredients": [
            {"ingredient_id": "I0069", "name_mm": "သင်္ဘောသီး", "name_en": "Green papaya", "quantity": 20, "unit": "ကျပ်သား (g)", "notes_mm": "သင်္ဘောသီးစိမ်း ခြစ်ပြီး (၃၂၇ ဂရမ်)", "notes_en": "Shredded green papaya (327g)"},
            {"ingredient_id": "I0044", "name_mm": "ငရုတ်သီးစိမ်း", "name_en": "Green chili", "quantity": 7, "unit": "တောင့် (pod)", "notes_mm": "၇ တောင့်", "notes_en": "7 pods"},
            {"ingredient_id": "I0022", "name_mm": "ကြက်သွန်ဖြူ", "name_en": "Garlic", "quantity": 6, "unit": "မြွှာ (clove)", "notes_mm": "၆ မြွှာ", "notes_en": "6 cloves"},
            {"ingredient_id": "I0078", "name_mm": "မြေပဲလှော်", "name_en": "Roasted peanuts", "quantity": 4, "unit": "ကျပ်သား (g)", "notes_mm": "ဆားမပါ (၆၅ ဂရမ်)", "notes_en": "Unsalted (65g)"},
            {"ingredient_id": "I0021", "name_mm": "ပုစွန်ခြောက်", "name_en": "Dried shrimp", "quantity": 2, "unit": "ကျပ်သား (g)", "notes_mm": "၃၃ ဂရမ်", "notes_en": "33g"},
            {"ingredient_id": "I0042", "name_mm": "ခရမ်းချဉ်သီး", "name_en": "Tomato", "quantity": 6, "unit": "လုံး (piece)", "notes_mm": "၆ လုံး", "notes_en": "6 tomatoes"},
            {"ingredient_id": "I0106", "name_mm": "သံပရာသီး", "name_en": "Lime", "quantity": 0.5, "unit": "နို့ဆီဘူး (ml)", "notes_mm": "သံပရာရည် ၁/၂ နို့ဆီဘူး (၁၅၀ မီလီလီတာ)", "notes_en": "Fresh lime juice 1/2 tin (150 ml)"},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "quantity": 1, "unit": "စားပွဲဇွန်း (tbsp / g)", "notes_mm": "၁ စပဇ", "notes_en": "1 tbsp"},
            {"ingredient_id": "I0115", "name_mm": "ငံပြာရည်", "name_en": "Fish sauce", "quantity": 1, "unit": "စားပွဲဇွန်း (tbsp / ml)", "notes_mm": "၁ စပဇ", "notes_en": "1 tbsp"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "ငရုတ်သီးစိမ်းကို ခပ်ကြမ်းကြမ်း လှီးပြီး ကြက်သွန်ဖြူနှင့်အတူ ဆုံတွင် ခပ်ကြမ်းကြမ်း ထောင်းပါ။",
            "သင်္ဘောသီးစိမ်းကို အခွံနွှာ ခြစ်ထားပြီး ထောင်းထားသော ငရုတ်သီးကြက်သွန်ဖြူထဲသို့ နည်းနည်းချင်းထည့်ကာ ခပ်ကြမ်းကြမ်း ထုထောင်းပါ။",
            "ခွက်တစ်ခုတွင် ထည့်ကာ မြေပဲလှော်၊ ပုစွန်ခြောက်၊ လှီးထားသော ခရမ်းချဉ်သီး၊ သံပရာရည်၊ သကြားနှင့် ငံပြာရည်တို့ ထည့်ပြီး သမအောင် နယ်ဖတ်၍ တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "Roughly chop green chilies and lightly pound in a mortar together with peeled garlic cloves.",
            "Peel and finely shred green papaya; add gradually to the mortar, bruising gently with the pestle to absorb flavours.",
            "Transfer to a bowl, toss with roasted peanuts, dried shrimp, sliced tomatoes, lime juice, sugar, and fish sauce until well blended, and serve."
        ],
        "tags": ["Salad", "Papaya Salad", "Som Tum", "Thai-Inspired", "Spicy Salad"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 154},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 154"}
    },
    {
        "recipe_id": "R0152",
        "name_mm": "ရွှေဖရုံသီးအလုံးလိုက်ပူတင်း",
        "name_en": "Custard in Pumpkin",
        "description_mm": "ရွှေဖရုံသီးအလုံးလိုက် အတွင်းသားကို ထွင်းထုတ်ပြီး ကြက်ဥ၊ သကြားနှင့် အုန်းနို့အရော လောင်းထည့်ကာ ပေါင်းထားသော ရွှေဖရုံသီးပူတင်း။",
        "description_en": "Whole small pumpkin hollowed out and filled with rich coconut milk and egg custard, steamed until tender, and sliced into wedges.",
        "category": "မုန့်ပဲသွားရည်စာနှင့် အဆာပြေ",
        "meal_types": ["Dessert", "Snack"],
        "ingredients": [
            {"ingredient_id": "I0162", "name_mm": "ရွှေဖရုံသီး", "name_en": "Pumpkin", "quantity": 1, "unit": "လုံး (piece)", "notes_mm": "အသေး ၁ လုံး", "notes_en": "1 small whole pumpkin"},
            {"ingredient_id": "I0026", "name_mm": "ကြက်ဥ", "name_en": "Chicken egg", "quantity": 9, "unit": "လုံး (piece)", "notes_mm": "၉ လုံး", "notes_en": "9 eggs"},
            {"ingredient_id": "I0005", "name_mm": "သကြား", "name_en": "Sugar", "quantity": 20, "unit": "ကျပ်သား (g)", "notes_mm": "၃၂၇ ဂရမ်", "notes_en": "327g"},
            {"ingredient_id": "I0097", "name_mm": "အုန်းနို့", "name_en": "Coconut milk", "quantity": 0.17, "unit": "နို့ဆီဘူး (ml)", "notes_mm": "အုန်းနို့နှောင်းရည် ၁/၆ နို့ဆီဘူး (၅၀ မီလီလီတာ)", "notes_en": "Thin coconut milk 1/6 tin (50 ml)"}
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "ရွှေဖရုံသီးထိပ်မှ အညှာအောက်ခြေသားကို လုံးပတ်ကာ အပေါက်ဖောက် လှီးဖွင့်ပြီး အတွင်းရှိ အစေ့များကို သန့်စင်အောင် ခြစ်ထုတ်ပါ။",
            "ကြက်ဥကို ခေါက်ပြီး သကြား၊ အုန်းနို့ရည်တို့ဖြင့် အမြှုပ်ပွလာသည်အထိ ခေါက်ကာ ၁၀ မိနစ်ခန့် ထားပြီး အဝတ်ပါးဖြင့် စစ်ကာ ရွှေဖရုံသီးထဲသို့ လောင်းထည့်ပြီး အညှာဖုံး ပြန်အုပ်ပါ။",
            "ပေါင်းချောင်ထဲတွင် ထည့်၍ အဖုံးအုပ်ပြီး မိနစ် ၃၀ ခန့် ပေါင်းပါ၊ တံစို့ဖြင့် ထိုးစိုက်ကြည့်၍ မကပ်ပါက ကျက်နပ်ပါပြီ။",
            "မတည်ခင်းမီ ရေခဲသေတ္တာထဲ ထည့်ကာ အအေးခံပြီး အညှာအုပ်ကို ဖွင့်၍ အစိပ်လိုက် လှီးစိတ်ကာ တည်ခင်းပါ။"
        ],
        "instructions_en": [
            "Cut a round lid off the top of the pumpkin around the stem and scoop out all the inner seeds and fibers cleanly with a spoon.",
            "Whisk eggs with sugar and thin coconut milk until frothy, rest for 10 minutes, strain through a fine cloth, pour into the hollowed pumpkin, and replace the pumpkin top lid.",
            "Place into a steamer basket, cover tightly, and steam over simmering water for about 30 minutes until a skewer inserted comes out clean.",
            "Chill thoroughly in the refrigerator before serving, remove the lid, slice into beautiful wedges displaying the rich custard inside, and serve."
        ],
        "tags": ["Custard", "Pumpkin", "Dessert", "Coconut Milk", "Steamed"],
        "nutrition": {"calories": None, "protein_g": None, "fat_g": None, "carbohydrates_g": None},
        "estimated_cost_mmk": None,
        "source": {"book_title_mm": "ဟင်းချက်နည်းများ", "book_title_en": "Myanmar Cookbook Recipes", "page_number": 154},
        "data_quality": {"is_verified": True, "verification_notes": "Extracted from printed cookbook p. 154"}
    }
]
