import cv2
import numpy as np

img = cv2.imread("dataset/flower.jpg")
rows,cols,ch = img.shape

#scale x=0.5 y=0.5
M = np.float32([[0.8,0,0],[0,0.8,0]])
res =cv2.warpAffine(img,M,(cols,rows))

cv2.imshow("Result Image",res)
cv2.waitKey(0)
cv2.destroyAllWindows()