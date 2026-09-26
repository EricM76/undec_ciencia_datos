## Ejercicio 4
# Podemos usar el desvío estándar o la distancia intercuartil para comprarar la dispersión en las ventas de USA y Japan
# durante el 2004. ¿Qué podemos decir sobre la dispersión en esos dos países durante ese año?

import os

import numpy as np

# Armamos la ruta al CSV relativa a este script (carpeta DataSet un nivel arriba)
data_location = os.path.join(
    os.path.dirname(__file__), "..", "DataSet", "sales_data_sample_excercise.csv"
)

# Leemos todo como texto (dtype=str) porque el CSV mezcla numeros y cadenas
# skip_header=1 saltea la fila de nombres de columnas; delimiter="\t" indica tabulacion
data = np.genfromtxt(data_location, skip_header=1, delimiter="\t", dtype=str)

# Extraemos las columnas que necesitamos por indice (ndarray[:, col])
# Columna 1 = SALES -> la convertimos a float para poder calcular estadisticos
sales = data[:, 1].astype(float)
# Columna 3 = YEAR_ID (queda como string, ej. "2004")
year = data[:, 3]
# Columna 5 = COUNTRY (queda como string, ej. "USA", "Japan")
country = data[:, 5]

# Mascara booleana: True solo en las filas del anio 2004
mask_2004 = year == "2004"

# Filtramos SALES combinando pais + anio con & (AND elemento a elemento)
# Resultado: un array con solo las ventas de ese pais en 2004
sales_usa_2004 = sales[(country == "USA") & mask_2004]
sales_japan_2004 = sales[(country == "Japan") & mask_2004]


def calcular_iqr(valores):
    """IQR = Q3 - Q1: mide la dispersion del 50% central de los datos (robusto a outliers)."""
    # Percentil 25 = Q1 (25% de los datos estan por debajo)
    # Percentil 75 = Q3 (75% de los datos estan por debajo)
    q1, q3 = np.percentile(valores, [25, 75])
    # Devolvemos tambien Q1 y Q3 para poder mostrarlos despues
    return q1, q3, q3 - q1


# Desvio estandar: dispersion promedio respecto de la media (sensible a valores extremos)
# np.std usa ddof=0 por defecto (formula poblacional)
std_usa = np.std(sales_usa_2004)
std_japan = np.std(sales_japan_2004)

# Distancia intercuartil (IQR) para cada pais
q1_usa, q3_usa, iqr_usa = calcular_iqr(sales_usa_2004)
q1_japan, q3_japan, iqr_japan = calcular_iqr(sales_japan_2004)

# Contexto: cuantas observaciones hay en cada grupo (Japan tiene muchas menos)
print(f"Cantidad de ventas USA 2004: {len(sales_usa_2004)}")
print(f"Cantidad de ventas Japan 2004: {len(sales_japan_2004)}")
print()

# Mostramos ambas medidas de dispersion lado a lado para comparar
print(f"USA 2004  -> desvio estandar={std_usa:.2f}, IQR={iqr_usa:.2f} (Q1={q1_usa:.2f}, Q3={q3_usa:.2f})")
print(
    f"Japan 2004 -> desvio estandar={std_japan:.2f}, IQR={iqr_japan:.2f} (Q1={q1_japan:.2f}, Q3={q3_japan:.2f})"
)
print()

# Comparacion 1: segun el desvio estandar (mayor valor = mas dispersion)
# Ojo: el desvio se infla si hay ventas muy altas (outliers)
if std_japan > std_usa:
    print("Por desvio estandar: Japan tiene mayor dispersion que USA en 2004.")
else:
    print("Por desvio estandar: USA tiene mayor (o igual) dispersion que Japan en 2004.")

# Comparacion 2: segun el IQR (mayor valor = mas dispersion en el 50% central)
# El IQR casi no se ve afectado por extremos porque ignora colas
if iqr_usa > iqr_japan:
    print("Por IQR: USA tiene mayor dispersion en el 50% central que Japan en 2004.")
else:
    print("Por IQR: Japan tiene mayor (o igual) dispersion en el 50% central que USA en 2004.")

# Conclusion:
# - Segun el desvio estandar, Japan dispersa un poco mas (1972.72 > 1792.17).
# - Segun el IQR, USA dispersa un poco mas en el 50% central (2121.19 > 1965.03).
# - La diferencia entre medidas se explica porque el desvio es sensible a valores extremos,
#   mientras el IQR es mas robusto (solo mira Q1 y Q3).
# - En ambos paises la dispersion es similar en magnitud; no hay una diferencia marcada.
print(
    "Conclusion general: la dispersion es comparable entre ambos paises; "
    "el desvio sugiere ligeramente mas dispersion en Japan (posible efecto de extremos), "
    "mientras el IQR sugiere ligeramente mas dispersion central en USA."
)
