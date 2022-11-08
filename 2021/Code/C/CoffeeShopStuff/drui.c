#include <stdlib.h>
#include <stdio.h>
int main(){

    char name[]="";

printf("Please enter your name here:");

scanf("%s",&name);
if(strcmp(&name,"dreu")==0)
{
printf("YOU'RE A BITCH!");
}else if(strcmp(&name,"drui")==0)
    {
        printf("YOU'RE A BITCH!");
    }else
    {
        printf("You're Probably as cool as me, or you are me!");
    }
    return 0;
}