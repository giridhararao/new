a=input()
b=[]
for i in range(0,len(a)):
	b.append(a[i])
c="".join(b[::-1])
if a!=c:
	print(a)
elif a==c:
	z=[]
	for i in range(0,len(a)-1):
		z.append(b[i])
	print("".join(z))
