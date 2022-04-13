import matplotlib.pyplot as plt
from ipFunctions import *
import numpy as np

RGB = plt.imread('cartagena.jpg')
Gris = rgb2gray(RGB)

Tam=21
K = np.ones([Tam,Tam])*(1/Tam**2)
n, m = K.shape
n = int(n)
m = int(m)

iniF=(n+1)//2;
iniC=(m+1)//2;
finF=iniF-1;
finC=iniC-1;
Ipad=np.pad(Gris,(finF,finC),'edge')
F,C = Ipad.shape
T=np.zeros([F,C])
for i in range(iniF,F-finF):
    for j in range(iniC,C-finC):
        V = Ipad[i-finF:i+finF,j-finC:j+finC]
        T[i,j] = np.sum(V*K)

T=np.uint8(T);
T=T[iniF:F-finF,iniC:C-finC]