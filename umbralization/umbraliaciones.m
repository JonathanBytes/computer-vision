clc
clear all
RGB=imread('papel.jpg');
[r,g,b]=imsplit(RGB);
r=fliplr(r');
step=8;
r=r(1:step:end,1:step:end);
% T=graythresh(r);
% hist=imhist(r);
% T=otsuthresh(hist);
% bw=im2bw(r,T);
%
%
% figure(1)
% imshow(r)
%
% figure(2)
% imshow(bw)
padr=double(padarray(r,[1 1],'replicate'));
[filas,cols]=size(r);
T=zeros(filas+2,cols+2);

n=15;
m=15;

IniC=(m+1)/2;
IniF=(n+1)/2;
FinC=IniC-1;
FinF=IniF-1;
Ks=0.2;
Rs=128;

for i=IniF:filas-(FinF)
    for j=IniC:cols-(FinC)
        W=padr(i-FinF:i+FinF,j-FinC:j+FinC);
        %T(i,j)=mean(W(:));
        %T(i,j)=mode(W(:));
        %T(i,j)=median(W(:));
        %T(i,j)=(max(W(:))+min(W(:)))/2;
        T(i,j)=mean(W(:))*(1+Ks*(std((W(:)))/Rs-1));
    end
end

bw=padr>=T;

figure(3)
imshow(bw)
