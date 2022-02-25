import matplotlib.pyplot as plt

def imsplit(img):
    rgb = plt.imread(img)
    r=rgb[:,:,0]
    g=rgb[:,:,1]
    b=rgb[:,:,2]
    return r,g,b
