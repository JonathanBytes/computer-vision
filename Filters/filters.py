import matplotlib.pyplot as plt
from ipFunctions import *
import numpy as np

RGB = plt.imread('cartagena.jpg')
r,g,b = imsplit(RGB)

""" paso = 4 """
filas, cols = r.shape
plt.figure()
plt.imshow(r)
""" print('filas %f cols %f'%(filas,cols))
for i in range(filas-1):
    for j in range(cols-1):
        r = r[i,j]
 """
""" r = r[1:paso:filas-1,1:paso:cols-1] """
""" print(r.shape)
plt.figure()
plt.imshow(r) """

Tam=21
K = np.ones([Tam,Tam])*(1/Tam**2)
n, m = K.shape
n = int(n)
m = int(m)

padn = (n-1)//2
padm = (m-1)//2

padr = np.pad(r,(padn,padm),'symmetric')
plt.figure()
plt.imshow(padr)

T = np.zeros([filas, cols])

iniF = (n+1)//2
iniC = (m+1)//2
FinF = iniF - 1
FinC = iniC - 1

for i in range(iniF,filas-FinF):
    for j in range(iniC,cols-FinC):
        W = padr[i-FinF:i+FinF,j-FinC:j+FinC]
        T[i,j]=np.sum(W*K)

T=T[iniF:filas-FinF,iniC:cols-FinC]
T = np.uint8(T)
plt.figure()
plt.set_cmap('gray')
plt.imshow(T)

plt.show()