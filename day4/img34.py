import cv2
import numpy as np
import matplotlib.pyplot as pl
img=cv2.imread("messi1.jpg")
img=img[:,:,1]
pl.hist(img)
pl.show()
