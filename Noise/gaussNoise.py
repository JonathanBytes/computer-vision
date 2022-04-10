import matplotlib.pyplot as plt
from ipFunctions import *
import numpy as np

I = plt.imread('cartagena.jpg')
filas, cols, capas = I.shape 
r,g,b = imsplit(I)

# noise = np.random.normal(loc=0,scale=20,size=[filas,cols])

# Ir = np.uint8(r + noise)

Ir = imnoise(r,'gaussian',0,0.01)
plt.figure()
plt.set_cmap('gray')
plt.subplot(1,2,1)
plt.imshow(Ir)
plt.subplot(1,2,2)
noise = np.random.normal(0,20,(filas,cols))
plt.imshow(np.uint8(noise))


# plt.figure()
# plt.set_cmap('gray')
# plt.subplot(2,2,1)
# plt.imshow(r)

# plt.subplot(2,2,2)
# Ir = imnoise(r,'salpimienta',0,0.5)
# plt.imshow(Ir)

# plt.subplot(2,2,3)
# I2r = imnoise(r,'gaussian',0,0.5)
# plt.imshow(I2r)

plt.show()

