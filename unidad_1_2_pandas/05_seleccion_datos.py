import pandas as pd
from tabulate import tabulate

area = pd.Series({'California': 423967, 'Texas': 695662,
                  'New York': 141297, 'Florida': 170312,
                  'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                 'New York': 19651127, 'Florida': 19552860,
                 'Illinois': 12882135})
data = pd.DataFrame({'area': area, 'pop': pop})
print("data:")
print(tabulate(data, headers="keys", tablefmt="psql"))

# =====================================================================
# Primeros / últimos n elementos
# =====================================================================
# head(n): primeras n filas (por defecto 5). tail(n): últimas n filas.
print("\ndata.head(2)")
print(tabulate(data.head(2), headers="keys", tablefmt="psql"))

print("\ndata.tail(3)")
print(tabulate(data.tail(3), headers="keys", tablefmt="psql"))

# =====================================================================
# Muestra aleatoria
# =====================================================================
# sample(n): n filas al azar. Cada ejecución da un resultado distinto,
# salvo que se fije random_state (semilla) para que sea reproducible.
print("\ndata.sample(2)")
print(tabulate(data.sample(2), headers="keys", tablefmt="psql"))

print("\ndata.sample(2, random_state=42) -> siempre las mismas filas")
print(tabulate(data.sample(2, random_state=42), headers="keys", tablefmt="psql"))

# =====================================================================
# Columnas
# =====================================================================
print("\ndata['area'] -> por nombre de columna")
print(data['area'])

print("\ndata.area -> como atributo")
print(data.area)

# Ambas formas devuelven exactamente el mismo objeto
print(f"\ndata['area'] is data.area: {data['area'] is data.area}")

# values: todos los datos como un numpy.ndarray (se pierden las etiquetas)
print(f"\ndata.values:\n{data.values}")

# =====================================================================
# Indexación con loc / iloc  [filas, columnas]
# =====================================================================
# iloc -> por POSICIÓN; el final del slice se EXCLUYE.
print("\ndata.iloc[:3, :2] -> filas 0 a 2, columnas 0 a 1")
print(tabulate(data.iloc[:3, :2], headers="keys", tablefmt="psql"))

# loc -> por ETIQUETA; el final del slice se INCLUYE.
print("\ndata.loc[:'Illinois', :'pop'] -> desde el inicio hasta 'Illinois' y hasta 'pop'")
print(tabulate(data.loc[:'Illinois', :'pop'], headers="keys", tablefmt="psql"))

# ---------- Boolean masking ----------
# data.area > 423000 produce una Series de True/False (la "máscara");
# loc se queda con las filas donde es True. ':' = todas las columnas.
print("\ndata.area > 423000 (máscara):")
print(data.area > 423000)
print("\ndata.loc[data.area > 423000, :]")
print(tabulate(data.loc[data.area > 423000, :], headers="keys", tablefmt="psql"))

# ---------- Fancy indexing ----------
# Pasar una LISTA de etiquetas; además permite reordenar las columnas.
print("\ndata.loc[:, ['pop', 'area']] -> columnas en otro orden")
print(tabulate(data.loc[:, ['pop', 'area']], headers="keys", tablefmt="psql"))

# ---------- Máscara booleana + fancy indexing ----------
print("\ndata.loc[data.area > 423000, ['pop', 'area']]")
print(tabulate(data.loc[data.area > 423000, ['pop', 'area']], headers="keys", tablefmt="psql"))

# =====================================================================
# Convenciones al indexar con UN solo índice: data[...]
# =====================================================================
# - Una lista (fancy indexing) se interpreta como COLUMNAS.
print("\ndata[['area', 'area']] -> lista = columnas (se puede repetir una)")
print(tabulate(data[['area', 'area']], headers="keys", tablefmt="psql"))

# - Un slice se interpreta como FILAS (por etiqueta, incluye el final)...
print("\ndata['Florida':'Illinois'] -> slice por etiqueta = filas")
print(tabulate(data['Florida':'Illinois'], headers="keys", tablefmt="psql"))

# ...o por posición (excluye el final).
print("\ndata[1:3] -> slice por posición = filas 1 y 2")
print(tabulate(data[1:3], headers="keys", tablefmt="psql"))

# - Una máscara booleana se aplica sobre FILAS.
print("\ndata[data.area > 423000] -> máscara = filas")
print(tabulate(data[data.area > 423000], headers="keys", tablefmt="psql"))

# =====================================================================
# Modificación de valores
# =====================================================================
# Crear una columna nueva a partir de una operación entre columnas.
# La operación se hace fila a fila (vectorizada), sin necesidad de un for.
data['density'] = data['pop'] / data['area']
print("\ndata con la nueva columna 'density' = pop / area")
print(tabulate(data, headers="keys", tablefmt="psql"))

# Cualquier forma de indexar sirve también para ASIGNAR valores.
# iloc[0, 2] -> fila 0 (California), columna 2 (density).
data.iloc[0, 2] = 90
print("\ndata después de data.iloc[0, 2] = 90")
print(tabulate(data, headers="keys", tablefmt="psql"))
