a=raw_input()
if a.isdigit():
	a=int(a)
	o=0
	b=raw_input().split()
	for i in range(len(b)-1):
		if ((int(b[i])>0 and int(b[i+1])<0) or (int(b[i])<0 and int(b[i+1])>0)):
			o=len(b)-i
			print o,
		else:
			print "1",
if o>0:
	print o-1
else:
	print "1"
