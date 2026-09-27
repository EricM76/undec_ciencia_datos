from pathlib import Path

import pandas as pd
from tabulate import tabulate

ruta = Path(__file__).parent.parent / 'DataSet' / 'winemag-data-130k-v2.csv'
wine_reviews_df = pd.read_csv(ruta)
del wine_reviews_df['Unnamed: 0']

# Misma limpieza que en 07_valores_faltantes.py
df = wine_reviews_df.copy(deep=True)
mean_price = df['price'].mean()
df['price'] = df['price'].fillna(mean_price)
df = df.fillna(value={'designation': 'dato faltante',
                      'region_1': 'dato faltante',
                      'region_2': 'dato faltante'})
df = df.dropna(axis=0)

COLS = ['country', 'points', 'price', 'province', 'variety']

# =====================================================================
# Filtro por máscara
# =====================================================================
# Igual que en NumPy: una comparación sobre una columna devuelve una Series
# de booleanos (la máscara), y df[mascara] se queda con las filas True.
mask_country = df['country'] == 'US'
print("Máscara country == 'US':")
print(mask_country)

print(f"\nForma del DataFrame filtrado: {df[mask_country].shape}")
print(tabulate(df[mask_country].head(5)[COLS], headers="keys", tablefmt="psql"))

# =====================================================================
# Funciones de DataFrames / Series
# =====================================================================

# a) ¿Qué valores distintos hay en la columna country?
#    unique() devuelve un array con cada valor sin repetir.
print("\na) Países únicos:")
print(df['country'].unique())

# b) ¿Cuántos valores distintos hay?
#    nunique() cuenta directamente los valores únicos.
print(f"\nb) Cantidad de países: {len(df['country'].unique())} (len + unique)")
print(f"   Cantidad de países: {df['country'].nunique()} (nunique)")

# c) ¿Cuántas veces aparece cada país?
#    value_counts() cuenta las apariciones, ordenadas de mayor a menor.
print("\nc) Frecuencia absoluta por país:")
print(df['country'].value_counts())

# normalize=True devuelve proporciones (0 a 1); * 100 -> porcentaje.
print("\n   Frecuencia relativa (%) por país:")
print(df['country'].value_counts(normalize=True) * 100)

# d) y e) Precio máximo y mínimo
print(f"\nd) Precio máximo: {df['price'].max()}")
print(f"e) Precio mínimo: {df['price'].min()}")

# f) ¿Cuál es el vino más caro?
#    Se filtra comparando contra el máximo: así aparecen TODOS los empatados
#    (idxmax devolvería solo el primero).
print("\nf) Vino/s más caro/s:")
print(tabulate(df[df["price"] == df["price"].max()][COLS], headers="keys", tablefmt="psql"))

# g) ¿Cuántos vinos tienen un precio por encima de la media?
mask_avg_price = df["price"] > mean_price
mayormedia = df[mask_avg_price]
print(f"\ng) Vinos con precio mayor a la media: {len(mayormedia)} (len)")
print(f"   Vinos con precio mayor a la media: {mayormedia.shape[0]} (shape[0])")
print(tabulate(mayormedia.head()[COLS], headers="keys", tablefmt="psql"))

# Ejercicio: ¿cuáles son los vinos más baratos?
mas_baratos = df[df["price"] == df["price"].min()]
print(f"\nVinos más baratos: {mas_baratos.shape[0]}")
print(tabulate(mas_baratos[COLS], headers="keys", tablefmt="psql"))
