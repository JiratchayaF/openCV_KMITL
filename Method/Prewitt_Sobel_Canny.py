import cv2
import numpy as np

img = cv2.resize(cv2.imread("dataset/bikesgray.jpg"),None,fx=0.7,fy=0.7)

kerGx = np.array([[1,0,-1],
                 [ 1,0,-1],
                 [ 1,0,-1]])
kerGy = np.array([[1, 1, 1],
                 [ 0, 0, 0],
                 [-1,-1,-1]])

kerSoGx = cv2.Sobel(img,0,1,0,ksize=3)
kerSoGy = cv2.Sobel(img,0,0,1,ksize=3)

resGx = cv2.filter2D(img,0,kerGx)
resGy = cv2.filter2D(img,0,kerGy)

resPrewitt = np.absolute(resGx) + np.absolute(resGy)
resSobel = np.absolute(kerSoGx) + np.absolute(kerSoGy)
resCanny = cv2.Canny(img,threshold1=100,threshold2=250)
cv2.imshow("Original",img)
cv2.imshow("Prewitt",resPrewitt)
cv2.imshow("Sobel",resSobel)
cv2.imshow("Canny",resCanny)
cv2.waitKey(0)
cv2.destroyAllWindows()