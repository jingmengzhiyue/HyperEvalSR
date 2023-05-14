import os
import scipy.io as scio
import tifffile as tiff

def load(file_path):
    root, extension = os.path.splitext(file_path)
    if extension == "tif":
        