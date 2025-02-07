import requests
import pytest
from app.db import Base
from app.db.session import engine

BASE_URL = "http://localhost:8000/api/v1/products"

@pytest.fixture(scope="session", autouse=True)
def prepare_test():
    Base.metadata.create_all(bind=engine)

    ini

def test_list_products():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_product():
    new_product = {
        "name": "Producto de prueba",
        "price": 10.99,
        "stock": 100
    }
    response = requests.post(BASE_URL, json=new_product)
    assert response.status_code == 201
    assert "id" in response.json()

def test_create_product_without_stock():
    new_product = {
        "name": "Producto sin stock",
        "price": 5.99
    }
    response = requests.post(BASE_URL, json=new_product)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["stock"] == 0

def test_update_stock():
    product_id = 1
    updated_stock = {"stock": 50}
    response = requests.put(f"{BASE_URL}/{product_id}/stock", json=updated_stock)
    assert response.status_code == 200
    assert response.json()["stock"] == 50
