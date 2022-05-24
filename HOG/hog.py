import matplotlib.pyplot as plt
from ipFunctions import *
from skimage import io
from skimage import color
from skimage.transform import resize
import math
from skimage.feature import hog
import numpy as np

img = resize(plt.imread("B.jpg"), (128, 64))

plt.imshow(img)

# plt.figure(figsize=(15, 8))
# plt.set_cmap('gray')
# plt.imshow(img, cmap='gray')
# plt.axis("off")
plt.show()
