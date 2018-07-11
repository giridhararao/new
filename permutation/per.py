def per(a):
	if len(a)==0:
		return []
	elif len(a)==1:
		return [a]
	else:
		l=[]
		for i in range(len(a)):
			x=a[i]
			xs=a[:i]+a[i+1:]
			for p in per(xs):
				l.append([x]+p)
		return(l)
a=input()
if a.isdigit():
	data=list(a)
	w=[]
	for p in per(data):
		if "".join(p) not in w:
			w.append("".join(p))
	for i in w:
		print(i)
