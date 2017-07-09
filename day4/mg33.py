import cv2
import numpy as np
img=cv2.imread("test.png")
blur=cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("window",blur)
cv2.waitKey(0)
