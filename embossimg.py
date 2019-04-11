import cv2
import numpy as np

np.set_printoptions(threshold=np.inf)
img = cv2.imread("pic1.jpg", cv2.IMREAD_COLOR)
img = cv2.resize(img, None, fx=0.12, fy=0.12, interpolation=cv2.INTER_AREA)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel_1 = np.array([[0, -1, -1],[1, 0, -1],[1, 1, 0]], dtype=np.float32)
kernel_2 = np.array([[0, 1, 1],[-1, 0, 1],[-1, -1, 0]], dtype=np.float32)
kernel_3 = np.array([[1, 0, 0],[0, 0, 0],[0, 0, -1]], dtype=np.float32)

embossed_img_1 = cv2.filter2D(gray_img, -1, kernel_1)
embossed_img_2 = cv2.filter2D(gray_img, -1, kernel_2) + 128
embossed_img_3 = cv2.filter2D(gray_img, -1, kernel_3) + 128

cv2.imshow("Original", img)
cv2.imshow("Embossed 1", embossed_img_1)
cv2.imshow("Embossed 2", embossed_img_2)
cv2.imshow("Embossed 3", embossed_img_3)

cv2.waitKey()