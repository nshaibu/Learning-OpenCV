import cv2
import numpy as np 

img = cv2.imread("pic1.jpg", cv2.IMREAD_COLOR)
img_scaled = cv2.resize(img, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_AREA)
rows, cols = img_scaled.shape[:2]

src_points = np.array([[0, 0], [cols-1, 0], [0, rows-1]], dtype=np.float32)
dst_points = np.array([[cols-1, 0], [0, 0], [cols-1, rows-1]], dtype=np.float32)
affine_matrix = cv2.getAffineTransform(src_points, dst_points)
translated_img = cv2.warpAffine(img_scaled, affine_matrix, (cols, rows), cv2.INTER_AREA)
cv2.imshow("original", img_scaled)
cv2.imshow("mirror", translated_img)
cv2.waitKey(9000)