import matplotlib.pyplot as plt

def plot4x4(im1,im2,im3):
    plt.subplot(2,2,1)
    plt.imshow(im1)
    plt.subplot(2,2,2)
    plt.imshow(im2)
    plt.subplot(2,2,3)
    plt.imshow(im3)
