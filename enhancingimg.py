import cv2
import numpy as np

img = cv2.imread("pic1.jpg", cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
img = cv2.resize(img, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)

histeq = np.copy(img)
histeq[:, :, 0] = cv2.equalizeHist(histeq[:, :, 0])
histeq = cv2.cvtColor(histeq, cv2.COLOR_YUV2BGR)

cv2.imshow("Original", img)
cv2.imshow("Histogram equalized", histeq)

cv2.waitKey()