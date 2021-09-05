import cv2
import numpy as np

img = cv2.imread("dataset/coins.jpg")
kernel = np.ones((3,3),np.uint8)

_,bw = cv2.threshold(img,40,255,cv2.THRESH_BINARY)
open1 = cv2.morphologyEx(bw,cv2.MORPH_OPEN,kernel)
CLOSE = cv2.morphologyEx(open1,cv2.MORPH_CLOSE,kernel,iterations = 2)

cv2.imshow("original",img)
cv2.imshow("OPEN",open1)
cv2.imshow("CLOSE",CLOSE)
cv2.waitKey(0)
cv2.destroyAllWindows()


