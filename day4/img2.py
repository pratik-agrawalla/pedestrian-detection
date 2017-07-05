import cv2
img=cv2.imread("test.png",0)
ret,thrash=cv2.threshold(img,250,255,cv2.THRESH_BINARY_INV)
print ret
cv2.imshow("window",thrash)
cv2.waitKey(0)
