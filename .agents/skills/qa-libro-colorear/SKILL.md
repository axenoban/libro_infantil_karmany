---
name: qa-libro-colorear
description: Validar páginas infantiles para colorear y PDF Carta, legibilidad, actividad, calidad gráfica y estado canónico.
---

# QA editorial, gráfico y técnico

## Cuándo usar
Antes de aprobar una lámina, combinar páginas, exportar PDF o preparar posible impresión.

## Procedimiento
1. Validar una ficha por página e ID único; confirmar estado `aprobado` si se integra en PDF.
2. Comprobar sin falsos positivos: canon y permisos, instrucciones breves correctas, diversidad de dibujos y actividad solucionable.
3. Revisar escala de grises: dibujo blanco/negro sin sombras que bloqueen la zona coloreable.
4. Revisar sujetos completos, contornos visibles, detalles coloreables y fondo ausente o aprobado.
5. Contrastar con la calidad mínima de `docs/05_REFERENCIA_VISUAL_CALIDAD.md`.
6. Exportar versión de prueba en Carta (215,9 × 279,4 mm); si PNG, verificar resolución real. La referencia operativa de prueba a 300 ppp es 2550 × 3300 px; **no interpolar** una imagen menor para aparentar más calidad.
7. Inspeccionar PDF a zoom 100 %, en miniatura y con impresión a escala si está disponible.
8. Confirmar índices, recuento, páginas, portada aparte y no inclusión de borradores en arte final.
9. Anotar defectos, reabrir revisión y exigir aprobación expresa luego de cambios importantes.

## Salida
Checklist por lámina, incidencias reproducibles, resultado pasa/falla y estado final.
