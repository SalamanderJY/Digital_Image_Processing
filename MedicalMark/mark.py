# -*- coding: UTF-8 -*-

import cv2
import cv2.cv as cv
import numpy as np

# 图像预处理，获得图像中红色的元素
img = cv2.imread("test3.jpg")

row = img.shape[0]
# print row
col = img.shape[1]
# print col
channel = img.shape[2]
# print channel

emptyImage = np.zeros((row, col, 1), np.uint8)
# print emptyImage.shape
count = 0
for i in range(1, row):
    for j in range(1, col): # print emptyImage[i, j]
        count += 1
        # For BGR image, it returns an array of Blue, Green, Red values.
        colorR = img.item(i, j, 2)
        # print ("count : %d %d" % (count, colorR))
        colorG = img.item(i, j, 1)
        colorB = img.item(i, j, 0)
        diff1 = colorR - colorB if colorR > colorB else 0
        diff2 = colorR - colorG if colorR > colorG else 0
        emptyImage[i, j] = diff1 if diff1 < diff2 else diff2

cv2.imwrite("test.jpg", emptyImage)





# opencv image show in python
# BGR image




