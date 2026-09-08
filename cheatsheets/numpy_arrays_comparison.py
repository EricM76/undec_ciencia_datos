import numpy as np

# Comparaciones: el resultado es un array de bool del mismo shape
#   a == b, a < 2, ...     -> celda a celda
#   np.array_equal(a, b)   -> un solo True/False (mismos shape y valores)
#   np.allclose(a, b)      -> igualdad "practica" para floats
# Combinar mascaras:  &  |  ~  (no uses and / or con arrays)


def show(name, arr):
    print(f"{name}: shape={getattr(arr, 'shape', ())}  dtype={getattr(arr, 'dtype', type(arr).__name__)}")
    print(arr)
    print()


# Mismos a, b que en mathematics_operations:
# a == b es True solo donde coinciden: (0,1)=2 y (0,2)=3
a = np.array([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]])
b = np.array([[1.5, 2.0, 3.0], [4.0, 5.0, 6.0]])
show("a", a)
show("b", b)

show("a == b  (np.equal)", a == b)
show("a != b  (np.not_equal)", a != b)
show("a < b   (np.less)", a < b)
show("a <= b  (np.less_equal)", a <= b)
show("a > b   (np.greater)", a > b)
show("a >= 2  (np.greater_equal; el 2 se estira)", a >= 2)

# El cheatsheet usa un vector para a < 2 -> [True, False, False]
v = np.array([1.0, 2.0, 3.0])
show("v < 2", v < 2)

# Array-wise: un unico booleano. False si cambia shape O algun valor.
print(f"np.array_equal(a, b)     = {np.array_equal(a, b)}")
print(f"np.array_equal(a, a)     = {np.array_equal(a, a)}")
print(f"np.array_equal(v, a[0])  = {np.array_equal(v, a[0])}")  # misma fila
print()

# Floats: == exige bits iguales. allclose admite un margen.
x = np.array([0.1 + 0.2])
y = np.array([0.3])
print(f"0.1+0.2 == 0.3           = {x == y}   (a veces False por redondeo)")
print(f"np.allclose(0.1+0.2, 0.3) = {np.allclose(x, y)}")
print()

# Combinar condiciones. Los parentesis son obligatorios: (a > 1) & (a < 3)
mask = (a >= 2) & (a <= 3)
show("(a >= 2) & (a <= 3)", mask)
show("(a < 2) | (b > 5)", (a < 2) | (b > 5))
show("~(a == b)  (negacion, igual a a != b)", ~(a == b))

# Resumir una mascara a un solo bool
print(f"np.any(a == b)  (alguna celda igual?) = {np.any(a == b)}")
print(f"np.all(a < b)   (todas a < b?)        = {np.all(a < b)}")
print()

# Usar la mascara para filtrar o para np.where
show("a[a >= 2]  (solo los que cumplen; queda 1D)", a[a >= 2])
show("np.where(a == b, a, 0)  (iguales se quedan, resto 0)", np.where(a == b, a, 0))

# Valores especiales
z = np.array([1.0, np.nan, np.inf, -np.inf])
show("np.isnan(z)", np.isnan(z))
show("np.isinf(z)", np.isinf(z))
show("np.isfinite(z)  (ni nan ni inf)", np.isfinite(z))
