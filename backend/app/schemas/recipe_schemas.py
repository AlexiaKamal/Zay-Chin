from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class RecipeIngredientResponse(BaseModel):
    id: int
    ingredient_id: str
    original_name: Optional[str] = None
    name_mm: str
    name_en: str
    quantity: Optional[float] = None
    unit: str
    original_quantity_text: Optional[str] = None
    normalized_quantity: Optional[float] = None
    normalized_unit: Optional[str] = None
    preparation_note_mm: Optional[str] = None
    preparation_note_en: Optional[str] = None

class RecipeInstructionResponse(BaseModel):
    step_number: int
    instruction_mm: str
    instruction_en: str

class RecipeSummaryResponse(BaseModel):
    id: str
    name_mm: str
    name_en: str
    description_mm: Optional[str] = None
    description_en: Optional[str] = None
    category: str
    meal_types: List[str] = []
    servings: Optional[int] = 4
    preparation_time_minutes: Optional[int] = None
    cooking_time_minutes: Optional[int] = None
    tags: Dict[str, Any] = {}
    
    # Dynamic calculations
    estimated_cost_mmk: Optional[float] = None
    cost_coverage_percentage: float = 0.0
    is_cost_complete: bool = False
    
    calories_kcal_per_serving: Optional[float] = None
    protein_g_per_serving: Optional[float] = None

class RecipeDetailResponse(RecipeSummaryResponse):
    source_document: str
    source_pdf_pages: List[int] = []
    source_printed_pages: List[int] = []
    extraction_method: str
    confidence: float
    is_verified: bool
    
    ingredients: List[RecipeIngredientResponse] = []
    instructions: List[RecipeInstructionResponse] = []
    
    cost_breakdown: Optional[Dict[str, Any]] = None
    nutrition_breakdown: Optional[Dict[str, Any]] = None

class CategoryCountResponse(BaseModel):
    category: str
    category_mm: str
    count: int

class RecipeListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    total_pages: int
    recipes: List[RecipeSummaryResponse]
