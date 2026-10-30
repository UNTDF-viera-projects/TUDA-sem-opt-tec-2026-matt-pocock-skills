# Issue tracker: Markdown local

Las specs y los tickets de este repo son archivos markdown dentro de `.scratch/`.

## Convenciones

- Una funcionalidad por carpeta: `.scratch/<slug-de-la-funcionalidad>/`
- La spec es `spec.md`; cada ticket es `issues/<NN>-<slug>.md`, numerado desde `01`
- Nunca un único archivo con todos los tickets
- El estado va en una línea `**Estado:**` cerca del inicio (ej.: `ready-for-agent`)
- Los bloqueos van en `**Bloqueado por:**`; un ticket está libre si sus bloqueos están resueltos
- Los comentarios se agregan al final, bajo `## Comments`

## Cuando una skill dice "publicar en el tracker"

Crear el archivo en `.scratch/<slug>/`, creando la carpeta si falta.

## Cuando dice "traer el ticket"

Leer el archivo indicado (la ruta o el número que pase quien usa la skill).
