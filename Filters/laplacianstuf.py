import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from ipFunctions import *

RGB = plt.imread('chess.jpg')
r, g, b = imsplit(RGB)

r = imundersize(r,4)

Klaplacian=np.array([[0,1,0],[1,-4,0],[0,1,0]])
K = fspecial('laplacian',3,alpha=0)
K2 = fspecial('laplacian',3,alpha=0.2)
print(K,'\n',K2)


K = fspecial('gaussian',21)
print(K)
Ifl = imfilter(r,K2)

plt.figure()
plt.set_cmap('gray')
plt.imshow(Ifl)

plt.show()
