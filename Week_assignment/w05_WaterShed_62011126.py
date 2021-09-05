import cv2
import numpy as np
#BGR --> Gray --> opening --> distance transforms --> threshold --> marker
#watershed -> mapping --> show 
#6 step
#resize
img = cv2.resize(cv2.imread("dataset/watershed.jpg"),None,fx=0.8,fy=0.8)
kernel = np.ones((3,3),np.uint8)
#step1 convert to gray
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#step2 threshold
_,thres=cv2.threshold(gray,180,255,cv2.THRESH_BINARY_INV)
#step3 noise removal and dilate
closing=cv2.morphologyEx(thres,cv2.MORPH_CLOSE,np.ones((7,7),np.uint8),iterations=1)
opening=cv2.morphologyEx(closing,cv2.MORPH_OPEN,kernel,iterations=1)
#opening = cv2.morphologyEx(opening,cv2.MORPH_DILATE,kernel,iterations = 2)
#step4 distance transform
dist = cv2.distanceTransform(opening,cv2.DIST_L2,3)
dt=dist.copy()
cv2.normalize(dt,dt,0,255,cv2.NORM_MINMAX)
cv2.normalize(dist,dist,0,1.0,cv2.NORM_MINMAX)

distu = np.uint8(dt)
#step5 Threshold & Marker
_,thr_dt = cv2.threshold(distu,0.5*dt.max(),255,cv2.THRESH_BINARY)
mark_obj = cv2.subtract(opening,thr_dt)
_,marker_label = cv2.connectedComponents(thr_dt)
min_value,max_value,p1,p2 = cv2.minMaxLoc(marker_label)
print("NUM: ",max_value)

marker_label=marker_label+1

marker_label[mark_obj==255]=0

marker_show = (marker_label*20).astype('uint8')

#step6 water shed
marker_label=cv2.watershed(img,marker_label)
for x in range(2,15):
    img[marker_label==x]=[np.random.randint(0,256),np.random.randint(0,256),np.random.randint(0,256)]

cv2.imshow("threshold",thres)
cv2.imshow("closing",closing)
cv2.imshow("Dis Tran",dt)
cv2.imshow("Marker obj",mark_obj)
cv2.imshow("Marker lebel",marker_show)
cv2.imshow("original",img)

cv2.waitKey(0)
cv2.destroyAllWindows()