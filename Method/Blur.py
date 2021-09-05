import cv2
import numpy as np

img = cv2.imread("dataset/flower.jpg")

ksize_1 = 5
ker_x1 = [np.ones(5)]
ker_y1 = np.transpose(ker_x1)
ker_blur1 = ker_y1*ker_x1
ker_blur1 = np.uint8(ker_blur1)/(ksize_1*ksize_1)

ksize_2 = 9
ker_x2 = [np.ones(9)]
ker_y2 = np.transpose(ker_x2)
ker_blur2 = ker_y2*ker_x2
ker_blur2 = np.uint8(ker_blur2)/(ksize_2*ksize_2)

ksize_3 = 15
ker_x3 = [np.ones(15)]
ker_y3 = np.transpose(ker_x3)
ker_blur3 = ker_y3*ker_x3
ker_blur3 = np.uint8(ker_blur3)/(ksize_3*ksize_3)

ksize_4 = 25
ker_x4 = [np.ones(25)]
ker_y4 = np.transpose(ker_x4)
ker_blur4 = ker_y4*ker_x4
ker_blur4 = np.uint8(ker_blur4)/(ksize_4*ksize_4)

print(ker_blur1)
print(ker_blur2)
print(ker_blur3)
print(ker_blur4)
res1 = cv2.filter2D(img,0,ker_blur1)
res2 = cv2.filter2D(img,0,ker_blur2)
res3 = cv2.filter2D(img,0,ker_blur3)
res4 = cv2.filter2D(img,0,ker_blur4)

cv2.imshow("Original", img)
cv2.imshow("No.1",res1)
cv2.imshow("No.2",res2)
cv2.imshow("No.3",res3)
cv2.imshow("No.4",res4)
cv2.waitKey(0)
cv2.destroyAllWindows()