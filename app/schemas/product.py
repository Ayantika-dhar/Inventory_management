from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    type: str
    sku: str
    image_url: str
    description: str
    quantity: int
    price: float

class ProductCreate(ProductBase):
    pass

class ProductQuantityUpdate(BaseModel):
    quantity: int

class ProductUpdate(BaseModel):
    quantity: int


class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True

