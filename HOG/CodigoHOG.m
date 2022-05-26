clc
clearvars
close all
[filename,pathname] = uigetfile({'*.png';'*.jpg';'*.jpeg'},...
'C:\Users\sepul\OneDrive\Escritorio\MACHINE LEARNING\HOG Proyecto\Imagenes','Seleccione una imagen');

filename=strcat(pathname,filename);
Imagen=imresize(imread(filename),[256,128]);
ImagenGris=im2gray(Imagen);

Kx=[-1 -2 -1;
     0  0  0;
     1  2  1];

Ky=[-1  0  1;
    -2  0  2;
    -1  0  1];

Ipwx=imfilter(double(ImagenGris),Kx);
Ipwy=imfilter(double(ImagenGris),Ky);

% Ipwx=my_prewitt(ImagenGris,Kx);
% Ipwy=my_prewitt(ImagenGris,Ky);
% Ipwx=im2double(Ipwx);
% Ipwy=im2double(Ipwy);

Gmag=sqrt(Ipwx.^2+Ipwy.^2);
Gangulo=abs(rad2deg(atan2(Ipwy,Ipwx)));

[Gmag2,Gangulo2]=imgradient(ImagenGris,'sobel');


figure(1);
subplot(121);imshow(Imagen);title('Imagen RGB');
subplot(122);imshow(ImagenGris);title('Imagen gris');

figure(2);
subplot(121);imshow(Ipwx);title('Sobel horizontal');
subplot(122);imshow(Ipwy);title('Sobel vertical');

figure(3);
subplot(121);imshowpair(Gmag,Gmag2,'montage');title('Magnitud del gradiente propio y MATLAB');
subplot(122);imshowpair(Gangulo,Gangulo2,'montage');title('Angulos del grandiente propio y MATLAB');

figure(4);
subplot(131);imshow(ImagenGris);
subplot(132);quiver(flipud(Ipwx),flipud(Ipwy));
subplot(133);imshow(ImagenGris);hold on; quiver(Ipwx,Ipwy);hold off;


[featureVector,hogVisualization] = extractHOGFeatures(Imagen);
featureVector=rad2deg(featureVector);

figure(5);
subplot(121);plot(hogVisualization);
subplot(122);histogram(featureVector);

M=Gmag;
A=Gangulo;
[F C]=size(M);

bin=9;
bloques=(F*C)/64;
H=zeros(bloques,bin);
contador=1;

while contador<bloques
for j=1:8:F
    for i=1:8:C
        m=M(j:j+7,i:i+7);
        a=A(j:j+7,i:i+7);
        for jj=1:8
            for ii=1:8
            
                if a(ii,jj)>=0 && a(ii,jj)<=20
                    H(contador,1)=m(ii,jj)*((20-a(ii,jj))/20)+H(contador,1);
                    H(contador,2)=m(ii,jj)*(a(ii,jj)-0)/20+H(contador,2);
                
                elseif a(ii,jj)>20 && a(ii,jj)<=40
                    H(contador,2)=m(ii,jj)*((40-a(ii,jj))/20)+H(contador,2);
                    H(contador,3)=m(ii,jj)*(a(ii,jj)-20)/20+H(contador,3);
                
                elseif a(ii,jj)>40 && a(ii,jj)<=60
                    H(contador,3)=m(ii,jj)*((60-a(ii,jj))/20)+H(contador,3);
                    H(contador,4)=m(ii,jj)*(a(ii,jj)-40)/20+H(contador,4);

                elseif a(ii,jj)>60 && a(ii,jj)<=80
                    H(contador,4)=m(ii,jj)*((80-a(ii,jj))/20)+H(contador,4);
                    H(contador,5)=m(ii,jj)*(a(ii,jj)-60)/20+H(contador,5);

                elseif a(ii,jj)>80 && a(ii,jj)<=100
                    H(contador,5)=m(ii,jj)*((100-a(ii,jj))/20)+H(contador,5);
                    H(contador,6)=m(ii,jj)*(a(ii,jj)-80)/20+H(contador,6);

                elseif a(ii,jj)>100 && a(ii,jj)<=120
                    H(contador,6)=m(ii,jj)*((120-a(ii,jj))/20)+H(contador,6);
                    H(contador,7)=m(ii,jj)*(a(ii,jj)-100)/20+H(contador,7);

                elseif a(ii,jj)>120 && a(ii,jj)<=140
                    H(contador,7)=m(ii,jj)*((140-a(ii,jj))/20)+H(contador,7);
                    H(contador,8)=m(ii,jj)*(a(ii,jj)-120)/20+H(contador,8);

                elseif a(ii,jj)>140 && a(ii,jj)<=160
                    H(contador,8)=m(ii,jj)*((160-a(ii,jj))/20)+H(contador,8);
                    H(contador,9)=m(ii,jj)*(a(ii,jj)-140)/20+H(contador,9);
                
                elseif a(ii,jj)>160
                    H(contador,1)=m(ii,jj)*((a(ii,jj)-160)/20)+H(contador,1);
                    H(contador,9)=a(ii,jj)-(m(ii,jj)*((a(ii,jj)-160)/20))+H(contador,9);
                   
                end
            end
        end
        contador=contador+1;
    end
end
end

H2=(H(:)');
figure(6);
bar(H2);
