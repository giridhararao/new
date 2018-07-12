a,b=input().split()
b=int(b)
la=len(a)
d=[]
for i in range(0,la):
         s=a[i]
         d.append(s)
z=[]
for i in range(b,la):
         s=d[i]
         z.append(s)
z.sort()
print("".join(z))
