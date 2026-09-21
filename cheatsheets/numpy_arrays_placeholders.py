import numpy as np

# Arrays "placeholder": no partimos de una lista, NumPy rellena el array.
#   zeros / ones / full / empty -> forma fija, valor de relleno
#   arange / linspace           -> secuencia numerica
#   eye                         -> matriz identidad
#   random                      -> valores aleatorios


def show(name, arr):
    print(f"{name}: shape={arr.shape}  ndim={arr.ndim}  dtype={arr.dtype}")
    print(arr)
    print()


# zeros: todos 0. dtype por defecto = float64
# shape=(3, 4)  ndim=2  -> 3 filas x 4 columnas
show("zeros 2D", np.zeros((3, 4)))

# Un entero como shape -> vector 1D. shape=(5,)  ndim=1
show("zeros 1D", np.zeros(5))

# ones: todos 1. dtype explicito: int16 en vez de float64
# shape=(2, 3, 4)  ndim=3  -> 2 bloques, cada uno 3x4
show("ones 3D (int16)", np.ones((2, 3, 4), dtype=np.int16))


# arange(start, stop, step): como range() de Python.
# stop NO se incluye. Aqui: 10, 15, 20  (25 queda afuera)
# shape=(3,)  ndim=1  dtype=int64
d = np.arange(10, 25, 5)
show("arange paso 5", d)

# Sin step: de 0 a stop-1. Util para indices.
show("arange hasta 5", np.arange(5))  # [0, 1, 2, 3, 4]

# Con floats el paso puede acumular error; para N puntos fijos usa linspace.
show("arange float (ojo con el stop)", np.arange(0.0, 1.0, 0.3))


# linspace(start, stop, num): N muestras, stop SI se incluye (endpoint=True).
# 9 puntos igualmente espaciados entre 0 y 2: 0.00, 0.25, ..., 2.00
# shape=(9,)  dtype=float64
show("linspace 9 puntos [0, 2]", np.linspace(0, 2, 9))

# endpoint=False: stop queda afuera (mas parecido a arange).
show("linspace sin incluir el stop", np.linspace(0, 2, 5, endpoint=False))


# full(shape, valor): todos los elementos iguales a "valor"
# shape=(2, 2)  dtype inferido del 7 -> int64
e = np.full((2, 2), 7)
show("full constante 7", e)

# El dtype sigue al valor: 7.0 -> float64
show("full constante 7.0", np.full((2, 2), 7.0))


# eye(n): matriz identidad n x n (1 en la diagonal, 0 en el resto)
# shape=(2, 2)  dtype=float64
f = np.eye(2)
show("eye 2x2", f)

# k desplaza la diagonal: k=1 es la diagonal de arriba
show("eye 3x3 diagonal k=1", np.eye(3, k=1))


# random.random(shape): floats uniformes en [0.0, 1.0)
# Cada ejecucion da valores distintos
show("random 2x2", np.random.random((2, 2)))


# empty: reserva memoria SIN inicializar. Mas rapido, pero el contenido
# es basura (lo que hubiera en esa memoria). No lo uses si necesitas 0.
show("empty 3x2 (valores indefinidos)", np.empty((3, 2)))
