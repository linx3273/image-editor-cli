import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def negate(image):
    neg=np.zeros(image.shape)
    neg=image.copy()
    for i in range(len(image)):
        for j in range(len(image[i])):
            for k in range(len(image[i][j])):
                neg[i][j][k]=255-neg[i][j][k]

    return neg
image = mpimg.imread("martian_surface.jfif")
# print(image)
# print("negated")
negativeImage=negate(image)
# print(negativeImage)
plt.imshow(negativeImage)
plt.show()