# Wayfinder · SDD · UNTDF 2026

Clase sobre [`/wayfinder`](https://github.com/mattpocock/skills/tree/main/skills/engineering/wayfinder)
(MIT, © Matt Pocock): planificar como un **mapa de tickets de decisión** un esfuerzo que no entra en
una sesión, hasta que el camino al destino queda claro y se entrega a `/to-spec`. Continúa la clase de
`../` (flujo `/grill-with-docs → /to-spec → /to-tickets → /implement → /retro`) con una idea más
grande y difusa: **un chat entre alumnos y docentes** en la demo de inscripciones.

## Presentación

```sh
# desde matt-skills/ (las slides reutilizan ../slides/vendor y el tema de la clase anterior)
python3 -m http.server 8020 --bind 127.0.0.1
# abrir http://localhost:8020/wayfinder/slides/
```

También abre con doble clic en `slides/index.html` si se conserva la carpeta `matt-skills/` completa.
`S` abre las notas del orador. Pensada para ~2 h: 55' de conceptos y caso, 45' en vivo y práctica.

`slides/index.html` se **genera**: editar `slides/index.src.html` y, desde esta carpeta, correr

```sh
python3 slides/build.py
```

El build inyecta el contenido real de los archivos marcados con `data-incluir` (el `SKILL.md` de
`referencias/` y los artefactos de `ejemplo/`).

## Estructura

| Carpeta | Qué hay |
|---|---|
| `slides/` | Deck reveal.js propio + `wayfinder.css`; reutiliza vendor, tema y logos de `../slides/`. |
| `demo/` | Copia de `../demo` tal como terminó la clase anterior (63 pruebas). Punto de partida de la corrida real; ya trae la skill en `.agents/skills/wayfinder` y el tracker local con su sección *Wayfinding operations*. |
| `ejemplo/` | Mapa **simulado** a mitad de camino: transcripciones de dos sesiones, mapa en dos momentos, nueve tickets, research, ADR y glosario. Escrito por el docente, no generado por la herramienta. |
| `referencias/` | Copia literal de `wayfinder/SKILL.md` (MIT, © Matt Pocock) para mostrar en clase. |

## Corrida real en clase

El ejemplo es una estimación: en clase se corre la skill de verdad y el mapa **va a salir distinto**.

1. **Preparar** (antes de clase): copia nueva de `demo/`, `uv sync --locked`, `./scripts/check.sh`.
   Confirmar que el agente ve la skill (`/wayfinder` o "usá la skill wayfinder").
2. **Sesión 1 · cartografiar** (20'): desde la copia,
   `/wayfinder Queremos un chat entre alumnos y docentes en la demo de inscripciones.`
   La clase contesta las rondas de grilling a mano alzada; el agente busca los hechos solo.
   Al final debe quedar `.scratch/<esfuerzo>/map.md`, los tickets en `issues/` y, si hubo research,
   un subagente lanzado. Con tracker local no hace falta empujar la rama `research/<nombre>`.
3. **Vigilar** durante la corrida: que no conteste sus propias preguntas, que no empiece a programar,
   que cablee `Blocked by:` en una segunda pasada y que deje niebla en *Not yet specified*.
4. **Commitear el mapa** en la copia: es el punto de partida común de la práctica.

## Práctica de los alumnos

Cada grupo parte de la copia con el mapa que salió en vivo, abre una sesión **nueva** y corre
`/wayfinder .scratch/<esfuerzo>/map.md` sin nombrar ticket: el agente elige el primero de la frontera
y lo reclama. Lo resuelven según su tipo (si es grilling, las respuestas son del grupo) y revisan qué
cambió en el mapa.

**Entregable:** `map.md` y los tickets tocados, con su comentario de resolución, más una reflexión de
3–5 líneas: qué decidieron distinto al ejemplo y qué pasó a niebla o a fuera de alcance, y por qué.
Si dos grupos reciben el mismo ticket, está bien: las decisiones de cada grupo pueden diferir.
