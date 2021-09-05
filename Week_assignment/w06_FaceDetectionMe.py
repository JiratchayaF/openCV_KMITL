import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("dataset/haarcascade_frontalface_default.xml")

cap =cv2.VideoCapture('dataset/book.MOV')

while(cap.isOpened()):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=6,minSize=(15,15))
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Face Detection",frame)
    k = cv2.waitKey(10) & 0xFF
    if k == 27: #press ESC to quit
        break

cap.release()
cv2.destroyAllWindow()
