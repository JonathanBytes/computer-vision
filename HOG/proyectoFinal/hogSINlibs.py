import matplotlib.pyplot as plt
import numpy as np
from ipFunctions import *

# Toma una imagen del usuario cartagena=True -> la imagen será cartagena
img = getuserimg(cartagena=True)
img = rgb2gray(img)
step = 5
F, C = img.shape
# Reduce la resolución de la imagen
img = resize(img, (F/step, C/step))

# Calcula los gradientes de la imagen
gx, gy = calcularGradientes(img)

# Cálculo de las magnitudes para cada uno de los gradientes
mag = np.sqrt(gx**2 + gy**2)
# Normalizar las magnitudes
mag = mag / np.max(mag)

# Cálculo de los ángulos para cada uno de los gradientes
theta = np.rad2deg(np.arctan2(gy, gx)) % 180

# Graficar las direcciones y magnitudes de los gradientes
plotHOG(theta,mag)
plt.title('Dirección de los gradientes')

# Grafica gradientes, ángulos y magnitudes por separado
plt.figure()
plt.set_cmap('gray')
plt.subplot(2,2,1)
plt.title('Gradientes en x')
plt.imshow(gx)
plt.subplot(2,2,2)
plt.title('Gradientes en y')
plt.imshow(gy)
plt.subplot(2,2,3)
plt.title('Magnitudes')
plt.imshow(mag)
plt.subplot(2,2,4)
plt.title('Ángulos')
plt.imshow(theta)

plt.show()
