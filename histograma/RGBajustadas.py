from ipFunctions import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

name = input('\nNombre de la imágen a procesar: ')
print()
img = name+'/'+name+'_reconstruida.jpeg'

r,g,b = imsplit(img)

# rs = imadjust(r)
# gs = imadjust(g)
# bs = imadjust(b)

# plt.subplot(2,3,1)
# plt.imshow(rs)
# plt.subplot(2,3,4)
# plt.title('Capa roja')
# imhist(rs)
# print('\nCapa R lista. ✅')

# plt.subplot(2,3,2)
# plt.imshow(gs)
# plt.subplot(2,3,5)
# plt.title('Capa verde')
# imhist(gs)
# print('Capa G lista. ✅')

# plt.subplot(2,3,3)
# plt.imshow(bs)
# plt.subplot(2,3,6)
# plt.title('Capa azul')
# imhist(bs)
# print('Capa B lista. ✅')

plt.show()

# imgname = name + '_R_ajustada'
# mpimg.imsave(imgname,rs)
# imgname = name + '_G_ajustada.jpeg'
# mpimg.imsave(imgname,gs)
# imgname = name + '_B_ajustada.jpeg'
# mpimg.imsave(imgname,bs)

print('Imágenes guardadas con éxito ✨🚀')
