RGB = imread('cartagena.jpg');
[r,g,b]= imsplit(RGB);

Ir_g = imnoise(r,'gaussian',0,0.1);

figure()
subplot(1,2,1)
title('Imagen de referencia')
imshow(r)

subplot(1,2,2)
title('Imagen con ruido')
imshow(Ir_g)

my_MSE = immse(r,Ir_g)

PSNR, SNR = psnr(r,Ir_g)