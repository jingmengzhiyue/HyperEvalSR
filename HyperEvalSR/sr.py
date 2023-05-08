import numpy as np
from scipy import ndimage

def fspecial_gauss(size, sigma):
    x, y = np.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]
    g = np.exp(-((x**2 + y**2)/(2.0*sigma**2)))
    return g/g.sum()

def downsample(image, factor, method='uniform'):
    """Downsamples a hyperspectral image using either Gaussian or uniform subsampling."""
    if method == 'uniform':
        # Downsample image with sub-sampling
        downsampled = image[::factor, ::factor, :]
    elif method == 'gaussian':
        # Define Gaussian kernel
        kernel_size = int(2 * factor) + 1
        kernel_sigma = factor / 2
        kernel = np.zeros((kernel_size, kernel_size))
        center = kernel_size // 2
        for i in range(kernel_size):
            for j in range(kernel_size):
                kernel[i, j] = np.exp(-0.5 * ((i - center) ** 2 + (j - center) ** 2) / kernel_sigma ** 2)
        kernel = kernel / np.sum(kernel)

        # Downsample image with Gaussian blur and sub-sampling
        blurred = ndimage.convolve(image, kernel)
        downsampled = blurred[::factor, ::factor, :]
    else:
        raise ValueError('Unknown downsampling method')

    return downsampled