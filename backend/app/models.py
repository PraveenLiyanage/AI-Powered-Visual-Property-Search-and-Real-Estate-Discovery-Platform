from sqlalchemy import Column, Integer, String, Float
from .db import Base

class Property(Base):
    __tablename__ = "properties"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, default="")
    description = Column(String, default="")
    price = Column(Float, nullable=True)
    currency = Column(String, default="USD")
    address = Column(String, default="")
    city = Column(String, default="")
    country = Column(String, default="")
    image_url = Column(String, default="")
