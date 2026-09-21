import contextlib
import io

import numpy as np

# Pedir ayuda en NumPy (no calcula nada: solo documentacion):
#   np.info(obj)   -> docstring de NumPy (funcion, atributo o metodo)
#   help(obj)      -> ayuda estandar de Python
#   dir(np)        -> lista nombres del modulo; se puede filtrar por texto
# En IPython/Jupyter tambien:  np.linspace?   /   np.ndarray.reshape?
# np.lookfor() existia en NumPy 1.x; en 2.x ya no esta.


def info_corto(obj, lineas=8):
    """Igual que np.info, pero solo las primeras lineas."""
    etiqueta = getattr(obj, "__qualname__", None) or getattr(obj, "__name__", obj)
    print(f">>> np.info({etiqueta})")
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        np.info(obj)
    texto = [ln.rstrip() for ln in buf.getvalue().splitlines() if ln.strip()]
    for ln in texto[:lineas]:
        print(ln)
    if len(texto) > lineas:
        print(f"  ... ({len(texto) - lineas} lineas mas; usa np.info para ver todo)")
    print()


def brief(obj):
    """Primera frase util de la docstring (salta firmas tipo a.reshape(...))."""
    descripcion = "(sin docstring)"
    for ln in (obj.__doc__ or "").splitlines():
        s = ln.strip()
        if not s or s.startswith(("a.", ">>>", "..", "Parameters", "Returns")):
            continue
        if "(" in s and s.endswith(")") and not s[0].isupper():
            continue
        descripcion = s
        break
    nombre = getattr(obj, "__qualname__", getattr(obj, "__name__", str(obj)))
    print(f"  {nombre:28} {descripcion}")


# --- np.info sobre un atributo, un metodo y una funcion ---
info_corto(np.ndarray.dtype)
info_corto(np.ndarray.reshape)
info_corto(np.linspace)

# --- buscar por nombre (reemplazo practico de np.lookfor, removido en NumPy 2) ---
print(">>> [n for n in dir(np) if 'lin' in n.lower()]")
hits = [n for n in dir(np) if "lin" in n.lower()]
print(hits)
print()

# --- propiedades mas relevantes de ndarray ---
print("propiedades (consultar con np.info(np.ndarray.NOMBRE)):")
for nombre in (
    "shape",
    "ndim",
    "size",
    "dtype",
    "T",
    "nbytes",
    "itemsize",
    "strides",
    "flags",
    "flat",
    "real",
    "imag",
    "base",
):
    brief(getattr(np.ndarray, nombre))
print()

# --- metodos mas relevantes de ndarray ---
print("metodos (consultar con np.info(np.ndarray.NOMBRE)):")
for nombre in (
    "reshape",
    "ravel",
    "flatten",
    "squeeze",
    "transpose",
    "copy",
    "view",
    "astype",
    "fill",
    "sum",
    "mean",
    "min",
    "max",
    "std",
    "var",
    "argmin",
    "argmax",
    "clip",
    "round",
    "sort",
    "argsort",
    "nonzero",
):
    brief(getattr(np.ndarray, nombre))
print()

# Mini demo: esas propiedades sobre un array concreto
a = np.array([[1.5, 2.0, 3.0], [4.0, 5.0, 6.0]])
print("sobre a =")
print(a)
print(f"  shape={a.shape}  ndim={a.ndim}  size={a.size}  dtype={a.dtype}")
print(f"  itemsize={a.itemsize} bytes/elem  nbytes={a.nbytes} bytes totales")
print(f"  T (transpuesta)=\n{a.T}")
print(f"  base={a.base}  (None = es dueno de su memoria, no es una vista)")
