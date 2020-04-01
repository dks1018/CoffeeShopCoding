#include <stdio.h>
#include <stdlib.h>

int funciton1()
{
int a; //ebp
int b; //esp
a = b; //mov ebp, esp
b = b - 24;

//memory address ebp-8
int *ebpPTR, c;//LEA move value into memory address
c = 7;
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