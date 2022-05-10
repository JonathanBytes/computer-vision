import matplotlib.pyplot as plt
from ipFunctions import *
import numpy as np

RGB = plt.imread('cartagena.jpg')
Gris = rgb2gray(RGB)

F, C = Gris.shape
Gris = imundersize(Gris,4)

Tam=21
Kaverage = fspecial('average',Tam)
Kgaussian = fspecial('gaussian',Tam)
Klog = fspecial('log',Tam)
Klaplacian = fspecial('laplacian',Tam)
Kprewitt = fspecial('prewitt',Tam)
Ksobel = fspecial('sobel',Tam)

Iaverage = imfilter(Gris,Kaverage)
Igaussian = imfilter(Gris,Kgaussian)
Ilog = imfilter(Gris,Klog)
Ilaplacian = imfilter(Gris,Klaplacian)
Iprewitt = imfilter(Gris,Kprewitt)
Isobel = imfilter(Gris,Ksobel)

plt.figure()
plt.set_cmap('gray')

plt.subplot(2,3,1)
plt.title('Imagen filtrada con Average')
plt.imshow(Iaverage)

plt.subplot(2,3,2)
plt.title('Imagen filtrada con Gaussian')
plt.imshow(Igaussian)

plt.subplot(2,3,3)
plt.title('Imagen filtrada con LOG')
plt.imshow(Ilog)

plt.subplot(2,3,4)
plt.title('Imagen filtrada con Laplacian')
plt.imshow(Ilaplacian)

plt.subplot(2,3,5)
plt.title('Imagen filtrada con Prewitt')
plt.imshow(Iprewitt)

plt.subplot(2,3,6)
plt.title('Imagen filtrada con Sobel')
plt.imshow(Isobel)

plt.show()
