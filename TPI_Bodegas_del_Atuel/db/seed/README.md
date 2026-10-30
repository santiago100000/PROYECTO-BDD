# Seed — Carga masiva de datos

## Ejecución con Docker Compose

```bash
docker compose --profile seed run --rm seed
```

El servicio `seed` se conecta como `bodegas_owner` (necesita `DISABLE TRIGGER` en algunas tablas).
Asegurate de que las migraciones `001_esquema.sql` y `007_roles.sql` ya estén aplicadas.

## Ejecución local

```bash
cp ../.env.example .env  # ajustar rutas según sea necesario
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python seed.py --seed 42
```

## Estructura

- `catalogos/`: archivos CSV con datos de referencia (cepas, maridajes, departamentos, etc.)
- `seed.py`: esqueleto con funciones vacías por tabla (TODO)
- `requirements.txt`: dependencias (psycopg[binary], Faker)

## Pendiente

El grupo debe completar cada función `cargar_*` con los INSERT reales, respetando el orden de dependencias definido en `ORDEN_DE_CARGA`.
