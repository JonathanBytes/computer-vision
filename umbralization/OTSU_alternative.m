rgb=imread('papel.jpg');
[r,g,b] = imsplit(rgb);
r=fliplr(r');

figure()
subplot(1,2,1)
imshow(r)

paso=2;
r=r(1:paso:end,1:paso:end);

T=graythresh(r)
hist = imhist(r);
T=otsuthresh(hist)
bw=im2bw(r,T);
subplot(1,2,2)
imshow(bw)
