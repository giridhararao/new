#include<stdio.h>
main()
{
int a,b[100],i=0,j=0,k;
scanf("%d",&a);
while(a>0)
{
b[i]=a%10;
a=a/10;
i=i++;
}
for(k=0;k<i;k++)
{
j=j+(b[k]*b[k]);
}
printf("%d",j);

}
