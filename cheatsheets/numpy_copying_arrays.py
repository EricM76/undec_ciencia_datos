import numpy as np

# Copiar vs ver:
#   b = a          -> alias: el MISMO objeto
#   a.view()       -> vista: otro objeto, MISMA memoria (cambiar uno cambia el otro)
#   a.copy()       -> copia: memoria propia (independiente)
#   np.copy(a)     -> igual que a.copy()
# Una slice a[0] o a[:, 1] tambien es una VISTA.
# Comprobar: np.shares_memory(x, a)  y  x.base


def estado(nombre, arr, origen):
    if arr.base is None:
        dueño = "None (es dueno de su memoria)"
    elif arr.base is origen:
        dueño = "origen"
    else:
        dueño = "otro array (copia interna)"
    print(f"{nombre}: {arr}")
    print(
        f"  is origen? {arr is origen}   "
        f"shares_memory? {np.shares_memory(arr, origen)}   "
        f"base={dueño}"
    )
    print()


a = np.array([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]])
print("a original:", a)
print()

# --- alias: no hay array nuevo ---
alias = a
alias[0, 0] = 99
print("alias = a  y  alias[0, 0] = 99")
estado("alias", alias, a)
print("a tambien cambio:", a)
print()

a = np.array([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]])

# --- vista: mismo dato, otro ndarray ---
h = a.view()
estado("h = a.view()  (antes de mutar)", h, a)
h[0, 0] = 99
print("h[0, 0] = 99")
print("a (cambio porque comparte memoria):", a)
print("h:", h)
print()

a = np.array([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]])

# --- slice = vista (el caso mas comun en la practica) ---
fila = a[0]
estado("fila = a[0]", fila, a)
fila[:] = 7
print("fila[:] = 7  -> a queda afectado:")
print(a)
print()

a = np.array([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]])

# --- copia: memoria nueva ---
c1 = np.copy(a)
c2 = a.copy()
estado("np.copy(a)", c1, a)
estado("a.copy()", c2, a)
c2[0, 0] = 99
print("c2[0, 0] = 99")
print("a intacto:", a)
print("c2:", c2)
print()

# Transpuesta y reshape suelen ser VISTAS (mismo dato, otro shape)
t = a.T
r = a.reshape(6)
estado("a.T", t, a)
estado("a.reshape(6)", r, a)

# Indexado con lista/mascara: COPIA (no comparte memoria)
cols = a[:, [0, 2]]
mask = a[a >= 2]
estado("a[:, [0, 2]]  (fancy indexing)", cols, a)
estado("a[a >= 2]  (mascara bool)", mask, a)

# np.asarray no copia si ya es ndarray; np.array por defecto tampoco en NumPy 2
# si queres forzar copia: np.array(a, copy=True)  o  a.copy()
print(f"np.asarray(a) is a  -> {np.asarray(a) is a}")
print(f"np.array(a, copy=True) shares_memory -> {np.shares_memory(np.array(a, copy=True), a)}")
