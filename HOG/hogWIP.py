import matplotlib.pyplot as plt
import numpy as np
from ipFunctions import *

img = getuserimg(cartagena=True)
img = imundersize(img,5)
img = rgb2gray(img)
F, C = img.shape
img = resize(img, (F, C))

gx, gy = calcularGradientes(img)

mag = np.sqrt(gx**2 + gy**2)
mag = mag / np.max(mag)

theta = np.rad2deg(np.arctan2(gy, gx)) % 180

plotHOG(theta,mag)

# plt.figure()
# plt.set_cmap('gray')
# plt.subplot(2,2,1)
# plt.imshow(gx)
# plt.subplot(2,2,2)
# plt.imshow(gy)
# plt.subplot(2,2,3)
# plt.imshow(mag)
# plt.subplot(2,2,4)
# plt.imshow(theta)

plt.show()
