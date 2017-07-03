for i in range(1000,3000):
	k=i%10
	m=i/10
	r=m%10
	l=m/10
	s=l%10
	p=l/10
	if(k%2==0 and r%2==0 and s%2==0 and p%2==0):
		print (', %d'%i)

