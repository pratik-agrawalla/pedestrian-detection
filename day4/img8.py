import cv2
import numpy as np
img=cv2.imread("messi1.jpg")
rows,col,channel=img.shape
m=np.float32([[1,0,100],[0,1,50]])
dat=cv2.warpAffine(img,m,(col,rows))
cv2.imshow("image",dat)
cv2.waitKey(0)
