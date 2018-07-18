a=int(input())
b=input().split()
c=len(b)
e=0
d=[]
f=0
for i in range(c):
        d.append(int(b[i]))
for i in d:
        if(i>0):
                e=e+i
                f=f+1
if(f==0):
    d.sort()
    print(d[c-1])
else:
    print(e)
