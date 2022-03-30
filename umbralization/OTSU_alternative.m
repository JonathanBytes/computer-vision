clear all

rgb=imread('papel.jpg');
[r,g,b] = imsplit(rgb);
r=fliplr(r');

% figure()
% subplot(1,5,1)
% imshow(r)

paso=4;
r=r(1:paso:end,1:paso:end);

% T=graythresh(r);
% hist = imhist(r);
% T=otsuthresh(hist)
% bw=im2bw(r,T);
% subplot(1,5,2)
% imshow(bw)

padr = padarray(r,[1 1],'replicate');

[filas,cols]=size(padr);
prom = zeros(filas,cols);
prom2 = zeros(filas,cols);
prom3 = zeros(filas,cols);
prom4 = zeros(filas,cols);

n=3;m=5;
iniF=(n+1)/2;
iniC=(m+1)/2;
FinF=iniF-1;
FinC=iniC-1;

for i=iniF:filas-FinF
    for j=iniC:cols-FinC
        w = padr(i-FinF:i+FinF,j-FinC:j+FinC)
        %prom(i,j) = mean(w(:));
        %prom2(i,j) = median(w(:));
        %prom3(i,j) = mode(w(:));     
        prom(i,j) = (max(w(:))+min(w(:)))/2;
    end
end

% bw=padr>=prom;
% subplot(1,5,3)
% imshow(bw)