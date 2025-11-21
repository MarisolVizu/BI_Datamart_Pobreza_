import pyodbc
import pandas as pd

###  crear conexion a dos bases de datos
def get_connection_origen():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=DESKTOP-VC03P0C\SQLEXPRESS;'
            'DATABASE=PobrezaOrigen;'
            'Trusted_Connection=yes;'

            #'UID=sa;'
            #'PWD=1234567890'
        )
        print("✓ Conexión a origen exitosa")
        return conn
    except pyodbc.Error as e:
        print(f"Error de conexión al origen: {e}")
        return None

def get_connection_destino():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=DESKTOP-VC03P0C\SQLEXPRESS;'
            'DATABASE=PobrezaDM1;'
            'Trusted_Connection=yes;'

            #'UID=sa;'
            #'PWD=1234567890'
        )
        print("✓ Conexión a destino exitosa")
        return conn
    except pyodbc.Error as e:
        print(f"Error de conexión al destino: {e}")
        return None
    
### crear las tablas de data mart
def create_datamart_schema(cursor):
    create_script = """

    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Dim_sexo' AND xtype='U')
    CREATE TABLE Dim_sexo (
        ID_SEXO INT IDENTITY(1,1) PRIMARY KEY,
        SEXO NVARCHAR(10) NOT NULL
    );

    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Dim_materialTechos' AND xtype='U')
    CREATE TABLE Dim_materialTechos (
        ID_MATERIAL_TECHOS INT IDENTITY(1,1) PRIMARY KEY,
        MATERIAL_TECHOS NVARCHAR(50) NOT NULL
    );

    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Dim_materialPisos' AND xtype='U')
    CREATE TABLE Dim_materialPisos (
        ID_MATERIAL_PISOS INT IDENTITY(1,1) PRIMARY KEY,
        MATERIAL_PISOS NVARCHAR(35) NOT NULL
    );

    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Dim_materialParedes' AND xtype='U')
    CREATE TABLE Dim_materialParedes (
        ID_MATERIAL_PAREDES INT IDENTITY(1,1) PRIMARY KEY,
        MATERIAL_PAREDES NVARCHAR(50) NOT NULL
    );

    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Dim_estratoSocial' AND xtype='U')
    CREATE TABLE Dim_estratoSocial (
        ID_ESTRATO_SOCIAL INT IDENTITY(1,1) PRIMARY KEY,
        ESTRATO_SOCIAL NVARCHAR(5) NOT NULL
    );

    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Dim_salud' AND xtype='U')
    CREATE TABLE Dim_salud (
        ID_SALUD INT IDENTITY(1,1) PRIMARY KEY,
        TIENE_SEGURO NVARCHAR(2) NOT NULL
    );

    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Dim_tipoContrato' AND xtype='U')
    CREATE TABLE Dim_tipoContrato (
        ID_TIPO_CONTRATO INT IDENTITY(1,1) PRIMARY KEY,
        TIPO_CONTRATO NVARCHAR(15) NOT NULL
    );

    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Dim_programasSociales' AND xtype='U')
    CREATE TABLE Dim_programasSociales (
        ID_PROGRAMA INT IDENTITY(1,1) PRIMARY KEY,
        RECIBIO NVARCHAR(10) NOT NULL
    );

    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Dim_educacionHijos' AND xtype='U')
    CREATE TABLE Dim_educacionHijos (
        ID_EDUCACION INT IDENTITY(1,1) PRIMARY KEY,
        NINOS_ASISTEN_COLEGIO NVARCHAR(10) NOT NULL,
        SITUACION_EDUCATIVA_ESPERADA NVARCHAR(40) NOT NULL
    );

    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Dim_serviciosBasicos' AND xtype='U')
    CREATE TABLE Dim_serviciosBasicos (
        ID_SERVICIOS INT IDENTITY(1,1) PRIMARY KEY,
        SERVICIOS_BASICOS NVARCHAR(20) NOT NULL
    );

    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Dim_nivelPobreza' AND xtype='U')
    CREATE TABLE Dim_nivelPobreza (
        ID_POBREZA INT IDENTITY(1,1) PRIMARY KEY,
        POBREZA NVARCHAR(20) NOT NULL
    );

    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Dim_locacion' AND xtype='U')
    CREATE TABLE Dim_locacion (
        ID_UBICACION INT IDENTITY(1,1) PRIMARY KEY,
        UBIGEO NVARCHAR(20) NOT NULL,
        DEPARTAMENTO NVARCHAR(20) NOT NULL,
        PROVINCIA NVARCHAR(50) NOT NULL
    );

    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Dim_tiempo' AND xtype='U')
    CREATE TABLE Dim_tiempo (
        ID_TIEMPO INT IDENTITY(1,1) PRIMARY KEY,
        FECHA DATE NOT NULL,
        ANIO INT NOT NULL,
        MES INT NOT NULL,
        TRIMESTRE INT NOT NULL,
        SEMESTRE INT NOT NULL,
        MES_NOMBRE NVARCHAR(20) NOT NULL
    );

    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='FactPobreza' AND xtype='U')
    CREATE TABLE FactPobreza (
        ID_DATA INT IDENTITY(1,1) PRIMARY KEY,
        ID_TIPO_CONTRATO INT NOT NULL,
        ID_MATERIAL_PISOS INT NOT NULL,
        ID_PROGRAMA INT NOT NULL,
        ID_EDUCACION INT NOT NULL,
        ID_SERVICIOS INT NOT NULL,
        ID_TIEMPO INT NOT NULL,
        ID_POBREZA INT NOT NULL,
        ID_SALUD INT NOT NULL,
        ID_ESTRATO_SOCIAL INT NOT NULL,
        ID_SEXO INT NOT NULL,
        ID_MATERIAL_PAREDES INT NOT NULL,
        ID_MATERIAL_TECHOS INT NOT NULL,
        ID_UBICACION INT NOT NULL,

        GASTO_ALIMENTOS_HOGAR FLOAT NOT NULL,
        GASTO_ELECTRODOMESTICOS FLOAT NOT NULL,
        INGRESO_JUNTOS FLOAT NOT NULL,
        INGRESO_PENSION65 FLOAT NOT NULL,
        HORAS_SEMANA_OCUP_PRINCIPAL INT NOT NULL,
        INGRESO_TOTAL FLOAT NOT NULL,
        NUM_HABITACIONES INT NOT NULL,
        EDAD INT NOT NULL,

        FOREIGN KEY (ID_SEXO) REFERENCES Dim_sexo(ID_SEXO),
        FOREIGN KEY (ID_MATERIAL_TECHOS) REFERENCES Dim_materialTechos(ID_MATERIAL_TECHOS),
        FOREIGN KEY (ID_MATERIAL_PISOS) REFERENCES Dim_materialPisos(ID_MATERIAL_PISOS),
        FOREIGN KEY (ID_MATERIAL_PAREDES) REFERENCES Dim_materialParedes(ID_MATERIAL_PAREDES),
        FOREIGN KEY (ID_ESTRATO_SOCIAL) REFERENCES Dim_estratoSocial(ID_ESTRATO_SOCIAL),
        FOREIGN KEY (ID_SALUD) REFERENCES Dim_salud(ID_SALUD),
        FOREIGN KEY (ID_TIPO_CONTRATO) REFERENCES Dim_tipoContrato(ID_TIPO_CONTRATO),
        FOREIGN KEY (ID_PROGRAMA) REFERENCES Dim_programasSociales(ID_PROGRAMA),
        FOREIGN KEY (ID_EDUCACION) REFERENCES Dim_educacionHijos(ID_EDUCACION),
        FOREIGN KEY (ID_SERVICIOS) REFERENCES Dim_serviciosBasicos(ID_SERVICIOS),
        FOREIGN KEY (ID_POBREZA) REFERENCES Dim_nivelPobreza(ID_POBREZA),
        FOREIGN KEY (ID_UBICACION) REFERENCES Dim_locacion(ID_UBICACION),
        FOREIGN KEY (ID_TIEMPO) REFERENCES Dim_tiempo(ID_TIEMPO)
    );
    """
    cursor.execute(create_script)
    cursor.commit()


# Conexiones
source_conn = get_connection_origen()
dest_conn = get_connection_destino()

if not source_conn or not dest_conn:
    exit(1)

dest_cursor = dest_conn.cursor()
create_datamart_schema(dest_cursor)
dest_conn.commit()
print("✓ Esquema completo del Data Mart creado.")


### limpiar todas las tablas del datamart
def clean_datamart(cursor, conn):
    """
    Limpia todas las tablas del Data Mart en orden seguro.
    """
    print("🧹 Limpiando Data Mart...")
    
    # 1. Borrar hechos primero por integridad referencial
    cursor.execute("DELETE FROM FactPobreza")
    print("  → Tabla FactPobreza vaciada.")
   
    
    # 2. Borrar dimensiones
    
    cursor.execute("DELETE FROM Dim_sexo")
    print("  → Tabla Dim_sexo vaciada.")
    
    cursor.execute("DELETE FROM Dim_materialTechos")
    print("  → Tabla Dim_materialTechos vaciada.")
    
    cursor.execute("DELETE FROM Dim_materialPisos")
    print("  → Tabla Dim_materialPisos vaciada.")
    
    cursor.execute("DELETE FROM Dim_materialParedes")
    print("  → Tabla Dim_materialParedes vaciada.")
    
    cursor.execute("DELETE FROM Dim_estratoSocial")
    print("  → Tabla Dim_estratoSocial vaciada.")
    
    cursor.execute("DELETE FROM Dim_salud")
    print("  → Tabla Dim_salud vaciada.")
    
    cursor.execute("DELETE FROM Dim_tipoContrato")
    print("  → Tabla Dim_tipoContrato vaciada.")
    
    cursor.execute("DELETE FROM Dim_programasSociales")
    print("  → Tabla Dim_programasSociales vaciada.")
    
    cursor.execute("DELETE FROM Dim_educacionHijos")
    print("  → Tabla Dim_educacionHijos vaciada.")
    
    cursor.execute("DELETE FROM Dim_serviciosBasicos")
    print("  → Tabla Dim_serviciosBasicos vaciada.")
    
    cursor.execute("DELETE FROM Dim_nivelPobreza")
    print("  → Tabla Dim_nivelPobreza vaciada.")
    
    cursor.execute("DELETE FROM Dim_locacion")
    print("  → Tabla Dim_locacion vaciada.")
    
    cursor.execute("DELETE FROM Dim_tiempo")
    print("  → Tabla Dim_tiempo vaciada.")
    
    
    conn.commit()
    print(" Data Mart limpiado completamente.\n")

clean_datamart(dest_cursor, dest_conn)




# -------------------------------------------------------------- Cargar dimensiones ---

#------------------------------------------- Dim_sexo
print("Cargando Dim_sexo...")
query_sexo = """
        SELECT DISTINCT [SEXO]
        FROM [PobrezaOrigen].[dbo].[PobrezaOrigen]
        """
df_sexo = pd.read_sql(query_sexo, source_conn)
for _, r in df_sexo.iterrows():
    dest_cursor.execute("INSERT INTO Dim_sexo (SEXO) VALUES (?)", 
                       str(r['SEXO']))
dest_conn.commit()
print(f"✓ {len(df_sexo)} sexos cargados.")


#------------------------------------------- Dim_materialTechos
print("Cargando Dim_materialTechos...")
query_materialTechos = """
        SELECT DISTINCT [MATERIAL_TECHOS]
        FROM [PobrezaOrigen].[dbo].[PobrezaOrigen]
        """
df_materialTechos = pd.read_sql(query_materialTechos, source_conn)
for _, r in df_materialTechos.iterrows():
    dest_cursor.execute("INSERT INTO Dim_materialTechos (MATERIAL_TECHOS) VALUES (?)", 
                       str(r['MATERIAL_TECHOS']))
dest_conn.commit()
print(f"✓ {len(df_materialTechos)} materialTechos cargados.")


#------------------------------------------- Dim_materialPisos
print("Cargando Dim_materialPisos...")
query_materialPisos = """
        SELECT DISTINCT [MATERIAL_PISOS]
        FROM [PobrezaOrigen].[dbo].[PobrezaOrigen]
        """
df_materialPisos = pd.read_sql(query_materialPisos, source_conn)
for _, r in df_materialPisos.iterrows():
    dest_cursor.execute("INSERT INTO Dim_materialPisos (MATERIAL_PISOS) VALUES (?)", 
                       str(r['MATERIAL_PISOS']))
dest_conn.commit()
print(f"✓ {len(df_materialPisos)} materialPisos cargados.")


#------------------------------------------- Dim_materialParedes
print("Cargando Dim_materialParedes...")
query_materialParedes = """
        SELECT DISTINCT [MATERIAL_PAREDES]
        FROM [PobrezaOrigen].[dbo].[PobrezaOrigen]
        """
df_materialParedes = pd.read_sql(query_materialParedes, source_conn)
for _, r in df_materialParedes.iterrows():
    dest_cursor.execute("INSERT INTO Dim_materialParedes (MATERIAL_PAREDES) VALUES (?)", 
                       str(r['MATERIAL_PAREDES']))
dest_conn.commit()
print(f"✓ {len(df_materialParedes)} materialParedes cargados.")

#------------------------------------------- Dim_estratoSocial
print("Cargando Dim_estratoSocial...")
query_estratoSocial = """
        SELECT DISTINCT [ESTRSOCIAL] AS ESTRATO_SOCIAL
        FROM [PobrezaOrigen].[dbo].[PobrezaOrigen]
        """
df_estratoSocial = pd.read_sql(query_estratoSocial, source_conn)
for _, r in df_estratoSocial.iterrows():
    dest_cursor.execute("INSERT INTO Dim_estratoSocial (ESTRATO_SOCIAL) VALUES (?)", 
                       str(r['ESTRATO_SOCIAL']))
dest_conn.commit()
print(f"✓ {len(df_estratoSocial)} estratos sociales cargados.")

#------------------------------------------- Dim_salud
print("Cargando Dim_salud...")
query_salud = """
        SELECT DISTINCT [SIN_SEGURO] as TIENE_SEGURO
        FROM [PobrezaOrigen].[dbo].[PobrezaOrigen]
        """
df_salud = pd.read_sql(query_salud, source_conn)
for _, r in df_salud.iterrows():
    dest_cursor.execute("INSERT INTO Dim_salud (TIENE_SEGURO) VALUES (?)", 
                       str(r['TIENE_SEGURO']))
dest_conn.commit()
print(f"✓ {len(df_salud)} categorias cargadas.")


#------------------------------------------- Dim_tipoContrato
print("Cargando Dim_tipoContrato...")
query_contrato = """
        SELECT DISTINCT [TIPO_CONTRATO]
        FROM [PobrezaOrigen].[dbo].[PobrezaOrigen]
        """
df_contrato = pd.read_sql(query_contrato , source_conn)
for _, r in df_contrato.iterrows():
    dest_cursor.execute("INSERT INTO Dim_tipoContrato (TIPO_CONTRATO) VALUES (?)", 
                       str(r['TIPO_CONTRATO']))
dest_conn.commit()
print(f"✓ {len(df_contrato )} contratos cargadas.")


#------------------------------------------- Dim_programasSociales
print("Cargando Dim_programasSociales...")
query_programas = """
        SELECT DISTINCT [RECIBIO] 
        FROM [PobrezaOrigen].[dbo].[PobrezaOrigen]
        """
df_programas = pd.read_sql(query_programas , source_conn)
for _, r in df_programas.iterrows():
    dest_cursor.execute("INSERT INTO Dim_programasSociales (RECIBIO) VALUES (?)", 
                       str(r['RECIBIO']))
dest_conn.commit()
print(f"✓ {len(df_programas )} programas cargadas.")


#------------------------------------------- Dim_educacionHijos
print("Cargando Dim_educacionHijos...")
query_educacionHijos = """
        SELECT DISTINCT [NINOS_ASISTEN_COLEGIO]
                        ,[SITUACION_EDUCATIVA_ESPERADA]
        FROM [PobrezaOrigen].[dbo].[PobrezaOrigen]
        """
df_educacionHijos = pd.read_sql(query_educacionHijos , source_conn)
for _, r in df_educacionHijos.iterrows():
    dest_cursor.execute("INSERT INTO Dim_educacionHijos (NINOS_ASISTEN_COLEGIO, SITUACION_EDUCATIVA_ESPERADA) VALUES (?, ?)", 
                       str(r['NINOS_ASISTEN_COLEGIO']), str(r['SITUACION_EDUCATIVA_ESPERADA']))
dest_conn.commit()
print(f"✓ {len(df_educacionHijos  )} educacionHijos  cargadas.")


#------------------------------------------- Dim_serviciosBasicos
print("Cargando Dim_serviciosBasicos...")
query_servicios = """
        SELECT DISTINCT [SERVICIOS_BASICOS]
        FROM [PobrezaOrigen].[dbo].[PobrezaOrigen]
        """
df_servicios = pd.read_sql(query_servicios , source_conn)
for _, r in df_servicios.iterrows():
    dest_cursor.execute("INSERT INTO Dim_serviciosBasicos (SERVICIOS_BASICOS) VALUES (?)", 
                       str(r['SERVICIOS_BASICOS']))
dest_conn.commit()
print(f"✓ {len(df_servicios)} servicios  cargadas.")

#------------------------------------------- Dim_locacion
print("Cargando Dim_locacion...")
query_locacion = """
        SELECT DISTINCT [DEPARTAMENTO]
                      ,[PROVINCIA]
                      ,[UBIGEO]
        FROM [PobrezaOrigen].[dbo].[PobrezaOrigen]
        """
df_locacion = pd.read_sql(query_locacion , source_conn)
for _, r in df_locacion.iterrows():
    dest_cursor.execute("INSERT INTO Dim_locacion (DEPARTAMENTO, PROVINCIA, UBIGEO) VALUES (?, ?, ?)", 
                       str(r['DEPARTAMENTO']), str(r['PROVINCIA']), str(r['UBIGEO']))
dest_conn.commit()
print(f"✓ {len(df_locacion)} locaciones  cargadas.")


#------------------------------------------- Dim_nivelPobreza
print("Cargando Dim_nivelPobreza...")
query_nivelPobreza = """
        SELECT DISTINCT [POBREZA]
        FROM [PobrezaOrigen].[dbo].[PobrezaOrigen]
        """
df_nivelPobreza = pd.read_sql(query_nivelPobreza , source_conn)
for _, r in df_nivelPobreza.iterrows():
    dest_cursor.execute("INSERT INTO Dim_nivelPobreza (POBREZA) VALUES (?)", 
                       str(r['POBREZA']))
dest_conn.commit()
print(f"✓ {len(df_nivelPobreza)} nivelPobreza cargadas.")


#------------------------------------------- Dim_tiempo
print("Cargando Dim_tiempo...")
query_tiempo = """

        WITH BASE AS (
        SELECT DISTINCT DATEFROMPARTS([ANIO], [MES], 1) AS FECHA
        FROM [PobrezaOrigen].[dbo].[PobrezaOrigen]
        )
        SELECT
        	FECHA,
        	DATEPART(YEAR, FECHA) AS ANIO,
        	DATEPART(MONTH, FECHA) AS MES,
        	DATEPART(QUARTER, FECHA) AS TRIMESTRE,
        	 CASE 
                WHEN DATEPART(MONTH, FECHA) BETWEEN 1 AND 6 THEN 1
                ELSE 2
            END AS SEMESTRE,
        	DATENAME(MONTH, FECHA) AS MES_NOMBRE
        FROM BASE

        """
df_tiempo = pd.read_sql(query_tiempo , source_conn)
for _, r in df_tiempo.iterrows():
    dest_cursor.execute("INSERT INTO Dim_tiempo (FECHA, ANIO, MES, TRIMESTRE, SEMESTRE, MES_NOMBRE) VALUES (?, ?, ?, ?, ?, ?)", 
                       str(r['FECHA']), str(r['ANIO']), str(r['MES']), str(r['TRIMESTRE']), str(r['SEMESTRE']), str(r['MES_NOMBRE']))
dest_conn.commit()
print(f"✓ {len(df_tiempo)} fechas  cargadas.")


# -------------------------------------------------------------- Cargar Fact Table ---


#------------------------------------------- FactPobreza
print("Cargando FactPobreza...")
query_fact = """
            SELECT ID_TIPO_CONTRATO
            	  ,ID_MATERIAL_PISOS
            	  ,ID_PROGRAMA
            	  ,ID_EDUCACION
            	  ,ID_SERVICIOS
            	  ,ID_TIEMPO
            	  ,ID_POBREZA
            	  ,ID_SALUD
            	  ,ID_ESTRATO_SOCIAL
            	  ,ID_SEXO
            	  ,ID_MATERIAL_PAREDES
            	  ,ID_MATERIAL_TECHOS
            	  ,ID_UBICACION
            	   ,[GASTO_ALIMENTOS_HOGAR]
                  ,[GASTO_ELECTRODOMESTICOS]
                  ,[INGRESO_JUNTOS]
                  ,[INGRESO_PENSION65]
                  ,[HORAS_SEMANA_OCUP_PRINCIPAL]
                  ,[INGRESO_TOTAL]
                  ,[NUM_HABITACIONES]
                  ,[EDAD]
              FROM [PobrezaOrigen].[dbo].[PobrezaOrigen] A
              LEFT JOIN [PobrezaDM1].[dbo].[Dim_educacionHijos] B ON A.[NINOS_ASISTEN_COLEGIO] = B.NINOS_ASISTEN_COLEGIO AND A.SITUACION_EDUCATIVA_ESPERADA = B.SITUACION_EDUCATIVA_ESPERADA
              LEFT JOIN [PobrezaDM1].[dbo].Dim_estratoSocial C ON C.ESTRATO_SOCIAL = A.ESTRSOCIAL
              LEFT JOIN [PobrezaDM1].[dbo].Dim_locacion D ON D.UBIGEO = A.UBIGEO
              LEFT JOIN [PobrezaDM1].[dbo].Dim_materialParedes E ON E.MATERIAL_PAREDES = A.MATERIAL_PAREDES
              LEFT JOIN [PobrezaDM1].[dbo].Dim_materialPisos F ON F.MATERIAL_PISOS = A.MATERIAL_PISOS
              LEFT JOIN [PobrezaDM1].[dbo].Dim_materialTechos G ON G.MATERIAL_TECHOS = A.MATERIAL_TECHOS
              LEFT JOIN [PobrezaDM1].[dbo].Dim_nivelPobreza H ON H.POBREZA = A.POBREZA
              LEFT JOIN [PobrezaDM1].[dbo].Dim_programasSociales I ON I.RECIBIO = A.RECIBIO
              LEFT JOIN [PobrezaDM1].[dbo].Dim_salud J ON J.TIENE_SEGURO = A.SIN_SEGURO
              LEFT JOIN [PobrezaDM1].[dbo].Dim_serviciosBasicos K ON K.SERVICIOS_BASICOS = A.SERVICIOS_BASICOS
              LEFT JOIN [PobrezaDM1].[dbo].Dim_sexo L ON L.SEXO = A.SEXO
              LEFT JOIN [PobrezaDM1].[dbo].Dim_tiempo M ON M.MES = A.MES AND M.ANIO = A.ANIO
              LEFT JOIN [PobrezaDM1].[dbo].Dim_tipoContrato N ON N.TIPO_CONTRATO = A.TIPO_CONTRATO

        """
df_fact = pd.read_sql(query_fact , source_conn)
for _, r in df_fact.iterrows():
    dest_cursor.execute("""INSERT INTO FactPobreza (
                                ID_TIPO_CONTRATO, ID_MATERIAL_PISOS, ID_PROGRAMA, ID_EDUCACION, ID_SERVICIOS, 
                                ID_TIEMPO, ID_POBREZA, ID_SALUD, ID_ESTRATO_SOCIAL, ID_SEXO, 
                                ID_MATERIAL_PAREDES, ID_MATERIAL_TECHOS, ID_UBICACION, 
                                GASTO_ALIMENTOS_HOGAR, GASTO_ELECTRODOMESTICOS, INGRESO_JUNTOS, INGRESO_PENSION65, 
                                HORAS_SEMANA_OCUP_PRINCIPAL, INGRESO_TOTAL, NUM_HABITACIONES, EDAD) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", 
                       int(r['ID_TIPO_CONTRATO']), int(r['ID_MATERIAL_PISOS']), int(r['ID_PROGRAMA']), int(r['ID_EDUCACION']),
                       int(r['ID_SERVICIOS']), int(r['ID_TIEMPO']), int(r['ID_POBREZA']), int(r['ID_SALUD']), 
                       int(r['ID_ESTRATO_SOCIAL']), int(r['ID_SEXO']), int(r['ID_MATERIAL_PAREDES']), int(r['ID_MATERIAL_TECHOS']),
                       int(r['ID_UBICACION']),
                       float(r['GASTO_ALIMENTOS_HOGAR']), float(r['GASTO_ELECTRODOMESTICOS']), float(r['INGRESO_JUNTOS']), float(r['INGRESO_PENSION65']),
                       int(float(r['HORAS_SEMANA_OCUP_PRINCIPAL'])), float(r['INGRESO_TOTAL']), int(r['NUM_HABITACIONES']), int(r['EDAD']))
dest_conn.commit()
print(f"✓ {len(df_fact)} registros cargados.")

# Cerrar conexiones
source_conn.close()
dest_conn.close()
print("ETL completado exitosamente. Data Mart de Pobreza Multidimensional poblado correctamente.")