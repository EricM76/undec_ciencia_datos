from pathlib import Path

import pandas as pd

ruta = Path(__file__).parent.parent / 'DataSet' / 'winemag-data-130k-v2.csv'
wine_reviews_df = pd.read_csv(ruta)
del wine_reviews_df['Unnamed: 0']

# =====================================================================
# ¿Qué hacemos con los faltantes?
# =====================================================================
# fillna(): IMPUTA (rellena) los valores faltantes con otro valor.
# dropna(): ELIMINA las filas (axis=0) o columnas (axis=1) con faltantes.
# Para ver la documentación: help(pd.DataFrame.fillna) / help(pd.DataFrame.dropna)

# copy(deep=True) crea un DataFrame independiente: los cambios sobre df
# no afectan al original wine_reviews_df.
df = wine_reviews_df.copy(deep=True)

print("Faltantes por columna (antes):")
print(df.isna().sum())

# ---------- fillna con un valor calculado ----------
# Rellenamos los precios faltantes con el precio promedio.
# mean() ignora los NaN al calcular.
mean_price = df['price'].mean()
df['price'] = df['price'].fillna(mean_price)
print(f"\nPrecio medio usado para imputar: {mean_price:.2f}")

print("\nFaltantes después de imputar 'price' (debe dar 0):")
print(df.isna().sum())

# ---------- fillna con un diccionario ----------
# Se indica un valor por columna: {columna: valor_de_relleno}.
default_value = "dato faltante"
df = df.fillna(value={'designation': default_value,
                      'region_1': default_value,
                      'region_2': default_value})

print("\nFaltantes después de rellenar designation, region_1 y region_2:")
print(df.isna().sum())

# ---------- dropna ----------
# Para el resto de las columnas (country, taster_name, etc.) descartamos
# las filas que tengan AL MENOS un valor faltante.
filas_antes = df.shape[0]
df = df.dropna(axis=0)

print(f"\nFilas del dataset original:  {wine_reviews_df.shape[0]}")
print(f"Filas antes de dropna:        {filas_antes}")
print(f"Filas después de dropna:      {df.shape[0]}")
print(f"Filas eliminadas:             {wine_reviews_df.shape[0] - df.shape[0]}")

print("\nFaltantes al final (todo en 0):")
print(df.isna().sum())
