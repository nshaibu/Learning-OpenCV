import cv2
import numpy as np

img = cv2.imread("pic1.jpg", cv2.IMREAD_COLOR)
kernel = np.ones((3, 3), dtype=np.float32)
kernel[1, 1] = -7
sharpened_img = cv2.filter2D(img, -1, kernel)
cv2.imshow("sharpened", sharpened_img)
cv2.waitKey(10000)