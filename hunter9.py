a=int(input())
b=input().split()
c=[]
e=0
for i in range(a):
    c.append(int(b[i]))
for i in range(a):
    for j in range(a):
        if(i!=j):
            d=c[i]+c[j]
            if(d==0):
                print(str(c[i])+" "+str(c[j]))
                e=e+1
        break
if(e==0):
    print("-1 2")
