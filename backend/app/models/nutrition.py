from sqlalchemy import Column, String, Float, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship
from backend.app.core.database import Base

class IngredientNutrition(Base):
    __tablename__ = "ingredient_nutrition"

    id = Column(String(32), primary_key=True, index=True) # e.g. "N000001"
    ingredient_id = Column(String(32), ForeignKey("ingredients.id", ondelete="CASCADE"), unique=True, nullable=False, index=True)
    food_form = Column(String(64), default="raw")
    reference_quantity = Column(Float, default=100.0) # 100g basis
    reference_unit = Column(String(16), default="g")
    edible_portion_basis = Column(Boolean, default=True)
    
    # Nutrients per 100g
    energy_kcal = Column(Float, nullable=True)
    protein_g = Column(Float, nullable=True)
    total_fat_g = Column(Float, nullable=True)
    carbohydrates_g = Column(Float, nullable=True)
    fiber_g = Column(Float, nullable=True)
    sugar_g = Column(Float, nullable=True)
    sodium_mg = Column(Float, nullable=True)
    
    # Metadata & Source
    source_name = Column(String(255), nullable=True)
    source_food_id = Column(String(64), nullable=True)
    source_url = Column(String(512), nullable=True)
    match_type = Column(String(32), default="exact")
    verification_status = Column(String(32), default="verified")
    review_notes = Column(JSON, default=list)

    # Relationships
    ingredient = relationship("Ingredient", back_populates="nutrition")
