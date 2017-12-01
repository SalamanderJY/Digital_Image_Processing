import numpy as np
import cmath
import math
import time
import cv2 as cv


class DFT:

    # def fftlib(self, image):
        # s = np.fft.fft2(image)
        # print(s[0, 0])

    @staticmethod
    def freq2gray(x, y, freq):
        image = np.zeros((x, y, 1), np.uint8)
        for i in range(0, ((x + 7) // 8 - 1) * 8, 8):
            for j in range(0, ((y + 7) // 8 - 1) * 8, 8):
                maxvalue = 0
                minvalue = math.inf
                for ii in range(0, 8):
                    for jj in range(0, 8):
                        if freq[i + ii, j + jj].real > maxvalue:
                            maxvalue = freq[i + ii, j + jj].real
                        if freq[i + ii, j + jj].real < minvalue:
                            minvalue = freq[i + ii, j + jj].real
                each_value = 256 / (maxvalue - minvalue)
                for ii in range(0, 8):
                    for jj in range(0, 8):
                        image[i + ii, j + jj] = int((freq[i + ii, j + jj].real - minvalue) * each_value)
        cv.imwrite('graydft.bmp', image)

    @staticmethod
    def dft8(x, y, image, freq, dis):
        # resolve 8 * 8 block dft transform
        u = x
        v = y
        for i in range(0, 8):
            for j in range(0, 8):
                freq[u + i, v + j] = 0
                dis[u + i, v + j] = 0
                for ii in range(0, 8):
                    for jj in range(0, 8):
                        freq[u + i, v + j] += image[x + ii, y + jj] * \
                                                cmath.exp(1j * -2 * cmath.pi * (i * ii / 8 + j * jj / 8))
                dis[u + i, v + j] = math. sqrt(
                    math.pow(freq[u + i, v + j].real, 2) + math.pow(freq[u + i, v + j].imag, 2))

    @staticmethod
    def idft8(u, v, image, freq):
        x = u
        y = v
        for i in range(0, 8):
            for j in range(0, 8):
                temp = complex(0, 0)
                for ii in range(0, 8):
                    for jj in range(0, 8):
                        temp += freq[u + ii, v + jj] * \
                          cmath.exp(1j * 2 * cmath.pi * (i * ii / 8 + j * jj / 8))
                image[x + i, y + j] = (temp.real / 64)

    def dft(self, image):
        # BGR, 3 channels
        if image.shape[2] > 1:
            gray = np.arange(
                ((image.shape[0] + 7) // 8 * 8) * ((image.shape[1] + 7) // 8 * 8) * image.shape[2]).reshape(
                (image.shape[0] + 7) // 8 * 8, (image.shape[1] + 7) // 8 * 8, image.shape[2])

            m = (image.shape[0] + 7) // 8 * 8
            n = (image.shape[1] + 7) // 8 * 8
            l = image.shape[2]
            for ii in range(0, m):
                for jj in range(0, n):
                    for kk in range(0, l):
                        gray[ii, jj, kk] = 0
            for i in range(0, image.shape[0]):
                for j in range(0, image.shape[1]):
                    for k in range(0, image.shape[2]):
                        if k == 0:
                            gray[i, j, 2] = 0.615 * image[i, j, 2] - 0.515 * image[i, j, 1] - 0.100 * image[i, j, 0]
                        if k == 1:
                            gray[i, j, 1] = -0.147 * image[i, j, 2] - 0.289 * image[i, j, 1] + 0.436 * image[i, j, 0]
                        if k == 2:
                            gray[i, j, 0] = 0.299 * image[i, j, 2] + 0.587 * image[i, j, 1] + 0.114 * image[i, j, 0]

            # get frequency map of image
            freq = np.zeros(((image.shape[0] + 7) // 8 * 8, (image.shape[1] + 7) // 8 * 8), np.complex64)
            dis = np.zeros(((image.shape[0] + 7) // 8 * 8, (image.shape[1] + 7) // 8 * 8), np.complex64)
            idftimage = np.zeros(((image.shape[0] + 7) // 8 * 8, (image.shape[1] + 7) // 8 * 8, 1), np.uint8)

            # import gray image to 8*8 transformer
            time_start = time.time()  # time.time() 1970.1.1 start
            for u in range(0, image.shape[0], 8):
                for v in range(0, image.shape[1], 8):
                    self.dft8(u, v, gray[:, :, 0], freq, dis)
            time_end = time.time()  # time.time() 1970.1.1 end
            print(time_end - time_start)

            for u in range(0, image.shape[0], 8):
                for v in range(0, image.shape[1], 8):
                    self.idft8(u, v, idftimage, freq)
            cv.imwrite('idftgray.bmp', idftimage)

            # generate gray image of frequency map
            self.freq2gray(image.shape[0], image.shape[1], dis)


if __name__ == "__main__":
    pass
