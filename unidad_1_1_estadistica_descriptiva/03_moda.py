import numpy as np
from scipy import stats
from collections import Counter

# UNIMODAL: un solo valor se repite más que el resto
# 4 aparece 4 veces; el resto menos
data = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
moda = stats.mode(data, keepdims=True) # keepdims=True para que devuelva un array de una dimensión
print(f"UNIMODAL: La moda es {int(moda.mode[0])} (aparece {int(moda.count[0])} veces)")

# BIMODAL: dos valores empatan en la máxima frecuencia
# 3 y 4 aparecen 4 veces cada uno
data = np.array([1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5])

# tolist() para convertir el array a una lista
conteo = Counter(data.tolist()) 

# max() para obtener el valor máximo de la frecuencia
max_freq = max(conteo.values())

# sorted() para ordenar las modas
modas = sorted([valor for valor, freq in conteo.items() if freq == max_freq])

print(f"BIMODAL: Las modas son {modas} (aparecen {max_freq} veces cada una)")

# Nota: stats.mode solo devuelve una (la menor)
print(f"  (stats.mode solo muestra: {int(stats.mode(data, keepdims=True).mode[0])})")

# SIN MODA CLARA: todos los valores aparecen una sola vez
data = np.array([1, 2, 3, 4, 5])

# tolist() para convertir el array a una lista
conteo = Counter(data.tolist())

# max() para obtener el valor máximo de la frecuencia
max_freq = max(conteo.values())

# sorted() para ordenar las modas
modas = sorted([valor for valor, freq in conteo.items() if freq == max_freq])
print(f"SIN MODA UNICA: todos aparecen {max_freq} vez -> candidatos {modas}")

# CATEGORICA: la moda también sirve con datos no numéricos
colores = ["rojo", "azul", "rojo", "verde", "azul", "rojo"]

conteo = Counter(colores)

# most_common(1) para obtener la moda
moda_color = conteo.most_common(1)[0]
print(f"CATEGORICA: La moda es '{moda_color[0]}' (aparece {moda_color[1]} veces)")
