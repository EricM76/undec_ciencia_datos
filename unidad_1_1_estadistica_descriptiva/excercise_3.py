## Ejercicio 3
# Graficar los valores de la columna SALES para USA y Japan por separado para el año 2004.
# ¿Qué podemos decir sobre la distribución de ventas en esos dos países durante ese año?

import os

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def distribution_plotter(data, label):
    sns.set(rc={"figure.figsize": (7, 5)})
    sns.set_style("white")
    plt.figure()  # figura nueva para no pisar el grafico anterior
    dist = sns.histplot(
        data,
        stat="count",
        kde=False,
        line_kws={"linewidth": 5},
        binwidth=500,
    )
    dist.set_title("Distribucion " + label + "\n", fontsize=16)
    dist.set_xlabel("Valor de ventas")
    dist.set_ylabel("Cantidad")


# Ruta al CSV relativa a este script
data_location = os.path.join(
    os.path.dirname(__file__), "..", "DataSet", "sales_data_sample_excercise.csv"
)

data = np.genfromtxt(data_location, skip_header=1, delimiter="\t", dtype=str)

# Columnas: 1=SALES, 3=YEAR_ID, 5=COUNTRY
sales = data[:, 1].astype(float)
year = data[:, 3]
country = data[:, 5]

mask_2004 = year == "2004"
sales_usa_2004 = sales[(country == "USA") & mask_2004]
sales_japan_2004 = sales[(country == "Japan") & mask_2004]

print(f"Cantidad de ventas USA 2004: {len(sales_usa_2004)}")
print(f"Cantidad de ventas Japan 2004: {len(sales_japan_2004)}")
print(f"USA 2004 -> media={np.mean(sales_usa_2004):.2f}, mediana={np.median(sales_usa_2004):.2f}")
print(
    f"Japan 2004 -> media={np.mean(sales_japan_2004):.2f}, mediana={np.median(sales_japan_2004):.2f}"
)

distribution_plotter(sales_usa_2004, "SALES USA 2004")
distribution_plotter(sales_japan_2004, "SALES Japan 2004")
plt.show()  # muestra todas las figuras abiertas a la vez

# Conclusion:
# - USA tiene muchas mas observaciones que Japan en 2004.
# - En ambos paises la distribucion esta sesgada a la derecha (cola hacia ventas altas):
#   la media supera a la mediana porque hay ventas puntuales elevadas.
# - USA concentra mas ventas en rangos medios/bajos, con algunos valores altos.
# - Japan muestra menos datos y una dispersion relativa mas visible (menos concentracion).
