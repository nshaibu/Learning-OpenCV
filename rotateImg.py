import cv2
import numpy as np 

img = cv2.imread("pic1.jpg", cv2.IMREAD_COLOR)
img_scaled = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

rotation_matrix = cv2.getRotationMatrix2D((img_scaled.shape[0]/2, img_scaled.shape[1]/2), 40, 0.8)
translation_img = cv2.warpAffine(img_scaled, rotation_matrix, (img_scaled.shape[1], img_scaled.shape[0]), cv2.INTER_LINEAR)
cv2.imshow("Rotation", translation_img)
cv2.waitKey(8000)