import matplotlib.pyplot as plt
import numpy as np
from ipFunctions import *
import plot4x4 as plt4

img = 'cartagena.jpg'

RGB = plt.imread(img)

r,g,b = imsplit(img)

gray = rbg2gray(img)
# gray[:,:,0] = gray

# Máscara roja

MaskY,colorMaskY = makeMask(0,50,0,90,55,255,'cartagena.jpg',True)

MaskRr = (r>=90) & (r<=255)
MaskRg = (g>=0) & (g<=50)
MaskRb = (b>=0) & (b<=50)

plt.figure(1)
plt.set_cmap('gray')
plt4.plot4x4(MaskRr,MaskRg,MaskRb)
MaskR = MaskRr & MaskRg & MaskRb
filas,columnas,capas = RGB.shape
colorMaskR=np.zeros((filas,columnas,capas),dtype=np.uint8) # El tipo del arreglo debe ser uint8
colorMaskR[:,:,0] = np.uint8(MaskR) * r
colorMaskR[:,:,1] = np.uint8(MaskR) * g
colorMaskR[:,:,2] = np.uint8(MaskR) * b

plt.subplot(2,2,4)
plt.imshow(colorMaskR)

# Máscara amarilla
MaskY,colorMaskY = makeMask(130,255,80,255,0,70,img,True)

# MaskYr = (r>=130) & (r<=255)
# MaskYg = (g>=80) & (g<=255)
# MaskYb = (b>=0) & (b<=70)

# plt.figure(2)
# plt4.plot4x4(MaskYr,MaskYg,MaskYb)
# MaskY = MaskYr & MaskYg & MaskYb
# colorMaskY=np.zeros((filas,columnas,capas),dtype=np.uint8) # El tipo del arreglo debe ser uint8
# colorMaskY[:,:,0] = np.uint8(MaskY) * r
# colorMaskY[:,:,1] = np.uint8(MaskY) * g
# colorMaskY[:,:,2] = np.uint8(MaskY) * b

# plt.subplot(2,2,4)
# plt.imshow(colorMaskY)

# Máscara azul
MaskB,colorMaskB = makeMask(0,50,0,90,55,255,'cartagena.jpg',True)

# Máscara del cielo
Maskc,colorMaskc = makeMask(90,180,144,220,195,255,'cartagena.jpg')

colorMask = colorMaskR + colorMaskY + colorMaskB + colorMaskc
Mask = MaskY + MaskR + MaskB + Maskc

I=np.zeros((filas,columnas,capas),dtype=np.uint8) # El tipo del arreglo debe ser uint8
I[:,:,0] = np.uint8(Mask)
I[:,:,1] = np.uint8(Mask)
I[:,:,2] = np.uint8(Mask)

gray3=np.zeros((filas,columnas,capas),dtype=np.uint8) # El tipo del arreglo debe ser uint8
gray3[:,:,0] = gray
gray3[:,:,1] = gray 
gray3[:,:,2] = gray 

plt.figure()
plt.subplot(1,2,1)
plt.imshow((~I+2) * gray3 + I*RGB)
plt.subplot(1,2,2)
plt.imshow(RGB)

plt.figure()
plt.imshow(I * gray3 + (~I+2)*RGB)

plt.show()
