# Karmany Monsta — Libro infantil para colorear

Proyecto editorial independiente para producir un **libro digital en PDF** con dibujos infantiles para colorear, personajes humanos infantiles y Karmanys adaptados a una estética adorable de fantasía.

**Estado:** estructura editorial base de **28 láminas aprobada** por el creador (2026-11-15). La calidad visual de REF-ART-01 es la referencia mínima; diseños canónicos, láminas individuales y PDF final siguen pendientes de aprobación. No hay láminas publicables aprobadas todavía.

## Documentación de referencia

- [Documento maestro v0.4](docs/00_DOCUMENTO_MAESTRO.md): decisiones D01–D22, objetivos, alcance y pendientes.
- [Guía visual y de maquetación](docs/01_GUIA_VISUAL.md): criterios del line art y del diseño infantil.
- [Plan de prototipo y validación](docs/02_PLAN_PROTOTIPO.md): fases, pruebas y criterios de aceptación.
- [Protocolo de fuentes y canon](docs/03_TRAZABILIDAD_CANON.md): origen y aprobación de personajes/Karmanys.
- [Ficha de ilustración](docs/04_FICHA_LAMINA.md): plantilla obligatoria por arte.
- [Referencia visual mínima de calidad](docs/05_REFERENCIA_VISUAL_CALIDAD.md): acabado profesional, sin fondo, Karmany protagonista.
- [Índice base aprobado de 28 láminas](docs/06_INDICE_PROPUESTA_28_LAMINAS.md): títulos, objetivos, actividades y niveles como base editorial aprobada; textos específicos y elenco aún revisables.
- [Plan de páginas estructurado](editorial/plan_paginas.json): datos individuales en JSON para continuidad editorial.
- [Habilidades locales del proyecto](.agents/skills/): planificación, ilustración y control de calidad; son archivos de instrucciones y no implican instalación global en ChatGPT.
- [Organización de recursos](assets/README.md): archivos y estados de aprobación.

## Acuerdos principales

- Público infantil mixto; dificultad de ilustraciones **progresiva**.
- Libro para **colorear y realizar actividades simples**; primera lámina, **solo colorear**.
- Estilo **infantil adorable** como adaptación exclusiva, todavía sin diseño definitivo aprobado.
- Combinación de escenas de personajes humanos, Karmanys y ambos. Los protagonistas humanos del libro serán **niños**; apariencia, identidad y vínculos por definir.
- Dirección visual más reciente: **sin lluvia ni fondos** por ahora; escena mixta y Karmany protagonista, tomando la última muestra de aventura infantil como referencia de **acabado mínimo**. La idea anterior de lluvia se conserva como historial, pero quedó superada.
- Cada página llevará **título breve e instrucción corta**.
- Lienzo de trabajo **Carta vertical, 8,5 × 11 pulgadas (21,59 × 27,94 cm)**; el formato final para imprenta sigue abierto.
- Entrega **PDF digital**, concebida para permitir posible impresión futura.
- **28 láminas interiores aprobadas como estructura base**; portada, créditos y demás páginas editoriales se definirán aparte. El número de páginas del prototipo continúa pendiente. El número de páginas del primer prototipo continúa pendiente.
- Producción: validar **una lámina inicial**, luego trabajar en **lotes de 2–3**.
- Portada: presentar **2–3 enfoques visuales** antes de seleccionar uno.

## Principios de seguridad editorial

Los documentos y referencias de otros proyectos Karmany no se convierten automáticamente en canon de este libro. No se inventan nombres, especies, poderes, relaciones ni apariencias canónicas. Toda nueva decisión visual debe marcarse como **adaptación editorial pendiente/aprobada**.

## Estrategia de ramas

- `main`: versiones publicables.
- `dev/karmany-core`: última base editorial/producción validada.
- `feature/*`: cambios pendientes de aprobación.

Las pruebas visuales se desarrollarán fuera de `main`; no se integrarán sin revisión explícita del creador.

> Actualizado: 2026-11-15. Documento maestro: v0.5.

## Inicio de la producción secuencial

**D27 — 2026-11-15:** aprobado el índice base de **28 láminas** (8 iniciales, 10 intermedias y 10 avanzadas; 6 incluyen actividades). **No** implica que estén aprobadas las ilustraciones, criaturas específicas, composiciones finales o textos exactos.

**Procedimiento obligatorio:** generar **P01**, presentar para revisión; solo con aprobación explícita guardar archivo y ficha como aprobados en `dev/karmany-core`; después generar P02. No preparar un lote completo sin aprobar las páginas anteriores.
