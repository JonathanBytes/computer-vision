import numpy as np

def adaptthresh(r,V=[3,3],Pb=10):
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
            T[i,j]=np.mean(W)*(1-Pb/100)
    return T
