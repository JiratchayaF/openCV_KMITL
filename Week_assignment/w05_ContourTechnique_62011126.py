import cv2
import numpy as np

img = cv2.resize(cv2.imread("dataset/colorobject.png"),None,fx=0.7,fy=0.7)
mask = cv2.inRange(img,np.array([0,0,255]),np.array([0,0,255]))
res = cv2.bitwise_and(img,img,mask=mask)
gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
_,thres = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)

#find contour
contours,_ = cv2.findContours(thres,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for i in range(len(contours)):
    cv2.drawContours(img,contours,i,(255,255,255),3)

cv2.imshow("GRAY",gray)
cv2.imshow("Threshold",thres)
cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()