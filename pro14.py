n,q=input().split()
if n.isdigit() and q.isdigit():
	n=int(n)
	q=int(q)
	w=0
	a=input().split()
	for i in range(0,len(a)):
		if a[i].isdigit():
			w=w+1
	if w==len(a):
		l=[]
		m=[]
		for i in range(0,q):
			p=input().split()
			l.append(p)
		for i in range(0,len(l)):
			r=l[i]
			s=0
			if r[0].isdigit() and r[1].isdigit():
				for i in range(int(r[0])-1,int(r[1])):
					m.append(int(a[i]))
				for j in range(0,len(m)-1):
					xor=m[j+1]^m[j]
					m[j+1]=xor
				print(xor)
				m=[]
			else:
				continue
	else:
		print("invalid")
else:
	print("Invalid")
