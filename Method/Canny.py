import cv2
import numpy as np

img = cv2.resize(cv2.imread("dataset/flower.jpg"),None,fx=0.5,fy=0.5)

hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
mask = cv2.inRange(hsv,np.array([120,50,50]),np.array([150,255,255]))
res = cv2.bitwise_and(img,img,mask=mask)
ret,thres = cv2.threshold(mask,0,255,cv2.THRESH_BINARY)
resCan = cv2.Canny(thres,threshold1=50,threshold2=150)

cv2.imshow("Original img",img)
cv2.imshow("Result img",res)
cv2.imshow("Threshold image",thres)
cv2.imshow("Canny",resCan)
cv2.waitKey(0)
cv2.destroyAllWindows()