# 05: Admin y seed respetan las cancelaciones

**Qué construir:** El docente ve y filtra las cancelaciones en el admin, y los datos de demo
incluyen una inscripción cancelada sin romper el cálculo de Cupo.

**Bloqueado por:** 01

**Estado:** ready-for-agent

- [ ] El admin lista la fecha de Cancelación y permite filtrar canceladas y activas
- [ ] La fecha de Cancelación es de solo lectura; sigue sin poder agregar ni borrar inscripciones
- [ ] Bajar el Cupo de una actividad por debajo de sus Inscripciones activas se rechaza
- [ ] Las inscripciones canceladas no cuentan en esa validación
- [ ] El seed incluye una inscripción cancelada y reiniciar la demo la reproduce igual
