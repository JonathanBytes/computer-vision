import matplotlib.pyplot as plt
import numpy as np
from ipFunctions import *

file_path = getuserpath()

print('Se usará la imagen:',file_path)

# RGB = plt.imread(file_path)
# gray = rgb2gray(RGB)
# RGB = resize(RGB, (128, 64))
# img = resize(gray, (128, 64))

RGB = plt.imread(file_path)
RGB = imundersize(RGB,4)
img = gray = rgb2gray(RGB)

F,C,capas= RGB.shape

print(F,C)

mag = []
theta = []
for i in range(F):
  magnitudeArray = []
  angleArray = []
  for j in range(C):
    # Condition for axis 0
    if j-1 <= 0 or j+1 >= C:
      if j-1 <= 0:
        # Condition if first element
        Gx = img[i][j+1] - 0
      elif j + 1 >= len(img[0]):
        Gx = 0 - img[i][j-1]
    # Condition for first element
    else:
      Gx = img[i][j+1] - img[i][j-1]
    
    # Condition for axis 1
    if i-1 <= 0 or i+1 >= F:
      if i-1 <= 0:
        Gy = 0 - img[i+1][j]
      elif i +1 >= F:
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

print('mag %s , theta %s'%(mag.shape,theta.shape))

fig, ax = plt.subplots(figsize = (12, 7))
step = 14
for i in range(0,F,step):
    for j in range(0,C,step):
        x = np.cos(np.radians(theta[i,j]))
        y = np.sin(np.radians(theta[i,j]))
        ax.quiver(j, abs(i-F), x, y, scale=40, color=(mag[i,j],mag[i,j],mag[i,j]),headaxislength=3,headlength=3)
        # ax.arrow(j, abs(i-F), x, y, color=(mag[i,j],mag[i,j],mag[i,j]),width=step/8,head_width=step/4)
        ax.set_title('Quiver plot with one arrow')
    if i%10==0:
        print('mag = %f , theta = %f, i = %i , j = %i'%(mag[i,j],theta[i,j],i,j))

ax.set_facecolor('black')
ax.axis([0, C, 0, F])
ax.set_aspect('equal')

plt.figure()
plt.subplot(1,2,1)
plt.imshow(RGB)
plt.subplot(1,2,2)
plt.imshow(gray)

plt.show()
