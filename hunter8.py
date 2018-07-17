a=int(input())
b=input().split()
c=[]
for i in range(a):
    c.append(int(b[i]))
for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1,a):
            d=c[i]+c[j]
            if(d==c[k]):
                print(str(c[i])+" "+str(c[j])+" "+str(c[k]))
