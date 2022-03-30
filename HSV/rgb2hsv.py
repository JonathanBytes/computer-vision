import numpy as np
    
def my_rgb2hsv(I = None): 
    r = double(I(:,:,1)) / 255
    g = double(I(:,:,2)) / 255
    b = double(I(:,:,3)) / 255
    N,M,L = I.shape
    Cmax = np.zeros((N,M))
    d = np.zeros((N,M))
    H = np.zeros((N,M))
    S = np.zeros((N,M))
    V = np.zeros((N,M))
    for i in np.arange(1,N+1).reshape(-1):
        for j in np.arange(1,M+1).reshape(-1):
            maximo = np.amax(np.amax(r(i,j),g(i,j)),b(i,j))
            minimo = np.amin(np.amin(r(i,j),g(i,j)),b(i,j))
            Cmax[i,j] = maximo
            Cmin[i,j] = minimo
            d[i,j] = maximo - minimo
            #para H-----------
            if d(i,j) == 0:
                H[i,j] = 0
            if r(i,j) == maximo:
                H[i,j] = 60 * np.mod((g(i,j) - b(i,j)) / d(i,j),6)
            else:
                if g(i,j) == maximo:
                    H[i,j] = 60 * ((g(i,j) - b(i,j)) / d(i,j) + 2)
                else:
                    if b(i,j) == maximo:
                        H[i,j] = 60 * ((g(i,j) - b(i,j)) / d(i,j) + 4)
            #Fin H-----------------
            #Para S----------------
            if maximo == 0:
                S[i,j] = 0
            else:
                S[i,j] = d(i,j) / maximo
            #Fin S---------------
            #Para V--------------
            V[i,j] = maximo
            #fin V---------------
    
    H = H / 360
    return H,S,V
    
    return H,S,V