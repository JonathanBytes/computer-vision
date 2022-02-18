import cv2
import numpy as np

img=cv2.imread('astronaut.jpg')
imgred=np.copy(img)
imgred[:,:,1]=0
imgred[:,:,2]=0

cv2.imshow('Blue image',imgred)

cv2.waitKey(0)
