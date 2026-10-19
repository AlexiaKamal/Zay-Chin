from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.core.database import get_db
from backend.app.schemas.planner_schemas import (
    MealPlanGenerateRequest,
    MealPlanGenerateResponse,
    MealReplacementRequest,
    MealReplacementResponse
)
from backend.app.services.planner_service import PlannerService

router = APIRouter(prefix="/planner", tags=["Meal Planner"])

@router.post("/generate", response_model=MealPlanGenerateResponse)
def generate_meal_plan(
    req: MealPlanGenerateRequest,
    db: Session = Depends(get_db)
):
    """
    Generates an intelligent 7-day Myanmar meal plan tailored to household size, budget, and dietary preferences.
    """
    return PlannerService.generate_plan(db, req)

@router.post("/replace-options", response_model=MealReplacementResponse)
def get_replacement_options(
    req: MealReplacementRequest,
    db: Session = Depends(get_db)
):
    """
    Provides candidate replacement dishes for any specific slot with price difference comparison.
    """
    return PlannerService.get_replacement_options(db, req)
