import cv2

cap = cv2.VideoCapture(0)
if cap.isOpened():
    print("Error: Failed opening cam!")

curr_mode = None
output = None

while True:
    ret, frame = cap.read()
    if not ret:
        continue
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    c = cv2.waitKey(1)
    if c != -1 and c != 255 and c != curr_mode:
        curr_mode = c

    if curr_mode == ord('g'):
        output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif curr_mode == ord('y'):
        output = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    elif curr_mode == ord('h'):
        output = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    else:
        output = frame
    
    cv2.imshow("Output", output)

cap.release()
cv2.destroyAllWindows()