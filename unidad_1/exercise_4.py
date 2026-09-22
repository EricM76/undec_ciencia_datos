"""
## Ejercicio 4 - Indexing

a) ¿Cuántas ventas se hicieron en USA?

    - Ayuda: boolean indexing
    - Ejemplo:
        ```python
        import numpy as np
        a = np.array([1, 2, 3, 4, 5])
        b = a > 3
        print(b)
        ```
        - Output:
            ```python
            [False False False True True]
            ```
b) ¿Cuáles son los precios de las 5 ventas que están en las filas 6 a 10 del dataset?

    - Resolvamos usando array slicing y fancy indexing
    - Ejemplo:
        ```python
        import numpy as np
        a = np.array([1, 2, 3, 4, 5])
        b = a[1:5]
        print(b)
        ```
        - Output:
            ```python
            [2 3 4 5]
            ```
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
    data = np.genfromtxt(data_location, skip_header=1, delimiter="\t", dtype=str)  
    # Columna COUNTRY → array de str (ya viene como string)
    country_array = data[:, 5]
    # Columna SALES → array de float (ya viene como float)
    sales_array = data[:, 1].astype(float)
    # Boolean indexing para filtrar las ventas en USA
    usa_sales = sales_array[country_array == "USA"]
    print(f"\nVentas en USA: {usa_sales.shape[0]}")
    # Array slicing: filas 6 a 10 del dataset → índices 5..9
    sales_slice = sales_array[5:10]
    print(f"\nPrecios (slicing) filas 6 a 10:\n{sales_slice}")

    # Fancy indexing con range (mismas filas)
    indices = list(range(5, 10))
    sales_fancy = sales_array[indices]
    print(f"\nPrecios (fancy indexing) filas 6 a 10:\n{sales_fancy}")
else:
    # Mensaje claro si la ruta apunta a un archivo inexistente
    print(f"¡Error! El archivo NO existe en la ruta: {data_location}") 