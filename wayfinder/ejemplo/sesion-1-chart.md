# Sesión 1 · Chart the map (simulada)

> /wayfinder Queremos un chat entre alumnos y docentes en la demo de inscripciones.

🔎 **Hechos** (relevados por el agente, no son preguntas): una actividad tiene un único responsable
staff (`Activity.responsible`); la inscripción cancelada se conserva (`Registration.cancelled_at`,
ADR 0001); no hay Channels ni ASGI en `pyproject.toml` ni en `config/`.

## Paso 1 · Nombrar el destino (grilling + domain-modeling)

❓ **Q1** - **Tipo de destino**: ¿El mapa termina en una spec lista para `/to-spec`, sin construir nada?

➡️ Sí: construir queda fuera del mapa.

---

❓ **Q2** - **Quién habla con quién**: ¿Es una conversación privada entre un alumno y el docente
responsable de una actividad, anclada a esa actividad?

➡️ Sí: el código ya tiene ese vínculo.

---

❓ **Q3** - **Nombre en el dominio**: ¿Adoptamos **Conversación** y **Mensaje**, y evitamos "chat"?

➡️ Sí.

---

❓ **Q4** - **¿"Chat" implica tiempo real?**: ¿Lo dejamos abierto como decisión del mapa?

➡️ Sí: es la decisión técnica más cara.

**Respuestas:** Q1 sí. Q2 sí. Q3 sí. Q4 sí.

📍 Destino escrito en el mapa.

## Paso 2 · Mapear la frontera (grilling en amplitud)

Propongo estos frentes. Para cada uno: ¿es una pregunta que ya se puede escribir con precisión
(ticket), algo que todavía no se ve (niebla) o algo fuera del destino?

❓ **Q5** - **Acceso**: ¿Quién puede abrir y leer una Conversación? → ¿Ticket de grilling, sin bloqueos?

➡️ Sí.

---

❓ **Q6** - **Transporte**: ¿Investigamos WebSocket, SSE y polling contra este stack? → ¿Ticket de research?

➡️ Sí: es un hecho que busca el agente, no una decisión.

---

❓ **Q7** - **Tiempo real**: ¿La decisión producto-técnica queda como ticket bloqueado por la investigación?

➡️ Sí.

---

❓ **Q8** - **Medir Channels**: ¿Agregamos una tarea para levantar Daphne + Channels + Redis en Compose y
medir el costo antes de decidir?

➡️ Sí, bloqueada por "¿Tiempo real o asincrónico?".

---

❓ **Q9** - **Anuncios**: ¿El docente puede escribir a todos sus inscriptos a la vez? ¿Lo ticketeamos?

➡️ Sí, como grilling bloqueado por acceso.

---

❓ **Q10** - **No leídos, reinicio de la demo, moderación, pruebas, límites**: ¿Quedan en niebla porque
dependen de acceso, ciclo de vida o transporte?

➡️ Sí: todavía no se pueden escribir con precisión.

---

❓ **Q11** - **Grupos, adjuntos, videollamadas, email**: ¿Fuera de alcance?

➡️ Sí.

**Respuestas:** todas sí. Q9: "no estoy seguro de que entre, pero ticketealo y lo vemos".

## Resultado

- `map.md` creado: ver [evolucion/map-al-cartografiar.md](evolucion/map-al-cartografiar.md).
- Siete tickets creados; segunda pasada para cablear `Blocked by:` con números reales.
- Frontera: "Quién puede escribir y leer" y "Opciones de transporte". Los otros cinco esperan a alguno de ellos.
- Subagente `research` lanzado para "Opciones de transporte de mensajes" (resuelto en esta misma sesión:
  la excepción de la regla de un ticket por sesión).
- Fin de la sesión: charting no resuelve tickets a mano.
