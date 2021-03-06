import matplotlib.pyplot as plt
import numpy as np

size = (8,8,3)
img = np.zeros(size)

img[:,:,0]=np.array([
    [163, 27, 56, 163, 102, 102, 67, 67],
    [46, 67, 27, 67, 67, 102, 56, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ]
)
img[:,:,1]=np.array([
    [205, 94, 142, 205, 187, 187, 125, 160],
    [125, 160, 94, 160, 160, 187, 142, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ]
)
img[:,:,2]=np.array([
    [157, 32, 60, 157, 102, 102, 50, 71],
    [50, 71, 32, 71, 71, 102, 60, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ]
)

img = img / 255

plt.figure(figsize=(20,20))
plt.imshow(img,vmin=0,vmax=255)
plt.show()
