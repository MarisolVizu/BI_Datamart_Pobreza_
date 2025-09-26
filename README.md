# BI_Datamart_Pobreza_

## Proyecto para el curso de Business Intelligence 2025-02.

Este documento describe la estructura del modelo dimensional diseñado para el análisis de la pobreza multidimensional en el Perú, basado en datos de la ENAHO y el SISFOH. 
El modelo sigue un esquema en estrella, compuesto por una tabla de hechos y múltiples tablas de dimensiones.

Nota: Todos los identificadores (ID_) de las 18 dimensión son generados automáticamente (auto–incrementales). Estos campos funcionan como claves primarias y permiten establecer relaciones consistentes con la tabla de hechos.

-------------------------------------------------------------
TABLA DE HECHOS: Fact_Pobreza
-------------------------------------------------------------
Contiene los indicadores cuantitativos principales asociados a cada jefe de hogar.

- ID_DATA (int): Identificador único del registro (auto–generado).
- GASTO_ALIMENTOS_HOGAR (float): Gasto en alimentos.
- GASTO_ELECTRICIDAD (float): Gasto en electricidad.
- GASTO_ELECTRODOMESTICOS (float): Gasto en electrodomésticos.
- INGRESO_JUNTOS (float): Monto recibido del programa Juntos.
- INGRESO_PENSION65 (float): Monto recibido del programa Pensión 65.
- HORAS_SEMANA_OCUP_PRINCIPAL (float): Horas trabajadas semanalmente en la ocupación principal.
- INGRESOS_EXTRA_OTRO_TRABAJO (float): Ingreso por trabajos adicionales.
- INGRESO_TOTAL (float): Ingreso total del hogar.
- NUM_HABITACIONES (int): Número de habitaciones en la vivienda.
- EDAD (int): Edad del jefe de hogar.
- Claves foráneas (int): Campos que enlazan con las dimensiones (ej. ID_TIPO_TRABAJADOR, ID_VIVIENDA, ID_SALUD, etc.).

-------------------------------------------------------------
DIMENSIONES
-------------------------------------------------------------

Dim_departamento
- ID_DEPARTAMENTO (int, auto–generado): Identificador único.
- DEPARTAMENTO (nvarchar(20)): Nombre del departamento.
- UBIGEO_DEPARTAMENTO (nvarchar(2)): Código ubigeo.

Dim_provincia
- ID_PROVINCIA (int, auto–generado): Identificador único.
- PROVINCIA (nvarchar(30)): Nombre de la provincia.
- UBIGEO_PROVINCIA (nvarchar(4)): Código ubigeo.

Dim_sexo
- ID_SEXO (int, auto–generado): Identificador único.
- SEXO (nvarchar(6)): Hombre o mujer.

Dim_estadoCivil
- ID_ESTADOCIVIL (int, auto–generado): Identificador único.
- ESTADO_CIVIL (nvarchar(15)): Estado civil.

Dim_tipoTrabajador
- ID_TIPO_TRABAJADOR (int, auto–generado): Identificador único.
- TIPO_TRABAJADOR (nvarchar(20)): Clasificación laboral.

Dim_tipoContrato
- ID_TIPO_CONTRATO (int, auto–generado): Identificador único.
- TIPO_CONTRATO (nvarchar(15)): Tipo de contrato.

Dim_vivienda
- ID_VIVIENDA (int, auto–generado): Identificador único.
- TIPO_VIVIENDA (nvarchar(35)): Clasificación de la vivienda.

Dim_materialPisos
- ID_MATERIAL_PISOS (int, auto–generado): Identificador único.
- MATERIAL_PISOS (nvarchar(35)): Material predominante en los pisos.

Dim_materialTechos
- ID_MATERIAL_TECHOS (int, auto–generado): Identificador único.
- MATERIAL_TECHOS (nvarchar(50)): Material predominante en los techos.

Dim_materialParedes
- ID_MATERIAL_PAREDES (int, auto–generado): Identificador único.
- MATERIAL_PAREDES (nvarchar(40)): Material predominante en las paredes.

Dim_educacion
- ID_EDUCACION (int, auto–generado): Identificador único.
- NIÑOS_ASISTEN_COLEGIO (nvarchar(10)): Asistencia escolar de niños.
- NIVEL_EDUCATIVO (nvarchar(36)): Nivel educativo alcanzado.

Dim_salud
- ID_SALUD (int, auto–generado): Identificador único.
- ACUDIO_ESSALUD (nvarchar(2)): Acudió a ESSALUD o no (si o no).
- ACUDIO_CLINICA_PARTICULAR (nvarchar(10)): Acudió a clínica en particular o no (si o no).
- TIENE_SEGURO (nvarchar(10)): Cobertura de seguro médico (si o no).

Dim_enfermedad
- ID_ENFERMEDAD (int, auto–generado): Identificador único.
- ENFERMEDAD (nvarchar(28)): Tipo de enfermedad o condición reportada.

Dim_programasSociales
- ID_PROGRAMA (int, auto–generado): Identificador único.
- RECIBIO (nvarchar(10)): Indica de que programa recibió ayuda (pensión 65 o juntos).

Dim_serviciosBasicos
- ID_SERVICIOS (int, auto–generado): Identificador único.
- SERVICIOS_BASICOS (nvarchar(20)): Tipo de servicio básico (agua, electricidad, internet, etc.).

Dim_estratoSocial
- ID_ESTRATOSOCIAL (int, auto–generado): Identificador único.
- ESTRATO_SOCIAL (nvarchar(10)): Clasificación socioeconómica (A, B, C, D, E o Rural).

Dim_nivelPobreza
- ID_POBREZA (int, auto–generado): Identificador único.
- POBREZA (nvarchar(20)): Categoría de pobreza (pobre, pobre extremo, no pobre).

Dim_tiempo
- ID_TIEMPO (int, auto–generado): Identificador único.
- AÑO (int): Año de la encuesta.
- MES (int): Mes de la encuesta.

-------------------------------------------------------------
Este modelo dimensional permitirá analizar de forma estructurada múltiples dimensiones de la pobreza en el Perú. Asimismo, los identificadores (ID_), generados automáticamente, garantizan la integridad del modelo, facilitan la explotación analítica y permiten construir cubos OLAP y reportes dinámicos para la toma de decisiones basadas en evidencia.

----> Link del google drive del informe preparado: https://drive.google.com/drive/folders/1QfW_32XkMz97S-FR_SRneGh51o2eWcTg?usp=sharing
