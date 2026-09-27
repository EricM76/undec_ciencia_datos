from pathlib import Path

import pandas as pd
from tabulate import tabulate

# En el notebook el archivo se lee desde Google Drive; acá se usa la carpeta
# DataSet del repositorio, relativa a la ubicación de este script.
ruta = Path(__file__).parent.parent / 'DataSet' / 'winemag-data-130k-v2.csv'

# Columnas cortas para imprimir (la columna 'description' es un texto muy largo)
COLS = ['country', 'points', 'price', 'province', 'variety']

# =====================================================================
# Lectura del dataset de reseñas de vinos
# =====================================================================
# read_csv lee un archivo de valores separados por comas y devuelve un DataFrame.
wine_reviews_df = pd.read_csv(ruta)
print("head():")
print(tabulate(wine_reviews_df.head(), headers="keys", tablefmt="psql"))

# 'Unnamed: 0' es una columna con números secuenciales (el índice que se guardó
# al exportar el CSV). No aporta información, así que la eliminamos.
del wine_reviews_df['Unnamed: 0']
# Equivalente: wine_reviews_df = wine_reviews_df.drop(columns=['Unnamed: 0'])
print("\nhead(2) sin 'Unnamed: 0':")
print(tabulate(wine_reviews_df.head(2)[COLS], headers="keys", tablefmt="psql"))


# =====================================================================
# Función de análisis descriptivo básico
# =====================================================================
def descriptivo(datos):
    """Imprime un resumen general de un DataFrame."""
    separador = "-" * 65 + "\n"

    print("\nHead")
    print(datos.head())
    print(separador)

    print("Nombre columnas")
    print(datos.columns)
    print(separador)

    # shape: tupla (cantidad de filas, cantidad de columnas)
    print("Shape")
    print(datos.shape)
    print(separador)

    # info() imprime por sí mismo tipos de datos, no nulos y memoria (devuelve None)
    print("Information")
    datos.info()
    print(separador)

    # describe(): estadísticos (count, mean, std, min, cuartiles, max)
    # de las columnas numéricas
    print("Describe")
    print(datos.describe())
    print(separador)

    # isna() marca con True los faltantes; sum() cuenta los True por columna
    print("Datos ausentes")
    print(datos.isna().sum())
    print(separador)


descriptivo(wine_reviews_df)

# =====================================================================
# Máximos y mínimos
# =====================================================================
# max(): el valor máximo. idxmax(): la ETIQUETA del índice donde aparece
# (si hay varios máximos, devuelve el primero).
max_point = wine_reviews_df["points"].max()
print(f"Puntaje máximo: {max_point}")
print(f"Índice del primer vino con puntaje máximo: {wine_reviews_df['points'].idxmax()}")

# Fila completa del vino con más puntos. Acá iloc funciona porque el índice es
# 0, 1, 2, ... (etiqueta == posición); en general conviene loc con idxmax.
print("\nVino con puntaje máximo:")
print(wine_reviews_df.iloc[wine_reviews_df["points"].idxmax()])

# loc permite combinar la etiqueta de la fila con el nombre de una columna
print("\nDescripción de ese vino:")
print(wine_reviews_df.loc[wine_reviews_df["points"].idxmax(), "description"])

print("\nVino con puntaje mínimo:")
print(wine_reviews_df.iloc[wine_reviews_df["points"].idxmin()])

# ¿Cuántos vinos tienen el puntaje máximo? Filtro con máscara booleana.
maximos = wine_reviews_df[wine_reviews_df['points'] == max_point]
print(f"\nCantidad de vinos con {max_point} puntos: {len(maximos)}")
print(tabulate(maximos[["country", "designation", "price"]], headers="keys", tablefmt="psql"))

# =====================================================================
# Tamaño y datos faltantes
# =====================================================================
filas, columnas = wine_reviews_df.shape
print(f"\nEl dataset tiene {filas} filas y {columnas} columnas")

print("\nValores faltantes por columna:")
print(wine_reviews_df.isna().sum())

# Porcentaje: faltantes / total de filas * 100
print("\nPorcentaje de valores faltantes por columna:")
print((wine_reviews_df.isna().sum() / wine_reviews_df.shape[0]) * 100)
