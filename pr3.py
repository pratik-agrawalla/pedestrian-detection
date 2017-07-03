import sys
import numpy as np
def inp(k):
	x=int(k[0])
	y=int(k[1])
	a=np.zeros((x,y))
	for i in range(x):
		for j in range(y):
			a[i,j]=i*j
	print(a)
inp(sys.argv[1:])
		
