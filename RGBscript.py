import matplotlib.pyplot as plt
import numpy as np


R=np.copy('cubes_R.jpg');
G=np.copy('cubes_G.jpg');
B=np.copy('cubes_B.jpg');
C=np.copy('cubes_color.jpg')

r=R[:,:,0];
g=G[:,:,1];
b=B[:,:,2];

# [filas columnas capas]=size(C);

filas,columnas,capas=C.shape

filas = C.shape[0]
columnas = C.shape[1]
capas = C.shape[2]

I=np.zeros((filas, columnas, capas),dtype=np.uint8)

I[:,:,0]=r
I(:,:,1]=g
I[:,:,2]=b
