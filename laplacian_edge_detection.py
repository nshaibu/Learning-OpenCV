import cv2
import numpy as np

img = cv2.imread("pic1.jpg", cv2.IMREAD_COLOR)
img = cv2.resize(img, None, fx=0.12, fy=0.12, interpolation=cv2.INTER_AREA)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

detected_img = cv2.Laplacian(gray_img, cv2.CV_64F)

cv2.imshow("Original", img)
cv2.imshow("Laplacian", detected_img)

cv2.waitKey()