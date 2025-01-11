

from manejador_datos import GestorBaseDatos, InsertarDatos
from pathlib import Path

def main():
    # Ruta a la carpeta "Data"
    base_path = Path("D:/proyectos de codigo/ddb project/Data")
    base_path.mkdir(parents=True, exist_ok=True)  # Crea el directorio si no existe

    # Ruta completa al archivo de la base de datos
    db_file = base_path / "base_de_datos.duckdb"

    # Crear la base de datos y la tabla
    conexion = GestorBaseDatos(
        str(db_file),  # Ruta al archivo de la base de datos
        "clientes",  # Nombre de la tabla
        ID="INTEGER",
        Year_Birth="INTEGER",
        Education="VARCHAR",
        Marital_Status="VARCHAR",
        Income="VARCHAR",
        Kidhome="INTEGER",
        Teenhome="INTEGER",
        Dt_Customer="DATE",
        Recency="INTEGER",
        MntWines="INTEGER",
        MntFruits="INTEGER",
        MntMeatProducts="INTEGER",
        MntFishProducts="INTEGER",
        MntSweetProducts="INTEGER",
        MntGoldProds="INTEGER",
        NumDealsPurchases="INTEGER",
        NumWebPurchases="INTEGER",
        NumCatalogPurchases="INTEGER",
        NumStorePurchases="INTEGER",
        NumWebVisitsMonth="INTEGER",
        AcceptedCmp3="INTEGER",
        AcceptedCmp4="INTEGER",
        AcceptedCmp5="INTEGER",
        AcceptedCmp1="INTEGER",
        AcceptedCmp2="INTEGER",
        Response="INTEGER",
        Complain="INTEGER",
        Country="VARCHAR"
    )

    conexion.crear_base_datos()  # Crear la base de datos y la tabla si no existe

    # Ruta al archivo CSV de datos
    csv_path = Path(r"D:\proyectos de codigo\ddb project\Data\marketing.csv")

    # Insertar los datos desde el archivo CSV directamente
    insertar = InsertarDatos(
        str(csv_path),  # Ruta al archivo CSV
        str(db_file),  # Ruta de la base de datos
        'clientes'  # Nombre de la tabla
    )
    insertar.insertar_db()  # Insertar los datos en la tabla

if __name__ == "__main__":
    main()
