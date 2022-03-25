import matplotlib.pyplot as plt 
from ipFunctions import *

I = plt.imread('cartagena.jpg')

gray = rgb2gray('cartagena.jpg')

plt.figure(1)

plt.subplot(1,2,1)
plt.imshow(I)
plt.title('Color')

plt.subplot(1,2,2)
plt.imshow(gray)
plt.title('Escala de grises')

plt.set_cmap('gray')

plt.show()
