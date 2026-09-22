import numpy as np

# BASICA: raiz cuadrada de la varianza (mismas unidades que los datos)
xs = np.array([8, 5, -1])
desvio = np.std(xs)  # por defecto ddof=0 (poblacion)
print(f"DATOS: {xs}")
print(f"DESVIO ESTANDAR (ddof=0): {desvio}")
print(f"VERIFICACION: sqrt(var) = {np.sqrt(np.var(xs))}")

# MUESTRAL: divide por n-1
desvio_muestra = np.std(xs, ddof=1)
print(f"DESVIO MUESTRAL (ddof=1): {desvio_muestra}")

# INTERPRETACION: datos mas "apretados" tienen menor desvio
notas_homogeneas = np.array([7, 7, 8, 8, 7])
notas_heterogeneas = np.array([2, 10, 4, 9, 5])
print(f"HOMOGENEAS: media={np.mean(notas_homogeneas)}, std={np.std(notas_homogeneas):.2f}")
print(f"HETEROGENEAS: media={np.mean(notas_heterogeneas)}, std={np.std(notas_heterogeneas):.2f}")

# EFECTO DEL OUTLIER: el desvio crece mucho con valores extremos
sin_outlier = np.array([30, 36, 47, 50, 52, 52, 56, 60, 63, 70, 70])
con_outlier = np.array([30, 36, 47, 50, 52, 52, 56, 60, 63, 70, 70, 110])
print(f"SIN OUTLIER: std={np.std(sin_outlier):.2f}")
print(f"CON OUTLIER: std={np.std(con_outlier):.2f}")

# VENTAJA vs VARIANZA: el desvio se interpreta en la misma unidad (ej. pesos, cm)
print(f"UNIDADES: var={np.var(xs):.2f} (al cuadrado), std={np.std(xs):.2f} (misma unidad)")
