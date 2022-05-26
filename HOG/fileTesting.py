import matplotlib.pyplot as plt
import numpy as np
from ipFunctions import *

file_path = getuserpath()

print('Se usará la imagen:',file_path)

RGB = plt.imread(file_path)
gray = rgb2gray(RGB)
RGB = resize(RGB, (128, 64))
img = resize(gray, (128, 64))

mag = []
theta = []
for i in range(128):
  magnitudeArray = []
  angleArray = []
  for j in range(64):
    # Condition for axis 0
    if j-1 <= 0 or j+1 >= 64:
      if j-1 <= 0:
        # Condition if first element
        Gx = img[i][j+1] - 0
      elif j + 1 >= len(img[0]):
        Gx = 0 - img[i][j-1]
    # Condition for first element
    else:
      Gx = img[i][j+1] - img[i][j-1]
    
    # Condition for axis 1
    if i-1 <= 0 or i+1 >= 128:
      if i-1 <= 0:
        Gy = 0 - img[i+1][j]
      elif i +1 >= 128:
        Gy = img[i-1][j] - 0
    else:
      Gy = img[i-1][j] - img[i+1][j]

    # Calculating magnitude
    magnitude = np.sqrt(pow(Gx, 2) + pow(Gy, 2))
    magnitudeArray.append(round(magnitude, 9))

    # Calculating angle
    if Gx == 0:
      angle = np.degrees(0.0)
    else:
      angle = np.degrees(abs(np.arctan(Gy / Gx)))
    angleArray.append(round(angle, 9))
  mag.append(magnitudeArray)
  theta.append(angleArray)

mag = np.array(mag)
mag = mag / np.max(mag)
theta = np.array(theta)

print('mag %f , theta %f'%(np.min(mag),np.max(mag)))

fig, ax = plt.subplots(figsize = (12, 7))
step = 1
for i in range(0,128,step):
    for j in range(0,64,step):
        x = mag[i,j] * np.cos(np.radians(theta[i,j]))
        y = mag[i,j] * np.sin(np.radians(theta[i,j]))
        ax.quiver(j, i, x, y, scale=None, color=(mag[i,j],mag[i,j],mag[i,j]),headaxislength=3,headlength=3,linewidth=30)
        ax.set_title('Quiver plot with one arrow')
    if i%5==0:
        print('mag = %f , theta = %f, i = %i , j = %i'%(mag[i,j],theta[i,j],i,j))

ax.set_facecolor('black')
ax.axis([0, 64, 0, 128])
ax.set_aspect('equal')

plt.figure()
plt.subplot(1,2,1)
plt.imshow(RGB)
plt.subplot(1,2,2)
plt.imshow(gray)

plt.set_cmap('gray')
plt.show()
