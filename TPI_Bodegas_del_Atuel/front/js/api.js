"\"\"Único lugar que llama a la API. Devuelve los mensajes de error tal cual los manda la API.\"\"\""

async function getSalud() {
  const response = await fetch(`${API_BASE_URL}/salud`);
  if (!response.ok) {
    const body = await response.json().catch(() => ({}));
    throw new Error(body.detail || `Error ${response.status} al consultar /salud`);
  }
  return response.json();
}

window.api = { getSalud };
