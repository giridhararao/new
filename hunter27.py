n=input()
k=[]
for i in range(0,len(n)):
	k.append(n[i])
c="".join(k[::-1])
if n!=c:
	print(n)
elif n==c:
	z=[]
	for i in range(0,len(n)-1):
		z.append(k[i])
	print("".join(z))
