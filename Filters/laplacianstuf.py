import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from ipFunctions import *

RGB = plt.imread('cartagena.jpg')
r, g, b = imsplit(RGB)

r = imundersize(r,4)

r = imfilter(r,fspecial('average',21))

Klaplacian4=np.array([[0,1,0],[1,-4,0],[0,1,0]])
Klaplacian8=np.array([[1,1,1],[1,-8,1],[1,1,1]])

# K = fspecial('laplacian',3,alpha=0)
# K2 = fspecial('laplacian',3,alpha=0.2)
# print(K,'\n',K2)

K = fspecial('average',21,3)
print('Kernel:',K)
Ifl = imfilter(r,Klaplacian4)
print(Ifl)

plt.figure()
plt.set_cmap('gray')
plt.imshow(Ifl)

plt.show()
