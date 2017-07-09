import cv2
import numpy as np
img=cv2.imread("test.png")
kernel=np.array(([0,-1,0],[-1,4,-1],[0,-1,0]))
br=cv2.filter2D(img,-1,kernel)
cv2.imshow("window",br)
cv2.waitKey(0)
