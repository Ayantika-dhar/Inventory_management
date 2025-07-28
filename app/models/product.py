from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    sku = Column(String, unique=True)
    image_url = Column(String)
    description = Column(String)
    quantity = Column(Integer)
    price = Column(Float)

