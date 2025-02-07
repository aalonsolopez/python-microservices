# Microservicios de Productos y Pedidos

Este repositorio contiene dos microservicios para la gestión de productos y la administración de pedidos:

1. **Product Management (product-management)**  
   - Framework: **FastAPI**  
   - Gestión de productos y stock  
   - Base de datos: **SQLite** (usando **SQLAlchemy**)  
   - Pruebas con **pytest**  
   - Rutas para crear, listar y actualizar productos

2. **Order Management (order-management)**  
   - Framework: **FastAPI**  
   - Creación y seguimiento de pedidos  
   - Validación de datos con **pydantic**  
   - Integración con el microservicio de productos para actualizar su inventario y seguimiento de pedidos
   - Base de datos: **SQLite** (usando **SQLAlchemy**)

> [!IMPORTANT]  
> Debido a falta de tiempo, no me ha sido posible realizar los tests de integración entre ambos microservicios, ni los test unitarios del microservicio de orders.


## Requisitos

- Python 3.12 (ver archivo `.python-version`)
- Dependencias listadas en `pyproject.toml` de cada proyecto

## Configuración

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/aalonsolopez/python-microservices.git
   ```
2. Acceder a cada microservicio (ejemplo: `cd product-management`).
3. Crear y activar el entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
4. Instalar dependencias:
   ```bash
   pip install . # Asegurarse de estar en la carpeta del microservicio y de que la versión de pip sea compatible con archivos .toml
   ```
5. Iniciar la aplicación:
   ```bash
   uvicorn app.main:app --reload
   ```
6. Acceder a la documentación de cada microservicio bajo el endpoint `/redoc` (ejemplo: `http://127.0.0.1:8000/redoc`).

---

## Estructura de Carpetas

```plaintext
python-microservices/
├─ product-management/
│  ├─ app/
│  ├─ tests/
│  └─ pyproject.toml
├─ order-management/
│  ├─ app/
│  └─ pyproject.toml
└─ README.md
```

- **app/**: Código principal (rutas, modelos, etc.)  
- **tests/**: Pruebas unitarias e integradas  
- **pyproject.toml**: Dependencias y configuración del proyecto

## Ejecución de Pruebas

Dentro de cada carpeta:

```bash
pytest
```


