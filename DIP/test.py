from bmp import Bmp

bmp = Bmp()
bmp.resolve('head24.bmp')
result = bmp.bmp_to_array()
print(result[0, 0])
