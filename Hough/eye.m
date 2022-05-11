RGB = imread('ojo2.jpg');

gris=rgb2gray(RGB);
K=fspecial('log',21,3);
If=imfilter(gris,K);
bw=imbinarize(If);
figure()
imshow(bw,[])
hold on

[centers, radii]=imfindcircles(bw,[20 25],'sensitivity',0.94);
my_viscircles(centers,radii,'b')

[centers, radii]=imfindcircles(bw,[50 80],'sensitivity',0.9);
my_viscircles(centers,radii,'r')

[centers, radii]=imfindcircles(bw,[80 350],'sensitivity',0.9);
my_viscircles(centers,radii,'g')


