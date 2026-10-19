from sqlalchemy import Column, String, Float, ForeignKey, JSON, Date, DateTime
from sqlalchemy.orm import relationship
from backend.app.core.database import Base

class IngredientPrice(Base):
    __tablename__ = "ingredient_prices"

    id = Column(String(32), primary_key=True, index=True) # e.g. "P000001"
    ingredient_id = Column(String(32), ForeignKey("ingredients.id", ondelete="CASCADE"), nullable=False, index=True)
    city = Column(String(64), nullable=False, index=True) # Yangon / Mandalay
    market_name = Column(String(255), nullable=True, index=True)
    market_id = Column(String(64), ForeignKey("markets.id", ondelete="SET NULL"), nullable=True)
    vendor_name = Column(String(255), nullable=True)
    product_name = Column(String(255), nullable=True)
    brand = Column(String(128), nullable=True)
    
    price_mmk = Column(Float, nullable=False)
    original_quantity = Column(Float, nullable=True)
    original_unit = Column(String(64), nullable=True)
    normalized_price_mmk_per_kg = Column(Float, nullable=True) # Null for discrete units
    
    price_type = Column(String(32), default="retail") # retail, wholesale, estimate
    observation_type = Column(String(64), nullable=True)
    observed_date = Column(String(32), nullable=True, index=True)
    collected_at = Column(String(64), nullable=True)
    
    source_name = Column(String(255), nullable=True)
    source_url = Column(String(512), nullable=True)
    source_record_id = Column(String(128), nullable=True)
    availability_status = Column(String(32), default="available")
    verification_status = Column(String(32), default="verified")
    review_notes = Column(JSON, default=list)

    # Relationships
    ingredient = relationship("Ingredient", back_populates="prices")
    market_rel = relationship("Market", back_populates="prices")
