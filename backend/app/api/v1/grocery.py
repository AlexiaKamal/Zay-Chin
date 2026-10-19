from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.core.database import get_db
from backend.app.schemas.grocery_schemas import (
    GroceryListGenerateRequest,
    GroceryListResponse,
    GroceryItemToggleRequest
)
from backend.app.services.grocery_service import GroceryService

router = APIRouter(prefix="/grocery", tags=["Grocery Lists"])

@router.post("/generate", response_model=GroceryListResponse)
def generate_grocery_list(
    req: GroceryListGenerateRequest,
    db: Session = Depends(get_db)
):
    """
    Aggregates ingredients from selected recipes or weekly meal plans into a categorized grocery checklist.
    """
    if not req.recipe_ids:
        raise HTTPException(status_code=400, detail="At least one recipe ID must be provided.")
    return GroceryService.generate_grocery_list(db, req)
