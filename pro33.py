a=input()
b=len(a)
c=[]
y=0
for i in range(0,b):
	c.append(a[i])
z=ord(c[0])
k=[]
for i in range(0,b):
	if z<ord(c[i]):
		y=i
		break
for i in range(y,b):
        k.append(c[i])
print("".join(k))
