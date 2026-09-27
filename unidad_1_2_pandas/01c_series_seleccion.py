import pandas as pd

data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
print(f"data:\n{data}")

# =====================================================================
# Series como array de una dimensión: slicing, masking, fancy indexing
# =====================================================================

# ---------- Slicing explícito (por etiqueta): el final SE INCLUYE ----------
print("\ndata['a':'c']")
print(data['a':'c'])

# ---------- Slicing implícito (por posición): el final NO se incluye ----------
print("\ndata[0:2]")
print(data[0:2])

# ---------- Boolean masking ----------
# Cada condición genera una Series de True/False. Se combinan con
# & (y), | (o), ~ (no); cada condición va entre paréntesis porque
# & tiene más prioridad que > y <.
mascara = (data > 0.3) & (data < 0.8)
print(f"\nmáscara (data > 0.3) & (data < 0.8):\n{mascara}")
print(f"\ndata[mascara]:\n{data[mascara]}")

# ---------- Fancy indexing ----------
# Se pasa una LISTA de etiquetas; se pueden repetir y cambiar el orden.
print(f"\ndata[['a', 'd', 'b', 'b']]:\n{data[['a', 'd', 'b', 'b']]}")

# El notebook usa data[['a', 'e']]: 'e' no existe en el índice.
# En versiones viejas devolvía NaN; hoy lanza KeyError.
try:
    print(data[['a', 'e']])
except KeyError as e:
    print(f"\ndata[['a', 'e']] -> KeyError: {e}")

# Si se quieren incluir etiquetas inexistentes (con NaN), se usa reindex
print(f"\ndata.reindex(['a', 'e', 'e', 'b']):\n{data.reindex(['a', 'e', 'e', 'b'])}")

# =====================================================================
# Indexers: loc (por etiqueta) e iloc (por posición)
# =====================================================================

# ---------- loc ----------
# Doc: https://pandas.pydata.org/docs/reference/api/pandas.Series.loc.html
# Acepta una etiqueta, un slice de etiquetas, una lista o un array de booleanos.
print(f"\ndata.loc['a'] = {data.loc['a']}")
print(f"\ndata.loc['a':'c']:\n{data.loc['a':'c']}")

# Lista de booleanos: se queda con las posiciones donde hay True.
# Debe tener EXACTAMENTE la misma cantidad de elementos que la Series.
filtro = [True, False, False, True]
print(f"\ndata.loc[{filtro}]:\n{data.loc[filtro]}")

# ¿Qué pasa si el filtro tiene más o menos elementos que la Series?
# En ambos casos: IndexError.
for filtro_mal in ([True, False, False, True, False], [True, False]):
    try:
        print(data.loc[filtro_mal])
    except IndexError as e:
        print(f"\ndata.loc[{filtro_mal}] -> IndexError: {e}")

# ---------- iloc ----------
# Doc: https://pandas.pydata.org/docs/reference/api/pandas.Series.iloc.html
# Solo acepta posiciones enteras (como un array de NumPy).
print(f"\ndata.iloc[1] = {data.iloc[1]}")
print(f"\ndata.iloc[0:3]:\n{data.iloc[0:3]}")

posiciones = [0, 2, 3]
print(f"\ndata.iloc[{posiciones}]:\n{data.iloc[posiciones]}")

# La posición 4 no existe (las posiciones válidas son 0 a 3) -> IndexError
posiciones = [0, 2, 4]
try:
    print(data.iloc[posiciones])
except IndexError as e:
    print(f"\ndata.iloc[{posiciones}] -> IndexError: {e}")
