clc;clear all;
RGB = imread('mango6.jpg');

[r,g,b] = imsplit(RGB);
bina_r=r>=140;
bina_g=g>=145;
bina_b=b>=125;

figure()
subplot(3,3,1)
imshow(r)
subplot(3,3,4)
imhist(r)
subplot(3,3,7)
imshow(bina_r)

subplot(3,3,2)
imshow(g)
subplot(3,3,5)
imhist(g)
subplot(3,3,8)
imshow(bina_g)

subplot(3,3,3)
imshow(b)
subplot(3,3,6)
imhist(b)
subplot(3,3,9)
imshow(bina_b)

for T=1:255
    bb=b>=T;
    figure(2)
    imshow(bb)
    pause(0.001)
end