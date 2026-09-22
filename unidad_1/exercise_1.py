"""
## Ejercicio 1

Leer los datos del archivo ../DataSet/sales_data_sample_excercise.csv
Este archivo tiene algunos datos numéricos y otros de tipo cadena de caracteres.

Las columnas son:

* ORDERNUMBER: int, id de la orden
* SALES: float, monto abonado
* MONTH_ID: int, mes
* YEAR_ID: int, año
* PRODUCTLINE: str, producto
* COUNTRY: str, país de venta
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
    # genfromtxt lee el archivo como array NumPy.
    # skip_header=1 → omite la fila de nombres de columnas
    # delimiter='\t' → las columnas están separadas por tabulaciones
    #
    # Por defecto solo interpreta valores numéricos.
    # PRODUCTLINE y COUNTRY (str) quedan como nan.
    data_type_default = np.genfromtxt(data_location, skip_header=1, delimiter="\t")
    print(f"\ndata_type_default: \n{data_type_default}")

    # Ahora le decimos a genfromtxt que interprete las columnas como cadenas de caracteres.
    data_type_str = np.genfromtxt(data_location, skip_header=1, delimiter='\t', dtype= str)
    print(f"\ndata_type_str: \n{data_type_str}")

    # Ahora le decimos a genfromtxt que interprete las columnas como enteros.
    data_type_int = np.genfromtxt(data_location, skip_header=1, delimiter='\t', dtype= int)
    print(f"\ndata_type_int: \n{data_type_int}")

    # Ahora le decimos a genfromtxt que interprete las columnas como flotantes.
    data_type_float = np.genfromtxt(data_location, skip_header=1, delimiter='\t', dtype= float)
    print(f"\ndata_type_float: \n{data_type_float}")
else:
    # Mensaje claro si la ruta apunta a un archivo inexistente
    print(f"¡Error! El archivo NO existe en la ruta: {data_location}")
