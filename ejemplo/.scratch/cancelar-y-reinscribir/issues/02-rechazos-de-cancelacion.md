# 02: Rechazos de cancelación

**Qué construir:** Los casos en que cancelar no procede: fuera del Plazo de cancelación, ajena o
inexistente (respuesta genérica) y repetida (idempotente). Una actividad deshabilitada sí cancela.

**Bloqueado por:** 01

**Estado:** ready-for-agent

- [ ] Con menos de 24 h para el inicio se rechaza con un mensaje claro y sigue activa
- [ ] Una inscripción ajena y una inexistente reciben exactamente la misma respuesta genérica
- [ ] Cancelar otra vez conserva la fecha original y no libera un segundo Cupo
- [ ] La repetición es idempotente incluso fuera de plazo
- [ ] Una actividad deshabilitada se cancela si se cumple el plazo
- [ ] Sin sesión autenticada se redirige al login y no se cancela nada
- [ ] Cada rechazo deja datos y Cupo sin cambios
