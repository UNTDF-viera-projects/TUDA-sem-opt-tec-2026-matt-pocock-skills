# Ejemplo ilustrativo: artefactos del workflow de skills
Carpeta **escrita por el docente** con fines didácticos. Muestra qué dejaría en el repo el
workflow (grill-with-docs → to-spec → to-tickets → tdd → code-review → retro) para una
funcionalidad de la demo de inscripciones. No es salida de ninguna herramienta.

```
ejemplo/
├── AGENTS.md                      # bloque "Agent skills" (setup)
├── GLOSSARY.md                    # lenguaje del dominio
├── grilling.md                    # extracto de la entrevista
├── docs/
│   ├── agents/{issue-tracker,domain}.md
│   └── adr/0001-reinscripcion-reactiva-la-misma-inscripcion.md
└── .scratch/cancelar-y-reinscribir/
    ├── spec.md
    └── issues/01 … 05
```

## Orden de aparición
1. **Setup:** `AGENTS.md` y `docs/agents/` dicen dónde viven tickets y glosario.
2. **Grilling:** `grilling.md`, dos rondas de preguntas con recomendación.
3. **Docs vivos:** `GLOSSARY.md` y la ADR se actualizan durante el grilling.
4. **Spec:** `spec.md` sintetiza lo acordado, sin entrevistar de nuevo.
5. **Tickets:** cinco cortes verticales (01 → 02, 03, 05; 02 y 03 → 04).
Tdd, code-review y retro actúan sobre el código y no se muestran acá.
