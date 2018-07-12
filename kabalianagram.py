ka=['k','a','b','a','l','i']
u=list(set(ka))
x=int(input())
c=[]
count=0
for i in range(0,x):
	b=input()
	c.append(b)
for i in range(0,x):
	n=[]
	g=len(c[i])
	w=c[i]
	f=0
	for j in range(0,g):
		if(w[j] in ka):
			n.append(w[j])
	m=list(set(n))
	if(len(m)==len(u)):
		for k in range(0,len(m)):
			if(m[k] in u):
				f=f+1
			if(f==len(u)):
				count=count+1
print(count)
