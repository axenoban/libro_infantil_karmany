# Protocolo de agentes — Karmany Monsta libro infantil para colorear

## Fuente prioritaria y estados

1. Verifica estado **real** de GitHub: rama, HEAD y archivos antes de comenzar.
2. Lee `docs/00_DOCUMENTO_MAESTRO.md`, `docs/03_TRAZABILIDAD_CANON.md` y `docs/05_REFERENCIA_VISUAL_CALIDAD.md`.
3. Las **28 láminas** son `propuesta_editorial`; no se han aprobado como extensión definitiva.
4. REF visual aceptada = **barra mínima de calidad del acabado**, no diseños canónicos del niño ni Karmany.
5. El diseño actual evita **lluvia y fondos**, centra a los Karmanys y no baja calidad en páginas sencillas.
6. Sin invenciones canónicas: documentar referencia de cada rasgo o marcar propuesta no canónica pendiente de aprobación.

## Habilidades instaladas en el repositorio

- [Planificar libro infantil](.agents/skills/planificar-libro-infantil/SKILL.md) — plan página por página y progresión.
- [Dirigir ilustraciones para colorear](.agents/skills/dirigir-ilustraciones-colorear/SKILL.md) — arte premium y anatomía legible.
- [QA de libro para colorear](.agents/skills/qa-libro-colorear/SKILL.md) — controles visuales, actividades y PDF Carta.

Antes de ejecutar una etapa, lee la skill correspondiente. Estos son archivos compatibles con herramientas que soportan Agent Skills; **no implican que se haya instalado una extensión global en ChatGPT**.

## Edición y ramas

- `feature/*` = pruebas y propuestas pendientes.
- `dev/karmany-core` = bloques aprobados.
- `main` = publicación.

No hacer force push, no fusionar sin revisión, no adoptar canon de otros proyectos. Los trabajos gráficos individuales necesitan ficha, QA y aprobación explícita.

## Enlaces base

- [Índice propuesto de 28 láminas](docs/06_INDICE_PROPUESTA_28_LAMINAS.md).
- [Plan estructurado en JSON](editorial/plan_paginas.json).
- [Plantilla de ficha por lámina](docs/04_FICHA_LAMINA.md).

## Fase de bestiario previa a P04

Consulta `docs/09_BIBLIA_KARMANYS_LIBRO.md` antes de seleccionar, describir o reutilizar cualquier Karmany. **16 es una preselección, no el reparto aprobado**. Sus formas oficiales no pueden deducirse de los títulos. Para personajes recurrentes crear y aprobar `docs/10_PLANTILLA_MODELO_KARMANY.md` por criatura. Las páginas P01–P03 aprobadas visualmente no tienen identidad de catálogo asignada. No generar P04 hasta cerrar la decisión del elenco.
