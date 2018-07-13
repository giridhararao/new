a,b=input().split()
e=[]
if(a.isdigit() and b.isdigit()):
    c=input().split()
    d=len(c)
    for i in range(d):
        x=int(c[i])
        e.append(x)
    e.sort()
    b=int(b)
    print(e[d-b])
