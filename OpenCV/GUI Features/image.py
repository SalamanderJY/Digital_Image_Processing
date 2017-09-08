# -*- coding: UTF-8 -*-

# Use the function cv2.imread() to read an image. The image should be in the working directory or a full path of image should be given.

import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('comic.jpg', 0)

# print img

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('gray.png', img)

img = cv2.imread('comic.jpg', 0)
cv2.imshow('image', img)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('comic.png', img)
    cv2.destroyAllWindows()