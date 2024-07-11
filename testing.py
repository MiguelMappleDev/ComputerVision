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
import sys

def main():
 
    # validatelibraries(libraries)

    # # Open an image file
    # img = Image.open('src\checkerboard_18x18.png')
    # img2 = Image.open('src\checkerboard_84x84.jpg ')
    # # Display image
    # img.show()
    # img2.show()
    # # Close image (optional)
    # img.close()
    # img2.close()

    s = 0
    if len(sys.argv) > 1:
        s = sys.argv[1]

    source = cv2.VideoCapture(s)

    win_name = 'Camera Preview'
    cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

    while cv2.waitKey(1) != 27: # Escape
        has_frame, frame = source.read()
        if not has_frame:
            break
        cv2.imshow(win_name, frame)

    source.release()
    cv2.destroyWindow(win_name)


if __name__ == "__main__":
    main()