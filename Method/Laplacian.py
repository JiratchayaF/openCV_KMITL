import cv2
import numpy as np

img = cv2.imread("dataset/butterfly.jpg")

sharpen = np.array([[0,-1,0],
              [-1,5,-1],
              [0,-1, 0]])
res = cv2.filter2D(img,0,sharpen)

ker = [[0,1,0],
    [1,-4,1],
    [0,1,0]]

resul = cv2.filter2D(np.uint8(res),0,np.uint8(ker))
result = cv2.Laplacian(resul,0,ksize=3)
print(result)
cv2.imshow("Original",img)
cv2.imshow("Result",result)
cv2.waitKey(0)
cv2.destroyAllWindows()