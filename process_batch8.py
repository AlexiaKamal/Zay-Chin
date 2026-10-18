# -*- coding: utf-8 -*-
"""
Process Batch 8: Merges recipes R0118 - R0127 (10 recipes) and catalog ingredients I0176 - I0189
into recipes.json, ingredients.json, and updates extraction_report.json.
"""

import json
import os
import sys

from batch8_data import BATCH8_RECIPES, NEW_INGREDIENTS_BATCH8

def main():
    print("Processing Batch 8...")
    print(f"Loaded {len(BATCH8_RECIPES)} recipes")
    print(f"Loaded {len(NEW_INGREDIENTS_BATCH8)} new catalog ingredients")

    # 1. Update ingredients.json
    with open("ingredients.json", "r", encoding="utf-8") as f:
        ingredients = json.load(f)

    existing_ing_ids = {i["ingredient_id"] for i in ingredients}
    added_ings = 0
    for new_ing in NEW_INGREDIENTS_BATCH8:
        if new_ing["ingredient_id"] not in existing_ing_ids:
            ingredients.append(new_ing)
            existing_ing_ids.add(new_ing["ingredient_id"])
            added_ings += 1

    with open("ingredients.json", "w", encoding="utf-8") as f:
        json.dump(ingredients, f, ensure_ascii=False, indent=2)
    print(f"Added {added_ings} new ingredients to ingredients.json (Total now: {len(ingredients)})")

    # 2. Update recipes.json
    with open("recipes.json", "r", encoding="utf-8") as f:
        recipes = json.load(f)

    existing_recipe_ids = {r["recipe_id"] for r in recipes}
    added_recipes = 0
    for rec in BATCH8_RECIPES:
        if rec["recipe_id"] in existing_recipe_ids:
            print(f"Warning: duplicate recipe {rec['recipe_id']}, skipping")
        else:
            recipes.append(rec)
            existing_recipe_ids.add(rec["recipe_id"])
            added_recipes += 1

    with open("recipes.json", "w", encoding="utf-8") as f:
        json.dump(recipes, f, ensure_ascii=False, indent=2)
    print(f"Added {added_recipes} new recipes to recipes.json (Total now: {len(recipes)})")

    # 3. Update extraction_report.json
    report_path = "extraction_report.json"
    if os.path.exists(report_path):
        with open(report_path, "r", encoding="utf-8") as f:
            report = json.load(f)
    else:
        report = {}

    report["total_recipes_extracted"] = len(recipes)
    report["total_ingredients_cataloged"] = len(ingredients)
    report["batches_completed"] = report.get("batches_completed", [])
    if "batch_8" not in report["batches_completed"]:
        report["batches_completed"].append("batch_8")

    report["batch_summary"] = report.get("batch_summary", {})
    report["batch_summary"]["batch_8"] = {
        "recipes_count": len(BATCH8_RECIPES),
        "recipe_range": f"{BATCH8_RECIPES[0]['recipe_id']} - {BATCH8_RECIPES[-1]['recipe_id']}",
        "categories": ["noodle", "salad", "soup"],
        "book_pages": "133-137",
        "pdf_pages": "73-75",
        "new_ingredients_count": added_ings,
        "status": "completed_verified"
    }

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print("Updated extraction_report.json")

if __name__ == "__main__":
    main()
