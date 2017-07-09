import cv2
import numpy as np
import matplotlib.pyplot as pltS
img=cv2.imread("test.png",0)
ret,thrash=cv2.threshold(img,250,255,cv2.THRESH_BINARY_INV)
image,contours,heirachy=cv2.findContours(thrash,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
k=0
h=[]
for i in range(0,(len(contours))):
	img1=cv2.drawContours(img,contours,i,(0,255,0),3)
	corners=cv2.goodFeaturesToTrack(img1,20,0.5,10)
	corners=np.int0(corners)
	j=len(corners)-k
	print(j)
	h.append(j)
	k=len(corners)
j=0
r=[]
t=[]
for i in h:
	for m in range(j,(j+i)):
		r.append(corners[m])
	j=i
	t.append(r)
	r=[]
for i in range(len(t)):
	print(t[i])

		
	
	


