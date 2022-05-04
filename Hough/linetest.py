from ipFunctions import *
import matplotlib.pyplot as plt
import numpy as np

RGB = plt.imread('linea1.jpg')
ri, g, b = imsplit(RGB)
step = 1
ri = imundersize(ri,step)

plt.figure()
plt.set_cmap('gray')
plt.imshow(ri)

T=graythresh(ri)
bw=~im2bw(ri,T)

# figure(2)
# imshow(bw)

M, N = bw.shape
rhomax = np.ceil((N**2+M**2)**0.5)
angulo = 90
theta = np.arange(-angulo,angulo+1,step)
thetamax = len(theta)
H = np.zeros([int(thetamax),int(2*rhomax)])
rho = np.arange(-rhomax,rhomax+1)

# figure(3)
# imshow(H)

for i in range(1,N):
    for j in range(1,M):
        if bw[i,j]==1:
            for t in theta:
                r=(np.ceil(j*np.cos(np.radians(t))+i*np.sin(np.radians(t))))+1
                H[int(t+angulo),int(r+rhomax+1)]=H[int(t+angulo),int(r+rhomax+1)]+1

H = np.transpose(H)
a = imadjust(np.uint8(H / np.max(H)))
print(a)

plt.figure()
# plt.imshow(a,'XData',theta,'YData',rho,'InitialMagnification','fit')
plt.imshow(histeq(np.uint8(a/np.max(a))))
plt.title('Hough transform');
plt.xlabel('theta') 
plt.ylabel('rho')
# axis on, axis normal, hold on;
plt.set_cmap('hot')

a, b = np.where(H==np.max(H))
print(a,b)

rhoL=rho[a]
thetaL=theta[b]

x = np.arange(1,M)
y = - (1/(np.tan(np.radians(thetaL))))*x+rhoL/np.sin(np.radians(thetaL))

plt.figure()
plt.imshow(ri)
plt.plot(x,y,'r--')

plt.show()
