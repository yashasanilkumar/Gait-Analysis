import cv2
import numpy as np 
import imutils

cap = cv2.VideoCapture('man_walk.mp4')
no_of_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

while cap.isOpened():
    ret, frame = cap.read()
    #CONVERT TO GRAYSCALE
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #GAUSSIAN BLUR FOR CLEAR CONTOURS
    frame = cv2.GaussianBlur(frame, (5, 5), 0)

    #THRESHOLD TO BINARY IMAGE TO REMOVE ALL COLORS
    frame = cv2.threshold(frame, 45, 255, cv2.THRESH_BINARY)

    #FINDING THE CONTOURS
    frame, contours, heirarchy = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if imutils.is_cv2() else contours[1]
    c = max(contours, key = cv2.contourArea)

    #GET TOP AND BOTTOM POINTS
    face = tuple(c[c[:, :, 1].argmin()][0])
    foot = tuple(c[c[:, :, 1].argmax()][0])

    #DRAWING CONTOURS AND ENCLOSING FACE, FEET
    cv2.drawContours(frame, [c], -1, (0, 255, 255), 3)
    cv2.circle(frame, face, 8, (0, 255, 255), -1)
    cv2.cirlce(frame, bottom, 8, (0, 255, 255), -1)

    #DISPLAY IMAGE
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()
cv2.destroyAllWindows()
