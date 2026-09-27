import calendar
from pathlib import Path

import pandas as pd
from tabulate import tabulate

ruta_archivo = (Path(__file__).parent.parent / 'DataSet'
                / 'certificados-personas-por-fecha-ingreso-provincia-localidad.csv')

datos3 = pd.read_csv(ruta_archivo)
datos3['fecha_ingreso'] = pd.to_datetime(datos3['fecha_ingreso'], format='%Y-%m-%d')
datos3['year'] = datos3['fecha_ingreso'].dt.year
datos3['month'] = datos3['fecha_ingreso'].dt.month
datos3['day'] = datos3['fecha_ingreso'].dt.day

# ---------------------------------------------------------------------
# 1) Cómo ver el día de la semana
# ---------------------------------------------------------------------
print("1) Fila 100:")
print(datos3.loc[100])

# Cada elemento de la columna es un Timestamp, con atributos y métodos propios.
fecha = datos3["fecha_ingreso"][1]
print(f"\nFecha de la fila 1: {fecha}")
print(f"Mes: {fecha.month}")

# weekday(): 0 = lunes ... 6 = domingo. El módulo calendar traduce números a nombres.
print(f"Día de la semana: {calendar.day_name[fecha.weekday()]}")
print(f"Nombre del mes:   {calendar.month_name[fecha.month]}")

# ---------------------------------------------------------------------
# 2) Primeras 5, últimas 5 y 5 filas al azar
# ---------------------------------------------------------------------
print("\n2) head(5)")
print(tabulate(datos3.head(5), headers="keys", tablefmt="psql"))
print("tail(5)")
print(tabulate(datos3.tail(5), headers="keys", tablefmt="psql"))
print("sample(5)")
print(tabulate(datos3.sample(5), headers="keys", tablefmt="psql"))

# ---------------------------------------------------------------------
# 3) ¿Cuántas filas y columnas tiene el dataset?
# ---------------------------------------------------------------------
print(f"\n3) shape (filas, columnas): {datos3.shape}")

# ---------------------------------------------------------------------
# 4) ¿Cuántos valores nulos hay en cada columna?
# ---------------------------------------------------------------------
# isna() -> DataFrame de True/False; sum() cuenta los True por columna.
print("\n4) Nulos por columna:")
print(datos3.isna().sum())

# ---------------------------------------------------------------------
# 5) ¿Qué porcentaje de valores nulos hay en cada columna?
# ---------------------------------------------------------------------
print("\n5) Porcentaje de nulos por columna:")
print((datos3.isna().sum() / datos3.shape[0]) * 100)

# ---------------------------------------------------------------------
# 6) ¿Cuántos valores distintos hay en destino_provincia y destino_localidad?
# ---------------------------------------------------------------------
print("\n6) Provincias únicas:")
print(datos3['destino_provincia'].unique())
print(f"Cantidad de provincias: {datos3['destino_provincia'].nunique()}")
print(f"Cantidad de localidades: {datos3['destino_localidad'].nunique()}")

# value_counts: cuántas filas hay por cada fecha
print("\nFilas por fecha:")
print(datos3['fecha_ingreso'].value_counts())

# ---------------------------------------------------------------------
# 7) Convertir destino_provincia a minúsculas
# ---------------------------------------------------------------------
# apply ejecuta la función sobre cada elemento de la columna.
datos3['destino_provincia'] = datos3['destino_provincia'].apply(lambda x: str.lower(x))
# Forma vectorizada (más rápida) con el accesor .str:
# datos3['destino_provincia'] = datos3['destino_provincia'].str.lower()
print("\n7) Provincias en minúsculas:")
print(datos3['destino_provincia'].unique())

# ---------------------------------------------------------------------
# 8) Media y mediana de cantidad_personas
# ---------------------------------------------------------------------
media_antes = datos3["cantidad_personas"].mean()
mediana = datos3["cantidad_personas"].median()
print(f"\n8) Media: {media_antes:.4f} | Mediana: {mediana}")

# ---------------------------------------------------------------------
# 9) Completar los nulos con la mediana y recalcular la media
# ---------------------------------------------------------------------
# Al rellenar con un valor menor que la media, la media baja. La mediana se usa
# porque es robusta frente a valores extremos (outliers).
datos3["cantidad_personas"] = datos3["cantidad_personas"].fillna(mediana)
media_despues = datos3["cantidad_personas"].mean()
print(f"\n9) Media después de imputar con la mediana: {media_despues:.4f}")
print(f"   Variación respecto del punto 8: {media_despues - media_antes:.4f}")

# ---------------------------------------------------------------------
# 10) Fecha mínima y máxima de ingreso
# ---------------------------------------------------------------------
print(f"\n10) Fecha mínima: {datos3['fecha_ingreso'].min()}")
print(f"    Fecha máxima: {datos3['fecha_ingreso'].max()}")

# ---------------------------------------------------------------------
# 11) ¿Cuántos certificados se emitieron en febrero de 2021?
# ---------------------------------------------------------------------
# Las condiciones se combinan con & (y) / | (o), cada una entre paréntesis.
mask_mes_anio = (datos3['month'] == 2) & (datos3['year'] == 2021)
print(f"\n11) Certificados en febrero de 2021: "
      f"{datos3[mask_mes_anio]['cantidad_certificados'].sum()}")

# 11.1) Certificados por cada año y mes.
# Agrupar solo por 'month' mezclaría el mismo mes de años distintos;
# por eso se agrupa por ['year', 'month'].
print("\n11.1) Agrupado solo por mes:")
print(datos3.groupby(['month']).agg({'cantidad_certificados': ["sum"]}))

print("\n11.1) Agrupado por año y mes:")
print(datos3.groupby(['year', 'month'], as_index=False).agg({'cantidad_certificados': ["sum"]}))


# ---------------------------------------------------------------------
# 12) Función remove_spaces
# ---------------------------------------------------------------------
def remove_spaces(string: str) -> str:
    """Devuelve el string recibido sin espacios."""
    return string.replace(" ", "")


print(f"\n12) remove_spaces('Mar del Plata') -> {remove_spaces('Mar del Plata')}")

# ---------------------------------------------------------------------
# 13) Aplicar remove_spaces sobre destino_localidad con apply
# ---------------------------------------------------------------------
# Se pasa la función sin paréntesis: apply la llama con cada valor.
datos3['sin_espacio'] = datos3['destino_localidad'].apply(remove_spaces)
print("\n13) Localidades sin espacios:")
print(datos3[['destino_localidad', 'sin_espacio']].head(5))

# ---------------------------------------------------------------------
# 14) Agrupar por destino_provincia
# ---------------------------------------------------------------------
group_by_destino_provincia = datos3.groupby(['destino_provincia'])

# Total de certificados y de personas. Para seleccionar varias columnas del
# grupo se usa una LISTA (doble corchete).
print("\n14) Certificados y personas por provincia:")
print(group_by_destino_provincia[['cantidad_certificados', 'cantidad_personas']].sum())

# Fecha del último certificado emitido
fecha_final = datos3.groupby(['destino_provincia'], as_index=False).agg({'fecha_ingreso': ["max"]})
fecha_final.columns = ["Provincia", 'Fecha final']
print("\n14) Fecha del último certificado por provincia:")
print(tabulate(fecha_final, headers="keys", tablefmt="psql"))

# ---------------------------------------------------------------------
# 15) Provincia con más certificados en enero de 2021
# ---------------------------------------------------------------------
mask = (datos3["month"] == 1) & (datos3["year"] == 2021)

certificados_totales = datos3[mask].groupby(['destino_provincia'], as_index=False).agg(
    {'cantidad_certificados': ["sum"]})
certificados_totales.columns = ["Provincia", 'Certificados totales']
print("\n15) Certificados por provincia en enero de 2021:")
print(tabulate(certificados_totales, headers="keys", tablefmt="psql"))

# idxmax devuelve la etiqueta de la fila con el máximo; loc trae esa fila.
print("\nProvincia con más certificados:")
print(certificados_totales.loc[certificados_totales['Certificados totales'].idxmax()])
