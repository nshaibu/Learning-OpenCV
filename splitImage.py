import cv2

img = cv2.imread("pic1.jpg", cv2.IMREAD_COLOR)
yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
y, u, v = cv2.split(yuv_img)
cv2.imshow("Y channel", y)
cv2.imshow("U channel", u)
cv2.imshow("V channel", v)
cv2.imshow("Image", yuv_img)

print("MERGING CHANNELS")
bgr_img = cv2.cvtColor(yuv_img, cv2.COLOR_YUV2BGR)
b, g, r = cv2.split(bgr_img)
cv2.imshow("B channel", b)
cv2.imshow("G channel", g)
cv2.imshow("R channel", r)
cv2.imshow("rbr merge", cv2.merge((r, b, r)))
cv2.waitKey(80000)