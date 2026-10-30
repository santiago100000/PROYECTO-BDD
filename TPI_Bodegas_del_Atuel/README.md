# Bodegas del Atuel — TPI Integrador de Bases de Datos (UTN FRSR)

Gestión y distribución de una empresa vitivinícola. Repositorio con el andamiaje inicial (scaffolding) del Trabajo Práctico Integrador.

## Integrantes y roles

| Integrante | Rol | GitHub |
|---|---|---|
| Placeholder | Desarrollador API | @usuario |
| Placeholder | Modelado y DDL | @usuario |
| Placeholder | Frontend y pruebas | @usuario |
| Placeholder | Datos y catálogos | @usuario |

## Requisitos

- Docker y Docker Compose
- (Opcional) Python 3.12 + psycopg 3 para pruebas locales de la API
- (Opcional) psql cliente para ejecutar pruebas SQL

## Cómo levantar

```bash
cp .env.example .env
# Editar .env con credenciales reales (nunca commitear .env)
docker compose up --build
```

- `db` (PostgreSQL 16): puerto 5432 solo en 127.0.0.1
- `migrate`: aplica migraciones en orden y termina
- `api`: FastAPI en http://localhost:8000 (docs en /docs)
- `front`: nginx en http://localhost:8080

## Cómo correr el seed

```bash
docker compose --profile seed run --rm seed
```

El seed se conecta como `bodegas_owner` y necesita `DISABLE TRIGVER`. Requiere que las migraciones 001 y 007 ya estén aplicadas.

## Cómo correr las pruebas SQL (base)

```bash
docker compose exec db psql -U bodegas_owner -d bodegas -f /tests/db_tests.sql
```

## Cómo correr las pruebas de la API

```bash
docker compose exec api pytest -v
```

## URLs locales

- API: http://localhost:8000
- Swagger/OpenAPI: http://localhost:8000/docs
- Front: http://localhost:8080

## Tabla de hitos

- [ ] H1 Modelado (DER, esquema relacional, diccionario y DDL base)
- [ ] H2 Integridad y lógica en la base (constraints, funciones, procedimientos, triggers, vistas, roles y pruebas SQL)
- [ ] H3 Carga masiva (scripts reproducibles y reporte de conteos y tiempos)
- [ ] H4 Índices y rendimiento (informe con planes antes y después)
- [ ] H5 Consultas SQL (INSERT, UPDATE, DELETE y SELECT comentadas)
- [ ] H6 API (REST funcionando en local con Docker Compose)
- [ ] H7 Front (conectado a la API)
- [ ] H8 Nube (URL pública, backup y restauración probados)
- [ ] H9 Documentación y defensa (informe final, README, demo y defensa oral)

## Decisiones

1. **ORM/query builder**: se usa driver nativo psycopg 3 sin ORM ni query builders (requisito del TP).
2. **Cálculos en API/front**: la API y el front NO calculan totales, descuentos ni stock. Esa lógica vive exclusivamente en la base de datos (funciones, procedimientos y triggers).
3. **Migraciones repetibles**: el servicio `migrate` registra cada archivo aplicado en `ops.schema_migrations` y salta los ya aplicados.
4. **Stub de SQL**: todos los archivos `.sql` de migraciones y consultas contienen únicamente comentarios y TODO. El grupo debe escribirlos a mano.
5. **Base de datos vacía inicial**: los .sql stubs deben ejecutarse sin error sobre una base vacía.

## Despliegue en la nube

TODO: proveedor elegido, configuración de seguridad, backup y restauración.
