import numpy as np

# Covarianza: mide si dos variables se mueven juntas
# > 0: tienden a subir/bajar juntas
# < 0: cuando una sube, la otra baja
# ~ 0: no hay asociacion lineal clara
# Unidades: producto de las unidades de X e Y (dificil de interpretar)

# Ejemplo de la teoria
x = np.array([-2.1, -1, 4.3])
y = np.array([3, 1.1, 0.12])

# POSITIVA: horas de estudio vs nota
horas = np.array([1, 2, 3, 4, 5])
notas = np.array([4, 5, 6, 8, 9])
cov_pos = np.cov(horas, notas, ddof=0)[0, 1]
print(f"POSITIVA (horas vs notas): cov={cov_pos:.2f}")

# NEGATIVA: precio vs demanda
precio = np.array([10, 20, 30, 40, 50])
demanda = np.array([90, 70, 55, 40, 20])
cov_neg = np.cov(precio, demanda, ddof=0)[0, 1]
print(f"NEGATIVA (precio vs demanda): cov={cov_neg:.2f}")

# CERCANA A CERO: sin relacion lineal
ruido = np.array([3, 8, 1, 9, 4])
cov_cero = np.cov(horas, ruido, ddof=0)[0, 1]
print(f"CERCA DE CERO (sin relacion): cov={cov_cero:.2f}")

# MATRIZ DE COVARIANZAS (como en la teoria)
X = np.array([x, y])
matriz = np.cov(X)  # por defecto ddof=1 (muestral)
print(f"DATOS X:\n{X}")
print(f"MATRIZ DE COVARIANZAS:\n{matriz}")
print("-> Diagonal: varianzas de cada variable")
print("-> Fuera de diagonal: covarianza entre variables")

# POBLACION vs MUESTRA
print(f"ddof=0 (poblacion):\n{np.cov(X, ddof=0)}")
print(f"ddof=1 (muestra):\n{np.cov(X, ddof=1)}")
