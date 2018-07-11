i=input()
b=[]
c=[]
for j in range(0,len(i)):
      b.append(i[j])
e=[]
for j in b:
     if j not in e:
           e.append(j)
print("".join(e))
