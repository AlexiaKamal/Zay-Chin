from sqlalchemy import Column, String, Integer, Float, ForeignKey, JSON, Boolean, Text
from sqlalchemy.orm import relationship
from backend.app.core.database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(String(32), primary_key=True, index=True) # e.g. "R0001"
    name_mm = Column(String(255), nullable=False, index=True)
    name_en = Column(String(255), nullable=False, index=True)
    description_mm = Column(Text, nullable=True)
    description_en = Column(Text, nullable=True)
    category = Column(String(64), nullable=False, index=True)
    meal_types = Column(JSON, default=list) # e.g. ["lunch", "dinner"]
    servings = Column(Integer, nullable=True, default=4)
    preparation_time_minutes = Column(Integer, nullable=True)
    cooking_time_minutes = Column(Integer, nullable=True)
    
    tags = Column(JSON, default=dict) # dietary, seasonal, festival, main_ingredients
    source_document = Column(String(255), default="ဟင်းချက်နည်းများ.pdf")
    source_pdf_pages = Column(JSON, default=list)
    source_printed_pages = Column(JSON, default=list)
    extraction_method = Column(String(128), default="manual_visual_transcription_from_scanned_spread")
    
    confidence = Column(Float, default=1.0)
    is_verified = Column(Boolean, default=True)

    # Relationships
    ingredients = relationship("RecipeIngredient", back_populates="recipe", cascade="all, delete-orphan", order_by="RecipeIngredient.id")
    instructions = relationship("RecipeInstruction", back_populates="recipe", cascade="all, delete-orphan", order_by="RecipeInstruction.step_number")
    favorites = relationship("Favorite", back_populates="recipe", cascade="all, delete-orphan")


class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(String(32), ForeignKey("recipes.id", ondelete="CASCADE"), nullable=False, index=True)
    ingredient_id = Column(String(32), ForeignKey("ingredients.id", ondelete="RESTRICT"), nullable=False, index=True)
    
    original_name = Column(String(255), nullable=True)
    name_mm = Column(String(255), nullable=False)
    name_en = Column(String(255), nullable=False)
    
    quantity = Column(Float, nullable=True)
    unit = Column(String(64), nullable=False)
    original_quantity_text = Column(String(128), nullable=True)
    
    normalized_quantity = Column(Float, nullable=True)
    normalized_unit = Column(String(32), nullable=True) # g, ml, piece, bunch, sheet, slice, to_taste
    
    preparation_note_mm = Column(String(255), nullable=True)
    preparation_note_en = Column(String(255), nullable=True)

    # Relationships
    recipe = relationship("Recipe", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="recipe_usages")


class RecipeInstruction(Base):
    __tablename__ = "recipe_instructions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(String(32), ForeignKey("recipes.id", ondelete="CASCADE"), nullable=False, index=True)
    step_number = Column(Integer, nullable=False)
    instruction_mm = Column(Text, nullable=False)
    instruction_en = Column(Text, nullable=False)

    recipe = relationship("Recipe", back_populates="instructions")
