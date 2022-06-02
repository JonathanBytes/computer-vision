import matplotlib.pyplot as plt
import numpy as np
from ipFunctions import *
from histogramaHOG import *

img = getuserimg(cartagena=True)
img = imundersize(img,6)
img = rgb2gray(img)
F, C = img.shape
img = resize(img, (F, C))

gx, gy = calcularGradientes(img)

gy_check, gx_check = np.gradient(img) # Note that the result of np.gradient is in the reversed order

print('diff_gx:', np.linalg.norm(gx - gx_check))
print('diff_gy', np.linalg.norm(gy - gy_check))

mag = np.sqrt(gx**2 + gy**2)
print('mag max %f'%(np.max(mag)))
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
    gx, gy = calcularGradientes(image)
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
