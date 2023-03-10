from ascii_magic import AsciiArt, from_image
import sys, argparse
from PIL import ImageEnhance

descStr = "This program converts an image into ASCII art."
parser = argparse.ArgumentParser(description=descStr) 
parser.add_argument('--file',    dest = 'imgFile', required=False)
parser.add_argument('--str',     dest = 'imgSrc' , required=False)

# parse args 
args = parser.parse_args() 
imgFile = ""
ImgSrc = ""

if (args.imgFile is not None):
    imgFile = args.imgFile 
elif (args.imgSrc is not None):
    imgFile = AsciiArt.from_craiyon(args.imgSrc)
    
if (imgFile != ""):
    img = from_image(imgFile)
    img.to_terminal()
    img.image = ImageEnhance.Brightness(img.image).enhance(0.2)
    img.to_terminal()