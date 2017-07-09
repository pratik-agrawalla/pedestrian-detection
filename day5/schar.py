import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi1.jpg',0)
scharrx=cv2.Scharr(img,cv2.CV_64F,0,1)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(scharrx,cmap = 'gray')
plt.title('schar x'), plt.xticks([]), plt.yticks([])
plt.show()
