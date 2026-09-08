import numpy as np

# Extraer datos de un array:
#   a[i] / b[i, j]     -> un elemento (subsetting)
#   a[i:j] / b[i:j, k] -> rebanada; el stop NO entra; suele ser VISTA
#   a[a < 2]           -> mascara bool; es COPIA
#   b[[1, 0], [0, 1]]  -> fancy (listas de indices); es COPIA
# Indices empiezan en 0.  b[1, 2] es mejor que b[1][2].


def show(name, arr):
    print(f"{name}: shape={arr.shape}  dtype={arr.dtype}")
    print(arr)
    print()


# a 1D (como el cheatsheet: a[2] -> 3).  b y c los de siempre.
a = np.array([1.0, 2.0, 3.0])
b = np.array([[1.5, 2.0, 3.0], [4.0, 5.0, 6.0]])
c = np.array(
    [
        [[1.5, 2.0, 3.0], [4.0, 5.0, 6.0]],
        [[3.0, 2.0, 1.0], [4.0, 5.0, 6.0]],
    ]
)
show("a  vector", a)
show("b  matriz", b)
show("c  3D", c)

print("--- subsetting (un elemento) ---")
print(f"a[2]     = {a[2]}")          # tercer elemento (indice 2)
print(f"b[1, 2]  = {b[1, 2]}")      # fila 1, columna 2 -> 6.0
print(f"b[1][2]  = {b[1][2]}   (equivale, pero hace dos indexados)")
print(f"a[-1]    = {a[-1]}    (ultimo)")
print()

print("--- slicing (rebanadas: start:stop, stop afuera) ---")
show("a[0:2]     indices 0 y 1", a[0:2])
show("b[0:2, 1]  filas 0-1, columna 1", b[0:2, 1])
show("b[:1]      fila 0, SIGUE siendo 2D", b[:1])
show("b[0]       fila 0, baja a 1D", b[0])
show("b[:, 1]    toda la columna 1", b[:, 1])
show("a[::-1]    al reves", a[::-1])

# ... = "el resto de los ejes"
show("c[1, ...]  igual a c[1, :, :]", c[1, ...])
show("c[..., 0]  primer elemento de cada vector interno", c[..., 0])

print(f"a[0:2] es VISTA de a? {np.shares_memory(a[0:2], a)}")
print()

print("--- boolean indexing (mascara; COPIA) ---")
show("a < 2", a < 2)
show("a[a < 2]", a[a < 2])
show("b[b >= 4]", b[b >= 4])  # queda 1D: solo los que cumplen
print(f"a[a < 2] es VISTA? {np.shares_memory(a[a < 2], a)}")
print()

print("--- fancy indexing (listas de indices; COPIA) ---")
# Pares (fila, col): (1,0)=4, (0,1)=2, (1,2)=6, (0,0)=1.5
show("b[[1, 0, 1, 0], [0, 1, 2, 0]]", b[[1, 0, 1, 0], [0, 1, 2, 0]])

# Primero filas [1,0,1,0], despues esas columnas [0,1,2,0]
filas = b[[1, 0, 1, 0]]
show("b[[1, 0, 1, 0]]  (reordena filas)", filas)
show("...[:, [0, 1, 2, 0]]  (reordena columnas)", filas[:, [0, 1, 2, 0]])
print(f"fancy es VISTA? {np.shares_memory(b[[1, 0], [0, 1]], b)}")
print()

# Asignar: slice modifica el original; mascara/fancy no (trabajan sobre copia
# al leer, pero al ESCRIBIR a[a<2]=0 si actualiza a)
a2 = a.copy()
a2[a2 < 2] = 0
show("a2[a2 < 2] = 0", a2)
b2 = b.copy()
b2[0, :] = 9
show("b2[0, :] = 9  (slice: cambia la fila)", b2)
