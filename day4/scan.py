import cv2
import numpy as np
	
img=cv2.imread("test.jpg")
points=[]
def track_point(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),10,(255,0,0),-1)
        points.append([x,y])
def warp(point):
    rows,cols,_=img.shape
    pts1=np.float32([point[0],point[1],point[2],point[3]])
    pts2=np.float32([[0,0],[300,0],[300,300],[0,300]])
    M=cv2.getPerspectiveTransform(pts1,pts2)
    dst=cv2.warpPerspective(img,M,(300,300))
    cv2.imshow("result",dst)
    cv2.waitKey(2000)
	
cv2.namedWindow("image")
cv2.setMouseCallback('image',track_point)
while(1):
    cv2.imshow("image",img)
    if(len(points) == 4):
        warp(points)
        break
    if cv2.waitKey(20) & 0xFF == 27 :
        break
cv2.destroyAllWindows()
