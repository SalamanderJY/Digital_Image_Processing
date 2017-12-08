import random
import numpy as np
import cv2 as cv


class SaltPepperNoise:

    def addSaltPepperNoise(self, image, snr):

        pixels = image.shape[0] * image.shape[1]
        noisies = int(pixels * (1 - snr))

        gray = np.copy(image)

        for i in range(1, noisies):
            rand_x = random.randint(0, gray.shape[0] - 1)
            rand_y = random.randint(0, gray.shape[1] - 1)
            if random.randint(0, 1) == 0:
                gray[rand_x, rand_y] = 0
            else:
                gray[rand_x, rand_y] = 255

        cv.imwrite('SaltPepperNoise.bmp', gray)






