---
status: accepted
---
# Los Mensajes se refrescan por polling, sin WebSocket

La pantalla de una Conversación pide Mensajes nuevos cada 15 segundos mientras está abierta. No se
agrega ASGI, Channels ni Redis: la demo sigue siendo un único servicio WSGI con SQLite.

## Opciones consideradas

- **Polling cada 15 s** (elegida): funciona con el stack actual y se prueba con la suite de siempre;
  un Mensaje puede tardar hasta 15 s en aparecer.
- **WebSocket con Channels**: Mensajes al instante, pero exige servidor ASGI, channel layer con Redis y
  un segundo servicio en Compose.
- **Server-Sent Events**: sin dependencias nuevas, pero bajo WSGI cada pantalla abierta retiene un worker.

## Consecuencias

Si más adelante hace falta tiempo real, es un esfuerzo nuevo con su propio mapa, no un ajuste.
