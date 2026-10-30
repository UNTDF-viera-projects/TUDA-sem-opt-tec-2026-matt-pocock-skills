# Grilling (extracto) · cancelar y volver a inscribirse

## Ronda 1: la cancelación

❓ **Q1** - **¿Borra o marca?**: ¿Cancelar deja la inscripción marcada con su fecha de
cancelación, en vez de borrarla?

➡️ Sí: se marca. Queda constancia y la fila no se pierde.

---

❓ **Q2** - **¿Quién puede?**: ¿Solo el titular puede cancelar su inscripción?

➡️ Sí. Una ajena o inexistente recibe la misma respuesta genérica.

---

❓ **Q3** - **¿Hasta cuándo?**: ¿Se puede cancelar hasta el momento del inicio de la actividad?

➡️ Sí: es la regla más simple de explicar.

---

❓ **Q4** - **¿Libera cupo?**: ¿Cancelar libera exactamente un cupo, y repetir la
cancelación no libera otro?

➡️ Sí: el cupo se cuenta solo con inscripciones activas.

**Respuestas:** Q1 sí. Q2 sí. Q3 no: hasta 24 h antes, inclusive. Q4 sí.

📝 GLOSSARY.md actualizado: Cancelación, Plazo de cancelación

## Ronda 2: la frontera avanzó (reinscripción)

🔎 **Hecho** (lo busqué en el código, no es una pregunta): la inscripción ya tiene una
restricción de unicidad por alumno y actividad. No pueden coexistir dos filas del par.

❓ **Q5** - **¿Mismas reglas?**: ¿La Reinscripción exige lo mismo que una inscripción
nueva (cupo disponible, actividad habilitada, no iniciada)?

➡️ Sí: ninguna regla especial para quien ya había cancelado.

---

❓ **Q6** - **¿Reactivar o fila nueva?**: Dado el hecho, ¿la Reinscripción reactiva la misma
inscripción (borra su cancelación) en vez de crear una fila nueva?

➡️ Sí: no toca la unicidad. La alternativa pide una restricción condicional y migración.

---

❓ **Q7** - **¿Cuántos ciclos?**: ¿No hay límite de cancelar y reinscribirse en esta versión?

➡️ Sí: los límites anti-abuso quedan fuera de alcance.

**Respuestas:** Q5 sí. Q6 sí. Q7 sí.

📝 GLOSSARY.md actualizado: Cancelación, Reinscripción
📄 ADR creada: 0001-reinscripcion-reactiva-la-misma-inscripcion
