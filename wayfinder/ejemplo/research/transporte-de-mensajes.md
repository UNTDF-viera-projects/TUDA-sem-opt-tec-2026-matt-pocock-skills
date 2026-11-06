# Transporte de mensajes en Django 5.2 con SQLite

> Ticket: Opciones de transporte de mensajes en Django 5.2 con SQLite (`02-opciones-de-transporte.md`).
> Rama descartable `research/transporte-de-mensajes`: se empuja, nunca se mergea.
> **Simulado para la clase**: en la corrida real lo escribe un subagente con la skill `research`.

## Pregunta

¿Qué le exige a este stack cada forma de entregar Mensajes?

## Hallazgos

| Opción | Servidor | Dependencias y servicios | Riesgo con SQLite |
|---|---|---|---|
| **WebSocket** (Django Channels) | ASGI (Daphne o Uvicorn) | `channels`; un channel layer. La capa en memoria es para tests o desarrollo y no cruza procesos; la única capa oficial para producción usa Redis (`channels_redis`), un servicio más en Compose | Bajo: las escrituras siguen siendo una por Mensaje |
| **Server-Sent Events** | ASGI recomendado | Ninguna extra. Una respuesta en streaming por cliente; bajo WSGI cada respuesta retiene un worker mientras dura | Medio: si se consulta la base en loop por conexión, se multiplican las lecturas |
| **Polling** | WSGI actual | Ninguna | Bajo: una lectura por intervalo y por pantalla abierta |

- SQLite admite muchos lectores pero **un solo escritor a la vez**; la demo ya serializa escrituras con
  transacciones `IMMEDIATE`. Un Mensaje es una escritura corta más.
- La demo corre hoy con `runserver` (WSGI) en un único servicio de Compose.

## Fuentes primarias

- Django Channels, *Channel Layers*: https://channels.readthedocs.io/en/latest/topics/channel_layers.html
- Django 5.2, *StreamingHttpResponse objects*: https://docs.djangoproject.com/en/5.2/ref/request-response/#streaminghttpresponse-objects
- Django 5.2, *How to deploy with ASGI*: https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
- SQLite, *Appropriate Uses For SQLite*: https://www.sqlite.org/whentouse.html

## Lo que no decide

Si hace falta tiempo real: eso es una decisión de producto ("¿Tiempo real o asincrónico?"), no un hecho.
