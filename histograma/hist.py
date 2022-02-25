import matplotlib.pyplot as plt
import numpy as np
from imsplit import imsplit
from imhist import imhist

rgb = plt.imread('cartagena.jpg')

r,g,b = imsplit(rgb)

h = imhist(r)
