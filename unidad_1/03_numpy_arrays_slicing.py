import numpy as np

one_d_array = np.arange(10)
print(one_d_array)

# Start = 1: con esto comenzamos por el segundo elemento
# Stop: Al no estar definido, llegamos hasta el final.
# Step: El paso o distancia entre los elementos es 2.
print(one_d_array[1::2])

# Start: Al no estar definido, entonces comenzamos desde el primero.
# Stop: Al no estar definido, entonces llegamos hasta el final.
# Step = -1, me permite invertir el orden del array
print(one_d_array[::-1])