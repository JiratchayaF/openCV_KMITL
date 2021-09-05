import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("dataset/haarcascade_frontalface_default.xml")
img = cv2.imread("dataset/nasa.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=3,minSize=(15,15))

print("Detect {0} face".format(len(faces)))
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Face Detection",img)

cv2.waitKey(0)
cv2.destroyAllWindows()