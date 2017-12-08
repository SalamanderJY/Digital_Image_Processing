import numpy as np
import cv2 as cv
import math

class WaveletTransform:

    # resolve input m*n dimensional matrix in 2D wavelet transform.
    # input variables: image, m*n 2D matrix.
    # output variables: wavelet, LL, HL, LH, HH, divide source matrix into four parts.
    def dwt2(self, image, series):
        # H2 Haar filter
        lpd = [1/2, 1/2]
        hpd = [-1/2, 1/2]
        row = image.shape[1]
        col = image.shape[0]

        for i in range(0, row):
            temp = image[i, :]
            temp_dwt = self.dwt(temp, lpd, hpd)
            image[i, :] = temp_dwt

        for j in range(0, col):
            temp = image[:, j]
            temp_dwt = self.dwt(temp, lpd, hpd)
            image[:, j] = temp_dwt

        LL = image[0:int(row // 2), 0:int(col // 2)]
        LH = image[int(row // 2):row, 0:int(col // 2)]
        HL = image[0:int(row // 2), int(col // 2):col]
        HH = image[int(row // 2):row, int(col // 2):col]

        print(LL.shape, LH.shape, HL.shape, HH.shape)

        if series == 2:
            self.dwt2(image[0:int(row // 2), 0:int(col // 2)], 1)

        cv.imwrite('dwt.bmp', image)

    def idwt2(self, LL, HL, LH, HH):
        lpr = [1, 1]
        hpr = [1, -1]
        matrix1 = np.concatenate((LL, HL), 1)
        matrix2 = np.concatenate((LH, HH), 1)
        matrix = np.concatenate((matrix1, matrix2), 0)
        output = np.copy(matrix)

        row = matrix.shape[1]
        col = matrix.shape[0]

        for i in range(0, col):
            ca1 = matrix[0:row//2, i]
            cd1 = matrix[row//2:row, i]
            # median = np.median(cd1)
            # for t in range(0, row // 2):
            #     if math.fabs(cd1[t]) < median / 0.6745:
            #         cd1[t] = 0
            temp = self.idwt(ca1, cd1, lpr, hpr)
            output[:, i] = temp

        for j in range(0, row):
            ca2 = output[j, 0:col//2]
            cd2 = output[j, col//2:col]
            # median = np.median(cd1)*0.01
            # for t in range(0, row // 2):
            #     if math.fabs(cd1[t]) < median:
            #         cd1[t] = 0
            temp = self.idwt(ca2, cd2, lpr, hpr)
            output[j, :] = temp

        cv.imwrite('idwt.bmp', output)

    # vector : input vector
    # lpd: low pass filter
    # hpd: high pass filter
    # dim: resolve series
    def dwt(self, vector, lpd, hpd):
        cA = np.copy(vector)
        cvl = np.convolve(cA, lpd)
        dnl = self.downspl(cvl)
        cvh = np.convolve(cA, hpd)
        dnh = self.downspl(cvh)
        return dnl + dnh

    # down sampling with even number
    def downspl(self, vector):
        length = len(vector)
        outlen = int(np.floor(length / 2))
        output = []
        for i in range(0, outlen):
            output.append(vector[2 * i])
        return output

    def idwt(self, cA, cD, lpr, hpr):
        lca = len(cA)
        lcd = len(cD)

        while lcd >= lca:
            upl = self.upspl(cA)
            cvl = np.convolve(upl, lpr)
            cDup = cD[lcd-lca:lcd]
            uph = self.upspl(cDup)
            cvh = np.convolve(uph, hpr)

            cA = cvl + cvh
            cD = cD[0:lcd - lca]
            lca = len(cA)
            lcd = len(cD)
        return cA

    # up sampling with appending 0
    def upspl(self, vector):
        n = len(vector)
        m = 2 * n - 1
        output = []
        for i in range(0, m):
            if i % 2 == 0:
                output.append(vector[i // 2])
            else:
                output.append(0)
        return output


if __name__ == "__main__":
    wavelet = WaveletTransform()
    img = cv.imread('SaltPepperNoise.bmp', 0)
    row = img.shape[1]
    col = img.shape[0]
    wavelet.dwt2(img, 1)

    LL = img[0:int(row // 2), 0:int(col // 2)]
    LH = img[int(row // 2):row, 0:int(col // 2)]
    HL = img[0:int(row // 2), int(col // 2):col]
    HH = img[int(row // 2):row, int(col // 2):col]

    wavelet.idwt2(LL, HL, LH, HH)












