import sys
import src.usage as usage
from src.imageEdit import imageEdit
import os


def main():
    if len(sys.argv)==1:
        print(usage.inf())
    else:
        if len(sys.argv)>1:
            if sys.argv[1]=="--help" or sys.argv[1]=="-h":
                print(usage.inf())
            else:
                if len(sys.argv)!=4:
                    print("Missing Arguments. Run 'python main.py --help'")
                else:
                    if sys.argv[1]=="detect-edges":
                        print("Detecting edges on image")
                        obj = imageEdit(sys.argv[2],sys.argv[3])
                        obj.loadImg()
                        obj.edgeDetection()
                        print("Saving image")
                        obj.writeImg('edge')
                        print("Done")
                        os.system(f"start {sys.argv[3]}")

                    elif sys.argv[1]=="grayscale":
                        print("Converting image to grayscale")
                        obj = imageEdit(sys.argv[2],sys.argv[3])
                        obj.loadImg()
                        obj.grayscale()
                        print("Saving image")
                        obj.writeImg('grayscale')
                        print("Done")
                        os.system(f"start {sys.argv[3]}")
                        

                    elif sys.argv[1]=="upscale":
                        obj = imageEdit(sys.argv[2],sys.argv[3])
                        obj.loadImg()
                        obj.upscale()
                        print("Saving image")
                        obj.writeImg('upscaled')
                        print("Done")
                        os.system(f"start {sys.argv[3]}")

                    elif sys.argv[1]=="downscale":
                        obj = imageEdit(sys.argv[2],sys.argv[3])
                        obj.loadImg()
                        obj.downscale()
                        print("Saving image")
                        obj.writeImg('downscaled')
                        print("Done")
                        os.system(f"start {sys.argv[3]}")


                    elif sys.argv[1]=="flip":
                        print("Flipping image")
                        obj = imageEdit(sys.argv[2],sys.argv[3])
                        obj.loadImg()
                        obj.flip()
                        print("Saving image")
                        obj.writeImg('flipped')
                        print("Done")
                        os.system(f"start {sys.argv[3]}")

                    elif sys.argv[1]=="rotate":
                        obj = imageEdit(sys.argv[2],sys.argv[3])
                        obj.loadImg()
                        obj.rotate()
                        print("Saving image")
                        obj.writeImg('rotated')
                        print("Done")
                        os.system(f"start {sys.argv[3]}")
                        
                    elif sys.argv[1]=="invert-color":
                        print("Inverting color of image")
                        obj = imageEdit(sys.argv[2],sys.argv[3])
                        obj.loadImg()
                        obj.invertColor()
                        print("Saving image")
                        obj.writeImg('negative')
                        print("Done")
                        os.system(f"start {sys.argv[3]}")


                    else:
                        print("Invalid arguments. Run 'python main.py --help'")


if __name__=="__main__":
    main()