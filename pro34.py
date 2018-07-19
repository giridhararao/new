a,b=input().split()
a=int(a)
b=int(b)
c=[]
s='R'
y='G'
for i in range(0,a):
	d=input()
	c.append(d)
e=[]
sum=0
for i in range(0,a):
	t=c[i]
	for j in range(0,b):
		e.append(t[j])
	for j in range(0,b-1):
		if e[j]==e[j+1]:
			if e[j]==s:
				e[j]=y
				sum=sum+5
			else:
				e[j]=s
				sum=sum+3
	e=[]
print(sum)
