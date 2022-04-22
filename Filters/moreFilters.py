import matplotlib.pyplot as plt
from ipFunctions import *
import numpy as np

RGB = plt.imread('cartagena.jpg')
Gris = rgb2gray(RGB)

F,C = Gris.shape
Gris = imundersize(Gris,4)

K = np.ones([5,5])
# Istd = stdfilt(Gris,K)
Ient = entropyfilt(Gris,K)

print('Image filtering complete ✅')

plt.figure()
plt.set_cmap('gray')
plt.imshow(Ient)

plt.show()
