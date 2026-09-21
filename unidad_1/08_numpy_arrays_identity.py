import numpy as np

# --- Matriz identidad 5×5 ---
print(np.eye(5))
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]

# --- Matriz rectangular 4×5 (unos en la diagonal) ---
print(np.eye(4, 5))
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]]

# --- Solo matrices cuadradas (equivalente a np.eye(5)) ---
print(np.identity(5))
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]
