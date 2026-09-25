## Ejercicio 2
# La función distribution_plotter grafica los datos que recibe como parámetro en una instancia de numpy array
#
# Graficar los precios de ventas en tres países. ¿Qué pueden decir respecto a sus distribuciones?
#
# Comparar las distribuciones con la de los precios de ventas sin distinguir por paises

import os

import matplotlib.pyplot as plt  # pyright: ignore[reportMissingImports]
import numpy as np  # pyright: ignore[reportMissingImports]
import seaborn as sns  # pyright: ignore[reportMissingImports]


def distribution_plotter(data, label, bin_width=500):
    sns.set(rc={"figure.figsize": (7, 5)})
    sns.set_style("white")
    dist = sns.histplot(
        data,
        stat="count",
        kde=False,
        line_kws={"linewidth": 5},
        binwidth=bin_width,
    )
    media = np.mean(data)
    mediana = np.median(data)
    dist.axvline(
        media,
        color="#d62728",
        linestyle="--",
        linewidth=2,
        label=f"Media ({media:,.2f})",
    )
    dist.axvline(
        mediana,
        color="#2ca02c",
        linestyle="-",
        linewidth=2,
        label=f"Mediana ({mediana:,.2f})",
    )
    dist.legend()
    dist.set_title("Distribucion " + label + "\n", fontsize=16)


# Ruta al CSV relativa a este script (misma lectura que el ejercicio 1: array de strings).
data_location = os.path.join(
    os.path.dirname(__file__), "..", "DataSet", "sales_data_sample_excercise.csv"
)
data = np.genfromtxt(data_location, skip_header=1, delimiter="\t", dtype=str)

# Columnas: 0 ORDERNUMBER, 1 SALES, 2 MONTH_ID, 3 YEAR_ID, 4 PRODUCTLINE, 5 COUNTRY
sales_vector = data[:, 1].astype(float)
country_vector = data[:, 5]

paises_unicos = np.unique(country_vector)
print(paises_unicos)

# Tres países con más observaciones, para que el histograma sea comparable.
paises = ["USA", "Spain", "France"]

for pais in paises:
    ventas_pais = sales_vector[country_vector == pais]
    plt.figure()
    distribution_plotter(ventas_pais, pais)
    print(
        f"{pais}: n={ventas_pais.size}, "
        f"media={np.mean(ventas_pais):.2f}, mediana={np.median(ventas_pais):.2f}"
    )

plt.figure()
distribution_plotter(sales_vector, "todos los paises")
print(
    f"Todos: n={sales_vector.size}, "
    f"media={np.mean(sales_vector):.2f}, mediana={np.median(sales_vector):.2f}"
)

# Las tres distribuciones y la global están sesgadas a la derecha (media > mediana):
# la mayoría de las ventas se concentra en valores bajos-medios y hay una cola de ventas altas.
# USA, España y Francia se parecen entre sí y a la distribución conjunta.
plt.show()
