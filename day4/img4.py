import cv2
import numpy as np
img=cv2.imread("messi1.jpg")
rows,col,channel=img.shape
channels=cv2.split(img)
arr=np.zeros_like(channels[0])
img=cv2.merge((channels[0],arr,arr))
img1=cv2.merge((arr,channels[1],arr))
img2=cv2.merge((arr,arr,channels[2]))
img3=cv2.imread("messi1.jpg",0)
img3 = cv2.merge((img3, img3, img3))
res=np.zeros_like(img)
res[:rows/2,:col/2]=img[:rows/2,:col/2]
res[:rows/2,col/2:col]=img1[:rows/2,col/2:col]
res[rows/2:rows,:col/2]=img2[rows/2:rows,:col/2]
res[rows/2:rows,col/2:col]=img3[rows/2:rows,col/2:col]
cv2.imshow("window",res)
cv2.waitKey(0)


