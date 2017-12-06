import random
import cv2 as cv
import numpy as np


class SaltPepperNoise:

    def addSaltPepperNoise(self, image, snr):

        pixelcount = image.shape[0] * image.shape[1]
        randomcount = int(pixelcount * (1 - snr))

        gray = np.zeros((image.shape[0], image.shape[1]), np.uint8)

        for i in range(0, image.shape[0]):
            for j in range(0, image.shape[1]):
                gray[i, j] = 0.299 * image[i, j, 2] + 0.587 * image[i, j, 1] + 0.114 * image[i, j, 0]

        cv.imwrite('gray.bmp', gray)

        for i in range(1, randomcount):
            randx = random.randint(0, gray.shape[0] - 1)
            randy = random.randint(0, gray.shape[1] - 1)
            if random.randint(0, 1) == 0:
                gray[randx, randy] = 0
            else:
                gray[randx, randy] = 255

        cv.imwrite('SaltPepperNoise.bmp', gray)






