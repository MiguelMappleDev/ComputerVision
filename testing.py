# python 3.11.1.64 bits

import subprocess
import importlib.util

import cv2
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from IPython.display import Image
libraries = ["cv2", "numpy", "matplotlib.pyplot", "IPython"]

from validatelibraries import validatelibraries

def main():
 
    validatelibraries(libraries)



if __name__ == "__main__":
    main()