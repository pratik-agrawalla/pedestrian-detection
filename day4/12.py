import cv2
import numpy as np
import matplotlib.pyplot as pl
img=cv2.imread("test.png")
red=img[:,:,1]
pl.hist(red)
pl.show()
