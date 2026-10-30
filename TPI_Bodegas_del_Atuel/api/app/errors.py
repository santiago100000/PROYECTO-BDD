"\"\"Handler central que traduce SQLSTATE de PostgreSQL a códigos HTTP.\"\"\""

from __future__ import annotations

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import psycopg


SQLSTATE_TO_HTTP: dict[str, tuple[int, str]] = {
    "23505": (409, "Conflicto: valor único violado."),
    "23503": (409, "Conflicto: clave foránea violada."),
    "23514": (422, "Entidad no procesable: CHECK violado."),
    "23502": (422, "Entidad no procesable: NOT NULL violado."),
    "P0001": (409, "Conflicto: regla de negocio rechazada."),
    "22P02": (400, "Solicitud incorrecta: formato de texto inválido."),
    "40001": (503, "Servicio no disponible: fallo de serialización. Reintentar."),
    "40P01": (503, "Servicio no disponible: deadlock detectado. Reintentar."),
}


def traduccion_error(mensaje: str, sqlstate: str | None) -> tuple[int, str]:
    """Devuelve (status_code, detalle) dado un mensaje y un SQLSTATE."""
    if sqlstate and sqlstate in SQLSTATE_TO_HTTP:
        status, detalle_base = SQLSTATE_TO_HTTP[sqlstate]
        # Si es P0001, usar el mensaje de la regla (trigger/procedimiento)
        if sqlstate == "P0001" and mensaje:
            return status, mensaje
        return status, f"{detalle_base} ({mensaje})" if mensaje else detalle_base
    return 500, f"Error interno de base de datos: {mensaje}"


def instalar_handler(app: FastAPI) -> None:
    """Registra el handler de excepciones de psycopg en la aplicación FastAPI."""

    @app.exception_handler(psycopg.Error)
    async def handle_db_error(request: Request, exc: psycopg.Error):
        sqlstate = getattr(exc, "sqlstate", None)
        mensaje = str(exc)
        status, detalle = traduccion_error(mensaje, sqlstate)
        return JSONResponse(status_code=status, content={"detail": detalle})
