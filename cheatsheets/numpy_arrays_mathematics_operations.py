import numpy as np

# Operaciones matematicas: se aplican a CADA elemento (vectorizado).
#   a - b, a + b, a / b, a * b  <->  subtract, add, divide, multiply
#   *  NO es producto matricial; para eso:  a @ b  o  a.dot(b)
#   exp / sqrt / sin / cos / log  -> una funcion, un resultado por celda


def show(name, arr):
    print(f"{name}: shape={arr.shape}  dtype={arr.dtype}")
    print(arr)
    print()


# Mismos datos que el cheatsheet: a y b tienen IGUAL shape, se operan celda a celda.
# a[0,0] - b[0,0] = 1.0 - 1.5 = -0.5, etc.
a = np.array([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]])
b = np.array([[1.5, 2.0, 3.0], [4.0, 5.0, 6.0]])
show("a", a)
show("b", b)

# Operador y funcion de NumPy son equivalentes. El resultado es un array NUEVO.
show("a - b  (np.subtract)", a - b)
show("b + a  (np.add)", b + a)
show("a / b  (np.divide)", a / b)
show("a * b  (np.multiply, elemento a elemento)", a * b)

# Otras aritmeticas utiles
show("a ** 2  (np.power, cada elemento al cuadrado)", a ** 2)
show("b % 2  (np.remainder, resto)", b % 2)
show("np.abs(a - b)  (valor absoluto)", np.abs(a - b))

# Broadcasting: un escalar se "estira" a todas las celdas
show("a + 10", a + 10)
show("b * 0.5", b * 0.5)

# Funciones unarias: mismo shape de salida. log/sqrt piden valores >= 0.
show("np.exp(b)  e**x", np.exp(b))
show("np.sqrt(b)", np.sqrt(b))
show("np.sin(a)", np.sin(a))
show("np.cos(b)", np.cos(b))
show("np.log(a)  (logaritmo natural, base e)", np.log(a))
show("np.log10(b)  (logaritmo base 10)", np.log10(b))

# Producto punto / matricial: NO es celda a celda.
# 1D: producto interno (escalar).  2D: filas de izq x columnas de der.
e = np.full((2, 2), 7.0)
f = np.eye(2)
show("e (constante 7)", e)
show("f (identidad 2x2)", f)
show("e.dot(f)  ==  e @ f", e.dot(f))

# Contraste * vs @
v = np.array([1.0, 2.0, 3.0])
w = np.array([0.0, 1.0, 0.0])
print(f"v * w  (elemento a elemento) = {v * w}")
print(f"v @ w  (producto interno)    = {v @ w}")  # 1*0 + 2*1 + 3*0 = 2
print()

m = np.array([[1.0, 2.0], [3.0, 4.0]])
n = np.array([[5.0, 6.0], [7.0, 8.0]])
show("m * n  (celda a celda)", m * n)
show("m @ n  (filas x columnas)", m @ n)
