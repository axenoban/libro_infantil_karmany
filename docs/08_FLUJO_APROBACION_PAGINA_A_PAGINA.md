# Flujo de láminas P01–P28 — secuencia de aprobación

**D27 (2026-11-15):** estructura base de 28 interiores aprobada. La ilustración final de cada página se aprueba **por separado**.

## Protocolo obligatorio

1. Leer `editorial/plan_paginas.json` y la ficha de la **primera página pendiente**.
2. Confirmar rasgos canónicos autorizados. Si faltan, generar únicamente **concepto editorial no canónico** claramente identificado.
3. Crear propuesta en rama `feature/pNN-*`, con referencia de calidad `docs/05_REFERENCIA_VISUAL_CALIDAD.md`.
4. Presentar la imagen en el chat para aprobación o cambios. **No cambiar estado a aprobado sin autorización explícita.**
5. Una vez aprobada, documentar: versión, identificador de generación, dimensiones reales, QA, fuente gráfica y resultado; guardar **archivo gráfico real** en `assets/laminas/` y ficha.
6. Verificar que el archivo binario descargable está realmente en GitHub y que la rama/commit son correctos.
7. Integrar a `dev/karmany-core` solo el bloque aprobado (fast-forward si la historia lo permite), sin tocar `main`.
8. **Solo entonces generar la próxima página.**

No usar un enlace a la imagen de la conversación como sustituto de guardar sus bytes. No se considera exportable a 300 ppp una imagen que no tenga la resolución real suficiente. Si la herramienta usada no permite escribir el binario a GitHub, avisar y no afirmar que está guardado.

## Estados individuales

`pendiente` → `propuesta` → `en_revision` → `aprobado` → `en_dev` → `en_pdf_final`

Si la imagen cambia sustancialmente después de aprobarse, volver a `en_revision` y requerir nueva aprobación.

## P01: ficha de producción inicial

- **ID:** P01.
- **Título provisional:** ¡Hola, Karmany!
- **Instrucción provisional:** Colorea a este Karmany.
- **Nivel:** inicial.
- **Contenido:** un Karmany grande, de cuerpo completo, expresión alegre, sin fondo.
- **Actividad:** solo colorear.
- **Estilo:** line art premium infantil, calidad de REF-ART-01.
- **Identidad:** no definida; si se diseña criatura original, **adaptación editorial NO CANÓNICA**.
- **Estado:** `pendiente`, hasta recibir la primera propuesta y revisión.
