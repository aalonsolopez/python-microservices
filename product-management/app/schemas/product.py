from decimal import Decimal
from typing import Optional
from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: Decimal
    stock: Optional[int] = 0

class ProductUpdate(BaseModel):
    stock: int

class ProductResponse(BaseModel):
    id: int
    name: str
    price: Decimal
    stock: int
    
    class Config:
        from_attributes = True