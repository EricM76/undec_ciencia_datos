import numpy as np

# Creamos una Lista de python
python_list = [1, 4, 2, 5, 3]

# Creamos un Arreglo (array) de enteros instanciado a partir de una lista:
my_numpy_array = np.array(python_list)

# visualizamos el primer elemento
print(my_numpy_array[0])

# ahora el segundo elemento
print(my_numpy_array[1])

# y el último elemento
print(my_numpy_array[len(my_numpy_array)-1])

