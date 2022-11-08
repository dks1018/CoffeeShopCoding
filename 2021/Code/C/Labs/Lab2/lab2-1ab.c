#include <stdio.h>
#include <stdlib.h>

int main()
{
int a; //ebp

int b = a; //esp is b
b = b - 16;

int c = 32; //memory address ebp-12
int d = 46; //memory address ebp-8
int e = 55; //memory address ebp-4
int f = c; // edx is f
int g = d; // eax is g

g = f + g;
e = e + g;

g = g + e;

printf("Print variables %d %d %d %d %d %d %d",a, b, c, d, e, f, g);


return 0;
}