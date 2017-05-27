# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import cv2.cv as cv
import matplotlib.pyplot as plt

img = cv2.imread('test.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#灰度图像

plt.subplot(121), plt.imshow(gray,'gray')
plt.xticks([]), plt.yticks([])
#hough transform
circles1 = cv2.HoughCircles(gray,cv.CV_HOUGH_GRADIENT,1,20,
                            param1=200,param2=50,minRadius=0,maxRadius=0)
circles = circles1[0,:,:]#提取为二维
circles = np.uint16(np.around(circles))#四舍五入，取整
for i in circles[:]:
    cv2.circle(img,(i[0],i[1]),i[2],(255,0,0),2)#画圆
    cv2.circle(img,(i[0],i[1]),2,(255,0,255),3)#画圆心

plt.subplot(122), plt.imshow(img)
plt.xticks([]), plt.yticks([])

cv2.namedWindow("Image")
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
