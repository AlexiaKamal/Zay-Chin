from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_

from backend.app.core.database import get_db
import backend.app.models as models
from backend.app.schemas.recipe_schemas import (
    RecipeSummaryResponse,
    RecipeDetailResponse,
    RecipeListResponse,
    CategoryCountResponse,
    RecipeIngredientResponse,
    RecipeInstructionResponse
)
from backend.app.services.pricing_service import PricingService
from backend.app.services.nutrition_service import NutritionService

router = APIRouter(prefix="/recipes", tags=["Recipes"])

# Category Burmese dictionary
CATEGORY_TRANSLATIONS = {
    "Rice dishes": "ထမင်းဟင်းလျာများ",
    "Poultry dishes": "ကြက်၊ ဘဲ ဟင်းလျာများ",
    "Pork dishes": "ဝက်သား ဟင်းလျာများ",
    "Beef dishes": "အမဲသား ဟင်းလျာများ",
    "Mutton dishes": "ဆိတ်သား ဟင်းလျာများ",
    "Egg dishes": "ဥဟင်းလျာများ",
    "Fish and prawn curries": "ငါးနှင့် ပုစွန် ဟင်းလျာများ",
    "curry": "ဟင်းလျာများ",
    "soup": "ဟင်းချို၊ ဟင်းခါးများ",
    "salad": "အသုပ်များ",
    "stir_fry": "အကြော်အလှော်များ",
    "deep_fried": "ကြော်ချက်များ",
    "chutney": "ငပိချက်၊ သနပ်စုံများ",
    "pickle_preserve": "အချဉ်တည်နည်း၊ ယိုများ",
    "Preserves and pickles": "ယိုနှင့် အချဉ်များ",
    "noodle": "ခေါက်ဆွဲ၊ မုန့်ဟင်းခါး",
    "dessert": "အချိုပွဲ၊ မုန့်များ",
    "snack": "သရေစာများ",
    "condiment": "အရန်ဟင်းလျာများ",
}

@router.get("", response_model=RecipeListResponse)
def list_recipes(
    page: int = Query(1, ge=1),
    page_size: int = Query(12, ge=1, le=100),
    search: Optional[str] = Query(None, description="Search in Myanmar Unicode or English"),
    category: Optional[str] = Query(None),
    meal_type: Optional[str] = Query(None),
    dietary: Optional[str] = Query(None),
    seasonal: Optional[str] = Query(None),
    festival: Optional[str] = Query(None),
    city: str = Query("Yangon", description="City for price calculations (Yangon or Mandalay)"),
    db: Session = Depends(get_db)
):
    query = db.query(models.Recipe)

    # Search in Myanmar or English
    if search:
        search_term = f"%{search.strip()}%"
        # Search recipe name or ingredients
        query = query.filter(
            or_(
                models.Recipe.name_mm.ilike(search_term),
                models.Recipe.name_en.ilike(search_term),
                models.Recipe.description_mm.ilike(search_term),
                models.Recipe.description_en.ilike(search_term),
                models.Recipe.id.ilike(search_term),
            )
        )

    if category:
        query = query.filter(models.Recipe.category == category)

    total = query.count()
    recipes = query.order_by(models.Recipe.id).offset((page - 1) * page_size).limit(page_size).all()

    recipe_summaries = []
    for r in recipes:
        # Dynamic cost estimate
        cost_info = PricingService.calculate_recipe_cost(r, db, city=city)
        # Dynamic nutrition estimate
        nutr_info = NutritionService.calculate_recipe_nutrition(r, db)

        # Filters for JSON tags / meal_types
        if meal_type and meal_type not in (r.meal_types or []):
            continue
        if dietary and dietary not in (r.tags.get("dietary", []) if r.tags else []):
            continue
        if seasonal and seasonal not in (r.tags.get("seasonal", []) if r.tags else []):
            continue
        if festival and festival not in (r.tags.get("festival", []) if r.tags else []):
            continue

        recipe_summaries.append(
            RecipeSummaryResponse(
                id=r.id,
                name_mm=r.name_mm,
                name_en=r.name_en,
                description_mm=r.description_mm,
                description_en=r.description_en,
                category=r.category,
                meal_types=r.meal_types or [],
                servings=r.servings,
                preparation_time_minutes=r.preparation_time_minutes,
                cooking_time_minutes=r.cooking_time_minutes,
                tags=r.tags or {},
                estimated_cost_mmk=cost_info["estimated_cost_mmk"],
                cost_coverage_percentage=cost_info["cost_coverage_percentage"],
                is_cost_complete=cost_info["is_cost_complete"],
                calories_kcal_per_serving=nutr_info["per_serving"]["calories_kcal"],
                protein_g_per_serving=nutr_info["per_serving"]["protein_g"],
            )
        )

    total_pages = (total + page_size - 1) // page_size if page_size else 1

    return RecipeListResponse(
        total=total,
        page=page,
        page_size=page_size,
        total_pages=total_pages,
        recipes=recipe_summaries
    )


@router.get("/categories", response_model=List[CategoryCountResponse])
def get_categories(db: Session = Depends(get_db)):
    recipes = db.query(models.Recipe).all()
    counts = {}
    for r in recipes:
        counts[r.category] = counts.get(r.category, 0) + 1

    result = []
    for cat, count in sorted(counts.items(), key=lambda x: -x[1]):
        result.append(
            CategoryCountResponse(
                category=cat,
                category_mm=CATEGORY_TRANSLATIONS.get(cat, cat),
                count=count
            )
        )
    return result


@router.get("/{recipe_id}", response_model=RecipeDetailResponse)
def get_recipe_detail(
    recipe_id: str,
    servings: Optional[int] = Query(None, ge=1, le=50, description="Override servings count to scale ingredients"),
    city: str = Query("Yangon", description="City for price observations (Yangon / Mandalay)"),
    db: Session = Depends(get_db)
):
    recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail=f"Recipe '{recipe_id}' not found.")

    base_servings = recipe.servings or 4
    target_servings = servings or base_servings
    multiplier = target_servings / base_servings if base_servings else 1.0

    # Calculate dynamic costs and nutrition
    cost_info = PricingService.calculate_recipe_cost(recipe, db, city=city, servings_multiplier=multiplier)
    nutr_info = NutritionService.calculate_recipe_nutrition(recipe, db)

    # Scaled ingredients list
    scaled_ingredients = []
    for ri in recipe.ingredients:
        sq = (ri.quantity * multiplier) if ri.quantity is not None else None
        snq = (ri.normalized_quantity * multiplier) if ri.normalized_quantity is not None else None
        scaled_ingredients.append(
            RecipeIngredientResponse(
                id=ri.id,
                ingredient_id=ri.ingredient_id,
                original_name=ri.original_name,
                name_mm=ri.name_mm,
                name_en=ri.name_en,
                quantity=round(sq, 2) if sq is not None else None,
                unit=ri.unit,
                original_quantity_text=ri.original_quantity_text,
                normalized_quantity=round(snq, 2) if snq is not None else None,
                normalized_unit=ri.normalized_unit,
                preparation_note_mm=ri.preparation_note_mm,
                preparation_note_en=ri.preparation_note_en,
            )
        )

    instructions = [
        RecipeInstructionResponse(
            step_number=ins.step_number,
            instruction_mm=ins.instruction_mm,
            instruction_en=ins.instruction_en,
        )
        for ins in recipe.instructions
    ]

    return RecipeDetailResponse(
        id=recipe.id,
        name_mm=recipe.name_mm,
        name_en=recipe.name_en,
        description_mm=recipe.description_mm,
        description_en=recipe.description_en,
        category=recipe.category,
        meal_types=recipe.meal_types or [],
        servings=target_servings,
        preparation_time_minutes=recipe.preparation_time_minutes,
        cooking_time_minutes=recipe.cooking_time_minutes,
        tags=recipe.tags or {},
        source_document=recipe.source_document,
        source_pdf_pages=recipe.source_pdf_pages or [],
        source_printed_pages=recipe.source_printed_pages or [],
        extraction_method=recipe.extraction_method,
        confidence=recipe.confidence,
        is_verified=recipe.is_verified,
        estimated_cost_mmk=cost_info["estimated_cost_mmk"],
        cost_coverage_percentage=cost_info["cost_coverage_percentage"],
        is_cost_complete=cost_info["is_cost_complete"],
        calories_kcal_per_serving=nutr_info["per_serving"]["calories_kcal"],
        protein_g_per_serving=nutr_info["per_serving"]["protein_g"],
        ingredients=scaled_ingredients,
        instructions=instructions,
        cost_breakdown=cost_info,
        nutrition_breakdown=nutr_info,
    )
