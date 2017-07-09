import cv2
import numpy as np
img=cv2.imread("test.png")
kernel=np.ones((5,5),np.float32)/25
br=cv2.filter2D(img,-1,kernel)
cv2.imshow("window",br)
cv2.waitKey(0)
