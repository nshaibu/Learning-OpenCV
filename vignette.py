import cv2
import numpy as np

img = cv2.imread("pic2.jpg")
img = cv2.resize(img, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_AREA)
rows, cols = img.shape[:2]

kernel_x = cv2.getGaussianKernel(cols, 200)
kernel_y = cv2.getGaussianKernel(rows, 200)
kernel = kernel_y * kernel_x.T
mask = 255 * kernel / np.linalg.norm(kernel)
output = np.copy(img)

for i in range(3):
    output[:,:,i] = output[:,:,i] * mask

cv2.imshow("Original", img)
cv2.imshow("Vignette", output)
cv2.waitKey()