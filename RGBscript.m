R=imread('RGB photos/cubes_R.jpg');
G=imread('RGB photos/cubes_G.jpg');
B=imread('RGB photos/cubes_B.jpg');
C=imread('RGB photos/cubes_color.jpg');

r=R(:,:,1);
g=G(:,:,2);
b=B(:,:,3);

[filas columnas capas]=size(C);

I=uint8(zeros(filas, columnas, capas));

I(:,:,1)=r;
I(:,:,2)=g;
I(:,:,3)=b;

figure(1)
subplot(1,2,1)
imshow(C)
subplot(1,2,2)
imshow(I)
