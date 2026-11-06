# Ejemplo ilustrativo: un mapa de wayfinder a mitad de camino
Carpeta **escrita por el docente** con fines didácticos. Simula qué deja `/wayfinder` en el repo
para "un chat entre alumnos y docentes" sobre `../demo`. No es salida de ninguna herramienta: en clase
se corre de verdad y el resultado puede diferir.

```
ejemplo/
├── sesion-1-chart.md              # transcripción: destino + frontera en amplitud
├── sesion-4-ticket-04.md          # transcripción: resolver un ticket de grilling
├── evolucion/map-al-cartografiar.md   # el mapa al terminar la sesión 1
├── .scratch/conversaciones-alumno-docente/
│   ├── map.md                     # el mapa hoy (sesión 5 en curso)
│   └── issues/01 … 09             # tickets de decisión
├── research/transporte-de-mensajes.md # lo que deja el subagente research
├── docs/adr/0002-mensajes-por-polling-sin-websocket.md
└── GLOSSARY.md                    # términos que agregó el mapa
```

## Cómo leerlo
1. **Charting:** `sesion-1-chart.md` y `evolucion/map-al-cartografiar.md`. Destino, siete tickets,
   niebla y fuera de alcance. Ninguna decisión todavía.
2. **Una sesión de trabajo:** `sesion-4-ticket-04.md`. Elegir de la frontera, reclamar, resolver,
   registrar, invalidar un ticket y graduar niebla.
3. **El mapa hoy:** `.scratch/.../map.md`. Comparar con la foto del paso 1.

## Recorrido de los tickets
| Ticket | Tipo | Bloqueado por | Estado |
|---|---|---|---|
| 01 Quién puede escribir y leer | grilling | — | resuelto (s2) |
| 02 Opciones de transporte | research | — | resuelto (s1, subagente) |
| 03 Ciclo de vida | grilling | 01 | resuelto (s3) |
| 04 ¿Tiempo real o asincrónico? | grilling | 02 | resuelto (s4) → ADR 0002 |
| 05 Cómo se ve una Conversación | prototype | 03, 04 | **frontera** |
| 06 Medir Channels en Compose | task | 04 | invalidado por 04 |
| 07 Anuncios a todos los inscriptos | grilling | 01 | fuera de alcance (s2) |
| 08 Conversaciones al reiniciar la demo | grilling | — | **frontera** (graduado en s3) |
| 09 Mensajes no leídos | grilling | — | reclamado (graduado en s4) |

Cuando la frontera quede vacía y no quede niebla, el mapa **no construye**: se pasa a `/to-spec`,
que junta las decisiones enlazadas en una spec, y de ahí `/to-tickets` e `/implement` como siempre.
