import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.experimental import enable_iterative_imputer  # noqa: F401 (habilita IterativeImputer)
from sklearn.impute import IterativeImputer
from sklearn.preprocessing import StandardScaler

##################################################################
# 1° Paso: Cargamos el DataSet y Realizamos la Exploración Inicial
##################################################################

data_location = Path(__file__).resolve().parent.parent / 'DataSet' / 'coffee_shop_sales.csv'
df_Coffe_Shop = pd.read_csv(data_location)

# Vista rápida de las primeras 5 filas
print(f"\nPrimeras filas:\n{df_Coffe_Shop.head()}")

# Total de filas y columnas, nombres de columnas y tipos de datos, valores no nulos y uso de memoria
print("\nInformación del DataFrame:\n")
df_Coffe_Shop.info()

# Descripción estadística de las variables numéricas
print(f"\nDescripción estadística:\n{df_Coffe_Shop.describe().T}")

##################################################################
# 2° Paso: Identificación de Datos Inconsistentes y Outliers
##################################################################

# 2_1 Valores negativos o nulos en cantidades, precios y totales
datos_inconsistentes = df_Coffe_Shop[
    (df_Coffe_Shop['quantity'] <= 0) | (df_Coffe_Shop['unit_price'] <= 0) | (df_Coffe_Shop['total_amount'] < 0)
]
print(f"\nRegistros con cantidad, precio o total inválidos: {len(datos_inconsistentes)}")

# 2_2 Categorías mal escritas: revisamos los valores únicos de las variables categóricas
columnas_texto = ['city', 'country', 'store_type', 'product_category', 'payment_method',
                  'customer_age_group', 'customer_gender', 'weather_condition', 'holiday_name']
print("\nValores únicos de las variables categóricas:")
for col in columnas_texto:
    print(f"{col}: {df_Coffe_Shop[col].unique()}")

# 2_3 Coherencia entre columnas
# Cada ciudad debe pertenecer a un único país y cada local a una única ciudad
print("\nPaíses por ciudad:")
print(df_Coffe_Shop.groupby('city')['country'].unique())
locales_multiciudad = (df_Coffe_Shop.groupby('store_id')['city'].nunique() > 1).sum()
print(f"Locales asociados a más de una ciudad: {locales_multiciudad}")

# El total debe ser precio x cantidad, menos el descuento cuando se aplicó
proporcion_pagada = (df_Coffe_Shop['total_amount'] / (df_Coffe_Shop['unit_price'] * df_Coffe_Shop['quantity'])).round(2)
print("\nProporción pagada del importe bruto según discount_applied:")
print(pd.crosstab(proporcion_pagada, df_Coffe_Shop['discount_applied']))
# Resultado: sin descuento se paga el 100%, con descuento entre el 80% y el 95%. Los totales son coherentes.


# 2_4 Detección de outliers con el rango intercuartílico (IQR)
def detectar_outliers(col):
    Q1 = df_Coffe_Shop[col].quantile(0.25)
    Q3 = df_Coffe_Shop[col].quantile(0.75)
    IQR = Q3 - Q1

    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR

    return df_Coffe_Shop[(df_Coffe_Shop[col] < limite_inferior) | (df_Coffe_Shop[col] > limite_superior)]


print("\nOutliers (IQR):")
for col in ['quantity', 'unit_price', 'total_amount', 'temperature_c']:
    print(f"{col}: {len(detectar_outliers(col))}")

print("\nCategorías de los productos con precio atípico:")
print(detectar_outliers('unit_price')['product_category'].value_counts())
# Los precios atípicos son casi todos de Merchandise (tazas, bolsas de café), más caro que una bebida,
# más algunos sándwiches y smoothies grandes; las cantidades altas (hasta 9) son compras posibles.
# Son valores reales, por lo que se conservan.

##################################################################
# 3° Paso: Manejo de Datos Faltantes
##################################################################

# 3_1 Identificamos los datos faltantes
print(f"\nValores nulos por columna:\n{df_Coffe_Shop.isnull().sum()}")

# Clima y temperatura faltan siempre juntos (falla el registro meteorológico de esa transacción)
print("\nNulos de weather_condition vs temperature_c:")
print(pd.crosstab(df_Coffe_Shop['weather_condition'].isnull(), df_Coffe_Shop['temperature_c'].isnull()))

# 3_2 Eliminación de filas con nulos
df_drop = df_Coffe_Shop.dropna()
print(f"\nFilas que quedarían con dropna(): {len(df_drop)} de {len(df_Coffe_Shop)}")
# holiday_name es nulo en casi todas las filas (los días que no son feriado), así que dropna()
# eliminaría el 98% del dataset. Ese nulo significa "no es feriado": es estructural, no un dato perdido.
df_Coffe_Shop['holiday_name'] = df_Coffe_Shop['holiday_name'].fillna('No Holiday')

# Las técnicas de imputación del apunte se prueban sobre una COPIA para compararlas
df_demo = df_Coffe_Shop.copy()

# 3_3 Imputación simple: la media para numéricas y la moda para categóricas
media_temperatura = df_demo['temperature_c'].mean()
moda_clima = df_demo['weather_condition'].mode()[0]
df_demo['temperature_c'] = df_demo['temperature_c'].fillna(media_temperatura)
df_demo['weather_condition'] = df_demo['weather_condition'].fillna(moda_clima)
print(f"\nImputación simple: temperatura con la media ({media_temperatura:.2f} °C), clima con la moda ('{moda_clima}')")

# 3_4 Imputación múltiple (MICE)
num_cols = df_Coffe_Shop.select_dtypes(include=np.number).columns
imputer = IterativeImputer(random_state=0)
df_demo_mice = df_Coffe_Shop.copy()
df_demo_mice[num_cols] = imputer.fit_transform(df_demo_mice[num_cols])
imputados = df_demo_mice.loc[df_Coffe_Shop['temperature_c'].isnull(), 'temperature_c']
print(f"MICE: temperaturas imputadas entre {imputados.min():.2f} y {imputados.max():.2f} °C")
# Las demás columnas numéricas (precio, cantidad, id del local) no explican la temperatura, así que
# MICE devuelve casi siempre la media global. Tanto la media global como MICE ignoran que la
# temperatura depende de la ciudad y de la época del año (Toronto en enero vs Sydney en enero).

# 3_5 Imputación elegida para el dataset final: media / moda por ciudad y mes
mes = pd.to_datetime(df_Coffe_Shop['timestamp']).dt.month
df_Coffe_Shop['temperature_c'] = df_Coffe_Shop['temperature_c'].fillna(
    df_Coffe_Shop.groupby(['city', mes])['temperature_c'].transform('mean').round(1)
)
df_Coffe_Shop['weather_condition'] = df_Coffe_Shop['weather_condition'].fillna(
    df_Coffe_Shop.groupby(['city', mes])['weather_condition'].transform(lambda s: s.mode()[0])
)

# Edad y género del cliente: no hay forma de deducirlos de otras columnas; imputar la moda
# inventaría clientes. Se usa una categoría explícita 'Unknown'.
df_Coffe_Shop['customer_age_group'] = df_Coffe_Shop['customer_age_group'].fillna('Unknown')
df_Coffe_Shop['customer_gender'] = df_Coffe_Shop['customer_gender'].fillna('Unknown')
print(f"\nNulos tras la imputación: {df_Coffe_Shop.isnull().sum().sum()}")

##################################################################
# 4° Paso: Manejo de Datos Duplicados y Errores de Codificación
##################################################################

# 4_1 Detección y eliminación de duplicados
print(f"\nDuplicados (todas las columnas): {df_Coffe_Shop.duplicated().sum()}")
# transaction_id es único por fila, así que también buscamos duplicados ignorándolo
print(f"Duplicados (sin transaction_id): {df_Coffe_Shop.drop(columns='transaction_id').duplicated().sum()}")
df_Coffe_Shop = df_Coffe_Shop.drop_duplicates()

# 4_2 Normalización del texto: quitamos espacios sobrantes en las variables categóricas
for col in columnas_texto + ['product_name']:
    df_Coffe_Shop[col] = df_Coffe_Shop[col].str.strip()

# 4_3 Corrección de categorías: verificamos que cada categoría aparezca escrita de una sola forma
# (misma palabra con distintas mayúsculas/minúsculas)
for col in columnas_texto + ['product_name']:
    valores = df_Coffe_Shop[col].unique()
    if len(valores) != len({v.lower() for v in valores}):
        print(f"{col}: hay categorías escritas de distintas formas")
print("Categorías revisadas: no se encontraron variantes a corregir.")

##################################################################
# 5° Paso: Mejoras en la Calidad de los Datos
##################################################################

# 5_1 Conversión de tipos: timestamp se leyó como texto
df_Coffe_Shop['timestamp'] = pd.to_datetime(df_Coffe_Shop['timestamp'], errors='coerce')
print(f"\nFechas inválidas tras la conversión: {df_Coffe_Shop['timestamp'].isnull().sum()}")
print(f"Rango de fechas: {df_Coffe_Shop['timestamp'].min()} a {df_Coffe_Shop['timestamp'].max()}")

# 5_2 Creación de variables derivadas
df_Coffe_Shop['month'] = df_Coffe_Shop['timestamp'].dt.month
df_Coffe_Shop['day_of_week'] = df_Coffe_Shop['timestamp'].dt.day_name()
df_Coffe_Shop['hour'] = df_Coffe_Shop['timestamp'].dt.hour
df_Coffe_Shop['gross_amount'] = (df_Coffe_Shop['unit_price'] * df_Coffe_Shop['quantity']).round(2)
df_Coffe_Shop['discount_amount'] = (df_Coffe_Shop['gross_amount'] - df_Coffe_Shop['total_amount']).round(2)
df_Coffe_Shop['is_holiday'] = df_Coffe_Shop['holiday_name'] != 'No Holiday'

# 5_3 Validación: el total no debe ser negativo ni superar el importe bruto
invalidos = (df_Coffe_Shop['total_amount'] < 0) | (df_Coffe_Shop['discount_amount'] < 0)
print(f"Registros con total negativo o mayor al bruto: {invalidos.sum()}")
df_Coffe_Shop = df_Coffe_Shop[~invalidos]

# 5_4 Estandarización (media 0, desvío 1) sobre una copia: el CSV final conserva precios y cantidades
# reales para poder interpretarlos; la estandarización se aplica recién al entrenar un modelo.
df_estandarizado = df_Coffe_Shop.copy()
scaler = StandardScaler()
df_estandarizado[['unit_price', 'quantity']] = scaler.fit_transform(df_estandarizado[['unit_price', 'quantity']])
print(f"\nPrecio y cantidad estandarizados:\n{df_estandarizado[['unit_price', 'quantity']].describe().round(2)}")

##################################################################
# 6° Paso: Los Riesgos que Puedo Tener
##################################################################

# - Pérdida de información: dropna() hubiera eliminado el 98% de las filas por los nulos de holiday_name.
# - Sesgo estadístico: imputar la temperatura con la media global mezcla ciudades y estaciones;
#   por eso se imputó por ciudad y mes.
# - Datos inventados: rellenar edad y género con la moda crearía clientes ficticios; se usó 'Unknown'.
# - Outliers reales eliminados: los precios altos son sobre todo de Merchandise y las cantidades altas son
#   compras posibles, por eso se conservaron.
# - Errores semánticos: si hubiera correcciones manuales de categorías, podrían agruparse mal.

##################################################################
# 7° Paso: Imprimir el DataSet Resultante y Guardar el Nuevo DataSet
##################################################################

print("\nDataset limpio:\n")
df_Coffe_Shop.info()

output_location = data_location.parent / 'coffee_shop_sales_limpio.csv'
df_Coffe_Shop.to_csv(output_location, index=False)
print(f"\nCSV exportado en: {output_location}")
