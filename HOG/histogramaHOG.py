import numpy as np

def Hog_Histogramas(magnitudes,angulos,numBins=9):
    # Volvemos el tamaño de las celdas a radianes
    Cell_Size = np.pi / numBins
    min_ang = 0
    # Aquellos angulos negativos se les suma 180 para quitarles el signo 
    # angulos[angulos < 0] = angulos[angulos < 0) + pi;
    angulos[np.where(angulos<0)] = angulos[np.where(angulos<0)] + np.pi

    # Como los angulos quedan en la "mitad" de cada celda se tiene que encontrar
    # el peso en el histograma
    IzqCell_index = np.round((angulos - min_ang) / Cell_Size); #Aprox el valor 
    DerCell_index = IzqCell_index + 1

    # Normalizamos el brillo por cada pixel 
    Nom_brillo = ((IzqCell_index + 1.5) * Cell_Size) - min_ang;

    rightPortions = angulos - Nom_brillo;
    leftPortions = Cell_Size - rightPortions;
    rightPortions = rightPortions / Cell_Size;
    leftPortions = leftPortions / Cell_Size;

    # Arreglamos los valores limite del Histograma. 
    IzqCell_index[np.where(IzqCell_index==0)] = numBins
    DerCell_index[np.where(DerCell_index == (numBins + 1))] = 1

    H = np.zeros([1, numBins])

    # Para grupo de pixeles, se debe asignar una celda i hacia ambos lados. A cada uno se le ha de sumer la magnitud del gradiente 
    for i in range(numBins):
        #Celda Asignada Izquierda
        pixels = np.where(IzqCell_index == i)
        
        #Suma magnitud del gradiente Izquierda
        H[0, i] = H[0, i] + np.sum(np.transpose(leftPortions[pixels]) * magnitudes[pixels])
        
        #Celda Asignada Derecha 
        pixels = np.where(DerCell_index == i)
            
        #Suma magnitud del gradiente Derecha
        H[0, i] = H[0, i] + np.sum(np.transpose(rightPortions[pixels]) * magnitudes[pixels])
    return H
