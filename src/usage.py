def inf():
    return '''Usage:
    python main.py <Option> src dest
    
Option:
    --help      -h      Loads this message
    detect-edges        Perform edge detection on given image
    grayscale           Convert image to grayscale
    upscale             Upscale image
    downscale           Downscale image
    flip                Flips the image
    rotate              Rotate image by given angle
    invert-color        Invert colors of the image
    contrast            To adjust contrast of image
    rgb-channels        To obtain image containg only r,g or b or a mixture of those


src - source of image
dest - destination location to save image
'''