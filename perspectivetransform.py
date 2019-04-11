import cv2
import numpy as np

img = cv2.imread("pic1.jpg", cv2.IMREAD_COLOR)
img_scaled = cv2.resize(img, None, fx=0.7, fy=0.7, interpolation=cv2.INTER_AREA)
rows, cols = img_scaled.shape[:2]
src_points = np.float32([[0, 0], [cols-1, 0], [0, rows-1], [cols-1, rows-1]])
dst_points = np.array([[0, 0], [cols-1, 0], [0.33*(cols-1), rows-1], [0.66*(cols-1), rows-1]], dtype=np.float32)
perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
translated_img = cv2.warpPerspective(img_scaled, perspective_matrix, (cols, rows))
cv2.imshow("Perspective transform", translated_img)
cv2.waitKey(9000)