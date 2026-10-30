# Inscripciones

Contexto de la demo: los alumnos se inscriben a actividades con cupo limitado y pueden cancelar.

## Language

**Actividad**:
Evento con fecha de inicio y cupo, que puede estar habilitado o deshabilitado.

**Cupo**:
Cantidad máxima de inscripciones activas que admite una actividad.
_Avoid_: capacidad, plaza, vacante

**Inscripción**:
Vínculo entre un alumno y una actividad. Hay uno solo por par y no se borra.
_Avoid_: reserva, registro

**Inscripción activa**:
Inscripción que no está cancelada; es la única que ocupa un cupo.

**Titular**:
El alumno a nombre de quien está una inscripción; solo él puede cancelarla.
_Avoid_: dueño, usuario, estudiante

**Cancelación**:
Acto del titular que marca la inscripción como cancelada, con su fecha, y libera un cupo.
_Avoid_: baja, borrado, desinscripción

**Plazo de cancelación**:
Hasta 24 horas antes del inicio de la actividad, inclusive.

**Reinscripción**:
Inscripción del titular a una actividad que había cancelado; vuelve a ser activa la misma.
_Avoid_: nueva inscripción, reactivación

## Ambigüedades resueltas

- "Baja" se usaba para borrar y para cancelar: nada se borra, se dice **Cancelación**.
- "Inscripción" nombraba el vínculo y el cupo ocupado: solo la **Inscripción activa** ocupa cupo.
