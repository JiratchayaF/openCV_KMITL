import cv2
import numpy as np

img = cv2.imread("dataset/flower.jpg")
print(img.shape)
rows,cols,ch = img.shape

#rotation
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1) #90 deg
N = cv2.getRotationMatrix2D((cols/2,rows/2),45,1) #45 deg
res =cv2.warpAffine(img,M,(cols,rows))
Nres =cv2.warpAffine(img,N,(cols,rows))
print(M)
cv2.imshow("Original Image",img)
cv2.imshow("Result Image",res)
cv2.imshow("Result Image2",Nres)
cv2.waitKey(0)
cv2.destroyAllWindows()