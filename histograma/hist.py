from imsplit import imsplit

import sys
sys.path
sys.path.append('~/Documents/Universidad/2022-1/computer-vision/histograma/')
print(sys.path)

from imhist import imhist 

r,g,b = imsplit('cartagena.jpg')

h = imhist(r)
