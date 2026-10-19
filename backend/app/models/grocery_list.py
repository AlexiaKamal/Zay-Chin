from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app.core.database import Base

class GroceryList(Base):
    __tablename__ = "grocery_lists"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    meal_plan_id = Column(Integer, ForeignKey("meal_plans.id", ondelete="SET NULL"), nullable=True)
    city = Column(String(64), default="Yangon")
    created_at = Column(DateTime, default=datetime.utcnow)
    estimated_total_mmk = Column(Float, default=0.0)

    # Relationships
    user = relationship("User", back_populates="grocery_lists")
    meal_plan = relationship("MealPlan", back_populates="grocery_lists")
    items = relationship("GroceryListItem", back_populates="grocery_list", cascade="all, delete-orphan", order_by="GroceryListItem.category, GroceryListItem.ingredient_name_en")


class GroceryListItem(Base):
    __tablename__ = "grocery_list_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    grocery_list_id = Column(Integer, ForeignKey("grocery_lists.id", ondelete="CASCADE"), nullable=False, index=True)
    ingredient_id = Column(String(32), ForeignKey("ingredients.id", ondelete="RESTRICT"), nullable=False, index=True)
    
    ingredient_name_mm = Column(String(255), nullable=False)
    ingredient_name_en = Column(String(255), nullable=False)
    category = Column(String(64), default="produce")
    
    quantity = Column(Float, nullable=False)
    unit = Column(String(32), nullable=False) # g, ml, piece, etc.
    
    estimated_price_mmk = Column(Float, nullable=True)
    is_price_available = Column(Boolean, default=True)
    price_observation_date = Column(String(32), nullable=True)
    price_source_name = Column(String(255), nullable=True)
    
    is_purchased = Column(Boolean, default=False)
    notes = Column(String(255), nullable=True)

    grocery_list = relationship("GroceryList", back_populates="items")
    ingredient = relationship("Ingredient")
