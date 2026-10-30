"\"\"Router de salud: GET /salud\"\"\""

from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.dal.base import ping

router = APIRouter(tags=["salud"])


@router.get("/salud")
def salud():
    """Verifica que la API puede conectar con la base de datos.

    Devuelve 200 con {"api":"ok","db":"ok"} si la conexión funciona.
    Si la base no conecta (por ejemplo, mientras 007_roles.sql sea un stub
    y no exista app_rw), responde 503 con un mensaje claro.
    """
    try:
        db_ok = ping()
    except Exception as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Base de datos no disponible: {exc}",
        )
    if not db_ok:
        raise HTTPException(
            status_code=503,
            detail="Base de datos respondió pero SELECT 1 no retornó el valor esperado.",
        )
    return {"api": "ok", "db": "ok"}
