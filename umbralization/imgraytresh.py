import matplotlib.pyplot as plt
from ipFunctions import *
import numpy as np

RGBgray = 'mango6.jpg'
RGB = plt.imread(RGBgray)

h=imhist(RGBgray)
lh=len(h)
filas,cols=RGB.shape
tan=filas*cols;
maxV=0
for T in range(1,lh-1):
    wb=sum(h[1:T])/tan
    ub=sum((1:T-1)*h[1:T])/sum(h[1:T]);

    wf=1-wb;
    uf=sum(([T:lh-1])*h(T+1:end))/sum(h(T+1:end));

    BCV=wb*wf*(ub-uf)^2;
        if BCV >= maxV
            maxV=BCV;
            umbral=(T-1)/255;
