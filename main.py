import sys
import src.usage as usage


def main():
    if len(sys.argv)==1:
        print(usage.inf())
    else:
        if len(sys.argv)>2:
            if sys.argv[1]=="--help" or sys.argv[1]=="-h":
                pass
            elif sys.argv[1]=="edges":
                pass
            elif sys.argv[1]=="crop":
                pass
            elif sys.argv[1]=="flip":
                pass
            elif sys.argv[1]=="rotate":
                pass
            elif sys.argv[1]=="negative":
                pass
        else:
            pass

if __name__=="__main__":
    main()