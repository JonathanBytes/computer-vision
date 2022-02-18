import matplotlib.pyplot as plt
import numpy as np

size = (8,12,3)

img = np.zeros(size)

img[:,:,0]=np.array([
                     [255,255,0,0,0,0,255,255,255,255,0,0],
                     [255,255,0,0,0,0,255,255,255,255,0,0],
                     [255,255,0,0,0,0,255,255,255,255,0,0],
                     [255,255,0,0,0,0,255,255,255,255,0,0],
                     [255,255,0,0,0,0,255,255,255,255,0,0],
                     [255,255,0,0,0,0,255,255,255,255,0,0],
                     [255,250,225,200,175,150,125,100,75,50,25,0],
                     [255,250,225,200,175,150,125,100,75,50,25,0],
                     ])


img[:,:,1]=np.array([
                     [255,255,255,255,255,255,0,0,0,0,0,0],
                     [255,255,255,255,255,255,0,0,0,0,0,0],
                     [255,255,255,255,255,255,0,0,0,0,0,0],
                     [255,255,255,255,255,255,0,0,0,0,0,0],
                     [255,255,255,255,255,255,0,0,0,0,0,0],
                     [255,255,255,255,255,255,0,0,0,0,0,0],
                     [255,250,225,200,175,150,125,100,75,50,25,0],
                     [255,250,225,200,175,150,125,100,75,50,25,0],
                     ])

img[:,:,2]=np.array([
                     [0,0,255,255,0,0,255,255,0,0,255,255],
                     [0,0,255,255,0,0,255,255,0,0,255,255],
                     [0,0,255,255,0,0,255,255,0,0,255,255],
                     [0,0,255,255,0,0,255,255,0,0,255,255],
                     [0,0,255,255,0,0,255,255,0,0,255,255],
                     [0,0,255,255,0,0,255,255,0,0,255,255],
                     [255,250,225,200,175,150,125,100,75,50,25,0],
                     [255,250,225,200,175,150,125,100,75,50,25,0],
                     ])
img=img.astype('int')
plt.figure(figsize=(20,20))
plt.imshow(img,vmin=0,vmax=255)

