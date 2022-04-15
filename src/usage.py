def inf():
    return '''Usage:
    python main.py <Option> src dest
    
Option:
    --help      -h      Loads this message
    detect-edges        Perform edge detection on given image
    grayscale           Convert image to grayscale
    crop                To crop the image based on provided coordinates
    flip                Flips the image
    rotate              Rotate image by given angle
    invert-color            Invert colors of the image


src - source of image
dest - destination location to save image
'''