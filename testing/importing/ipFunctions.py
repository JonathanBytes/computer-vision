import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def imhist(r):
    h = np.zeros(256)    
    filas,cols = r.shape
    for i in range(1,filas):
        for j in range(1,cols):
            h[r[i,j]] = h[r[i,j]]+1
    n = np.linspace(0,255,256)
    # fig, ax = plt.subplots(1)
    # ax.set_ylim(0, 0.3*max(h))
    # ax.set_xlim(0,255)
    # plt.xlabel('Intensidad')
    # plt.title('Histograma')
    # plt.ylabel('Cantidad')
    plt.bar(n,h)
    plt.set_cmap('gray')
    norm=mpl.colors.Normalize(vmin=0,vmax=255)
    escala=plt.cm.ScalarMappable(cmap='gray',norm=norm)
    escala.set_array([])
    plt.colorbar(escala,orientation="horizontal",ticks=[0,50,100,150,200,255])
    plt.xlim(0, 255)
    plt.ylim(0, max(h)*0.3)
    plt.xlabel('Intensidad')
    plt.ylabel('Cantidad')

def imsplit(img):
    rgb = plt.imread(img)
    r=rgb[:,:,0]
    g=rgb[:,:,1]
    b=rgb[:,:,2]
    return r,g,b