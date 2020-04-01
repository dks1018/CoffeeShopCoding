#include <stdlib.h>
#include <stdio.h>

int divideTwoNumber(float x,float y)
{
float result = x / y;

return result;
}


int main()
{
    char string[]="";
    scanf("%s", &string);
    char stringText[] = "Enter your values to be divded: \n";
    float result = scanf("%d %d",divideTwoNumber(8,9));

    printf("This is practice for funtions %.2f\n", result);
    printf("%s", stringText);

    return 0;
}