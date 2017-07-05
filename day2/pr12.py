import numpy as np
import matplotlib.pyplot as plt
x=[]
y=[]
with open("dat1.txt")as filename:
        for line in filename:
                x.append(line.split()[0])
                y.append(line.split()[1])
n=len(x)
x=np.float32(x)
y=np.float32(y)
xsum=np.sum(x)
ysum=np.sum(y)
xsqsum=np.sum(np.square(x))
xpro=np.inner(x,y)
mat=np.array(([n,xsum],[xsum,xsqsum]))
mat=np.linalg.inv(mat)
mat1=np.array(([ysum],[xpro]))
ans=np.matmul(mat,mat1)
print(ans[0])
print(ans[1])
ypre=ans[0]+ans[1]*x
plt.plot(x,ypre)
plt.plot(x,y,'ro')
plt.show()

