import matplotlib as plt
import numpy as np
from ipFunctions import *

RGB = plt.imread('cartagena.jpg')
r,g,b = imsplit(RGB)

r = imundersize(r,4)

L = 5
# size = (L-1)//2

# a = np.arange(-size,size+1)
# b = np.arange(-size,size+1)

# X,Y = np.meshgrid(a,b)
# S=0.5
# G=(1/(2*np.pi*S**2))*np.exp(-(X**2+Y**2)/(2*S**2))
# normalG = G / np.sum(G)

K = fspecial('gaussian',21,3.5)
I = imfilter(r,K)

plt.figure()
plt.set_cmap('gray')
plt.imshow(I)

plt.show()
