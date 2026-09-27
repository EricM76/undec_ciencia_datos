from pathlib import Path

import pandas as pd
from tabulate import tabulate

ruta = Path(__file__).parent.parent / 'DataSet' / 'winemag-data-130k-v2.csv'
wine_reviews_df = pd.read_csv(ruta)
del wine_reviews_df['Unnamed: 0']

# Misma limpieza que en 07_valores_faltantes.py
df = wine_reviews_df.copy(deep=True)
df['price'] = df['price'].fillna(df['price'].mean())
df = df.fillna(value={'designation': 'dato faltante',
                      'region_1': 'dato faltante',
                      'region_2': 'dato faltante'})
df = df.dropna(axis=0)

# =====================================================================
# Group by
# =====================================================================
# groupby separa el DataFrame en grupos según los valores de una o más
# columnas; luego una función de agregación resume cada grupo en una fila.
# Esquema: dividir -> aplicar -> combinar.
group_by_country = df.groupby('country')
print(f"Objeto devuelto por groupby: {type(group_by_country)}")

# count(): cantidad de valores no nulos de cada columna, por país.
print("\ngroup_by_country.count().head()")
print(tabulate(group_by_country.count().head(), headers="keys", tablefmt="psql"))

# mean(): promedio por país. Solo tiene sentido en columnas numéricas
# (points y price); por eso el resultado tiene menos columnas.
# En pandas >= 2.0 hay que indicarlo con numeric_only=True, si no da error
# al intentar promediar columnas de texto.
print("\ngroup_by_country.mean(numeric_only=True).head()")
print(tabulate(group_by_country.mean(numeric_only=True).head(), headers="keys", tablefmt="psql"))

# ---------- Agrupar por varias columnas ----------
# El resultado tiene un índice de dos niveles (MultiIndex): país y provincia.
group_by_country_prov = df.groupby(['country', 'province'])
print("\ngroupby(['country', 'province']).mean(numeric_only=True).head()")
print(group_by_country_prov.mean(numeric_only=True).head())

# as_index=False: las columnas de agrupación quedan como columnas comunes
# y el índice es 0, 1, 2, ...
group_by_country_prov = df.groupby(['country', 'province'], as_index=False)
print("\ngroupby(['country', 'province'], as_index=False).mean(numeric_only=True).head()")
print(tabulate(group_by_country_prov.mean(numeric_only=True).head(), headers="keys", tablefmt="psql"))

# ---------- Distintas agregaciones por columna con agg ----------
# agg recibe un diccionario {columna: [funciones]}.
# Precio medio por país y cantidad de reseñas (count de points).
group_by_country_agg = df.groupby(['country'], as_index=False).agg({'price': ['mean'],
                                                                    'points': ['count']})
# agg con listas genera nombres de columna de dos niveles (('price', 'mean'), ...);
# los reemplazamos por nombres simples.
group_by_country_agg.columns = ["Country", 'Price mean', 'Points count']
print("\nagg({'price': ['mean'], 'points': ['count']})")
print(tabulate(group_by_country_agg.head(), headers="keys", tablefmt="psql"))

# =====================================================================
# Sort values
# =====================================================================
# sort_values(by=[...], ascending=[...]) ordena según una o más columnas.
print("\nTabla ascendente por 'Points count'")
print(tabulate(group_by_country_agg.sort_values(by=['Points count'], ascending=[True]).head(),
               headers="keys", tablefmt="psql"))

print("\nTabla descendente por 'Points count'")
print(tabulate(group_by_country_agg.sort_values(by=['Points count'], ascending=[False]).head(),
               headers="keys", tablefmt="psql"))
