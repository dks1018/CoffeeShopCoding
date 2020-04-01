#include <stdio.h>
#include <stdlib.h>

int main()
{
int a; //ebp
int b; //esp
a = b; //mov ebp, esp
b = b - 16;

int c = 10; //memory address ebp-8
int d = 14; //memory address ebp-4
int e = c; //eax is c

if(e <= d)
{
    goto L2;

}else{
    goto L3;
}

L2:
e=2;

L3:
return 0;
}