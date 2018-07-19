a=input()
b=len(a)
c=[]
for i in range(0,b):
	c.append(a[i])
z=ord(c[0])
k=[]
for i in range(0,b):
	if z<ord(c[i]):
		y=i
for i in range(0,b):
	if i>=y:
		k.append(c[i])
print("".join(k))
