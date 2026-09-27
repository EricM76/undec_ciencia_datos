# Ejercicio DataFrame
import pandas as pd

cantidades_prod1 = pd.Series([3, 7, 1], index=['local_a', 'local_b', 'local_c'])
cantidades_prod2 = pd.Series([54, 70, 985], index=['local_a', 'local_b', 'local_c'])

# Construir una instancia de DataFrame usando las dos series del ejercicio anterior como columnas.
df = pd.DataFrame({
    'cantidades_prod1': cantidades_prod1,
    'cantidades_prod2': cantidades_prod2
})
print(df)

# Agregar al dataframe del paso anterior la columna 'total' cuyos datos sean el resultado de sumar las columnas 'cantidades_prod1' y 'cantidades_prod2'
df['total'] = df['cantidades_prod1'] + df['cantidades_prod2']
print(df)

# Mostrar los primeros dos registros de ese dataframe
print(df.head(2))

# Mostrar los últimos dos registros de ese dataframe
print(df.tail(2))

# Obtener los nombres de locales que tengan en total más de 60 productos
locales_mas_60 = df[df['total'] > 60].index
print(list(locales_mas_60))
