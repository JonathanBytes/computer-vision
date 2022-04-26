import numpy as np

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
            if method.lower() == 'sauvola':
                T[i,j]=np.mean(W)*(1+Ks*(np.std(W)/Rs-1)) #Souvola
            if method.lower() == 'bradley':
                T[i,j]=np.mean(W)*(1-Pb/100)
    return T
