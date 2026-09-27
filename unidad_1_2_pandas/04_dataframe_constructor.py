import numpy as np
import pandas as pd
from tabulate import tabulate

# =====================================================================
# DataFrame como un diccionario de Series "alineadas"
# =====================================================================
# Un DataFrame es una tabla: cada columna es una Series y todas comparten
# el mismo índice (las etiquetas de las filas).

# 1) Series con el área de algunos estados, creada desde un diccionario:
#    las keys pasan a ser el índice y los values los datos.
area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
             'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)
print("area:")
print(area)

# 2) Series con la población, creada desde dos listas (valores + índice).
#    Notar que el orden de los estados es DISTINTO al de 'area'.
states_list = ['Illinois', 'Texas', 'New York', 'Florida', 'California']
states_pop = [12882135, 26448193, 19651127, 19552860, 38332521]
population = pd.Series(states_pop, index=states_list)
print("\npopulation:")
print(population)

# 3) DataFrame a partir de las dos Series.
#    Pandas ALINEA por etiqueta: el valor de 'Texas' en area queda en la
#    misma fila que el valor de 'Texas' en population, sin importar el orden.
states = pd.DataFrame({'population': population, 'area': area})
print("\nstates:")
print(tabulate(states, headers="keys", tablefmt="psql"))

# index: etiquetas de las filas / columns: etiquetas de las columnas.
# Ambos son objetos de tipo Index.
print(f"\nstates.index:   {states.index}")
print(f"states.columns: {states.columns}")

# =====================================================================
# DataFrame como un diccionario especializado
# =====================================================================
# Así como un dict mapea key -> valor, un DataFrame mapea
# nombre de columna -> Series.

print("\nstates['area'] -> acceso tipo diccionario")
print(states['area'])

print("\nstates.area -> acceso como atributo (solo si el nombre no tiene espacios"
      " ni coincide con un método del DataFrame)")
print(states.area)

# Ambas formas devuelven una Series
print(f"\ntype(states['area']): {type(states['area'])}")
print(f"type(states.area):    {type(states.area)}")

# ¿Qué diferencia hay entre == e is?
#   'is' compara IDENTIDAD: si ambos nombres apuntan al mismo objeto en memoria.
#   '==' compara VALORES elemento a elemento y devuelve una Series de booleanos.
print(f"\nstates['area'] is states.area: {states['area'] is states.area}")
print("states['area'] == states.area:")
print(states['area'] == states.area)

# =====================================================================
# Constructores de DataFrame
# =====================================================================
# Documentación: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

# ---------- Desde una Series ----------
# Una Series es una sola columna; con 'columns' le damos nombre.
print("\npd.DataFrame(population, columns=['population'])")
print(tabulate(pd.DataFrame(population, columns=['population']), headers="keys", tablefmt="psql"))

# ---------- Desde una lista de diccionarios ----------
# Cada diccionario es una FILA; las keys son los nombres de columna.
dict_0 = {'a': 0, 'b': 0}
dict_1 = {'a': 1, 'b': 2}
dict_2 = {'a': 2, 'b': 4}
data = [dict_0, dict_1, dict_2]
print("\npd.DataFrame(lista_de_dicts)")
print(tabulate(pd.DataFrame(data), headers="keys", tablefmt="psql"))

# Lo mismo, generando la lista con una lista por comprensión
data = [{'a': i, 'b': 2 * i} for i in range(3)]
print(f"\nlista por comprensión: {data}")
print(tabulate(pd.DataFrame(data), headers="keys", tablefmt="psql"))

# Si a un diccionario le falta alguna key, pandas completa con NaN
# (Not a Number = dato faltante).
print("\nkeys faltantes -> NaN")
print(tabulate(pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]), headers="keys", tablefmt="psql"))

# ---------- Desde un array NumPy de dos dimensiones ----------
# Matriz de 3 filas x 2 columnas con números aleatorios entre 0 y 1.
array_2d = np.random.rand(3, 2)
print(f"\narray_2d:\n{array_2d}")

# columns e index le ponen etiquetas; su largo debe coincidir con la forma del array.
columns_names = ['foo', 'bar']
rows_names = ['a', 'b', 'c']
print("\npd.DataFrame(array_2d, columns=..., index=...)")
print(tabulate(pd.DataFrame(array_2d, columns=columns_names, index=rows_names), headers="keys", tablefmt="psql"))
