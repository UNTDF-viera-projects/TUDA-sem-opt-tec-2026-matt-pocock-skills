# Mapa · Conversaciones entre alumno y docente

Labels: wayfinder:map

## Destination

Una spec de **Conversaciones alumno–docente** lista para `/to-spec`: quién habla con quién, cuándo
se abre y se cierra una Conversación, cómo llegan los Mensajes y cómo se ven. Nada construido.

## Notes

- Dominio: demo de inscripciones (`GLOSSARY.md`, `docs/adr/`). Consultar `domain-modeling` en cada sesión.
- Stack fijo: Django 5.2, SQLite con transacciones `IMMEDIATE`, Docker Compose con un solo servicio.
- Preferencia: lo más simple que cumpla; cada dependencia nueva se justifica en un ticket.
- Un ticket por sesión. El mapa se usa en clase: preferir decisiones explicables en 5 minutos.

## Decisions so far

- [Opciones de transporte de mensajes en Django 5.2 con SQLite](issues/02-opciones-de-transporte.md): WebSocket pide ASGI y channel layer; SSE bajo WSGI ocupa un worker por conexión; el polling corre en el stack actual.
- [Quién puede escribir y leer una Conversación](issues/01-quien-puede-escribir-y-leer.md): solo el alumno inscripto (vigente o cancelado) y el responsable actual de la actividad; la abre el alumno.
- [Ciclo de vida de la Conversación frente a la Actividad y la Inscripción](issues/03-ciclo-de-vida.md): abierta desde la inscripción hasta 7 días después del inicio; después, solo lectura.
- [¿Tiempo real o asincrónico?](issues/04-tiempo-real-o-asincronico.md): asincrónico con refresco cada 15 s mientras la Conversación está abierta; sin WebSocket (ADR 0002).

## Not yet specified

- **Moderación.** ¿El docente puede ocultar un Mensaje? ¿Hay que dejar rastro? Depende de cómo se vea
  la Conversación y de si hay no leídos.
- **Cómo se prueba el refresco.** Qué verifica la suite y qué queda para el navegador; espera a que el
  prototipo fije la forma de la pantalla.
- **Límites.** Largo máximo de un Mensaje y frecuencia de envío, si hacen falta.

## Out of scope

- [Anuncios del docente a todos sus inscriptos](issues/07-anuncios-a-todos-los-inscriptos.md): la Conversación es uno a uno; un anuncio es otra funcionalidad.
- Salas grupales y Mensajes entre alumnos.
- Archivos adjuntos, videollamadas, notificaciones por email o push.
