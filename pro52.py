a=input().split()
b=input().split()
c=input().split()
d=input().split()
if a[0].isdigit() and a[1].isdigit():
	if b[0].isdigit() and b[1].isdigit():
		if c[0].isdigit() and c[1].isdigit():
			if d[0].isdigit() and d[1].isdigit():
				if a[0]==b[0]:
					e=int(a[1])-int(b[1])
					e=abs(e)
				else:
					e=0
				if a[1]==d[1]:
					f=int(a[0])-int(d[0])
					f=abs(f)
				else:
					f=0
				if b[1]==c[1]:
					g=int(b[0])-int(c[0])
					g=abs(g)
				else:
					g=0
				if c[0]==d[0]:
					h=int(c[1])-int(d[1])
          h=abs(h)
				else:
					h=0
				if(e==f==g==h):
					print("yes")
				else:
					print("no")
