#include <stdio.h>

int func(int num1,int num2) 
    
    {
    int num3;
    num3 = (num1 + num2) - 4;

    return(num3);
    }

int main()
{
    int num1=20;
    int num2=40;
    int result;

    result = func(num1,num2);
    printf("%d",result);
    return 0;
    }
    
    