import numpy as np

# IMPAR: la mediana es el valor central (posicion n//2 tras ordenar)
data = np.array([1, 2, 3, 4, 5])
median = np.median(data)
print(f"IMPAR: La mediana es {median}")  # valor central = 3

# PAR: promedio de los dos valores centrales
data = np.array([1, 2, 3, 4, 5, 6])
median = np.median(data)
print(f"PAR: La mediana es {median}")  # (3+4)/2 = 3.5

# DESORDENADA: np.median ordena internamente; no hace falta ordenar a mano
data = np.array([9, 1, 7, 3, 5])
print(f"DESORDENADA: datos={data} -> mediana={np.median(data)}")  # equivale a [1,3,5,7,9]

# ROBUSTA ANTE OUTLIERS: la mediana casi no se mueve; la media si
data_outlier = np.array([1, 2, 3, 4, 5, 100])
print(f"CON OUTLIER: media={np.mean(data_outlier)}, mediana={np.median(data_outlier)}")

# COMPARACION: con asimetrica a la derecha, media > mediana
sueldos = np.array([30, 32, 35, 36, 38, 40, 120])  # el 120 es un sueldo atipico
print(f"ASIMETRIA: media={np.mean(sueldos):.2f} > mediana={np.median(sueldos)}")
