import numpy as np

# Inspeccionar un ndarray (no cambia los datos, solo los describe):
#   shape       -> tamano de cada eje, p.ej. (2, 5) = 2 filas x 5 columnas
#   len(arr)    -> tamano del PRIMER eje (no la cantidad total de elementos)
#   ndim        -> cantidad de ejes: len(shape)
#   size        -> cantidad TOTAL de elementos: producto de shape
#   dtype       -> tipo de TODOS los elementos
#   dtype.name  -> nombre del tipo, como string
#   astype(...) -> copia el array a otro tipo


def inspect(name, arr):
    print(f"{name}:")
    print(arr)
    print(
        f"  shape={arr.shape}  len={len(arr)}  ndim={arr.ndim}  "
        f"size={arr.size}  dtype={arr.dtype}  dtype.name={arr.dtype.name}"
    )
    print()


# Vector: shape=(5,)  ->  len=5, ndim=1, size=5
a = np.array([1, 2, 3, 4, 5])
inspect("vector a", a)

# Matriz: shape=(2, 5)  ->  len=2 (filas), ndim=2, size=10 (2*5)
b = np.array([[1.5, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
inspect("matriz b", b)

# 3D: shape=(2, 2, 3)  ->  len=2 (bloques), ndim=3, size=12 (2*2*3)
e = np.array(
    [
        [[1, 2, 3], [4, 5, 6]],
        [[7, 8, 9], [10, 11, 12]],
    ]
)
inspect("cubo e", e)

print("--- relacion entre atributos ---")
print(f"ndim == len(shape):     {b.ndim} == {len(b.shape)}")
print(f"size == producto shape: {b.size} == {2 * 5}")
print(f"len(b) == shape[0]:     {len(b)} == {b.shape[0]}")
print()

print("--- dtype vs dtype.name ---")
print(f"b.dtype      -> {b.dtype!r}   (objeto dtype de NumPy)")
print(f"b.dtype.name -> {b.dtype.name!r}        (string)")
print()

# astype: DEVUELVE un array nuevo. El original no cambia.
# float -> int TRUNCA (no redondea): 1.5 -> 1
print("--- astype: copia a otro tipo ---")
print(f"b original:     {b}")
print(f"b.astype(int):  {b.astype(int)}")
print(f"b sigue igual:  {b}")
print()

# Otros destinos utiles
print(f"a.astype(float): {a.astype(float)}")  # 1 -> 1.0
print(f"a.astype(bool):  {a.astype(bool)}")  # 0=False, resto=True
print(f"a.astype(str):   {a.astype(str)}")  # cada numero como texto
