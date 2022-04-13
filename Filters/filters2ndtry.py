import matplotlib.pyplot as plt
from ipFunctions import *
import numpy as np

RGB = plt.imread('cartagena.jpg')
Gris = rgb2gray(RGB)

F,C = Gris.shape
Gris = imundersize(Gris,4)

Tam=5
K = np.ones([Tam,Tam])*(1/Tam**2)

tipoRuido = 'salpimienta'
GrayNoisy = imnoise(Gris,'salpimienta',0,0.2)
print('Noisy image complete ✅')

#T = imfilter(GrayNoisy,K)
T = medfilt2(GrayNoisy,[5,5])
#T = modefilt(Gris,[5,5])
#T = ordfilt2(GrayNoisy,1,np.ones([3,3]))
print('Filtering image complete ✅')

plt.figure()
plt.set_cmap('gray')
plt.subplot(1,2,1)
plt.title('Imagen con ruido %s'%(tipoRuido))
plt.imshow(GrayNoisy)
plt.subplot(1,2,2)
plt.title('Imagen filtrada')
plt.imshow(T)

plt.show()