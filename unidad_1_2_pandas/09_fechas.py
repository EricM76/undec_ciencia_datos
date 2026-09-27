from pathlib import Path

import pandas as pd
from tabulate import tabulate

ruta_archivo = (Path(__file__).parent.parent / 'DataSet'
                / 'certificados-personas-por-fecha-ingreso-provincia-localidad.csv')

# =====================================================================
# Lectura sin indicar fechas
# =====================================================================
datos = pd.read_csv(ruta_archivo)
print(tabulate(datos.head(5), headers="keys", tablefmt="psql"))

# Por defecto 'fecha_ingreso' se lee como TEXTO (str), no como fecha:
# no podríamos extraer el mes, el año, comparar rangos, etc.
print()
datos.info()

# =====================================================================
# pd.to_datetime: convertir texto a fecha (Timestamp)
# =====================================================================
# Formato ISO (año-mes-día): se interpreta sin ambigüedad.
print(f"\npd.to_datetime('2023-06-29'): {pd.to_datetime('2023-06-29')}")

# Formatos ambiguos: pandas "adivina" el orden y puede equivocarse.
# '9-6-2023' lo toma como mes-día-año -> 6 de septiembre.
print(f"pd.to_datetime('9-6-2023'):   {pd.to_datetime('9-6-2023')}")

# Con 'format' indicamos el orden exacto:
#   %d = día, %m = mes, %Y = año con 4 dígitos, %y = año con 2 dígitos.
print(f"pd.to_datetime('9-6-2023', format='%d-%m-%Y'): "
      f"{pd.to_datetime('9-6-2023', format='%d-%m-%Y')}")

# Aplicado a una columna completa: crea una nueva columna de tipo datetime64.
datos['fecha_ingreso_2'] = pd.to_datetime(datos['fecha_ingreso'])
print()
datos.info()
print(tabulate(datos.head(), headers="keys", tablefmt="psql"))

# =====================================================================
# Indicar las fechas al leer el CSV
# =====================================================================
# parse_dates: lista de columnas que deben interpretarse como fecha.
# (El notebook usa además 'date_parser', que fue eliminado en pandas 2;
#  hoy se usa 'date_format' para indicar el formato.)
datos2 = pd.read_csv(ruta_archivo, parse_dates=['fecha_ingreso'], date_format='%Y-%m-%d')
print("\ndatos2 con parse_dates:")
datos2.info()

# index_col: además, usar la fecha como índice del DataFrame.
# El índice resultante es un DatetimeIndex.
datos2 = pd.read_csv(ruta_archivo, parse_dates=['fecha_ingreso'],
                     date_format='%Y-%m-%d', index_col="fecha_ingreso")
print("\ndatos2 con la fecha como índice:")
print(tabulate(datos2.head(5), headers="keys", tablefmt="psql"))
print(f"\ndatos2.index:\n{datos2.index}")

# =====================================================================
# Acceder a día / mes / año con el accesor .dt
# =====================================================================
datos3 = pd.read_csv(ruta_archivo)
datos3['fecha_ingreso'] = pd.to_datetime(datos3['fecha_ingreso'], format='%Y-%m-%d')

# .dt da acceso a los componentes de una columna datetime.
# Otra forma: pd.DatetimeIndex(datos3['fecha_ingreso']).year
datos3['year'] = datos3['fecha_ingreso'].dt.year
datos3['month'] = datos3['fecha_ingreso'].dt.month
datos3['day'] = datos3['fecha_ingreso'].dt.day

print("\ndatos3 con year, month y day:")
print(tabulate(datos3.head(5), headers="keys", tablefmt="psql"))
datos3.info()

# =====================================================================
# Filtrar por fecha
# =====================================================================
# Con DatetimeIndex, loc acepta la fecha como texto (y también fechas
# parciales, ej. '2020-12' = todo diciembre de 2020).
print("\ndatos2.loc['2020-12-01'].head(5) -> fecha en el índice")
print(tabulate(datos2.loc["2020-12-01"].head(5), headers="keys", tablefmt="psql"))

# Con la fecha como columna, se usa una máscara booleana.
print("\ndatos3.loc[datos3['fecha_ingreso'] == '2020-12-01'].head(5) -> fecha en columna")
print(tabulate(datos3.loc[datos3["fecha_ingreso"] == "2020-12-01"].head(5),
               headers="keys", tablefmt="psql"))

# =====================================================================
# Semana del año y día de la semana
# =====================================================================
# isocalendar() devuelve año, semana y día según la norma ISO 8601.
datos3["semana"] = datos3['fecha_ingreso'].dt.isocalendar().week

# dayofweek: 0 = lunes ... 6 = domingo. day_name(): nombre del día.
datos3["dia_semana"] = datos3['fecha_ingreso'].dt.dayofweek
datos3["nombre_dia"] = datos3['fecha_ingreso'].dt.day_name()

print("\ndatos3 con semana y día de la semana:")
print(tabulate(datos3.head(10), headers="keys", tablefmt="psql"))

# Hay muchos más atributos, por ejemplo si la fecha es el primer día del mes:
# https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_month_start.html
print(f"\nFilas que caen en el primer día del mes: {datos3['fecha_ingreso'].dt.is_month_start.sum()}")
