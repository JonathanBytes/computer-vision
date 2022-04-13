import matplotlib.pyplot as plt
from ipFunctions import *
import numpy as np

RGB = plt.imread('cartagena.jpg')
Gris = rgb2gray(RGB)

F,C = Gris.shape
paso = 4
gray = Gris[0:F:paso,0:C:paso]

plt.figure()
plt.set_cmap('gray')
plt.subplot(1,2,1)
plt.imshow(Gris)
plt.subplot(1,2,2)
plt.imshow(gray)

plt.show()