import cv2
import numpy as np

img = cv2.imread("dataset/flower.jpg")
print(img.shape)

rows,cols,ch = img.shape
#translation x=100px y=50px
M = np.float32([[1,0,100],[0,1,50]])

res =cv2.warpAffine(img,M,(cols,rows))

cv2.imshow("Original",img)
cv2.imshow("Result Image",res)
cv2.waitKey(0)
cv2.destroyAllWindows()