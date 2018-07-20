a=input().split()
b=a[0]
c=a[1]
l=0
for i in range(0,len(b)):
	for j in range(i+1,len(b)+1):
		d=b[i:j]
		if d in c:
			if len(d)>1:
				l=l+1
if l>0:
	print("yes")
else:
	print("no")
