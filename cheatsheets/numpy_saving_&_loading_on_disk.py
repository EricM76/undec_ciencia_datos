from pathlib import Path

import numpy as np

# Guardar / leer en disco (binario, conserva dtype y shape):
#   np.save / np.load              -> un array  (.npy)
#   np.savez / np.savez_compressed -> varios arrays (.npz)
#
# Texto y CSV: numpy_saving_&_loading_text_files.py
# Archivos reales: cheatsheets/io_ejemplos/


def show(name, arr):
    print(f"{name}: shape={arr.shape}  dtype={arr.dtype}")
    print(arr)
    print()


a = np.array([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]])
b = np.array([[1.5, 2.0, 3.0], [4.0, 5.0, 6.0]])
show("a", a)
show("b", b)

carpeta = Path(__file__).resolve().parent / "io_ejemplos"
carpeta.mkdir(exist_ok=True)
print(f"carpeta de archivos -> {carpeta}\n")

# --- un array: .npy ---
# Si no pones extension, NumPy agrega .npy
np.save(carpeta / "my_array", a)
npy = carpeta / "my_array.npy"
print(f"np.save -> {npy.name}  ({npy.stat().st_size} bytes)")
show("np.load('my_array.npy')", np.load(npy))
print(f"array_equal(a, leido)? {np.array_equal(a, np.load(npy))}\n")

# --- varios arrays: .npz (sin nombres -> arr_0, arr_1, ...) ---
np.savez(carpeta / "array.npz", a, b)
with np.load(carpeta / "array.npz") as npz:
    print(f"np.savez(a, b) claves: {npz.files}")
    show("npz['arr_0']  (era a)", npz["arr_0"])
    show("npz['arr_1']  (era b)", npz["arr_1"])

# Con nombres: se recuperan por clave, no por posicion
np.savez(carpeta / "nombrado.npz", medias=a, datos=b)
with np.load(carpeta / "nombrado.npz") as npz:
    print(f"np.savez(medias=a, datos=b) claves: {npz.files}")
    show("npz['datos']", npz["datos"])

# Comprimido: mismo uso, archivo mas chico si hay muchos ceros/repetidos
np.savez_compressed(carpeta / "array_zip.npz", medias=a, datos=b)
print(
    f"savez: {(carpeta / 'nombrado.npz').stat().st_size} bytes  |  "
    f"compressed: {(carpeta / 'array_zip.npz').stat().st_size} bytes"
)
print()

print("archivos binarios en io_ejemplos:")
for f in sorted(carpeta.iterdir()):
    if f.suffix in {".npy", ".npz"}:
        print(f"  {f.name:20} {f.stat().st_size:5} bytes")
