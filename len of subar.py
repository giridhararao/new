def maxim(a,b):
    x=1
    y=1
    for i in range(1,b):
        if(a[i]>a[i-1]):
            x=x+1
        else:
            if(y<x):
                y=x
            x=1
    if(y<x):
        y=x
    return(y)
a=int(input())
b=input().split()
c=[]
for i in range(0,a):
    c.append(int(b[i]))
d=maxim(c,a)
print(d)
