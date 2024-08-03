from ultralytics import YOLO
import cv2
import numpy as np
import cvzone


cap = cv2.VideoCapture('test.mp4')

while True:
    rt,frame = cap.read()

    # resize video here 
    frame = cv2.resize(frame,(640,480))


    cv2.imshow('frame',frame)
    cv2.waitKey(1) # 1 because 