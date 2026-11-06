# Mapa · Conversaciones entre alumno y docente

<!-- Foto del mapa al terminar la sesión 1 (chart the map). Compararla con
     ../.scratch/conversaciones-alumno-docente/map.md, que es el mismo mapa después de la sesión 4. -->

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

<!-- vacío: charting no resuelve tickets -->

## Not yet specified

- **Mensajes no leídos y avisos.** Si el alumno o el docente se enteran de un Mensaje nuevo y dónde.
  Depende de cómo se entregan los Mensajes.
- **Qué pasa con las Conversaciones al reiniciar la demo.** `seed_demo` y `--reset` borran
  inscripciones; no sabemos todavía a qué está atada una Conversación.
- **Moderación.** ¿El docente puede ocultar un Mensaje? ¿Hay que dejar rastro?
- **Cómo se prueba.** Depende del transporte: no es lo mismo testear polling que WebSocket.
- **Límites.** Largo máximo de un Mensaje y frecuencia de envío, si hacen falta.

## Out of scope

- Salas grupales y Mensajes entre alumnos.
- Archivos adjuntos, videollamadas, notificaciones por email o push.
