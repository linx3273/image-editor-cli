import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from pathlib import Path



class imageEdit:
    def __init__(self,src,dest):
        self.src = Path(src).resolve()
        self.dest = Path(dest).resolve()
        self.inp = None
        self.outp = None



    def loadImg(self):
        self.inp = mpimg.imread(self.src)



    def writeImg(self,format):
        self.dest = Path(str(self.dest) + '/' + str(self.src.stem) + '_' + f'{format}' + str(self.src.suffix)).resolve()
        mpimg.imsave(self.dest,self.outp)



    def showOutput(self):
        plt.imshow(self.outp)
        plt.show()



    def edgeDetection(self):
        self.grayscale = self.grayscale()
    
        vertical_sobel_filter=[[-1,-2,-1],[0,0,0],[1,2,1]]
        hortizontal_sobel_filter=[[-1,0,1],[-2,0,2],[-1,0,1]]
        n,m,d = self.inp.shape
        
        edges_img=np.zeros_like(self.grayscale)
        for row in range(3, n-2):
            for col in range(3,m-2):
                local_pixels=self.grayscale[row-1:row+2, col-1:col+2,0]

                vertica_transformed_pixels=vertical_sobel_filter*local_pixels
                vertical_score=vertica_transformed_pixels.sum()/4

                horizonta_transformed_pxels=hortizontal_sobel_filter*local_pixels
                hortizontal_score=horizonta_transformed_pxels.sum()/4

                edge_score=(vertical_score**2+hortizontal_score**2)**.5
                edges_img[row, col]=[edge_score]*3
        edges_img=edges_img/edges_img.max()

        self.outp = edges_img



    def grayscale(self):
        self.outp = np.zeros(self.inp.shape)
        R = np.array(self.inp[:, :, 0])
        G = np.array(self.inp[:, :, 1])
        B = np.array(self.inp[:, :, 2])

        R = (R *.299)
        G = (G *.587)
        B = (B *.114)

        Avg = (R+G+B)
        self.outp = self.inp.copy()

        for i in range(3):
           self.outp[:,:,i] = Avg

        return self.outp



    def crop(self):
        pass



    def flip(self):
        pass



    def rotate(self):
        pass



    def invertColor(self):
        self.outp = self.inp.copy()

        for i in range(len(self.inp)):
            for j in range(len(self.inp[i])):
                for k in range(len(self.inp[i][j])):
                    self.outp[i][j][k] = 255 - self.outp[i][j][k]


        