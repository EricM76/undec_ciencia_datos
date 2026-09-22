import numpy as np

# IMPAR
data = np.array([1, 2, 3, 4, 5])
median = np.median(data)
print(f"IMPAR: La mediana de los datos es: {median}") # La mediana es el valor central

# PAR
data = np.array([1, 2, 3, 4, 5, 6])
median = np.median(data)
print(f"PAR: La mediana de los datos es: {median}") # La mediana es el promedio de los dos valores centrales