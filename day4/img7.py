import cv2
import numpy as np
img=cv2.imread("messi1.jpg")
res=cv2.resize(img,(100,100))
cv2.imshow("window",res)
cv2.waitKey(0)
