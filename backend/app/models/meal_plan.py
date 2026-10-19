from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app.core.database import Base

class MealPlan(Base):
    __tablename__ = "meal_plans"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=True) # Nullable for guest/local plans
    plan_name = Column(String(255), default="My Weekly Meal Plan")
    city = Column(String(64), default="Yangon")
    household_size = Column(Integer, default=1)
    target_budget_mmk = Column(Float, nullable=True)
    estimated_total_cost_mmk = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="meal_plans")
    items = relationship("MealPlanItem", back_populates="meal_plan", cascade="all, delete-orphan", order_by="MealPlanItem.day_of_week, MealPlanItem.meal_type")
    grocery_lists = relationship("GroceryList", back_populates="meal_plan")


class MealPlanItem(Base):
    __tablename__ = "meal_plan_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    meal_plan_id = Column(Integer, ForeignKey("meal_plans.id", ondelete="CASCADE"), nullable=False, index=True)
    recipe_id = Column(String(32), ForeignKey("recipes.id", ondelete="CASCADE"), nullable=False, index=True)
    
    day_of_week = Column(Integer, nullable=False) # 1=Monday, ..., 7=Sunday
    meal_type = Column(String(32), nullable=False) # breakfast, lunch, dinner
    servings = Column(Integer, default=1)
    estimated_cost_mmk = Column(Float, nullable=True)

    meal_plan = relationship("MealPlan", back_populates="items")
    recipe = relationship("Recipe")
