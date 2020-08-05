# Meadow

## Goals
- make stuff

## Languages
- python? (we never even agreed on a version so probably a virtualenv wouldn't hurt)
- C#?

## Stuff
- print images to cmd as ascii art
- color said images

## Handmade Image Parser python script (hip.py)
### Requires
- python 3.x
- pip
- PIL

### Args
Called from command line, accepts arguements
- --file MANDATORY, path to the image file to be converted
- --scale optional, how the original image should be scaled down/up before converting (default 0.43)
- --cols optional, the number of columns the converted image should have (width of the target cmd window)
- --details optional, how detailed the grayscale ascii charset should be (9, 70, 96), funny enough usually the lower char number gives a clearer picture, but it depends on the picture. Currently hardcoded to the lowest.
