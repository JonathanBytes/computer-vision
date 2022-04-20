from adaptthresh import *
from ipFunctions import *
import matplotlib.pyplot as plt


RGB = plt.imread('mangot6.jpg')
r,g,b = imsplit(RGB)

T = adaptthresh(r,[5,5],0)
