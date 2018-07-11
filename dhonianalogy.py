g=raw_input()
if len(g)<100000:
     c=['d','h','o','n','i']
     m=[]
     for i in range(0,len(g)):
              m.append(a[i])
     res=[]
     if len(m)==len(c):
        for i in m:
               if i in c:
                     if i not in res:
                             res.append(i)
        if len(res)==len(c):
              print("yes")
        else:
             peint("no")
     else:
        print("no")
else:
   print("Invalid")
