from ipFunctions import *
import matplotlib.pyplot as plt

r,g,b = imsplit('cartagena.jpg')

plt.subplot(2,3,1)
plt.imshow(r)
plt.subplot(2,3,4)
imhist(r)

plt.subplot(2,3,2)
plt.imshow(g)
plt.subplot(2,3,5)
h = imhist(g)

plt.subplot(2,3,3)
plt.imshow(b)
plt.subplot(2,3,6)
h = imhist(b)

plt.show()

