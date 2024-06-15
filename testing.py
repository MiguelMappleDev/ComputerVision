# python 3.11.1.64 bits

import subprocess
import importlib.util

import cv2
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline #only for jupyter
from IPython.display import Image
from PIL import Image
libraries = ["cv2", "numpy", "matplotlib.pyplot", "IPython", "PIL"]
from validatelibraries import validatelibraries

def main():
 
    validatelibraries(libraries)

    # Open an image file
    img = Image.open('src\checkerboard_18x18.png')
    img2 = Image.open('src\checkerboard_84x84.jpg')
    # Display image
    img.show()
    img2.show()
    # Close image (optional)
    img.close()
    img2.close()


if __name__ == "__main__":
    main()