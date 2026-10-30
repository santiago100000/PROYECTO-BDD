"\"\"Aplicación FastAPI de Bodegas del Atuel.\"\"\""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.errors import instalar_handler
from app.routers import health

# Routers mínimos (endpoints como TODO según el PDF):
# - Vinos: GET /vinos, GET /vinos/{cod}, POST /vinos, PUT /vinos/{cod}, DELETE /vinos/{cod}
# - Clientes: CRUD sobre /clientes
# - Comprobantes: POST /comprobantes, GET /comprobantes/{nro}
# - Transferencias: POST /transferencias, POST /transferencias/{nro}/renglones, POST /transferencias/{nro}/terminar, POST /transferencias/{nro}/procesar
# - Ingresos: POST /ingresos, POST /ingresos/{cod}/renglones, POST /ingresos/{cod}/procesar
# - Reportes (solo lectura): GET /reportes/top-vinos, /reportes/ventas-por-sala, /reportes/vinos-sin-stock, /reportes/transportista-activo, /reportes/trazabilidad/{cod}

app = FastAPI(title="Bodegas del Atuel API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

instalar_handler(app)

app.include_router(health.router)

# TODO (grupo): incluir routers de vinos, clientes, comprobantes, transferencias, ingresos y reportes.
# Ejemplo: app.include_router(vinos.router, prefix="/vinos")


@app.get("/")
def root():
    return {"service": "bodegas-del-atuel-api", "status": "running"}
