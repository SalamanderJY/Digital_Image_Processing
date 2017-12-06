from bmp import BMP
from GaussianNoise import GaussianNoise
from SaltPepperNoise import SaltPepperNoise

bmp = BMP()
bmp.resolve('head24.bmp')
result = bmp.bmp2array()

gn = GaussianNoise()
gn.addGaussianNoise(result, 0, 5)


spn = SaltPepperNoise()
spn.addSaltPepperNoise(result, 0.8)
