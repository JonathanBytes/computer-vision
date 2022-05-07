from ipFunctions import *
import matplotlib.pyplot as plt

# RGB = plt.imread('n09.jpg');
RGB = plt.imread('papel.jpg');

r, g, b = imsplit(RGB);
r=np.fliplr(np.transpose(r))
r = imundersize(r,2)

bw2 = imbinarize(r,method='otsu')
bw = imbinarize(r,method='bradley')

plt.figure()
plt.set_cmap('gray')
plt.imshow(r)

plt.figure()
plt.set_cmap('gray')
plt.subplot(1,2,1)
plt.imshow(bw2)
plt.title('Binarización con OTSU')
plt.subplot(1,2,2)
plt.imshow(bw)
plt.title('Binarización con Bradley')

plt.show()
