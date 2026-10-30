"\"\"Conexión a PostgreSQL con psycopg_pool (abierta de forma lazy) y contexto de transacción.\"\"\""

from __future__ import annotations

from contextlib import contextmanager
from typing import Generator

from psycopg_pool import ConnectionPool

from app.config import settings

_pool: ConnectionPool | None = None


def get_pool() -> ConnectionPool:
    """Devuelve el pool de conexiones, creándolo la primera vez (lazy)."""
    global _pool
    if _pool is None:
        conninfo = (
            f"host={settings.DB_HOST} port={settings.DB_PORT} "
            f"dbname={settings.DB_NAME} user={settings.DB_USER} "
            f"password={settings.DB_PASSWORD}"
        )
        _pool = ConnectionPool(conninfo=conninfo, open=False)
        _pool.open()
    return _pool


@contextmanager
def transaccion() -> Generator:
    """Context manager de transacción con BEGIN/COMMIT/ROLLBACK explícitos.

    Uso:
        with transaccion() as cur:
            cur.execute("INSERT ...")
            cur.execute("UPDATE ...")
    # Si no hay excepción, se hace COMMIT. Si hay excepción, ROLLBACK.
    """
    pool = get_pool()
    conn = pool.getconn()
    try:
        cur = conn.cursor()
        try:
            cur.execute("BEGIN")
            yield cur
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            cur.close()
    finally:
        pool.putconn(conn)
