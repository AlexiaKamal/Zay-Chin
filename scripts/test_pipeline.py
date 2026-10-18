import json
import pytest
from schemas import PriceObservation, NutritionRecord, DataSource

def test_master_catalog_integrity():
    with open("ingredients.json", "r", encoding="utf-8") as f:
        catalog = json.load(f)
    assert len(catalog) == 221
    ids = [item["ingredient_id"] for item in catalog]
    assert len(ids) == len(set(ids)), "Duplicate ingredient IDs found in master catalog"
    # Check first 5 IDs
    assert ids[:5] == ["I0001", "I0002", "I0003", "I0004", "I0005"]

def test_data_sources_validity():
    with open("data_sources.json", "r", encoding="utf-8") as f:
        sources = json.load(f)
    assert len(sources) == 8
    for s in sources:
        # Validate Pydantic model
        ds = DataSource(**s)
        assert ds.source_id.startswith("SRC")
        assert ds.website_url.startswith("http")

def test_nutrition_records_validity():
    with open("ingredients.json", "r", encoding="utf-8") as f:
        master_ids = set(item["ingredient_id"] for item in json.load(f))
    with open("ingredient_nutrition.json", "r", encoding="utf-8") as f:
        nutrition = json.load(f)
    
    assert len(nutrition) == 221
    for n in nutrition:
        rec = NutritionRecord(**n)
        assert rec.ingredient_id in master_ids
        assert rec.reference_quantity == 100.0
        assert rec.reference_unit == "g"
        assert rec.edible_portion_basis is True
        if rec.energy_kcal is not None:
            assert rec.energy_kcal >= 0.0
        if rec.protein_g is not None:
            assert rec.protein_g >= 0.0
        if rec.total_fat_g is not None:
            assert rec.total_fat_g >= 0.0
        if rec.carbohydrates_g is not None:
            assert rec.carbohydrates_g >= 0.0

def test_price_observations_validity():
    with open("ingredients.json", "r", encoding="utf-8") as f:
        master_ids = set(item["ingredient_id"] for item in json.load(f))
    with open("ingredient_prices.json", "r", encoding="utf-8") as f:
        prices = json.load(f)
    
    assert len(prices) > 0
    for p in prices:
        obs = PriceObservation(**p)
        assert obs.ingredient_id in master_ids
        assert obs.city in ["Yangon", "Mandalay"]
        assert obs.price_mmk > 0
        if obs.normalized_price_mmk_per_kg is not None:
            assert obs.normalized_price_mmk_per_kg > 0
        assert obs.price_type in ["retail", "wholesale", "estimate"]
        assert obs.observation_type in ["official_retail_average", "commodity_exchange_quote", "supermarket_listing", "model_estimate"]

def test_latest_retail_prices_by_city():
    with open("latest_retail_prices_by_city.json", "r", encoding="utf-8") as f:
        city_prices = json.load(f)
    assert "cities" in city_prices
    assert "Yangon" in city_prices["cities"]
    assert "Mandalay" in city_prices["cities"]
    assert len(city_prices["cities"]["Yangon"]) > 0

def test_data_quality_report():
    with open("data_quality_report.json", "r", encoding="utf-8") as f:
        report = json.load(f)
    m = report["metrics"]
    assert m["total_input_ingredients"] == 221
    assert m["nutrition_coverage_percentage"] == 100.0
    assert m["price_coverage_percentage"] > 0.0
    assert m["duplicate_records_detected"] == 0
