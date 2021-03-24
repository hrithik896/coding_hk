// Program to find Even and odd numbers in an array
#include<stdio.h>
#define SIZE 5
int main()
{
    int arr[SIZE],i,Even=0, Odd=0;
    for(i=0; i<SIZE; i++)
    {
        printf("Enter the value for arr[%d]",i);
        scanf("%d",&arr[i]);
        if(arr[i]%2==0)
            Even++;
        else
            Odd++;
    }
    printf("Even no. =%d,Odd no.=%d",Even,Odd);
    return 0;
}
