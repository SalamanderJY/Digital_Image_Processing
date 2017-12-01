from bmp import BMP
from dft import DFT
from dct import DCT

bmp = BMP()
bmp.resolve('head24.bmp')
result = bmp.bmp2array()

# dft = DFT()
# dft.dft(result)

dct = DCT()
dct.dct(result)




