#!/usr/bin/env python3
# Reading an animated GIF file using Python Image Processing Library - Pillow

from PIL import Image

from PIL import GifImagePlugin

import sys

#argv[1] = "filename of gif in folder"
 

imageObject = Image.open(sys.argv[1])

print(imageObject.is_animated)

print(imageObject.n_frames)

 

# Display individual frames from the loaded animated GIF file

for frame in range(0,imageObject.n_frames):

    imageObject.seek(frame)

    imageObject.show() 