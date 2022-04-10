import matplotlib.pyplot as plt
from ipFunctions import *
import numpy as np

RGB = plt.imread('cartagena.jpg')
r,g,b = imsplit(RGB)

Ir_g = imnoise(r,'gaussian',0,0.05)

plt.figure()
plt.set_cmap('twilight')
# plt.set_cmap('gray')
plt.subplot(1,2,1)
plt.imshow(r)
plt.subplot(1,2,2)
plt.imshow(Ir_g)

# filas, cols = r.shape

# SE=(np.double(r)-np.double(Ir_g))**2
# MSE = np.sum(SE)/(filas*cols)
# print('El ruido medio cuadrático es: ',MSE)
# print('The Mean square error is: ',MSE)

MSE = immse(r,Ir_g)
print('The mean square error is:',MSE)


# PSNR = 10*np.log10(255**2/MSE)
# meanNoise = np.mean(np.double(Ir_g)**2)
# SNR = 10*np.log10(meanNoise/MSE)

PSNR, SNR = psnr(r,Ir_g)
print('PSNR = %.2f, SNR = %.2f' %(PSNR,SNR))

plt.show()
