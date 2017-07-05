import numpy as np
import matplotlib.pyplot as plt
img=plt.imread("messi.jpg")
y=np.dot(img,[0.299,0.587,0.114]).astype("uint8")
plt.imshow(y, cmap = 'gray')
plt.show()
