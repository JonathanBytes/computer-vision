import matplotlib.pyplot as plt
import numpy as np

def imsplit(img):
    rgb = plt.imread(img)
    r=rgb[:,:,0]
    g=rgb[:,:,1]
    b=rgb[:,:,2]
    return r,g,b

def imhist(r):
    h = np.zeros(256)    
    filas,cols = r.shape

    for i in range(1,filas):
        for j in range(1,cols):
            h[r[i,j]] = h[r[i,j]]+1

    n = np.linspace(0,255,256)
    fig, ax = plt.subplots(1)
    plt.bar(n,h)
    ax.set_ylim(0, 0.3*max(h))
    ax.set_xlim(0,255)
    plt.xlabel('Intensidad')
    plt.ylabel('Cantidad')
    plt.title('Histograma')
    plt.show()

r,g,b = imsplit('cartagena.jpg')

h = imhist(r)
