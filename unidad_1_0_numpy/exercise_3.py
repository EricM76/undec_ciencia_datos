"""
## Ejercicio 3: FUNCIONES DE AGREGACIÓN
Ayuda: https://docs.scipy.org/doc/numpy-1.17.0/reference/routines.statistics.html

Sobre los datos de precios de ventas (columna SALES) calcular:

- Mínimo
- Máximo
- Promedio
- Cantidad
- Suma
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
    # Leemos solo la columna SALES (índice 1) ya como float
    sales_array = np.genfromtxt(
        data_location, skip_header=1, delimiter="\t", usecols=1, dtype=float
    )
    print(f"\nsales_array: \n{sales_array}")
    print(f"dtype: {sales_array.dtype}")

    # Calculamos el mínimo
    min_sales = np.min(sales_array)
    print(f"\nMínimo: {min_sales}")

    # Calculamos el máximo
    max_sales = np.max(sales_array)
    print(f"\nMáximo: {max_sales}")

    # Calculamos el promedio
    avg_sales = np.mean(sales_array)
    print(f"\nPromedio: {avg_sales}")

    # Calculamos la cantidad
    count_sales = np.size(sales_array)
    print(f"\nCantidad: {count_sales}")

    # Calculamos la suma
    sum_sales = np.sum(sales_array)
    print(f"\nSuma: {sum_sales}")
else:
    # Mensaje claro si la ruta apunta a un archivo inexistente
    print(f"¡Error! El archivo NO existe en la ruta: {data_location}")
