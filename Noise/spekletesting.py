import matplotlib.pyplot as plt
from ipFunctions import *

I = plt.imread('cartagena.jpg')
r,g,b = imsplit(I)
r = imundersize(r,4)

spekle = imnoise(r,'spekle',0,0.1)

plt.figure()
plt.set_cmap('gray')
plt.imshow(spekle)

plt.show()
