from fastapi import FastAPI
from app.api.v1.orders import router as orders_router
from fastapi.openapi.utils import get_openapi

app = FastAPI()

app.include_router(orders_router, prefix="/api/v1", tags=["orders"])


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Order Management API",
        version="0.1.0",
        summary="This is a documentation for the **Order Management API**",
        description="The documentation of the endpoints and the models of the Order Management API",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi