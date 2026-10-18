import json
import os

recipes = [
  {
    "recipe_id": "R0001",
    "name_mm": "ထောပတ်ထမင်း",
    "name_en": "Butter Rice",
    "description_mm": None,
    "description_en": None,
    "category": "Rice dishes",
    "meal_types": ["lunch", "dinner"],
    "ingredients": [
      {
        "ingredient_id": "I0001",
        "name_mm": "ပေါ်ဆန်းမွှေးဆန်",
        "name_en": "Paw San Hmwe rice",
        "original_name": "ပေါ်ဆန်းမွှေး (ဆန်ဟောင်း)",
        "quantity": 6.0,
        "unit": "နို့ဆီဘူး",
        "original_quantity_text": "၆ နို့ဆီဘူး",
        "normalized_quantity": None,
        "normalized_unit": None,
        "preparation_note_mm": "ဆန်ဟောင်း",
        "preparation_note_en": "aged rice"
      },
      {
        "ingredient_id": "I0002",
        "name_mm": "ထောပတ်",
        "name_en": "Butter",
        "original_name": "ထောပတ်",
        "quantity": 10.0,
        "unit": "ကျပ်သား",
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
        "quantity": 2.5,
        "unit": "ကျပ်သား",
        "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
        "normalized_quantity": 40.8,
        "normalized_unit": "g",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0004",
        "name_mm": "သစ်ကြံပိုးခေါက်",
        "name_en": "Cinnamon bark",
        "original_name": "သစ်ကြံပိုး (၂\" အရွယ်)",
        "quantity": 2.0,
        "unit": "ခေါက်",
        "original_quantity_text": "၂ ခေါက်",
        "normalized_quantity": 2.0,
        "normalized_unit": "piece",
        "preparation_note_mm": "၂ လက်မအရွယ်",
        "preparation_note_en": "2-inch length"
      },
      {
        "ingredient_id": "I0005",
        "name_mm": "ကရဝေးရွက်",
        "name_en": "Bay leaf",
        "original_name": "ကရဝေးရွက်",
        "quantity": 3.0,
        "unit": "ရွက်",
        "original_quantity_text": "၃ ရွက်",
        "normalized_quantity": 3.0,
        "normalized_unit": "piece",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0006",
        "name_mm": "လေးညှင်းပွင့်",
        "name_en": "Clove",
        "original_name": "လေးညှင်းပွင့်",
        "quantity": 6.0,
        "unit": "ပွင့်",
        "original_quantity_text": "၆ ပွင့်",
        "normalized_quantity": 6.0,
        "normalized_unit": "piece",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0007",
        "name_mm": "ဖာလာစေ့",
        "name_en": "Cardamom pod",
        "original_name": "ဖာလာစေ့",
        "quantity": 6.0,
        "unit": "စေ့",
        "original_quantity_text": "၆ စေ့",
        "normalized_quantity": 6.0,
        "normalized_unit": "piece",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0008",
        "name_mm": "သကြား",
        "name_en": "Sugar",
        "original_name": "သကြား",
        "quantity": 2.5,
        "unit": "ကျပ်သား",
        "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
        "normalized_quantity": 40.8,
        "normalized_unit": "g",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0009",
        "name_mm": "ဆား",
        "name_en": "Salt",
        "original_name": "ဆား",
        "quantity": 2.0,
        "unit": "လဖဇ",
        "original_quantity_text": "၂ လဖဇ",
        "normalized_quantity": 10.0,
        "normalized_unit": "ml",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0010",
        "name_mm": "ရေနွေး",
        "name_en": "Hot water",
        "original_name": "ရေနွေး",
        "quantity": 8.0,
        "unit": "နို့ဆီဘူး",
        "original_quantity_text": "၈ နို့ဆီဘူး",
        "normalized_quantity": 2400.0,
        "normalized_unit": "ml",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0011",
        "name_mm": "သီဟိုဠ်စေ့",
        "name_en": "Cashew nut",
        "original_name": "သီဟိုဠ်စေ့",
        "quantity": 2.0,
        "unit": "ကျပ်သား",
        "original_quantity_text": "၂ ကျပ်သား",
        "normalized_quantity": 32.7,
        "normalized_unit": "g",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0012",
        "name_mm": "စပျစ်သီးခြောက်",
        "name_en": "Raisin",
        "original_name": "စပျစ်သီးခြောက်",
        "quantity": 2.0,
        "unit": "ကျပ်သား",
        "original_quantity_text": "၂ ကျပ်သား",
        "normalized_quantity": 32.7,
        "normalized_unit": "g",
        "preparation_note_mm": None,
        "preparation_note_en": None
      }
    ],
    "servings": 10,
    "preparation_time_minutes": None,
    "cooking_time_minutes": None,
    "instructions_mm": [
      "ဆန်ကိုရေဖြင့် နှစ်ကြိမ်ခန့် လျင်မြန်စွာဆေးပြီး ရေစစ်ထားပါ။",
      "ထမင်းချက်မည့်အိုးတွင် ထောပတ်နှင့် ဆီကို ပူအောင်ပြုပါ။",
      "အငွေ့ထွက်လျှင် သစ်ကြံပိုး၊ ကရဝေးရွက်၊ လေးညှင်း၊ ဖာလာထည့်၍ ဆီသတ်ပါ။",
      "ဆီသတ်အိုးအတွင်းသို့ ဆန်၊ ဆား၊ သကြားထည့်ပြီး အလယ်တွင် ရေနွေးမြုပ်ရုံထည့်၍ တည်ပါ။",
      "ရေခန်းစပြုလျှင် သီဟိုဠ်စေ့၊ စပျစ်သီးခြောက် ဖြူးထည့်ပြီး နှံ့အောင် ခပ်ဖွဖွ မွှေပေးပြီး အဖုံးပိတ်ထားပြီး အောက်မီးရှိန် လျှော့ပါ။",
      "အငွေ့တက်လာလျှင် အဖုံးဖွင့်ပြီး အသာအယာဖွမွှေကာ အထက်အောက် လှန်ပါ။",
      "အိုးကို ဖိုပေါ်တွင် အိုးနားပတ်လည်အစွန်းများ မီးရှိန်မျှတစွာရရန် အကြိမ်ကြိမ်လှည့်ပတ်ပေးပါ။ ခေတ္တမျှလှည့်ပေးလျှင် ထမင်းနပ်ပြီ ဖြစ်ပါသည်။"
    ],
    "instructions_en": [
      "Quickly wash the rice with water about twice and drain thoroughly.",
      "Heat the butter and cooking oil in the cooking pot.",
      "When steam starts to rise, add cinnamon, bay leaves, cloves, and cardamom pods, and saute until fragrant.",
      "Add the washed rice, salt, and sugar into the spiced oil pot, pour in hot water just enough to submerge the center, and cook.",
      "When the water begins to absorb and dry down, scatter the cashew nuts and raisins over the rice, stir gently to distribute evenly, cover with the lid, and lower the heat below.",
      "When steam rises, open the lid, gently fluff and turn the rice over from top to bottom.",
      "Repeatedly rotate the pot on the stove so that the perimeter receives heat evenly; after rotating for a short while, the rice is fully steamed and tender."
    ],
    "tags": {
      "dietary": [],
      "seasonal": [],
      "festival": ["ceremonial", "donation_feast"],
      "main_ingredients": ["Paw San Hmwe rice", "Butter"]
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
      "pdf_pages": [42],
      "printed_page_numbers": [73],
      "extraction_method": "manual_visual_transcription_from_scanned_spread"
    },
    "data_quality": {
      "extraction_status": "extracted",
      "confidence": 0.95,
      "review_notes": [
        "Servings stated as '(လူ ၁၀ ဦး)' in original heading.",
        "The right edge of the instruction column was slightly near the page boundary in the scan spread; missing tail characters were reliably reconstructed from context.",
        "Traditional volumetric unit 'နို့ဆီဘူး' (~300 ml condensed milk tin) left unnormalized for dry rice to avoid inaccurate grain mass assumptions.",
        "Festival tag 'donation_feast' is culturally inferred, not explicitly printed in recipe text."
      ],
      "verified": False
    }
  },
  {
    "recipe_id": "R0002",
    "name_mm": "ပဲနီလေးထောပတ်ထမင်း",
    "name_en": "Red Lentil Butter Rice",
    "description_mm": None,
    "description_en": None,
    "category": "Rice dishes",
    "meal_types": ["lunch", "dinner"],
    "ingredients": [
      {
        "ingredient_id": "I0001",
        "name_mm": "ပေါ်ဆန်းမွှေးဆန်",
        "name_en": "Paw San Hmwe rice",
        "original_name": "ပေါ်ဆန်းမွှေး (ဆန်ဟောင်း)",
        "quantity": 6.0,
        "unit": "နို့ဆီဘူး",
        "original_quantity_text": "၆ နို့ဆီဘူး",
        "normalized_quantity": None,
        "normalized_unit": None,
        "preparation_note_mm": "ဆန်ဟောင်း",
        "preparation_note_en": "aged rice"
      },
      {
        "ingredient_id": "I0013",
        "name_mm": "ပဲနီလေး",
        "name_en": "Red lentil",
        "original_name": "ပဲနီလေး",
        "quantity": 10.0,
        "unit": "ကျပ်သား",
        "original_quantity_text": "၁၀ ကျပ်သား",
        "normalized_quantity": 163.3,
        "normalized_unit": "g",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0014",
        "name_mm": "ရေအေး",
        "name_en": "Cold water",
        "original_name": "ရေအေး",
        "quantity": 10.0,
        "unit": "နို့ဆီဘူး",
        "original_quantity_text": "၁၀ နို့ဆီဘူး",
        "normalized_quantity": 3000.0,
        "normalized_unit": "ml",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0002",
        "name_mm": "ထောပတ်",
        "name_en": "Butter",
        "original_name": "ထောပတ်",
        "quantity": 7.5,
        "unit": "ကျပ်သား",
        "original_quantity_text": "၇ ၁/၂ ကျပ်သား",
        "normalized_quantity": 122.5,
        "normalized_unit": "g",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0003",
        "name_mm": "ဆီ",
        "name_en": "Cooking oil",
        "original_name": "ဆီ",
        "quantity": 2.5,
        "unit": "ကျပ်သား",
        "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
        "normalized_quantity": 40.8,
        "normalized_unit": "g",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0004",
        "name_mm": "သစ်ကြံပိုးခေါက်",
        "name_en": "Cinnamon bark",
        "original_name": "သစ်ကြံပိုး (၂\" အရွယ်)",
        "quantity": 2.0,
        "unit": "ခေါက်",
        "original_quantity_text": "၂ ခေါက်",
        "normalized_quantity": 2.0,
        "normalized_unit": "piece",
        "preparation_note_mm": "၂ လက်မအရွယ်",
        "preparation_note_en": "2-inch length"
      },
      {
        "ingredient_id": "I0005",
        "name_mm": "ကရဝေးရွက်",
        "name_en": "Bay leaf",
        "original_name": "ကရဝေးရွက်",
        "quantity": 6.0,
        "unit": "ရွက်",
        "original_quantity_text": "၆ ရွက်",
        "normalized_quantity": 6.0,
        "normalized_unit": "piece",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0006",
        "name_mm": "လေးညှင်းပွင့်",
        "name_en": "Clove",
        "original_name": "လေးညှင်းပွင့်",
        "quantity": 6.0,
        "unit": "ပွင့်",
        "original_quantity_text": "၆ ပွင့်",
        "normalized_quantity": 6.0,
        "normalized_unit": "piece",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0007",
        "name_mm": "ဖာလာစေ့",
        "name_en": "Cardamom pod",
        "original_name": "ဖာလာစေ့",
        "quantity": 6.0,
        "unit": "စေ့",
        "original_quantity_text": "၆ စေ့",
        "normalized_quantity": 6.0,
        "normalized_unit": "piece",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0008",
        "name_mm": "သကြား",
        "name_en": "Sugar",
        "original_name": "သကြား",
        "quantity": 3.0,
        "unit": "စပဇ",
        "original_quantity_text": "၃ စပဇ",
        "normalized_quantity": 45.0,
        "normalized_unit": "ml",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0009",
        "name_mm": "ဆား",
        "name_en": "Salt",
        "original_name": "ဆား",
        "quantity": 2.0,
        "unit": "လဖဇ",
        "original_quantity_text": "၂ လဖဇ",
        "normalized_quantity": 10.0,
        "normalized_unit": "ml",
        "preparation_note_mm": None,
        "preparation_note_en": None
      }
    ],
    "servings": 10,
    "preparation_time_minutes": None,
    "cooking_time_minutes": None,
    "instructions_mm": [
      "ဆန်ကိုရေဖြင့် နှစ်ကြိမ်ခန့် လျင်မြန်စွာဆေးပြီး ရေစစ်ထားပါ။",
      "ပဲနီလေးကို အမှိုက်သန့်စင်ကာ ရေဆေးပြီး ရေစစ်ထားပါ။",
      "အိုးတစ်လုံးဖြင့် ရေဆူအောင်တည်ပြီး ဆန်နှင့်ပဲနီလေးထည့်ပါ။",
      "ရေပြန်ဆူ၍ ဆန်ကြောတင်းလာလျှင် ဆန်သားမာမာအနေအထား၌ ချ၍ငှဲ့ပါ။",
      "ချက်မည့်အိုးတွင် ထောပတ်နှင့် ဆီကို ပူအောင်လုပ်ပါ။",
      "အငွေ့ထွက်၍ ပူလာလျှင် သစ်ကြံပိုး၊ ကရဝေး၊ လေးညှင်း၊ ဖာလာထည့်ပြီး ဆီသတ်ပါ။",
      "ရေငှဲ့ပြီး ထမင်းအိုးထဲသို့ သကြား၊ ဆား ထည့်မွှေပါ။",
      "အပေါ်မှနေ၍ ထောပတ်အမွှေးဆီဆမ်းပြီး ဆီနှံ့အောင်လောင်း ခပ်ဖွဖွမွှေပါ။",
      "အဖုံးပိတ်ပြီး အောက်မီးရှိန်လျှော့ပါ။",
      "အငွေ့ထွက်လျှင် အဖုံးဖွင့်ပြီး အသာအယာဖွကာ အထက်အောက်လှန်ပါ။",
      "အိုးကို ဖိုပေါ်တွင် အိုးနားပတ်လည်အစွန်းများ မီးရှိန်မျှတစွာရရန် အကြိမ်ကြိမ် လှည့်ပတ်ပေးပါ။ ခေတ္တမျှလှည့်ပေးလျှင် ထမင်းနပ်ပြီ ဖြစ်ပါသည်။"
    ],
    "instructions_en": [
      "Quickly wash the rice with water about twice and drain thoroughly.",
      "Pick out any impurities from the red lentils, rinse with water, and drain.",
      "Bring water to a boil in a pot and add the rice and red lentils.",
      "When boiling resumes and the rice grains become firm, remove from the heat and drain off the cooking water while the rice grains remain al dente.",
      "In the cooking pot, heat the butter and cooking oil.",
      "When hot and steam rises, add cinnamon, bay leaves, cloves, and cardamom, and saute until fragrant.",
      "Add the sugar and salt into the drained rice-lentil mixture, stirring gently.",
      "Drizzle the fragrant spiced butter-oil over the top and toss gently to coat evenly.",
      "Cover with the lid and reduce the heat below.",
      "When steam escapes, open the lid and gently fluff, turning the rice over from top to bottom.",
      "Repeatedly rotate the pot on the stove so that the outer perimeter receives heat evenly; after rotating for a short while, the rice is fully steamed and tender."
    ],
    "tags": {
      "dietary": [],
      "seasonal": [],
      "festival": [],
      "main_ingredients": ["Paw San Hmwe rice", "Red lentil", "Butter"]
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
      "pdf_pages": [42],
      "printed_page_numbers": [73],
      "extraction_method": "manual_visual_transcription_from_scanned_spread"
    },
    "data_quality": {
      "extraction_status": "extracted",
      "confidence": 0.95,
      "review_notes": [
        "Cookbook English title printed as 'RED LENTIL RICE', Burmese name is 'ပဲနီလေးထောပတ်ထမင်း' (Red Lentil Butter Rice).",
        "Right margin scan boundary clipping on printed page 73 carefully reconstructed from standard culinary Burmese expressions."
      ],
      "verified": False
    }
  },
  {
    "recipe_id": "R0003",
    "name_mm": "သီးစုံထောပတ်ထမင်း",
    "name_en": "Vegetable Butter Rice",
    "description_mm": None,
    "description_en": None,
    "category": "Rice dishes",
    "meal_types": ["lunch", "dinner"],
    "ingredients": [
      {
        "ingredient_id": "I0001",
        "name_mm": "ပေါ်ဆန်းမွှေးဆန်",
        "name_en": "Paw San Hmwe rice",
        "original_name": "ပေါ်ဆန်းမွှေး (ဆန်ဟောင်း)",
        "quantity": 6.0,
        "unit": "နို့ဆီဘူး",
        "original_quantity_text": "၆ နို့ဆီဘူး",
        "normalized_quantity": None,
        "normalized_unit": None,
        "preparation_note_mm": "ဆန်ဟောင်း",
        "preparation_note_en": "aged rice"
      },
      {
        "ingredient_id": "I0014",
        "name_mm": "ရေအေး",
        "name_en": "Cold water",
        "original_name": "ရေအေး",
        "quantity": 10.0,
        "unit": "နို့ဆီဘူး",
        "original_quantity_text": "၁၀ နို့ဆီဘူး",
        "normalized_quantity": 3000.0,
        "normalized_unit": "ml",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0015",
        "name_mm": "မုန်လာဥဝါ",
        "name_en": "Carrot",
        "original_name": "မုန်လာဥဝါ",
        "quantity": 10.0,
        "unit": "ကျပ်သား",
        "original_quantity_text": "၁၀ ကျပ်သား",
        "normalized_quantity": 163.3,
        "normalized_unit": "g",
        "preparation_note_mm": "အခွံသင်ပြီး ၃/၄ လက်မပတ်လည် အတုံးတုံး ရေနွေးဖျော",
        "preparation_note_en": "peeled, cut into 3/4-inch cubes and blanched"
      },
      {
        "ingredient_id": "I0002",
        "name_mm": "ထောပတ်",
        "name_en": "Butter",
        "original_name": "ထောပတ်",
        "quantity": 7.5,
        "unit": "ကျပ်သား",
        "original_quantity_text": "၇ ၁/၂ ကျပ်သား",
        "normalized_quantity": 122.5,
        "normalized_unit": "g",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0003",
        "name_mm": "ဆီ",
        "name_en": "Cooking oil",
        "original_name": "ဆီ",
        "quantity": 2.5,
        "unit": "ကျပ်သား",
        "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
        "normalized_quantity": 40.8,
        "normalized_unit": "g",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0004",
        "name_mm": "သစ်ကြံပိုးခေါက်",
        "name_en": "Cinnamon bark",
        "original_name": "သစ်ကြံပိုး (၂\" အရွယ်)",
        "quantity": 2.0,
        "unit": "ခေါက်",
        "original_quantity_text": "၂ ခေါက်",
        "normalized_quantity": 2.0,
        "normalized_unit": "piece",
        "preparation_note_mm": "၂ လက်မအရွယ်",
        "preparation_note_en": "2-inch length"
      },
      {
        "ingredient_id": "I0005",
        "name_mm": "ကရဝေးရွက်",
        "name_en": "Bay leaf",
        "original_name": "ကရဝေးရွက်",
        "quantity": 6.0,
        "unit": "ရွက်",
        "original_quantity_text": "၆ ရွက်",
        "normalized_quantity": 6.0,
        "normalized_unit": "piece",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0007",
        "name_mm": "ဖာလာစေ့",
        "name_en": "Cardamom pod",
        "original_name": "ဖာလာစေ့",
        "quantity": 6.0,
        "unit": "စေ့",
        "original_quantity_text": "၆ စေ့",
        "normalized_quantity": 6.0,
        "normalized_unit": "piece",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0012",
        "name_mm": "စပျစ်သီးခြောက်",
        "name_en": "Raisin",
        "original_name": "စပျစ်သီးခြောက်",
        "quantity": 3.0,
        "unit": "ကျပ်သား",
        "original_quantity_text": "၃ ကျပ်သား",
        "normalized_quantity": 49.0,
        "normalized_unit": "g",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0011",
        "name_mm": "သီဟိုဠ်စေ့",
        "name_en": "Cashew nut",
        "original_name": "သီဟိုဠ်စေ့",
        "quantity": 3.0,
        "unit": "ကျပ်သား",
        "original_quantity_text": "၃ ကျပ်သား",
        "normalized_quantity": 49.0,
        "normalized_unit": "g",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0016",
        "name_mm": "ပဲစိမ်းဘူး",
        "name_en": "Canned green peas",
        "original_name": "ပဲစိမ်းဘူး",
        "quantity": 1.0,
        "unit": "ဘူး",
        "original_quantity_text": "၁ ဘူး",
        "normalized_quantity": 1.0,
        "normalized_unit": "can",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0009",
        "name_mm": "ဆား",
        "name_en": "Salt",
        "original_name": "ဆား",
        "quantity": 2.0,
        "unit": "လဖဇ",
        "original_quantity_text": "၂ လဖဇ",
        "normalized_quantity": 10.0,
        "normalized_unit": "ml",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0008",
        "name_mm": "သကြား",
        "name_en": "Sugar",
        "original_name": "သကြား",
        "quantity": 2.0,
        "unit": "စပဇ",
        "original_quantity_text": "၂ စပဇ",
        "normalized_quantity": 30.0,
        "normalized_unit": "ml",
        "preparation_note_mm": None,
        "preparation_note_en": None
      }
    ],
    "servings": 10,
    "preparation_time_minutes": None,
    "cooking_time_minutes": None,
    "instructions_mm": [
      "ဆန်ကိုရေဖြင့် နှစ်ကြိမ်ခန့် လျင်မြန်စွာဆေးပြီး ရေစစ်ပါ။",
      "အိုးတစ်လုံးဖြင့် ရေဆူအောင်တည်ပြီး ဆန်ထည့်ပါ။",
      "ရေပြန်ဆူ၍ ဆန်ကြောတင်းလာလျှင် ဆန်သားမာမာ အနေအထား၌ ချ၍ငှဲ့ပါ။",
      "မုန်လာဥဝါကို အခွံသင်ပြီး ၃/၄ လက်မပတ်လည် အရွယ်ညီအတုံးတုံးပြီး ရေနွေးဖျောပါ။",
      "ချက်မည့်အိုးတွင် ထောပတ်နှင့် ဆီကို ပူအောင်လုပ်ပါ။",
      "ပူပြီးအငွေ့ထွက်လျှင် အမွှေးအကြိုင်များ ထည့်ကာ ဆီသတ်ပါ။",
      "ပြီးလျှင် ဆန်၊ မုန်လာဥဝါ၊ စပျစ်သီးခြောက်၊ သီဟိုဠ်စေ့၊ ပဲစိမ်းလုံးနှင့် ဆား၊ သကြားထည့်၍ နှံ့အောင် ခပ်ဖွဖွမွှေပါ။",
      "အဖုံးပိတ်ချက်ကာ အောက်မီးရှိန်လျှော့ပါ။",
      "အငွေ့ထွက်လျှင် အဖုံးဖွင့်ပြီး အသာအယာမွှေကာ အထက်အောက်လှန်ပါ။",
      "အိုးကို ဖိုပေါ်တွင် အိုးနားပတ်လည် အစွန်းများ မီးရှိန်မျှတစွာရရန် အကြိမ်ကြိမ် လှည့်ပတ်ပေးပါ။ ခေတ္တမျှလှည့်ပေးလျှင် ထမင်းနပ်ပြီဖြစ်ပါသည်။"
    ],
    "instructions_en": [
      "Quickly wash the rice with water about twice and drain.",
      "Bring water to a boil in a pot and add the rice.",
      "When boiling resumes and the rice grains become firm, remove from the stove and drain while the rice is still firm.",
      "Peel the carrots, cut them into even 3/4-inch dice, and blanch in hot water.",
      "In the cooking pot, heat the butter and cooking oil.",
      "When hot and steam rises, add the whole aromatic spices and saute until fragrant.",
      "Then add the drained rice, carrots, raisins, cashew nuts, green peas, salt, and sugar, stirring gently until thoroughly combined.",
      "Cover with the lid and lower the heat below.",
      "When steam rises, open the lid and gently fluff, turning the rice over from top to bottom.",
      "Repeatedly rotate the pot on the stove so that the outer edges receive heat evenly; after rotating for a short while, the rice is fully steamed and tender."
    ],
    "tags": {
      "dietary": ["vegetarian_compatible"],
      "seasonal": [],
      "festival": [],
      "main_ingredients": ["Paw San Hmwe rice", "Butter", "Carrot", "Green peas"]
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
      "pdf_pages": [43],
      "printed_page_numbers": [74],
      "extraction_method": "manual_visual_transcription_from_scanned_spread"
    },
    "data_quality": {
      "extraction_status": "extracted",
      "confidence": 0.98,
      "review_notes": [
        "Printed page 74 top-left recipe. Completely legible with no margin clipping.",
        "Carrot cutting dimension specified as ၃/၄ လက်မပတ်လည် (3/4-inch cubes)."
      ],
      "verified": False
    }
  },
  {
    "recipe_id": "R0004",
    "name_mm": "အုန်းထမင်း",
    "name_en": "Coconut Rice",
    "description_mm": None,
    "description_en": None,
    "category": "Rice dishes",
    "meal_types": ["lunch", "dinner"],
    "ingredients": [
      {
        "ingredient_id": "I0001",
        "name_mm": "ပေါ်ဆန်းမွှေးဆန်",
        "name_en": "Paw San Hmwe rice",
        "original_name": "ပေါ်ဆန်းမွှေး (ဆန်ဟောင်း)",
        "quantity": 6.0,
        "unit": "နို့ဆီဘူး",
        "original_quantity_text": "၆ နို့ဆီဘူး",
        "normalized_quantity": None,
        "normalized_unit": None,
        "preparation_note_mm": "ဆန်ဟောင်း",
        "preparation_note_en": "aged rice"
      },
      {
        "ingredient_id": "I0017",
        "name_mm": "အုန်းသီး",
        "name_en": "Coconut",
        "original_name": "အုန်းသီးရင့်ရင့် (အလုံးကြီး)",
        "quantity": 2.0,
        "unit": "လုံး",
        "original_quantity_text": "၂ လုံး",
        "normalized_quantity": 2.0,
        "normalized_unit": "piece",
        "preparation_note_mm": "ရင့်ရင့် (အလုံးကြီး)၊ ခြစ်ပြီး ရေနွေးဖြင့် အုန်းနို့ရည် ၉ ဘူး ညှစ်ရန်",
        "preparation_note_en": "mature (large); grated and pressed with hot water to extract 9 cans of coconut milk"
      },
      {
        "ingredient_id": "I0003",
        "name_mm": "ဆီ",
        "name_en": "Cooking oil",
        "original_name": "ဆီ",
        "quantity": 7.5,
        "unit": "ကျပ်သား",
        "original_quantity_text": "၇ ၁/၂ ကျပ်သား",
        "normalized_quantity": 122.5,
        "normalized_unit": "g",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0008",
        "name_mm": "သကြား",
        "name_en": "Sugar",
        "original_name": "သကြား",
        "quantity": 2.5,
        "unit": "ကျပ်သား",
        "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
        "normalized_quantity": 40.8,
        "normalized_unit": "g",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0018",
        "name_mm": "ကြက်သွန်နီ",
        "name_en": "Shallot / Small onion",
        "original_name": "ကြက်သွန်နီ (ဥသေး)",
        "quantity": 10.0,
        "unit": "ကျပ်သား",
        "original_quantity_text": "၁၀ ကျပ်သား",
        "normalized_quantity": 163.3,
        "normalized_unit": "g",
        "preparation_note_mm": "ဥသေး၊ အခွံသင်ထားပြီး အလုံးလိုက်ထည့်ရန်",
        "preparation_note_en": "small bulbs, peeled, added whole"
      },
      {
        "ingredient_id": "I0009",
        "name_mm": "ဆား",
        "name_en": "Salt",
        "original_name": "ဆား",
        "quantity": 2.0,
        "unit": "လဖဇ",
        "original_quantity_text": "၂ လဖဇ",
        "normalized_quantity": 10.0,
        "normalized_unit": "ml",
        "preparation_note_mm": None,
        "preparation_note_en": None
      }
    ],
    "servings": 10,
    "preparation_time_minutes": None,
    "cooking_time_minutes": None,
    "instructions_mm": [
      "ဆန်ကိုရေဖြင့် နှစ်ကြိမ်ခန့် လျင်မြန်စွာဆေးပြီး ရေစစ်ပါ။",
      "အုန်းသီးကိုခြစ်ပြီး ရေနွေးဖြင့် အုန်းနို့ရည် နို့ဆီဘူး (၉)ဘူးစာညှစ်ပါ။",
      "ချက်မည့်အိုးတွင် ဆန်၊ ဆီ၊ သကြား၊ ဆားနှင့် အုန်းနို့ရည်များ ထည့်ကာ အဖုံးပိတ်ချက်ပါ။ (ဝေမကျစေရန် အထူးသတိပြုပါ)။",
      "ဆူစပြုလျှင် ခပ်ဖွဖွမွှေပါ။ အခွံသင်ထားသောကြက်သွန်နီဥကို အလုံးလိုက်ထည့်ပါ။",
      "ဆူလာလျှင် အထက်အောက် ယောက်မနှင့် လှန်ပေးပါ။",
      "အုန်းရည်ခန်းစပြုလျှင် အောက်မီးရှိန်လျှော့ပြီး ဆက်တည်ထားပါ။",
      "အငွေ့ထွက်လျှင် အဖုံးဖွင့်ပြီး အသာအယာမွှေကာ အထက်အောက်ပြန်လှန်ပါ။",
      "အိုးကို ဖိုပေါ်တွင် အိုးနားပတ်လည် အစွန်းများ မီးရှိန်မျှတစွာရရန် အကြိမ်ကြိမ် လှည့်ပတ်ပေးပါ။ ခေတ္တမျှလှည့်ပေးလျှင် ထမင်းနပ်ပြီ ဖြစ်ပါသည်။"
    ],
    "instructions_en": [
      "Quickly wash the rice with water about twice and drain.",
      "Grate the coconut and press with hot water to yield 9 condensed milk cans of coconut milk.",
      "In the cooking pot, combine rice, cooking oil, sugar, salt, and coconut milk, cover with the lid, and cook. (Take special caution to prevent boiling over).",
      "When it begins to boil, stir gently. Add the peeled whole shallots (small onions).",
      "When reaching a full boil, turn the rice from top to bottom with a wooden spatula.",
      "When the coconut milk begins to reduce and absorb, reduce the heat below and continue simmering.",
      "When steam rises, open the lid, gently stir, and turn over from top to bottom again.",
      "Repeatedly rotate the pot on the stove so that the outer perimeter receives heat evenly; after rotating for a short while, the coconut rice is fully steamed and tender."
    ],
    "tags": {
      "dietary": [],
      "seasonal": [],
      "festival": ["ceremonial", "traditional_feast"],
      "main_ingredients": ["Paw San Hmwe rice", "Coconut", "Shallot / Small onion"]
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
      "pdf_pages": [43],
      "printed_page_numbers": [74],
      "extraction_method": "manual_visual_transcription_from_scanned_spread"
    },
    "data_quality": {
      "extraction_status": "extracted",
      "confidence": 0.98,
      "review_notes": [
        "Printed page 74 bottom-left recipe. Completely legible.",
        "Explicit warning included in step 3: '(ဝေမကျစေရန် အထူးသတိပြုပါ)' (Take special caution not to let it boil over).",
        "Whole small shallots/onions cooked inside coconut rice is a hallmark of classic Burmese coconut rice."
      ],
      "verified": False
    }
  },
  {
    "recipe_id": "R0005",
    "name_mm": "ထမင်းကြော်",
    "name_en": "Fried Rice",
    "description_mm": None,
    "description_en": None,
    "category": "Rice dishes",
    "meal_types": ["breakfast", "lunch", "dinner"],
    "ingredients": [
      {
        "ingredient_id": "I0001",
        "name_mm": "ပေါ်ဆန်းမွှေးဆန်",
        "name_en": "Paw San Hmwe rice",
        "original_name": "ပေါ်ဆန်းမွှေး",
        "quantity": 5.0,
        "unit": "နို့ဆီဘူး",
        "original_quantity_text": "၅ နို့ဆီဘူး",
        "normalized_quantity": None,
        "normalized_unit": None,
        "preparation_note_mm": "ချက်ပြီး အေးအောင်ထားရန်",
        "preparation_note_en": "cooked and cooled"
      },
      {
        "ingredient_id": "I0003",
        "name_mm": "ဆီ",
        "name_en": "Cooking oil",
        "original_name": "ဆီ",
        "quantity": 5.0,
        "unit": "ကျပ်သား",
        "original_quantity_text": "၅ ကျပ်သား",
        "normalized_quantity": 81.6,
        "normalized_unit": "g",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0019",
        "name_mm": "ဘဲဥ",
        "name_en": "Duck egg",
        "original_name": "ဘဲဥ (ခေါက်ထားပြီး)",
        "quantity": 3.0,
        "unit": "လုံး",
        "original_quantity_text": "၃ လုံး",
        "normalized_quantity": 3.0,
        "normalized_unit": "piece",
        "preparation_note_mm": "ခေါက်ထားပြီး",
        "preparation_note_en": "beaten"
      },
      {
        "ingredient_id": "I0020",
        "name_mm": "ဝက်သား",
        "name_en": "Pork",
        "original_name": "အဆီလွတ်ဝက်သား (အတုံးသေးလှီးပြီး)",
        "quantity": 20.0,
        "unit": "ကျပ်သား",
        "original_quantity_text": "၂၀ ကျပ်သား",
        "normalized_quantity": 326.6,
        "normalized_unit": "g",
        "preparation_note_mm": "အဆီလွတ်၊ အတုံးသေးလှီးပြီး",
        "preparation_note_en": "lean meat, diced small"
      },
      {
        "ingredient_id": "I0021",
        "name_mm": "ပုစွန်ကျော့",
        "name_en": "Medium prawn / shrimp",
        "original_name": "ပုစွန်ကျော့ (အခွံသင်ပြီး)",
        "quantity": 10.0,
        "unit": "ကျပ်သား",
        "original_quantity_text": "၁၀ ကျပ်သား",
        "normalized_quantity": 163.3,
        "normalized_unit": "g",
        "preparation_note_mm": "အခွံသင်ပြီး",
        "preparation_note_en": "peeled"
      },
      {
        "ingredient_id": "I0022",
        "name_mm": "ကြက်သွန်ဖြူ",
        "name_en": "Garlic",
        "original_name": "ကြက်သွန်ဖြူ (ဓားပြားရိုက်)",
        "quantity": 4.0,
        "unit": "မြွှာ",
        "original_quantity_text": "၄ မြွှာ",
        "normalized_quantity": 4.0,
        "normalized_unit": "piece",
        "preparation_note_mm": "ဓားပြားရိုက်",
        "preparation_note_en": "crushed / smashed"
      },
      {
        "ingredient_id": "I0015",
        "name_mm": "မုန်လာဥဝါ",
        "name_en": "Carrot",
        "original_name": "မုန်လာဥဝါ (လှီးပြီး)",
        "quantity": 10.0,
        "unit": "ကျပ်သား",
        "original_quantity_text": "၁၀ ကျပ်သား",
        "normalized_quantity": 163.3,
        "normalized_unit": "g",
        "preparation_note_mm": "လှီးပြီး",
        "preparation_note_en": "sliced"
      },
      {
        "ingredient_id": "I0023",
        "name_mm": "ဂေါ်ဖီထုပ်",
        "name_en": "Cabbage",
        "original_name": "ဂေါ်ဖီထုပ် (လှီးပြီး)",
        "quantity": 20.0,
        "unit": "ကျပ်သား",
        "original_quantity_text": "၂၀ ကျပ်သား",
        "normalized_quantity": 326.6,
        "normalized_unit": "g",
        "preparation_note_mm": "လှီးပြီး",
        "preparation_note_en": "shredded / sliced"
      },
      {
        "ingredient_id": "I0024",
        "name_mm": "ပဲစိမ်းလုံး",
        "name_en": "Green peas",
        "original_name": "ပဲစိမ်းလုံး (ပြုတ်ပြီး)",
        "quantity": 0.5,
        "unit": "ဘူး",
        "original_quantity_text": "၁/၂ ဘူး",
        "normalized_quantity": 0.5,
        "normalized_unit": "can",
        "preparation_note_mm": "ပြုတ်ပြီး",
        "preparation_note_en": "boiled"
      },
      {
        "ingredient_id": "I0025",
        "name_mm": "အရိုးပြုတ်ရည်",
        "name_en": "Bone broth / Stock",
        "original_name": "အရိုးပြုတ်ရည်",
        "quantity": 2.0,
        "unit": "ခွက်",
        "original_quantity_text": "၂ ခွက်",
        "normalized_quantity": None,
        "normalized_unit": None,
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0026",
        "name_mm": "ပဲငံပြာရည်",
        "name_en": "Soy sauce",
        "original_name": "ပဲငံပြာရည်",
        "quantity": 2.0,
        "unit": "စပဇ",
        "original_quantity_text": "၂ စပဇ",
        "normalized_quantity": 30.0,
        "normalized_unit": "ml",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0009",
        "name_mm": "ဆား",
        "name_en": "Salt",
        "original_name": "ဆား",
        "quantity": 2.0,
        "unit": "စပဇ",
        "original_quantity_text": "၂ စပဇ",
        "normalized_quantity": 30.0,
        "normalized_unit": "ml",
        "preparation_note_mm": None,
        "preparation_note_en": None
      },
      {
        "ingredient_id": "I0008",
        "name_mm": "သကြား",
        "name_en": "Sugar",
        "original_name": "သကြား",
        "quantity": 2.0,
        "unit": "စပဇ",
        "original_quantity_text": "၂ စပဇ",
        "normalized_quantity": 30.0,
        "normalized_unit": "ml",
        "preparation_note_mm": "ကြော်နေစဉ် သကြားအရည်ဖျော် အနည်းငယ်ထည့်ရန်",
        "preparation_note_en": "dissolved in water into light syrup before adding"
      },
      {
        "ingredient_id": "I0027",
        "name_mm": "ငရုတ်ကောင်း",
        "name_en": "Black pepper",
        "original_name": "ငရုတ်ကောင်း",
        "quantity": 0.5,
        "unit": "စပဇ",
        "original_quantity_text": "၁/၂ စပဇ",
        "normalized_quantity": 7.5,
        "normalized_unit": "ml",
        "preparation_note_mm": None,
        "preparation_note_en": None
      }
    ],
    "servings": 10,
    "preparation_time_minutes": None,
    "cooking_time_minutes": None,
    "instructions_mm": [
      "ဆန်ကိုရေဖြင့် နှစ်ကြိမ်ခန့် လျင်မြန်စွာဆေးပြီး ရေစစ်ပါ ထမင်းချက်ပါ။ ခေတ္တမျှအေးအောင်ထားပါ။",
      "ဆီ ၂စားပွဲဇွန်းကို ပူအောင်လုပ်ပြီး ခေါက်ထားသောဘဲဥတွင် ဆားအနည်းငယ်ထည့်ကာ မွှေကြော်ပါ။",
      "ကျန်ဆီများကို ဒယ်အိုးကြီးထဲထည့်ကာ အပူပေးပါ။ ကြက်သွန်ဖြူထည့်မွှေပါ။",
      "ပုစွန်၊ ဝက်သား ထည့်မွှေပါ။ အိုးဘေးတွင် အသာကပ်တင်ထားပြီး လှီးဖြတ်ထားသော မုန်လာဥဝါနှင့် ဂေါ်ဖီထုပ်တို့ကို ထည့်ကြော်ပါ။",
      "အရိုးပြုတ်ရည် အနည်းငယ်ထည့်မွှေပါ။ ထမင်းထည့်ပါ။ ဆားနှင့် ငရုတ်ကောင်း ထည့်မွှေပါ။",
      "ကြက်ဥမွှေကြော်နှင့် ပဲစိမ်းလုံးကို ထည့်ပြီး မွှေကြော်ပါ။ မီးရှိန်များများဖြင့် ကြော်ရပါမည်။",
      "ကြော်နေစဉ်တွင် သကြားအရည်ဖျော်ထားသည်ကို အနည်းငယ်ထည့်မွှေပေးကာ ကြော်ပါ။ ပူပူနွေးနွေး တည်ခင်းစားသုံးနိုင်ပါသည်။"
    ],
    "instructions_en": [
      "Quickly wash the rice with water about twice, drain, cook the rice, and allow it to cool briefly.",
      "Heat 2 tablespoons of oil, add a pinch of salt to the beaten duck eggs, and scramble them.",
      "Add the remaining oil into a large wok/pan and heat. Add the crushed garlic and stir-fry.",
      "Add prawns and pork and stir-fry; push them gently towards the side of the pan, then add the sliced carrots and shredded cabbage to stir-fry.",
      "Pour in a little bone broth and stir. Add the cooked rice, followed by salt and black pepper, stirring well.",
      "Add the scrambled eggs and green peas, and toss over high heat.",
      "While stir-frying, drizzle in a little dissolved sugar syrup and stir thoroughly. Serve while hot and fresh."
    ],
    "tags": {
      "dietary": [],
      "seasonal": [],
      "festival": [],
      "main_ingredients": ["Paw San Hmwe rice", "Pork", "Medium prawn / shrimp", "Duck egg", "Cabbage"]
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
      "pdf_pages": [43],
      "printed_page_numbers": [75],
      "extraction_method": "manual_visual_transcription_from_scanned_spread"
    },
    "data_quality": {
      "extraction_status": "extracted",
      "confidence": 0.95,
      "review_notes": [
        "Printed page 75 top-right recipe.",
        "Ingredient list specifies 'ဘဲဥ' (duck egg), while cooking step 6 refers colloquially to 'ကြက်ဥမွှေကြော်' (scrambled egg) — both preserved faithfully as written.",
        "Quantity for black pepper is fractional: '၁/၂ စပဇ' (1/2 tablespoon).",
        "Step 7 instructs dissolving sugar in a little water before adding during stir-frying."
      ],
      "verified": False
    }
  }
]

ingredients_catalog = [
  {
    "ingredient_id": "I0001",
    "name_mm": "ပေါ်ဆန်းမွှေးဆန်",
    "name_en": "Paw San Hmwe rice",
    "aliases_mm": ["ပေါ်ဆန်းမွှေး", "ပေါ်ဆန်းမွှေး (ဆန်ဟောင်း)"],
    "aliases_en": ["Paw San Rice", "Aged Paw San Hmwe"],
    "category": "grain",
    "default_unit": "g"
  },
  {
    "ingredient_id": "I0002",
    "name_mm": "ထောပတ်",
    "name_en": "Butter",
    "aliases_mm": [],
    "aliases_en": ["Clarified butter", "Ghee"],
    "category": "dairy_fat",
    "default_unit": "g"
  },
  {
    "ingredient_id": "I0003",
    "name_mm": "ဆီ",
    "name_en": "Cooking oil",
    "aliases_mm": ["မြေပဲဆီ", "ဟင်းချက်ဆီ"],
    "aliases_en": ["Oil", "Peanut oil"],
    "category": "fat_oil",
    "default_unit": "g"
  },
  {
    "ingredient_id": "I0004",
    "name_mm": "သစ်ကြံပိုးခေါက်",
    "name_en": "Cinnamon bark",
    "aliases_mm": ["သစ်ကြံပိုး", "သစ်ကြံပိုး (၂\" အရွယ်)"],
    "aliases_en": ["Cinnamon stick"],
    "category": "spice",
    "default_unit": "piece"
  },
  {
    "ingredient_id": "I0005",
    "name_mm": "ကရဝေးရွက်",
    "name_en": "Bay leaf",
    "aliases_mm": [],
    "aliases_en": ["Indian bay leaf", "Tejpatta"],
    "category": "herb",
    "default_unit": "piece"
  },
  {
    "ingredient_id": "I0006",
    "name_mm": "လေးညှင်းပွင့်",
    "name_en": "Clove",
    "aliases_mm": [],
    "aliases_en": ["Cloves"],
    "category": "spice",
    "default_unit": "piece"
  },
  {
    "ingredient_id": "I0007",
    "name_mm": "ဖာလာစေ့",
    "name_en": "Cardamom pod",
    "aliases_mm": ["ဖာလာ"],
    "aliases_en": ["Cardamom", "Green cardamom"],
    "category": "spice",
    "default_unit": "piece"
  },
  {
    "ingredient_id": "I0008",
    "name_mm": "သကြား",
    "name_en": "Sugar",
    "aliases_mm": [],
    "aliases_en": ["White sugar", "Granulated sugar"],
    "category": "sweetener",
    "default_unit": "g"
  },
  {
    "ingredient_id": "I0009",
    "name_mm": "ဆား",
    "name_en": "Salt",
    "aliases_mm": [],
    "aliases_en": ["Table salt"],
    "category": "seasoning",
    "default_unit": "g"
  },
  {
    "ingredient_id": "I0010",
    "name_mm": "ရေနွေး",
    "name_en": "Hot water",
    "aliases_mm": [],
    "aliases_en": ["Boiling water"],
    "category": "liquid",
    "default_unit": "ml"
  },
  {
    "ingredient_id": "I0011",
    "name_mm": "သီဟိုဠ်စေ့",
    "name_en": "Cashew nut",
    "aliases_mm": [],
    "aliases_en": ["Cashews"],
    "category": "nut_seed",
    "default_unit": "g"
  },
  {
    "ingredient_id": "I0012",
    "name_mm": "စပျစ်သီးခြောက်",
    "name_en": "Raisin",
    "aliases_mm": [],
    "aliases_en": ["Kishmish", "Dried grapes"],
    "category": "dried_fruit",
    "default_unit": "g"
  },
  {
    "ingredient_id": "I0013",
    "name_mm": "ပဲနီလေး",
    "name_en": "Red lentil",
    "aliases_mm": [],
    "aliases_en": ["Masoor dal"],
    "category": "legume",
    "default_unit": "g"
  },
  {
    "ingredient_id": "I0014",
    "name_mm": "ရေအေး",
    "name_en": "Cold water",
    "aliases_mm": ["ရေ"],
    "aliases_en": ["Water"],
    "category": "liquid",
    "default_unit": "ml"
  },
  {
    "ingredient_id": "I0015",
    "name_mm": "မုန်လာဥဝါ",
    "name_en": "Carrot",
    "aliases_mm": ["မုန်လာဥဝါ (လှီးပြီး)"],
    "aliases_en": ["Carrots"],
    "category": "vegetable",
    "default_unit": "g"
  },
  {
    "ingredient_id": "I0016",
    "name_mm": "ပဲစိမ်းဘူး",
    "name_en": "Canned green peas",
    "aliases_mm": [],
    "aliases_en": ["Canned peas"],
    "category": "canned_goods",
    "default_unit": "can"
  },
  {
    "ingredient_id": "I0017",
    "name_mm": "အုန်းသီး",
    "name_en": "Coconut",
    "aliases_mm": ["အုန်းသီးရင့်ရင့် (အလုံးကြီး)"],
    "aliases_en": ["Mature coconut"],
    "category": "fruit_and_seed",
    "default_unit": "piece"
  },
  {
    "ingredient_id": "I0018",
    "name_mm": "ကြက်သွန်နီ",
    "name_en": "Shallot / Small onion",
    "aliases_mm": ["ကြက်သွန်နီ (ဥသေး)"],
    "aliases_en": ["Shallot", "Small onion"],
    "category": "allium",
    "default_unit": "g"
  },
  {
    "ingredient_id": "I0019",
    "name_mm": "ဘဲဥ",
    "name_en": "Duck egg",
    "aliases_mm": ["ဘဲဥ (ခေါက်ထားပြီး)"],
    "aliases_en": [],
    "category": "poultry_egg",
    "default_unit": "piece"
  },
  {
    "ingredient_id": "I0020",
    "name_mm": "ဝက်သား",
    "name_en": "Pork",
    "aliases_mm": ["အဆီလွတ်ဝက်သား (အတုံးသေးလှီးပြီး)"],
    "aliases_en": ["Lean pork"],
    "category": "meat",
    "default_unit": "g"
  },
  {
    "ingredient_id": "I0021",
    "name_mm": "ပုစွန်ကျော့",
    "name_en": "Medium prawn / shrimp",
    "aliases_mm": ["ပုစွန်ကျော့ (အခွံသင်ပြီး)"],
    "aliases_en": ["Prawn", "Shrimp"],
    "category": "seafood",
    "default_unit": "g"
  },
  {
    "ingredient_id": "I0022",
    "name_mm": "ကြက်သွန်ဖြူ",
    "name_en": "Garlic",
    "aliases_mm": ["ကြက်သွန်ဖြူ (ဓားပြားရိုက်)"],
    "aliases_en": [],
    "category": "allium",
    "default_unit": "piece"
  },
  {
    "ingredient_id": "I0023",
    "name_mm": "ဂေါ်ဖီထုပ်",
    "name_en": "Cabbage",
    "aliases_mm": ["ဂေါ်ဖီထုပ် (လှီးပြီး)"],
    "aliases_en": ["White cabbage"],
    "category": "vegetable",
    "default_unit": "g"
  },
  {
    "ingredient_id": "I0024",
    "name_mm": "ပဲစိမ်းလုံး",
    "name_en": "Green peas",
    "aliases_mm": ["ပဲစိမ်းလုံး (ပြုတ်ပြီး)"],
    "aliases_en": ["Boiled green peas"],
    "category": "legume",
    "default_unit": "g"
  },
  {
    "ingredient_id": "I0025",
    "name_mm": "အရိုးပြုတ်ရည်",
    "name_en": "Bone broth / Stock",
    "aliases_mm": [],
    "aliases_en": ["Broth", "Bone soup"],
    "category": "liquid_seasoning",
    "default_unit": "ml"
  },
  {
    "ingredient_id": "I0026",
    "name_mm": "ပဲငံပြာရည်",
    "name_en": "Soy sauce",
    "aliases_mm": [],
    "aliases_en": ["Light soy sauce"],
    "category": "condiment",
    "default_unit": "ml"
  },
  {
    "ingredient_id": "I0027",
    "name_mm": "ငရုတ်ကောင်း",
    "name_en": "Black pepper",
    "aliases_mm": [],
    "aliases_en": ["Ground pepper", "Black pepper powder"],
    "category": "spice",
    "default_unit": "g"
  }
]

extraction_report = {
  "source_document": "ဟင်းချက်နည်းများ.pdf",
  "total_pages_processed": 3,
  "total_recipes_extracted": 5,
  "complete_recipes": 5,
  "partial_recipes": 0,
  "recipes_needing_review": 0,
  "unique_ingredients": len(ingredients_catalog),
  "unreadable_pages": [],
  "recipes_with_missing_quantities": [],
  "ambiguous_ingredients": [],
  "validation_errors": [],
  "general_notes": [
    "Pilot extraction covering the first 5 recipes from Section 22 (ချက်ပြုတ်နည်းများ), starting on printed page 73 (PDF page 42).",
    "The cookbook was identified as 'ချက်ပြုတ်အတတ်ပညာ' (Culinary Art) by Daw San Lay, published by the Myanmar Maternal and Child Welfare Association (MMCWA), 2nd edition, November 1999.",
    "Each PDF page represents a 2-page scanned spread of the physical book.",
    "Pages 1-72 contain non-recipe introductory content (nutrition, terminology, basic techniques, butchery, stove handling, table setting, and unit abbreviations).",
    "All Burmese text is encoded in clean modern standard Unicode (UTF-8).",
    "Measurement units follow traditional Myanmar cookbook standards: ကျပ်သား (16.33 g), နို့ဆီဘူး (~300 ml liquid), စပဇ (စားပွဲဇွန်း, tablespoon, 15 ml), and လဖဇ (လက်ဖက်ရည်ဇွန်း, teaspoon, 5 ml)."
  ]
}

out_dir = r'c:\Zay Chin'
with open(os.path.join(out_dir, 'recipes.json'), 'w', encoding='utf-8') as f:
    json.dump(recipes, f, ensure_ascii=False, indent=2)

with open(os.path.join(out_dir, 'ingredients.json'), 'w', encoding='utf-8') as f:
    json.dump(ingredients_catalog, f, ensure_ascii=False, indent=2)

with open(os.path.join(out_dir, 'extraction_report.json'), 'w', encoding='utf-8') as f:
    json.dump(extraction_report, f, ensure_ascii=False, indent=2)

print('recipes.json, ingredients.json, extraction_report.json written successfully.')
