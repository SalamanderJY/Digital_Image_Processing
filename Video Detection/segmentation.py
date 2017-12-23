import cv2
import math


# Capture the video stream
cap = cv2.VideoCapture('test.avi')
# Output loop.
while cap.isOpened():
    ret, frame = cap.read()
    # If current frame is exist
    if ret:
        print(frame.shape)
        # Get source image into gray scale.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        # Get width and height of source image.
        width = gray.shape[0]
        height = gray.shape[1]
        # Get binary image through traditional thresholded method
        ret_threshold, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
        cv2.imshow('detection', threshold)
        # avoid noise from edge
        ret_threshold, threshold = cv2.threshold(gray[0:int(width * 0.95), 0:int(height * 0.95)], 200, 255,
                                                 cv2.THRESH_BINARY)
        threshold, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        # if the contours is exist.
        if len(contours) > 0:
            count = 0
            index = 0
            minval = math.inf
            # 遍历所有的轮廓
            for i in contours:
                # 将轮廓分解为识别对象的左上角坐标和宽、高
                x, y, w, h = cv2.boundingRect(i)
                # 获取最顶端的轮廓
                if minval > y:
                    minval = y
                    index = count
                count += 1

            # print(index)
            cv2.drawContours(frame, contours[index], -1, (0, 0, 255), 3)
            cv2.imshow('contours', frame)

        cv2.waitKey(0)
        # exit operation executed when program running.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Detect end of stream and finish loop.
    else:
        break

cap.release()
cv2.destroyAllWindows()
