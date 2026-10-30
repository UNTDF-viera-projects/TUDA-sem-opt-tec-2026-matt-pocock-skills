---
status: accepted
---
# La Reinscripción reactiva la misma Inscripción

Una Reinscripción limpia la Cancelación de la misma inscripción en lugar de crear otra.
Así se conserva la unicidad por alumno y actividad que ya existe, sin tocar el esquema.

## Opciones consideradas

- **Reactivar la misma fila** (elegida): simple y sin migración de restricciones; solo
  se conserva la última Cancelación, no el historial completo de ciclos.
- **Una fila nueva por inscripción**, con unicidad condicional a una sola activa: guarda todo
  el historial, pero obliga a migrar la restricción y a revisar cada cálculo de Cupo.
