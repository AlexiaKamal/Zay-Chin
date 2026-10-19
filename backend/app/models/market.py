from sqlalchemy import Column, String, Float, Boolean, Text
from sqlalchemy.orm import relationship
from backend.app.core.database import Base

class Market(Base):
    __tablename__ = "markets"

    id = Column(String(64), primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    city = Column(String(64), nullable=False, index=True) # Yangon / Mandalay
    market_type = Column(String(64), default="supermarket") # supermarket, wholesale, wet_market, model_estimate
    vendor_name = Column(String(255), nullable=True)
    address = Column(Text, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    has_verified_coordinates = Column(Boolean, default=False)
    source_reference = Column(String(255), nullable=True)

    # Relationships
    prices = relationship("IngredientPrice", back_populates="market_rel")
