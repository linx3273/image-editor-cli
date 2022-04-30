import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from pathlib import Path
import re

class imageEdit:
    def __init__(self,src,dest):
        self.__src = Path(src).resolve()
        self.__dest = Path(dest).resolve()
        self.__inp = None
        self.__outp = None


    def loadImg(self):
        self.__inp = mpimg.imread(self.__src)


    def writeImg(self,format):
        self.__dest = Path(str(self.__dest) + '/' + str(self.__src.stem) + '_' + f'{format}' + str(self.__src.suffix)).resolve()
        mpimg.imsave(self.__dest,self.__outp)


    def showOutput(self):
        plt.imshow(self.__outp)
        plt.show()


    def edgeDetection(self):
        gray = self.grayscale()
    
        vertical_sobel_filter = [[-1,-2,-1],[0,0,0],[1,2,1]]
        hortizontal_sobel_filter = [[-1,0,1],[-2,0,2],[-1,0,1]]
        n,m,d = self.__inp.shape
        
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

        self.__outp = edges_img

        return self.__outp


    def grayscale(self):
        self.__outp = np.zeros(self.__inp.shape)
        R = np.array(self.__inp[:, :, 0])
        G = np.array(self.__inp[:, :, 1])
        B = np.array(self.__inp[:, :, 2])

        R = (R *.299)
        G = (G *.587)
        B = (B *.114)

        Avg = (R+G+B)
        self.__outp = self.__inp.copy()

        for i in range(3):
           self.__outp[:,:,i] = Avg

        return self.__outp


    # def resize(self):
    #     w = float(input("Enter scaling factor for width: "))
    #     h = float(input("Enter scaling factor for height: "))

    #     # self.__outp = self.__inp[::h,::w]
    
    #     if w>1 and h>1:
    #         # upscaling width and height
    #         self.__outp = self.__inp.repeat(h,axis=0).repeat(w,axis=1)
    #     elif w>1 and h<=1:
    #         # upscaling width, downscaling height
    #         self.__outp = self.__inp[::1,::int(w)]
    #         self.__outp = self.__outp.repeat(h,axis=0).repeat(1,axis=1)
    #     elif w<=1 and h>1:
    #         # downscaling width, upscaling height
    #         self.__outp = self.__inp[::int(h),::1]
    #         self.__outp = self.__outp.repeat(w,axis=1).repeat(1,axis=0)
    #     else:
    #         # downscaling width and height
    #         self.__outp = self.__inp[::int(1/h),::int(1/w)]

    #     return self.__outp

            
    def upscale(self):
        self.factor = int(input("Enter scaling factor: "))
        self.__outp = self.__inp.repeat(self.factor,axis=0).repeat(self.factor,axis=1)

        return self.__outp


    def downscale(self):
        self.factor = int(input("Enter downscale factor: "))
        self.__outp = self.__inp[::self.factor,::self.factor]

        return self.__outp
        

    def flip(self):
        self.__outp = np.fliplr(self.__inp)

        self.__outp


    def rotate(self):
        self.ang = int(input("Enter angle in degrees: "))
        SIN = np.sin(self.ang*np.pi/180)  # obtaining sin value
        COS = np.cos(self.ang*np.pi/180)  # obtaining cos value

        # defining height and width of the image
        height,width= self.__inp.shape[0],self.__inp.shape[1]

        # defining the height and width of the image post rotation
        new_height = round(abs(self.__inp.shape[0]*COS)+abs(self.__inp.shape[1]*SIN))+1
        new_width = round(abs(self.__inp.shape[1]*COS)+abs(self.__inp.shape[0]*SIN))+1

        # creating template in output with new dimensions
        self.__outp = np.zeros((new_height,new_width,self.__inp.shape[2]))

        # finding centre about which image must be rotated
        # calculated wrt original image
        og_centre_height = round(((self.__inp.shape[0]+1)/2)-1)
        og_centre_width = round(((self.__inp.shape[1]+1)/2)-1)

        
        # finding centre of the new image that will be obtained
        # calcualted wrt new dimensions
        new_centre_height = round(((new_height+1)/2)-1)
        new_centre_width = round(((new_width+1)/2)-1)

        for i in range(height):
            for j in range(width):
                # coords of pixel wrt the centre of original shape
                y = self.__inp.shape[0]-1-i-og_centre_height
                x = self.__inp.shape[1]-1-j-og_centre_width

                # coords of pixel wrt to the rotated matrix
                new_y = round(-x*SIN+y*COS)
                new_x = round(x*COS+y*SIN)

                # since image will be rotated the centre will change too
                # to adjust that we need to chage new_x and new_y to the new centre
                new_y = new_centre_height - new_y
                new_x = new_centre_width - new_x

                # adding if check to prevent any errors while procesing
                if 0<=new_x < new_width and 0<=new_y<new_height and new_x>=0 and new_y>=0:
                    self.__outp[new_y,new_x,:] = self.__inp[i,j,:]      # copying pixel value to given index             

        # not sure why this line is required but without this I was getting value errors
        # stating that the RGB values are floating point/ int32 etc and that they 
        # are supposed to be of type uint8
        self.__outp = self.__outp.astype(np.uint8)

        return self.__outp


    def invertColor(self):
        self.__outp = self.__inp.copy()

        self.__outp = ~self.__outp

        # for i in range(len(self.__inp)):
        #     for j in range(len(self.__inp[i])):
        #         self.__outp[i][j][0] = 255 - self.__outp[i][j][0]
        #         self.__outp[i][j][1] = 255 - self.__outp[i][j][1]
        #         self.__outp[i][j][2] = 255 - self.__outp[i][j][2]


    def contrast(self):
        # pixvals = ((self.__inp - self.__inp.min)/(self.__inp.max() - self.__inp.min()))*255
        percentage = int(input("Enter contrast percentage: "))
        self.multiplier = int(percentage/100 * 255)

        minval = np.percentile(self.__inp, 2)
        maxval = np.percentile(self.__inp, 98)

        pixvals = np.clip(self.__inp, minval, maxval)
        pixvals = ((pixvals - minval) / (maxval - minval))*self.multiplier

        self.__outp = pixvals.astype(np.uint8)

        return self.__outp


    def rgbchannel(self):
        reg = "^r?g?b?|r?b?g|g?r?b?|g?b?r?|b?r?g?|b?g?r?$"

        print("Input should be a combination of r g and b")
        self.channel = input("Enter channel composition: ").lower()

        if re.search(reg,self.channel):
            
            self.__outp = np.zeros(self.__inp.shape)

            if 'r' in self.channel:
                self.__outp[:,:,0] = self.__inp[:,:,0]
            if 'g' in self.channel:
                self.__outp[:,:,1] = self.__inp[:,:,1]
            if 'b' in self.channel:
                self.__outp[:,:,2] = self.__inp[:,:,2]

            self.__outp = self.__outp.astype(np.uint8)


        else:
            print("Invalid input composition")

        return self.__outp


    def transparency(self):
        self.__outp = np.zeros((self.__inp.shape[0],self.__inp.shape[1],4)).astype(np.uint8)

        self.percentage = float(input("Enter transparency percentage: "))
        self.multiplier = int((100-self.percentage)/100 * 255)

        self.__outp[:,:,0:3] = self.__inp[:,:,0:3]
        self.__outp[:,:,3] = self.multiplier

        return self.__outp


        
        



        