clc
clear all; close all
RGB=imread('cartagena.jpg');

gris=rgb2gray(RGB);
paso=4;
gris=gris(1:paso:end,1:paso:end);

%figure()
%imshow(gris)

%Ir=imnoise(gris,'salt & pepper',0.2);
%Ir=imnoise(gris,'gaussian',0.2);

%figure()
%imshow(Ir)

L=21; K=ones(L)/L^2;

If=my_imfilter(gris,K);

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
