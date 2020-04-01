#include <stdio.h>
#include <stdlib.h>
int func2();
int func1(int num1, int num2)
{
    //declare valriable
    int a,b,c;
    int result1 = a + b;
    int result2 = b + c;
    //call function
    func2(3,b);
return result1, result2;
}

int func2(int num3,int num4)
{
    //calculate sub eax, dword PTR [ebp+12]
    int result = num4 - num3;

return result;
}

int main() 
{
    //cal func1 push values 6 and 4
    int numVal = func1(6,4);

    return 0;
}