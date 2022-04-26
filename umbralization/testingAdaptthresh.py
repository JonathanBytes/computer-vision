from ipFunctions import *
import matplotlib.pyplot as plt


method = input('Método: ')
RGB = plt.imread('dibujo.jpg')
r,g,b = imsplit(RGB)

r = imundersize(r,3)
r=np.fliplr(np.transpose(r))

T = adaptthresh(r,[9,9],method=method)

bw = r >= T 

plt.figure()
plt.set_cmap('gray')
plt.subplot(1,2,1)
plt.imshow(r)
plt.subplot(1,2,2)
plt.imshow(bw)

plt.show()
