<center>
    <img style="border-radius: 0.3125em;
    box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" 
    src="./logo-color.svg">
    <br>
    <div style="color:orange; border-bottom: 1px solid #d9d9d9;
    display: inline-block;
    color: #999;
    padding: 2px;">Hyperspectral image super-resolution evaluation metrics </div>
</center>

Sure! Here's the translated version of the README file in English using Markdown format:

---

# HyperEvalSR

HyperEvalSR is an open-source project that provides evaluation metrics for hyperspectral image quality assessment. The included metrics are as follows:

- **Peak Signal to Noise Ratio (PSNR)**: Measures the ratio between the maximum possible power of a signal and the power of corrupting noise.
- **Reconstruction Signal-to-Noise Ratio (RSNR)**: Evaluates the signal-to-noise ratio of the reconstructed image.
- **Degree of Distortion (DD)**: Represents the level of distortion in the image.
- **Spectral Angle Mapper (SAM)**: Measures the spectral similarity between two images using the angle between their spectral vectors.
- **Root Mean Squared Error (RMSE)**: Computes the square root of the average squared differences between the reference and reconstructed images.
- **Erreur Relative Globale Adimensionnelle de Synthèse (ERGAS)**: Calculates the relative global dimensionless synthesis error.
- **Structural Similarity Index (SSIM)**: Assesses the structural similarity between the reference and reconstructed images.

In this context, we assume that the reference image and the reconstructed image obtained from the algorithm are denoted as $\mathbf{X}$ and $\widehat{\mathbf{X}}$, respectively.

---
## PSNR
Peak Signal-to-Noise Ratio (PSNR) is commonly used to measure the similarity between a reconstructed image and an original image. It is expressed in decibels (dB), and a higher value indicates a higher similarity between the reconstructed and original images. The calculation formula for PSNR is as follows:

$$
\mathrm{PSNR}=10\log _{10}\left( \frac{\max ^2\left( \widehat{\mathbf{X}} \right)}{\mathrm{MSE}\left( \mathbf{X},\widehat{\mathbf{X}} \right)} \right) 
$$

where $\mathrm{MSE}$ represents the mean squared error, calculated as:

$$
\mathrm{MSE}=\frac{1}{N_wN_h}||\widehat{\mathbf{X}}-\mathbf{X}||_{F}^{2} \tag{1} \label{eq1}
$$

In this formula, $N_w$ and $N_h$ represent the width and height of the image, respectively.
## RMSE
The RMSE is a commonly used indicator to describe the degree of difference between the reconstructed image and the reference image. Smaller errors result in smaller RMSE values. When the reconstructed image and the reference image are exactly the same, the RMSE equals 0. The RMSE is defined as:

$$
\mathrm{RMSE}=\sqrt{\mathrm{MSE}}
$$

The definition of $\mathrm{MSE}$ is shown in formula $\eqref{eq1}$.
## RSNR
The RSNR is commonly used to measure the spatial quality of the reconstructed image. Higher RSNR values indicate smaller differences between the reconstructed and original images, and thus better image quality. The RSNR is calculated as:

$$
\mathrm{RSNR}=10\log _{10}\left( \frac{||\mathbf{X}||_{F}^{2}}{||\widehat{\mathbf{X}}-\mathbf{X}||_{F}^{2}} \right) 
$$
## DD
The Degree of Distortion (DD) is an indicator used to describe the degree of signal distortion, typically used to evaluate the distortion during signal transmission or storage. Smaller distortions result in smaller DD values, with the optimal value being 0. The DD is defined as:

$$
\mathrm{DD}=\frac{1}{N_wN_h}||\mathrm{vec}\left( \widehat{\mathbf{X}} \right) -\mathrm{vec}\left( \mathbf{X} \right) ||_{1}^{2}
$$

In this formula, $N_w$ and $N_h$ represent the width and height of the image, respectively.
## SAM
The Spectral Angle Mapper (SAM) compares the similarity between the reconstructed and reference images by measuring the spectral angle of each pixel. The higher the similarity, the smaller the SAM value. The SAM is calculated as:

$$
\mathrm{SAM}=\frac{1}{M}\sum_{n=1}^M{\mathrm{arc}\cos}\left( \frac{\left( \hat{\mathbf{x}}\left[ n \right] \right) ^{\mathrm{T}}\mathbf{x}\left[ n \right]}{|\hat{\mathbf{x}}\left[ n \right] |_2\cdot |\mathbf{x}\}\left[ n \right] |_2} \right) 
$$

In this formula, $\mathbf{z}\left[ n \right]$ represents the $n$-th column of $\mathbf{Z}$, and $M$ represents the number of spectral bands.
## ERGAS
ERGAS is a relative error indicator that can be used to compare the quality of reconstructed remote sensing images with different resolutions and sizes, as well as to evaluate image quality at different compression ratios. Smaller ERGAS values indicate higher spatial and spectral similarity between the reconstructed and reference images. The ERGAS is calculated as:

$$
\mathrm{ERGAS}=\frac{100}{r}\sqrt{\frac{1}{M}\sum_{m=1}^M{\frac{\mathrm{RMSE}_{m}^{2}}{\mu _{\mathbf{X}^{\left( m \right)}}^{2}}}}
$$

In this formula, $r$ represents the spatial down-sampling ratio, $\mu _{\mathbf{X}^{\left( m \right)}}$ represents the mean of the $m$-th row of $\mathbf{X}$, and $\mathrm{RMSE}_m$ represents the RMSE value of the $m$-th spectral band.
## SSIM
The Structural Similarity Index (SSIM) is an indicator used to evaluate the similarity between two images and to quantitatively assess the degree of image distortion. The SSIM value ranges between $[-1,1]$, with larger values indicating greater similarity. The SSIM index calculation is based on the characteristics of the human visual system, simulating human perception. Specifically, the SSIM index decomposes the image into three components for evaluation: luminance, contrast, and structure. The luminance component represents the similarity between the average brightness of the two images; the contrast component represents the similarity between the standard deviations of the two images; and the structure component represents the difference between the correlations of the two images. The SSIM index can be calculated using the following formula:

$$
\mathrm{SSIM}=\left[ l\left( \widehat{\mathbf{X}},\mathbf{X} \right) \right] ^{\alpha}\left[ c\left( \widehat{\mathbf{X}},\mathbf{X} \right) \right] ^{\beta}\left[ s\left( \widehat{\mathbf{X}},\mathbf{X} \right) \right] ^{\gamma}
$$

In this formula, $\widehat{\mathbf{X}}$ and $\mathbf{X}$ represent the two images to be compared, and $l\left( \widehat{\mathbf{X}},\mathbf{X} \right)$, $c\left( \widehat{\mathbf{X}},\mathbf{X} \right)$, and $s\left( \widehat{\mathbf{X}},\mathbf{X} \right)$ represent their luminance, contrast, and structure similarity, respectively. These are defined as:
$$
l\left( \widehat{\mathbf{X}},\mathbf{X} \right) =\frac{2\mu _{\widehat{\mathbf{X}}}\mu _{\mathbf{X}}+c_1}{\mu _{\widehat{\mathbf{X}}}^{2}+\mu _{\mathbf{X}}^{2}+c_1}\\	c\left( \widehat{\mathbf{X}},\mathbf{X} \right) =\frac{2\sigma _{\widehat{\mathbf{X}}\mathbf{X}}+c_2}{\sigma _{\widehat{\mathbf{X}}}^{2}+\sigma _{\mathbf{X}}^{2}+c_2}\\	s\left( \widehat{\mathbf{X}},\mathbf{X} \right) =\frac{\sigma _{\widehat{\mathbf{X}}}+c_3}{\sigma _{\widehat{\mathbf{X}}}+\sigma _{\mathbf{X}}+c_3}
$$
In these formulas, $\mu$ represents the mean of the image, $\sigma$ represents the standard deviation of the image, and $\sigma _{\widehat{\mathbf{X}}\mathbf{X}}$ represents the covariance between the two images. $c1, c2$, and $c3$ are constants, usually set to $c1=\left( 0.01*N_wN_h \right) ^2, c2=\left( 0.03*N_wN_h \right) ^2, c3=c2/2$. The values of $\alpha$, $\beta$, and $\gamma$ are usually set to 1.
