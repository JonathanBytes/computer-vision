import matplotlib.pyplot as plt
import numpy as np
from ipFunctions import *

img = 'barranquero.jpeg'

RGB = plt.imread(img)
r,g,b = imsplit(img)
gray = rbg2gray(img)
filas,columnas,capas = RGB.shape

# Máscara ojo rojo
MaskR,colorMaskR = makeMask(66,145,20,55,40,85,img)

# Máscara azul
MaskB,colorMaskB = makeMask(5,135,110,255,70,255,img,True)

colorMask = colorMaskB + colorMaskR
Mask = MaskB + MaskR
Mask = np.uint8(Mask)

I=np.zeros((filas,columnas,capas),dtype=np.uint8) # El tipo del arreglo debe ser uint8
I = np.dstack((Mask,Mask,Mask))

gray3=np.zeros((filas,columnas,capas),dtype=np.uint8) # El tipo del arreglo debe ser uint8
gray3 = np.dstack((gray,gray,gray))

plt.figure()
plt.subplot(1,2,1)
plt.imshow((~I+2) * gray3 + I*RGB)
plt.subplot(1,2,2)
plt.imshow(RGB)

# plt.figure()
# plt.imshow(I * gray3 + (~I+2)*RGB)

plt.figure()
plt.imshow(RGB)

plt.show()
