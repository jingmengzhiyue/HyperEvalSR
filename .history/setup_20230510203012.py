from distutils.command.install_data import install_data
from ensurepip import version
from re import U
from struct import pack
import setuptools
with open(".\docs\index.md", "r") as f:
    long_description = f.read()
setuptools.setup(
    name = "HyperEvalSR",
    version="0.3",
    author = "jingmengzhiyue",
    author_email = "jingmengzhiyue@gmail.com",
    description = "An open source python package for super-resolution/recovery quality evaluation of hyperspectral images, including RMSE, ERGAS, SSIM, RSNR, PSNR, CC, DD, and SAM.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/jingmengzhiyue/HyperEvalSR",
    packages =  setuptools.find_packages(),
    classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
    install_requires = [
    'numpy',
    'scipy'
    ],
    python_requires = ">=3",

)