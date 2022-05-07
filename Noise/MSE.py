import matplotlib.pyplot as plt
from ipFunctions import *

RGB = plt.imread('cartagena.jpg')
r,g,b = imsplit(RGB)
r = imundersize(r,4)

Ir_g = imnoise(r,'gaussian',0,0.1)

plt.figure()
# plt.set_cmap('twilight')
plt.set_cmap('gray')

plt.subplot(1,2,1)
plt.title('Imagen de referencia')
plt.imshow(r)

plt.subplot(1,2,2)
plt.title('Imagen con ruido')
plt.imshow(Ir_g)

MSE = immse(r,Ir_g)
print('\nThe mean square error is: %.2f'%MSE)

PSNR, SNR = psnr(r,Ir_g)
print('PSNR = %.2f, SNR = %.2f' %(PSNR,SNR))

plt.show()
