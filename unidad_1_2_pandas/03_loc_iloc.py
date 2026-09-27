import pandas as pd
from tabulate import tabulate

area = pd.Series({'California': 423967, 'Texas': 695662, 'New York': 141297, 'Florida': 170312, 'Illinois': 149995})
population = pd.Series({'California': 38332521, 'Texas': 26448193, 'New York': 19651127, 'Florida': 19552860, 'Illinois': 12882135})
states = pd.DataFrame({'population': population, 'area': area})

print("states:")
print(tabulate(states, headers="keys", tablefmt="psql"))

# loc: selecciona por ETIQUETA (nombre del índice / nombre de la columna)
# iloc: selecciona por POSICIÓN (número entero, empieza en 0)

# ---------- UNA FILA ----------
print("\nloc['Texas'] -> fila con etiqueta 'Texas'")
print(states.loc['Texas'])

print("\niloc[1] -> segunda fila (posición 1)")
print(states.iloc[1])

# ---------- UN VALOR (fila, columna) ----------
print(f"\nloc['Texas', 'area']: {states.loc['Texas', 'area']}")
print(f"iloc[1, 1]: {states.iloc[1, 1]}")

# ---------- RANGOS (slicing) ----------
# loc INCLUYE el final; iloc lo EXCLUYE (como range en Python)
print("\nloc['California':'New York'] -> incluye 'New York'")
print(tabulate(states.loc['California':'New York'], headers="keys", tablefmt="psql"))

print("\niloc[0:3] -> posiciones 0, 1 y 2 (excluye la 3)")
print(tabulate(states.iloc[0:3], headers="keys", tablefmt="psql"))

# ---------- LISTAS DE FILAS Y COLUMNAS ----------
print("\nloc[['Florida', 'Illinois'], ['area']]")
print(tabulate(states.loc[['Florida', 'Illinois'], ['area']], headers="keys", tablefmt="psql"))

print("\niloc[[3, 4], [1]] -> filas 3 y 4, columna 1")
print(tabulate(states.iloc[[3, 4], [1]], headers="keys", tablefmt="psql"))

# ---------- TODAS LAS FILAS, UNA COLUMNA ----------
# ':' significa "todas"
print("\nloc[:, 'population']")
print(states.loc[:, 'population'])

print("\niloc[:, 0] -> primera columna")
print(states.iloc[:, 0])

# ---------- POSICIONES NEGATIVAS (solo iloc) ----------
print("\niloc[-1] -> última fila")
print(states.iloc[-1])

# ---------- FILTRO BOOLEANO (solo loc) ----------
# La condición devuelve una Series de True/False; loc se queda con las filas True
print("\nloc[states['area'] > 200000] -> estados con área mayor a 200.000")
print(tabulate(states.loc[states['area'] > 200000], headers="keys", tablefmt="psql"))

print("\nloc[states['population'] > 19_600_000, ['population']]")
print(tabulate(states.loc[states['population'] > 19_600_000, ['population']], headers="keys", tablefmt="psql"))

# ---------- MODIFICAR VALORES ----------
# Se usa la misma sintaxis a la izquierda del '='
states_copia = states.copy()  # copia para no alterar el original
states_copia.loc['Texas', 'area'] = 0
states_copia.iloc[0, 0] = 0  # California, population
print("\nstates_copia después de modificar con loc e iloc:")
print(tabulate(states_copia, headers="keys", tablefmt="psql"))
