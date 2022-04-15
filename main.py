import sys
import src.usage as usage
from src.imageEdit import imageEdit


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
                        obj = imageEdit(sys.argv[2],sys.argv[3])
                        obj.loadImg()
                        obj.edgeDetection()
                        obj.writeImg('edge')

                    elif sys.argv[1]=="grayscale":
                        obj = imageEdit(sys.argv[2],sys.argv[3])
                        obj.loadImg()
                        obj.grayscale()
                        obj.writeImg('grayscale')

                    elif sys.argv[1]=="crop":
                        obj = imageEdit(sys.argv[2],sys.argv[3])
                    elif sys.argv[1]=="flip":
                        pass
                    elif sys.argv[1]=="rotate":
                        pass
                    elif sys.argv[1]=="invert-color":
                        obj = imageEdit(sys.argv[2],sys.argv[3])
                        obj.loadImg()
                        obj.invertColor()
                        obj.writeImg('negative')
                    else:
                        print("Invalid arguments. Run 'python main.py --help'")


if __name__=="__main__":
    main()