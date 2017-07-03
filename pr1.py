import sys
import math
def inp(arg):
	ans=[]
	for x in arg:
		ans.append(math.factorial(int(x)))
	print(ans)
inp(sys.argv[1:])
