import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb_to_gray(img):
        grayImage = np.zeros(img.shape)
        R = np.array(img[:, :, 0])
        G = np.array(img[:, :, 1])
        B = np.array(img[:, :, 2])

        R = (R *.299)
        G = (G *.587)
        B = (B *.114)

        Avg = (R+G+B)
        grayImage = img.copy()

        for i in range(3):
           grayImage[:,:,i] = Avg
           
        return grayImage       

image = mpimg.imread("martian_surface.jpg")   
grayImage = rgb_to_gray(image)  

# print(grayImage)
vertical_sobel_filter=[[-1,-2,-1],[0,0,0],[1,2,1]]
hortizontal_sobel_filter=[[-1,0,1],[-2,0,2],[-1,0,1]]
n,m,d=image.shape

edges_img=np.zeros_like(grayImage)
for row in range(3, n-2):
    for col in range(3,m-2):
        local_pixels=grayImage[row-1:row+2, col-1:col+2,0]

        vertica_transformed_pixels=vertical_sobel_filter*local_pixels
        vertical_score=vertica_transformed_pixels.sum()/4

        horizonta_transformed_pxels=hortizontal_sobel_filter*local_pixels
        hortizontal_score=horizonta_transformed_pxels.sum()/4

        edge_score=(vertical_score**2+hortizontal_score**2)**.5
        edges_img[row, col]=[edge_score]*3
edges_img=edges_img/edges_img.max()

plt.imshow(edges_img)
plt.show()