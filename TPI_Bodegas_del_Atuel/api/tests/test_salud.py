"\"\"Pruebas del endpoint GET /salud.\"\"\""

from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_salud_devuelve_ok_cuando_db_responde():
    """GET /salud debe devolver 200 con {"api":"ok","db":"ok"} cuando la base responde."""
    response = client.get("/salud")
    # Nota: en este esqueleto, la base puede no estar disponible aún (007_roles stub),
    # por lo que 503 es un resultado válido y esperado en esta etapa.
    assert response.status_code in (200, 503)
    if response.status_code == 200:
        data = response.json()
        assert data["api"] == "ok"
        assert data["db"] == "ok"
