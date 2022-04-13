clc
clear all; close all
RGB=imread('cartagena.jpg');

Gris=rgb2gray(RGB);
paso=4;
Gris=Gris(1:paso:end,1:paso:end);

figure()
imshow(Gris)

%Ir=imnoise(gris,'salt & pepper',0.2);
%Ir=imnoise(gris,'gaussian',0.2);

%figure()
%imshow(Ir)

L=21; K=ones(L)/L^2;
V=[5,5]
n=V(1);
m=V(2);


iniF=(n+1)/2;
iniC=(m+1)/2;
finF=iniF-1;
finC=iniC-1;
Ipad=padarray(Gris,[finF finC],'replicate');
[F C]=size(Ipad);
T=zeros(F,C);
for i=iniF:F-finF
    for j=iniC:C-finC
        V=Ipad(i-finF:i+finF,j-finC:j+finC);
        Orden=sort(V(:));
        T(i,j)=Orden((n*m+1)/2);
    end
end
T=uint8(T);
T=T(iniF:F-finF,iniC:C-finC);


If = T;
%If=my_imfilter(Gris,K);

figure()
imshow(If)

%Ifmed=my_medfilt2(Ir,[5,5]);

%figure()
%imshow(Ifmed)

%Ifmoda=my_modfilt(Ir,[5,5]);
%Ifmoda=my_modfilt(gris,[15,15]);

%figure()
%imshow(Ifmoda)

%Ifmin=my_ordfilt2(gris,1,ones(3,3));

%figure()
%imshow(Ifmin)
