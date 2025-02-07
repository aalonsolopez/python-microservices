from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./orders.db"
    PRODUCT_API_URL: str = "http://localhost:8001"

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
