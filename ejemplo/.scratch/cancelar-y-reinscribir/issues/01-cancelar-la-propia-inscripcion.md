# 01: Cancelar la propia inscripción dentro del plazo

**Qué construir:** El Titular abre una confirmación desde "Mis inscripciones", confirma por POST
y su inscripción queda cancelada, con fecha, y libera un Cupo. Corte vertical de punta a punta.

**Bloqueado por:** Ninguno (puede empezar de inmediato)

**Estado:** ready-for-agent

- [ ] Una Inscripción activa ofrece "Cancelar", que lleva a una confirmación; el GET no cancela
- [ ] Confirmar por POST con sesión y CSRF válidos cancela y vuelve a "Mis inscripciones" con aviso
- [ ] "Mis inscripciones" muestra "Cancelada" y ya no ofrece cancelar
- [ ] Se acepta cancelar hasta 24 h antes del inicio, inclusive; en el límite exacto sí
- [ ] El Cupo disponible sube exactamente uno en catálogo y detalle
- [ ] Las inscripciones previas al cambio siguen siendo activas
- [ ] Tests de servicio y de vistas cubren lo anterior
