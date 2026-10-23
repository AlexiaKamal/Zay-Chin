import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"

def test_recipes_list():
    response = client.get("/api/v1/recipes?page=1&page_size=5&city=Yangon")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 171
    assert len(data["recipes"]) == 5
    first = data["recipes"][0]
    assert first["id"] == "R0001"
    assert first["name_mm"] == "ထောပတ်ထမင်း"
    assert first["estimated_cost_mmk"] is not None
    assert first["estimated_cost_mmk"] > 0
    assert first["calories_kcal_per_serving"] is not None

def test_bilingual_search():
    # Search in Myanmar
    res_mm = client.get("/api/v1/recipes?search=ထောပတ်")
    assert res_mm.status_code == 200
    assert res_mm.json()["total"] >= 1

    # Search in English
    res_en = client.get("/api/v1/recipes?search=Butter")
    assert res_en.status_code == 200
    assert res_en.json()["total"] >= 1

def test_recipe_detail():
    response = client.get("/api/v1/recipes/R0001?city=Yangon")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "R0001"
    assert len(data["ingredients"]) == 12
    assert len(data["instructions"]) == 7
    assert data["cost_breakdown"] is not None
    assert data["nutrition_breakdown"] is not None

def test_categories():
    response = client.get("/api/v1/recipes/categories")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 15
    cats = [c["category"] for c in data]
    assert "Rice dishes" in cats

def test_markets():
    response = client.get("/api/v1/markets")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 4

def test_planner_generation():
    payload = {
        "city": "Yangon",
        "household_size": 2,
        "weekly_budget_mmk": 75000,
        "meals_per_day": 3,
        "plan_duration_days": 7
    }
    response = client.post("/api/v1/planner/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["city"] == "Yangon"
    assert data["household_size"] == 2
    assert len(data["schedule"]) == 21  # 7 days * 3 meals
    assert len(data["daily_summaries"]) == 7
    assert data["estimated_total_cost_mmk"] > 0
    assert data["estimated_total_cost_mmk"] <= 75000
    assert data["is_budget_exceeded"] is False
    assert "Generated within your budget" in data["budget_status_message_en"]
    assert data["average_daily_calories_per_person"] > 0

def test_planner_replacement():
    payload = {
        "city": "Yangon",
        "household_size": 2,
        "day_of_week": 1,
        "meal_type": "lunch",
        "current_recipe_id": "R0001"
    }
    response = client.post("/api/v1/planner/replace-options", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert len(data["candidates"]) >= 1
    assert data["current_recipe_id"] == "R0001"

def test_grocery_generation():
    payload = {
        "city": "Yangon",
        "household_size": 2,
        "recipe_ids": ["R0001", "R0002", "R0003"]
    }
    response = client.post("/api/v1/grocery/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["total_items_count"] > 0
    assert len(data["groups"]) >= 1
    assert data["estimated_total_mmk"] > 0
