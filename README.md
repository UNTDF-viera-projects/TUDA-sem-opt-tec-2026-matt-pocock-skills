# Skills de Matt Pocock · SDD · UNTDF 2026

Clase sobre el flujo de trabajo con agentes que propone Matt Pocock
([mattpocock/skills](https://github.com/mattpocock/skills), MIT · [aihero.dev/skills](https://www.aihero.dev/skills)):
`/grill-with-docs → /to-spec → /to-tickets → /implement (tdd + code-review) → /retro`, aplicado a la
demo de inscripciones con la idea de **cancelar una inscripción y volver a inscribirse**.

## Presentación

```sh
# desde esta carpeta
python3 -m http.server 8020 --bind 127.0.0.1
# abrir http://localhost:8020/slides/
```

También abre directo con doble clic en `slides/index.html` (todo es local, sin Internet).
Teclas de reveal.js: flechas para avanzar, `S` abre las notas del orador, `Esc` la vista general,
`F` pantalla completa. Pensada para ~2 h: 50' de flujo y conceptos, 15' de caso, 45' de práctica.

`slides/index.html` se **genera**: editar `slides/index.src.html` y correr

```sh
python3 slides/build.py
```

El build inyecta el contenido real de los archivos marcados con `data-incluir` (los `SKILL.md`
de `referencias/skills/` y los artefactos de `ejemplo/`), así las slides siempre muestran lo mismo
que el repo.

## Estructura

| Carpeta | Qué hay |
|---|---|
| `slides/` | Deck reveal.js 6 (vendorizado) con el tema UNTDF de la clase de Docker + `matt.css`. |
| `ejemplo/` | Artefactos ilustrativos que el flujo deja en el repo: `AGENTS.md`, `GLOSSARY.md`, ADR, transcripción de grilling, spec y 5 tickets en `.scratch/`. Escritos por el docente, no generados por la herramienta. |
| `referencias/skills/` | Copia literal de `grilling`, `grill-with-docs` e `implement` (MIT, © Matt Pocock) para mostrarlas en clase. |

## Práctica de los alumnos

Parten de una copia nueva de `../demo-inscripciones` (base sin cancelación). La consigna completa está
en las slides de la sección 7; el ejemplo docente de referencia está en `ejemplo/`. Las decisiones
del grill son de cada grupo: pueden diferir del ejemplo.
