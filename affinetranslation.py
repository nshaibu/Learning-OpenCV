import cv2
import numpy as np 

img = cv2.imread("pic1.jpg", cv2.IMREAD_COLOR)
num_rows, num_cols = img.shape[:2]
translation_matrix = np.float32([[1, 0, 30], [0, 1, 30]])
translated_img = cv2.warpAffine(img, translation_matrix, (num_cols+60, num_rows+60), 
                                cv2.INTER_LINEAR, cv2.BORDER_WRAP, 1)
cv2.imshow("Translation", translated_img)
cv2.waitKey(8000)