import numpy as np

# CV = (desvio / media) * 100
# Permite comparar dispersion entre variables con medias o unidades distintas
# No tiene unidades (es adimensional)

# EJEMPLO 1: dos grupos con distinta media
usa = np.array([3200, 3500, 3100, 3600, 3400])
japan = np.array([2800, 4500, 2200, 5100, 3900])

cv_usa = (np.std(usa) / np.mean(usa)) * 100
cv_japan = (np.std(japan) / np.mean(japan)) * 100

print(f"USA: media={np.mean(usa):.1f}, std={np.std(usa):.1f}, CV={cv_usa:.1f}%")
print(f"JAPAN: media={np.mean(japan):.1f}, std={np.std(japan):.1f}, CV={cv_japan:.1f}%")
print("-> Japan tiene mayor dispersion relativa (CV mas alto)")

# EJEMPLO 2: distintas unidades (no se pueden comparar solo con el desvio)
alturas_cm = np.array([160, 165, 170, 175, 180])  # centimetros
pesos_kg = np.array([55, 62, 70, 80, 90])  # kilogramos

cv_altura = (np.std(alturas_cm) / np.mean(alturas_cm)) * 100
cv_peso = (np.std(pesos_kg) / np.mean(pesos_kg)) * 100

print(f"ALTURA: std={np.std(alturas_cm):.2f} cm, CV={cv_altura:.1f}%")
print(f"PESO: std={np.std(pesos_kg):.2f} kg, CV={cv_peso:.1f}%")
print("-> El CV permite comparar dispersion pese a unidades distintas")

# CUIDADO: si la media es cercana a 0, el CV se vuelve inestable
casi_cero = np.array([-1, 0, 1, 0, 1])
print(f"MEDIA CERCA DE 0: media={np.mean(casi_cero)}, CV poco interpretable")
