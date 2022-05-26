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
theta = np.array(theta)

# plt.figure()
# plt.subplot(1,2,1)
# plt.imshow(RGB)
# plt.subplot(1,2,2)
# plt.imshow(gray)

# plt.set_cmap('gray')
# plt.show()
