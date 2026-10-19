from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from backend.app.core.database import get_db
import backend.app.models as models

router = APIRouter(prefix="/ingredients", tags=["Ingredients"])

@router.get("")
def list_ingredients(
    category: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(models.Ingredient)
    if category:
        query = query.filter(models.Ingredient.category == category)
    if search:
        st = f"%{search.strip()}%"
        query = query.filter(
            (models.Ingredient.name_mm.ilike(st)) | (models.Ingredient.name_en.ilike(st))
        )
    return query.order_by(models.Ingredient.id).all()

@router.get("/{ingredient_id}")
def get_ingredient(ingredient_id: str, db: Session = Depends(get_db)):
    ing = db.query(models.Ingredient).filter(models.Ingredient.id == ingredient_id).first()
    if not ing:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    
    return {
        "id": ing.id,
        "name_mm": ing.name_mm,
        "name_en": ing.name_en,
        "category": ing.category,
        "default_unit": ing.default_unit,
        "nutrition": ing.nutrition,
        "prices": ing.prices
    }
