from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class GroceryItemSchema(BaseModel):
    id: Optional[int] = None
    ingredient_id: str
    name_en: str
    name_mm: str
    category: str
    total_quantity: float
    unit: str
    purchasable_quantity: Optional[float] = None
    purchasable_unit_en: Optional[str] = None
    purchasable_unit_mm: Optional[str] = None
    package_description_en: Optional[str] = None
    package_description_mm: Optional[str] = None
    estimated_price_mmk: Optional[float] = None
    retail_package_price_mmk: Optional[float] = None
    is_pantry_staple: bool = False
    in_pantry: bool = False
    is_price_available: bool = True
    is_zero_cost_utility: bool = False
    observation_source: Optional[str] = None
    observation_date: Optional[str] = None
    is_purchased: bool = False

class GroceryCategoryGroup(BaseModel):
    category_id: str
    category_name_en: str
    category_name_mm: str
    subtotal_mmk: float
    items: List[GroceryItemSchema]

class GroceryListGenerateRequest(BaseModel):
    city: str = Field("Yangon", description="Yangon or Mandalay")
    household_size: int = Field(2, ge=1, le=12)
    recipe_ids: List[str] = Field(..., description="List of recipe IDs included in plan/shopping")
    custom_items: List[Dict[str, Any]] = Field(default_factory=list)

class GroceryListResponse(BaseModel):
    id: Optional[int] = None
    city: str
    household_size: int
    total_items_count: int
    purchased_items_count: int
    estimated_total_mmk: float
    retail_total_mmk: Optional[float] = None
    pantry_adjusted_total_mmk: Optional[float] = None
    pantry_items_count: int = 0
    coverage_percentage: float
    groups: List[GroceryCategoryGroup]
    unpriced_items_count: int

class GroceryItemToggleRequest(BaseModel):
    is_purchased: bool
