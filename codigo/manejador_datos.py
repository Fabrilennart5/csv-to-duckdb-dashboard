# este archivo tiene contiene las clases que necesitamos para ejecutar las queries a nuestro csv
import duckdb

class GestorBaseDatos:
    """
    Clase para crear y manejar una base de datos en DuckDB.

    Atributos:
        path (str): Ruta al archivo de la base de datos.
        table_name (str): Nombre de la tabla a crear.
        columns (dict): Diccionario con nombres de columnas y sus tipos de datos.
    """

    def __init__(self, path, table_name, **columns):
        self.path = path
        self.table_name = table_name  # Nombre de la tabla que se va a crear
        self.columns = columns  # Almacenar las columnas como un diccionario

    def crear_base_datos(self):
        print(f"Conectando a la base de datos en {self.path}")
        
        # Conectar a DuckDB
        conn = duckdb.connect(self.path)
        
        # Crear la tabla con las columnas especificadas
        columnas_sql = ', '.join([f"{col} {dtype}" for col, dtype in self.columns.items()])
        conn.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} ({columnas_sql});")
        
        conn.close()
        print(f"Tabla '{self.table_name}' creada exitosamente.")

class InsertarDatos:
    """
    Clase para insertar datos en una tabla existente en DuckDB.

    Atributos:
        csv (str): Ruta al archivo CSV.
        db_path (str): Ruta de la base de datos donde se insertarán los datos.
        table_name (str): Nombre de la tabla donde se insertarán los datos.
    """

    def __init__(self, csv, db_path, table_name):
        self.csv = csv
        self.db_path = db_path
        self.table_name = table_name

    def insertar_db(self):
        print(f"Insertando datos desde {self.csv} en la tabla '{self.table_name}' de la base de datos {self.db_path}")
        
        # Conectar a la base de datos
        conn = duckdb.connect(self.db_path)

        # Insertar datos del CSV ignorando la primera fila como datos
        conn.execute(f"""
            COPY {self.table_name} 
            FROM '{self.csv}' 
            (AUTO_DETECT TRUE, HEADER TRUE);
        """)
        
        conn.close()
        print("Datos insertados exitosamente.")