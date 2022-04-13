import matplotlib.pyplot as plt
import numpy as np
from ipFunctions import *

RGB = plt.imread('cartagena.jpg')

r,g,b = imsplit(RGB)

h,s,v = rgbToHSV(r,g,b)