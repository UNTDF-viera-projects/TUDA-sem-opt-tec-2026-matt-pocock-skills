# 03: Reinscribirse después de cancelar

**Qué construir:** Tras cancelar, el detalle de la actividad vuelve a ofrecer el formulario; al
enviarlo se hace una Reinscripción que reactiva la misma inscripción (ADR 0001).

**Bloqueado por:** 01

**Estado:** ready-for-agent

- [ ] Con Cupo, actividad habilitada y sin iniciar, la Reinscripción deja una Inscripción activa
- [ ] Sigue habiendo una sola inscripción por alumno y actividad; la Cancelación queda sin fecha
- [ ] Sin Cupo, deshabilitada o iniciada: mismos mensajes que una inscripción nueva; sigue cancelada
- [ ] Con la inscripción activa se sigue respondiendo "ya inscripto"
- [ ] El detalle muestra el formulario tras cancelar y lo oculta tras reinscribirse
- [ ] Se puede cancelar y reinscribirse repetidas veces, sin límite
