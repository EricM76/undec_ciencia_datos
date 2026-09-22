import numpy as np

# BASICA: mide cuanto se alejan los datos de la media (unidades al cuadrado)
xs = np.array([8, 5, -1])
varianza = np.var(xs)  # por defecto divide por n (poblacion)
print(f"DATOS: {xs}")
print(f"VARIANZA (ddof=0, poblacion): {varianza}")

# PASO A PASO: promedio de (x_i - media)^2
media = np.mean(xs)
desvios_al_cuadrado = (xs - media) ** 2
varianza_manual = np.mean(desvios_al_cuadrado)
print(f"MANUAL: media={media}, desvios^2={desvios_al_cuadrado} -> var={varianza_manual}")

# MUESTRA vs POBLACION: en muestras suele usarse n-1 (ddof=1)
varianza_muestra = np.var(xs, ddof=1)
print(f"VARIANZA MUESTRAL (ddof=1): {varianza_muestra}")

# COMPARACION: datos concentrados vs dispersos
concentrados = np.array([10, 11, 10, 9, 10])
dispersos = np.array([2, 18, 5, 20, 5])
print(f"CONCENTRADOS: media={np.mean(concentrados)}, var={np.var(concentrados)}")
print(f"DISPERSOS: media={np.mean(dispersos)}, var={np.var(dispersos)}")

# RELACION CON EL DESVIO: var == std**2
print(f"CHEQUEO: var == std**2 ? {np.var(xs) == np.std(xs) ** 2}")
