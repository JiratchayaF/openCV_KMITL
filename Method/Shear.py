import cv2
import numpy as np

img = cv2.imread("dataset/rectangle2.png")
print(img.shape)
rows,cols,ch = img.shape
#shear transformation
#shear x
degree = 30
theta = np.tan(np.deg2rad(degree))
M = np.float32([[1,theta,0],[0,1,0]])

print(M)

res =cv2.warpAffine(img,M,(cols,rows))
cv2.imshow("Original Image",img)
cv2.imshow("Result Image",res)
cv2.waitKey(0)
cv2.destroyAllWindows()