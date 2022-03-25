import matplotlib.pyplot as plt
from ipFunctions import *
from time import sleep

RGB = plt.imread('mango6.jpg')

r,g,b = imsplit('mango6.jpg')

bina_r=r>=140
bina_g=g>=145
bina_b=b>=125

plt.figure()
plt.subplot(3,3,1)
plt.imshow(r)
plt.subplot(3,3,4)
imhist(r)
plt.subplot(3,3,7)
plt.imshow(bina_r)

plt.subplot(3,3,2)
plt.imshow(g)
plt.subplot(3,3,5)
imhist(g)
plt.subplot(3,3,8)
plt.imshow(bina_g)

plt.subplot(3,3,3)
plt.imshow(b)
plt.subplot(3,3,6)
imhist(b)
plt.subplot(3,3,9)
plt.imshow(bina_b)

plt.show()

for T in range(125):
    bb=b>=T;
    plt.figure(2)
    plt.imshow(bb)
    plt.draw()
    plt.pause(0.01)
    plt.clf()

plt.show()
