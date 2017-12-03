from dct import DCT
from dft import DFT

from bmp import BMP

bmp = BMP()
bmp.resolve('head24.bmp')
result = bmp.bmp2array()

dft = DFT()
dft.dft(result)

dct = DCT()
dct.dct(result)




