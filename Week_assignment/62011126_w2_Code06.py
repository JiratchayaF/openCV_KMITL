import cv2
import numpy as np

img = cv2.imread("dataset/graylevel.jpg")

kerGx = np.array([[1,0,-1],
                 [ 1,0,-1],
                 [ 1,0,-1]])
kerGy = np.array([[1, 1, 1],
                 [ 0, 0, 0],
                 [-1,-1,-1]])

ret,thres1 = cv2.threshold(img,100,255,cv2.THRESH_TOZERO)
ret,thres2 = cv2.threshold(thres1,200,255,cv2.THRESH_TOZERO_INV)
ret,thres3 = cv2.threshold(thres2,0,255,cv2.THRESH_BINARY)
kerSoGx = cv2.Sobel(thres3,0,2,0,ksize=3)
kerSoGy = cv2.Sobel(thres3,0,0,2,ksize=3)

resSobel = np.absolute(kerSoGx) + np.absolute(kerSoGy)

cv2.imshow("Original", img)
cv2.imshow("THRESH_TOZERO",thres1)
cv2.imshow("THRESH_TOZERO_INV",thres2)
cv2.imshow("THRESH_BINARY",thres3)
cv2.imshow("Sobel",resSobel)
cv2.waitKey(0)
cv2.destroyAllWindows()