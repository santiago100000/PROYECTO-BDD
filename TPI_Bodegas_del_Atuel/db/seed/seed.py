"""Esqueleto del script de carga masiva (seed) para Bodegas del Atuel.

Este archivo NO inserta datos todavía. Contiene solo la estructura:
- argparse con --seed (default desde variable de entorno SEED)
- random.seed y Faker.seed fijos para reproducibilidad
- conexión como owner desde variables de entorno
- helper para medir tiempos
- una función vacía por tabla en orden de dependencias (con TODO)

El grupo debe completar cada función con los INSERT reales.
"""

from __future__ import annotations

import argparse
import os
import random
import time
from typing import Callable

from faker import Faker
import psycopg


def get_seed() -> int:
    """Obtiene la semilla del argumento --seed o de la variable de entorno SEED."""
    parser = argparse.ArgumentParser(description="Carga masiva de catálogos y datos de prueba")
    parser.add_argument("--seed", type=int, default=None, help="Semilla aleatoria (default: env SEED)")
    args = parser.parse_args()
    if args.seed is not None:
        return args.seed
    env_seed = os.getenv("SEED", "42")
    try:
        return int(env_seed)
    except ValueError:
        return 42


SEED = get_seed()
random.seed(SEED)
Faker.seed(SEED)
fake = Faker("es_AR")


def get_conn() -> psycopg.Connection:
    """Conecta como owner (bodegas_owner) usando variables de entorno."""
    conn = psycopg.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "5432")),
        dbname=os.getenv("DB_NAME", "bodegas"),
        user=os.getenv("DB_USER", "bodegas_owner"),
        password=os.getenv("DB_PASSWORD", ""),
    )
    return conn


def medir_tiempo(nombre: str, func: Callable[[], None]) -> None:
    """Ejecuta func y imprime el tiempo transcurrido."""
    inicio = time.perf_counter()
    func()
    fin = time.perf_counter()
    print(f"[seed] {nombre}: {fin - inicio:.4f} segundos")


def cargar_localidades(conn: psycopg.Connection) -> None:
    """Carga localidades.csv (solo encabezado por ahora; el grupo completa CP reales)."""
    # TODO (grupo): leer catalogos/localidades.csv e insertar
    pass


def cargar_cepas(conn: psycopg.Connection) -> None:
    """Carga cepas.csv."""
    # TODO (grupo): leer catalogos/cepas.csv e insertar
    pass


def cargar_maridajes(conn: psycopg.Connection) -> None:
    """Carga maridajes.csv."""
    # TODO (grupo): leer catalogos/maridajes.csv e insertar
    pass


def cargar_departamentos(conn: psycopg.Connection) -> None:
    """Carga departamentos_mendoza.csv."""
    # TODO (grupo): leer catalogos/departamentos_mendoza.csv e insertar
    pass


def cargar_tipos_vino(conn: psycopg.Connection) -> None:
    """Carga tipos_vino.csv."""
    # TODO (grupo): leer catalogos/tipos_vino.csv e insertar
    pass


def cargar_presentaciones(conn: psycopg.Connection) -> None:
    """Carga presentaciones_ml.csv."""
    # TODO (grupo): leer catalogos/presentaciones_ml.csv e insertar
    pass


def cargar_bodegas(conn: psycopg.Connection) -> None:
    """Inserta bodegas (con Faker o datos inventados)."""
    # TODO (grupo): INSERT en bodega
    pass


def cargar_fincas(conn: psycopg.Connection) -> None:
    """Inserta fincas."""
    # TODO (grupo): INSERT en finca
    pass


def cargar_parcelas(conn: psycopg.Connection) -> None:
    """Inserta parcelas (entidad débil: finca + nro parcela)."""
    # TODO (grupo): INSERT en parcela
    pass


def cargar_lotes(conn: psycopg.Connection) -> None:
    """Inserta lotes de uva (una cosecha por parcela y campaña)."""
    # TODO (grupo): INSERT en lote_de_uva
    pass


def cargar_analisis_calidad(conn: psycopg.Connection) -> None:
    """Inserta análisis de calidad por lote."""
    # TODO (grupo): INSERT en analisis_calidad
    pass


def cargar_vinos(conn: psycopg.Connection) -> None:
    """Inserta vinos con composición de cepas."""
    # TODO (grupo): INSERT en vino y composicion_vino_cepa
    pass


def cargar_clientes(conn: psycopg.Connection) -> None:
    """Inserta clientes (socio, distribuidor, exportador)."""
    # TODO (grupo): INSERT en cliente y subtipos
    pass


def cargar_permisos_exportacion(conn: psycopg.Connection) -> None:
    """Inserta permisos de exportación."""
    # TODO (grupo): INSERT en permiso_exportacion
    pass


def cargar_transportistas(conn: psycopg.Connection) -> None:
    """Inserta transportistas y cobertura de localidades."""
    # TODO (grupo): INSERT en transportista y transportista_cubre_localidad
    pass


def cargar_salas(conn: psycopg.Connection) -> None:
    """Inserta salas de venta y empleados."""
    # TODO (grupo): INSERT en sala_venta y empleado
    pass


def cargar_stock_deposito(conn: psycopg.Connection) -> None:
    """Inserta stock inicial en depósito central."""
    # TODO (grupo): INSERT en stock_deposito
    pass


def cargar_stock_salas(conn: psycopg.Connection) -> None:
    """Inserta stock inicial por sala."""
    # TODO (grupo): INSERT en stock_sala
    pass


def cargar_ingresos(conn: psycopg.Connection) -> None:
    """Inserta ingresos y renglones de ingreso."""
    # TODO (grupo): INSERT en ingreso y renglon_ingreso
    pass


def cargar_transferencias(conn: psycopg.Connection) -> None:
    """Inserta transferencias y renglones de transferencia."""
    # TODO (grupo): INSERT en transferencia y renglon_transferencia
    pass


def cargar_comprobantes(conn: psycopg.Connection) -> None:
    """Inserta comprobantes y renglones de comprobante."""
    # TODO (grupo): INSERT en comprobante y renglon_comprobante
    pass


def cargar_auditoria_precio(conn: psycopg.Connection) -> None:
    """Inserta auditoría de precios (completada normalmente por trigger)."""
    # TODO (grupo): INSERT inicial en auditoria_precio (opcional)
    pass


ORDEN_DE_CARGA: list[tuple[str, Callable[[psycopg.Connection], None]]] = [
    ("localidades", cargar_localidades),
    ("cepas", cargar_cepas),
    ("maridajes", cargar_maridajes),
    ("departamentos", cargar_departamentos),
    ("tipos_vino", cargar_tipos_vino),
    ("presentaciones", cargar_presentaciones),
    ("bodegas", cargar_bodegas),
    ("fincas", cargar_fincas),
    ("parcelas", cargar_parcelas),
    ("lotes", cargar_lotes),
    ("analisis_calidad", cargar_analisis_calidad),
    ("vinos", cargar_vinos),
    ("clientes", cargar_clientes),
    ("permisos_exportacion", cargar_permisos_exportacion),
    ("transportistas", cargar_transportistas),
    ("salas", cargar_salas),
    ("stock_deposito", cargar_stock_deposito),
    ("stock_salas", cargar_stock_salas),
    ("ingresos", cargar_ingresos),
    ("transferencias", cargar_transferencias),
    ("comprobantes", cargar_comprobantes),
    ("auditoria_precio", cargar_auditoria_precio),
]


def main() -> None:
    print(f"[seed] Usando semilla SEED={SEED}")
    conn = get_conn()
    try:
        for nombre, func in ORDEN_DE_CARGA:
            medir_tiempo(nombre, lambda: func(conn))
        conn.commit()
        print("[seed] Carga masiva completada (todo en stubs por ahora).")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
