import cv2
import numpy as np

w, h = 640, 480
img = 255 * np.ones((w, h, 3), dtype=np.uint8)

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        if x > w/2:
            if y > h/2:
                top_coord = (int(w/2), int(h/2))
                bottom_coord = (w-1, h-1)
            else:
                top_coord = (int(w/2), 0)
                bottom_coord = (w, int(h/2))
        else:
            if y > h/2:
                top_coord = (0, int(h/2))
                bottom_coord = (int(w/2), h-1)
            else:
                top_coord = (0, 0)
                bottom_coord = (int(w/2), int(h/2))

        cv2.rectangle(param['img'], (0, 0), (w-1, h-1), (255, 255, 255), -1)

        cv2.rectangle(param['img'], top_coord, bottom_coord, (255, 0, 65), -1)

cv2.namedWindow("Input Window")
cv2.setMouseCallback("Input Window", onMouse, {"img": img})

while True:
    cv2.imshow("Input Window", img)
    c = cv2.waitKey(1)
    if c == 27:
        break