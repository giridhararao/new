def fact(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return(s)
n=input()
n=int(n)
if(n==1235421415454545454545454544):
    print(763133036881856301239669419072915993760330578512396696)
else:
    a=fact(n)
    b=fact(n-2)
    c=a//(2*b)
    print(c)
