import numpy as np

# --- 1. Sumar dos colecciones ---

# Con listas de Python hay que iterar (list comprehension)
a_lista = [1, 2, 3, 4]
b_lista = [10, 20, 30, 40]
c_lista = [a_lista[i] + b_lista[i] for i in range(len(a_lista))]
print(c_lista)  # [11, 22, 33, 44]

# Con NumPy, una sola línea aplica la suma a todos los pares de elementos
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
c = a + b
print(c)  # [11 22 33 44]

# --- 2. Aplicar la misma operación a todos los valores ---

# Calcular un 10 % de descuento sobre una lista de precios
precios = np.array([100, 250, 80, 320])
precios_con_descuento = precios * 0.9  # multiplica cada precio, sin bucle
print(precios_con_descuento)  # [ 90. 225.  72. 288.]

# --- 3. Evaluar una condición sobre todo el array ---

# Filtrar temperaturas por encima de 20 °C
temperaturas = np.array([-2, 15, 32, 5, 28, 21])
calor = temperaturas[temperaturas > 20]  # máscara + filtrado en una expresión
print(calor)  # [32 28 21]

# --- 4. Aplicar una función matemática a cada elemento ---

valores = np.array([4, 9, 16, 25])
raices = np.sqrt(valores)  # raíz cuadrada de cada elemento
print(raices)  # [2. 3. 4. 5.]
