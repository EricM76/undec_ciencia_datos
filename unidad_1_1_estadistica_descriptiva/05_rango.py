import numpy as np

# Datos de ejemplo (mismos que en cuartiles, para comparar)
data = np.array([30, 36, 47, 50, 52, 52, 56, 60, 63, 70, 70, 110])

# RANGO: diferencia entre el maximo y el minimo
rango = np.max(data) - np.min(data)
print(f"DATOS: {data}")
print(f"RANGO: max - min = {np.max(data)} - {np.min(data)} = {rango}")

# SENSIBLE A OUTLIERS: un valor extremo agranda mucho el rango
data_sin_outlier = data[data != 110]
rango_sin = np.max(data_sin_outlier) - np.min(data_sin_outlier)
print(f"SIN OUTLIER (110): rango = {rango_sin}")  # baja de 80 a 40

# IQR (rango intercuartilico): dispersion del 50% central; mas robusto
q1, q3 = np.percentile(data, [25, 75])
iqr = q3 - q1
print(f"IQR = Q3 - Q1 = {q3} - {q1} = {iqr}")

# COMPARACION: el IQR casi no cambia al quitar el outlier
q1_s, q3_s = np.percentile(data_sin_outlier, [25, 75])
print(f"IQR SIN OUTLIER: {q3_s - q1_s}")  # se mantiene estable

# CON PANDAS (alternativa)
import pandas as pd

serie = pd.Series(data)
print(f"RANGO CON PANDAS: {serie.max() - serie.min()}")
