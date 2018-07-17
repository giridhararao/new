a,b=input().split()
a=int(a)
b=int(b)
c=input().split()
d=input().split()
k=0
e=[]
f=[]
for i in range(a):
    e.append(c[i])
for i in range(b):    
    f.append(d[i])
for i in e:
    for j in f:
        if(i==j):
            k=k+1
if(k==b):
    print("YES")
else:
    print("NO")
