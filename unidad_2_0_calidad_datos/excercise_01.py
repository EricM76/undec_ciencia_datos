import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

##################################################################
# 1° Paso: Cargamos el DataSet y Realizamos la Exploración Inicial
##################################################################

data_location = Path(__file__).resolve().parent.parent / 'DataSet' / 'linkedin-jobs-usa.csv'
data = pd.read_csv(data_location, sep=',', encoding='latin1')

# ¿Cuántas filas y columnas tiene el DataFrame?
print(f"\nFilas: {data.shape[0]}")
print(f"Columnas: {data.shape[1]}")

# Primeros 5 registros
print(f"\nPrimeros 5 registros:")
print(f"\n{data.head()}")

# Información del DataFrame
print(f"\nInformación del DataFrame:\n")
data.info()

##################################################################
# 2° Paso: Tratamientos de Datos Duplicados
##################################################################

# ¿Cuántos registros duplicados hay en el DataFrame?
print(f"\nDuplicados (todas las columnas): {data.duplicated().sum()}")

# Los links traen parámetros de seguimiento distintos (?refId=...&trackingId=...) para la misma oferta
data['link'] = data['link'].str.split('?').str[0]
print(f"Duplicados (link sin parámetros): {data['link'].duplicated().sum()}")

data = data.drop_duplicates(subset='link')
print(f"Filas tras eliminar duplicados: {data.shape[0]}")

##################################################################
# 3° Paso: Tratamientos de Datos Nulos
##################################################################

# ¿Cuántos valores nulos hay en el DataFrame?
print(f"\nValores nulos:\n{data.isnull().sum()}")

# 3_1 Eliminación de filas que contienen valores nulos
data_sin_filas_nulas = data.dropna()
print(f"\nFilas tras eliminar valores nulos: {data_sin_filas_nulas.shape[0]}")

# 3_2 Eliminación de columnas que contienen valores nulos
data_sin_columnas_nulas = data.dropna(axis=1)
print(f"\nColumnas tras eliminar columnas con valores nulos: {data_sin_columnas_nulas.shape[1]}")

##################################################################
# 4° Paso: Transformación de los Datos
##################################################################

# 4_1 Convertir 'salary' de texto ("$80,000.00 - $100,000.00") al promedio numérico del rango
# ADVERTENCIA: el dataset no indica si cada salario es por hora, mensual o anual, por lo que
# la columna mezcla escalas (min = 23, 25% = 50, mediana = 67.500). Se corrige en el paso 5_3.
rango = data['salary'].str.replace(r'[$,\s]', '', regex=True).str.split('-', expand=True)
salario_min = pd.to_numeric(rango[0])
salario_max = pd.to_numeric(rango[1])
data['salary'] = (salario_min + salario_max) / 2
print(f"\nSalary numérico:\n{data['salary'].describe()}")

##################################################################
# 5° Paso: Vemos el DataFrame en Forma Gráfica
##################################################################

# 5_1 Boxplot de la columna 'salary' (matplotlib no admite NaN al calcular los cuartiles)
plt.boxplot(data['salary'].dropna())

# Le añadimos la etiqueta y el título
plt.xlabel('Salarios')
plt.ylabel('Valores en USD')
plt.title('Boxplot')
plt.show()

# 5_2 Histograma de la columna 'salary'
plt.hist(data['salary'].dropna(), bins=30, color='blue', alpha=0.7)
plt.xlabel('Valores en USD')
plt.ylabel('Frecuencia')
plt.title('Histograma de Salarios')
plt.show()

# 5_3 Eliminamos los salarios menores a 50.000 (salarios por hora), conservando los nulos para imputarlos
data = data[data['salary'].isnull() | (data['salary'] >= 50000)]
print(f"\nFilas tras eliminar salarios menores a 50.000: {data.shape[0]}")

plt.hist(data['salary'].dropna(), bins=30, color='blue', alpha=0.7)
plt.xlabel('Valores en USD')
plt.ylabel('Frecuencia')
plt.title('Histograma de Salarios (>= 50.000)')
plt.show()

##################################################################
# 6° Paso: Reemplazamos los Valores Nulos con la Media
##################################################################

# 6_1 Rellenamos los NaNs de 'salary' con la media de la columna
# ADVERTENCIA: imputar con la media no cambia la media, pero sí distorsiona la distribución:
# la mayoría de los valores quedan iguales, la desviación estándar baja y los cuartiles colapsan en la media.
data_imputada = data.copy()
media_salario = data_imputada['salary'].mean()
data_imputada['salary'] = data_imputada['salary'].fillna(media_salario)
print(f"\nMedia de salary: {media_salario:,.2f}")
print(f"Nulos en salary tras imputar: {data_imputada['salary'].isnull().sum()}")
print(f"\nSalary tras imputar:\n{data_imputada['salary'].describe()}")

##################################################################
# 7° Paso: Agrupamos y Agregamos Datos
##################################################################

# Agrupamos por título y calculamos la media, la mediana y la cantidad de ofertas
data_agrupada = data_imputada.groupby('title')['salary'].agg(['mean', 'median', 'count']).reset_index()
data_agrupada.columns = ['title', 'salary_mean', 'salary_median', 'job_count']

data_agrupada['salary_mean'] = data_agrupada['salary_mean'].round(0).astype(int)
data_agrupada['salary_median'] = data_agrupada['salary_median'].round(0).astype(int)

data_agrupada = data_agrupada.sort_values('job_count', ascending=False)
print(f"\nSalario por título:\n{data_agrupada.to_string(index=False)}")

##################################################################
# 8° Paso: Exportamos el CSV Resultante
##################################################################

output_location = data_location.parent / 'nuevo_linkedin_jobs_usa.csv'
data_imputada.to_csv(output_location, index=False)
print(f"\nCSV exportado en: {output_location}")
