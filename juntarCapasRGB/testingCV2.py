# Librería para mostrar gráficos o imágenes
from cv2 import cv2
# Crear arreglos de varias dimensiones para las nuevas imágenes
import numpy as np

print('\nPor favor asegúrese que las imágenes que desea procesar están en el mismo directorio que este script. \nLas imágenes deben tener la extensión .jpg y cada una de las capas debe ser diferencias con _S donde ese será la capa (R,G,B o color). \n\nPor ejemplo: \n\n\tPara la capa R: imageName_R.jpg')
img = input('\nNombre de la imágen a analizar: ')

capaR = img+'_R.jpg'
capaG = img+'_G.jpg'
capaB = img+'_B.jpg'
capaC = img+'_color.jpg'

# Es importante la ruta si se ejecuta con el atajo <F5>, ya que la terminal se ejecuta en la raíz del repo de git
# Guardar los datos de las imágenes en variables R,G,B y C para posteriormente juntarlas
R=cv2.imread(capaR)
G=cv2.imread(capaG)
B=cv2.imread(capaB)
C=cv2.imread(capaC)

# Definición del tamaño de la imágen resultante, así como de sus capas RGB (0,1,2)
filas,columnas,capas = C.shape

# Crear arreglo lleno de ceros con las dimensiones de la imágen y las tres capas RGB
I=np.zeros((filas,columnas,capas),dtype=np.uint8) # El tipo del arreglo debe ser uint8

# Regenar cada una de las capas RGB de I con los datos de las imágenes R,G y B separadas
I[:,:,0]=R[:,:,0] # Se usa la capa 0 porque la imágen es a blanco y 
I[:,:,1]=G[:,:,0] # negro y tiene la misma información en sus 3 capas
I[:,:,2]=B[:,:,0]

# Muestra la nueva imágen "I" con ayuda de pyplot
cv2.imshow('Ventana',I)
cv2.waitKey(10000)

# Mantiene la ventana visible
# plt.show()
