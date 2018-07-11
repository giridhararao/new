i=input()
b=[]
c=[]
for j in range(0,len(i)):
      b.append(i[j])
for j in b:
     if j not in c:
           c.append(j)
print("".join(c))
