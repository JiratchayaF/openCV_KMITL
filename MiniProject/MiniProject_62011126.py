import cv2
import numpy as np
#pic1
cap = cv2.VideoCapture('newset/book.MOV')
#pic2
#cap = cv2.VideoCapture('newset/forkSpoon.MOV')
#pic3
#cap = cv2.VideoCapture('newset/guitar.MOV')
#pic4
#cap = cv2.VideoCapture('newset/glass.MOV')
#pic5
#cap = cv2.VideoCapture('newset/test.MOV')
kernel = np.ones((3,3),np.uint8)
sigma = 3.2
ksize = 5
ker_gaux = cv2.getGaussianKernel(ksize,sigma)
ker_gauy = np.transpose(ker_gaux)
ker_gau = ker_gaux*ker_gauy
while(cap.isOpened()):
    ret,frame=cap.read()
    ori = frame.copy()
    gua = cv2.filter2D(frame,0,ker_gau)
    gray = cv2.cvtColor(gua,cv2.COLOR_BGR2GRAY)
    #pic1
    ret, thres = cv2.threshold(gray,80,255,cv2.THRESH_BINARY_INV)
    close = cv2.morphologyEx(thres,cv2.MORPH_CLOSE,kernel,iterations = 9)
    opening = cv2.morphologyEx(close,cv2.MORPH_OPEN,kernel,iterations = 3)
    contours,_ = cv2.findContours(opening.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    #pic2
    #ret, thres = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
    #close = cv2.morphologyEx(thres,cv2.MORPH_CLOSE,kernel,iterations = 1)
    #opening = cv2.morphologyEx(close,cv2.MORPH_OPEN,kernel,iterations = 8)
    #contours,_ = cv2.findContours(opening.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
    #pic3
    #ret, thres = cv2.threshold(gray,125,255,cv2.THRESH_BINARY_INV)
    #close = cv2.morphologyEx(thres,cv2.MORPH_CLOSE,kernel,iterations = 15)
    #opening = cv2.morphologyEx(close,cv2.MORPH_OPEN,kernel,iterations = 10)
    #contours,_ = cv2.findContours(opening.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    #pic4
    #ret, thres = cv2.threshold(gray,92,255,cv2.THRESH_BINARY_INV)
    #close = cv2.morphologyEx(thres,cv2.MORPH_CLOSE,kernel,iterations = 25)
    #opening = cv2.morphologyEx(close,cv2.MORPH_OPEN,kernel,iterations = 2)
    #contours,_ = cv2.findContours(opening.copy(),cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
    
    #pic5
    #ret, thres = cv2.threshold(gray,95,255,cv2.THRESH_BINARY_INV)
    #close = cv2.morphologyEx(thres,cv2.MORPH_CLOSE,kernel,iterations = 15)
    #opening = cv2.morphologyEx(close,cv2.MORPH_OPEN,kernel,iterations = 1)
    #contours,_ = cv2.findContours(opening.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
   
    for i in range(len(contours)):
        cv2.drawContours(frame,contours,i,(255,0,0),6)
    cv2.imshow("Original",ori)
    cv2.imshow("Gaussian",gua)
    cv2.imshow("gray",gray)
    cv2.imshow("thres",thres)
    cv2.imshow("close",close)
    cv2.imshow("open",opening)
    cv2.imshow("Contour",frame)
    k = cv2.waitKey(10) & 0xFF
    if k == 27: #press ESC to quit
        break

cap.release()
cv2.destroyAllWindows()