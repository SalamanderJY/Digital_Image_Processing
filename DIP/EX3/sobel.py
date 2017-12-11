import numpy as np
import cv2 as cv
from scipy import signal


class Sobel:

    def sobel_detection(self, image):
        # create kernel filters
        xSobel = np.array([(-1, 0, 1), (-2, 0, 2), (-1, 0, 1)])
        ySobel = np.array([(1, 2, 1), (0, 0, 0), (-1, -2, -1)])
        Gx = signal.convolve2d(image, xSobel)
        Gy = signal.convolve2d(image, ySobel)

        cv.imwrite('xSobel.bmp', Gx)
        cv.imwrite('ySobel.bmp', Gy)

        Gxy = np.sqrt(np.square(Gx) + np.square(Gy))

        cv.imwrite('xySobel.bmp', Gxy)

if __name__ == "__main__":

    sobel = Sobel()
    image = cv.imread('gray.bmp', 0)
    sobel.sobel_detection(image)
