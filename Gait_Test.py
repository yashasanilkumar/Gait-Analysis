import cv2
import numpy as np 

cap = cv2.VideoCapture('male-runner.avi')
no_of_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    GG_frame = cv2.GaussianBlur(frame, (5,5), 0)
    TGG_frame = cv2.threshold(GG_frame, 45, 255, cv2.THRESH_BINARY)[1]
    #TGG_frame = cv2.erode(TGG_frame, None, iterations = 2)
    #TGG_frame = cv2.dilate(TGG_frame, None, iterations = 2)
    cv2.imshow('Tgg', TGG_frame)

cap.release()
cv2.destroyAllWindows()
    
    
    
    