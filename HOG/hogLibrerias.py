import matplotlib.pyplot as plt
from ipFunctions import *
from skimage.transform import resize
from skimage.feature import hog

img = getuserimg(cartagena=True)
img = imundersize(img,6)
F, C, layers = img.shape
img = resize(img,(F,C))

plt.figure()
plt.subplot(1,2,1)
plt.set_cmap('gray')
plt.imshow(img)

fd, hog_image = hog(img, orientations=9, pixels_per_cell=(8, 8),
                	cells_per_block=(2, 2), visualize=True, multichannel=True)
plt.subplot(1,2,2)
plt.axis("off")
plt.imshow(hog_image, cmap="gray")

plt.show()
