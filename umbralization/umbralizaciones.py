from ipFunctions import *
import numpy as np
import matplotlib.pyplot as plt

RGB = plt.imread('papel.jpg');

r, g, b = imsplit(RGB);
r=np.fliplr(np.transpose(r))
r = imundersize(r,8)

# T = graythresh(r)
# h = imhist(r,False)
# T2 = otsuthresh(h)
# print('T = %f T2 = %f'%(T,T2))
# bw = im2bw(r,T2)

bw = imbinarize(r)

plt.figure()
plt.set_cmap('gray')
plt.imshow(bw)

# padr=double(padarray(r,[1 1],'replicate'));
# [filas,cols]=size(r);
# T=zeros(filas+2,cols+2);

# n=15;
# m=15;

# IniC=(m+1)/2;
# IniF=(n+1)/2;
# FinC=IniC-1;
# FinF=IniF-1;
# Ks=0.2;
# Rs=128;

# for i=IniF:filas-(FinF)
#     for j=IniC:cols-(FinC)
#         W=padr(i-FinF:i+FinF,j-FinC:j+FinC);
#         %T(i,j)=mean(W(:)); %media
#         %T(i,j)=mode(W(:)); %moda
#         %T(i,j)=median(W(:)); %mediana
#         %T(i,j)=(max(W(:))+min(W(:)))/2; %maxmin
#         %T(i,j)=mean(W(:))*(1+Ks*(std((W(:)))/Rs-1)); %Souvola
#         % T(i,j)=mean(W(:))*(1-Pb/100); %Bradley
#     end
# end

# bw=padr>=T;

# figure(3)
# imshow(bw)

plt.show()
