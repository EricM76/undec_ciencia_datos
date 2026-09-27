# =============================================================================
# Ejercicio 1
# =============================================================================
#
# Busquemos en la documentación de pandas la sintaxis del método `read_csv` y
# leamos en un `DataFrame` llamado `data` los datos del archivo
# /DataSet/data_filt.csv
# (https://drive.google.com/file/d/1qaNC6mBn9HD9VCVKFVqh5IaOZYrMZNqM/view?usp=sharing)
#
# Este archivo tiene algunos datos numéricos y otros de tipo cadena de caracteres.
#
# Columnas:
#   - ch06     (int)    : edad
#   - nivel_ed (string) : nivel educativo
#   - htot     (int)    : cantidad de horas totales trabajadas en el período
#   - calif    (string) : calificación de la tarea
#   - p47t     (int)    : ingreso
#
# Consignas:
#   1. Mostrar los primeros tres registros y los últimos cinco.
#   2. ¿Cuántas filas y cuántas columnas tiene `data`?
#   3. ¿Cuáles son los nombres de las columnas?
#   4. ¿Cuál es el índice del DataFrame?
#   5. Renombrar las columnas con estos valores:
#      ['edad', 'nivel_educativo', 'hs_trabajados', 'calif_ocupacional', 'ingreso_ult_mes']
#   6. ¿Cuál es el tipo de datos de la cuarta columna de `data`?
#   7. ¿Cómo están distribuidos los niveles educativos? ¿Cuál es el más común?
#   8. ¿Cuál es el ingreso medio de la población?
#   9. Construir un DataFrame con las columnas `nivel_educativo` e
#      `ingreso_ult_mes` de `data`.
#  10. Seleccionar las primeras 20 filas de ese DataFrame.
#  11. Seleccionar una muestra aleatoria de 500 filas de ese DataFrame.
#  12. Construir un DataFrame con todas las columnas de `data` excluyendo
#      `nivel_educativo`.
#  13. Ordenar `data` según la columna `edad` en forma decreciente.
#  14. ¿Cuál es el promedio de horas trabajadas de los jóvenes entre 14 y 25
#      años y poco calificados?
#  15. Generar un nuevo DataFrame con los trabajadores que ganan más del
#      promedio de ingresos general y están por debajo de la cantidad media de
#      horas trabajadas. ¿Cuántos trabajadores cumplen esta condición?
#      ¿Cuál es su edad mediana?
# =============================================================================

from pathlib import Path

import pandas as pd


# --- Carga de datos ----------------------------------------------------------
data_location = Path(__file__).resolve().parent.parent / 'DataSet' / 'data_filt.csv'
data = pd.read_csv(data_location, sep=',', encoding='latin1')

# --- Información general -----------------------------------------------------
print(f"Información sobre el DataFrame:\n{data.info()}")

# --- Dimensiones (filas y columnas) ------------------------------------------
print(f"\nFilas: {data.shape[0]}")
print(f"Columnas: {data.shape[1]}")

# --- Primeros y últimos registros --------------------------------------------
print(f"\nPrimeros 3 registros:\n{data.head(3)}")
print(f"\nÚltimos 5 registros:\n{data.tail(5)}")

# --- Nombres de columnas e índice --------------------------------------------
print(f"\nNombres de las columnas:\n{data.columns}")
print(f"\nÍndice del DataFrame:\n{data.index}")

# --- Renombrar columnas ------------------------------------------------------
data.columns = ['edad', 'nivel_educativo', 'hs_trabajados', 'calif_ocupacional', 'ingreso_ult_mes']
print(f"\nNombres de las columnas (renombradas):\n{data.columns}")

# --- Tipo de datos de la cuarta columna --------------------------------------
cuarta_columna = data.columns[3]
print(f"\nTipo de datos de la cuarta columna ('{cuarta_columna}'): {data[cuarta_columna].dtype}")

# --- Distribución de los niveles educativos ----------------------------------
distribucion_nivel_ed = data['nivel_educativo'].value_counts()
print(f"\nDistribución de los niveles educativos:\n{distribucion_nivel_ed}")
print(f"\nNivel educativo más común: {distribucion_nivel_ed.idxmax()}")

# --- Ingreso medio de la población -------------------------------------------
ingreso_medio = data['ingreso_ult_mes'].mean()
print(f"\nIngreso medio de la población: {ingreso_medio:.2f}")

# --- DataFrame con nivel educativo e ingreso ---------------------------------
nivel_ingreso = data[['nivel_educativo', 'ingreso_ult_mes']]
print(f"\nDataFrame con nivel educativo e ingreso:\n{nivel_ingreso}")

# --- Primeras 20 filas -------------------------------------------------------
primeras_20 = nivel_ingreso.head(20)
print(f"\nPrimeras 20 filas:\n{primeras_20}")

# --- Muestra aleatoria de 500 filas ------------------------------------------
muestra_500 = nivel_ingreso.sample(n=500, random_state=42)
print(f"\nMuestra aleatoria de 500 filas:\n{muestra_500}")

# --- DataFrame sin la columna nivel_educativo --------------------------------
sin_nivel_ed = data.drop(columns='nivel_educativo')
print(f"\nDataFrame sin 'nivel_educativo':\n{sin_nivel_ed}")

# --- Ordenar por edad (decreciente) ------------------------------------------
data_ordenada = data.sort_values(by='edad', ascending=False)
print(f"\nData ordenada por edad (decreciente):\n{data_ordenada}")

# --- Horas promedio de jóvenes (14 a 25 años) poco calificados ---------------
jovenes_poco_calif = data[
    data['edad'].between(14, 25)
    & (data['calif_ocupacional'] == '2_Op./No calif.')
]
horas_promedio_jovenes = jovenes_poco_calif['hs_trabajados'].mean()
print(f"\nHoras promedio de jóvenes (14-25) poco calificados: {horas_promedio_jovenes:.2f}")

# --- Ganan más que el promedio y trabajan menos horas que la media -----------
horas_media = data['hs_trabajados'].mean()
ganan_mas_trabajan_menos = data[
    (data['ingreso_ult_mes'] > ingreso_medio)
    & (data['hs_trabajados'] < horas_media)
]
print(f"\nTrabajadores que ganan más del promedio y trabajan menos que la media: "
      f"{len(ganan_mas_trabajan_menos)}")
print(f"Edad mediana de esos trabajadores: {ganan_mas_trabajan_menos['edad'].median()}")
