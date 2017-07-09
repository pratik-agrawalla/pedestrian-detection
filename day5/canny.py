import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img1.jpg',0)
edges = cv2.Canny(img,100,200)
laplacian=cv2.Laplacian(img,cv2.CV_64F)
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobelx=np.absolute(sobelx)
sobelx=np.uint8(sobelx)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
plt.subplot(122),plt.imshow(sobelx,cmap = 'gray')
plt.title('sobel x'), plt.xticks([]), plt.yticks([])
plt.show()
plt.subplot(122),plt.imshow(sobely,cmap = 'gray')
plt.title('sobel y'), plt.xticks([]), plt.yticks([])
plt.show()
