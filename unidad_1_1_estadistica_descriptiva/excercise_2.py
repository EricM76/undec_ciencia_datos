## Ejercicio 2
# Calcular la media y mediana de la columna SALES. ¿Qué podemos decir sobre la simetría en la
# distribución de estos valores?

import os

import numpy as np

# Ruta al CSV relativa a este script (misma lectura que el ejercicio 1: array de strings).
data_location = os.path.join(
    os.path.dirname(__file__), "..", "DataSet", "sales_data_sample_excercise.csv"
)

data = np.genfromtxt(data_location, skip_header=1, delimiter="\t", dtype=str)

# Columna SALES (indice 1): convertir a float para poder calcular estadisticos
sales = data[:, 1].astype(float)

media = np.mean(sales)
mediana = np.median(sales)

print(f"Media de SALES: {media:.2f}")
print(f"Mediana de SALES: {mediana:.2f}")

# Simetria: comparar media y mediana
# - media ≈ mediana  -> distribucion simetrica
# - media > mediana  -> asimetria a la derecha (cola hacia valores altos / outliers altos)
# - media < mediana  -> asimetria a la izquierda (cola hacia valores bajos)
if media > mediana:
    print(
        "Conclusion: media > mediana -> la distribucion de SALES es asimetria a la derecha "
        "(valores altos / outliers empujan la media hacia arriba)."
    )
elif media < mediana:
    print(
        "Conclusion: media < mediana -> la distribucion de SALES es asimetria a la izquierda."
    )
else:
    print("Conclusion: media ≈ mediana -> la distribucion de SALES es aproximadamente simetrica.")
