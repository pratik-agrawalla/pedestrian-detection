import cv2
import numpy as np

img = cv2.imread('new.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

lines = cv2.HoughLines(edges,1,np.pi/180,280)
print(len(lines))
for x in lines:
    print(x)
    rho,theta=x[0]
    degrre=57.2958*theta
    print(degrre)
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('houghlines3.jpg',img)
cv2.imshow("cnny",edges)
cv2.waitKey(0)
