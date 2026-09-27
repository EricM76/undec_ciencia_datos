import pandas as pd

# Lista de valores numéricos (floats)
lista = [0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]

# Series: estructura unidimensional de pandas (como una columna con índice)
# Por defecto, el índice es 0, 1, 2, 3...
data = pd.Series(lista)

print(f"data: {data}")  # muestra índice | valor


print(f"data.values: {data.values}")  # muestra solo los valores

# RangeIndex: objeto que describe el índice (inicio, fin exclusivo, paso)
# No imprime [0, 1, 2, 3, ..., 7], sino RangeIndex(start=0, stop=8, step=1)
print(f"data.index: {data.index}")

print(f"data.dtype: {data.dtype}")  # muestra el tipo de datos

print(f"data.shape: {data.shape}")  # forma de la serie: (n,) — n elementos

print(f"data.size: {data.size}")  # muestra el número de elementos

print(f"data.head(): {data.head()}")  # muestra las primeras 5 filas