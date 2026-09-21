import numpy as np

# =============================================================================
# Ejercicio 1
#
# Dada la instancia de NumPy array:
#
#   data = np.array([[0, 1, 2, 3, 4],
#                    [2, 3, 5, 6, 7],
#                    [5, 6, 7, 8, 9],
#                    [10, 11, 12, 13, 14],
#                    [15, 16, 17, 18, 19],
#                    [1, 2, 3, 4, 5]])
#
# Obtener un array que tenga sólo las filas pares de 'data' usando:
#   * Slicing
#   * Fancy indexing
#
# El resultado debe ser:
#
#   np.array([[0, 1, 2, 3, 4],
#             [5, 6, 7, 8, 9],
#             [15, 16, 17, 18, 19]])
# =============================================================================

# Array de partida (6 filas × 5 columnas)
# Índices de fila: 0, 1, 2, 3, 4, 5  →  las pares son 0, 2 y 4
data = np.array([
    [0, 1, 2, 3, 4],
    [2, 3, 5, 6, 7],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [1, 2, 3, 4, 5],
])
print("data:")
print(data)
print("shape:", data.shape)  # (6, 5)

# --- Solución con Slicing ---
# start:stop:step sobre el eje de las filas
# ::2 → desde el inicio hasta el final, de 2 en 2 (filas 0, 2, 4)
filas_pares_slicing = data[::2]
print("\nFilas pares (slicing):")
print(filas_pares_slicing)

# Equivalente más explícito:
# data[0:len(data):2]  o  data[0:data.shape[0]:2]

# --- Solución con Fancy Indexing ---
# Lista (o array) con los índices de las filas que queremos seleccionar
indices_filas_pares = [0, 2, 4]
filas_pares_fancy = data[indices_filas_pares]
print("\nFilas pares (fancy indexing):")
print(filas_pares_fancy)

# También se puede construir la lista de índices de forma dinámica:
# indices = [i for i in range(data.shape[0]) if i % 2 == 0]
# data[indices]
