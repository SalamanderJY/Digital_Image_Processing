import cv2 as cv
import numpy as np


class MeanFilter:

    def filter(self, filename):
        gray = cv.imread(filename, 0)
        image = np.copy(gray)
        # print(gray.shape)

        for i in range(1, gray.shape[0] - 1):
            for j in range(1, gray.shape[1] - 1):
                image[i, j] = np.sum(gray[i - 1:i + 2, j - 1:j + 2]) // 9

        cv.imwrite('MeanFilter.bmp', image)
