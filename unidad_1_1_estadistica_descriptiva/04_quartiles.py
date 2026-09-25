import numpy as np

# Datos de ejemplo (ya ordenados para facilitar la lectura)
data = np.array([30, 36, 47, 50, 52, 52, 56, 60, 63, 70, 70, 110])

# CUARTILES: dividen los datos ordenados en 4 partes iguales
# Q1 = percentil 25, Q2 = percentil 50 (mediana), Q3 = percentil 75
q1 = np.quantile(data, 0.25)
q2 = np.quantile(data, 0.50)
q3 = np.quantile(data, 0.75)

print(f"DATOS: {data}")
print(f"Q1 (25%): {q1}")  # 25% de los datos estan por debajo
print(f"Q2 (50% / mediana): {q2}")
print(f"Q3 (75%): {q3}")  # 75% de los datos estan por debajo

# IQR (rango intercuartilico): dispersion del 50% central
iqr = q3 - q1
print(f"IQR = Q3 - Q1 = {iqr}")

# RESUMEN DE CINCO NUMEROS: min, Q1, mediana, Q3, max
resumen = [float(np.min(data)), float(q1), float(q2), float(q3), float(np.max(data))]
print(f"RESUMEN DE 5 NUMEROS: {resumen}")

# PERCENTILES: generalizacion de los cuartiles a cualquier proporcion
p10 = np.percentile(data, 10)
p90 = np.percentile(data, 90)
print(f"PERCENTILES: P10={p10}, P90={p90}")

# DETECCION DE OUTLIERS (regla 1.5 * IQR)
limite_inf = q1 - 1.5 * iqr
limite_sup = q3 + 1.5 * iqr
outliers = data[(data < limite_inf) | (data > limite_sup)]
print(f"LIMITES IQR: [{limite_inf}, {limite_sup}]")
print(f"OUTLIERS DETECTADOS: {outliers}")

# VARIOS CUARTILES DE UNA VEZ
cuartiles = np.quantile(data, [0.25, 0.50, 0.75])
print(f"TODOS A LA VEZ: {cuartiles}")
