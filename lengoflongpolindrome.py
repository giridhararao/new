i=raw_input()
l=len(i)
a=[]
b=[]
for j in range(0,l):
     a.append(i[j])
for j in a:
      if j in b:
            break
      if j not in b:
            b.append(j)
print(len(b))
