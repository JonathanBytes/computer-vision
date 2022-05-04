clc 
clear all
RGB=imread('linea1.jpg');
[ri,g,b]=imsplit(RGB);
step=1;
ri=ri(1:step:end,1:step:end);

figure(1)
imshow(ri)

T=graythresh(ri);
bw=~im2bw(ri,T);

% figure(2)
% imshow(bw)

[M N]=size(bw);
rhomax=ceil((N^2+M^2)^0.5);
angulo=90
theta=[-angulo:step:angulo];
thetamax=length(theta);
H=zeros(thetamax,2*rhomax);
rho=[-rhomax:rhomax];

% figure(3)
% imshow(H)

for i=1:M
    for j=1:N
        if bw(i,j)==1
            for t=theta
                r=(ceil(j*cosd(t)+i*sind(t)))+1;
                H(t+angulo+1,r+rhomax+1)=H(t+angulo+1,r+rhomax+1)+1;
            end
        end
    end
end

figure(4)
imshow(imadjust(H/max(H(:)))','XData',theta,'YData',rho,'InitialMagnification','fit');
title('Hough transform');
xlabel('\theta'), ylabel('\rho');
axis on, axis normal, hold on;
colormap(gca,hot);
[H, T, R]=hough(bw,'RhoResolution',1,'Theta',-90:1:89);
figure(5)
imshow(imadjust(rescale(H)),'XData',T,'YData',R,'InitialMagnification','fit');
title('Hough transform');
xlabel('\theta'), ylabel('\rho');
axis on, axis normal, hold on;
colormap(gca,hot);

[a b]=find(H==max(H(:)))

rhoL=rho(a)
thetaL=theta(b)

x=[1:M]
y=-cotd(thetaL)*x+rhoL/sind(thetaL)

figure(6)
imshow(ri)
hold on
plot(x,y,'r--')
hold off
