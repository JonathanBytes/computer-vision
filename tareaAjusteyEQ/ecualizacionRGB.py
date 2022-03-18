from ipFunctions import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

name = input('\nNombre de la imágen a procesar (frame, cubes): ')
print()
img = name+'/'+name+'_reconstruida.jpeg'

r,g,b = imsplit(img)

# Graficar las 3 capas de la imágen antes de la ecualización 
plt.figure(1)
plt.subplot(2,3,1)
plt.title('Capa roja')
plt.imshow(r)
plt.subplot(2,3,4)
imhist(r)
print('\nCapa R lista. ✅')

plt.subplot(2,3,2)
plt.title('Capa verde')
plt.imshow(g)
plt.subplot(2,3,5)
imhist(g)
print('Capa G lista. ✅')

plt.subplot(2,3,3)
plt.title('Capa azul')
plt.imshow(b)
plt.subplot(2,3,6)
imhist(b)
print('Capa B lista. ✅\n')

# Ecualizar las 3 capas
rq = histeq(r)
gq = histeq(g)
bq = histeq(b)

# Graficar las 3 capas de la imágen después de la ecualización 
plt.figure(2)
plt.subplot(2,3,1)
plt.title('Capa roja')
plt.imshow(rq)
plt.subplot(2,3,4)
imhist(rq)
print('\nCapa R ajustada lista. ✅')

plt.subplot(2,3,2)
plt.title('Capa verde')
plt.imshow(gq)
plt.subplot(2,3,5)
imhist(gq)
print('Capa G ajustada lista. ✅')

plt.subplot(2,3,3)
plt.title('Capa azul')
plt.imshow(bq)
plt.subplot(2,3,6)
imhist(bq)
print('Capa B ajustada lista. ✅')

plt.show()

print('¡Hasta pronto!')
