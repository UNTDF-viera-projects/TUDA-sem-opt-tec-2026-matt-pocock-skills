# Opciones de transporte de mensajes en Django 5.2 con SQLite

Type: research
Status: resolved
Blocked by: ninguno

## Question

¿Qué opciones hay para que un Mensaje llegue al otro lado (WebSocket con Channels, Server-Sent
Events, polling) y qué le exige cada una a este stack: servidor ASGI o WSGI, dependencias, servicios
extra en Compose y escrituras concurrentes en SQLite?

## Comments

**Resolución (sesión 1, subagente `research`):** hallazgos en
[research/transporte-de-mensajes.md](../../../research/transporte-de-mensajes.md), en la rama descartable
`research/transporte-de-mensajes`.
