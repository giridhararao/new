ia,ib=raw_input().split()
ia=int(ia)
ib=int(ib)
c=raw_input().split()
l=[]
for i in range(ia):
	l.append(int(c[i]))
w=[]
k=[]
z=[]
if ib>=3:
	print max(l)
elif ib==1:
	print min(l)
elif ib==2:
	for i in range(0,ia-1):
		w.append(min(l[0:ia-i-1]))
		k.append(min(l[ia-i-1:ia]))
	for i in range(0,ia-1):
		z.append(max(w[i],k[i]))
	print max(z)
