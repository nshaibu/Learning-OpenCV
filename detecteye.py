import cv2
import numpy as np
import matplotlib.pyplot as plt

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_smile.xml')
full_body_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_upperbody.xml')

cap = cv2.VideoCapture(0)
plt.ion()

while True:
    ret, frame = cap.read()

    if not ret:
        continue
    frame = cv2.resize(frame, None, fx=0.7, fy=0.7, interpolation=cv2.INTER_AREA)
    #frame = cv2.medianBlur(frame, 7)
    #frame = cv2.GaussianBlur(frame, (13, 13) , 0)
    frame = cv2.bilateralFilter(frame, 7, 70, 50)
    areaOfInterest = np.ones(frame.shape, dtype=np.uint8)

    faces = face_cascade.detectMultiScale(frame, 1.3, 3)
    full_body = full_body_cascade.detectMultiScale(frame, 1.3, 3)

    for x, y, w, h in full_body:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 34), 3)

    for x, y, w, h  in faces:
        face_roi = frame[y:y+h, x:x+w]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,56,25), 3)
        eyes = eye_cascade.detectMultiScale(face_roi, scaleFactor=1.3, minNeighbors=13)
        for eye_x, eye_y, eye_w, eye_h in eyes:
            center = (eye_x + int(0.5 * eye_w), eye_y + int(0.5 * eye_h))
            radius = int(0.5 * eye_h)
            cv2.circle(face_roi, center, radius, (0, 67, 255), 3)

        smile = smile_cascade.detectMultiScale(face_roi, scaleFactor=1.3, minNeighbors=20)
        for smile_x, smile_y, smile_w, smile_h in smile:
            cv2.rectangle(face_roi, (smile_x, smile_y), (smile_x+smile_w, smile_y+smile_h), (255, 12, 128), 3)
        
        frame[y:y+h, x:x+w] = face_roi
        areaOfInterest[y:y+h, x:x+h] = face_roi
    #plt.hist(frame.ravel(), 128)
    cv2.imshow("Area Of Interest", areaOfInterest)
    cv2.imshow("Detect Eyes", frame)
    c = cv2.waitKey(1)
    if c == 27:
        break
    #plt.draw()

cap.release()
cv2.destroyAllWindows()