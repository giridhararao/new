a=int(input())
b=input().split()
c=[]
d=[]
f=0
for i in range(a):
    x=int(b[i])
    c.append(x)
for i in range(a):
    for j in range(a):
        if(i!=j):
             if(c[i]==c[j]):
                 d.append(c[i])
                 f=f+1
if(f==0):
    print("unique")
else:
    e=list(set(d))
    e.sort()
    l=len(e)
    h=[]
    for i in range(l):
        h.append(str(e[i])+" ")
    p=""
    for z in h:
        p+=z
    print(p[:(len(p)-1)])
