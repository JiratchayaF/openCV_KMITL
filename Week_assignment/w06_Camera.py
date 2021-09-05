import cv2
import numpy as np

capture = cv2.VideoCapture(0) #index = 0

while True:
    ret, img = cap.read()

    cv2.imshow("Camera capture",img)
    k = cv2.waitKey(30) & 0xFF
    if k == 27: #press ESC to quit
        break

cap.release()
cv2.destroyAllWindow()