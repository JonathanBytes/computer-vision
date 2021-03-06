import matplotlib.pyplot as plt
import numpy as np
from ipFunctions import *

img = getuserimg(cartagena=True)
img = imundersize(img,6)
img = rgb2gray(img)
F, C = img.shape
img = resize(img, (F, C))

gx, gy = calcularGradientes(img)

gy_check, gx_check = np.gradient(img) 

print('diff_gx:', np.linalg.norm(gx - gx_check))

print('diff_gy', np.linalg.norm(gy - gy_check))

mag = np.sqrt(gx**2 + gy**2)
print('mag max %f'%(np.max(mag)))
mag = mag / np.max(mag)
theta = np.rad2deg(np.arctan2(gy, gx)) % 180
print('min theta = %f'%(np.min(theta)))
