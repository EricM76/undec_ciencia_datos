"""
## Ejercicio 2: TIPOS DE DATOS

Crear un array numérico que tenga como valores las columna SALES y otro array de str que tenga como valores
la columna COUNTRY
"""

import numpy as np
import os

# Armamos la ruta al CSV relativa a este script (no al cwd).
# Así funciona aunque se ejecute desde la raíz del proyecto o desde unidad_1.
data_location = os.path.join(
    os.path.dirname(__file__), "..", "DataSet", "sales_data_sample_excercise.csv"
)

# Verificamos que el archivo exista antes de intentar leerlo
if os.path.exists(data_location):
    # Leemos todo el archivo como strings (todas las columnas del mismo tipo)
    # Columnas: 0 ORDERNUMBER, 1 SALES, 2 MONTH_ID, 3 YEAR_ID, 4 PRODUCTLINE, 5 COUNTRY
    data = np.genfromtxt(data_location, skip_header=1, delimiter="\t", dtype=str)

    # Columna SALES → array numérico (usamos astype para convertir de str a float)
    sales_array = data[:, 1].astype(float)
    print(f"\nsales_array: \n{sales_array}")
    print(f"dtype: {sales_array.dtype}")

    # Columna COUNTRY → array de str (ya viene como string)
    country_array = data[:, 5]
    print(f"\ncountry_array: \n{country_array}")
    print(f"dtype: {country_array.dtype}")
else:
    # Mensaje claro si la ruta apunta a un archivo inexistente
    print(f"¡Error! El archivo NO existe en la ruta: {data_location}")
