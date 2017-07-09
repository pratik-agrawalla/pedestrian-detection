import cv2
import numpy as np

img = cv2.imread('img3.jpg')
copy=img.copy()
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(copy,(i[0],i[1]),i[2],(0,255,0),2)
    

cv2.imshow('detected circles',copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
