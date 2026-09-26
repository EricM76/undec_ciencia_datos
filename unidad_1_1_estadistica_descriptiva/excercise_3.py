## Ejercicio 3
# Graficar los valores de la columna SALES para USA y Japan por separado para el año 2004.
# ¿Qué podemos decir sobre la distribución de ventas en esos dos países durante ese año?

import os

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def distribution_plotter(data, label):
    """Dibuja un histograma de la serie 'data' con el titulo 'label'."""
    # Tamano de la figura y fondo blanco (estilo limpio)
    sns.set(rc={"figure.figsize": (7, 5)})
    sns.set_style("white")
    # Cada llamada abre una figura nueva para no pisar el grafico anterior
    plt.figure()
    # histplot: cuenta cuantas ventas caen en cada intervalo (bin)
    # binwidth=500 -> cada barra agrupa 500 unidades de SALES
    # kde=False -> no dibuja la curva de densidad suave encima
    dist = sns.histplot(
        data,
        stat="count",
        kde=False,
        line_kws={"linewidth": 5},
        binwidth=500,
    )
    # Etiquetas del grafico para interpretar ejes y titulo
    dist.set_title("Distribucion " + label + "\n", fontsize=16)
    dist.set_xlabel("Valor de ventas")
    dist.set_ylabel("Cantidad")


# Armamos la ruta al CSV relativa a este script (carpeta DataSet un nivel arriba)
data_location = os.path.join(
    os.path.dirname(__file__), "..", "DataSet", "sales_data_sample_excercise.csv"
)

# Leemos todo como texto (dtype=str) porque el CSV mezcla numeros y cadenas
# skip_header=1 saltea la fila de nombres de columnas; delimiter="\t" indica tabulacion
data = np.genfromtxt(data_location, skip_header=1, delimiter="\t", dtype=str)

# Extraemos las columnas que necesitamos por indice (ndarray[:, col])
# Columna 1 = SALES -> la convertimos a float para poder calcular media/mediana y graficar
sales = data[:, 1].astype(float)
# Columna 3 = YEAR_ID (queda como string, ej. "2004")
year = data[:, 3]
# Columna 5 = COUNTRY (queda como string, ej. "USA", "Japan")
country = data[:, 5]

# Mascara booleana: True solo en las filas del anio 2004
mask_2004 = year == "2004"

# Filtramos SALES combinando pais + anio con & (AND elemento a elemento)
# Resultado: un array con solo las ventas de ese pais en 2004
sales_usa_2004 = sales[(country == "USA") & mask_2004]
sales_japan_2004 = sales[(country == "Japan") & mask_2004]

# Contexto numerico: cuantas observaciones hay (USA suele tener muchas mas que Japan)
print(f"Cantidad de ventas USA 2004: {len(sales_usa_2004)}")
print(f"Cantidad de ventas Japan 2004: {len(sales_japan_2004)}")

# Media vs mediana: si media > mediana -> asimetria a la derecha (cola hacia ventas altas)
print(f"USA 2004 -> media={np.mean(sales_usa_2004):.2f}, mediana={np.median(sales_usa_2004):.2f}")
print(
    f"Japan 2004 -> media={np.mean(sales_japan_2004):.2f}, mediana={np.median(sales_japan_2004):.2f}"
)

# Un histograma por pais para comparar formas de la distribucion a ojo
distribution_plotter(sales_usa_2004, "SALES USA 2004")
distribution_plotter(sales_japan_2004, "SALES Japan 2004")
# Muestra todas las figuras abiertas a la vez (bloquea hasta cerrar las ventanas)
plt.show()

# Conclusion:
# - USA tiene muchas mas observaciones que Japan en 2004.
# - En ambos paises la distribucion esta sesgada a la derecha (cola hacia ventas altas):
#   la media supera a la mediana porque hay ventas puntuales elevadas.
# - USA concentra mas ventas en rangos medios/bajos, con algunos valores altos.
# - Japan muestra menos datos y una dispersion relativa mas visible (menos concentracion).
