# -*- coding: UTF-8 -*-

import cv2
import cv2.cv as cv
import numpy as np

# opencv image show in python
img1 = cv2.imread("test2.jpg")
print img1.shape
# BGR image
for i in range(0, 511):
    for j in range(0, 511):
        #if img1[i,j][0] < 150 and img1[i,j][1] < 150 and img1[i,j][2] > 170:
        #    img1[i,j] = [255,255,255]
        #else:
        #    img1[i,j] = [0,0,0]

        # better pixel accessing and editing method
        diff1 = img1.item(i, j, 2) - img1.item(i, j, 0)
        diff2 = img1.item(i, j, 2) - img1.item(i, j, 0)

        if diff1 - diff2 >= 0:
            if diff2 > 30:
                img1[i, j] = [255, 255, 255]
            else:
                img1[i, j] = [0, 0, 0]
        else:
            if diff1 > 30:
                img1[i, j] = [255, 255, 255]
            else:
                img1[i, j] = [0, 0, 0]
cv2.imwrite('test.jpg', img1);

cv2.namedWindow("Image")
cv2.imshow("Image", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()



