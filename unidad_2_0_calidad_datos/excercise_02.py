import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.experimental import enable_iterative_imputer  # noqa: F401 (habilita IterativeImputer)
from sklearn.impute import IterativeImputer

# Columnas que solo tienen valor cuando el estudiante recibió una oferta (Offer_Received = 1)
COLUMNAS_OFERTA = ['Time_to_Offer_Days', 'Offer_Salary', 'Company_Size_Offered', 'Role_Relevance', 'Accepted_Offer']

##################################################################
# 1° Paso: Cargamos el DataSet y Realizamos la Exploración Inicial
##################################################################

data_location = Path(__file__).resolve().parent.parent / 'DataSet' / 'job_search_platform_efficacy_100k.csv'
data = pd.read_csv(data_location)

# Total de filas y columnas, nombres de columnas y tipos de datos, valores no nulos y uso de memoria
print("\nInformación del DataFrame:\n")
data.info()

# Descripción estadística de las variables numéricas
print(f"\nDescripción estadística:\n{data.describe().T}")

# Cantidad de valores nulos por columna
print(f"\nValores nulos por columna:\n{data.isnull().sum()}")

# Los nulos aparecen solo en las columnas de la oferta: verificamos si coinciden con Offer_Received = 0
print("\nNulos en Offer_Salary según Offer_Received:")
print(pd.crosstab(data['Offer_Salary'].isnull(), data['Offer_Received']))
# Resultado: las 5 columnas de la oferta son nulas exactamente cuando no hubo oferta.
# Son nulos ESTRUCTURALES (el dato no existe), no datos perdidos: no deben imputarse en el dataset final.

##################################################################
# 2° Paso: Identificación de Datos Inconsistentes y Outliers
##################################################################

# 2_1 Categorías inválidas: revisamos los valores únicos de las variables categóricas
columnas_texto = data.select_dtypes(include=['object', 'str']).columns.drop('Student_ID')
print("\nValores únicos de las variables categóricas:")
for col in columnas_texto:
    print(f"{col}: {data[col].unique()[:10]}")

# 2_2 Valores lógicos fuera de rango
fuera_de_rango = {
    'Role_Relevance fuera de 0-10': (data['Role_Relevance'] < 0) | (data['Role_Relevance'] > 10),
    'GPA fuera de 0-4': (data['GPA'] < 0) | (data['GPA'] > 4),
    'Más entrevistas de 2° ronda que de 1°': data['Second_Round_Interviews'] > data['First_Round_Interviews'],
    'Más entrevistas de 1° ronda que postulaciones': data['First_Round_Interviews'] > data['Applications_Submitted'],
}
print("\nRegistros con datos inconsistentes:")
for regla, mascara in fuera_de_rango.items():
    print(f"{regla}: {mascara.sum()}")


# 2_3 Detección de outliers con el rango intercuartílico (IQR)
def detectar_outliers_iqr(df, col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    return df[(df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR)]


print("\nOutliers (IQR):")
for col in ['Role_Relevance', 'Offer_Salary', 'GPA', 'Applications_Submitted']:
    print(f"{col}: {len(detectar_outliers_iqr(data, col))}")
# Los outliers son valores posibles (p. ej. relevancia 1 o 2, o 300 postulaciones), no errores de carga,
# por lo que se conservan. El IQR señala valores atípicos, no necesariamente incorrectos.

##################################################################
# 3° Paso: Manejo de Datos Faltantes
##################################################################

# 3_1 Eliminación de filas con demasiados nulos: se conservan las filas con al menos 15 valores no nulos
data_drop = data.dropna(thresh=15)
print(f"\nFilas eliminadas con dropna(thresh=15): {data.shape[0] - data_drop.shape[0]}")
# Cada fila tiene 20 columnas y como máximo 5 nulos (15 valores no nulos), por lo que no se elimina ninguna.

# Las técnicas de imputación se aplican sobre una COPIA para practicarlas sin inventar datos en el dataset final
data_demo = data.copy()

# 3_2 Imputación con la media (variable numérica)
media_relevancia = data_demo['Role_Relevance'].mean()
data_demo['Role_Relevance'] = data_demo['Role_Relevance'].fillna(media_relevancia)
print(f"\nRole_Relevance imputada con la media ({media_relevancia:.2f}). Nulos: {data_demo['Role_Relevance'].isnull().sum()}")

# 3_3 Imputación con la moda (variable categórica)
# Se usa Company_Size_Offered porque University_Rating no tiene nulos
moda_empresa = data_demo['Company_Size_Offered'].mode()[0]
data_demo['Company_Size_Offered'] = data_demo['Company_Size_Offered'].fillna(moda_empresa)
print(f"Company_Size_Offered imputada con la moda ('{moda_empresa}'). Nulos: {data_demo['Company_Size_Offered'].isnull().sum()}")

# 3_4 Imputación múltiple (MICE): cada columna con nulos se estima con una regresión sobre las demás
columnas_numericas = data_demo.select_dtypes(include=np.number).columns
imputer = IterativeImputer(random_state=0)
data_demo[columnas_numericas] = imputer.fit_transform(data_demo[columnas_numericas])

print("\nOffer_Salary antes y después de MICE:")
print(pd.DataFrame({'original': data['Offer_Salary'].describe(), 'MICE': data_demo['Offer_Salary'].describe()}))
no_binarios = (~data_demo['Accepted_Offer'].isin([0, 1])).sum()
print(f"Valores de Accepted_Offer que dejaron de ser 0 o 1 tras MICE: {no_binarios}")
# MICE inventa salarios y aceptaciones para estudiantes sin oferta, y además convierte una variable
# binaria (0/1) en decimales. Por eso el dataset final conserva los nulos estructurales.

##################################################################
# 4° Paso: Manejo de Datos Duplicados y Errores de Codificación
##################################################################

# 4_1 Detección y eliminación de duplicados
print(f"\nDuplicados (todas las columnas): {data.duplicated().sum()}")
# Student_ID es único por fila, así que también buscamos duplicados ignorándolo
print(f"Duplicados (sin Student_ID): {data.drop(columns='Student_ID').duplicated().sum()}")
data = data.drop_duplicates()

# 4_2 Normalización del texto: quitamos espacios sobrantes en todas las variables categóricas
for col in columnas_texto:
    data[col] = data[col].str.strip()

# Pasamos University_Rating a minúsculas para unificar mayúsculas/minúsculas
data['University_Rating'] = data['University_Rating'].str.lower()

# 4_3 Corrección de categorías escritas de distintas formas
data['University_Rating'] = data['University_Rating'].replace({
    'mid tier': 'mid-tier',
    'lower tier': 'lower-tier',
    'top tier': 'top-tier'
})
print(f"\nCategorías de University_Rating: {data['University_Rating'].unique()}")

##################################################################
# 5° Paso: Mejoras en la Calidad de los Datos
##################################################################

# 5_1 Conversión de tipos: Accepted_Offer es 0/1 pero se leyó como float por los nulos.
# 'Int64' (con mayúscula) es el entero de pandas que admite nulos; astype('int') fallaría con NaN.
data['Accepted_Offer'] = data['Accepted_Offer'].astype('Int64')

# 5_2 Creación de variables derivadas: ofertas con relevancia alta (mayor a 7)
# Sin oferta queda como nulo (<NA>) y no como False, porque no hay relevancia que evaluar
data['High_Relevance'] = (data['Role_Relevance'] > 7).astype('boolean')
data.loc[data['Role_Relevance'].isnull(), 'High_Relevance'] = pd.NA

# 5_3 Validación final
print(f"\nValores nulos por columna:\n{data.isnull().sum()}")
nulos_con_oferta = data.loc[data['Offer_Received'] == 1, COLUMNAS_OFERTA + ['High_Relevance']].isnull().sum().sum()
print(f"Nulos en columnas de la oferta para estudiantes CON oferta: {nulos_con_oferta}")

##################################################################
# 6° Paso: Los Riesgos que Puedo Tener
##################################################################

# - Imputación incorrecta: rellenar nulos estructurales inventa datos (salarios de ofertas inexistentes).
# - Outliers no tratados: los detectados por IQR se conservaron por ser valores posibles; conviene
#   revisarlos si se entrena un modelo sensible a ellos (p. ej. regresión lineal).
# - Errores de codificación: categorías escritas de distintas formas se contarían como grupos distintos.
# - Datos duplicados: un identificador único (Student_ID) puede ocultar filas repetidas.

##################################################################
# 7° Paso: Guardar el Nuevo DataSet
##################################################################

output_location = data_location.parent / 'job_search_platform_efficacy_limpio.csv'
data.to_csv(output_location, index=False)
print(f"\nCSV exportado en: {output_location}")
