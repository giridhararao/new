inp=int(input())
a=[]
for i in range(0,inp):
	b=input()
	a.append(b)
n=len(a)
l=[]
e=[]
for i in range(0,n-1):
	s=a[0]
	f=a[i+1]
	q=len(s)
	t=len(f)
	if q>t:
		u=t
	elif q<t:
		u=q
	elif q==t:
		u=q
	for j in range(0,u):
		if(s[j]==f[j]):
			l.append(f[j])
		else:
			break
	r=("".join(l))
	e.append(r)
	l=[]
h=len(e)
w=[]
v=[]
if(h==1):
	print(e[0])
else:
	for i in range(0,h-1):
		s=e[0]
		f=e[i+1]
		q=len(s)
		t=len(f)
		if(q>t):
			u=t
		elif(q<t):
			u=q
		elif(q==t):
			u=q
		for j in range(0,u):
			if(s[j]==f[j]):
				w.append(f[j])
			else:
				break
		r=("".join(w))
		v.append(r)
		w=[]
	print(v[0])
