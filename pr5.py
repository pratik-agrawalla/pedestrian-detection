import sys
def inp(k):
	h=0
	ans=[]
	for i in k:
		for j in range(int(i)+1):
			h=h+(float(j)/float(j+1))
		ans.append(h)
	print(ans)
inp(sys.argv[1:])
