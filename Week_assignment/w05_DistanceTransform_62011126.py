import cv2
import numpy as np

img = cv2.imread("dataset/coin2.jpg",0)
kernel = np.ones((4,4),np.uint8)

#threshold
_,thres = cv2.threshold(img,80,255,cv2.THRESH_BINARY)
#closing
CLOSE = cv2.morphologyEx(thres,cv2.MORPH_CLOSE,kernel,iterations = 3)
#applied distance transform
dt = cv2.distanceTransform(CLOSE,cv2.DIST_L2,5)
#normalize the distance image for range 0.0 to 1.0
cv2.normalize(dt,dt,0,1.0,cv2.NORM_MINMAX)

cv2.imshow("original",img)
cv2.imshow("thres",CLOSE)
cv2.imshow("Distance result",dt)
cv2.waitKey(0)
cv2.destroyAllWindows()