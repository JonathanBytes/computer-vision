clc
clear all
close all
RGB=imread('cartagena.jpg');
[r,g,b]=imsplit(RGB);

figure()
imshow(r)
[filas,cols]=size(r);
porcentaje = 1;
Puntos=filas*cols*porcentaje;

Ir=r;

for i=1:Puntos
    x=randi(filas);
    y=randi(cols);
    Ir(x,y)=255*rand(1);
end

figure()
imshow(Ir)