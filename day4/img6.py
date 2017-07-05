import cv2
import numpy as np
img=cv2.imread("messi1.jpg")
rows,col,channel=img.shape
def draw_circle(event,x,y,flags,param):
	if event==cv2.EVENT_LBUTTONDBLCLK:
		if (x<col/2 and y<rows/2):
			cv2.circle(img,(x,y),100,(255,0,0),-1)
		elif(x>col/2 and y<rows/2):
			cv2.circle(img,(x,y),100,(0,255,0),-1)
			
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
	cv2.imshow('image',img)
	if cv2.waitKey(20) & 0xFF ==27:
		break
cv2.destroyAllWIndows()
