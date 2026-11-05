# ¿Tiempo real o asincrónico?

Type: grilling
Status: resolved
Blocked by: 02

## Question

Con los hallazgos de "Opciones de transporte de mensajes", ¿los Mensajes tienen que aparecer al
instante (WebSocket o SSE) o alcanza con que aparezcan al recargar o refrescar cada tanto (polling)?

## Comments

**Resolución (sesión 4):**

- **Asincrónico.** La pantalla de la Conversación pide Mensajes nuevos **cada 15 segundos** mientras
  está abierta; fuera de ella no hay refresco.
- Sin WebSocket ni SSE en esta versión: no se agrega ASGI, Redis ni un segundo servicio en Compose.
- Un Mensaje es una escritura más en SQLite, dentro de la misma disciplina de transacciones.
- ADR creada: [0002-mensajes-por-polling-sin-websocket](../../../docs/adr/0002-mensajes-por-polling-sin-websocket.md).
- Invalida "Medir Daphne + Channels + Redis en el Compose": cerrado sin ejecutar.
- Gradúa "Mensajes no leídos: qué cuenta y dónde se avisa" desde la niebla.
