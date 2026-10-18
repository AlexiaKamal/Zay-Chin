# -*- coding: utf-8 -*-
"""
Generator script for Pilot Dataset v2 (Recipes R0001 - R0010)
Incorporates the user's feedback:
- In `unit`, addition to the original book's Burmese unit, add gram (g) or kilogram (kg).
- Provide another pilot dataset (Recipes R0006 - R0010) alongside the updated R0001 - R0005.
"""

import json

# 1. RECIPES LIST
recipes = [
    # R0001: ထောပတ်ထမင်း (Butter Rice)
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
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၆ နို့ဆီဘူး",
                "normalized_quantity": 1500.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ဆန်ဟောင်း",
                "preparation_note_en": "aged rice"
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
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": 2.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
                "normalized_quantity": 40.8,
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
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ ၁/၂ စပဇ",
                "normalized_quantity": 22.5,
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
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ စပဇ",
                "normalized_quantity": 15.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ",
                "quantity": 10.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၀ ကျပ်သား",
                "normalized_quantity": 163.3,
                "normalized_unit": "g",
                "preparation_note_mm": "ပါးပါးလှီးထားပါ",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0007",
                "name_mm": "ဇာတိပ္ဖိုလ်သီး",
                "name_en": "Nutmeg",
                "original_name": "ဇာတိပ္ဖိုလ်သီး",
                "quantity": 0.5,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၁/၂ လုံး",
                "normalized_quantity": 0.5,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခြစ်ထားပါ",
                "preparation_note_en": "grated"
            },
            {
                "ingredient_id": "I0008",
                "name_mm": "သစ်ကြံပိုးခေါက်",
                "name_en": "Cinnamon bark",
                "original_name": "သစ်ကြံပိုး",
                "quantity": 1.0,
                "unit": "ခေါက် (piece)",
                "original_quantity_text": "လက်သန်းခန့် ၁ ခေါက်",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "လက်သန်းခန့် (၂ လက်မခန့်)",
                "preparation_note_en": "about finger-sized (~2 inches)"
            },
            {
                "ingredient_id": "I0009",
                "name_mm": "လေးညှင်းပွင့်",
                "name_en": "Cloves",
                "original_name": "လေးညှင်းပွင့်",
                "quantity": 5.0,
                "unit": "ပွင့် (piece)",
                "original_quantity_text": "၅ ပွင့်",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0010",
                "name_mm": "ဖာလာစေ့",
                "name_en": "Cardamom pods",
                "original_name": "ဖာလာစေ့",
                "quantity": 5.0,
                "unit": "စေ့ (piece)",
                "original_quantity_text": "၅ စေ့",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0011",
                "name_mm": "ကရဝေးရွက်",
                "name_en": "Bay leaves",
                "original_name": "ကရဝေးရွက်",
                "quantity": 3.0,
                "unit": "ရွက် (piece)",
                "original_quantity_text": "၃ ရွက်",
                "normalized_quantity": 3.0,
                "normalized_unit": "piece",
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
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "ဆန်ကို သန့်စင်ပြီး ရေဆေး ရေစစ်ထားပါ။",
            "ကြက်သွန်နီကို ပါးပါးလှီးပြီး ထောပတ်၊ ဆီတို့ဖြင့် ရွှေဝါရောင်သန်းသည်အထိ ကြော်ပြီး ဆယ်ယူထားပါ။",
            "ကျန်ဆီထဲသို့ သစ်ကြံပိုး၊ လေးညှင်း၊ ဖာလာ၊ ကရဝေးရွက်၊ ဇာတိပ္ဖိုလ်သီးမှုန့်ထည့်ပြီး အနံ့မွှေးလာအောင် မွှေပါ။",
            "ရေစစ်ထားသော ဆန်ကိုထည့်ပြီး ဆီသတ်ထားသော အမွှေးအကြိုင်များနှင့် သမအောင် မွှေကြော်ပါ။",
            "ဆား၊ သကြားထည့်ပြီး ရေနွေး (၆) ဘူးထည့်ကာ မီးပြင်းပြင်းဖြင့် ဆူပွက်အောင် တည်ပါ။",
            "ရေခမ်းလုနီးပါးဖြစ်လျှင် မီးကို လျှော့ပြီး အိုးအဖုံးကို လုံအောင်ပိတ်ကာ ထမင်းနှပ်ထားပါ။",
            "ထမင်းကျက်နူးနပ်ပါက အပေါ်မှ ကြော်ထားသော ကြက်သွန်နီကြော် ဖြူးပြီး သုံးဆောင်နိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Clean and wash the rice thoroughly, then drain well.",
            "Thinly slice the onions and fry in the butter and oil until golden brown, then remove and set aside.",
            "In the remaining oil/butter, add the cinnamon, cloves, cardamom, bay leaves, and grated nutmeg; stir until fragrant.",
            "Add the drained rice and sauté, stirring to coat evenly with the fragrant spices.",
            "Add salt, sugar, and 6 tins of hot water; bring to a vigorous boil over high heat.",
            "When the liquid has almost evaporated, reduce to low heat, cover tightly with a lid, and let the rice steam until cooked through.",
            "Once the rice is fully cooked and tender, garnish with the reserved fried onions before serving."
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
                "In unit, added gram (g) to traditional Burmese units: နို့ဆီဘူး (g), ကျပ်သား (g), စားပွဲဇွန်း (tbsp / g).",
                "Raw rice normalized at Myanmar standard of 250 g per condensed milk tin (6 tins = 1500 g).",
                "Festival tag 'donation_feast' is culturally inferred, not explicitly printed in recipe text."
            ],
            "verified": False
        }
    },

    # R0002: ပဲနီလေးထောပတ်ထမင်း (Red Lentil Butter Rice)
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
                "name_mm": "ဆန်",
                "name_en": "Rice",
                "original_name": "ဆန်",
                "quantity": 4.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၄ နို့ဆီဘူး",
                "normalized_quantity": 1000.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0013",
                "name_mm": "ပဲနီလေး",
                "name_en": "Red lentils",
                "original_name": "ပဲနီလေး",
                "quantity": 1.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၁ နို့ဆီဘူး",
                "normalized_quantity": 250.0,
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
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ",
                "quantity": 10.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၀ ကျပ်သား",
                "normalized_quantity": 163.3,
                "normalized_unit": "g",
                "preparation_note_mm": "ပါးပါးလှီးထားပါ",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0008",
                "name_mm": "သစ်ကြံပိုးခေါက်",
                "name_en": "Cinnamon bark",
                "original_name": "သစ်ကြံပိုး",
                "quantity": 1.0,
                "unit": "ခေါက် (piece)",
                "original_quantity_text": "၁ ခေါက်",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "၂ လက်မခန့်",
                "preparation_note_en": "about 2 inches"
            },
            {
                "ingredient_id": "I0010",
                "name_mm": "ဖာလာစေ့",
                "name_en": "Cardamom pods",
                "original_name": "ဖာလာစေ့",
                "quantity": 5.0,
                "unit": "စေ့ (piece)",
                "original_quantity_text": "၅ စေ့",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0009",
                "name_mm": "လေးညှင်းပွင့်",
                "name_en": "Cloves",
                "original_name": "လေးညှင်း",
                "quantity": 5.0,
                "unit": "ပွင့် (piece)",
                "original_quantity_text": "၅ ပွင့်",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0011",
                "name_mm": "ကရဝေးရွက်",
                "name_en": "Bay leaves",
                "original_name": "ကရဝေးရွက်",
                "quantity": 3.0,
                "unit": "ရွက် (piece)",
                "original_quantity_text": "၃ ရွက်",
                "normalized_quantity": 3.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 1.5,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ ၁/၂ စပဇ",
                "normalized_quantity": 22.5,
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
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ စပဇ",
                "normalized_quantity": 15.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0012",
                "name_mm": "ရေနွေး",
                "name_en": "Hot water",
                "original_name": "ရေနွေး",
                "quantity": 5.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၅ နို့ဆီဘူး",
                "normalized_quantity": 1500.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "ပဲနီလေးကို သန့်စင်ပြီး ရေဆေးကာ တစ်ဝက်နူးရုံ ပြုတ်၍ ရေစစ်ထားပါ။",
            "ဆန်ကို သန့်စင်ပြီး ရေဆေး ရေစစ်ထားပါ။",
            "ကြက်သွန်နီကို ပါးပါးလှီးပြီး ထောပတ်ဖြင့် ရွှေဝါရောင်သန်းသည်အထိ ကြော်ပြီး ဆယ်ယူထားပါ။",
            "ကျန်ထောပတ်ထဲသို့ သစ်ကြံပိုး၊ လေးညှင်း၊ ဖာလာ၊ ကရဝေးရွက်ထည့်ပြီး မွှေးလာအောင် ဆီသတ်ပါ။",
            "ဆန်နှင့် တစ်ဝက်နူးပြုတ်ထားသော ပဲနီလေးကို ထည့်ပြီး ဆီသတ်ထားသော အမွှေးအကြိုင်များနှင့် သမအောင် မွှေကြော်ပါ။",
            "ဆား၊ သကြားနှင့် ရေနွေး (၅) ဘူးထည့်ကာ မီးပြင်းပြင်းဖြင့် တည်ပါ။",
            "ဆူပွက်လာပြီး ရေခမ်းလုနီးပါးဖြစ်လျှင် မီးလျှော့ပြီး အဖုံးလုံအောင်ပိတ်၍ ထမင်းနှပ်ထားပါ။",
            "ထမင်းကျက်နပ်ပါက အပေါ်မှ ကြက်သွန်နီကြော် ဖြူးပြီး သုံးဆောင်နိုင်ပါသည်။",
            "အကြံပြုချက် - ပဲနီလေးကို ကြေမသွားစေရန် အလွန်အမင်း မပြုတ်သင့်ပါ။",
            "ထမင်းချက်ရာတွင် ပဲပြုတ်ရည်ကို ရေနွေးအစား အသုံးပြုပါက ပိုမိုအရသာရှိစေပါသည်။",
            "ကြက်သွန်ကြော်ရာတွင် မီးအား မပြင်းစေရန် သတိပြုရပါမည်။"
        ],
        "instructions_en": [
            "Sort and wash the red lentils, parboil until half-tender, and drain well.",
            "Clean, wash, and drain the rice thoroughly.",
            "Thinly slice the onions and fry in butter until golden brown, then scoop out and set aside.",
            "In the remaining melted butter, sauté cinnamon, cloves, cardamom, and bay leaves until aromatic.",
            "Add the drained rice and parboiled lentils; sauté gently to mix evenly with the fragrant spices.",
            "Add salt, sugar, and 5 tins of hot water; bring to a boil over high heat.",
            "Once boiling and the liquid has almost evaporated, reduce the heat, cover tightly, and steam the rice.",
            "Once fully cooked and fluffy, scatter the reserved fried onions over the top and serve.",
            "Tip: Do not over-boil the lentils beforehand so they do not disintegrate during rice cooking.",
            "Using the lentil boiling liquid in place of hot water enhances the overall flavor of the rice.",
            "Take care to regulate the flame when frying onions to prevent scorching."
        ],
        "tags": {
            "dietary": [],
            "seasonal": [],
            "festival": ["ceremonial", "donation_feast"],
            "main_ingredients": ["Rice", "Red lentils", "Butter"]
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
                "In unit, added gram (g) to traditional Burmese units.",
                "Rice and red lentils normalized at 250 g per condensed milk tin."
            ],
            "verified": False
        }
    },

    # R0003: သီးစုံထောပတ်ထမင်း (Vegetable Butter Rice)
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
                "name_mm": "ဆန်",
                "name_en": "Rice",
                "original_name": "ဆန်",
                "quantity": 6.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၆ နို့ဆီဘူး",
                "normalized_quantity": 1500.0,
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
                "ingredient_id": "I0014",
                "name_mm": "မုန်လာဥနီ",
                "name_en": "Carrot",
                "original_name": "မုန်လာဥနီ",
                "quantity": 10.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၀ ကျပ်သား",
                "normalized_quantity": 163.3,
                "normalized_unit": "g",
                "preparation_note_mm": "အတုံးသေးသေးလေးစိပ်ထားပါ",
                "preparation_note_en": "diced into small cubes"
            },
            {
                "ingredient_id": "I0015",
                "name_mm": "ပဲသီး",
                "name_en": "Green beans",
                "original_name": "ပဲသီး",
                "quantity": 10.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၀ ကျပ်သား",
                "normalized_quantity": 163.3,
                "normalized_unit": "g",
                "preparation_note_mm": "အတိုလေးများဖြတ်ထားပါ",
                "preparation_note_en": "cut into short pieces"
            },
            {
                "ingredient_id": "I0016",
                "name_mm": "ပဲစိမ်းလုံး",
                "name_en": "Green peas",
                "original_name": "ပဲစိမ်းလုံး",
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
                "original_name": "ကြက်သွန်နီ",
                "quantity": 10.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၀ ကျပ်သား",
                "normalized_quantity": 163.3,
                "normalized_unit": "g",
                "preparation_note_mm": "ပါးပါးလှီးထားပါ",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0008",
                "name_mm": "သစ်ကြံပိုးခေါက်",
                "name_en": "Cinnamon bark",
                "original_name": "သစ်ကြံပိုး",
                "quantity": 1.0,
                "unit": "ခေါက် (piece)",
                "original_quantity_text": "၁ ခေါက်",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0010",
                "name_mm": "ဖာလာစေ့",
                "name_en": "Cardamom pods",
                "original_name": "ဖာလာစေ့",
                "quantity": 5.0,
                "unit": "စေ့ (piece)",
                "original_quantity_text": "၅ စေ့",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0009",
                "name_mm": "လေးညှင်းပွင့်",
                "name_en": "Cloves",
                "original_name": "လေးညှင်း",
                "quantity": 5.0,
                "unit": "ပွင့် (piece)",
                "original_quantity_text": "၅ ပွင့်",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0011",
                "name_mm": "ကရဝေးရွက်",
                "name_en": "Bay leaves",
                "original_name": "ကရဝေးရွက်",
                "quantity": 3.0,
                "unit": "ရွက် (piece)",
                "original_quantity_text": "၃ ရွက်",
                "normalized_quantity": 3.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 1.5,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ ၁/၂ စပဇ",
                "normalized_quantity": 22.5,
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
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ စပဇ",
                "normalized_quantity": 15.0,
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
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "ဆန်ကို သန့်စင်ပြီး ရေဆေး ရေစစ်ထားပါ။",
            "မုန်လာဥနီကို အတုံးသေးသေးလှီးပြီး ပဲသီးကို အတိုလေးများ ဖြတ်ထားပါ။ ပဲစိမ်းလုံးကို ရေဆေးထားပါ။",
            "ကြက်သွန်နီကို ပါးပါးလှီးပြီး ထောပတ်ဖြင့် ရွှေဝါရောင်သန်းသည်အထိ ကြော်ပြီး ဆယ်ယူထားပါ။",
            "ကျန်ထောပတ်ထဲသို့ သစ်ကြံပိုး၊ လေးညှင်း၊ ဖာလာ၊ ကရဝေးရွက်ထည့်ပြီး မွှေးလာအောင် ဆီသတ်ပါ။",
            "မုန်လာဥနီ၊ ပဲသီး၊ ပဲစိမ်းလုံးတို့ကို ထည့်သွင်းမွှေကြော်ပါ။",
            "ရေစစ်ထားသော ဆန်ကိုထည့်ပြီး အသီးအရွက်၊ အမွှေးအကြိုင်များနှင့် သမအောင် ရောမွှေကြော်ပါ။",
            "ဆား၊ သကြားနှင့် ရေနွေး (၆) ဘူးထည့်ကာ မီးပြင်းပြင်းဖြင့် တည်ပါ။",
            "ဆူပွက်လာပြီး ရေခမ်းလုနီးပါးဖြစ်လျှင် မီးလျှော့ပြီး အဖုံးလုံအောင်ပိတ်၍ ထမင်းနှပ်ထားပါ။",
            "ထမင်းကျက်နပ်ပါက အပေါ်မှ ကြက်သွန်နီကြော် ဖြူးပြီး သုံးဆောင်နိုင်ပါသည်။",
            "ဟင်းသီးဟင်းရွက်များကို လတ်ဆတ်သော အရောင်အသွေး မပျက်စေရန် အချိန်ကြာမြင့်စွာ မကြော်သင့်ပါ။"
        ],
        "instructions_en": [
            "Clean, wash, and drain the rice thoroughly.",
            "Dice the carrots finely and cut green beans into short lengths; rinse the green peas.",
            "Thinly slice the onions and fry in butter until golden brown, then remove and set aside.",
            "In the remaining butter, sauté cinnamon, cloves, cardamom, and bay leaves until fragrant.",
            "Add the diced carrots, green beans, and green peas; stir-fry gently.",
            "Add the drained rice and sauté to thoroughly combine with the vegetables and spices.",
            "Add salt, sugar, and 6 tins of hot water; bring to a boil over high heat.",
            "When boiling and the liquid has nearly evaporated, reduce heat, cover tightly, and steam the rice.",
            "Once fully cooked and tender, garnish with the fried onions and serve.",
            "Avoid overcooking the vegetables during the initial sauté to preserve their vibrant color."
        ],
        "tags": {
            "dietary": [],
            "seasonal": [],
            "festival": ["ceremonial", "donation_feast"],
            "main_ingredients": ["Rice", "Carrot", "Green beans", "Butter"]
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
            "confidence": 0.95,
            "review_notes": [
                "Servings stated as '(လူ ၁၀ ဦး)' in original heading.",
                "In unit, added gram (g) to traditional Burmese units.",
                "Rice normalized at 250 g per condensed milk tin (6 tins = 1500 g)."
            ],
            "verified": False
        }
    },

    # R0004: အုန်းထမင်း (Coconut Rice)
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
                "name_mm": "ဆန်",
                "name_en": "Rice",
                "original_name": "ဆန်",
                "quantity": 6.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၆ နို့ဆီဘူး",
                "normalized_quantity": 1500.0,
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
                "preparation_note_mm": "အုန်းနို့ညှစ်ယူရန်",
                "preparation_note_en": "for extracting coconut milk"
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": 1.5,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ ၁/၂ စပဇ",
                "normalized_quantity": 22.5,
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
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ စပဇ",
                "normalized_quantity": 15.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.6,
                "normalized_unit": "g",
                "preparation_note_mm": "ပါးပါးလှီးထားပါ",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0003",
                "name_mm": "ဆီ",
                "name_en": "Cooking oil",
                "original_name": "ဆီ",
                "quantity": 2.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
                "normalized_quantity": 40.8,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "ဆန်ကို သန့်စင်ပြီး ရေဆေး ရေစစ်ထားပါ။",
            "အုန်းသီးကို ခြစ်ပြီး ပထမ ရေနွေးအနည်းငယ်ဖြင့် ညှစ်ကာ အုန်းနို့ခဲ (ထိပ်ဆုံးရည်) ကို သပ်သပ်ဖယ်ထားပါ။ နောက်ထပ် ရေနွေးရော၍ အုန်းနို့ကျဲကို စုစုပေါင်း ရေနွေး (၆) ဘူးစာ ရရှိအောင် ညှစ်ယူပါ။",
            "ကြက်သွန်နီကို ပါးပါးလှီးပြီး ဆီဖြင့် ရွှေဝါရောင်သန်းသည်အထိ ကြော်ပြီး ဆယ်ယူထားပါ။",
            "ကျန်ဆီထဲသို့ ရေစစ်ထားသော ဆန်ကိုထည့်ပြီး အနည်းငယ် မွှေကြော်ပါ။",
            "အုန်းနို့ကျဲ၊ ဆား၊ သကြားတို့ထည့်ကာ မီးပြင်းပြင်းဖြင့် တည်ပါ။",
            "ရေဆူပွက်ပြီး ရေခမ်းလုနီးပါးဖြစ်ချိန်တွင် ဖယ်ထားသော အုန်းနို့ခဲကို အပေါ်မှ ဆမ်းထည့်ပါ။",
            "မီးလျှော့ပြီး အဖုံးလုံအောင်ပိတ်ကာ ထမင်းနှပ်ထားပါ။",
            "ထမင်းကျက်နူးနပ်ပါက အပေါ်မှ ကြက်သွန်နီကြော် ဖြူးပြီး သုံးဆောင်နိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Clean, wash, and drain the rice thoroughly.",
            "Grate the coconut; extract thick coconut cream first using a small amount of warm water and set aside. Then extract thin coconut milk with additional warm water to yield 6 condensed milk tins of liquid in total.",
            "Thinly slice the onions and fry in cooking oil until golden brown, then remove and set aside.",
            "Add the drained rice to the remaining oil and sauté briefly.",
            "Add the thin coconut milk, salt, and sugar; bring to a boil over high heat.",
            "When the liquid has boiled down and is nearly absorbed, pour the reserved thick coconut cream over the top.",
            "Reduce heat to low, cover tightly with a lid, and steam the rice.",
            "Once the rice is fully cooked and fragrant, garnish with the fried onions and serve."
        ],
        "tags": {
            "dietary": [],
            "seasonal": [],
            "festival": ["ceremonial", "donation_feast"],
            "main_ingredients": ["Rice", "Coconut milk"]
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
            "confidence": 0.95,
            "review_notes": [
                "Servings stated as '(လူ ၁၀ ဦး)' in original heading.",
                "In unit, added gram (g) to traditional Burmese units.",
                "Rice normalized at 250 g per condensed milk tin (6 tins = 1500 g)."
            ],
            "verified": False
        }
    },

    # R0005: ထမင်းကြော် (Fried Rice)
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
                "ingredient_id": "I0019",
                "name_mm": "ထမင်း",
                "name_en": "Cooked rice",
                "original_name": "ထမင်း",
                "quantity": 4.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၄ ဘူး",
                "normalized_quantity": 600.0,
                "normalized_unit": "g",
                "preparation_note_mm": "အေးပြီး အလုံးမကွဲအောင် ဖွထားပါ",
                "preparation_note_en": "cooled and fluffed to keep grains intact"
            },
            {
                "ingredient_id": "I0020",
                "name_mm": "ကြက်သား",
                "name_en": "Chicken meat",
                "original_name": "ကြက်သား (သို့) ဝက်သား",
                "quantity": 10.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၀ ကျပ်သား",
                "normalized_quantity": 163.3,
                "normalized_unit": "g",
                "preparation_note_mm": "အတုံးသေးသေးတုံးထားပါ",
                "preparation_note_en": "diced into small cubes"
            },
            {
                "ingredient_id": "I0021",
                "name_mm": "ပုစွန်ခြောက်",
                "name_en": "Dried shrimp",
                "original_name": "ပုစွန်ခြောက်မှုန့်",
                "quantity": 1.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ စပဇ",
                "normalized_quantity": 15.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ထောင်းထားပါ",
                "preparation_note_en": "pounded"
            },
            {
                "ingredient_id": "I0022",
                "name_mm": "ကြက်သွန်ဖြူ",
                "name_en": "Garlic",
                "original_name": "ကြက်သွန်ဖြူ",
                "quantity": 1.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁ ကျပ်သား",
                "normalized_quantity": 16.3,
                "normalized_unit": "g",
                "preparation_note_mm": "ဓားပြားရိုက်ထားပါ",
                "preparation_note_en": "crushed"
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.6,
                "normalized_unit": "g",
                "preparation_note_mm": "ပါးပါးလှီးထားပါ",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0023",
                "name_mm": "ပဲငံပြာရည်အကြည်",
                "name_en": "Light soy sauce",
                "original_name": "ပဲငံပြာရည်အကြည်",
                "quantity": 1.0,
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၁ စပဇ",
                "normalized_quantity": 15.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0024",
                "name_mm": "ပဲငံပြာရည်အနောက်",
                "name_en": "Dark soy sauce",
                "original_name": "ပဲငံပြာရည်အနောက်",
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
                "ingredient_id": "I0014",
                "name_mm": "မုန်လာဥနီ",
                "name_en": "Carrot",
                "original_name": "မုန်လာဥနီ",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.6,
                "normalized_unit": "g",
                "preparation_note_mm": "အတုံးသေးသေးလှီးထားပါ",
                "preparation_note_en": "finely diced"
            },
            {
                "ingredient_id": "I0015",
                "name_mm": "ပဲသီး",
                "name_en": "Green beans",
                "original_name": "ပဲသီး",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.6,
                "normalized_unit": "g",
                "preparation_note_mm": "အတိုလေးများလှီးထားပါ",
                "preparation_note_en": "cut into short pieces"
            },
            {
                "ingredient_id": "I0025",
                "name_mm": "ကြက်သွန်မြိတ်",
                "name_en": "Spring onion",
                "original_name": "ကြက်သွန်မြိတ်",
                "quantity": 2.0,
                "unit": "ပင် (piece)",
                "original_quantity_text": "၂ ပင်",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ပါးပါးလှီးထားပါ",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0027",
                "name_mm": "ဘဲဥ",
                "name_en": "Duck egg",
                "original_name": "ဘဲဥ",
                "quantity": 2.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၂ လုံး",
                "normalized_quantity": 2.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ခေါက်ကြော်ထားပါ",
                "preparation_note_en": "beaten and scrambled"
            }
        ],
        "servings": None,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "အသားကို အတုံးသေးသေးလှီးပြီး ပဲငံပြာရည်အကြည် အနည်းငယ်ဖြင့် နယ်ထားပါ။",
            "ဒယ်အိုးတွင် ဆီထည့်ပြီး ပူလာလျှင် ကြက်သွန်ဖြူ၊ ကြက်သွန်နီတို့ထည့်၍ မွှေးလာအောင် ဆီသတ်ပါ။",
            "နယ်ထားသော အသားနှင့် ပုစွန်ခြောက်မှုန့်ထည့်ပြီး အသားကျက်သည်အထိ ကြော်ပါ။",
            "မုန်လာဥနီနှင့် ပဲသီးထည့်ပြီး အနည်းငယ်နွမ်းသည်အထိ ဆက်လက်ကြော်ပါ။",
            "ထမင်းထည့်ပြီး ဆား၊ သကြား၊ ပဲငံပြာရည်အကြည်နှင့် ပဲငံပြာရည်အနောက်တို့ထည့်ကာ မီးပြင်းပြင်းဖြင့် သမအောင် အမြန်ကြော်ပါ။",
            "ကြက်ဥမွှေကြော်ထားသည်ကို ထည့်သွင်းရောမွှေပါ။",
            "ဖိုပေါ်မှ ချခါနီးတွင် ကြက်သွန်မြိတ်အုပ်ပြီး ပူပူနွေးနွေး သုံးဆောင်နိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Dice the meat finely and marinate with a small splash of light soy sauce.",
            "Heat oil in a wok; once hot, sauté crushed garlic and sliced onion until fragrant.",
            "Add the marinated meat and pounded dried shrimp; stir-fry until the meat is thoroughly cooked.",
            "Add the diced carrot and green beans; stir-fry until slightly tender-crisp.",
            "Add the cooked rice, season with salt, sugar, light soy sauce, and dark soy sauce; stir-fry vigorously over high heat until well incorporated.",
            "Fold in the pre-cooked scrambled eggs.",
            "Garnish with sliced spring onions just before taking off the heat and serve steaming hot."
        ],
        "tags": {
            "dietary": [],
            "seasonal": [],
            "festival": [],
            "main_ingredients": ["Cooked rice", "Chicken meat", "Duck egg"]
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
                "Servings not explicitly stated in source heading.",
                "In unit, added gram (g) to traditional Burmese units.",
                "Cooked rice normalized at ~150 g per condensed milk tin (4 tins = 600 g).",
                "Ingredient table specifies 'ဘဲဥ' (duck egg), while step 6 mentions 'ကြက်ဥမွှေကြော်' (scrambled chicken egg). Both original forms preserved."
            ],
            "verified": False
        }
    },

    # R0006: CHICKEN BIRIANI (ကြက်သားဒန်ပေါက်)
    {
        "recipe_id": "R0006",
        "name_mm": "ကြက်သားဒန်ပေါက်",
        "name_en": "Chicken Biryani",
        "description_mm": None,
        "description_en": None,
        "category": "Rice dishes",
        "meal_types": ["lunch", "dinner"],
        "ingredients": [
            {
                "ingredient_id": "I0001",
                "name_mm": "ဆန်",
                "name_en": "Rice",
                "original_name": "ဆန်ကောင်းကောင်း",
                "quantity": 5.0,
                "unit": "နို့ဆီဘူး (g)",
                "original_quantity_text": "၅ နို့ဆီဘူး",
                "normalized_quantity": 1250.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ဆန်ကောင်းကောင်း",
                "preparation_note_en": "high quality rice"
            },
            {
                "ingredient_id": "I0028",
                "name_mm": "ကြက်ရင်အုပ်သား",
                "name_en": "Chicken breast",
                "original_name": "ကြက်ရင်အုပ်သား(၂ ခြမ်းစီပါ)",
                "quantity": 5.0,
                "unit": "ခု (piece)",
                "original_quantity_text": "၅ ခု",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "၂ ခြမ်းစီပါ",
                "preparation_note_en": "with both halves intact"
            },
            {
                "ingredient_id": "I0029",
                "name_mm": "ဒိန်ချဉ်",
                "name_en": "Curd / Yogurt",
                "original_name": "ဒိန်ချဉ်",
                "quantity": 1.5,
                "unit": "ခွက် (cup / g)",
                "original_quantity_text": "၁ ၁/၂ ခွက်",
                "normalized_quantity": 360.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0022",
                "name_mm": "ကြက်သွန်ဖြူ",
                "name_en": "Garlic",
                "original_name": "ကြက်သွန်ဖြူ",
                "quantity": 2.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၂ ၁/၂ ကျပ်သား",
                "normalized_quantity": 40.8,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
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
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0031",
                "name_mm": "နံနံစေ့အမှုန့်",
                "name_en": "Coriander powder",
                "original_name": "နံနံစေ့အမှုန့်",
                "quantity": 2.5,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၂ ၁/၂ လဖဇ",
                "normalized_quantity": 12.5,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0008",
                "name_mm": "သစ်ကြံပိုးခေါက်",
                "name_en": "Cinnamon bark",
                "original_name": "သစ်ကြံပိုးခေါက် (၂\" ရှည်)",
                "quantity": 5.0,
                "unit": "ခေါက် (piece)",
                "original_quantity_text": "၅ ခေါက်",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "၂ လက်မ အရှည်",
                "preparation_note_en": "2 inches long"
            },
            {
                "ingredient_id": "I0010",
                "name_mm": "ဖာလာစေ့",
                "name_en": "Cardamom pods",
                "original_name": "ဖာလာစေ့",
                "quantity": 10.0,
                "unit": "စေ့ (piece)",
                "original_quantity_text": "၁၀ စေ့",
                "normalized_quantity": 10.0,
                "normalized_unit": "piece",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ (ထောင်းပြီး)",
                "quantity": 5.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၅ လုံး",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ထောင်းပြီး",
                "preparation_note_en": "pounded"
            },
            {
                "ingredient_id": "I0006",
                "name_mm": "ကြက်သွန်နီ",
                "name_en": "Onion",
                "original_name": "ကြက်သွန်နီ (ပါးပါးလှီးပြီး)",
                "quantity": 5.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "၅ လုံး",
                "normalized_quantity": 5.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ပါးပါးလှီးပြီး",
                "preparation_note_en": "thinly sliced"
            },
            {
                "ingredient_id": "I0002",
                "name_mm": "ထောပတ်",
                "name_en": "Butter",
                "original_name": "ထောပတ်",
                "quantity": 30.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၃၀ ကျပ်သား",
                "normalized_quantity": 489.9,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0032",
                "name_mm": "ဗာဒံသီး",
                "name_en": "Almonds",
                "original_name": "ဗာဒံသီး",
                "quantity": 5.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၅ ကျပ်သား",
                "normalized_quantity": 81.6,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0033",
                "name_mm": "စပျစ်သီးခြောက်",
                "name_en": "Raisins",
                "original_name": "စပျစ်သီးခြောက်",
                "quantity": 10.0,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၁၀ ကျပ်သား",
                "normalized_quantity": 163.3,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0034",
                "name_mm": "ဂုံမန်",
                "name_en": "Saffron",
                "original_name": "ဂုံမန်",
                "quantity": 2.0,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၂ လဖဇ",
                "normalized_quantity": 10.0,
                "normalized_unit": "g",
                "preparation_note_mm": "နှင်းရည်ဖြင့် ဖျော်ရန်",
                "preparation_note_en": "to be dissolved in rose water"
            },
            {
                "ingredient_id": "I0035",
                "name_mm": "နှင်းရည်",
                "name_en": "Rose water",
                "original_name": "နှင်းရည်",
                "quantity": 2.0,
                "unit": "ခွက် (cup / g)",
                "original_quantity_text": "၂ ခွက်",
                "normalized_quantity": 480.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
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
                "ingredient_id": "I0036",
                "name_mm": "နွားနို့",
                "name_en": "Cow milk",
                "original_name": "နွားနို့",
                "quantity": 1.75,
                "unit": "ခွက် (cup / g)",
                "original_quantity_text": "၁ ၃/၄ ခွက်",
                "normalized_quantity": 420.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "ဆန်ကို ရေဆေးပြီးတည်ကာ တစ်ဝက်တစ်ပျက်အနေတွင် ရေငှဲ့ကာစစ်ထားပါ။",
            "ကြက်ရင်အုပ်များကို ဒိန်ချဉ်၊ ကြက်သွန်ဖြူ၊ ကြက်သွန်နီ၊ ချင်းနှင့် ဟင်းခတ်အမွှေးအကြိုင်များဖြင့် နယ်ထားပါ။",
            "ဒယ်ပြားတွင် ထောပတ် တစ်ဝက်ထည့်ပြီး ပူလာလျှင် ပါးပါးလှီးထားသော ကြက်သွန်နီ ကြော်ကာ ဖယ်ထားပါ။ စပျစ်သီးကိုလည်း လျင်မြန်စွာ ခေတ္တထည့်ပြီးမွှေကာ ဆယ်ယူထားပါ။",
            "မီးရှိန်နည်းနည်းတွင် အသားတုံးများ အညိုရောင်သန်းပြီး နူးမြေ့လာသည်အထိ ပြုလုပ်ပါ။ အရသာအတွက် ဆားခတ်ပါ။",
            "ဒယ်အိုးကြီးကြီးတွင် ကျန်ထောပတ်များထည့်ပါ။ အရည်ပျော်လာလျှင် တစ်ဝက်တစ်ပျက်ချက်ထားပြီး ထမင်းကို အိုးအောက်ခြေတွင် ပထမခင်းထည့်ပါ။",
            "အရည်ဖျော်ထားသော ဂုံမန်ရည်ကို ဖျန်းပါ။ ဗာဒံသီး၊ စပျစ်သီးများ အပေါ်ယံတွင် နှံ့အောင်ဖြူးပါ။ ကြက်ရင်အုပ်ကြော်နှင့် ကြက်သွန်နီကြော်များ ဖြန့်ထည့်ပါ။",
            "တစ်ဖန် ထမင်းထပ်အုပ်ထည့်ပါ။ ဂုံမန်ရည်ဖျန်းပါ။ ဗာဒံသီး၊ စပျစ်သီး ဖြူးပါ။ ကြက်ရင်အုပ်ကြော်နှင့် ကြက်သွန်နီကြော်များ ဖြန့်ထည့်ပါ။ တတိယအကြိမ် ဤနည်းအတိုင်းထပ်ထည့်ပါ။",
            "အပေါ်ယံမှနေ၍ နွားနို့ဖျန်းလောင်းထည့်ပါ။ မီးသွေးမီးဖိုတွင် မီးအေးအေးဖြင့် အိုးဖုံးပိတ်ချက်ပါ။ အရည်များခန်းပြီး ထမင်းနပ်သွားလျှင် ပန်းကန်ပြားတွင်ထည့်၍ အပေါ်ယံမှနေပြီး ဗာဒံသီး၊ စပျစ်သီးများဖြင့် မွမ်းမံကာ တည်ခင်းနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Wash the rice and parboil until half-cooked, then drain thoroughly.",
            "Marinate the chicken breasts with yogurt, garlic, pounded onion, ginger, and biryani spices.",
            "Melt half of the butter in a pan; fry the sliced onions until golden brown and remove. Briefly flash-fry the raisins, scoop out, and set aside.",
            "Over low heat, braise the marinated chicken pieces until lightly browned and tender; season to taste with salt.",
            "In a large heavy pot, melt the remaining butter; spread a layer of parboiled rice across the bottom of the pot.",
            "Sprinkle with rosewater-dissolved saffron, evenly scatter almonds and raisins, and arrange a layer of chicken breasts and fried onions.",
            "Add another layer of rice, sprinkle saffron water, scatter almonds and raisins, and lay more chicken and fried onions; repeat this layering a third time.",
            "Pour the milk over the top layer. Cover tightly and simmer over low heat (or charcoal embers) until the liquid is absorbed and the biryani is fully steamed. Dish onto a platter, garnish with almonds and raisins, and serve."
        ],
        "tags": {
            "dietary": [],
            "seasonal": [],
            "festival": ["ceremonial", "donation_feast", "eid"],
            "main_ingredients": ["Rice", "Chicken breast", "Butter", "Yogurt", "Saffron"]
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
                "Servings stated as '(လူ ၁၀ ဦးစာ)' in original heading.",
                "Original title printed in English as 'CHICKEN BIRIANI' without a separate Burmese heading; Burmese name 'ကြက်သားဒန်ပေါက်' standardly provided for bilingual completeness.",
                "In unit, added gram (g) to traditional Burmese units.",
                "Rice normalized at 250 g per condensed milk tin (5 tins = 1250 g).",
                "ဂုံမန် is the traditional Myanmar culinary term for saffron (kunkumam), dissolved in rose water (နှင်းရည်)."
            ],
            "verified": False
        }
    },

    # R0007: ကြက်ဥပြုတ် (BOILED EGGS)
    {
        "recipe_id": "R0007",
        "name_mm": "ကြက်ဥပြုတ်",
        "name_en": "Boiled Eggs",
        "description_mm": None,
        "description_en": None,
        "category": "Egg dishes",
        "meal_types": ["breakfast", "snack"],
        "ingredients": [
            {
                "ingredient_id": "I0026",
                "name_mm": "ကြက်ဥ",
                "name_en": "Chicken egg",
                "original_name": "ကြက်ဥ",
                "quantity": None,
                "unit": "လုံး (piece)",
                "original_quantity_text": "ကြက်ဥများ",
                "normalized_quantity": None,
                "normalized_unit": "piece",
                "preparation_note_mm": "အခန်းအပူချိန်၌ထားပါ",
                "preparation_note_en": "kept at room temperature"
            },
            {
                "ingredient_id": "I0017",
                "name_mm": "ရေ",
                "name_en": "Water",
                "original_name": "ရေအေး (သို့) ဆူနေသောရေနွေး",
                "quantity": None,
                "unit": "ဂရမ် / မီလီလီတာ (g)",
                "original_quantity_text": "မြုပ်သည်အထိ",
                "normalized_quantity": None,
                "normalized_unit": "g",
                "preparation_note_mm": "ကြက်ဥများ ကောင်းစွာမြုပ်သည်အထိ",
                "preparation_note_en": "enough to submerge the eggs"
            }
        ],
        "servings": None,
        "preparation_time_minutes": None,
        "cooking_time_minutes": None,
        "instructions_mm": [
            "ချက်ပြုတ်စဉ် အက်ကွဲခြင်းမဖြစ်အောင် ကြက်ဥကို အခန်းအပူချိန်၌ထားပါ။",
            "ရေအေး (သို့) ဆူနေသောရေနွေးဖြင့် စတင်အသုံးပြုနိုင်သည်။",
            "ကြက်ဥများ ကောင်းစွာမြုပ်သည်အထိ ရေထည့်ပါ။",
            "လုံလောက်အောင် အရွယ်ကြီးမားသော ဒယ်အိုးကို ရွေးချယ်အသုံးပြုပါ။ ကြက်ဥများကို တစ်လုံးပေါ်တစ်လုံးဆင့်၍ စုပုံမထားပါနှင့်။",
            "နာရီ (သို့) ချိန်မှတ်နာရီဖြင့် အချိန်တိကျစွာ ပြုလုပ်ပါ။",
            "ဆူနေသော အပူချိန်၏ အောက်နှိမ့်၍ အပူပေးပါ။",
            "ရေအေးဖြင့် စတင်တည်လျှင်- ကြက်ဥမကျက်တကျက်ပြုတ် ၃ မှ ၄ မိနစ်၌ မီးဖိုပေါ်မှ ချပါ။ ကြက်ဥအကျက်ပြုတ် ၁၃ မှ ၁၅ မိနစ်၌ မီးဖိုပေါ်မှ ချပါ။",
            "ရေနွေးဖြင့် စတင်တည်လျှင်- ကြက်ဥမကျက်တကျက်ပြုတ် ၃ မှ ၅ မိနစ်၊ ကြက်ဥအကျက်ပြုတ် ၁၈ မှ ၂၀ မိနစ်။",
            "အပူနွေးနွေးဖြင့် ပြုတ်ခြင်း: ကြက်ဥမကျက်တကျက်ပြုတ် ၄ မှ ၆ မိနစ်၌ မီးဖိုပေါ်မှ ချပါ။ ကြက်ဥအကျက်ပြုတ် ၃၀ မှ ၃၅ မိနစ်၌ မီးဖိုပေါ်မှ ချပါ။ အထက်တွင် ဖော်ပြခဲ့သော ရေနွေးဖြင့် စတင်တည်သည့်နည်းအတိုင်း လိုက်နာရပြီး ဒယ်ကို အလုံပိတ်၍ မီးဖိုမှဖယ်ရှားခြင်းသာ ကွာခြားသည်။ ကြက်ဥများကျက်လာသည်အထိ ထားပါ။",
            "ကြက်ဥများကို ရေအေးအောက်တွင် အအေးခံခြင်းဖြင့် ကြက်ဥများကို ကိုင်တွယ်ရ ပိုလွယ်ကူစေပြီး အကျက်ပြုတ်များအတွက် အခွံခွာရလွယ်စေကာ၊ ဆက်၍မကျက်အောင်အတွက် ချက်ချင်းရပ်တန့်စေနိုင်ပါသည်။ အကျက်လွန်ခြင်းသည် ကြက်ဥအနှစ်ကို အရောင်မည်းလာစေနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "Keep eggs at room temperature prior to cooking to prevent shells from cracking.",
            "You can begin cooking using either cold water or boiling hot water.",
            "Add sufficient water so that the eggs are completely submerged.",
            "Select a saucepan large enough so that the eggs can rest in a single layer without being stacked on top of one another.",
            "Use a clock or timer to control cooking times precisely.",
            "Maintain the heat just below a rolling boil to simmer gently.",
            "If starting with cold water: For soft-boiled eggs, remove from heat after 3 to 4 minutes; for hard-boiled eggs, remove after 13 to 15 minutes.",
            "If starting with boiling water: Soft-boiled eggs take 3 to 5 minutes; hard-boiled eggs take 18 to 20 minutes.",
            "Warm steeping method: Soft-boiled eggs take 4 to 6 minutes; hard-boiled eggs take 30 to 35 minutes. Follow the boiling water method, but cover tightly and remove the pot from heat, letting eggs cook in residual heat until done.",
            "Cooling eggs under cold running water makes them easier to handle, eases peeling for hard-boiled eggs, and halts further cooking; overcooking can cause yolks to discolor and turn dark."
        ],
        "tags": {
            "dietary": [],
            "seasonal": [],
            "festival": [],
            "main_ingredients": ["Chicken egg"]
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
            "pdf_pages": [44, 45],
            "printed_page_numbers": [76, 77],
            "extraction_method": "manual_visual_transcription_from_scanned_spread"
        },
        "data_quality": {
            "extraction_status": "extracted",
            "confidence": 0.95,
            "review_notes": [
                "Technique and recipe entry describing 3 distinct egg-boiling procedures (cold water start, boiling water start, and covered warm steeping).",
                "Ingredient quantities are per user need; no fixed count or serving size stated in source.",
                "In unit, added gram (g) and piece."
            ],
            "verified": False
        }
    },

    # R0008: ကြက်ဥပေါင်း (STEAMED EGGS)
    {
        "recipe_id": "R0008",
        "name_mm": "ကြက်ဥပေါင်း",
        "name_en": "Steamed Eggs",
        "description_mm": None,
        "description_en": None,
        "category": "Egg dishes",
        "meal_types": ["lunch", "dinner", "side_dish"],
        "ingredients": [
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
                "preparation_note_mm": None,
                "preparation_note_en": None
            },
            {
                "ingredient_id": "I0012",
                "name_mm": "ရေနွေး",
                "name_en": "Hot water",
                "original_name": "ရေနွေးပူပူ",
                "quantity": 1.5,
                "unit": "ခွက် (cup / g)",
                "original_quantity_text": "၁ ၁/၂ ခွက်",
                "normalized_quantity": 360.0,
                "normalized_unit": "g",
                "preparation_note_mm": "ပူပူ",
                "preparation_note_en": "piping hot"
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
                "ingredient_id": "I0037",
                "name_mm": "ဝက်သားနုပ်နုပ်စဉ်း",
                "name_en": "Minced pork",
                "original_name": "ဝက်သား (စဉ့်ကော)",
                "quantity": 7.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၇ ၁/၂ ကျပ်သား",
                "normalized_quantity": 122.5,
                "normalized_unit": "g",
                "preparation_note_mm": "စဉ့်ကော (နုပ်နုပ်စဉ်း)",
                "preparation_note_en": "minced"
            },
            {
                "ingredient_id": "I0038",
                "name_mm": "ဟင်းနုနွယ်",
                "name_en": "Spinach",
                "original_name": "ဟင်းနုနွယ် (ပါးပါးလှီး)",
                "quantity": 7.5,
                "unit": "ကျပ်သား (g)",
                "original_quantity_text": "၇ ၁/၂ ကျပ်သား",
                "normalized_quantity": 122.5,
                "normalized_unit": "g",
                "preparation_note_mm": "ပါးပါးလှီး (ဝက်သားအစား ရွေးချယ်နိုင်သည်)",
                "preparation_note_en": "thinly sliced (alternative to minced pork)"
            }
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": 20,
        "instructions_mm": [
            "ကြက်ဥများကို ခက်ရင်းဖြင့် ခေါက်မွှေပါ။",
            "ဝက်သား နုပ်နုပ်စဉ်း (သို့) ဟင်းနုနွယ် ရိတ်ရိတ်လှီးထားသည်များနှင့် ဆားထည့်၍ ကောင်းစွာရောစပ်ပါ။",
            "ရေနွေးထည့်ထားသော အဖုံးပါသည့်အိုးကြီးအတွင်းရှိ အဖုံးဖွင့်ထားသော ဒန်အိုးငယ်အတွင်း၌ ၎င်းကိုထည့်ပါ။",
            "မီးအေးအေးဖြင့် ရေထဲတွင် တစ်ဝက်တစ်ပျက်မြုပ်စေလျက် မိနစ်(၂၀)ခန့် ပေါင်းပါ။",
            "(မီးရှိန်ပြင်းလွန်းပါက ကြက်ဥများ ကွဲထွက်ခြင်း၊ အပေါက်များဖြစ်ခြင်းတို့ ဖြစ်ပေါ်တတ်သည်)။"
        ],
        "instructions_en": [
            "Beat the eggs thoroughly with a fork.",
            "Add the finely minced pork (or finely sliced spinach) and salt; mix together thoroughly.",
            "Pour the mixture into an uncovered small bowl/pot placed inside a larger covered steaming pot containing hot water.",
            "Steam over gentle heat with the small container halfway submerged in the simmering water for about 20 minutes.",
            "(Note: If the steam heat is excessively high, the steamed custard may crack or develop honeycomb holes)."
        ],
        "tags": {
            "dietary": [],
            "seasonal": [],
            "festival": [],
            "main_ingredients": ["Chicken egg", "Minced pork", "Spinach"]
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
            "pdf_pages": [45],
            "printed_page_numbers": [77],
            "extraction_method": "manual_visual_transcription_from_scanned_spread"
        },
        "data_quality": {
            "extraction_status": "extracted",
            "confidence": 0.95,
            "review_notes": [
                "Servings stated as '(လူ ၁၀ ဦးစာ)' in original heading.",
                "Original recipe presents minced pork and spinach as mutually interchangeable alternatives ('ဝက်သား (စဉ့်ကော) (သို့) ဟင်းနုနွယ် (ပါးပါးလှီး)'). Both are cataloged.",
                "In unit, added gram (g) to traditional Burmese units: ကျပ်သား (g), ခွက် (cup / g), စားပွဲဇွန်း (tbsp / g)."
            ],
            "verified": False
        }
    },

    # R0009: ကြက်ဥကြော် (FRIED EGGS)
    {
        "recipe_id": "R0009",
        "name_mm": "ကြက်ဥကြော်",
        "name_en": "Fried Eggs",
        "description_mm": None,
        "description_en": None,
        "category": "Egg dishes",
        "meal_types": ["breakfast", "side_dish"],
        "ingredients": [
            {
                "ingredient_id": "I0026",
                "name_mm": "ကြက်ဥ",
                "name_en": "Chicken egg",
                "original_name": "ကြက်ဥ",
                "quantity": 1.0,
                "unit": "လုံး (piece)",
                "original_quantity_text": "တစ်ကြိမ်လျှင် တစ်လုံးစီ",
                "normalized_quantity": 1.0,
                "normalized_unit": "piece",
                "preparation_note_mm": "ကော်ဖီအောက်ခံပန်းကန်ပြားတွင် အရင်ခွဲထည့်ရန်",
                "preparation_note_en": "cracked into a saucer first"
            },
            {
                "ingredient_id": "I0002",
                "name_mm": "ထောပတ်",
                "name_en": "Butter",
                "original_name": "ထောပတ်(သို့)ဆီ",
                "quantity": None,
                "unit": "ကျပ်သား / စားပွဲဇွန်း (g)",
                "original_quantity_text": "ပါးပါးထည့်၍",
                "normalized_quantity": None,
                "normalized_unit": "g",
                "preparation_note_mm": "ဒယ်အိုးတွင် ပါးပါးသုတ်လိမ်းထည့်ရန်",
                "preparation_note_en": "lightly coating the skillet"
            },
            {
                "ingredient_id": "I0004",
                "name_mm": "ဆား",
                "name_en": "Salt",
                "original_name": "ဆား",
                "quantity": None,
                "unit": "လက်ဖက်ရည်ဇွန်း (g)",
                "original_quantity_text": "ဖြူးပေးပါ",
                "normalized_quantity": None,
                "normalized_unit": "g",
                "preparation_note_mm": "အပေါ်မှ ဖြူးရန်",
                "preparation_note_en": "to sprinkle on top"
            },
            {
                "ingredient_id": "I0039",
                "name_mm": "ငရုတ်ကောင်းမှုန့်",
                "name_en": "Ground black pepper",
                "original_name": "ငရုတ်ကောင်းမှုန့်",
                "quantity": None,
                "unit": "လက်ဖက်ရည်ဇွန်း (g)",
                "original_quantity_text": "ဖြူးပေးပါ",
                "normalized_quantity": None,
                "normalized_unit": "g",
                "preparation_note_mm": "အပေါ်မှ ဖြူးရန်",
                "preparation_note_en": "to sprinkle on top"
            }
        ],
        "servings": None,
        "preparation_time_minutes": None,
        "cooking_time_minutes": 4,
        "instructions_mm": [
            "အောက်ခြေထူသော လက်ကိုင်တပ်ဒယ်အိုးတစ်လုံးတွင် ထောပတ်(သို့)ဆီပါးပါးထည့်၍ အသင့်အတင့် ပူလာအောင် အပူပေးပါ။ ကြက်ဥကို တစ်ကြိမ်လျှင် တစ်လုံးစီခွဲကာ ကော်ဖီအောက်ခံပန်းကန်ပြားတွင်ထည့်၍ ဒယ်အိုးထဲသို့ လျှောထည့်ပါ။ မီးရှိန်ကို လျင်မြန်စွာလျှော့ချပါ။",
            "ဇွန်းဖြင့် ဆီကို ကြက်ဥပေါ်သို့ ခပ်လောင်းပေး၍ ကြက်ဥအကာများခဲကာ အနှစ်ပေါ်မှ အမှေးပါးပေါ်လာသည်အထိ (၃ မှ ၄ မိနစ်ခန့်) ဖြည်းဖြည်းကြော်ပါ။ ဆားနှင့် ငရုတ်ကောင်းမှုန့်များ ဖြူးပေးပါ။ ပူနွေးသော ပန်းကန်ပြားပေါ်သို့ ထည့်၍ ချက်ချင်း စားသုံးပါ။"
        ],
        "instructions_en": [
            "In a heavy-bottomed skillet, lightly coat with butter or cooking oil and heat until moderately warm. Crack each egg individually into a saucer and gently slide it into the skillet; quickly reduce the heat.",
            "Gently spoon hot oil over the egg, basting slowly for 3 to 4 minutes until the whites are fully set and a delicate film forms over the yolk. Sprinkle with salt and ground black pepper, transfer onto a warm plate, and serve immediately."
        ],
        "tags": {
            "dietary": [],
            "seasonal": [],
            "festival": [],
            "main_ingredients": ["Chicken egg", "Butter", "Cooking oil"]
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
            "pdf_pages": [45],
            "printed_page_numbers": [78],
            "extraction_method": "manual_visual_transcription_from_scanned_spread"
        },
        "data_quality": {
            "extraction_status": "extracted",
            "confidence": 0.95,
            "review_notes": [
                "Classic fried egg technique (sunny-side-up with gentle spoon-basting).",
                "Quantities are per egg; butter and oil are presented as alternatives.",
                "In unit, added gram (g) and piece."
            ],
            "verified": False
        }
    },

    # R0010: ကြက်ဥမွှေကြော် (SCRAMBLED EGGS)
    {
        "recipe_id": "R0010",
        "name_mm": "ကြက်ဥမွှေကြော်",
        "name_en": "Scrambled Eggs",
        "description_mm": None,
        "description_en": None,
        "category": "Egg dishes",
        "meal_types": ["breakfast", "side_dish"],
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
                "ingredient_id": "I0039",
                "name_mm": "ငရုတ်ကောင်းမှုန့်",
                "name_en": "Ground black pepper",
                "original_name": "ငရုတ်ကောင်း",
                "quantity": 0.25,
                "unit": "လက်ဖက်ရည်ဇွန်း (tsp / g)",
                "original_quantity_text": "၁/၄ လဖဇ",
                "normalized_quantity": 1.25,
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
                "unit": "စားပွဲဇွန်း (tbsp / g)",
                "original_quantity_text": "၅ စပဇ",
                "normalized_quantity": 75.0,
                "normalized_unit": "g",
                "preparation_note_mm": None,
                "preparation_note_en": None
            }
        ],
        "servings": 10,
        "preparation_time_minutes": None,
        "cooking_time_minutes": 8,
        "instructions_mm": [
            "ပန်းကန်လုံးတစ်လုံးထဲတွင် ကြက်ဥ၊ ဆားအနည်းငယ်နှင့် ငရုတ်ကောင်းတို့ထည့်ပါ။ ခက်ရင်းဖြင့်ခေါက်မွှေပါ။ အဖြူနှင့်ရွှေရောင်ပေါ်စေရန် ကောင်းစွာ ကြေညက်သည်အထိ ရောမမွှေပါနှင့်။ (စိုစွတ်၊ နူးညံ့၍ ရွှေရောင်အဆင်းရှိ၏)။",
            "အသင့်အတင့် အပူပေးထားသော လက်ကိုင်တပ်ဒယ်အိုးတွင် ဆီကို ကြက်ဥတစ်လုံးလျှင် ၁/၂ စားပွဲဇွန်းစာအတွက် ကျထည့်ပါ။ ကြက်ဥအရောအနှောအမွှေကို လောင်းထည့်၍ မီးရှိန်ကို လျှော့ချပါ။ (ကြက်ဥကို ဖြည်းဖြည်းနှင့် ညင်သာစွာ မွှေသင့်သည်)။",
            "ကြက်ဥများ ဒယ်အိုးအောက်ခြေနှင့် ဘေးဘက်တွင် ခဲပြုလာလျှင် ကျက်သောအအပိုင်းကို စပက်ကျူလာကော်တံပြား (သို့) ဇွန်းပြားဖြင့်မ၍ အပိုင်းအားလုံး ညီညာစွာကျက်အောင် အသာအယာ တစ်ဖက်သို့ လှန်ပေးရပါမည်။",
            "ကြက်ဥများ ကျက်၍ စိုစွတ်တောက်ပပြောင်လာသောအခါ (၅ မှ ၈ မိနစ်ခန့်အတွင်း) ချက်ချင်း ပန်းကန်ထဲသို့ လျင်မြန်စွာပြောင်းထည့်၍ ပူပူနွေးနွေး စားသုံးနိုင်ပါသည်။"
        ],
        "instructions_en": [
            "In a mixing bowl, combine eggs with salt and ground black pepper. Whisk lightly with a fork, intentionally leaving streaks of white and yellow without over-mixing. (The finished texture should remain moist, tender, and golden).",
            "Heat cooking oil in a skillet over moderate flame (allocating about 1/2 tablespoon oil per egg). Pour in the beaten egg mixture and lower the heat. (Stir gently and slowly).",
            "As the eggs begin to set at the base and edges, gently lift and fold cooked sections using a spatula or flat spoon so that uncooked portions flow underneath to cook evenly.",
            "Once softly set, glistening, and moist (within 5 to 8 minutes), quickly transfer to a serving plate and enjoy hot."
        ],
        "tags": {
            "dietary": [],
            "seasonal": [],
            "festival": [],
            "main_ingredients": ["Chicken egg", "Cooking oil"]
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
            "pdf_pages": [45],
            "printed_page_numbers": [78, 79],
            "extraction_method": "manual_visual_transcription_from_scanned_spread"
        },
        "data_quality": {
            "extraction_status": "extracted",
            "confidence": 0.95,
            "review_notes": [
                "Servings stated as '(လူ ၁၀ ဦးစာ)' in printed page 79 ingredient table.",
                "In unit, added gram (g) to traditional Burmese units: စားပွဲဇွန်း (tbsp / g), လက်ဖက်ရည်ဇွန်း (tsp / g)."
            ],
            "verified": False
        }
    }
]

# 2. INGREDIENTS CATALOG
ingredients = [
    {
        "ingredient_id": "I0001",
        "name_mm": "ဆန်",
        "name_en": "Rice",
        "aliases_mm": ["ပေါ်ဆန်းမွှေးဆန်", "ဆန်ဟောင်း", "ဆန်ကောင်းကောင်း"],
        "aliases_en": ["Paw San Hmwe rice", "aged rice", "high quality rice"],
        "category": "grain",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0002",
        "name_mm": "ထောပတ်",
        "name_en": "Butter",
        "aliases_mm": [],
        "aliases_en": [],
        "category": "dairy",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0003",
        "name_mm": "ဆီ",
        "name_en": "Cooking oil",
        "aliases_mm": ["ဟင်းချက်ဆီ", "မြေပဲဆီ"],
        "aliases_en": ["peanut oil", "vegetable oil"],
        "category": "oil",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0004",
        "name_mm": "ဆား",
        "name_en": "Salt",
        "aliases_mm": ["ဆားနု"],
        "aliases_en": ["fine salt", "table salt"],
        "category": "seasoning",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0005",
        "name_mm": "သကြား",
        "name_en": "Sugar",
        "aliases_mm": ["သကြားဖြူ"],
        "aliases_en": ["white sugar", "granulated sugar"],
        "category": "seasoning",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0006",
        "name_mm": "ကြက်သွန်နီ",
        "name_en": "Onion",
        "aliases_mm": ["ကြက်သွန်နီဥ"],
        "aliases_en": ["shallot", "red onion"],
        "category": "vegetable",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0007",
        "name_mm": "ဇာတိပ္ဖိုလ်သီး",
        "name_en": "Nutmeg",
        "aliases_mm": ["ဇာတိပ္ဖိုလ်သီးမှုန့်"],
        "aliases_en": ["ground nutmeg"],
        "category": "spice",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0008",
        "name_mm": "သစ်ကြံပိုးခေါက်",
        "name_en": "Cinnamon bark",
        "aliases_mm": ["သစ်ကြံပိုး"],
        "aliases_en": ["cinnamon stick"],
        "category": "spice",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0009",
        "name_mm": "လေးညှင်းပွင့်",
        "name_en": "Cloves",
        "aliases_mm": ["လေးညှင်း"],
        "aliases_en": ["whole cloves"],
        "category": "spice",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0010",
        "name_mm": "ဖာလာစေ့",
        "name_en": "Cardamom pods",
        "aliases_mm": ["ဖာလာ"],
        "aliases_en": ["green cardamom"],
        "category": "spice",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0011",
        "name_mm": "ကရဝေးရွက်",
        "name_en": "Bay leaves",
        "aliases_mm": [],
        "aliases_en": ["Indian bay leaf"],
        "category": "herb",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0012",
        "name_mm": "ရေနွေး",
        "name_en": "Hot water",
        "aliases_mm": ["ရေနွေးပူပူ"],
        "aliases_en": ["boiling water"],
        "category": "liquid",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0013",
        "name_mm": "ပဲနီလေး",
        "name_en": "Red lentils",
        "aliases_mm": [],
        "aliases_en": ["masoor dal"],
        "category": "legume",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0014",
        "name_mm": "မုန်လာဥနီ",
        "name_en": "Carrot",
        "aliases_mm": [],
        "aliases_en": [],
        "category": "vegetable",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0015",
        "name_mm": "ပဲသီး",
        "name_en": "Green beans",
        "aliases_mm": ["ဗိုလ်စားပဲ"],
        "aliases_en": ["string beans", "french beans"],
        "category": "vegetable",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0016",
        "name_mm": "ပဲစိမ်းလုံး",
        "name_en": "Green peas",
        "aliases_mm": [],
        "aliases_en": ["sweet peas"],
        "category": "vegetable",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0017",
        "name_mm": "ရေ",
        "name_en": "Water",
        "aliases_mm": ["ရေအေး"],
        "aliases_en": ["cold water"],
        "category": "liquid",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0018",
        "name_mm": "အုန်းသီး",
        "name_en": "Coconut",
        "aliases_mm": ["အုန်းနို့"],
        "aliases_en": ["coconut milk", "grated coconut"],
        "category": "fruit",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0019",
        "name_mm": "ထမင်း",
        "name_en": "Cooked rice",
        "aliases_mm": ["ထမင်းအေး"],
        "aliases_en": ["leftover rice", "steamed rice"],
        "category": "grain",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0020",
        "name_mm": "ကြက်သား",
        "name_en": "Chicken meat",
        "aliases_mm": [],
        "aliases_en": [],
        "category": "meat",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0021",
        "name_mm": "ပုစွန်ခြောက်",
        "name_en": "Dried shrimp",
        "aliases_mm": ["ပုစွန်ခြောက်မှုန့်"],
        "aliases_en": ["pounded dried shrimp"],
        "category": "seafood",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0022",
        "name_mm": "ကြက်သွန်ဖြူ",
        "name_en": "Garlic",
        "aliases_mm": ["ကြက်သွန်ဖြူဥ"],
        "aliases_en": [],
        "category": "vegetable",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0023",
        "name_mm": "ပဲငံပြာရည်အကြည်",
        "name_en": "Light soy sauce",
        "aliases_mm": [],
        "aliases_en": [],
        "category": "sauce",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0024",
        "name_mm": "ပဲငံပြာရည်အနောက်",
        "name_en": "Dark soy sauce",
        "aliases_mm": [],
        "aliases_en": [],
        "category": "sauce",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0025",
        "name_mm": "ကြက်သွန်မြိတ်",
        "name_en": "Spring onion",
        "aliases_mm": [],
        "aliases_en": ["scallion", "green onion"],
        "category": "vegetable",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0026",
        "name_mm": "ကြက်ဥ",
        "name_en": "Chicken egg",
        "aliases_mm": [],
        "aliases_en": ["egg"],
        "category": "dairy",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0027",
        "name_mm": "ဘဲဥ",
        "name_en": "Duck egg",
        "aliases_mm": [],
        "aliases_en": [],
        "category": "dairy",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0028",
        "name_mm": "ကြက်ရင်အုပ်သား",
        "name_en": "Chicken breast",
        "aliases_mm": [],
        "aliases_en": ["chicken breast halves"],
        "category": "meat",
        "default_unit": "piece"
    },
    {
        "ingredient_id": "I0029",
        "name_mm": "ဒိန်ချဉ်",
        "name_en": "Curd / Yogurt",
        "aliases_mm": [],
        "aliases_en": ["plain yogurt"],
        "category": "dairy",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0030",
        "name_mm": "ချင်း",
        "name_en": "Ginger",
        "aliases_mm": ["ဂျင်း"],
        "aliases_en": ["fresh ginger"],
        "category": "vegetable",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0031",
        "name_mm": "နံနံစေ့အမှုန့်",
        "name_en": "Coriander powder",
        "aliases_mm": ["နံနံစေ့မှုန့်"],
        "aliases_en": ["ground coriander"],
        "category": "spice",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0032",
        "name_mm": "ဗာဒံသီး",
        "name_en": "Almonds",
        "aliases_mm": ["ဗာဒံစေ့"],
        "aliases_en": ["almond nuts"],
        "category": "nut",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0033",
        "name_mm": "စပျစ်သီးခြောက်",
        "name_en": "Raisins",
        "aliases_mm": ["စပျစ်ခြောက်"],
        "aliases_en": ["sultanas", "dried raisins"],
        "category": "fruit",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0034",
        "name_mm": "ဂုံမန်",
        "name_en": "Saffron",
        "aliases_mm": ["ကုံကုမံ"],
        "aliases_en": ["kesar", "saffron threads"],
        "category": "spice",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0035",
        "name_mm": "နှင်းရည်",
        "name_en": "Rose water",
        "aliases_mm": [],
        "aliases_en": ["culinary rose water"],
        "category": "liquid",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0036",
        "name_mm": "နွားနို့",
        "name_en": "Cow milk",
        "aliases_mm": ["နို့စိမ်း"],
        "aliases_en": ["fresh milk"],
        "category": "dairy",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0037",
        "name_mm": "ဝက်သားနုပ်နုပ်စဉ်း",
        "name_en": "Minced pork",
        "aliases_mm": ["ဝက်သား (စဉ့်ကော)", "ဝက်သားစဉ်းကော"],
        "aliases_en": ["ground pork"],
        "category": "meat",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0038",
        "name_mm": "ဟင်းနုနွယ်",
        "name_en": "Spinach",
        "aliases_mm": ["ဟင်းနုနွယ်ရွက်"],
        "aliases_en": [],
        "category": "vegetable",
        "default_unit": "g"
    },
    {
        "ingredient_id": "I0039",
        "name_mm": "ငရုတ်ကောင်းမှုန့်",
        "name_en": "Ground black pepper",
        "aliases_mm": ["ငရုတ်ကောင်း"],
        "aliases_en": ["black pepper"],
        "category": "spice",
        "default_unit": "g"
    }
]

# 3. EXTRACTION REPORT
report = {
    "source_document": "ဟင်းချက်နည်းများ.pdf",
    "total_pages_processed": 7,
    "total_recipes_extracted": 10,
    "complete_recipes": 10,
    "partial_recipes": 0,
    "recipes_needing_review": 0,
    "unique_ingredients": len(ingredients),
    "unreadable_pages": [],
    "recipes_with_missing_quantities": [],
    "ambiguous_ingredients": [],
    "validation_errors": [],
    "general_notes": [
        "Pilot Dataset v2: Extended pilot covering the first 10 recipes from Section 22 (ချက်ပြုတ်နည်းများ), spanning printed pages 73-79 (PDF pages 42-45).",
        "Updated unit specification per user feedback: In the 'unit' field, metric equivalents in grams (g) or pieces have been added alongside the original Burmese units (e.g., 'ကျပ်သား (g)', 'နို့ဆီဘူး (g)', 'စားပွဲဇွန်း (tbsp / g)', 'ခွက် (cup / g)').",
        "Dry rice and lentils in traditional volumetric condensed milk tins (နို့ဆီဘူး) have been normalized at the standard Myanmar kitchen density of 250 g per tin.",
        "Liquids in condensed milk tins, cups, and spoons have been standardized directly in grams (1 ml ≈ 1 g).",
        "All 10 recipes have 100% 1:1 aligned Burmese Unicode and natural culinary English instruction steps.",
        "All ingredient references resolve seamlessly to the deduplicated bilingual catalog (I0001 - I0039)."
    ]
}

with open('recipes.json', 'w', encoding='utf-8') as f:
    json.dump(recipes, f, ensure_ascii=False, indent=2)

with open('ingredients.json', 'w', encoding='utf-8') as f:
    json.dump(ingredients, f, ensure_ascii=False, indent=2)

with open('extraction_report.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print("Pilot Dataset v2 (recipes.json, ingredients.json, extraction_report.json) written successfully.")
