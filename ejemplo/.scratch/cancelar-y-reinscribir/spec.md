# Cancelar una inscripción y volver a inscribirse

**Estado:** ready-for-agent

## Problem Statement

Hoy una inscripción no se puede deshacer: ocupa un Cupo hasta el final y nadie más lo usa.
Tampoco hay forma de volver a inscribirse si el alumno cambia de opinión.

## Solution

El Titular cancela desde "Mis inscripciones", con una confirmación previa. La inscripción queda
marcada como cancelada y libera su Cupo. Después puede hacer una Reinscripción.

## User Stories

1. Como titular, quiero cancelar mi inscripción, para liberar mi Cupo si no puedo asistir.
2. Como titular, quiero una confirmación previa, para no cancelar por error.
3. Como titular, quiero ver la inscripción como "Cancelada", para tener constancia.
4. Como titular, quiero cancelar hasta 24 h antes del inicio, inclusive, con una regla clara.
5. Como titular, quiero un mensaje claro si estoy fuera del Plazo de cancelación, para entender.
6. Como titular, quiero que repetir la Cancelación no cambie nada, por si hago doble clic.
7. Como titular, quiero cancelar aunque la actividad se haya deshabilitado, para no quedar atado.
8. Como titular, quiero hacer una Reinscripción si hay Cupo y la actividad sigue abierta.
9. Como alumno, quiero que nadie cancele mi inscripción ni sepa si existe, por privacidad.
10. Como alumno, quiero ver el Cupo liberado en el catálogo, para poder inscribirme.
11. Como docente, quiero que dos cancelaciones simultáneas liberen un solo Cupo.
12. Como docente, quiero ver las cancelaciones en el admin y en los datos de demo.

## Implementation Decisions

- Una Inscripción tiene una fecha de Cancelación, vacía mientras es Inscripción activa. Las
  existentes quedan activas. La unicidad por alumno y actividad no cambia (ver ADR 0001).
- El Cupo y la disponibilidad cuentan solo Inscripciones activas, también en la validación
  de capacidad del admin.
- Nuevo servicio de cancelación con el mismo estilo que la inscripción: códigos de resultado,
  mensajes y un instante "ahora" inyectable. Orden de decisión: no es el Titular o no existe
  (respuesta genérica), ya cancelada (idempotente), fuera de plazo y, si no, cancelar.
- La Reinscripción extiende el servicio de inscripción: si la fila está cancelada y se cumplen
  las reglas habituales, limpia la fecha de Cancelación; si está activa, "ya inscripto".
- Cancelar y reinscribir corren en la misma transacción protegida que la inscripción actual.
- Interfaz: página de confirmación (GET), ejecución por POST con sesión y CSRF; "Mis inscripciones"
  distingue Confirmada de Cancelada y el detalle vuelve a ofrecer el formulario tras cancelar.

## Testing Decisions

- Un buen test comprueba comportamiento observable (resultado, estado, cupo), no detalles internos.
- Costuras: las funciones del servicio (reglas, tiempo, idempotencia) y las vistas HTTP con el
  cliente de pruebas de Django (confirmación, POST, CSRF, respuesta genérica).
- Antecedentes: las pruebas de inscripción de la app de actividades, incluidas las de concurrencia.

## Out of Scope

- Límites anti-abuso de ciclos de cancelar y reinscribirse.
- Notificaciones, lista de espera y reembolsos.

## Further Notes

Las reglas de Cancelación son las de la clase anterior (F1). Vocabulario: `GLOSSARY.md`.
