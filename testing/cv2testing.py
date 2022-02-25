from cv2 import cv2

C=cv2.imread('frame_color.jpg')

print(C)

filas,columnas,capas = C.shape
