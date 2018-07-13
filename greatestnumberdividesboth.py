a,b=input().split()
b=int(b)
a=int(a)
c=min(a,b)
d=0
for i in range(1,c+1):
    if(a%i==0 and b%i==0):
        d=i;
print(d)
