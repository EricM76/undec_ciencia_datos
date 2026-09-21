import numpy as np

# =============================================================================
# Ejercicio 2
#
# Seleccionar los elementos de valor par de 'data' usando boolean indexing
#
# Partimos del mismo array del Ejercicio 1:
#
#   data = np.array([[0, 1, 2, 3, 4],
#                    [2, 3, 5, 6, 7],
#                    [5, 6, 7, 8, 9],
#                    [10, 11, 12, 13, 14],
#                    [15, 16, 17, 18, 19],
#                    [1, 2, 3, 4, 5]])
# =============================================================================

# Array de partida (6 filas × 5 columnas)
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

# --- Solución con Boolean Indexing ---
# % 2 == 0 → True donde el valor es par, False donde es impar
# La máscara tiene la misma shape que data: (6, 5)
mascara = data % 2 == 0
print("\nMáscara booleana (True = par):")
print(mascara)

# Al indexar con la máscara, NumPy devuelve un array 1D
# solo con los elementos donde la máscara es True
elementos_pares = data[mascara]
print("\nElementos pares (boolean indexing):")
print(elementos_pares)
# [ 0  2  4  2  6  6  8 10 12 14 16 18  2  4]
