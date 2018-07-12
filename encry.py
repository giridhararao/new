in1=input()
in2=input()
a=0
n=96
m=64
s=0
if(len(in1)==len(in2)):
	l=[]
	for i in range(0,len(in1)):
		if(in1[i].isdigit() or in2[i].isdigit()):
			a=a+1
	if(a==0):
		for i in range(0,len(in1)):
			h=ord(in1[i])
			r=ord(in2[i])
			if(h>96 and h<123):
				h=26+h-122
			else:
				s=s+1
				if(h>64 and h<92):
					h=27+h-91
			if(r>96 and r<123):
				r=26+r-122
			else:
				s=s+1
				if(r>64 and r<92):
					r=27+r-91
			p=r+h
			if(p>26):
				p=p-26
			if(s==0):
				p=n+p
				l.append(chr(p))
			elif(s>0):
				p=m+p
				l.append(chr(p))
		print("".join(l))
	else:
		print("Invalid")
else:
	print("Invalid")
