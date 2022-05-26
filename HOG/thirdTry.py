import matplotlib.pyplot as plt
import numpy as np
from ipFunctions import *
from histogramaHOG import *

# file_path = getuserpath()
# file_path = '/home/jonathan/Documents/Universidad/2022-1/computer-vision/HOG/abu.jpeg'

# print('Se usará la imagen:',file_path)

# RGB = plt.imread(file_path)
# gray = rgb2gray(RGB)
# RGB = resize(RGB, (F, C))
# img = resize(gray, (F, C))

from skimage import data, color

original_image = data.astronaut()
img = rgb2gray(original_image)
F,C,capas= original_image.shape
img = resize(img, (F, C))

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

gy_check, gx_check = np.gradient(img) # Note that the result of np.gradient is in the reversed order

print('diff_gx:', np.linalg.norm(gx - gx_check))
print('diff_gy', np.linalg.norm(gy - gy_check))


mag = np.sqrt(gx**2 + gy**2)
print('mag min %f'%(np.min(mag)))
mag = mag / np.max(mag)
theta = np.rad2deg(np.arctan2(gy, gx)) % 180
print('min theta = %f'%(np.min(theta)))

def compute_hog_cell(n_orientations: int, magnitudes: np.ndarray, orientations: np.ndarray) -> np.ndarray:
    """
    Compute 1 HOG feature of a cell. Return a row vector of size `n_orientations`
    """
    bin_width = int(180 / n_orientations)
    hog = np.zeros(n_orientations)
    for i in range(orientations.shape[0]):
        for j in range(orientations.shape[1]):
            orientation = orientations[i, j]
            lower_bin_idx = int(orientation / bin_width)
            hog[lower_bin_idx] += magnitudes[i, j]

    return hog / (magnitudes.shape[0] * magnitudes.shape[1])

def normalize_vector(v, eps=1e-5):
    """
    Return a normalized vector (which has norm2 as 1) 
    """
    # eps is used to prevent zero divide exceptions (in case v is zero)
    return v / np.sqrt(np.sum(v ** 2) + eps ** 2) 


def compute_hog_features(image: np.ndarray,
                         n_orientations: int = 9, pixels_per_cell: (int, int) = (8, 8),
                         cells_per_block: (int, int) = (1, 1)) -> np.ndarray:
    """
    Compute HOG features of an image. Return a row vector
    """
    gx, gy = compute_gradient(image)
    sy, sx = gx.shape
    cx, cy = pixels_per_cell
    bx, by = cells_per_block

    magnitudes = np.hypot(gx, gy)   # = np.sqrt(gx**2 + gy**2)
    orientations = np.rad2deg(np.arctan2(gy, gx)) % 180

    n_cellsx = int(sx / cx) # Number of cells in x axis
    n_cellsy = int(sy / cy) # Number of cells in y axis
    n_blocksx = int(n_cellsx - bx) + 1
    n_blocksy = int(n_cellsy - by) + 1

    hog_cells = np.zeros((n_cellsx, n_cellsy, n_orientations))

    prev_x = 0
    # Compute HOG of each cell
    for it_x in range(n_cellsx):
        prev_y = 0
        for it_y in range(n_cellsy):
            magnitudes_patch = magnitudes[prev_y:prev_y + cy, prev_x:prev_x + cx]
            orientations_patch = orientations[prev_y:prev_y + cy, prev_x:prev_x + cx]

            hog_cells[it_y, it_x] = compute_hog_cell(n_orientations, magnitudes_patch, orientations_patch)

            prev_y += cy
        prev_x += cx

    hog_blocks_normalized = np.zeros((n_blocksx, n_blocksy, n_orientations))

    # Normalize HOG by block
    for it_blocksx in range(n_blocksx):
        for it_blocky in range(n_blocksy):
            hog_block = hog_cells[it_blocky:it_blocky + by, it_blocksx:it_blocksx + bx].ravel()
            hog_blocks_normalized[it_blocky, it_blocksx] = normalize_vector(hog_block)

    return hog_blocks_normalized.ravel()

# Compare the results with skimage.feature.hog
hog_features = compute_hog_features(
    img, n_orientations=9,
    pixels_per_cell=(8, 8),
    cells_per_block=(1, 1))

from skimage.feature import hog

hog_features_check = hog(
    img, orientations=9,
    pixels_per_cell=(8, 8), cells_per_block=(1, 1),
    block_norm='L2')

assert hog_features.shape == hog_features_check.shape
print(np.allclose(hog_features, hog_features_check))
print(hog_features.shape)

import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import hog

_, hog_image = hog(
    img, orientations=9, pixels_per_cell=(8, 8),
    cells_per_block=(1, 1), block_norm='L2',
    visualize=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

ax1.axis('off'); ax2.axis('off')
ax1.imshow(img, cmap=plt.get_cmap('gray'))
ax1.set_title('Input image')

ax2.imshow(hog_image, cmap=plt.get_cmap('gray'))
ax2.set_title('HOG')
plt.show()

# fig, ax = plt.subplots()
# stepF = F // 50
# stepC = C // 50
# for i in range(0,F,stepF):
#     for j in range(0,C,stepC):
#         x = np.cos(np.radians(theta[i,j]))
#         y = np.sin(np.radians(theta[i,j]))
#         ax.arrow(j, abs(i-F), x, y, color=(mag[i,j],mag[i,j],mag[i,j]),width=stepF/16,head_width=stepF/8)
#         # ax.quiver(j, abs(i-F), x, y, scale=None, color=(mag[i,j],mag[i,j],mag[i,j]),headaxislength=2,headlength=2)
#         ax.set_title('Quiver plot with one arrow')
#     if i%5==0:
#         print('mag = %f , theta = %f, i = %i , j = %i'%(mag[i,j],theta[i,j],i,j))

# ax.set_facecolor('black')
# ax.axis([0, C, 0, F])
# ax.set_aspect('equal')

# plt.show()
