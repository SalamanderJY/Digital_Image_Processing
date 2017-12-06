import random
import cv2 as cv
import numpy as np


class GaussianNoise:

    def addGaussianNoise(self, source_image, means, sigma):
        # Gaussian means and sigma
        image = np.copy(source_image)
        for i in range(0, image.shape[0]):
            for j in range(0, image.shape[1]):
                delta_b = random.gauss(means, sigma)
                image[i, j, 0] = self.normalize(image[i, j, 0], delta_b)
                delta_g = random.gauss(means, sigma)
                image[i, j, 1] = self.normalize(image[i, j, 1], delta_g)
                delta_r = random.gauss(means, sigma)
                image[i, j, 2] = self.normalize(image[i, j, 2], delta_r)
        cv.imwrite('GaussianNoise.bmp', image)

        self.MeanFilter(image, 3, 3)

    def normalize(self, pixel, delta):
        if pixel + delta > 255:
            result = 255
            return result
        if pixel + delta < 0:
            result = 0
            return result
        return int(pixel + delta)

    def MeanFilter(self, source_image, m, n):
        image = np.copy(source_image)
        # kernel 3 * 3
        for i in range(1, image.shape[0] - 1):
            for j in range(1, image.shape[1] - 1):
                sumb = 0
                for ii in range(i - 1, i + 2):
                    for jj in range(j - 1, j + 2):
                        sumb += source_image[ii, jj, 0]
                image[i, j, 0] = int(sumb / m / n)

                sumg = 0
                for ii in range(i - 1, i + 2):
                    for jj in range(j - 1, j + 2):
                        sumg += source_image[ii, jj, 1]
                image[i, j, 1] = int(sumg / m / n)

                sumr = 0
                for ii in range(i - 1, i + 2):
                    for jj in range(j - 1, j + 2):
                        sumr += source_image[ii, jj, 2]
                image[i, j, 2] = int(sumr / m / n)

        cv.imwrite('MeanFilter.bmp', image)



