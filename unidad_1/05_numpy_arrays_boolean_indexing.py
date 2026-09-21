import numpy as np

# Array 1D de ejemplo: [0 1 2 3 4 5 6 7 8 9]
one_d_array = np.arange(10)
#print(one_d_array)

# Máscara booleana: True donde el elemento es múltiplo de 3
# % es el operador módulo (resto de la división)
mask_pair_number = one_d_array % 3 == 0
print(mask_pair_number)  # [True False False True False False True False False True]

# Boolean indexing: devuelve solo los elementos donde la máscara es True
print(one_d_array[mask_pair_number])  # [0 3 6 9]

# Matriz 2D aleatoria 3×4 con valores en [0, 10)
two_d_array = np.random.default_rng().uniform(0, 10, (3, 4))
#print(two_d_array)

# Máscara booleana: True donde el valor es mayor que 5
mask_great_5 = two_d_array > 5
print(mask_great_5)  # matriz 3×4 de True/False

# Devuelve un array 1D solo con los valores que cumplen la condición
print(two_d_array[mask_great_5])
