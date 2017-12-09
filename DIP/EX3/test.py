from bmp import BMP
from GaussianNoise import GaussianNoise
from SaltPepperNoise import SaltPepperNoise
from MeanFilter import MeanFilter
from MedianFilter import MedianFilter

import cv2 as cv
import evaluation as ev

bmp = BMP()
bmp.resolve('head24.bmp')
result = bmp.bmp2gray()
cv.imwrite('gray.bmp', result)

for i in range(1, 4):
    gn = GaussianNoise()
    gn.addGaussianNoise(result, 0, i * 5)

    spn = SaltPepperNoise()
    spn.addSaltPepperNoise(result, 1 - 0.05 * i)

    meanfilter = MeanFilter()
    meanfilter.filter('GaussianNoise.bmp')

    medianfilter = MedianFilter()
    medianfilter.filter('SaltPepperNoise.bmp')

    source = cv.imread('gray.bmp', 0)
    meanfilter_result = cv.imread('MeanFilter.bmp', 0)
    medianfilter_result = cv.imread('MedianFilter.bmp', 0)

    psnr_mean = ev.psnr(source, meanfilter_result)
    ssim_mean = ev.ssim(source, meanfilter_result)
    print('Mean Filter:')
    print('Gussian Means and Sigma:', 0, i * 5)
    print('PSNR: %f, SSIM: %f' % (psnr_mean, ssim_mean))

    psnr_median = ev.psnr(source, medianfilter_result)
    ssim_median = ev.ssim(source, medianfilter_result)
    print('Median Filter:')
    print('SNR:', 1 - 0.05 * i)
    print('PSNR: %f, SSIM: %f' % (psnr_median, ssim_median))

