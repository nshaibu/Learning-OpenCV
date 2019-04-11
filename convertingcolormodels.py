import cv2

img = cv2.imread("pic1.jpg", cv2.IMREAD_COLOR)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray_img)
cv2.waitKey(6000)