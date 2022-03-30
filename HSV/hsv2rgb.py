import numpy as np
    
def my_hsv2rgb(hsv = None): 
    F = 1
    N,M,L = hsv.shape
    X = np.zeros((N,M))
    m = np.zeros((N,M))
    R = np.zeros((N,M))
    G = np.zeros((N,M))
    B = np.zeros((N,M))
    v = hsv(:,:,3)
    s = hsv(:,:,2)
    h = hsv(:,:,1) * 360
    for i in np.arange(1,N+1).reshape(-1):
        for j in np.arange(1,M+1).reshape(-1):
            C[i,j] = v(i,j) * s(i,j)
            X[i,j] = C(i,j) * (1 - np.abs(np.mod(h(i,j) / 60,2) - 1))
            m[i,j] = v(i,j) - C(i,j)
            if h(i,j) >= 0 and h(i,j) < 60 / F:
                R[i,j] = C(i,j)
                G[i,j] = X(i,j)
                B[i,j] = 0
            else:
                if h(i,j) >= 60 / F and h(i,j) < 120 / F:
                    R[i,j] = X(i,j)
                    G[i,j] = C(i,j)
                    B[i,j] = 0
                else:
                    if h(i,j) >= 120 / F and h(i,j) < 180 / F:
                        R[i,j] = 0
                        G[i,j] = C(i,j)
                        B[i,j] = X(i,j)
                    else:
                        if h(i,j) >= 180 / F and h(i,j) < 240 / F:
                            R[i,j] = 0
                            G[i,j] = X(i,j)
                            B[i,j] = C(i,j)
                        else:
                            if h(i,j) >= 240 / F and h(i,j) < 300 / F:
                                R[i,j] = X(i,j)
                                G[i,j] = 0
                                B[i,j] = C(i,j)
                            else:
                                if h(i,j) >= 300 / F and h(i,j) < 360 / F:
                                    R[i,j] = C(i,j)
                                    G[i,j] = 0
                                    B[i,j] = X(i,j)
            #Fin -------------------
    
    r = (R + m) * 255
    g = (G + m) * 255
    b = (B + m) * 255
    return r,g,b
    
    return r,g,b