a,b=input().split()
if a.isdigit() and b.isdigit():
	a=int(a)
	b=int(b)
	def ans():
		i=1
		e=10**b
		while(i<a):
			c=a*i
			i=i+1
			if c%a==0:
				if c%e==0:
					print(c)
					break
	def ans1():
		i=1
		e=10**b
		while(i<a):
			c=a*i
			i=i*10
			if c%a==0:
				if c%e==0:
					print(c)
					break
	if b<6:
		ans()
	else:
		ans1()
else:
	print("Invalid")
