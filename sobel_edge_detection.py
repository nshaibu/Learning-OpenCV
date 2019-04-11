import cv2
import numpy as np

c_img = cv2.imread("pic1.jpg", cv2.IMREAD_COLOR)
img = cv2.cvtColor(c_img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, None, fx=0.12, fy=0.12, interpolation=cv2.INTER_AREA)

detected_img_vertical = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
detected_img_horizontal = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
detected_img = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=5)

cv2.imshow("Original", img)
cv2.imshow("vertical", detected_img_vertical)
cv2.imshow("horizontal", detected_img_horizontal)
cv2.imshow("All", detected_img)

cv2.waitKey()