import numpy as np
import math
import time
import cv2 as cv


class DCT:

    @staticmethod
    def basefunc(x):
        image = np.zeros((x * x, x * x, 1), np.uint8)
        image64 = np.zeros((x * x, x * x, 1), np.float)
        maxvalue = -math.inf
        minvalue = math.inf
        for u in range(0, x):
            for v in range(0, x):
                for i in range(0, x):
                    for j in range(0, x):
                        # if u == 0 & v == 0:
                        #     image64[u * x + i, v * x + j] = 1 / x
                        # if u == 0 & v != 0:
                        #     image64[u * x + i, v * x + j] = math.cos((2 * j + 1) * v * math.pi / 2 / x) * \
                        #                                     math.sqrt(2) / x
                        # if u != 0 & v == 0:
                        #     image64[u * x + i, v * x + j] = math.cos((2 * i + 1) * u * math.pi / 2 / x) * \
                        #                                     math.sqrt(2) / x
                        # if u != 0 & v != 0:
                            image64[u * x + i, v * x + j] = math.cos((2 * i + 1) * u * math.pi / 2 / x) * \
                                math.cos((2 * j + 1) * v * math.pi / 2 / x) / x * 2
        for i in range(0, x * x):
            for j in range(0, x * x):
                if maxvalue < image64[i, j]:
                    maxvalue = image64[i, j]
                if minvalue > image64[i, j]:
                    minvalue = image64[i, j]
        print(maxvalue, minvalue)
        each = 255 / (maxvalue - minvalue)
        for i in range(0, x * x):
            for j in range(0, x * x):
                image[i, j] = (image64[i, j] - minvalue) * each
                #print(image64[i, j])
        cv.imwrite('basefunc.bmp', image)

    @staticmethod
    def freq2gray(x, y, freq):
        image = np.zeros((x, y, 1), np.uint8)
        for i in range(0, ((x + 7) // 8 - 1) * 8, 8):
            for j in range(0, ((y + 7) // 8 - 1) * 8, 8):
                maxvalue = -math.inf
                minvalue = math.inf
                for ii in range(0, 8):
                    for jj in range(0, 8):
                        if freq[i + ii, j + jj] > maxvalue:
                            maxvalue = freq[i + ii, j + jj]
                        if freq[i + ii, j + jj] < minvalue:
                            minvalue = freq[i + ii, j + jj]
                each_value = 256 / (maxvalue - minvalue)
                for ii in range(0, 8):
                    for jj in range(0, 8):
                        image[i + ii, j + jj] = int((freq[i + ii, j + jj] - minvalue) * each_value)
        cv.imwrite('graydct.bmp', image)

    @staticmethod
    def dct8matrix(x, keep):
        matrix = np.zeros((x, x), np.float)
        if keep == 0:
            for i in range(0, x):
                for j in range(0, x):
                    if i == 0:
                        matrix[i, j] = math.sqrt(2 / x) * math.sqrt(1 / 2)
                        #print(matrix[i, j])
                    else:
                        matrix[i, j] = math.sqrt(2 / x) * math.cos((2 * (j + 1) - 1) * i / 2 / x * math.pi)
                        #print(matrix[i, j])
        else:
            for i in range(0, keep):
                for j in range(0, keep):
                    if i == 0:
                        matrix[i, j] = math.sqrt(2 / x) * math.sqrt(1 / 2)
                    else:
                        matrix[i, j] = math.sqrt(2 / x) * math.cos((2 * (j + 1) - 1) * i / 2 / x * math.pi)

        return matrix

    def dct8(self, x, y, image, freq, keep=0):
        # resolve 8 * 8 block dft transform
        imagematrix = np.zeros((8, 8), np.float)
        for i in range(0, 8):
            for j in range(0, 8):
                imagematrix[i, j] = image[x + i, y + j]
        dctmatrix = self.dct8matrix(8, keep)
        dctmatrixtrans = dctmatrix.T
        temp = np.dot(dctmatrix, imagematrix)
        result = np.dot(temp, dctmatrixtrans)
        for i in range(0, 8):
            for j in range(0, 8):
                freq[x + i, y + j] = result[i, j]

    def idct8(self, u, v, image, freq, keep=0):
        freqmatrix = np.zeros((8, 8), np.float)
        for i in range(0, 8):
            for j in range(0, 8):
                freqmatrix[i, j] = freq[u + i, v + j]
        dctmatrix = self.dct8matrix(8, keep)
        dctmatrixtrans = dctmatrix.T
        temp = np.dot(dctmatrixtrans, freqmatrix)
        result = np.dot(temp, dctmatrix)
        for i in range(0, 8):
            for j in range(0, 8):
                image[u + i, v + j] = result[i, j]

    @staticmethod
    def psnr(image1, image2):
        diff = np.abs(image1 - image2)
        rmse = np.sqrt(diff).sum()
        psnr = 20 * np.log10(255 / rmse)
        return psnr

    def dct(self, image):
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
            freq = np.zeros(((image.shape[0] + 7) // 8 * 8, (image.shape[1] + 7) // 8 * 8), np.float)
            idctimage = np.zeros(((image.shape[0] + 7) // 8 * 8, (image.shape[1] + 7) // 8 * 8, 1), np.uint8)

            for u in range(0, image.shape[0], 8):
                for v in range(0, image.shape[1], 8):
                    self.dct8(u, v, gray[:, :, 0], freq)
            self.freq2gray(image.shape[0], image.shape[1], freq)

            for u in range(0, image.shape[0], 8):
                for v in range(0, image.shape[1], 8):
                    self.idct8(u, v, idctimage, freq)
            cv.imwrite('idctgray.bmp', idctimage)

            for keep in range(0, 8):
                for u in range(0, image.shape[0], 8):
                    for v in range(0, image.shape[1], 8):
                        self.dct8(u, v, gray[:, :, 0], freq, keep)

                for u in range(0, image.shape[0], 8):
                    for v in range(0, image.shape[1], 8):
                        self.idct8(u, v, idctimage, freq, keep)
                cv.imwrite('idctgray'+str(keep)+'.bmp', idctimage)
                psnrvalue = self.psnr(gray[:, :, 0], idctimage)
                print(psnrvalue)

if __name__ == "__main__":
    dct = DCT()
    dct.basefunc(8)
    # dctmatrix = dct.dct8matrix(4)
