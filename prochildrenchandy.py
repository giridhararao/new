n=input()
if(n.isdigit()):
	n=int(n)
	k=input().split()
	if(len(k)==n or len(k)>n):
		l=[]
		for j in range(n):
			l.append(1)
		for i in range(0,n-1):
			if(int(k[i+1])>int(k[i])):
				l[i+1]=l[i+1]+l[i]
		print(sum(l))
