from sqlalchemy import Column, String, Boolean, Text
from backend.app.core.database import Base

class DataSource(Base):
    __tablename__ = "data_sources"

    source_id = Column(String(32), primary_key=True, index=True) # e.g. "SRC01"
    organization = Column(String(255), nullable=False)
    website_url = Column(String(512), nullable=False)
    dataset_or_api_name = Column(String(255), nullable=False)
    data_type = Column(String(64), nullable=False)
    geographic_coverage = Column(String(255), nullable=False)
    date_accessed = Column(String(32), nullable=False)
    publication_or_observation_date = Column(String(32), nullable=True)
    license_or_terms_of_use = Column(Text, nullable=False)
    redistribution_permitted = Column(Boolean, default=True)
    automated_collection_permitted = Column(Boolean, default=True)
    attribution_requirements = Column(Text, nullable=False)
    known_limitations = Column(Text, nullable=True)
