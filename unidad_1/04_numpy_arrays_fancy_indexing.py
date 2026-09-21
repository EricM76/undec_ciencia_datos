import numpy as np

# Límite inferior del rango de valores aleatorios (se incluye)
low = 0
# Límite superior del rango (no se incluye): intervalo [0, 10)
high = 10
# Forma del array: 3 filas × 4 columnas
size = (3, 4)

# Crea un generador aleatorio moderno de NumPy
# (sin semilla → valores distintos en cada ejecución)
random_generator = np.random.default_rng()
# random_generator = np.random.default_rng(42)  # con semilla fija → siempre los mismos números

# Genera una matriz 3×4 con valores float distribuidos
# uniformemente en el intervalo [low, high)
two_d_array = random_generator.uniform(low, high, size)

# Muestra el array generado (en notebook o consola interactiva)
print(two_d_array)

# Fancy indexing por filas: seleccionamos las filas 0, 2, 1 y repetimos la 0
lista_indices_filas = [0, 2, 1, 0]
print(two_d_array[lista_indices_filas])

# Fancy indexing por columnas: todas las filas (:),
# columnas 2, 3, 1 y repetimos la 2
lista_indices_columnas = [2, 3, 1, 2]
print(two_d_array[:, lista_indices_columnas])
