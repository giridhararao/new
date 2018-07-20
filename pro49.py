a=input()
b=input()
i=1
e=len(a)
f=len(b)
if(e>f):
        g=f
        h=b
        j=a
else:
        g=e
        h=a
        j=b
while i<g:
	d=h*i
	if d==j:
		print(i)
	i=i+1
