import matplotlib.pyplot as plt
import numpy as np
from ipFunctions import *

img = 'cartagena.jpg'

RGB = plt.imread(img)
r,g,b = imsplit(img)
gray = rbg2gray(img)
filas,columnas,capas = RGB.shape

# Máscara roja
MaskR,colorMaskR = makeMask(30,255,0,50,0,50,img,True)

# Máscara amarilla
MaskY,colorMaskY = makeMask(130,255,80,255,0,70,img)

# Máscara azul
MaskB,colorMaskB = makeMask(0,50,0,90,55,255,'cartagena.jpg')

# Máscara del cielo
Maskc,colorMaskc = makeMask(90,180,144,220,195,255,'cartagena.jpg')

colorMask = colorMaskR + colorMaskY + colorMaskB
Mask = MaskY + MaskR + MaskB 
Mask = np.uint8(Mask)

I=np.zeros((filas,columnas,capas),dtype=np.uint8) # El tipo del arreglo debe ser uint8
# I[:,:,0] = np.uint8(Mask)
# I[:,:,1] = np.uint8(Mask)
# I[:,:,2] = np.uint8(Mask)
I = np.dstack((Mask,Mask,Mask))

gray3=np.zeros((filas,columnas,capas),dtype=np.uint8) # El tipo del arreglo debe ser uint8
gray3 = np.dstack((gray,gray,gray))

plt.figure()
plt.subplot(1,2,1)
plt.imshow((~I+2) * gray3 + I*RGB)
plt.subplot(1,2,2)
plt.imshow(RGB)

plt.figure()
plt.imshow(I * gray3 + (~I+2)*RGB)

# plt.figure()
# plt.imshow(I)

plt.show()
