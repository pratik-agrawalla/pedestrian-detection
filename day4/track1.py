import cv2
import numpy as np
stat=0
x1,x2,y1,y2=0,0,0,0
hsv_low=np.array([0,50,50])
hsv_hgh=np.array([0,250,250])
cap = cv2.VideoCapture(0)
def hsv_update():
    global stat,frame
    tar=frame
    print(x1)
    print(x2)
    print(y1)
    print(y2)
    tar=tar[y1:y2,x1:x2,:]
    hsv = cv2.cvtColor(tar, cv2.COLOR_BGR2HSV)
    h=hsv[:,:,0:1]
    mean=np.mean(h)
    std=np.std(h)
    hsv_low[0]=mean-std
    hsv_hgh[0]=mean+std
    stat=1
	    
def track_color(event,x,y,flags,param):
    global x1,x2,y1,y2
    if event == cv2.EVENT_LBUTTONDOWN:
        print('butd')
        x1=x
        y1=y
    elif event == cv2.EVENT_LBUTTONUP:
        print('butu')
        x2=x
        y2=y
        #cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),-1)
        hsv_update()
	        
cv2.namedWindow("frame")
cv2.setMouseCallback('frame',track_color)

while(1):
    _,frame=cap.read()

    if stat == 1:
        mod=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask=cv2.inRange(mod,hsv_low,hsv_hgh)
        cv2.imshow('mask',mask)
	        
    elif stat == 0:
        cv2.imshow('frame',frame)
	        
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
       break
	
cv2.destroyAllWindows()
