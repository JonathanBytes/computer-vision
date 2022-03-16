import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def imsplit(img):
    rgb = plt.imread(img)
    r=rgb[:,:,0]
    g=rgb[:,:,1]
    b=rgb[:,:,2]
    return r,g,b

def imhist(r,show=True):
    h = np.zeros(256)    
    filas,cols = r.shape
    for i in range(1,filas):
        for j in range(1,cols):
            h[r[i,j]] = h[r[i,j]]+1
    if show==True:
        n = np.linspace(0,255,256)
        plt.bar(n,h)
        plt.set_cmap('gray')
        norm=mpl.colors.Normalize(vmin=0,vmax=255)
        escala=plt.cm.ScalarMappable(cmap='gray',norm=norm)
        escala.set_array([])
        plt.colorbar(escala,orientation="horizontal",ticks=[0,50,100,150,200,255])
        plt.xlim(0, 255)
        plt.ylim(0, max(h)*0.3)
        # plt.xlabel('Intensidad')
        # plt.ylabel('Cantidad')
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

""" def imhisteq(img):
    x,y = img.shape
    histeq = np.zeros(256)
    n=k=1
    hist = imhist(img,False)
    for n in range(256):
            for k in range(n):
                print('n =',n,'k =',k)
                histeq[n] = histeq[n] + hist[k]
            histeq = (histeq[n]) / (x * y)
    recon = np.zeros(256)       
    for i in range(x):
            for j in range(y):
                recon[i,j] = np.int8(histeq[img[i,j]+1]*255)
    return recon """

def histeq(I): # Try of a translation of a Matlab code.
    h=imhist(I,False)
    ha=np.zeros(255)
    for i in range(len(h)):
        ha[i]=np.sum(h[0:i])
    he=(ha/np.sum(h))*255
    S=np.uint8(he[I])
    return S

def rbg2gray(I):
    r,g,b=imsplit(I)
    return np.uint8(0.299*np.double(r)+0.587*np.double(g)+0.114*np.double(b))