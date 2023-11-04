import os
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

for im in os.listdir("images"):
    image = mpimg.imread("images/" + im)
    plt.imshow(image)
    plt.show()
    break
