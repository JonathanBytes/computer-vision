import matplotlib.pyplot as plt
from ipFunctions import *

RGB = plt.imread('elpepe.jpg')
r, g, b = imsplit(RGB)

r = imundersize(r,1)

# r = imfilter(r,fspecial('average',21))

# Klaplacian4=np.array([[0,1,0],[1,-4,0],[0,1,0]])
# Klaplacian8=np.array([[1,1,1],[1,-8,1],[1,1,1]])

# K = fspecial('laplacian',3,alpha=0)
# K2 = fspecial('laplacian',3,alpha=0.2)
# print(K,'\n',K2)
# Ifl = imfilter(r,Klaplacian4)
# print(Ifl)

K = fspecial('log',size=5,S=0.5)
# K = np.transpose(K)
print('Kernel:',K)
Ifl = imfilter(r,K)

plt.figure()
plt.set_cmap('gray')
plt.imshow(Ifl)

# imsave('recibo-filtrado',Ifl)

plt.show()
