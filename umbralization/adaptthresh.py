import numpy as np

def adaptthresh(r,V,Pb):
    padn=(V[0]-1)//2
    padm=(V[1]-1)//2
    padr=np.pad(r,(padn,padm),'edge')
    filas,cols = r.shape
    T=np.zeros([filas,cols])

    iniF=(V[0]+1)//2
    iniC=(V[1]+1)//2
    FinF=iniF-1
    FinC=iniC-1

    for i in range(iniF,cols-FinF):
        for j in range(iniC,cols-FinC):
            W = padr[i-FinF:i+FinF,j-FinC:j+FinC]
            T[i,j]=np.mean(W)*(1-Pb/100)
    return T


