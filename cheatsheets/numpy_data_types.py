import numpy as np

# dtype: TODOS los elementos del array son del mismo tipo.
#   int64      entero con signo, 64 bits
#   float32    coma flotante simple (4 bytes)  -- NO es doble precision
#   float64    coma flotante doble (8 bytes)   -- el "float" habitual
#   complex128 complejo: dos float64 (real + imaginario)
#   bool_      True / False
#   object_    cualquier objeto de Python (se pierde la vectorizacion)
#   bytes_     texto de largo FIJO en bytes   (antes np.string_)
#   str_       texto de largo FIJO en Unicode (antes np.unicode_)
#
# En NumPy 2 ya no existen: np.complex, np.object, np.string_, np.unicode_


def show(name, arr):
    print(f"{name}: dtype={arr.dtype}  itemsize={arr.itemsize} B/elem  nbytes={arr.nbytes}")
    print(arr)
    print()


# Sin dtype, NumPy INFIERE: enteros -> int64, con punto -> float64
show("inferido enteros", np.array([1, 2, 3]))
show("inferido floats", np.array([1.0, 2.5, 3.0]))

# Enteros con signo. int64 es el default en esta maquina.
show("np.int64", np.array([1, 2, 3], dtype=np.int64))
show("np.int32 (mitad de memoria)", np.array([1, 2, 3], dtype=np.int32))

# Cuidado: un entero chico DESBORDA (da la vuelta). En NumPy 2,
# np.array([256], dtype=uint8) tira error; el wrap aparece al convertir o sumar.
show("uint8 por astype: 256 -> 0, 257 -> 1", np.array([255, 256, 257]).astype(np.uint8))
u = np.array([255], dtype=np.uint8)
print(f"uint8(255) + 1 = {u + np.uint8(1)}")  # 0
print()

# float32 = simple precision. El cheatsheet lo llama "double"; eso es float64.
show("np.float32 (simple)", np.array([1, 2, 3], dtype=np.float32))
show("np.float64 (doble, default)", np.array([1, 2, 3], dtype=np.float64))

# Misma cuenta, distinta precision
x32 = np.array([0.1, 0.2, 0.3], dtype=np.float32)
x64 = np.array([0.1, 0.2, 0.3], dtype=np.float64)
print(f"suma float32 = {x32.sum()}")
print(f"suma float64 = {x64.sum()}")
print()

# Complejo: 1+2j. complex64 = 2*float32, complex128 = 2*float64
z = np.array([1 + 2j, 3 + 4j], dtype=np.complex128)
show("np.complex128", z)
print(f"  .real = {z.real}   .imag = {z.imag}")
print()

# Bool: 0 -> False, cualquier otro numero -> True
show("np.bool_ desde 0/1", np.array([0, 1, 2, -1], dtype=np.bool_))
show("np.bool_ desde comparacion", np.array([1.0, 2.0, 3.0]) < 2)

# object: cada celda es un objeto Python. Flexible, pero lento.
show("np.object_ (mezcla tipos)", np.array([1, "dos", [3, 4]], dtype=np.object_))

# Texto de largo FIJO. Si te pasas, TRUNCA.
show("bytes_  dtype='S4'  (antes string_)", np.array(["hola", "mundo"], dtype="S4"))
show("str_    dtype='U4'  (antes unicode_)", np.array(["hola", "mundo"], dtype="U4"))
show("U3 trunca 'numpy' -> 'num'", np.array(["numpy"], dtype="U3"))

# astype: copia a otro tipo. float -> int TRUNCA
f = np.array([1.9, 2.1, 3.0])
show("original float64", f)
show("astype int64 (trunca)", f.astype(np.int64))
show("astype float32", f.astype(np.float32))
show("astype bool", f.astype(np.bool_))
