# Karmany Monsta — Libro infantil para colorear

Proyecto editorial independiente para producir un **libro digital en PDF** con dibujos infantiles para colorear, personajes humanos infantiles y Karmanys adaptados a una estética adorable de fantasía.

**Estado:** bases editoriales v0.4 registradas; primera ilustración y canon visual **pendientes de aprobación**. No hay láminas aprobadas todavía.

## Documentación de referencia

- [Documento maestro v0.4](docs/00_DOCUMENTO_MAESTRO.md): decisiones D01–D22, objetivos, alcance y pendientes.
- [Guía visual y de maquetación](docs/01_GUIA_VISUAL.md): criterios del line art y del diseño infantil.
- [Plan de prototipo y validación](docs/02_PLAN_PROTOTIPO.md): fases, pruebas y criterios de aceptación.
- [Protocolo de fuentes y canon](docs/03_TRAZABILIDAD_CANON.md): origen y aprobación de personajes/Karmanys.
- [Ficha de ilustración](docs/04_FICHA_LAMINA.md): plantilla obligatoria por arte.
- [Organización de recursos](assets/README.md): archivos y estados de aprobación.

## Acuerdos principales

- Público infantil mixto; dificultad de ilustraciones **progresiva**.
- Libro para **colorear y realizar actividades simples**; primera lámina, **solo colorear**.
- Estilo **infantil adorable** como adaptación exclusiva, todavía sin diseño definitivo aprobado.
- Combinación de escenas de personajes humanos, Karmanys y ambos. Los protagonistas humanos del libro serán **niños**; apariencia, identidad y vínculos por definir.
- Primera prueba: **escena mixta**, ambiente de **lluvia suave y charcos**, fondo contextual moderado y composición casi a página completa.
- Cada página llevará **título breve e instrucción corta**.
- Lienzo de trabajo **Carta vertical, 8,5 × 11 pulgadas (21,59 × 27,94 cm)**; el formato final para imprenta sigue abierto.
- Entrega **PDF digital**, concebida para permitir posible impresión futura.
- Extensión del libro y número de páginas del prototipo: se decidirán **tras la primera ilustración**.
- Producción: validar **una lámina inicial**, luego trabajar en **lotes de 2–3**.
- Portada: presentar **2–3 enfoques visuales** antes de seleccionar uno.

## Principios de seguridad editorial

Los documentos y referencias de otros proyectos Karmany no se convierten automáticamente en canon de este libro. No se inventan nombres, especies, poderes, relaciones ni apariencias canónicas. Toda nueva decisión visual debe marcarse como **adaptación editorial pendiente/aprobada**.

## Estrategia de ramas

- `main`: versiones publicables.
- `dev/karmany-core`: última base editorial/producción validada.
- `feature/*`: cambios pendientes de aprobación.

Las pruebas visuales se desarrollarán fuera de `main`; no se integrarán sin revisión explícita del creador.

> Actualizado: 2026-11-15. Documento maestro: v0.4.
