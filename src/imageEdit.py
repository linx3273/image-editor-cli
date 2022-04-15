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
        gray = self.grayscale()
    
        vertical_sobel_filter = [[-1,-2,-1],[0,0,0],[1,2,1]]
        hortizontal_sobel_filter = [[-1,0,1],[-2,0,2],[-1,0,1]]
        n,m,d = self.inp.shape
        
        edges_img=np.zeros_like(gray)
        for row in range(3, n-2):
            for col in range(3,m-2):
                local_pixels = gray[row-1:row+2, col-1:col+2,0]

                vertica_transformed_pixels=vertical_sobel_filter*local_pixels
                vertical_score = vertica_transformed_pixels.sum()/4

                horizonta_transformed_pxels = hortizontal_sobel_filter*local_pixels
                hortizontal_score = horizonta_transformed_pxels.sum()/4

                edge_score = (vertical_score**2+hortizontal_score**2)**.5
                edges_img[row, col] = [edge_score]*3
                
        edges_img = edges_img/edges_img.max()

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
        ang = int(input("Enter angle in degrees: "))
        SIN = np.sin(ang*np.pi/180)  # obtaining sin value
        COS = np.cos(ang*np.pi/180)  # obtaining cos value

        # defining height and width of the image
        height,width= self.inp.shape[0],self.inp.shape[1]

        # defining the height and width of the image post rotation
        new_height = round(abs(self.inp.shape[0]*COS)+abs(self.inp.shape[1]*SIN))+1
        new_width = round(abs(self.inp.shape[1]*COS)+abs(self.inp.shape[0]*SIN))+1

        # creating template in output with new dimensions
        self.outp = np.zeros((new_height,new_width,self.inp.shape[2]))

        # finding centre about which image must be rotated
        # calculated wrt original image
        og_centre_height = round(((self.inp.shape[0]+1)/2)-1)
        og_centre_width = round(((self.inp.shape[1]+1)/2)-1)

        
        # finding centre of the new image that will be obtained
        # calcualted wrt new dimensions
        new_centre_height = round(((new_height+1)/2)-1)
        new_centre_width = round(((new_width+1)/2)-1)


        for i in range(height):
            for j in range(width):
                # coords of pixel wrt the centre of original shape
                y = self.inp.shape[0]-1-i-og_centre_height
                x = self.inp.shape[1]-1-j-og_centre_width

                # coords of pixel wrt to the rotated matrix
                new_y = round(-x*SIN+y*COS)
                new_x = round(x*COS+y*SIN)

                # since image will be rotated the centre will change too
                # to adjust that we need to chage new_x and new_y to the new centre
                new_y = new_centre_height - new_y
                new_x = new_centre_width - new_x

                # adding if check to prevent any errors while procesing
                if 0<=new_x < new_width and 0<=new_y<new_height and new_x>=0 and new_y>=0:
                    self.outp[new_y,new_x,:] = self.inp[i,j,:]      # copying pixel value to given index             

        # not sure why this line is required but without this I was getting value errors
        # stating that the RGB values are floating point/ int32 etc and that they 
        # are supposed to be of type uint8
        self.outp = self.outp.astype(np.uint8)




    def invertColor(self):
        self.outp = self.inp.copy()

        for i in range(len(self.inp)):
            for j in range(len(self.inp[i])):
                for k in range(len(self.inp[i][j])):
                    self.outp[i][j][k] = 255 - self.outp[i][j][k]


        