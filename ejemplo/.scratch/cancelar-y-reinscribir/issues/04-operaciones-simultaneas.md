# 04: Dos operaciones simultáneas

**Qué construir:** El sistema se mantiene coherente con cancelaciones concurrentes y con una
Reinscripción que compite contra otra inscripción por el último Cupo.

**Bloqueado por:** 02, 03

**Estado:** ready-for-agent

- [ ] Dos cancelaciones simultáneas de la misma inscripción producen una sola transición
- [ ] Esas dos cancelaciones liberan exactamente un Cupo
- [ ] Con un solo Cupo libre, una Reinscripción y una inscripción ajena simultáneas: gana una
- [ ] La que pierde recibe "sin cupos" y no modifica datos
- [ ] Nunca hay más Inscripciones activas que el Cupo
- [ ] Ante contención de la base se responde "ocupada" sin modificar datos
- [ ] Un test reproduce la concurrencia con conexiones separadas
