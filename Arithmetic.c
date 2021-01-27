#include<stdio.h>
#include<math.h>
int main()
{   
 int n,i;
 float a,d;
 printf("Enter the first number\n");
 scanf("%f",&a);
 printf("Enter the  common difference\n");
 scanf("%f",&d);
 printf("Enter the  number\n");
 scanf("%d",&n);
 for(i=1;i<=n;i++)
  {
   printf("%f\n",(a+(i-1)*d));
}
return 0;
}
