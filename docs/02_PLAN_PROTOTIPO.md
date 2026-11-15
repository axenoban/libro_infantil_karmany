# Plan de prototipo, aprobación y regresión visual

## Estado

**No hay ilustraciones aprobadas.** La primera escena mixta será una **prueba de estilo**, no una versión publicada.

## Etapa A — Preparación de la primera lámina

1. Confirmar que las decisiones D01–D22 están registradas.
2. Elegir niño(s) humano(s) protagonista(s) y Karmany(s) llamativo(s) y adorable(s); sus identidades y apariencias **siguen abiertas**.
3. Reunir referencias visuales aprobadas o declarar que el arte será una **propuesta nueva editorial NO CANÓNICA**.
4. Dibujar la escena mixta con **lluvia suave y charcos**, figuras predominantes, fondo moderado y actividad exclusivamente de colorear.
5. Proponer título e instrucción corta para revisión.
6. Entregar imagen individual y ficha con versión, procedencia y estado de aprobación.

## Etapa B — Prueba local y criterio de aceptación

**Control visual:** verificar tamaño de página, legibilidad de siluetas, simplicidad, limpieza de trazado, rasgos coherentes, fondo subordinado y líneas aptas para colorear.

**Control editorial:** ninguna atribución canónica inventada; texto correcto; condición de propuesta explícita.

**Control técnico propuesto:**
- Comprobar proporción Carta 8,5 × 11 pulgadas y exportación PNG/PDF.
- Inspeccionar al 100 % y en previsualización reducida.
- Imprimir una hoja de prueba a escala real si hay impresora; verificar que ninguna línea desaparezca ni queden elementos cortados.
- Comprobar que el PDF mantiene el tamaño físico de página y contornos sin pixelación excesiva.

**Aceptar únicamente si** el creador confirma visualmente la lámina y los controles editoriales/técnicos están superados. Las correcciones no equivalen a una aprobación automática.

## Etapa C — Producción iterativa

Después de aprobar la primera ilustración:

1. Confirmar número de páginas del prototipo.
2. Producir un **lote de 2–3** composiciones, variando complejidad con criterio.
3. Realizar QA por lámina y una revisión conjunta de consistencia.
4. Registrar aprobación/revisión en las fichas.
5. Repetir hasta el volumen aprobado.
6. Probar 2–3 enfoques visuales para la portada en una fase editorial específica.

## Estados obligatorios

`idea` → `boceto` → `en_revision` → `aprobado` → `integrado_en_pdf`

Una corrección significativa vuelve a `en_revision`. Ningún archivo en `idea`, `boceto` o `en_revision` debe publicarse como definitivo.

## Contrato de ramas

- `feature/*`: arte nuevo, adaptaciones y pruebas sin validación.
- `dev/karmany-core`: solo contenido previamente aprobado.
- `main`: entregables finales publicables.
- No hacer merges ciegos, `force push` ni sobrescritura de historia. Integrar por PR tras revisión.

## Decisiones aplazadas intencionalmente

Longitud final, número de láminas del prototipo, selección de protagonistas, canon visual aprobado, contenido exacto de actividades, portada, sangrado y especificaciones de imprenta.
