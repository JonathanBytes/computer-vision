RGB = imread('bullet.jpg');

gris=rgb2gray(RGB);
K=fspecial('log',21,3);
If=imfilter(gris,K);
bw=imbinarize(If);
figure()
imshow(bw,[])
hold on

[centers, radii]=imfindcircles(bw,[15 30],'sensitivity',0.8);
my_viscircles(centers,radii,'b')

[centers, radii]=imfindcircles(bw,[50 80],'sensitivity',0.8);
my_viscircles(centers,radii,'r')

[centers, radii]=imfindcircles(bw,[80 350],'sensitivity',0.9);
my_viscircles(centers,radii,'g')

[X Y]=meshgrid(1:1000,1:500);

M=(X-centers(2,1)).^2+(Y-centers(2,2)).^2> radii(2).^2;

figure()
imshow(uint8(~M).*RGB)
