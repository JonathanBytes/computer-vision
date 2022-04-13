import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def imsplit(rgb):
    r=rgb[:,:,0]
    g=rgb[:,:,1]
    b=rgb[:,:,2]
    return r,g,b

def imhist(r,show=True):
    print('\nComenzando histograma ⌛\n')
    h = np.zeros(256)    
    filas,cols = r.shape
    for i in range(1,filas):
        for j in range(1,cols):
            h[r[i,j]] = h[r[i,j]]+1
    print('\nHistograma completado ✅')
    if show==True:
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
        print('\nSe usará el método de Gauss')
        M=P
        S=V*255
        noise = np.random.normal(M,S,(filas,cols))
        return non_overflowing_sum(I,noise) 

    if tipo == 'salpimienta':
        print('\nSe usará el método de Sal Pimienta')
        Puntos = filas*cols*V
        print(Puntos,'puntos')
        Ir = I
        for i in range(1,int(Puntos)):
            x = np.random.randint(1,filas)
            y = np.random.randint(1,cols)
            Ir[x,y]=np.uint8(255*np.random.randint(0,1))
        return Ir
    if tipo == "spekle":
        M=0
        S=P
        noise= np.random.normal(M,S,[filas, cols])
        return np.uint8(I * (noise+1))
        
def non_overflowing_sum(I,noise):
    c = np.uint16(I)+noise
    c[np.where(c>255)] = 255
    return np.uint8(c)

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

def undersize(I,step):
    F,C = I.shape
    return I[0:F:step,0:C:step]

def imfilter(I,K):
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
            T[i,j] = np.sum(V*K)

    T=T[iniF:F-finF,iniC:C-finC]
    return np.uint8(T)