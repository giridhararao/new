i=raw_input().split()
f=len(i)
for j in range(0,f):
	k=i[j]
	l=[]
	for j in range(1,len(k)):
		l.append(k[-j])
	l.append(k[0])
	print "".join(l),
