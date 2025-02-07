from pydantic import BaseModel
from typing import List, Optional

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    items: List[OrderItemCreate]

class OrderItem(BaseModel):
    product_id: int
    quantity: int
    price: float

    class Config:
        orm_mode = True

class OrderOutput(BaseModel):
    id: int
    title: Optional[str]
    description: Optional[str]
    items: List[OrderItem]
    total_price: float

    class Config:
        orm_mode = True
