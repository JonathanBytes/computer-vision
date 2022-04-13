import matplotlib.pyplot as plt
from ipFunctions import *
import numpy as np

RGB = plt.imread('cartagena.jpg')
Gris = rgb2gray(RGB)

F,C = Gris.shape
Gris = undersize(Gris,4)

Tam=21
K = np.ones([Tam,Tam])*(1/Tam**2)

T = imfilter(Gris,K)

plt.figure()
plt.set_cmap('gray')
plt.imshow(T)

plt.show()