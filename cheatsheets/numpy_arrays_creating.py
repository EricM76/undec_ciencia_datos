import numpy as np

# Atributos de un ndarray:
#   shape  -> tamaño en cada eje, p.ej. (2, 5) = 2 filas x 5 columnas
#   ndim   -> cantidad de ejes (len(shape)): 1=vector, 2=matriz, 3=cubo
#   dtype  -> tipo de TODOS los elementos (int64, float64, bool, ...)


def show(name, arr):
    print(f"{name}: shape={arr.shape}  ndim={arr.ndim}  dtype={arr.dtype}")
    print(arr)
    print()


# Lista 1D -> vector. shape=(5,)  ndim=1  dtype=int64 (inferido)
a = np.array([1, 2, 3, 4, 5])
show("lista 1D", a)

# Tupla 1D: np.array acepta cualquier secuencia; el resultado es el mismo
a_tupla = np.array((1, 2, 3, 4, 5))
show("tupla 1D", a_tupla)

# Lista de listas -> matriz. El anidamiento define las dimensiones.
# shape=(2, 5)  ndim=2  dtype=int64
b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
show("lista de listas", b)

# Lista de tuplas: tambien 2D. dtype=float convierte 1 -> 1.
# shape=(2, 5)  ndim=2  dtype=float64
b_tuplas = np.array([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], dtype=float)
show("lista de tuplas (dtype=float)", b_tuplas)

# Tres niveles de anidamiento -> array 3D.
# shape=(2, 2, 3): 2 bloques, cada uno 2x3
c = np.array(
    [
        [[1, 2, 3], [4, 5, 6]],
        [[7, 8, 9], [10, 11, 12]],
    ]
)
show("listas anidadas 3D", c)

# Mezcla lista/tupla: lo que importa es el anidamiento, no el tipo de secuencia.
# shape=(2, 2, 5)  ndim=3  dtype=float64
c_mixto = np.array(
    [
        [(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)],
        [(11, 12, 13, 14, 15), (16, 17, 18, 19, 20)],
    ],
    dtype=float,
)
show("lista de listas de tuplas 3D", c_mixto)

# dtype explicito: no se infiere, lo fijamos nosotros
show("enteros explicitos", np.array([1, 2, 3], dtype=np.int32))  # int32
show("booleanos desde 0/1", np.array([0, 1, 1, 0], dtype=bool))  # 0=False, 1=True
show("texto", np.array(["uno", "dos", "tres"]))  # <U4: Unicode de hasta 4 chars

# ndmin: no cambia los datos, solo agrega ejes de tamaño 1
show("lista 1D con ndmin=2 (fila)", np.array([1, 2, 3], ndmin=2))  # shape=(1, 3)
show("lista 1D con ndmin=3", np.array([1, 2, 3], ndmin=3))  # shape=(1, 1, 3)
