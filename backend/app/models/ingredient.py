from sqlalchemy import Column, String, JSON
from sqlalchemy.orm import relationship
from backend.app.core.database import Base

class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(String(32), primary_key=True, index=True) # e.g. "I0001"
    name_mm = Column(String(255), nullable=False, index=True)
    name_en = Column(String(255), nullable=False, index=True)
    aliases_mm = Column(JSON, default=list)
    aliases_en = Column(JSON, default=list)
    category = Column(String(64), nullable=False, index=True)
    default_unit = Column(String(32), nullable=False, default="g")

    # Relationships
    nutrition = relationship("IngredientNutrition", back_populates="ingredient", uselist=False, cascade="all, delete-orphan")
    prices = relationship("IngredientPrice", back_populates="ingredient", cascade="all, delete-orphan")
    recipe_usages = relationship("RecipeIngredient", back_populates="ingredient")
