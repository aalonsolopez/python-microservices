from app.db.session import SessionLocal, engine
from app.db import Base
from app.models.product import Product

def init_db():
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()

    productos = [
        Product(name="Producto A", price=19.99, stock=100),
        Product(name="Producto B", price=29.99, stock=50),
        Product(name="Producto C", price=9.99, stock=200),
    ]
    
    for producto in productos:
        db.add(producto)
    
    db.commit()
    db.close()
    print("Base de datos generada y poblada con datos de ejemplo.")

if __name__ == "__main__":
    init_db()