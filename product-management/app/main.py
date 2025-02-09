from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.api.v1 import api_router

app = FastAPI(title="Product Management API")

app.include_router(api_router, prefix="/api/v1")



def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Product Management API",
        version="0.1.0",
        summary="This is the documentation for the **Product Management API**",
        description="The documentation of the endpoints and the models of the Product Management API",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
