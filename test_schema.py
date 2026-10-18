import json
import sys

with open('recipes.json', encoding='utf-8') as f:
    recipes = json.load(f)

with open('ingredients.json', encoding='utf-8') as f:
    ingredients = json.load(f)

with open('extraction_report.json', encoding='utf-8') as f:
    report = json.load(f)

ing_ids = {i['ingredient_id'] for i in ingredients}

recipe_expected_keys = {
    'recipe_id', 'name_mm', 'name_en', 'description_mm', 'description_en',
    'category', 'meal_types', 'ingredients', 'servings',
    'preparation_time_minutes', 'cooking_time_minutes',
    'instructions_mm', 'instructions_en', 'tags', 'nutrition',
    'estimated_cost_mmk', 'source', 'data_quality'
}

ing_item_keys = {
    'ingredient_id', 'name_mm', 'name_en', 'original_name',
    'quantity', 'unit', 'original_quantity_text',
    'normalized_quantity', 'normalized_unit',
    'preparation_note_mm', 'preparation_note_en'
}

catalog_keys = {
    'ingredient_id', 'name_mm', 'name_en', 'aliases_mm', 'aliases_en',
    'category', 'default_unit'
}

tags_keys = {'dietary', 'seasonal', 'festival', 'main_ingredients'}
nutrition_keys = {'calories_kcal_per_serving', 'protein_g_per_serving', 'carbohydrates_g_per_serving', 'fat_g_per_serving'}
source_keys = {'document', 'pdf_pages', 'printed_page_numbers', 'extraction_method'}
dq_keys = {'extraction_status', 'confidence', 'review_notes', 'verified'}

for i in ingredients:
    assert set(i.keys()) == catalog_keys, f"Catalog mismatch: {set(i.keys()) ^ catalog_keys}"

for r in recipes:
    assert set(r.keys()) == recipe_expected_keys, f"Recipe {r['recipe_id']} keys mismatch: {set(r.keys()) ^ recipe_expected_keys}"
    assert set(r['tags'].keys()) == tags_keys, f"Recipe {r['recipe_id']} tags mismatch"
    assert set(r['nutrition'].keys()) == nutrition_keys, f"Recipe {r['recipe_id']} nutrition mismatch"
    assert set(r['source'].keys()) == source_keys, f"Recipe {r['recipe_id']} source mismatch"
    assert set(r['data_quality'].keys()) == dq_keys, f"Recipe {r['recipe_id']} data_quality mismatch"
    assert len(r['instructions_mm']) == len(r['instructions_en']), f"Instruction mismatch in {r['recipe_id']}: {len(r['instructions_mm'])} mm vs {len(r['instructions_en'])} en"
    for ing in r['ingredients']:
        assert set(ing.keys()) == ing_item_keys, f"Ingredient keys mismatch: {set(ing.keys()) ^ ing_item_keys}"
        if ing['ingredient_id']:
            assert ing['ingredient_id'] in ing_ids, f"Ingredient ID {ing['ingredient_id']} not found in catalog"

print("ALL SCHEMA AND INTEGRITY CHECKS PASSED SUCCESSFULLY!")
