from typing import List, Optional, Literal, Union
from pydantic import BaseModel, Field, field_validator

class PriceObservation(BaseModel):
    price_id: str
    ingredient_id: str
    ingredient_name_mm: str
    ingredient_name_en: str
    city: Optional[str] = None
    market_name: Optional[str] = None
    vendor_name: Optional[str] = None
    product_name: Optional[str] = None
    brand: Optional[str] = None
    price_mmk: Optional[float] = None
    original_quantity: Optional[float] = None
    original_unit: Optional[str] = None
    normalized_price_mmk_per_kg: Optional[float] = None
    price_type: Optional[Literal["retail", "wholesale", "estimate"]] = None
    observation_type: Optional[Literal["official_retail_average", "commodity_exchange_quote", "supermarket_listing", "model_estimate"]] = None
    observed_date: Optional[str] = None
    collected_at: Optional[str] = None
    source_name: Optional[str] = None
    source_url: Optional[str] = None
    source_record_id: Optional[str] = None
    availability_status: Literal["available", "out_of_stock", "unknown"] = "unknown"
    verification_status: Literal["verified", "unverified", "flagged_for_review"] = "unverified"
    review_notes: List[str] = Field(default_factory=list)

    @field_validator("price_mmk", "normalized_price_mmk_per_kg")
    def validate_positive_price(cls, v):
        if v is not None and v <= 0:
            raise ValueError("Price must be positive")
        return v

class NutritionRecord(BaseModel):
    nutrition_id: str
    ingredient_id: str
    ingredient_name_mm: str
    ingredient_name_en: str
    food_form: str
    reference_quantity: float = 100.0
    reference_unit: str = "g"
    edible_portion_basis: bool = True
    energy_kcal: Optional[float] = None
    protein_g: Optional[float] = None
    total_fat_g: Optional[float] = None
    carbohydrates_g: Optional[float] = None
    fiber_g: Optional[float] = None
    sugar_g: Optional[float] = None
    sodium_mg: Optional[float] = None
    source_name: Optional[str] = None
    source_food_id: Optional[str] = None
    source_url: Optional[str] = None
    match_type: Optional[Literal["exact", "approximate"]] = None
    verification_status: Literal["verified", "unverified", "flagged_for_review"] = "unverified"
    review_notes: List[str] = Field(default_factory=list)

class DataSource(BaseModel):
    source_id: str
    organization: str
    website_url: str
    dataset_or_api_name: str
    data_type: str
    geographic_coverage: str
    date_accessed: str
    publication_or_observation_date: Optional[str] = None
    license_or_terms_of_use: str
    redistribution_permitted: bool
    automated_collection_permitted: bool
    attribution_requirements: str
    known_limitations: str

class AlternativeMatch(BaseModel):
    ingredient_id: str
    name_mm: str
    name_en: str
    candidate_source: str
    candidate_id: str
    candidate_name: str
    food_form: str
    match_type: str
    decision: Literal["selected_primary", "alternative_reference", "rejected"]
    rationale: str

class UnmatchedIngredient(BaseModel):
    ingredient_id: str
    name_mm: str
    name_en: str
    category: str
    reason: str
    attempted_sources: List[str]
    suggested_action: str
