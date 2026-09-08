from pathlib import Path

import numpy as np

# Guardar / leer texto (humano, se pierde el dtype nativo):
#   np.savetxt(ruta, arr, delimiter=" ")  -> escribe .txt / .csv
#   np.loadtxt(ruta)                      -> lee numeros (no banca huecos)
#   np.genfromtxt(ruta, delimiter=",")    -> lee CSV; huecos -> nan
#
# Archivos reales: cheatsheets/io_ejemplos/
# Binario .npy/.npz: nympy_saving_&_loading_on_disk.py


def show(name, arr):
    print(f"{name}: shape={arr.shape}  dtype={arr.dtype}")
    print(arr)
    print()


a = np.array([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]])
show("a (lo que vamos a guardar)", a)

carpeta = Path(__file__).resolve().parent / "io_ejemplos"
myarray_txt = carpeta / "myarray.txt"
myfile_txt = carpeta / "myfile.txt"
my_file_csv = carpeta / "my_file.csv"
print(f"carpeta de archivos -> {carpeta}\n")

# --- escribir: espacios entre columnas ---
# fmt evita la notacion cientifica por defecto (%.18e)
np.savetxt(myarray_txt, a, delimiter=" ", fmt="%.1f")
print(">>> np.savetxt('myarray.txt', a, delimiter=' ')")
print(myarray_txt.read_text(encoding="utf-8"))

# --- leer txt: delimiter por defecto = cualquier espacio ---
print(">>> np.loadtxt('myfile.txt')")
print(myfile_txt.read_text(encoding="utf-8"))
show("loadtxt myfile.txt", np.loadtxt(myfile_txt))

# --- leer CSV: hay que decir delimiter=',' ---
print(">>> np.genfromtxt('my_file.csv', delimiter=',')")
print(my_file_csv.read_text(encoding="utf-8"))
show("genfromtxt my_file.csv", np.genfromtxt(my_file_csv, delimiter=","))

# loadtxt no acepta celdas vacias; genfromtxt las convierte en nan
print(">>> np.loadtxt('my_file.csv', delimiter=',')")
try:
    np.loadtxt(my_file_csv, delimiter=",")
except ValueError as err:
    print(f"falla (hueco en la fila 2): {err}\n")

print("archivos de texto en io_ejemplos:")
for f in sorted(carpeta.iterdir()):
    if f.suffix in {".txt", ".csv"}:
        print(f"  {f.name:20} {f.stat().st_size:5} bytes")
