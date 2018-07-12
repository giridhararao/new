x,y=input().split()
if(x.isdigit() and y.isdigit()): 
              x=int(x)
              y=int(y)
              if(y==1):
                  print("1 2")
              else:
                 print("1 "+str(x-y))
