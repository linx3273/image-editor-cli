import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from pathlib import Path
import re

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

        return self.outp



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



    def resize(self):
        w = float(input("Enter scaling factor for width: "))
        h = float(input("Enter scaling factor for height: "))

        # self.outp = self.inp[::h,::w]
    
        if w>1 and h>1:
            # upscaling width and height
            self.outp = self.inp.repeat(h,axis=0).repeat(w,axis=1)
        elif w>1 and h<=1:
            # upscaling width, downscaling height
            self.outp = self.inp[::1,::int(w)]
            self.outp = self.outp.repeat(h,axis=0).repeat(1,axis=1)
        elif w<=1 and h>1:
            # downscaling width, upscaling height
            self.outp = self.inp[::int(h),::1]
            self.outp = self.outp.repeat(w,axis=1).repeat(1,axis=0)
        else:
            # downscaling width and height
            self.outp = self.inp[::int(1/h),::int(1/w)]


            
    def upscale(self):
        f = int(input("Enter scaling factor: "))
        self.outp = self.inp.repeat(f,axis=0).repeat(f,axis=1)


    def downscale(self):
        f = int(input("Enter downscale factor: "))
        self.outp = self.inp[::f,::f]
        




    def flip(self):
        self.outp = np.fliplr(self.inp)



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

        self.outp = ~self.outp

        # for i in range(len(self.inp)):
        #     for j in range(len(self.inp[i])):
        #         self.outp[i][j][0] = 255 - self.outp[i][j][0]
        #         self.outp[i][j][1] = 255 - self.outp[i][j][1]
        #         self.outp[i][j][2] = 255 - self.outp[i][j][2]


    def contrast(self):
        # pixvals = ((self.inp - self.inp.min)/(self.inp.max() - self.inp.min()))*255
        percentage = int(input("Enter contrast percentage: "))
        multiplier = int(percentage/100 * 255)

        minval = np.percentile(self.inp, 2)
        maxval = np.percentile(self.inp, 98)

        pixvals = np.clip(self.inp, minval, maxval)
        pixvals = ((pixvals - minval) / (maxval - minval))*multiplier

        self.outp = pixvals.astype(np.uint8)


    def rgbchannel(self):
        reg = "^r?g?b?$"
        while(True):
            print("Input should be a combination of r g and b")
            self.channel = input("Enter channel composition: ").lower()

            if re.search(reg,self.channel):
                
                self.outp = np.zeros(self.inp.shape)

                if 'r' in self.channel:
                    self.outp[:,:,0] = self.inp[:,:,0]
                if 'g' in self.channel:
                    self.outp[:,:,1] = self.inp[:,:,1]
                if 'b' in self.channel:
                    self.outp[:,:,2] = self.inp[:,:,2]

                self.outp = self.outp.astype(np.uint8)
                break

            else:
                print("Invalid input composition")

        



        