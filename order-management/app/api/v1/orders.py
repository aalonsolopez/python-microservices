from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
import requests

from app.db.session import get_db
from app.core.config import settings
from app.models.order import Order
from app.models.order_item import OrderItem
from app.schemas.order import OrderCreate, OrderOutput, OrderItem as OrderItemSchema

router = APIRouter()

@router.post("/orders", response_model=OrderOutput)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    total_price = 0.0
    order_items_data = []
    
    for item in order.items:
        response = requests.get(f"{settings.PRODUCT_API_URL}/products/{item.product_id}")
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail=f"Product {item.product_id} not found")
        product = response.json()
        if product["stock"] < item.quantity:
            raise HTTPException(status_code=400, detail=f"Insufficient stock for product {item.product_id}")
        patch_resp = requests.patch(
            f"{settings.PRODUCT_API_URL}/products/{item.product_id}",
            json={"stock": product["stock"] - item.quantity}
        )
        if patch_resp.status_code != 200:
            raise HTTPException(status_code=400, detail=f"Failed to update stock for product {item.product_id}")
        order_items_data.append({
            "product_id": item.product_id,
            "quantity": item.quantity,
            "price": product["price"]
        })
        total_price += product["price"] * item.quantity

    db_order = Order(title=order.title, description=order.description)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    for item_data in order_items_data:
        db_item = OrderItem(order_id=db_order.id,
                            product_id=item_data["product_id"],
                            quantity=item_data["quantity"],
                            price=item_data["price"])
        db.add(db_item)
    db.commit()

    db_order = db.query(Order).filter(Order.id == db_order.id).first()
    output = OrderOutput(
        id=db_order.id,
        title=db_order.title,
        description=db_order.description,
        items=[OrderItemSchema(product_id=oi.product_id, quantity=oi.quantity, price=oi.price) for oi in db_order.order_items],
        total_price=total_price
    )
    return output

@router.get("/orders", response_model=List[OrderOutput])
def list_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).all()
    result = []
    for order in orders:
        total_price = sum([item.price * item.quantity for item in order.order_items])
        result.append(OrderOutput(
            id=order.id,
            title=order.title,
            description=order.description,
            items=[OrderItemSchema(product_id=oi.product_id, quantity=oi.quantity, price=oi.price) for oi in order.order_items],
            total_price=total_price
        ))
    return result
