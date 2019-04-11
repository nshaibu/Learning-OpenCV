import cv2

gray_img = cv2.imread("pic1.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("output.png", gray_img, [cv2.IMWRITE_PNG_COMPRESSION])