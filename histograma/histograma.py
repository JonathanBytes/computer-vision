# Histograma de las tres capas de una imágen reconstruida
from ipFunctions import *
import matplotlib.pyplot as plt

name = input('\nNombre de la imágen a analizar: ')
img = name+'/'+name+'_reconstruida.jpeg'

r,g,b = imsplit(img)

plt.subplot(2,3,1)
plt.imshow(r)
plt.subplot(2,3,4)
plt.title('Capa roja')
imhist(r)
print('Capa R lista. ✅')

plt.subplot(2,3,2)
plt.imshow(g)
plt.subplot(2,3,5)
plt.title('Capa verde')
imhist(g)
print('Capa G lista. ✅')

plt.subplot(2,3,3)
plt.imshow(b)
plt.subplot(2,3,6)
plt.title('Capa azul')
imhist(b)
print('Capa B lista. ✅')

plt.show()
