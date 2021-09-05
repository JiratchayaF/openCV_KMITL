import cv2
import numpy as np

img = cv2.imread("dataset/flower.jpg")

sigma1 = 1.4
sigma2 = 3.2
ksize = 5
ksize2 = 7
ker_gaux1 = cv2.getGaussianKernel(ksize,sigma1)
ker_gauy1 = np.transpose(ker_gaux1)

ker_gaux2 = cv2.getGaussianKernel(ksize,sigma2)
ker_gauy2 = np.transpose(ker_gaux2)

ker_gaux3 = cv2.getGaussianKernel(ksize2,sigma1)
ker_gauy3 = np.transpose(ker_gaux3)

ker_gaux4 = cv2.getGaussianKernel(ksize2,sigma2)
ker_gauy4 = np.transpose(ker_gaux4)

ker_gau1 = ker_gaux1*ker_gauy1
ker_gau2 = ker_gaux2*ker_gauy2
ker_gau3 = ker_gaux3*ker_gauy3
ker_gau4 = ker_gaux4*ker_gauy4
print(ker_gau1)
print(ker_gau2)
print(ker_gau3)
print(ker_gau4)

res1 = cv2.filter2D(img,0,ker_gau1)
res2 = cv2.filter2D(img,0,ker_gau2)
res3 = cv2.filter2D(img,0,ker_gau3)
res4 = cv2.filter2D(img,0,ker_gau4)

cv2.imshow("Original", img)
cv2.imshow("No.1",res1)
cv2.imshow("No.2",res2)
cv2.imshow("No.3",res3)
cv2.imshow("No.4",res4)
cv2.waitKey(0)
cv2.destroyAllWindows()