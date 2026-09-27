# Ejercicio Series
# Dadas dos series que representan cantidades
#
# cantidades_prod1 = pd.Series([3, 7, 1], index=['local_a', 'local_b', 'local_c'])
#
# cantidades_prod2 = pd.Series([54, 70, 985], index=['local_a', 'local_b', 'local_c'])
#
import pandas as pd

cantidades_prod1 = pd.Series([3, 7, 1], index=['local_a', 'local_b', 'local_c'])
cantidades_prod2 = pd.Series([54, 70, 985], index=['local_a', 'local_b', 'local_c'])

# ¿Qué cantidad de prod2 hay en local_b?
cantidad_local_b = cantidades_prod2.loc['local_b']
print("Cantidad de prod2 en local_b:", cantidad_local_b)

# Usando iloc obtener la suma de prod1 en local_a y local_c
suma_a_c = cantidades_prod1.iloc[[0, 2]].sum()
print("Suma de prod1 en local_a y local_c:", suma_a_c)

# Usando index responder ¿qué local corresponde al índice 1 de cantidades_prod1?
local_indice_1 = cantidades_prod1.index[1]
print("Local en el índice 1 de cantidades_prod1:", local_indice_1)
