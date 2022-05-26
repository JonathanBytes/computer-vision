import matplotlib.pyplot as plt
import numpy as np
from ipFunctions import *

file_path = getuserpath()

print('Se usará la imagen:',file_path)

# RGB = plt.imread(file_path)
# RGB = imundersize(RGB,8)
# img = gray = rgb2gray(RGB)
# img = np.array(img)

RGB = plt.imread(file_path)
gray = rgb2gray(RGB)
RGB = resize(RGB, (128, 128))
img = resize(gray, (128, 128))

F,C,capas= RGB.shape

def compute_gradient(image: np.ndarray):
    """
    Compute gradient of an image by rows and columns
    """
    gx = np.zeros_like(image)
    gy = np.zeros_like(image)
    # Central difference
    gx[:, 1:-1] = (image[:, 2:] - image[:, :-2]) / 2
    gy[1:-1, :] = (image[2:, :] - image[:-2, :]) / 2

    # Forward difference
    gx[:, 0] = image[:, 1] - image[:, 0]
    gy[0, :] = image[1, :] - image[0, :]

    # Backward difference
    gx[:, -1] = image[:, -1] - image[:, -2]
    gy[-1, :] = image[-1, :] - image[-2, :]

    return gx, gy

gx, gy = compute_gradient(img)

mag = np.sqrt(gx**2 + gy**2)
mag = mag / np.max(mag)
theta = np.rad2deg(np.arctan2(gy, gx)) % 180

fig, ax = plt.subplots()
step = 2
for i in range(0,F,step):
    for j in range(0,C,step):
        x = mag[i,j] * np.cos(np.radians(theta[i,j]))
        y = mag[i,j] * np.sin(np.radians(theta[i,j]))
        ax.quiver(j, abs(i-F), x, y, scale=None, color=(mag[i,j],mag[i,j],mag[i,j]),headaxislength=2,headlength=2)
        ax.set_title('Quiver plot with one arrow')
    if i%5==0:
        print('mag = %f , theta = %f, i = %i , j = %i'%(mag[i,j],theta[i,j],i,j))

ax.set_facecolor('black')
ax.axis([0, C, 0, F])
ax.set_aspect('equal')

plt.show()
