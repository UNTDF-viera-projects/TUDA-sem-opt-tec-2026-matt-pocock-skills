# Sesión 4 · Work through the map (simulada)

> /wayfinder .scratch/conversaciones-alumno-docente/map.md

1. **Cargar el mapa**, no cada ticket: Destination, Notes, Decisions so far, niebla.
2. **Elegir el ticket.** Frontera (abiertos, sin bloqueo, sin reclamar):
   "¿Tiempo real o asincrónico?" y "Conversaciones al reiniciar la demo". Gana el primero por número.
   "Cómo se ve una Conversación" y "Medir Channels" siguen bloqueados por él.
3. **Reclamarlo**: `Status: claimed` **antes** de trabajar, para que otra sesión lo saltee.
4. **Resolver como grilling** (lo dice `Type:`, no el cuerpo), con zoom a "Opciones de transporte".

🔎 **Hechos** (del research, no son preguntas): WebSocket pide ASGI y Redis con más de un proceso;
SSE bajo WSGI retiene un worker por pantalla; el polling corre con lo que hay.

❓ **Q1** - **¿Al instante?**: Una Conversación con un docente no es un soporte en vivo. ¿Alcanza con que
un Mensaje aparezca en hasta unos segundos, sin WebSocket?

➡️ Sí: evita ASGI, Redis y un segundo servicio.

---

❓ **Q2** - **¿Cada cuánto?**: ¿Refrescamos cada 15 s y solo con la Conversación abierta?

➡️ Sí: carga despreciable para SQLite.

---

❓ **Q3** - **¿Se registra?**: Es difícil de revertir y alguien va a preguntar "¿por qué no WebSocket?".
¿Escribimos una ADR?

➡️ Sí.

**Respuestas:** Q1 sí. Q2 sí. Q3 sí.

5. **Registrar la resolución**: comentario de resolución en el ticket, `Status: resolved`, y una línea en
   _Decisions so far_ del mapa (el gist y el link, nunca el detalle).
6. **Actualizar el mapa**:
   - 📄 ADR `0002-mensajes-por-polling-sin-websocket`.
   - ✂️ "Medir Daphne + Channels + Redis" queda **invalidado**: se cierra sin ejecutar.
   - 🌫️→🎫 La niebla "Mensajes no leídos y avisos" ya se puede escribir con precisión: se gradúa al
     ticket "Mensajes no leídos: qué cuenta y dónde se avisa" y se borra de _Not yet specified_.
   - 🌫️ "Cómo se prueba" se reescribe: ya no depende del transporte, depende de la forma de la pantalla.

Fin de la sesión: un ticket resuelto. El próximo lo elige la próxima sesión, no el humano.
