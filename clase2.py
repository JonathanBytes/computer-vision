import matplotlib.pyplot as plt
import numpy as np

size = (3,3,3)

img = np.zeros(size)

img[:,:,0]=np.array([[255,0,0],[0,128,255],[0,255,255]])
img[:,:,1]=np.array([[0,0,255],[255,128,0],[0,255,255]])
img[:,:,2]=np.array([[0,0,255],[0,128,255],[255,255,0]])

img = img/255
plt.figure(figsize=(20,20))
plt.imshow(img,vmin=0,vmax=255)
plt.show()
