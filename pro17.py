n,k=input().split()
if n.isdigit() and k.isdigit():
	n=int(n)
	k=int(k)
	c=input().split()
	s=0
	def add():
		h=0
		for i in range(0,n):
			x=int(c[i])
			for j in range(0,n):
				if(i==j):
					continue
				else:
					w=x+int(c[j])
					if w==k:
						h=h+1
		if h>0:
			print("yes")
		else:
			print("no")
	for i in range(0,len(c)):
		if c[i].isdigit():
			s=s+1
	if len(c)==n:
		if s==n:
			add()
	elif n>len(c):
		n=len(c)
		if s==n:
			add()
	else:
		add()
else:
	print ("Invalid")
