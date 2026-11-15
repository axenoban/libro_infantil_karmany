# Biblia visual de Karmanys para libro infantil — v0.1

**Estado: ESQUEMA PARA APROBACIÓN; sin criaturas canónicas nuevas aprobadas.**  
**Bloqueante actual:** no generar P04 ni asignar nombres oficiales a P01–P03 hasta aprobar elenco y fichas de apariencia.

## 1. Alcance y autoridad

La estructura de **28 láminas interiores** ya está aprobada. El libro es una **adaptación infantil exclusiva** del universo Karmany Monsta: no traslada automáticamente gráficos, reglas o anatomías de videojuegos y juego de mesa.

**Fuente comprobada:** `Karmany_Monsta_Catalogo_Editable_v0_74(1).xlsx`, hoja **Karmany**, filas **4–31**. Incluye **28 criaturas con código, nombre, subtítulo y datos mecánicos**, pero **no es una biblia de apariencia**. Su uso como referencia de nombres no constituye aprobación de diseño visual. Se conserva el inventario verificable en `editorial/catalogo_karmany_v074.json` (fuente todavía externa al repositorio).

**Tres capas de aprobación diferentes:**
1. Identidad elegida para aparecer en el libro (elenco).
2. Diseño editorial específico del Karmany (model sheet).
3. Ilustración final de cada página (composición, calidad y texto).

Una criatura puede tener apariencia aprobada para el libro sin que esa apariencia pase a ser canon de Forja de Resonancia, Android o Blockchain.

## 2. Estado actual del arte

| Página | Diseño aprobado visualmente | Identidad oficial en catálogo | Estado de PNG en GitHub |
|---|---|---|---|
| P01 | Criatura fantástica con orejas largas, cola amplia, de pie en dos patas saludando; cuatro extremidades en total | **NO ASIGNADA**; no identificarla automáticamente como Selenix | Pendiente: respaldo persistente externo y hash en ficha |
| P02 | Criatura de silueta dracónica/anfibia, ojos expresivos, pose de salto y rasgos distintos de P01 | **NO ASIGNADA**; no identificarla automáticamente como Pyrox | Pendiente: respaldo persistente externo y hash en ficha |
| P03 | Criatura fantástica tipo tortuga con caparazón, junto a niño explorador | **NO ASIGNADA**; no identificarla automáticamente como Torkal | Pendiente: respaldo persistente externo y hash en ficha |

La aprobación visual de una página no modifica automáticamente la ficha de criatura del catálogo.

## 3. Propuesta editorial: 16 Karmanys reutilizables

Es preferible diseñar primero **un elenco consistente y repetible**, no 28 especies porque existan 28 láminas. Como propuesta inicial, **16 criaturas** permiten variedad de siluetas sin multiplicar innecesariamente las hojas de modelo. El número no es una decisión aprobada.

| Código | Nombre verificado | Subtítulo verificado | Motivo para evaluar | Anatomía oficial comprobada |
|---|---|---|---|---|
| K-02 | Aquaris | Guardian de Bruma | Interacciones sencillas y variedad de silueta por investigar; no asumir forma acuática | No documentada |
| K-03 | Pyrox | Salamandra Ignea | Subtítulo de salamandra; posible diseño infantil reptiliano, sujeto a validación | Salamandra (del subtítulo) |
| K-04 | Lumirra | Cria de Luz | Título de cría; candidato a criatura pequeña de introducción | No documentada |
| K-05 | Floravia | Custodia Verde | Motivo verde en subtítulo; posible contraste gráfico sin fijar anatomía | No documentada |
| K-06 | Brisu | Pequeno Veloz | Subtítulo pequeño/veloz; candidato a poses dinámicas | No documentada |
| K-07 | Rocerno | Cria de Piedra | Subtítulo cría/piedra; contraste de formas, sin fijar textura real | No documentada |
| K-08 | Mistolin | Eco de Niebla | Motivo niebla en subtítulo; expresión suave, cuerpo por definir | No documentada |
| K-12 | Nimbara | Guardiana de Lluvia | Motivo lluvia en nombre; no implica incluir fondo lluvioso | No documentada |
| K-14 | Selenix | Zorro de Resonancia | Zorro explícito en subtítulo; candidato a silueta con cola y orejas, sin marcas oficiales | Zorro (del subtítulo) |
| K-17 | Orial | Ciervo Luminico | Ciervo explícito; candidato a variedad cervina, cornamenta aún no confirmada | Ciervo (del subtítulo) |
| K-18 | Torkal | Tortuga de Ruinas | Tortuga explícita; candidato a silueta con caparazón, patrón no oficial | Tortuga (del subtítulo) |
| K-23 | Eryndra | Ave de Resonancia | Ave explícita; opción de silueta alada para niveles avanzados, plumaje por decidir | Ave (del subtítulo) |
| K-24 | Aeterna Draconis | Guardian de Memoria | Legendaria en catálogo; reservar para final si el creador aprueba su presencia | No documentada |
| K-25 | Zephyr | Cria de Viento Bruma | Cría viento/bruma; motivo sugerente, no determina alas | No documentada |
| K-27 | Gemmir | Topo de Cristal Tierno | Topo explícito en subtítulo; candidato con manos/patas grandes, sujeto a diseño | Topo (del subtítulo) |
| K-28 | Vulkai | Chispa Salvaje Menor | Chispa menor; candidato a expresividad dinámica, ninguna forma oficial asumida | No documentada |

**Reservas:** K-01 Terrakor; K-09 Verdan; K-10 Brumak; K-11 Rauk Colmillo; K-13 Ferrak; K-15 Lignar; K-16 Volcrin; K-19 Velkar; K-20 Dravok; K-21 Celestia; K-22 Runakar; K-26 Umbrio. Ninguna criatura fuera del elenco propuesto se considera eliminada del universo.

## 4. Campos obligatorios antes de ilustrar una criatura por segunda vez

- **Identidad:** código/nombre del catálogo o código editorial nuevo; versión del diseño; procedencia.
- **Morfología:** tipo de cuerpo y locomoción; **recuento exacto de extremidades**, articulaciones, cola, orejas, alas/aletas; cara y ojos.
- **Silueta única:** rasgos distinguibles a tamaño pequeño; patrón de marcas y accesorios **sin atributos de juego inventados**.
- **Proporciones:** cabeza/cuerpo/extremidades, medidas relativas y perspectiva. Describir solo tras aprobar boceto.
- **Expresiones permitidas:** alegría, curiosidad, sorpresa, descanso; sin atribuir personalidad o historia canónica.
- **Poses de referencia:** frontal neutral, 3/4, perfil, espalda cuando se vea la cola/alas, una acción coherente con la anatomía.
- **Restricciones:** partes que no se pueden inventar ni cambiar; elementos que deben mantenerse en todas las páginas.
- **Coloreabilidad:** divisiones grandes, contornos cerrados, ninguna mancha negra que impida colorear.
- **Fidelidad:** 1+ imagen fuente aprobada o un diseño editorial nuevo que el creador apruebe expresamente.
- **Estado:** pendiente → boceto → revisión → aprobado editorialmente → uso permitido en páginas. La aprobación no altera automáticamente otros proyectos.

El documento modelo por criatura está en `docs/10_PLANTILLA_MODELO_KARMANY.md`.

## 5. Reparto de páginas

Archivo `editorial/reparto_propuesto_28.json`: cada una de las 28 páginas tiene **candidatos tentativos**, no asignaciones definitivas. Las primeras tres contienen sugerencias de correspondencia visual **que no se deben aplicar automáticamente**. Todas las páginas deberán seguir el índice editorial aprobado, pero el nombre final puede cambiar tras revisar las fichas.

## 6. Secuencia sugerida

1. Confirmar **origen** del elenco (catálogo, nuevas criaturas para el libro o mixto).
2. Confirmar **cantidad** de Karmanys distintos que se diseñarán.
3. Decidir si las tres criaturas visualmente aprobadas se **mantienen como diseños originales del libro** o si deben vincularse a nombres existentes tras revisar su fidelidad.
4. Elegir elenco y cerrar fichas de morfología **una por una**. Una vez exista hoja de modelo aprobada, reutilizarla para mantener continuidad en las 28 láminas.
5. Validar ficha/modelo en vista 3/4 y de perfil; después autorizar su asignación a páginas.
6. Reanudar P04 solo cuando las criaturas que utiliza tengan su apariencia aprobada.

## 7. Regla de protección del canon

Los subtítulos «Zorro de Resonancia», «Tortuga de Ruinas», «Ciervo Lumínico», «Ave de Resonancia», «Topo de Cristal Tierno» y «Salamandra Ígnea» contienen pistas morfológicas literales. **No** especifican número de orejas, color, marcas, tamaño, forma del hocico o accesorios. Para el resto, ni siquiera está definida la familia anatómica. Cualquier propuesta visual se rotula **NO CANÓNICA** hasta aprobación.

**Nota técnica:** la referencia de calidad `docs/05_REFERENCIA_VISUAL_CALIDAD.md` continúa vigente en TODOS los niveles.
