from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.app.core.database import get_db
import backend.app.models as models

router = APIRouter(prefix="/markets", tags=["Markets"])

@router.get("")
def list_markets(city: Optional[str] = Query(None), db: Session = Depends(get_db)):
    query = db.query(models.Market)
    if city:
        query = query.filter(models.Market.city == city)
    markets = query.all()

    result = []
    for m in markets:
        # Count available price observations
        obs_count = db.query(models.IngredientPrice).filter(
            (models.IngredientPrice.market_id == m.id) | (models.IngredientPrice.market_name == m.name)
        ).count()
        
        result.append({
            "id": m.id,
            "name": m.name,
            "city": m.city,
            "market_type": m.market_type,
            "vendor_name": m.vendor_name,
            "address": m.address,
            "latitude": m.latitude,
            "longitude": m.longitude,
            "has_verified_coordinates": m.has_verified_coordinates,
            "source_reference": m.source_reference,
            "recorded_price_observations_count": obs_count
        })
    return result
