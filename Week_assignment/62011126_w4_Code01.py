import cv2
import numpy as np

img = cv2.imread("dataset/house.tif")

_,bw = cv2.threshold(img,100,255,cv2.THRESH_BINARY)

gra1 = cv2.morphologyEx(bw,cv2.MORPH_GRADIENT,np.ones((3,3),np.uint8),iterations = 1)
gra2 = cv2.morphologyEx(bw,cv2.MORPH_GRADIENT,np.ones((5,5),np.uint8),iterations = 1)
gra3 = cv2.morphologyEx(bw,cv2.MORPH_GRADIENT,np.ones((7,7),np.uint8),iterations = 1)
gra4 = cv2.morphologyEx(bw,cv2.MORPH_GRADIENT,np.ones((9,9),np.uint8),iterations = 1)

cv2.imshow("orginal",img)
cv2.imshow("3x3",gra1)
cv2.imshow("5x5",gra2)
cv2.imshow("7x7",gra3)
cv2.imshow("9x9",gra4)
cv2.waitKey(0)
cv2.destroyAllWindows()