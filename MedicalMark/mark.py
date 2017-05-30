# -*- coding: UTF-8 -*-

import cv2
import cv2.cv as cv
import numpy as np

# 图像预处理，获得图像中红色的元素
img = cv2.imread("test1.jpg")

# pre-processing image
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
# pre-processing image finished

# Clean Edge
left = 0.075
right = 0.075
top = 0.15
bottom = 0.15

edge = [left * row,
        row - right * row,
        top * col,
        col - bottom * row]

for i in range(1, row):
    for j in range(1, int(edge[0])):
        emptyImage[i, j] = 0
    for j in range(int(edge[1]), col):
        emptyImage[i, j] = 0

for j in range(1, col):
    for i in range(1, int(edge[2])):
        emptyImage[i, j] = 0
    for i in range(int(edge[3]), row):
        emptyImage[i, j] = 0

cv2.imwrite("test.jpg", emptyImage)

blur = cv2.GaussianBlur(emptyImage, (9, 9), 2)

cv2.imwrite("test.jpg", blur)

circles = cv2.HoughCircles(blur, cv.CV_HOUGH_GRADIENT, 1, 0.1, param1=100, param2=50)

if circles is None:
    for i in range(1, 20):
        circles = cv2.HoughCircles(blur, cv.CV_HOUGH_GRADIENT, 1, row / 20, param1=100 - 5 * i, param2=50 - 5 * i)
        if circles is not None:
            break

print circles

circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 1)
    # draw the center of the circle
    # cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 1)

cv2.imshow('detected circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
