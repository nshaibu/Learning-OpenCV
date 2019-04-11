import cv2
import numpy as np

dragging = False
x_initial, y_initial = (0, 0)
selected_area_coord = {"top_left_coord":(0, 0), "bottom_right_coord":(0, 0)}

def select_area(event, x, y, flags, params):
    global x_initial, y_initial, dragging
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Down")
        dragging = True
        x_initial, y_initial = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        print("Move")
        dragging = True
        params['top_left_coord'] = (min(x_initial, x), min(y_initial, y))
        params['bottom_right_coord'] = (max(x_initial, y), max(y_initial, y))
    elif event == cv2.EVENT_LBUTTONUP:
        print("Up")
        dragging = False

cv2.namedWindow("webcam")
cv2.setMouseCallback("webcam", select_area, selected_area_coord)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Failed opening cam!")

while True:
    ret, frame = cap.read()
    if not ret:
        continue
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    
    if dragging:
        (x0, y0), (x1, y1) = selected_area_coord['top_left_coord'], selected_area_coord["bottom_right_coord"]
        frame[y0:y1, x0:x1] = 255 - frame[y0:y1, x0:x1]

    cv2.imshow("webcam", frame)
    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()