import numpy as np

# --- 1. Escalar + array 1D ---
# Reglas 1 y 2: el escalar se estira a shape (3,) → [5, 5, 5]
resultado = np.arange(3) + 5
print(resultado)  # [5 6 7]

# --- 2. Matriz 2D + array 1D ---
# Regla 1: (3,) → (1, 3)
# Regla 2: (1, 3) se estira a (3, 3)
resultado = np.ones((3, 3)) + np.arange(3)
print(resultado)
# [[1. 2. 3.]
#  [1. 2. 3.]
#  [1. 2. 3.]]

# --- 3. Vector columna + vector fila ---
# Izquierda: (3, 1) se estira en columnas → [[0,0,0], [1,1,1], [2,2,2]]
# Derecha:   (3,) → (1, 3) se estira en filas → [[0,1,2], [0,1,2], [0,1,2]]
resultado = np.arange(3).reshape((3, 1)) + np.arange(3)
print(resultado)
# [[0 1 2]
#  [1 2 3]
#  [2 3 4]]

# --- 4. Caso incompatible (Regla 3) ---
a = np.ones((2, 3))
b = np.ones((3, 2))
# a + b  → ValueError: operands could not be broadcast together
# Descomentar la línea siguiente para ver el error:
# print(a + b)
