import numpy as np
import pandas as pd

# =====================================================================
# Pandas y la Series
# =====================================================================
# - Pandas ("Panel Data System") está construido sobre NumPy.
# - A diferencia de NumPy, permite datos de distintos tipos (entre columnas)
#   e identificar filas y columnas con ETIQUETAS, no solo con enteros.
# - Una Series es un vector unidimensional formado por:
#     * un array de valores (todos del mismo tipo)
#     * un array de etiquetas asociado, llamado ÍNDICE
# - Si no se indica índice, se asigna 0, 1, ..., N-1.

# =====================================================================
# Series como generalización de un array de NumPy
# =====================================================================
# Array de NumPy: índice entero IMPLÍCITO (la posición).
# Series: índice EXPLÍCITO, que puede no ser entero y hasta tener repetidos.
array = np.array([0.25, 0.5, 0.75, 1.0])
print(f"array NumPy: {array} -> array[1] = {array[1]}")

valores = [0.25, 0.5, 0.75, 1.0]
etiquetas = ['a', 'b', 'c', 'd']
etiquetas_num = [2, 5, 3, 1]
data1 = pd.Series(valores, index=etiquetas)      # índice de texto
data2 = pd.Series(valores, index=etiquetas_num)  # índice de enteros desordenados
print(f"\ndata1:\n{data1}")
print(f"\ndata2:\n{data2}")

# ---------- Acceso por etiqueta ----------
print(f"\ndata1['b'] = {data1['b']}")
print(f"data2[5]   = {data2[5]}  -> 5 es una ETIQUETA, no una posición")

# ---------- El problema: acceso por "posición" con [] ----------
# Con índice entero, data2[1] busca la ETIQUETA 1 (el último elemento),
# no la segunda posición. Por eso devuelve 1.0 y no 0.5.
print(f"\ndata2[1] = {data2[1]}  -> etiqueta 1, NO la posición 1")

# Con índice de texto, versiones viejas de pandas interpretaban data1[1] como
# posición. Desde pandas 3.0, [] con un entero siempre busca una etiqueta,
# así que da KeyError.
try:
    print(data1[1])
except KeyError as e:
    print(f"data1[1] -> KeyError: {e} (no existe la etiqueta 1)")

# ---------- La solución: loc e iloc ----------
# iloc ("integer location") -> siempre por POSICIÓN.
# loc                       -> siempre por ETIQUETA.
# Usarlos evita la ambigüedad de [].
print(f"\ndata1.iloc[1] = {data1.iloc[1]}  |  data2.iloc[1] = {data2.iloc[1]}  -> segunda posición")
print(f"data1.loc['b'] = {data1.loc['b']}  |  data2.loc[5]  = {data2.loc[5]}  -> por etiqueta")

# =====================================================================
# Series como un diccionario especializado
# =====================================================================
# Al crearla desde un dict, las keys pasan a ser el índice.
population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict)

print(f"\ninstancia de diccionario:\n{population_dict}")
print(f"\ninstancia de Series:\n{population}")

# Misma sintaxis para leer un valor
print(f"\npopulation['California']      = {population['California']}")
print(f"population_dict['California'] = {population_dict['California']}")

# A diferencia de un dict, la Series admite slicing:
# - con etiquetas (índice explícito) el final SE INCLUYE
print("\npopulation['California':'Florida'] -> incluye 'Florida'")
print(population['California':'Florida'])

# - con posiciones (índice implícito) el final NO se incluye
#   (se recomienda population.iloc[0:3] para dejarlo explícito)
print("\npopulation[0:3] -> posiciones 0, 1 y 2")
print(population[0:3])

# El slicing por etiqueta respeta el ORDEN del índice, no el alfabético
states_list = ['Illinois', 'Texas', 'New York', 'Florida', 'California']
states_pop = [12882135, 26448193, 19651127, 19552860, 38332521]
states = pd.Series(states_pop, index=states_list)
print("\nstates['Illinois':'New York']")
print(states['Illinois':'New York'])

# =====================================================================
# Otras formas de construir una Series
# =====================================================================
# 1) Desde una lista (o array de NumPy)
print(f"\npd.Series([2, 4, 6]):\n{pd.Series([2, 4, 6])}")

# 2) Un escalar repetido a lo largo del índice
print(f"\npd.Series(5, index=[100, 200, 300]):\n{pd.Series(5, index=[100, 200, 300])}")

# 3) Desde un diccionario (se respeta el orden de inserción de las keys)
print(f"\npd.Series({{2: 'a', 1: 'b', 3: 'c'}}):\n{pd.Series({2: 'a', 1: 'b', 3: 'c'})}")

# En todos los casos se puede indicar un índice explícito.
# El índice puede tener etiquetas REPETIDAS:
repetidos = pd.Series([2, 4, 6], index=[3, 2, 2])
print(f"\npd.Series([2, 4, 6], index=[3, 2, 2]):\n{repetidos}")
# ...y al buscar una etiqueta repetida se obtiene una Series, no un único valor
print(f"\nrepetidos.loc[2]:\n{repetidos.loc[2]}")

# Con un dict + index, el index SELECCIONA y ORDENA las keys a usar
# (puede repetirlas; si una etiqueta no está en el dict, queda NaN).
tmp = pd.Series({2: 'a', 1: 'b', 3: 'c'}, index=[3, 2, 2, 1])
print(f"\npd.Series({{2: 'a', 1: 'b', 3: 'c'}}, index=[3, 2, 2, 1]):\n{tmp}")
