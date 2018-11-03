def maxsum(x):
    a=0
    b=0
    o=0
    for i in x:
        c=b if(b>a) else a
        a=b+i
        b=c
    if(b>a):
        o=b
    else:
        o=a
    return(o)
        
a=int(input())
b=input().split()
c=[]
for i in range(0,a):
    c.append(int(b[i]))
d=maxsum(c)
print(d)
