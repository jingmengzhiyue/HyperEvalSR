import numpy as np


def RMSE(ref_img, rec_img):
    diff = ref_img - rec_img
    squared_diff = np.square(diff)
    mse = np.mean(squared_diff)
    Recult_rmse = np.sqrt(mse)
    return Recult_rmse

def CC(ref_img, rec_img, mask=None):
    _, _, bands = rec_img.shape

    out = np.zeros(bands)
    for i in range(bands):
        tar_tmp = rec_img[:, :, i]
        ref_tmp = ref_img[:, :, i]

        if mask is not None:
            mask_ = np.nonzero(mask)
            tar_tmp = tar_tmp[mask_]
            ref_tmp = ref_tmp[mask_]

        cc = np.corrcoef(tar_tmp.flatten(), ref_tmp.flatten())
        out[i] = cc[0, 1]

    Recult_CC = np.mean(out)
    return Recult_CC

def DD(ref_img, rec_img):

    Recult_DD = np.linalg.norm(ref_img.ravel() - rec_img.ravel(), ord=1) / ref_img.size

    # rows, cols, bands = RC.shape
    # Recult_DD = 1 / (bands * rows * cols) * np.linalg.norm(RC.reshape(-1, 1) - GT.reshape(-1, 1), ord=1)
    return Recult_DD



def ERGAS(ref_img, rec_img, downsampling_scale):
    m, n, k = ref_img.shape
    mm, nn, kk = rec_img.shape
    m = min(m, mm)
    n = min(n, nn)
    k = min(k, kk)
    imagery1 = ref_img[0:m, 0:n, 0:k]
    imagery2 = rec_img[0:m, 0:n, 0:k]

    ergas = 0
    for i in range(k):
        mse = np.mean((imagery1[:, :, i] - imagery2[:, :, i])**2)
        rmse = np.sqrt(mse)
        ergas += (rmse / np.mean(imagery1[:, :, i]))**2

    Result_ERGAS = 100 * np.sqrt(ergas / k) / downsampling_scale
    return Result_ERGAS



def PSNR(ref_img, rec_img):
    mse = np.mean((ref_img - rec_img) ** 2)
    max_val = np.max(ref_img)
    psnr = 20 * np.log10(max_val / np.sqrt(mse))
    return psnr

def RSNR(ref_img, rec_img, mask=None):
    tar = ref_img
    ref = rec_img
    _, _, bands = ref.shape

    if mask is None:
        ref = np.reshape(ref, (-1, bands))
        tar = np.reshape(tar, (-1, bands))

        msr = np.linalg.norm(ref - tar, 'fro') ** 2  # RSNR
        max2 = np.linalg.norm(ref, 'fro') ** 2  # RSNR
        rsnrall = 10 * np.log10(max2 / msr)  # RSNR

        out = {}
        out['all'] = rsnrall
        Result_RSNR = out['all']

    else:
        ref = np.reshape(ref, (-1, bands))
        tar = np.reshape(tar, (-1, bands))
        mask = mask != 0

        msr = np.mean((ref[mask, :] - tar[mask, :]) ** 2, axis=0)
        max2 = np.max(ref, axis=0) ** 2

        psnrall = 10 * np.log10(max2 / msr)
        out = {}
        out['all'] = psnrall
        out['ave'] = np.mean(psnrall)
        Result_RSNR = out['all']

    return Result_RSNR

def SAM(ref_img, rec_img):
    tmp = (np.sum(ref_img*rec_img, axis=2) + np.finfo(float).eps) \
        / (np.sqrt(np.sum(ref_img**2, axis=2)) + np.finfo(float).eps) \
        / (np.sqrt(np.sum(rec_img**2, axis=2)) + np.finfo(float).eps)
    sam = np.mean(np.real(np.arccos(tmp)))
    return sam


def SSIM(ref_img, rec_img, k1=0.01, k2=0.03, L=255):
    c1 = (k1 * L)**2
    c2 = (k2 * L)**2
    mu_x = np.mean(ref_img, axis=(1, 2), keepdims=True)
    mu_y = np.mean(rec_img, axis=(1, 2), keepdims=True)
    sigma_x = np.std(ref_img, axis=(1, 2), keepdims=True)
    sigma_y = np.std(rec_img, axis=(1, 2), keepdims=True)
    sigma_xy = np.mean((ref_img - mu_x) * (rec_img - mu_y), axis=(1, 2), keepdims=True)
    ssim = (2 * mu_x * mu_y + c1) * (2 * sigma_xy + c2) / \
           ((mu_x**2 + mu_y**2 + c1) * (sigma_x**2 + sigma_y**2 + c2))
    return np.mean(ssim)



def UIQI(ref_img, rec_img):
    c1 = (0.01 * 255) ** 2
    c2 = (0.03 * 255) ** 2

    tensor1_sq = ref_img * ref_img
    tensor2_sq = rec_img * rec_img
    tensor1_tensor2 = ref_img * rec_img

    tensor1_mean = np.mean(ref_img)
    tensor2_mean = np.mean(rec_img)

    tensor1_sq_mean = np.mean(tensor1_sq)
    tensor2_sq_mean = np.mean(tensor2_sq)
    tensor1_tensor2_mean = np.mean(tensor1_tensor2)

    numerator = 4 * tensor1_tensor2_mean * tensor1_mean * tensor2_mean
    denominator = (tensor1_sq_mean + tensor2_sq_mean) * (tensor1_mean ** 2 + tensor2_mean ** 2)

    uiqi = numerator / (denominator + c1 + c2)

    return uiqi

def fspecial_gauss(size, sigma):
    x, y = np.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]
    g = np.exp(-((x**2 + y**2)/(2.0*sigma**2)))
    return g/g.sum()

import numpy as np

def downsample_hyperspectral(image, factor, sigma=None):
    """Downsample a hyperspectral image by a factor using Gaussian or uniform downsampling.
    
    Args:
        image (numpy.ndarray): A 3D array representing a hyperspectral image.
        factor (int): The downsampling factor.
        sigma (float, optional): The standard deviation of the Gaussian kernel.
                                 If None, use uniform downsampling instead.
    
    Returns:
        numpy.ndarray: A downsampled 3D array representing the hyperspectral image.
    """
    if sigma is not None:
        # Use Gaussian downsampling
        size = int(2 * np.ceil(2 * sigma) + 1)
        x, y = np.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]
        g = np.exp(-((x**2 + y**2)/(2.0*sigma**2)))
        kernel = g / np.sum(g)
        smoothed = np.zeros((image.shape[0]//factor, image.shape[1]//factor, image.shape[2]))
        for i in range(image.shape[2]):
            smoothed[:,:,i] = np.real(np.fft.ifft2(np.fft.fft2(image[:,:,i]) * np.fft.fft2(kernel, image[:,:,i].shape)))
        downsampled = smoothed[::factor, ::factor, :]
    else:
        # Use uniform downsampling
        downsampled = image[::factor, ::factor, :]
    
    return downsampled
