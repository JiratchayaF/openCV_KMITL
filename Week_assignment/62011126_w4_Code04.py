import cv2
import numpy as np

img = cv2.imread("dataset/sudoku.jpg")
#Hough Line
canny = cv2.Canny(img,threshold1 = 50,threshold2 = 100)
line = cv2.HoughLinesP(canny,1,np.pi/270,140,minLineLength=150,maxLineGap=150)
print(len(line))
for i in range(len(line)):
    for x1,y1,x2,y2 in line[i]:
        cv2.line(img,(x1,y1),(x2,y2),(40,200,80),thickness=3)
#perspective
#rows,cols = img.shape
w = 300
h = 300
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
M = cv2.getPerspectiveTransform(pts1,pts2)
result =cv2.warpPerspective(img,M,(300,300))
#canny
can = cv2.Canny(result,threshold1 = 40,threshold2 = 100)
#closing
kernel = np.ones((3,3),np.uint8)
close = cv2.morphologyEx(can,cv2.MORPH_CLOSE,kernel,iterations = 1)
#Hough Line
cv2.imshow("Canny",can)
cv2.imshow("Closing",close)
cv2.imshow("Final result",result)
cv2.waitKey(0)
cv2.destroyAllWindows()