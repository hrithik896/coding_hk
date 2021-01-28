#include<stdio.h>

int main()

{

     long int  x,y,z;

    int n,i;

    x=0;

    y=1;

    printf("Enter the number\n");

    scanf("%d",&n);

    printf("%ld\n",y);

    for(i=1;i<n;i++)

    {

     z=x+y;

     printf("%ld\n",z);

    x=y;

    y=z; 

    }

    printf("\n");

    return 0;

}
