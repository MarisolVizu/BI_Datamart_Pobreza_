# BI_Datamart_Pobreza

## Business Intelligence aplicado al análisis de la pobreza multidimensional en el Perú

**Curso:** Business Intelligence 2025-02

**Integrantes:**
- Aguirre Zumaeta, Fiorella Andrea
- Rivera Vizurraga, Marisol

Lima, Perú 2025

---

## 1. Marco Teórico

### Business Intelligence
La Inteligencia de Negocios o Business Intelligence (BI) es el conjunto de estrategias, tecnologías, aplicaciones y procesos que permiten recopilar, integrar, analizar y presentar información procedente de diversas fuentes para apoyar la toma de decisiones empresariales. BI ayuda a convertir datos brutos en conocimiento útil, facilitando la identificación de tendencias, patrones y comportamientos relevantes para la gestión estratégica (Silva et al., 2019).

### Data Warehouse
Es un conjunto de datos orientado, porque organiza la información alrededor de un tema central; integrado, porque combina datos de múltiples fuentes con reglas de consistencia; variable en el tiempo, porque se realizan fotos basadas en hechos o fechas; y no volátil, porque los datos no se modifican ni eliminan por los usuarios finales (Inmon, 2002).

### Data Mart
Un Data Mart es un subconjunto temático y especializado de un Data Warehouse, orientado a cubrir las necesidades de información de un área o departamento específico de la organización. Al igual que el Data Warehouse, organiza la información en modelos multidimensionales como el esquema estrella o el esquema copo de nieve, pero con un alcance más reducido y focalizado (Díaz, 2011). Según Inmon (2002), un data mart puede ser dependiente (construido a partir del Data Warehouse) o independiente (alimentado directamente de fuentes operacionales).

### Elementos principales de un Data Warehouse
A diferencia de las bases de datos operacionales que siguen un diseño normalizado, en un Data Warehouse la información se desnormaliza para optimizar las consultas analíticas (Díaz, 2011):

- **Tabla de hechos:** Representa los procesos de negocio y contiene los datos cuantitativos principales.
- **Dimensiones:** Representan las vistas del proceso y permiten analizar los hechos desde distintos ángulos.
- **Métricas:** Son los indicadores cuantificables que miden el proceso de negocio.

---

## 2. Descripción del Proyecto

En el presente proyecto, la "empresa" objeto de análisis corresponde al **Estado peruano**, con énfasis en las instituciones responsables de la medición y focalización de la pobreza: el **Instituto Nacional de Estadística e Informática (INEI)** y el **Ministerio de Desarrollo e Inclusión Social (MIDIS)**. Dichas entidades administran información proveniente de la **Encuesta Nacional de Hogares (ENAHO)** y del **Sistema de Focalización de Hogares (SISFOH)**.

### Problemática
Actualmente, se evidencia una problemática estructural en el proceso de focalización de la pobreza. El SISFOH continúa sustentándose principalmente en indicadores monetarios y de patrimonio, lo que genera errores tanto de exclusión como de inclusión indebida en la entrega de subsidios. En consecuencia, existen hogares pobres que quedan fuera de la cobertura de programas sociales, mientras que otros, no necesariamente en situación de pobreza, acceden a dichos beneficios (ComexPerú, 2024; MIDIS, 2020).

### Solución Propuesta
La creación de un **datamart temático sobre pobreza multidimensional** se plantea como una estrategia clave para mejorar la calidad de la información disponible en la formulación y evaluación de políticas públicas. El diseño permitirá integrar de manera estructurada las distintas dimensiones de la ENAHO y generar perfiles más completos de los hogares.

---

## 3. Variables y Dimensiones

La selección de variables responde a las recomendaciones de la **Comisión Económica para América Latina y el Caribe (CEPAL, 2025)** para la construcción de un índice de pobreza multidimensional:

| Dimensión | Variables |
|-----------|-----------|
| **Vivienda** | Material de paredes, Material de pisos, Material de techos, Electricidad, Número de habitaciones, Internet |
| **Salud** | Agua potable, Servicios higiénicos, Seguro médico |
| **Educación** | Niños asisten al colegio, Situación educativa esperada, Sabe leer o escribir |
| **Economía** | Tipo de trabajador, Ingreso total, Recibió ayuda del programa Pensión 65, Recibió ayuda del programa Juntos, Monto recibido del programa Pensión 65, Monto recibido del programa Juntos |

> **Nota:** La unidad de análisis corresponde a los **jefes de hogar** en el periodo comprendido entre **2014 y 2024**.

---

## 4. Modelamiento Dimensional

Este modelo dimensional sigue un **esquema en estrella**, compuesto por una tabla de hechos y múltiples tablas de dimensiones.

> **Nota:** Todos los identificadores (ID_) de las 18 dimensiones son generados automáticamente (auto-incrementales). Estos campos funcionan como claves primarias y permiten establecer relaciones consistentes con la tabla de hechos.

### Tabla de Hechos: Fact_Pobreza

Contiene los indicadores cuantitativos principales asociados a cada jefe de hogar.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID_DATA | int | Identificador único del registro (auto-generado) |
| GASTO_ALIMENTOS_HOGAR | float | Gasto en alimentos |
| GASTO_ELECTRICIDAD | float | Gasto en electricidad |
| GASTO_ELECTRODOMESTICOS | float | Gasto en electrodomésticos |
| INGRESO_JUNTOS | float | Monto recibido del programa Juntos |
| INGRESO_PENSION65 | float | Monto recibido del programa Pensión 65 |
| HORAS_SEMANA_OCUP_PRINCIPAL | float | Horas trabajadas semanalmente en ocupación principal |
| INGRESOS_EXTRA_OTRO_TRABAJO | float | Ingreso por trabajos adicionales |
| INGRESO_TOTAL | float | Ingreso total del hogar |
| NUM_HABITACIONES | int | Número de habitaciones en la vivienda |
| EDAD | int | Edad del jefe de hogar |
| *Claves foráneas* | int | Campos que enlazan con las dimensiones |

### Dimensiones

#### Dim_departamento
| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID_DEPARTAMENTO | int | Identificador único (auto-generado) |
| DEPARTAMENTO | nvarchar(20) | Nombre del departamento |
| UBIGEO_DEPARTAMENTO | nvarchar(2) | Código ubigeo |

#### Dim_provincia
| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID_PROVINCIA | int | Identificador único (auto-generado) |
| PROVINCIA | nvarchar(30) | Nombre de la provincia |
| UBIGEO_PROVINCIA | nvarchar(4) | Código ubigeo |

#### Dim_sexo
| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID_SEXO | int | Identificador único (auto-generado) |
| SEXO | nvarchar(6) | Hombre o Mujer |

#### Dim_estadoCivil
| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID_ESTADOCIVIL | int | Identificador único (auto-generado) |
| ESTADO_CIVIL | nvarchar(15) | Estado civil |

#### Dim_tipoTrabajador
| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID_TIPO_TRABAJADOR | int | Identificador único (auto-generado) |
| TIPO_TRABAJADOR | nvarchar(20) | Clasificación laboral |

#### Dim_tipoContrato
| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID_TIPO_CONTRATO | int | Identificador único (auto-generado) |
| TIPO_CONTRATO | nvarchar(15) | Tipo de contrato |

#### Dim_vivienda
| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID_VIVIENDA | int | Identificador único (auto-generado) |
| TIPO_VIVIENDA | nvarchar(35) | Clasificación de la vivienda |

#### Dim_materialPisos
| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID_MATERIAL_PISOS | int | Identificador único (auto-generado) |
| MATERIAL_PISOS | nvarchar(35) | Material predominante en los pisos |

#### Dim_materialTechos
| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID_MATERIAL_TECHOS | int | Identificador único (auto-generado) |
| MATERIAL_TECHOS | nvarchar(50) | Material predominante en los techos |

#### Dim_materialParedes
| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID_MATERIAL_PAREDES | int | Identificador único (auto-generado) |
| MATERIAL_PAREDES | nvarchar(40) | Material predominante en las paredes |

#### Dim_educacion
| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID_EDUCACION | int | Identificador único (auto-generado) |
| NIÑOS_ASISTEN_COLEGIO | nvarchar(10) | Asistencia escolar de niños |
| NIVEL_EDUCATIVO | nvarchar(36) | Nivel educativo alcanzado |

#### Dim_salud
| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID_SALUD | int | Identificador único (auto-generado) |
| ACUDIO_ESSALUD | nvarchar(2) | Acudió a ESSALUD (sí/no) |
| ACUDIO_CLINICA_PARTICULAR | nvarchar(2) | Acudió a clínica particular (sí/no) |
| TIENE_SEGURO | nvarchar(2) | Cobertura de seguro médico (sí/no) |

#### Dim_enfermedad
| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID_ENFERMEDAD | int | Identificador único (auto-generado) |
| ENFERMEDAD | nvarchar(28) | Tipo de enfermedad o condición reportada |

#### Dim_programasSociales
| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID_PROGRAMA | int | Identificador único (auto-generado) |
| RECIBIO | nvarchar(10) | Programa del que recibió ayuda (Pensión 65 o Juntos) |

#### Dim_serviciosBasicos
| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID_SERVICIOS | int | Identificador único (auto-generado) |
| SERVICIOS_BASICOS | nvarchar(20) | Tipo de servicio básico (agua, electricidad, internet, etc.) |

#### Dim_estratoSocial
| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID_ESTRATOSOCIAL | int | Identificador único (auto-generado) |
| ESTRATO_SOCIAL | nvarchar(10) | Clasificación socioeconómica (A, B, C, D, E o Rural) |

#### Dim_nivelPobreza
| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID_POBREZA | int | Identificador único (auto-generado) |
| POBREZA | nvarchar(20) | Categoría de pobreza (pobre, pobre extremo, no pobre) |

#### Dim_tiempo
| Campo | Tipo | Descripción |
|-------|------|-------------|
| ID_TIEMPO | int | Identificador único (auto-generado) |
| AÑO | int | Año de la encuesta |
| MES | int | Mes de la encuesta |

---

## 5. Interpretación del Dashboard (Año 2023)

Para un análisis más delimitado y consistente, el análisis se centró exclusivamente en los datos correspondientes al año 2023.

### Hogares No Pobres
La clasificación del SISFOH identifica a este grupo como no pobres debido a su nivel de ingresos; sin embargo, una revisión multidimensional revela que presentan privaciones significativas, particularmente en la **dimensión de salud**. Aunque se ubican principalmente en los estratos D y E y cuentan con condiciones de infraestructura adecuadas (pisos y paredes formales, promedio de más de tres habitaciones), la gran mayoría carece de seguro médico. En términos laborales, predomina la informalidad y cerca del 98% no recibe apoyo de programas sociales. Pese a ello, muestran buenos niveles educativos y alta asistencia escolar.

### Hogares Pobres No Extremos
Este grupo muestra privaciones más amplias en las dimensiones de infraestructura y salud. Estos hogares, ubicados en estratos bajos y mayormente en zonas rurales, enfrentan condiciones laborales caracterizadas por informalidad. En infraestructura presentan materiales mixtos: pisos de cemento y techos semi-formales. En salud, más del 99% no cuenta con seguro médico, aunque sí disponen de servicios básicos. Los niveles de asistencia escolar se mantienen altos, pero existe cierto rezago educativo.

### Hogares Pobres Extremos
Presentan un patrón consistente de **privaciones simultáneas en todas las dimensiones** evaluadas. Se concentran en zonas rurales y en el estrato E, enfrentando ingresos considerablemente bajos junto con altas tasas de informalidad laboral. Su infraestructura evidencia condiciones claramente precarias: pisos deteriorados, paredes tradicionales y techos semi-formales. En el ámbito de salud, el 100% carece de seguro médico y una proporción significativa tiene dificultades de acceso a servicios esenciales.

---

## 6. Conclusiones

- La construcción del datamart permitió integrar y depurar las variables asociadas a la pobreza multidimensional, generando una base analítica sólida para contrastar la clasificación del SISFOH con otras dimensiones del bienestar.
- Se evidenciaron brechas que los indicadores monetarios no captan, como las privaciones persistentes en salud dentro de hogares catalogados como "no pobres".
- La articulación del datamart con las visualizaciones en Power BI facilitó un análisis desagregado más claro y preciso.
- Este enfoque contribuye a generar información más completa y oportuna para la asignación de subsidios en dimensiones específicas de la pobreza.

---

## 7. Referencias Bibliográficas

- CEPAL. (2025). *Índice de pobreza multidimensional para América Latina*. CEPAL. [Enlace](https://repositorio.cepal.org/entities/publication/b7aa9b0c-7522-41ea-96b3-8c76ac28d40b)
- ComexPerú. (2024, 14 de junio). 1.3 millones de infiltrados en el programa Vaso de Leche. *Semanario 1212*. [Enlace](https://www.comexperu.org.pe/articulo/13-millones-de-infiltrados-en-el-programa-vaso-de-leche)
- Díaz, J. C. (2011). *Introducción al Business Intelligence*. Editorial UOC.
- Inmon, W. H. (2002). *Building the Data Warehouse*. Wiley.
- MIDIS. (2020). *Revisiones de Evidencias N° 9 del Sistema de Focalización de Hogares (SISFOH)*. [Enlace](https://evidencia.midis.gob.pe/wp-content/uploads/2020/11/Sintesis-de-Estudios-SISFOH.pdf)
- Silva, G. E., Zapata, V. M., Morales, K. P., & Toaquiza, L. M. (2019). Análisis de metodologías para desarrollar Data Warehouse aplicado a la toma de decisiones. *Ciencia Digital*, 3(3.4), 229–244. [DOI](https://doi.org/10.33262/cienciadigital.v3i3.4.922)