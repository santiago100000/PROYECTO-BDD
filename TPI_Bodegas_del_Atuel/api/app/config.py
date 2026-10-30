"""Configuración de la API a partir de variables de entorno.

Ningún secreto se escribe acá: todos los valores vienen de os.getenv().
"""

import os


class Settings:
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", "5432"))
    DB_NAME: str = os.getenv("DB_NAME", "bodegas")
    DB_USER: str = os.getenv("DB_USER", "app_rw")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    CORS_ORIGINS: list[str] = [
        o.strip() for o in os.getenv("CORS_ORIGINS", "http://localhost:8080").split(",") if o.strip()
    ]


settings = Settings()
