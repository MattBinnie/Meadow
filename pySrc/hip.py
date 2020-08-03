# Handmade Image Parser
import numpy as np
import sys, argparse
from PIL import Image, ImageFilter

# gray scale level values from:
# http://paulbourke.net/dataformats/asciiart/

# 9 shades of gray
gScale0 = '.:-=+*#%@'

# 70 shades of gray 
gScale1 = ".'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

# 97 shades of gray
gScale2 = ".`:,;'_^\"\\></-!~=)(|j?}{ ][ti+l7v1%yrfcJ32uIC$zwo96sngaT5qpkYVOL40&mG8*xhedbZUSAQPFDXWK#RNEHBM@"

def getAverageL(image):
    ## Given PIL Image, return average value of grayscale value

    # get image as numpy array
    im = np.array(image)

    # get shape
    width, heigth = im.shape

    # get average
    return np.average(im.reshape(width * heigth))

def convertImageToAscii(fileName, cols, imScale, asciiDetail):
    ## Given Image and dims (rows, cols) returns an m*n list of Images
  
    # open image and convert to grayscale
    image = Image.open(fileName).convert('L')

    # adding some contrast for more appealing pictures
    unsharpenFilter = ImageFilter.UnsharpMask(radius=3, percent=200, threshold=2)
    image = image.filter(unsharpenFilter)

    # store dimensions
    pxWidth, pxHeight = image.size[0], image.size[1]
    print("input image dims: %d x %d" % (pxWidth, pxHeight))

    # compute width of tile
    widthScale = pxWidth/cols

    # compute tile height based on aspect ratio and scale
    heigthScale = widthScale/imScale

    # compute number of rows
    rows = int(pxHeight/heigthScale)

    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (widthScale, heigthScale))

    # check if image size is too small 
    if cols > pxWidth or rows > pxHeight: 
        print("Image too small for specified cols!") 
        exit(0) 
  
    # ascii image is a list of character strings 
    aImg = [] 
    # generate list of dimensions 
    for i in range(rows): 
        y1 = int(i * heigthScale) 
        y2 = int((i + 1) * heigthScale) 
  
        # correct last tile 
        if i == rows - 1: 
            y2 = pxHeight 
  
        # append an empty string 
        aImg.append("") 
  
        for j in range(cols): 
  
            # crop image to tile 
            x1 = int(j * widthScale) 
            x2 = int((j + 1) * widthScale) 
  
            # correct last tile 
            if j == cols - 1: 
                x2 = pxWidth 
  
            # crop image to extract tile 
            img = image.crop((x1, y1, x2, y2)) 
  
            # get average luminance 
            avg = int(getAverageL(img)) 
  
            # look up ascii charset
            gsSet = gScale0
            # get the ascii char
            gsChar = gsSet[int((avg * (len(gsSet) - 1)) / 255)]
  
            # append ascii char to string 
            aImg[i] += gsChar
      
    # return txt image 
    return aImg 

  
# main() function 
def main(): 
    # create parser 
    descStr = "This program converts an image into ASCII art."
    parser = argparse.ArgumentParser(description=descStr) 
    # add expected arguments 
    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--scale', dest='scale', required=False) 
    parser.add_argument('--cols', dest='cols', required=False) 
    parser.add_argument('--details',dest='details', required=False) 
  
    # parse args 
    args = parser.parse_args() 
    imgFile = ""
    imgFold = ""

    if (args.imgFile is not None):
        imgFile = args.imgFile 
  
    # set scale default as 0.43 which suits 
    # a Courier font 
    scale = 0.43
    if args.scale: 
        scale = float(args.scale) 
  
    # set cols 
    cols = 80
    if args.cols: 
        cols = int(args.cols) 
  
    print('generating ASCII art...') 
    # convert image to ascii txt 
    aimg = convertImageToAscii(imgFile, cols, scale, args.details) 
  
    for row in aimg:
        print(row)

# main like a python 
if __name__ == '__main__': 
    main() 