import numpy as np

# Correlacion: covarianza estandarizada
# Acotada entre -1 y 1; sin unidades
# +1: relacion lineal perfecta positiva
# -1: relacion lineal perfecta negativa
#  0: sin relacion lineal

# Ejemplo de la teoria
x = np.array([-2.1, -1, 4.3])
y = np.array([3, 1.1, 0.12])

# FUERTE POSITIVA
horas = np.array([1, 2, 3, 4, 5])
notas = np.array([4, 5, 6, 8, 9])
r_pos = np.corrcoef(horas, notas)[0, 1]
print(f"FUERTE POSITIVA (horas vs notas): r={r_pos:.3f}") #r=0.991

# FUERTE NEGATIVA
precio = np.array([10, 20, 30, 40, 50])
demanda = np.array([90, 70, 55, 40, 20])
r_neg = np.corrcoef(precio, demanda)[0, 1]
print(f"FUERTE NEGATIVA (precio vs demanda): r={r_neg:.3f}") #r=-0.998

# DEBIL / NULA
ruido = np.array([3, 8, 1, 9, 4])
r_nula = np.corrcoef(horas, ruido)[0, 1]
print(f"DEBIL/NULA (sin relacion): r={r_nula:.3f}") #r=0.140

# MATRIZ DE CORRELACION (como en la teoria)
X = np.array([x, y])
matriz = np.corrcoef(X)
print(f"DATOS X:\n{X}")
print(f"MATRIZ DE CORRELACION:\n{matriz}")
print("-> Diagonal siempre 1 (cada variable correlaciona perfecto consigo)")

# VENTAJA vs COVARIANZA: la correlacion es comparable entre pares de variables
# aunque tengan escalas distintas
a = np.array([1, 2, 3, 4, 5])
b_cm = a * 10  # misma relacion, otra escala
b_mm = a * 100
print(f"misma relacion en cm: r={np.corrcoef(a, b_cm)[0, 1]:.1f}")
print(f"misma relacion en mm: r={np.corrcoef(a, b_mm)[0, 1]:.1f}")
print(f"pero covarianza cambia: {np.cov(a, b_cm, ddof=0)[0, 1]} vs {np.cov(a, b_mm, ddof=0)[0, 1]}")

# RELACION CON COVARIANZA: r = cov / (sx * sy)
cov = np.cov(horas, notas, ddof=0)[0, 1]
r_manual = cov / (np.std(horas) * np.std(notas))
print(f"CHEQUEO: corrcoef={r_pos:.3f}, manual={r_manual:.3f}")
