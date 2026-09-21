import numpy as np

# Creamos una Lista de python
python_list = [1, 4, 2, 5, 3]

# Creamos un Arreglo (array) de enteros instanciado a partir de una lista:
my_numpy_array = np.array(python_list)

# Imprimimos la lista
print(python_list) # [1, 4, 2, 5, 3]
print(python_list[2]) # 2

# Imprimo el numpy array creado
print(my_numpy_array) # [1 4 2 5 3]
print(my_numpy_array[4]) # 3
