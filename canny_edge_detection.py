import cv2
import numpy as np

img = cv2.imread("pic1.jpg", cv2.IMREAD_COLOR)
img = cv2.resize(img, None, fx=0.12, fy=0.12, interpolation=cv2.INTER_AREA)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

detected_img = cv2.Canny(gray_img, 0, 1)

cv2.imshow("Original", img)
cv2.imshow("Canny", detected_img)

cv2.waitKey()