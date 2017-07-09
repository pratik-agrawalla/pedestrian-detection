import cv2
import numpy as np
import sys
import matplotlib.pyplot as pl
a=sys.argv[1:]
img=cv2.imread("messi1.jpg",0)
cv2.imshow("window",img)
min_=np.amin(img)
max_=np.amax(img)
img=img[:,:]-min_
img=img*((int(a[1])-int(a[0]))/float(max_-min_))
img=img+int(a[0])
print(img.dtype)
cv2.imshow("window1",np.array(img))
cv2.waitKey(0)
pl.hist(img)
pl.show()


