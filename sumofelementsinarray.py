a=int(input())
b=input().split()
c=[]
d=0
for i in range(a):
    x=int(b[i])
    c.append(x)
for i in c:
    d=d+i
if(d==0):
    c.sort()
    print(c[a-1])
else:
    print(d)
