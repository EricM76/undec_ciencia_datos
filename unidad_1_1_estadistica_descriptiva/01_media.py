import numpy as np

# BASICA: promedio aritmetico de todos los valores
data = np.array([2, 3, 5, 7, 11])
media = np.mean(data)
print(f"BASICA: La media es {media}")  # (2+3+5+7+11)/5 = 5.6

# CON OUTLIER: un valor extremo "empuja" la media hacia arriba
data_outlier = np.array([2, 3, 5, 7, 11, 100])
media_outlier = np.mean(data_outlier)
print(f"CON OUTLIER: La media sube a {media_outlier}")  # el 100 distorsiona el centro

# MEDIA PONDERADA: cada valor tiene un peso distinto
notas = np.array([8, 6, 9])
pesos = np.array([0.5, 0.3, 0.2])  # por ejemplo: parcial, TP y final
media_ponderada = np.average(notas, weights=pesos) # average() para calcular la media ponderada, weights es el peso de cada valor
print(f"PONDERADA: La media ponderada es {media_ponderada}")

# POR EJE: en matrices, axis=0 promedia columnas y axis=1 filas
matriz = np.array([
    [10, 20, 30],
    [40, 50, 60],
])
print(f"POR COLUMNAS (axis=0): {np.mean(matriz, axis=0)}")
print(f"POR FILAS (axis=1): {np.mean(matriz, axis=1)}")
