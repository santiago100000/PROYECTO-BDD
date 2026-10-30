"\"\"Capa de acceso a datos (DAL): una función por consulta.

Por ahora solo contiene ping(). El grupo debe agregar una función por consulta/endpoint.
\"\"\""

from __future__ import annotations

from app.db import transaccion


def ping() -> bool:
    """Ejecuta SELECT 1 para verificar conectividad con la base de datos."""
    with transaccion() as cur:
        cur.execute("SELECT 1")
        result = cur.fetchone()
    return result is not None and result[0] == 1
