## Ejercicio 1
#
# Leer los datos del archivo ../DataSet/sales_data_sample_excercise.csv
#
# Este archivo tiene algunos datos numéricos y otros de tipo cadena de caracteres.
#
# Las columnas son:
# * ORDERNUMBER: int, id de la orden
# * SALES: float, monto abonado
# * MONTH_ID: int, mes
# * YEAR_ID: int, año
# * PRODUCTLINE: str, producto
# * COUNTRY: str, país de venta
#
# Leer los datos del archivo y crear una instancia de ndarray de tipo cadena de caracteres.

import os

import numpy as np

# Ruta al CSV relativa a este script.
data_location = os.path.join(
    os.path.dirname(__file__), "..", "DataSet", "sales_data_sample_excercise.csv"
)

data = np.genfromtxt(data_location, skip_header=1, delimiter="\t", dtype=str)
print("data:\n", data)

data_type_str = np.genfromtxt(data_location, skip_header=1, delimiter="\t", dtype=str)
print("\ndata_type_str:\n", data_type_str)

data_type_int = np.genfromtxt(data_location, skip_header=1, delimiter="\t", dtype=int)
print("\ndata_type_int:\n", data_type_int)

data_type_float = np.genfromtxt(data_location, skip_header=1, delimiter="\t", dtype=float)
print("\ndata_type_float:\n", data_type_float)
