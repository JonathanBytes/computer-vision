import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import statistics as stat
import matplotlib.image as mpimg
import tkinter as tk
from tkinter import filedialog
from skimage.transform import resize
import os

def plotHOG(theta,mag,scale=4,step=8,detalles=False):
    """
    Esta función recibe como entrada dos matrices (theta y mag). 
    theta : matriz que da el ángulo de cada uno de los grandientes de la imagen
    mag : matriz que da la magnitud de cada uno de los grandientes de la imagen

    Además recibe dos parámetros extra, scale y step, que son opcionales.
    scale : Que tan largas serán las flechas vectoriales que se graficarán
    step : Cantidad de flechas graficadas, más flechas a medida que este parámetro baja
    """

    F,C = theta.shape
    fig, ax = plt.subplots(figsize = (12, 7))
    for i in range(0,F,step):
        for j in range(0,C,step):
            scale = 4
            # Se consiguen las coordenas cartecianas a partir de la magnitud y el ángulo, pero su magnitud mantiene siendo 1
            x = scale*np.cos(np.radians(theta[i,j]))
            y = scale*np.sin(np.radians(theta[i,j]))
            # Gráfico de una flecha cuyo color depende de la magnitud, si la magnitud es máxima el color es blanco, por el contrario, si es mínima, el color será negro
            ax.arrow(j, abs(i-F), x, y, color=(mag[i,j],mag[i,j],mag[i,j]),width=step/16,head_width=step/4,head_length=step/8)
        # Reporte de estado de la gráfica
        if i%10==0:
            if detalles: print('mag = %f , theta = %f, i = %i , j = %i'%(mag[i,j],theta[i,j],i,j))
            os.system("clear")
            porcentaje = i/F * 100 
            print('Graficando vectores: %i %% del procesamiento'%porcentaje)

    os.system("clear")
    print('Terminado')

    # Fondo negro, título, acotar los ejes coordenas y mantenerlos en la misma escala
    ax.set_title('HOG features')
    ax.set_facecolor('black')
    ax.axis([0, C, 0, F])
    ax.set_aspect('equal')

def calcularGradientes(img):
    """
    Esta función calcula los gradientes horizontales y verticales de una imagen dada como entrada
    """ 

    F,C = img.shape
    gx = np.zeros((F,C))
    gy = np.zeros((F,C))

    # Diferencia central 
    # Se usa la diferencia central para casi toda la imágen, menos la primera y últimas filas y columnas
    gx[:, 1:-1] = (img[:, 2:] - img[:, :-2]) / 2
    gy[1:-1, :] = (img[2:, :] - img[:-2, :]) / 2

    # Diferencia hacia delante
    # Se usa la diferencia hacia delante para el cálculo de la primer fila y columna
    gx[:, 0] = img[:, 1] - img[:, 0]
    gy[0, :] = img[1, :] - img[0, :]

    # Diferencia hacia atrás
    # Se usa la diferencia hacia atrás para el cálculo de la última fila y columna
    gx[:, -1] = img[:, -1] - img[:, -2]
    gy[-1, :] = img[-1, :] - img[-2, :]

    return gx, gy

def getuserimg(cartagena=False):
    if cartagena == True:
        return plt.imread('cartagena.jpg')
    else:
        path = getuserpath()
        return plt.imread(path)

def getuserpath():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()

def imsave(name,I):
    mpimg.imsave(name+'.jpeg',I)

def imsplit(rgb):
    r=rgb[:,:,0]
    g=rgb[:,:,1]
    b=rgb[:,:,2]
    return r,g,b

def imhist(r,show=True):
    if show==True:
        print('\nComenzando histograma ⌛\n')

    h = np.zeros(256)    
    filas,cols = r.shape
    for i in range(0,filas):
        for j in range(0,cols):
            h[r[i,j]] = h[r[i,j]]+1

    if show==True:
        print('\nHistograma completado ✅')
        print('\nGraficando histograma...')
        n = np.linspace(0,255,256)
        plt.bar(n,h)
        plt.set_cmap('gray')
        norm=mpl.colors.Normalize(vmin=0,vmax=255)
        escala=plt.cm.ScalarMappable(cmap='gray',norm=norm)
        escala.set_array([])
        plt.colorbar(escala,orientation="horizontal",ticks=[0,50,100,150,200,255])
        plt.xlim(0, 255)
        plt.ylim(0, max(h)*0.3)
    return h

def imadjust(I,E=None,S=(0,255),n=1):
    if E==None:
        E=stretchlim(I)
    Em=E[0]
    EM=E[1]
    Sm=S[0]
    SM=S[1]
    I=np.float16(I)
    Is=((SM-Sm)/(EM-Em)**n)*(np.absolute(I-Em))**n+Sm
    Is[np.where(Is>255)] = 255
    print('Em =',Em,'EM =',EM)
    return np.uint8(Is)

def stretchlim(I,Tol=0.01):
    Em=0
    EM=255
    h=imhist(I,False)
    i,j = np.shape(I)
    ha = np.zeros([256,1])
    hp = np.zeros([256,1])
    for k in range(256):
        ha[k]=np.sum(h[0:k+1])
        hp[k]=ha[k]/(i*j)
        if hp[k]<=0.01:
            Em=k
        if hp[k]<=1-Tol:
            EM=k
    return Em,EM

def histeq(I): # Try of a translation of a Matlab code.
    h=imhist(I,False)
    ha=np.zeros(256)
    for i in range(len(h)):
        ha[i]=np.sum(h[0:i])
    he=(ha/np.sum(h))*255
    S=np.uint8(he[I])
    return S

def rgb2gray(I):
    r,g,b=imsplit(I)
    return np.uint8(0.299*np.double(r)+0.587*np.double(g)+0.114*np.double(b))

def makeMask(ra,rb,ga,gb,ba,bb,img):
    r,g,b = imsplit(img)
    RGB = plt.imread(img)
    Maskr = (r>=ra) & (r<=rb)
    Maskg = (g>=ga) & (g<=gb)
    Maskb = (b>=ba) & (b<=bb)
    Mask = Maskr & Maskg & Maskb
    filas,columnas,capas = RGB.shape
    colorMask=np.zeros((filas,columnas,capas),dtype=np.uint8) # El tipo del arreglo debe ser uint8
    colorMask = np.dstack((Mask * r,Mask * g,Mask * b))
    # colorMask[:,:,0] = Mask * r # Es igual sin el uint8
    # colorMask[:,:,1] = np.uint8(Mask) * g
    # colorMask[:,:,2] = np.uint8(Mask) * b
    return Mask,colorMask

def graythresh(b):
    h = imhist(b,False)
    lh = len(h)
    tam = np.size(b)
    maxV = 0
    for T in range(lh):
        Acub = np.sum(h[0:T])
        Wb = Acub/tam
        Acuf = np.sum(h[T+1:lh])
        if Acub==0:
            Ub=0
        else:
            Ub=(np.arange(0,T,1) @ h[0:T])/Acub
        if Acuf==0:
            Uf = 0
        else:
            Uf=(np.arange(T+1,lh,1) @ h[T+1:lh])/Acuf
        Wf = 1-Wb
        BCV = Wb*Wf*(Ub-Uf)**2
        if BCV>=maxV:
            maxV=BCV
            umbral=(T+1)/255
    return umbral

def imnoise(I,tipo,P,V):
    filas, cols = I.shape
    if tipo == 'gaussian':
        print('\nSe usará el método de Gauss para añadir ruido')
        M=P
        S=V*255
        noise = np.random.normal(M,S,(filas,cols))
        return non_overflowing_sum(I,noise) 

    if tipo == 'salpimienta':
        print('\nSe usará el método de Sal Pimienta para añadir ruido')
        Puntos = filas*cols*V
        Ir = I
        for i in range(1,int(Puntos)):
            x = np.random.randint(1,filas)
            y = np.random.randint(1,cols)
            Ir[x,y]=np.uint8(255*np.random.randint(0,2))
        return Ir

    if tipo == 'spekle':
        print('\nSe usará el método de Spekle para añadir ruido')
        M=0
        S=V
        noise = np.random.normal(M,S,(filas,cols))
        return bits8(np.double(I) * (noise+1))
        
def non_overflowing_sum(I,noise):
    c = np.uint16(I)+noise
    c[np.where(c>255)] = 255
    c[np.where(I<0)] = 0
    return np.uint8(c)

def bits8(I):
    I[np.where(I>255)] = 255
    I[np.where(I<0)] = 0
    return np.uint8(I)

def immse(I,Ir):
    filas, cols = I.shape
    SE=(np.double(I)-np.double(Ir))**2
    return np.sum(SE)/(filas*cols)

def psnr(I,Ir):
    MSE = immse(I,Ir)
    PSNR = 10*np.log10(255**2/MSE)
    meanNoise = np.mean(np.double(Ir)**2)
    SNR = 10*np.log10(meanNoise/MSE)
    return PSNR, SNR

def imundersize(I,step):
    F,C,capas = I.shape
    return I[0:F:step,0:C:step]

def imfilter(I,K):
    n, m = K.shape
    n = int(n)
    m = int(m)
   
    iniF=(n+1)//2
    iniC=(m+1)//2
    finF=iniF - 1
    finC=iniC - 1
   
    I = np.double(I)
    Ipad=np.pad(I,(n,m),'edge')
   
    F, C = Ipad.shape
    T=np.zeros([F,C])
   
    for i in range(iniF,F-finF):
        for j in range(iniC,C-finC):
            V = Ipad[i-finF-1:i+finF,j-finC-1:j+finC]
            T[i,j] = np.sum(V*K)

    T=T[iniF:F-finF,iniC:C-finC]
    return bits8(T)

def fspecial(type,size=3,S=0.5,alpha=0.2): #Creador del Kernel
    if type.lower() == 'average':
        return np.ones([size,size])/size**2

    if type.lower() == 'gaussian': # Para revisar
        shape = (size-1)//2

        a = np.arange(-shape,shape+1)
        b = np.arange(-shape,shape+1)

        X,Y = np.meshgrid(a,b)
        S=0.5
        G=(1/(2*np.pi*S**2))*np.exp(-(X**2+Y**2)/(2*S**2))
        normalG = G / np.sum(G)
        print(normalG.shape)
        print(np.sum(normalG))
        return normalG

    if type.lower() == 'log':
        shape = (size-1)//2

        a = np.arange(-shape,shape+1)
        b = np.arange(-shape,shape+1)

        X,Y = np.meshgrid(a,b)
        G=1/(2*np.pi*S**2)*np.exp(-(X**2+Y**2)/(2*S**2))
        ks=np.sum(G)
        Termin_z=X**2 + Y**2 -2*S**2
        e=np.exp(-(X**2+Y**2)/(2*S**2))
        f=1/(2*np.pi*S**6*ks)
        Z=f*(Termin_z)*e
        my_K=Z-np.sum(Z)/size**2
        print(my_K.shape)
        print(np.sum(my_K))
        return my_K

    if type.lower() == 'laplacian':
        K = 4 / (alpha + 1) * np.array([[alpha/4,(1-alpha)/4,alpha/4],[(1-alpha)/4,-1,(1-alpha)/4],[alpha/4,(1-alpha)/4,alpha/4]])
        return K

    if type.lower() == 'prewitt':
        K = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
        return K

    if type.lower() == 'sobel':
        K = np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
        return K

def medfilt2(I,V):
    n = V[0]
    m = V[1]
    
    iniF=(n+1)//2
    iniC=(m+1)//2
    finF=iniF - 1
    finC=iniC - 1
    
    Ipad=np.pad(I,(finF,finC),'edge')
    
    F,C = Ipad.shape
    T=np.zeros([F,C])
    
    for i in range(iniF,F-finF):
        for j in range(iniC,C-finC):
            V = Ipad[i-finF-1:i+finF,j-finC-1:j+finC]
            order = np.sort(V.flatten())
            T[i,j] = order[(n*m+1)//2]

    T=T[iniF:F-finF,iniC:C-finC]
    return np.uint8(T)

def modefilt(I,W):
    n = W[0]
    m = W[1]
    
    iniF=(n+1)//2
    iniC=(m+1)//2
    finF=iniF - 1
    finC=iniC - 1
    
    Ipad=np.pad(I,(finF,finC),'edge')
    
    F,C = Ipad.shape
    T=np.zeros([F,C])
    
    for i in range(iniF,F-finF):
        for j in range(iniC,C-finC):
            V = Ipad[i-finF-1:i+finF,j-finC-1:j+finC]
            moda = stat.mode(V.flatten())
            T[i,j] = moda

    T=T[iniF:F-finF,iniC:C-finC]
    return np.uint8(T)

def ordfilt2(I,Termino,K):
    n, m = K.shape
    
    iniF=(n+1)//2
    iniC=(m+1)//2
    finF=iniF - 1
    finC=iniC - 1
    
    Ipad=np.pad(I,(finF,finC),'edge')
    
    F,C = Ipad.shape
    T=np.zeros([F,C])
    
    for i in range(iniF,F-finF):
        for j in range(iniC,C-finC):
            V = Ipad[i-finF-1:i+finF,j-finC-1:j+finC] * K
            order = np.sort(V.flatten())
            T[i,j] = order[Termino]

    T=T[iniF:F-finF,iniC:C-finC]
    return np.uint8(T)

def stdfilt(I,K):
    n, m = K.shape
    n = int(n)
    m = int(m)
    
    iniF=(n+1)//2
    iniC=(m+1)//2
    finF=iniF - 1
    finC=iniC - 1
    
    Ipad=np.pad(I,(finF,finC),'edge')
    
    F,C = Ipad.shape
    T=np.zeros([F,C])
    
    for i in range(iniF,F-finF):
        for j in range(iniC,C-finC):
            V = Ipad[i-finF-1:i+finF,j-finC-1:j+finC]
            T[i,j] = np.std(V*K)

    T=T[iniF:F-finF,iniC:C-finC]
    return T

def entropyfilt(I,K): # Para revisar
    n, m = K.shape
    n = int(n)
    m = int(m)
    
    iniF=(n+1)//2
    iniC=(m+1)//2
    finF=iniF - 1
    finC=iniC - 1
    
    Ipad=np.pad(I,(finF,finC),'edge')
    
    F,C = Ipad.shape
    T=np.zeros([F,C])
    
    for i in range(iniF,F-finF):
        for j in range(iniC,C-finC):
            V = Ipad[i-finF-1:i+finF,j-finC-1:j+finC]
            S = np.uint8(V*K)
            hist = imhist(S,False)
            normalHist = hist/np.sum(S)
            # T[i,j] = -np.sum(p*np.log2(p))
            T[i,j] = -np.dot(normalHist,np.log2(normalHist))

    T=T[iniF:F-finF,iniC:C-finC]
    return T

def gaussfilt(cosas):
    print(cosas)

def im2bw(I,T):
    if isinstance(T,np.ndarray):
        return I>=T
    if T < 1: T = T * 255
    return I>=T

def otsuthresh(h):
    lh = len(h)
    tam = np.sum(h)
    maxV = 0
    for T in range(lh):
        Acub = np.sum(h[0:T])
        Wb = Acub/tam
        Acuf = np.sum(h[T+1:lh])
        if Acub==0:
            Ub=0
        else:
            Ub=(np.arange(0,T,1) @ h[0:T])/Acub
        if Acuf==0:
            Uf = 0
        else:
            Uf=(np.arange(T+1,lh,1) @ h[T+1:lh])/Acuf
        Wf = 1-Wb
        BCV = Wb*Wf*(Ub-Uf)**2
        if BCV>=maxV:
            maxV=BCV
            umbral=(T+1)/255
    return umbral
    
def imbinarize(I,T=False,method='otsu'):
    if T != False:
        return im2bw(I,T)
    if method == 'otsu':
        print('Usando OTSU')
        T = graythresh(I)
        return im2bw(I,T)
    if method == 'bradley':
        print('Usando bradley')
        T = adaptthresh(I)
        return im2bw(I,T)

def adaptthresh(r,V=[3,3],Pb=10,Ks=0.2,Rs=128,method='bradley'):
    padn=(V[0]-1)//2
    padm=(V[1]-1)//2
    padr=np.pad(r,(padn,padm),'edge')
    F, C = r.shape
    T=np.zeros([F,C])

    iniF=(V[0]+1)//2
    iniC=(V[1]+1)//2
    FinF=iniF-1
    FinC=iniC-1

    for i in range(iniF,F-FinF):
        for j in range(iniC,C-FinC):
            W = padr[i-FinF-1:i+FinF,j-FinC-1:j+FinC]
            if method.lower() == 'bradley': T[i,j]=np.mean(W)*(1-Pb/100)
            if method.lower() == 'sauvola': T[i,j]=np.mean(W)*(1+Ks*(np.std(W)/Rs-1))
            if method.lower() == 'mean': T[i,j]=np.mean(W)
            if method.lower() == 'median': T[i,j]=np.median(W)
            if method.lower() == 'mode': T[i,j]=stat.mode(W.flatten())
            if method.lower() == 'maxmin': T[i,j]=(np.max(W)+np.min(W))/2
    return T
