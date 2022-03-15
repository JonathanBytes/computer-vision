from ipFunctions import *
import matplotlib.pyplot as plt

name = input('\nNombre de la imágen a analizar: ')
img = name+'/'+name+'_reconstruida.jpeg'

r,g,b = imsplit(img)

E = (6,108)
S = (0,255)
n = 1 
I = r
Is = imadjust(I)

# E = (6,108)
# rs = imadjust(r,E,S,n)

# E = (6,108)
# gs = imadjust(g,E,S,n)

# bs = imadjust(b,E,S,n)
# print('Ajuste completado')

plt.subplot(2,2,3)
imhist(I)
print('Histograma de la imagen original listo. ✅')
plt.subplot(2,2,1)
plt.imshow(I)

plt.subplot(2,2,4)
imhist(Is)
print('Histograma de la imagen ajustada listo. ✅')
plt.subplot(2,2,2)
plt.imshow(Is)

plt.show()
