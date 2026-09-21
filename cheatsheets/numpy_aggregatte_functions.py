import numpy as np

# Agregar = resumir varios valores en menos valores.
#   sin axis     -> un escalar (todo el array)
#   axis=0       -> colapsa FILAS    -> queda 1 valor por COLUMNA
#   axis=1       -> colapsa COLUMNAS -> queda 1 valor por FILA
# median y corrcoef NO son metodos del array: van como np.median / np.corrcoef


def show(name, arr):
    print(f"{name}: shape={arr.shape}  dtype={arr.dtype}")
    print(arr)
    print()


a = np.array([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]])
b = np.array([[1.5, 2.0, 3.0], [4.0, 5.0, 6.0]])
show("a", a)
show("b", b)

# Sin axis: recorre TODAS las celdas
print(f"a.sum()   = {a.sum()}")    # 1+2+3+1+2+3 = 12
print(f"a.min()   = {a.min()}")    # 1
print(f"a.max()   = {a.max()}")    # 3
print(f"a.mean()  = {a.mean()}")   # 12 / 6 = 2
print(f"a.prod()  = {a.prod()}")   # 1*2*3*1*2*3 = 36
print()

# axis: el numero es el eje que DESAPARECE
#   b.shape = (2, 3)  ->  eje 0 = 2 filas,  eje 1 = 3 columnas
#
#        col0  col1  col2
# fila0  1.5    2     3     ->  max de la fila = 3
# fila1   4     5     6     ->  max de la fila = 6
#         |     |     |
#        max=4 max=5 max=6
show("b.max(axis=0)  max de cada COLUMNA", b.max(axis=0))  # shape=(3,)
show("b.max(axis=1)  max de cada FILA", b.max(axis=1))     # shape=(2,)
show("b.min(axis=0)", b.min(axis=0))
show("b.sum(axis=1)  total por fila", b.sum(axis=1))

# keepdims=True: no saca el eje, lo deja en tamano 1 (util para broadcasting)
show("b.mean(axis=0, keepdims=True)", b.mean(axis=0, keepdims=True))  # (1, 3)

# cumsum: no resume a un valor, acumula a lo largo de un eje (mismo shape)
show("b.cumsum(axis=1)  acumulado a lo largo de la fila", b.cumsum(axis=1))
# fila0: 1.5, 1.5+2=3.5, 3.5+3=6.5
show("b.cumsum(axis=0)  acumulado hacia abajo", b.cumsum(axis=0))

# median y corrcoef: SOLO funciones de modulo (no existe a.median())
print(f"np.median(b)     = {np.median(b)}")  # centro de 1.5,2,3,4,5,6 = 3.5
print(f"np.median(b, axis=0) = {np.median(b, axis=0)}")
print()
show("np.corrcoef(a)  correlacion entre FILAS", np.corrcoef(a))
# las dos filas de a son iguales -> correlacion 1

print(f"np.std(b)   = {np.std(b)}")    # tambien b.std()
print(f"np.var(b)   = {np.var(b)}")    # varianza = std**2
print(f"np.ptp(b)   = {np.ptp(b)}")    # pico a pico: max - min  (6 - 1.5)
print()

# Donde esta el extremo (indice plano o por eje)
print(f"b.argmin()  = {b.argmin()}  (posicion plana del minimo: 1.5)")
print(f"b.argmax()  = {b.argmax()}  (posicion plana del maximo: 6)")
show("b.argmax(axis=1)  columna del maximo en cada fila", b.argmax(axis=1))

# Percentiles / cuantiles
print(f"np.percentile(b, 50)  = {np.percentile(b, 50)}")  # = mediana
print(f"np.percentile(b, [0, 50, 100]) = {np.percentile(b, [0, 50, 100])}")
print()

# Si hay nan, sum/mean se vuelven nan. Las versiones nan* lo ignoran.
c = np.array([1.0, 2.0, np.nan, 4.0])
print(f"c.mean()      = {c.mean()}")
print(f"np.nanmean(c) = {np.nanmean(c)}")  # (1+2+4)/3
print(f"np.nansum(c)  = {np.nansum(c)}")
