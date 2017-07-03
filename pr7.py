import sys
a=[]
b=[]
def inp(k):
	amnt=0;
	a=k[1: :2]
	b=k[0: :2]
	print(a)
	print(b)
	h=0
	for i in b:
		if(i=='d'):
			amnt=amnt+int(a[h])
		else:
			amnt=amnt-int(a[h])
		print(amnt)
		h+=1
	print(amnt)


inp(sys.argv[1:])


