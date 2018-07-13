n=input()
if(n.isdigit()):
	n=int(n)
	s=0
	a=input().split()
	l=[]
	for i in range(0,n):
		l.append(int(a[i]))
		s=s+int(a[i])
	su=0
	sum1=0
	m=0
	for i in range(0,n-1):
		avg=0
		avg1=0
		su=su+l[i]
		sum1=s-su
		avg=su/(i+1)
		avg1=sum1/(n-i-1)
		if avg==avg1:
			m=1
			print("yes")
			break
		else:
			continue
if m==0:
	print("no")
