from bmp import BMP
from GaussianNoise import GaussianNoise
from SaltPepperNoise import SaltPepperNoise
from MeanFilter import MeanFilter
from MedianFilter import MedianFilter
import cv2 as cv

bmp = BMP()
bmp.resolve('head24.bmp')
result = bmp.bmp2gray()
cv.imwrite('gray.bmp', result)


gn = GaussianNoise()
gn.addGaussianNoise(result, 0, 15)

spn = SaltPepperNoise()
spn.addSaltPepperNoise(result, 0.95)

meanfilter = MeanFilter()
meanfilter.filter('GaussianNoise.bmp')

medianfilter = MedianFilter()
medianfilter.filter('SaltPepperNoise.bmp')
