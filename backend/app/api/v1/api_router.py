from fastapi import APIRouter
from backend.app.api.v1.recipes import router as recipes_router
from backend.app.api.v1.ingredients import router as ingredients_router
from backend.app.api.v1.markets import router as markets_router
from backend.app.api.v1.planner import router as planner_router
from backend.app.api.v1.grocery import router as grocery_router

api_router = APIRouter()
api_router.include_router(recipes_router)
api_router.include_router(ingredients_router)
api_router.include_router(markets_router)
api_router.include_router(planner_router)
api_router.include_router(grocery_router)
