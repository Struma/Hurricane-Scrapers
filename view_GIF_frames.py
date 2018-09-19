#!/usr/bin/env python3

# Reading an animated GIF file using Python Image Processing Library - Pillow
# I got this code from the internet, I think from stack exchange.

from PIL import Image
from PIL import GifImagePlugin
import sys
 

imageObject = Image.open(sys.argv[1])
print(imageObject.is_animated)
print(imageObject.n_frames)

for frame in range(0,imageObject.n_frames):
    imageObject.seek(frame)
    imageObject.show() 
