import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        continue
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    try:
        face_rects = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=3)
    except cv2.error as e:
        print(str(e))
        break
    for x, y, w, h in face_rects:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,56,25), 3)

    cv2.imshow("Detect Face", frame)
    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()