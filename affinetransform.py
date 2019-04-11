import cv2
import numpy as np 

img = cv2.imread("pic1.jpg", cv2.IMREAD_COLOR)
img_scaled = cv2.resize(img, None, fx=0.7, fy=0.7, interpolation=cv2.INTER_AREA)
rows, cols = img_scaled.shape[:2]

src_points = np.array([[0, 0], [cols-1, 0], [0, rows-1]], dtype=np.float32)
dst_points = np.array([[0, 0], [0.6*(cols-1), 0], [0.4*(cols-1), rows-1]], dtype=np.float32)
affine_matrix = cv2.getAffineTransform(src_points, dst_points)
translated_img = cv2.warpAffine(img_scaled, affine_matrix, (cols, rows))
cv2.imshow("Show", translated_img)
cv2.waitKey(8000)