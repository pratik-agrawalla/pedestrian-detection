import cv2
import numpy as np
angles=[]
img = cv2.imread('ps1-input1.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

lines = cv2.HoughLines(edges,1,np.pi/180,140)
print(len(lines))
for x in lines:
    print(x)
    rho,theta=x[0]
    degrre=57.2958*theta
    if degrre>90:
	eff_deg=90-degrre
    else:
	eff_deg=degrre-90
    angles.append(eff_deg)
ang=np.mean(angles)
rows,cols,_= img.shape
M = cv2.getRotationMatrix2D((cols/2,rows/2),ang,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('houghlines3.jpg',dst)
cv2.imshow("cnny",edges)
cv2.waitKey(0)
