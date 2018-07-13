a=int(input())
g=input().split()
b=[]
c=[]
f=0
for d in range(a):
   x=int(g[d])
   b.append(x)
b.sort()
for e in range(a):
   f=f+(b[e]*(10**e))
print(f)
