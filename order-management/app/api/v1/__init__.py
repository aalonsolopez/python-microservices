from fastapi import APIRouter
from app.api.v1 import orders

api_router = APIRouter()

api_router.include_router(
    orders.router,
    prefix="/products",
    tags=["products"]
)

__all__ = ["api_router"]