import matplotlib.pyplot as plt
from ipFunctions import *

I = plt.imread('cartagena.jpg')
r,g,b = imsplit(I)
r = imundersize(r,4)
r2 = r

spekle = imnoise(imundersize(I[:,:,0],4),'spekle',0,0.1)
gauss = imnoise(r,'gaussian',0,0.1)

plt.figure()
plt.set_cmap('gray')
plt.subplot(2,2,1)
plt.title('Ruido gaussiano')
plt.imshow(gauss)
plt.subplot(2,2,3)
plt.title('Ruido Spekle')
plt.imshow(spekle)
plt.subplot(2,2,4)
plt.title('Imagen de referencia')
plt.imshow(r)
plt.subplot(2,2,2)
plt.title('Ruido Sal y pimienta')
saltpepper = imnoise(r,'salpimienta',0,0.1)
plt.imshow(saltpepper)

plt.show()
