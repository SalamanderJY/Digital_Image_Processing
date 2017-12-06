import numpy as np


def int_to_bytes(number, length, byteorder='little'):
    return number.to_bytes(length, byteorder)


def bytes_to_int(input_bytes, byteorder='little'):
    return int.from_bytes(input_bytes, byteorder)

'''
BmpFileHeader
字段              大小 	描述
bfType            2 	0x4d42，BM
bfSize 	          4 	文件大小
bfReserved1       2  	一般0
bfReserved2       2  	一般0
bfOffBits 	      4 	偏移
'''


class BmpFileHeader:
    def __init__(self):
        self.bfType = int_to_bytes(0, 2)        # 0x4d42 BM
        self.bfSize = int_to_bytes(0, 4)        # File Size
        self.bfReserved1 = int_to_bytes(0, 2)
        self.bfReserved2 = int_to_bytes(0, 2)
        self.bfOffBits = int_to_bytes(0, 4)     # Header Info Offsets

'''
BmpStructureHeader
字段 	         大小 	描述
biSize 	          4 	大小
biWidth 	      4 	width
biHeight  	      4 	height
biPlanes  	      2 	1
biBitCount  	  2 	一般24
biCompression  	  4 	一般0
biSizeImage  	  4 	bfSize-bfOffBits
biXPelsPerMeter   4 	一般0
biXPelsPerMeter   4 	一般0
biClrUsed         4 	一般0
biClrImportant    4 	一般0
'''


class BmpStructureHeader:
    def __init__(self):
        self.biSize = int_to_bytes(0, 4)        # Bmp Header Size
        self.biWidth = int_to_bytes(0, 4)
        self.biHeight = int_to_bytes(0, 4)
        self.biPlanes = int_to_bytes(0, 2)      # Default 1
        self.biBitCount = int_to_bytes(0, 2)    # one pixel occupy bytes size
        self.biCompression = int_to_bytes(0, 4)
        self.biSizeImage = int_to_bytes(0, 4)
        self.biXPelsPerMeter = int_to_bytes(0, 4)
        self.biYPelsPerMeter = int_to_bytes(0, 4)
        self.biClrUsed = int_to_bytes(0, 4)
        self.biClrImportant = int_to_bytes(0, 4)


class BMP(BmpFileHeader, BmpStructureHeader):
    def __init__(self):
        BmpFileHeader.__init__(self)
        BmpStructureHeader.__init__(self)
        self.__bitSize = 0                     # pixels size
        self.palette = []                      # pixels palette
        self.bits = []                         # pixels array

    @property
    def width(self):
        return bytes_to_int(self.biWidth)

    @property
    def height(self):
        return bytes_to_int(self.biHeight)

    # unit is byte
    @property
    def bit_count(self):
        return bytes_to_int(self.biBitCount) // 8

    @property
    def width_step(self):
        return self.bit_count * self.width

    # Resolve a bmp file
    def resolve(self, filename):
        file = open(filename, 'rb')
        # BmpFileHeader
        self.bfType = file.read(2)
        self.bfSize = file.read(4)
        self.bfReserved1 = file.read(2)
        self.bfReserved2 = file.read(2)
        self.bfOffBits = file.read(4)
        # BmpStructureHeader
        self.biSize = file.read(4)
        self.biWidth = file.read(4)
        self.biHeight = file.read(4)
        self.biPlanes = file.read(2)
        self.biBitCount = file.read(2)
        # pixel size
        self.__bitSize = self.width * self.height * self.bit_count
        self.biCompression = file.read(4)
        self.biSizeImage = file.read(4)
        self.biXPelsPerMeter = file.read(4)
        self.biYPelsPerMeter = file.read(4)
        self.biClrUsed = file.read(4)
        self.biClrImportant = file.read(4)

        # Judge biBitCount, Add palette
        if int.from_bytes(self.biBitCount, 'little') < 24:
            for i in range(0, 2 << (int.from_bytes(self.biBitCount, 'little')-1)):
                self.palette.append(file.read(4))

        # Load pixel info
        count = 0

        # 32 bit, 4 bytes aligned
        while count < (self.width * self.bit_count * 8 + 31) // 32 * 4 * self.height:
            self.bits.append(file.read(1))
            count += 1
        file.close()

    # From left bottom corner to right top corner change to normal position
    def bmp2array(self):
        data = np.arange(
            self.width * self.height * int.from_bytes(self.biBitCount, 'little') // 8).reshape(414, 414, self.bit_count)
        aligned = (self.width * self.bit_count * 8 + 31) // 32 * 4
        for i in range(0, self.width):
            for j in range(0, self.height):
                for k in range(0, self.bit_count):
                    data[self.width - i - 1, j, k] = int.from_bytes(self.bits[i*aligned + j*self.bit_count + k],
                                                                    'little')
        # print(data.shape[0])
        return data

    @staticmethod
    def histogram(data):
        if data.shape[2] == 1:
            histogram = np.zeros((1, 256), np.uint8)
            for i in range(0, data.shape[0]):
                for j in range(0, data.shape[1]):
                    histogram[data[i, j]] += 1
            return histogram

if __name__ == "__main__":
    # 24
    bmp1 = BMP()
    bmp1.resolve('head24.bmp')
    result1 = bmp1.bmp2array()
    print(result1[0, 0])
    # 8
    bmp2 = BMP()
    bmp2.resolve('head8.bmp')
    result2 = bmp2.bmp2array()
    print(result2[7, 7])




































